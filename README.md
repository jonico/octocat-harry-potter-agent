# Harry Potter / Octocats Example Agent

This project demonstrates how to use the `fast-agent` framework to connect to the Octocat Harry Potter MCP server.

## Getting Started

### Prerequisites
- Python 3.10+
- [`uv`](https://github.com/astral-sh/uv) (recommended for fast Python package management)


### Installation
1. Clone this repository or copy the files to your local machine.
2. Install the `fast-agent-mcp` package using `uv`:

```bash
# create and activate a python environment
uv venv
source .venv/bin/activate
# install the fast-agent-mcp package
uv pip install fast-agent-mcp
```


### Configuration
Before running the example, you need to adjust the Octocat HP MCP server settings in the `fastagent.config.yaml` file. Make sure the server address and credentials match your local or remote MCP server setup. Furthermore, you would need to set API keys for the model you are using in the `fastagent.secrets.yaml` file. You can use the example file `fastagent.secrets.yaml.example` as a template.


### Running the Example

Run the agent using `uv` (recommended):

```bash
uv run harry-potter-octocat.py --model  openai.gpt-4o
```

Or start an interactive session with fast-agent and point to any MCP server:

```bash
uv run fast-agent go --url http://localhost:9000/sse --model sonnet35
```

## Project Structure
- `harry-potter-octocat.py`: Main script to run the agent
- `fastagent.config.yaml`, `fastagent.secrets.yaml`, `fastagent.jsonl`: Configuration and secrets for the agent

## License
MIT (or specify your license here)
