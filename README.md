# Harry Potter / Octocats Example Agent

[fast-agent](https://fast-agent.ai) based example agent to connect to the [Octocat Harry Potter MCP server](https://github.com/jonico/octocat-harry-potter-mcp-server) and [advanced MCP server](https://github.com/jonico/typescript-anthropic-tool-use-example/).

<img width="1791" alt="image" src="https://github.com/user-attachments/assets/9279d543-27d4-4fde-a9aa-60ff3aa3e532" />


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

### Example output

### Harry Potter Characters Meet Octocats 🧙‍♂️🐱

## 1. Harry Potter - Heroic Octocat
| Harry Potter | Sentrytocat |
|--------------|--------------|
| <img src="https://ik.imagekit.io/hpapi/harry.jpg" alt="Harry Potter" width="100" height="100"> | <img src="https://octodex.github.com/images/Sentrytocat_octodx.jpg" alt="Heroic Octocat" width="100" height="100"> |
- **Traits Matched**: Brave, protective, stands against adversity
- **Octocat Reasoning**: The Sentrytocat embodies Harry's guardianship and courage

## 2. Hermione Granger - Professortocat
| Hermione Granger | Professortocat |
|------------------|----------------|
| <img src="https://ik.imagekit.io/hpapi/hermione.jpeg" alt="Hermione Granger" width="100" height="100"> | <img src="https://octodex.github.com/images/Professortocat_v2.png" alt="Professortocat" width="100" height="100"> |
- **Traits Matched**: Intelligent, studious, always prepared
- **Octocat Reasoning**: Reflects Hermione's academic brilliance and love of learning

## 3. Ron Weasley - Welcometocat
| Ron Weasley | Welcometocat |
|-------------|--------------|
| <img src="https://ik.imagekit.io/hpapi/ron.jpg" alt="Ron Weasley" width="100" height="100"> | <img src="https://octodex.github.com/images/welcometocat.png" alt="Welcometocat" width="100" height="100"> |
- **Traits Matched**: Loyal, friendly, warm-hearted
- **Octocat Reasoning**: Represents Ron's welcoming nature and importance of friendship

## 4. Draco Malfoy - Stormtroopocat
| Draco Malfoy | Stormtroopocat |
|--------------|----------------|
| <img src="https://ik.imagekit.io/hpapi/draco.jpg" alt="Draco Malfoy" width="100" height="100"> | <img src="https://octodex.github.com/images/stormtroopocat.png" alt="Stormtroopocat" width="100" height="100"> |
- **Traits Matched**: Stern, uniformed, follows a strict code
- **Octocat Reasoning**: Symbolizes Draco's rigid upbringing and conformity to Slytherin expectations

## 5. Minerva McGonagall - Justicetocat
| Minerva McGonagall | Justicetocat |
|--------------------|--------------|
| ![Minerva McGonagall](https://ik.imagekit.io/hpapi/mcgonagall.jpg) | ![Justicetocat](https://octodex.github.com/images/justicetocat.jpg) |
- **Traits Matched**: Disciplined, fair, protective of students
- **Octocat Reasoning**: Embodies McGonagall's strong sense of justice and principled leadership

*Magical matches brought to you by the intersection of wizardry and git magic! 🧙‍♀️🐱*
