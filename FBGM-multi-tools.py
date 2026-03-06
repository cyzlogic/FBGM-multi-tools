import os
import requests
import time
import random
import string
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.text import Text
from rich.progress import track, Progress # <-- FIXED IMPORT

# intilaztion
console = Console()

# header
def print_header():
    """Prints the new, even more fucking edgy header."""
    
    logo = """
      ________  _______    ______   __       __     
|        \|       \  /      \ |  \     /  \    
| $$$$$$$$| $$$$$$$\|  $$$$$$\| $$\   /  $$    
| $$__    | $$__/ $$| $$ __\$$| $$$\ /  $$$    
| $$  \   | $$    $$| $$|    \| $$$$\  $$$$    
| $$$$$   | $$$$$$$\| $$ \$$$$| $$\$$ $$ $$    
| $$      | $$__/ $$| $$__| $$| $$ \$$$| $$ __ 
| $$      | $$    $$ \$$    $$| $$  \$ | $$    
 \$$       \$$$$$$$   \$$$$$$  \$$      \$$    
    """
    
    header_text = Text("\nFBGM Toolkit", justify="center", style="bold red")
    logo_text = Text(logo, justify="center", style="bold yellow")
    
    console.print(Panel(Align.center(logo_text + header_text), border_style="bold magenta", title="[dim]Fuck Bitches, Get Money[/dim]"))

# --- OSINt functions
def search_local_breach_file(filepath, term):
    """Searches a local breach file. You know what this does by now."""
    if not os.path.exists(filepath):
        console.print(f"\n[bold red]ERROR:[/bold red] The file '{filepath}' doesn't fucking exist. Are you stupid?")
        return

    console.print(f"\n[cyan]Cracking open '{os.path.basename(filepath)}'...[/cyan]")
    found_lines = []
    
    try:
        total_lines = sum(1 for line in open(filepath, 'r', encoding='utf-8', errors='ignore'))
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in track(f, total=total_lines, description="[bold green]Digging through the filth...[/bold green]"):
                if term in line:
                    found_lines.append(line.strip())

        if found_lines:
            console.print(f"\n[bold red]PAYDIRT! Found [yellow]{term}[/yellow] in this shitpile:[/bold red]")
            for item in found_lines:
                console.print(f"  - [dim]{item}[/dim]")
        else:
            console.print(f"\n[bold green]Nothing found for '{term}' in this file. Lucky bastard.[/bold green]")

    except Exception as e:
        console.print(f"\n[bold red]Some shit went wrong reading the file:[/bold red] {e}")

# --- lwk discord funcs
def webhook_spammer():
    """Floods a Discord webhook with messages. For educational purposes, my ass."""
    console.print(Panel("[bold red]Webhook Annihilator[/bold red]", subtitle="[dim]Time to make someone's channel unusable.[/dim]"))
    webhook_url = Prompt.ask("[cyan]Paste the victim's Webhook URL[/cyan]")
    message = Prompt.ask("[cyan]What shitty message do you want to spam?[/cyan]")
    try:
        amount = int(Prompt.ask("[cyan]How many times should I send it?[/cyan]"))
    except ValueError:
        console.print("[bold red]That's not a fucking number. Try again.[/bold red]")
        return

    payload = {'content': message}
    
    console.print(f"\n[yellow]Alright, starting the fucking raid. Sending '{message}' {amount} times...[/yellow]")
    
    for _ in track(range(amount), description="[bold red]DEPLOYING SPAM...[/bold red]"):
        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code not in [200, 204]:
                console.print(f"\n[yellow]Warning:[/yellow] Got a weird status code {response.status_code}. They might be rate-limiting or the hook is dead.")
                time.sleep(1) 
            time.sleep(0.1)
        except requests.exceptions.RequestException as e:
            console.print(f"\n[bold red]ERROR:[/bold red] The webhook URL is fucked or you're not connected to the internet, dumbass. ({e})")
            return
            
    console.print(f"\n[bold green]Raid complete. {amount} messages sent. Hope you fucked their server up.[/bold green]")


