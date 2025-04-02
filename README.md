# PersonScope

**PersonScope** is a command-line tool designed for ethical OSINT (Open Source Intelligence).  
It generates advanced search queries ("Google Dorks") based on a person's name or username  
and opens them in your browser using multiple search engines like Google, DuckDuckGo, and Brave.

---

## ⚠️ Disclaimer

> This tool is intended strictly for **educational and ethical** use.  
> The author is not responsible for any misuse. Always respect privacy and legal boundaries.

---

## 🚀 Features

- Supports multiple search engines: Google, DuckDuckGo, Brave
- Smart dork queries based on name or username
- Colorful output using [Rich](https://github.com/Textualize/rich)
- Save results as `.txt` and `.json`
- Verbose and modular CLI tool

---

## 📦 Installation

### Basic

```bash
git clone https://github.com/yourusername/personscope.git
cd personscope
pip install -r requirements.txt

---

Recommended (with virtual environment)
python3 -m venv venv
source venv/bin/activate      # On Linux/macOS/WSL
# .\\venv\\Scripts\\activate  # On Windows

pip install .

---

🧑💻 Usage
Examples:
# Google search for a name
personscope -n "John Doe" -g

# DuckDuckGo search for a username
personscope -u johnd123 -d

# All engines, with output saved and verbose
personscope -n "John Doe" -u johnd123 -a -o output_file -v


---


Flags:
Option	Description
-n	    Person's full name
-u	    Username to search
-o	    Output file base name (.txt, .json)
-v	    Verbose output
-g	    Use Google search
-d	    Use DuckDuckGo search
-b	    Use Brave search
-a	    Use all supported search engines
-h	    Show help and usage examples

---


🖥️ Platform Support

    ✅ Linux (tested)

    ✅ macOS

    ✅ Windows

    ✅ WSL (If browser doesn't open, try installing wslu and using wslview)

---

⚠️ WSL Users: tcgetpgrp failed: Not a tty message
If you're running PersonScope on WSL (Windows Subsystem for Linux), you might see the following message in your terminal after running a search:
    tcgetpgrp failed: Not a tty

This is not an error, and it does not affect the tool's functionality. It's a harmless system message related to how WSL handles terminal sessions when opening multiple browser tabs.
💡 Want to hide it?

There are two simple ways:

1. Redirect the error output when running the command:
personscope -n "John Doe" -g 2>/dev/null

2. Create a shell alias to always hide the message:

Add this line to your ~/.bashrc (or ~/.zshrc if using Zsh):
alias personscope='personscope "$@" 2>/dev/null'

Then reload your shell with:
source ~/.bashrc
# or
source ~/.zshrc

This will make the message disappear automatically every time you use the tool.

---

👨💻 Author

Created with passion by **Dudditz**  
Senior Software Engineer | Ethical Hacker | OSINT Enthusiast  
Crafting clean tools with purpose, ethics, and style.

Feel free to connect: [GitHub](https://github.com/edsonsoaresramos)
