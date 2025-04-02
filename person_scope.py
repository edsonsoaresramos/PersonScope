import argparse
import urllib.parse
import webbrowser
import json
from datetime import datetime
from pathlib import Path
from rich.console import Console
from banner import show_banner
from helptext import show_help

console = Console()

def build_dorks(name=None, username=None):
    dorks = {}
    if name:
        dorks.update({
            "Emails": f'"{name}" "@gmail.com" OR "@yahoo.com" OR "@outlook.com"',
            "Leaked Emails": f'"{name}" site:pastebin.com OR site:throwbin.io OR site:breachforums.st',
            "Phone Numbers": f'"{name}" "phone" "contact" "mobile" "WhatsApp"',
            "GitHub Email": f'site:github.com "{name}" "gmail.com"',
            "Social Media Accounts": f'"{name}" site:linkedin.com OR site:facebook.com OR site:twitter.com OR site:instagram.com',
            "Facebook Public": f'site:facebook.com/public/ "{name}"',
            "Instagram": f'site:instagram.com "{name}"',
            "Forums": f'"{name}" site:reddit.com OR site:quora.com OR site:stackoverflow.com',
            "Blogs": f'"{name}" site:medium.com OR site:blogspot.com OR site:wordpress.com',
            "Amazon Wishlist": f'"{name}" site:amazon.com "wishlist"',
            "News Mentions": f'"{name}" site:nytimes.com OR site:bbc.com OR site:cnn.com',
            "Resume/CV": f'"{name}" filetype:pdf OR filetype:doc "resume" OR "curriculum vitae"',
            "LinkedIn Employment": f'site:linkedin.com/in "{name}"',
            "Past Job Applications": f'"{name}" site:indeed.com OR site:glassdoor.com',
            "Social Profiles": f'site:facebook.com OR site:twitter.com OR site:instagram.com "{name}"',
            "Facebook by Location": f'site:facebook.com "{name}" "New York"',
            "Photos": f'"{name}" site:flickr.com OR site:500px.com OR site:pinterest.com',
        })
    if username:
        dorks.update({
            "GitHub/Reddit Username": f'site:github.com OR site:reddit.com "username:{username}"',
            "Deep Search Profile": f'inurl:profile "{username}"',
        })
    return dorks

def open_queries_in_browser(dorks, engines, verbose=False):
    engine_urls = {
        "google": "https://www.google.com/search?q=",
        "duckduckgo": "https://duckduckgo.com/?q=",
        "brave": "https://search.brave.com/search?q="
    }
    for engine in engines:
        base_url = engine_urls.get(engine)
        if not base_url:
            continue
        for label, query in dorks.items():
            search_url = base_url + urllib.parse.quote(query)
            if verbose:
                console.print(f"[bold cyan]Opening ({engine}):[/bold cyan] [yellow]{label}[/yellow] → [green]{query}[/green]")
            webbrowser.open_new_tab(search_url)

def save_output(dorks, output_name):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_base = Path(f"{output_name}_{now}")
    with open(output_base.with_suffix(".txt"), 'w', encoding='utf-8') as f_txt:
        for label, query in dorks.items():
            f_txt.write(f"{label}:
{query}

")
    with open(output_base.with_suffix(".json"), 'w', encoding='utf-8') as f_json:
        json.dump(dorks, f_json, indent=4)
    console.print(f"\n[bold green]Saved TXT:[/bold green] {output_base}.txt")
    console.print(f"[bold green]Saved JSON:[/bold green] {output_base}.json")

def main():
    show_banner()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-n", "--name", type=str)
    parser.add_argument("-u", "--username", type=str)
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-g", "--google", action="store_true")
    parser.add_argument("-d", "--duckduckgo", action="store_true")
    parser.add_argument("-b", "--brave", action="store_true")
    parser.add_argument("-a", "--all", action="store_true")
    parser.add_argument("-h", "--help", action="store_true")
    args = parser.parse_args()

    if args.help:
        show_help()
        return

    if not args.name and not args.username:
        console.print("[bold red]Error:[/bold red] You must provide --name and/or --username")
        show_help()
        return

    engines = []
    if args.all:
        engines = ["google", "duckduckgo", "brave"]
    else:
        if args.google:
            engines.append("google")
        if args.duckduckgo:
            engines.append("duckduckgo")
        if args.brave:
            engines.append("brave")

    if not engines:
        console.print("[bold red]Error:[/bold red] You must specify at least one search engine: -g, -d, -b or -a")
        show_help()
        return

    dorks = build_dorks(args.name, args.username)
    open_queries_in_browser(dorks, engines, verbose=args.verbose)
    if args.output:
        save_output(dorks, args.output)

if __name__ == "__main__":
    main()
