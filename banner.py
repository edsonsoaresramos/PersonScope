        from rich.console import Console
        from rich.text import Text
        from dudditz_ascii import print_dudditz_ascii

        def show_banner():
            console = Console()
            banner_text = Text("""
██████╗ ███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝█████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║███████╗██║     ██║   ██║██████╔╝█████╗  
██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝  
██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║███████║╚██████╗╚██████╔╝██║     ███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝
""", style="bold yellow")
            console.print(banner_text)
            console.print("[cyan]Welcome to PersonScope[/cyan] — [green]For ethical and educational use only[/green]\n")
            print_dudditz_ascii()
