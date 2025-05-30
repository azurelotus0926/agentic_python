from agentic.tools.weather_tool import WeatherTool

from agentic.common import Agent, AgentRunner
from agentic.models import GPT_4O_MINI, LMSTUDIO_QWEN
# This is the "hello world" agent example. A simple agent with a tool for getting weather reports.

MODEL=GPT_4O_MINI # try locally with LMSTUDIO_QWEN

agent = Agent(
    name="Basic Agent",
    welcome="I am a simple agent here to help answer your weather questions.",
    instructions="You are a helpful assistant.",
    model=MODEL,
    tools=[WeatherTool()],
    prompts = {
        "NYC": "What is the weather in New York City?",
        "LA": "What is the weather in Los Angeles?",
    }
)

if __name__ == "__main__":
    AgentRunner(agent).repl_loop()
