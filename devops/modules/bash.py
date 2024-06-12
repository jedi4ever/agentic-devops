import click
import os
from modules.utils import run_aider_command

def create_bash_script():
    click.echo("\n🚀 Creating Bash Script...")
    instructions = click.prompt("Provide Bash script creation instructions", default="Create a basic deployment script.")
    guidance = click.prompt("Provide any initial optional guidance for the AI (press Enter to skip)", default="", show_default=False)
    if guidance:
        instructions = f"{guidance}. {instructions}"
    
    # Ensure the output directory exists
    output_dir = "./output/bash/"
    os.makedirs(output_dir, exist_ok=True)
    
    script_path = os.path.join(output_dir, "script.sh")
    run_aider_command(instructions, [script_path])
    click.echo("✅ Bash Script created successfully.")
    
    import coder
    coder.coder_menu(coder.main_menu)  # Call the coder menu again
