import os
import time
from google import genai
from rich.console import Console
from rich.panel import Panel

# Initialize our tools
client = genai.Client()
console = Console()

target_folder = "C:/Users/Atharv/Documents/Codes/Summer_Assignment_25112CN382/Week-5/Day-30"
all_files = os.listdir(target_folder)

console.print("[bold green]Starting AI Code Auditor Engine...[/bold green]\n")

for file_name in all_files:
    if file_name.endswith(".cpp"):
        full_path = os.path.join(target_folder, file_name)

        with open(full_path, "r") as f:
            raw_code = f.read()

        console.print(f"[yellow]Auditing {file_name}...[/yellow]")

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"File: {file_name}\nCode:\n{raw_code}",
            config=genai.types.GenerateContentConfig(
                system_instruction="Analyze the given C++ code. Highlight memory leaks, unused tracking components, or structural optimizations. Keep your points concise. Do not use markdown header symbols (# or ##) or bold markdown (**) in your raw text."
            ),
        )

        # Render the AI text response inside a beautiful, framed UI Panel
        console.print(Panel(response.text, title=f"Audit Report: {file_name}", border_style="cyan"))
        print("\n")

        # The Pacer Check: Pause for 3 seconds to keep us safely below the 20 Requests Per Minute limit
        time.sleep(3)

console.print("[bold green]All files successfully audited and finalized![/bold green]")