# --- USERNAME tools
def generate_usernames():
    """Generates 'rare' usernames that might bypass some gay filters."""
    console.print(Panel("[bold cyan]Username Snatcher[/bold cyan]", subtitle="[dim]Find a name that isn't already taken by some 12-year-old.[/dim]"))
    
    rare_users = [
        "israeli", "sexyjews", "holocaust", "nigger", "faggot", "tranny",
        "kys", "retard", "autism", "bomb", "terror", "jihad", "isis", "alqaeda",
        "hitler", "nazi", "gaschamber", "slave", "coon", "beastiality", "incest"
    ]
    bypasses = ['.', '_', 'x', 'xx', 'z', 'zz']

    console.print("\n[bold]What kind of username you want?[/bold]")
    choice = Prompt.ask("Choose one", choices=["3l", "4l", "rare"], default="rare")
    
    try:
        amount = int(Prompt.ask("[cyan]How many you wanna generate?[/cyan]"))
    except ValueError:
        console.print("[bold red]That's not a fucking number.[/bold red]")
        return
        
    generated = set()
    
    console.print(f"\n[yellow]Generating {amount} {choice} usernames...[/yellow]")
    console.print("[dim]Disclaimer: No guarantee these shits are available. This just generates them.[/dim]")
    
    # --- THIS IS THE FUCKING FIX ---
    with Progress(transient=True) as progress:
        task = progress.add_task("[bold green]Cooking up some names...[/bold green]", total=amount)
        while len(generated) < amount:
            user = ""
            if choice == '3l':
                user = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
            elif choice == '4l':
                user = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
            elif choice == 'rare':
                base = random.choice(rare_users)
                bypass_char = random.choice(bypasses)
                if random.random() > 0.5:
                    pos = random.randint(1, len(base) - 1)
                    user = base[:pos] + bypass_char + base[pos:]
                else:
                    user = base.replace(random.choice(base), random.choice(bypasses), 1)
            
            if user and user not in generated:
                generated.add(user)
                progress.update(task, advance=1)
    # --- END OF FIX ---

    console.print(Panel("[bold green]Here's your fucking list:[/bold green]", expand=False))
    for user in sorted(list(generated)):
        console.print(f"  - {user}")


# --- MENUS ---
def osint_menu():
    console.print("\n--- [bold yellow]OSINT Tools[/bold yellow] ---")
    filepath = Prompt.ask("[cyan]Enter the full path to the breach file[/cyan]")
    search_term = Prompt.ask("[cyan]Who we lookin' for? (email/username)[/cyan]")
    search_local_breach_file(filepath, search_term)

def discord_menu():
    console.print("\n--- [bold yellow]Discord Tools[/bold yellow] ---")
    webhook_spammer()
    
def user_tools_menu():
    console.print("\n--- [bold yellow]User Tools[/bold yellow] ---")
    generate_usernames()

# --- MAIN LOOP ---
def main():
    while True:
        print_header()
        console.print(Panel("[bold](1)[/bold] OSINT Tools      [bold](2)[/bold] Discord Tools      [bold](3)[/bold] User Tools", 
                          title="[bold]Main Menu[/bold]", subtitle="[dim]Choose your poison. ('q' to quit)[/dim]"))

        choice = Prompt.ask("\nSelect a category", choices=["1", "2", "3", "q"], default="q")

        if choice == '1':
            osint_menu()
        elif choice == '2':
            discord_menu()
        elif choice == '3':
            user_tools_menu()
        elif choice == 'q':
            console.print("\n[bold magenta]Aight, get the fuck out then.[/bold magenta]")
            break
        
        Prompt.ask("\n[dim]Press Enter to return to the main menu...[/dim]")
        console.clear()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold red]Caught you trying to quit with Ctrl+C. Bye, pussy.[/bold red]")
