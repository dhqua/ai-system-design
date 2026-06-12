import sys
import anthropic
from rich.markdown import Markdown
from rich.console import Console

# Read in code snippet from standard input
code = sys.stdin.read()

client = anthropic.Anthropic()

#Send prompt and code snippet to claude api
message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": f"Please review the following code for bugs, syntax errors, and potential improvements {code}",
        }
    ],
)

# Format the resulting markdown and print to the terminal
formatted_markdown = message.content[0].text
console = Console()
console.print(Markdown(formatted_markdown))