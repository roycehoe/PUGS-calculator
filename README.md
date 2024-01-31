# Introduction

Thanks everyone for coming for my talk. Here is the example I used; feel free to fork and play around with this repo.

# Further Readings

Here are some useful links about using the python debugger:

1. [Official pdb documentation](https://docs.python.org/3/library/pdb.html)
2. [pdb cheatsheet](https://kapeli.com/cheat_sheets/Python_Debugger.docset/Contents/Resources/Documents/index)
3. [ipdb](https://github.com/gotcha/ipdb) - pdb, but with better tab completion, syntax highlighting, tracebacks, and introspection
4. [VSCode python debugger documentation](https://code.visualstudio.com/docs/python/debugging)
5. [PUGS Presentation slides](https://docs.google.com/presentation/d/14K1Ryc3B9cYhhQndv4UB-Y4t_9HQMUZc22LtB-Sp5xY/edit?usp=sharing)

# Calculator App Setup Instructions

- Run `python main.py` on your terminal

# Web Server Setup Instructions

- Install [poetry](https://python-poetry.org/docs/1.3#installing-with-the-official-installer) on your machine
- Install all project dependencies by running `poetry install`
- Activate the project virtual environment by running the command `poetry shell`
- Run the web server with the debugger by opening vscode and pressing `F5`
- Alternatively, to run the web server without the debugger, run the command `uvicorn api:app --reload` on your terminal

The server should now be running on `localhost:8000`

Optional: To view the Swagger UI of this application, you may visit `localhost:8000/docs` on your web browser.
