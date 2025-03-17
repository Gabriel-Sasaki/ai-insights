from langchain.agents import AgentExecutor

class SQLAgentExecutor(AgentExecutor):
    """Agent executor for SQL queries.
    
    This executor is responsible for validating and executing SQL queries.
    
    Methods:
        _validate_output: Validate the output of the agent.
    """
    def _validate_output(self, output: str):
        prohibited_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "CREATE"]
        if any(keyword in output.upper() for keyword in prohibited_keywords):
            raise ValueError("Agent cannot execute a query with prohibited keywords")
        return output
