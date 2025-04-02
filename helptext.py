from rich.console import Console
from rich.markdown import Markdown

def show_help():
    console = Console()
    md = Markdown("""
    # PersonScope

    **Usage examples:**

    - `python person_scope.py -n "John Doe" -g`
    - `python person_scope.py -u dudditz -d`
    - `python person_scope.py -n "John Doe" -u dudditz -b -v`
    - `python person_scope.py -n "John Doe" -a -o output_file`

    **Options:**

    - `-n`, `--name`:         Person's full name (e.g., "John Doe")
    - `-u`, `--username`:     Username to search
    - `-o`, `--output`:       Base name for output files (.txt and .json)
    - `-v`, `--verbose`:      Show built queries in console
    - `-g`, `--google`:       Use Google search engine
    - `-d`, `--duckduckgo`:   Use DuckDuckGo search engine
    - `-b`, `--brave`:        Use Brave search engine
    - `-a`, `--all`:          Use all supported search engines (Google, DuckDuckGo, Brave)
    - `-h`, `--help`:         Show help and usage examples
    """)
    console.print(md)
