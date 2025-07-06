import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Harry Potter Octocat Example")

@fast.agent(
  instruction="Can you match the top 5 Harry Potter Characters with Octocats based on their characteristics",
  # servers=["octocat-hp-mcp-server-local"]
  servers=["octocat-hp-mcp-server-heroku", "advanced-postman-mcp-heroku"],
)
async def main():
  async with fast.run() as agent:
    await agent()

if __name__ == "__main__":
    asyncio.run(main())