import asyncio
import uuid
from openai.types.responses import ResponseContentPartDoneEvent, ResponseTextDeltaEvent
from agents import Agent, RawResponsesStreamEvent, Runner, TResponseInputItem, trace, OpenAIChatCompletionsModel, AsyncOpenAI

gemini_api_key = "api-key-here"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

french_agent = Agent(
    name="french_agent",
    instructions="You only speak French",
    model=OpenAIChatCompletionsModel(model="gemini-pro", openai_client=client)
)

spanish_agent = Agent(
    name="spanish_agent",
    instructions="You only speak Spanish",
    model=OpenAIChatCompletionsModel(model="gemini-pro", openai_client=client)
)

english_agent = Agent(
    name="english_agent",
    instructions="You only speak English",
    model=OpenAIChatCompletionsModel(model="gemini-pro", openai_client=client)
)

triage_agent = Agent(
    name="triage_agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[french_agent, spanish_agent, english_agent],
    model=OpenAIChatCompletionsModel(model="gemini-pro", openai_client=client)
)


async def main():
    conversation_id = str(uuid.uuid4().hex[:16])

    msg = input("Hi! We speak French, Spanish and English. How can I help? ")
    agent = triage_agent
    inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]

    while True:
        with trace("Routing example", group_id=conversation_id):
            result = Runner.run_streamed(
                agent,
                input=inputs,
            )
            async for event in result.stream_events():
                if not isinstance(event, RawResponsesStreamEvent):
                    continue
                data = event.data
                if isinstance(data, ResponseTextDeltaEvent):
                    print(data.delta, end="", flush=True)
                elif isinstance(data, ResponseContentPartDoneEvent):
                    print("\n")

        inputs = result.to_input_list()
        print("\n")

        user_msg = input("Enter a message: ")
        inputs.append({"content": user_msg, "role": "user"})
        agent = result.current_agent


if __name__ == "__main__":
    asyncio.run(main())