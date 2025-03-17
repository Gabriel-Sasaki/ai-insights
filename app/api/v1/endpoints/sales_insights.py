from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage

from app.db.session import get_db
from app.ai.prompts import SQL_QUERY_PROMPT
from app.ai.models import AgentExecutor
from app.schemas.sales_insights import SalesInsightsResponse

router = APIRouter()

@router.get("/sales-insights")
async def get_sales_insights(
    question: str,
    db: Session = Depends(get_db)
) -> SalesInsightsResponse:
    """Get sales insights for a given question."""
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    engine = db.get_bind()
    database = SQLDatabase(engine=engine)
    toolkit = SQLDatabaseToolkit(db=database, llm=llm)
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage(content=SQL_QUERY_PROMPT),
        HumanMessage(content=question),
        MessagesPlaceholder("agent_scratchpad"),
    ])
    agent = create_openai_tools_agent(
        llm=llm,
        tools=toolkit.get_tools(),
        prompt=prompt_template
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=toolkit.get_tools(),
        handle_parsing_errors=True
    )
    response = agent_executor.invoke({
        "input": question
    })
    return SalesInsightsResponse(aiAnswer=response["output"])
