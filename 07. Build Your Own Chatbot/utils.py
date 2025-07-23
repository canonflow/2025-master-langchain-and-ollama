from typing import Any
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

SQLITE_FILE_NAME = "messages_history.db"


def get_session_history(session_id: str) -> SQLChatMessageHistory:
    return SQLChatMessageHistory(
        session_id=session_id,
        connection_string=f"sqlite:///{SQLITE_FILE_NAME}",
        table_name="chatbot_message_store"
    )


def chat_with_llm(chain: RunnableWithMessageHistory, session_id: str, input: str) -> Any:
    # output = chain.invoke(
    #     {
    #         "input": input
    #     },
    #     config={
    #         "configurable": {
    #             "session_id": session_id
    #         }
    #     }
    # )

    for output in chain.stream(
        {
            "input": input
        },
        config={
            "configurable": {
                "session_id": session_id,
            }
        }
    ):
        yield output
