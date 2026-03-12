import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
# FIX: Import the native Ollama client, NOT the OpenAI one
from autogen_ext.models.ollama import OllamaChatCompletionClient

# 1. The Native Configuration
# No "base_url" or "api_key" hack needed anymore.
model_client = OllamaChatCompletionClient(
    model="phi3",
    # auto-detects localhost:11434
)

# 2. The Main Workflow
async def main():
    agent = AssistantAgent(
        name="Architect",
        model_client=model_client,
        system_message="You are a senior Enterprise Architect. Answer in 3 bullet points."
    )

    print("🚀 Connecting to Native Ollama (Phi-3)...")
    await Console(agent.run_stream(task="Explain the difference between Monolithic and Microservices."))

if __name__ == "__main__":
    asyncio.run(main())