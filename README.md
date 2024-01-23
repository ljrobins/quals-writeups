Installation Guide
==================

Dependencies:

- Python 3.9+ (install a newer version [here](https://www.python.org/downloads/) if `python3 --version` in the command line returns a version earlier than 3.9)
- [Pandoc](https://pandoc.org/installing.html)
- [TeX Live](https://www.tug.org/texlive/quickinstall.html) (for PDF generation. You should be fine if `pdflatex --version` in the command line works.)

Clone the repository and run the following commands to install the dependencies:

```bash
git clone https://github.com/liamrobinson1/quals-writeups.git
cd quals-writeups
python3 -m venv .
source bin/activate # or Scripts/activate.bat on Windows
pip install -r requirements.txt
```

To build the writeups to HTML and PDF simultaneously, run:

```bash
python convert.py
```

This script takes all the `.tex` files in the `tex/` directory and uses pandoc to convert them to `.rst` files which it places in `/docs/source`. It then uses Sphinx to build HTML versions of the `.tex` files and places them in `/docs/build/html`. Finally, it uses pandoc to convert the `.tex` files to a single `.pdf` file in the root directory.

You can view the documentation output by Sphinx by running `python -m http.server` in the `/docs/build/html` directory and navigating to `localhost:8000` in your browser.

Contributing
------------

To add a new problem writeup, navigate to the relevant course `.tex` file in the `tex/` directory and add a new `\section{}` with the problem name. `convert.py` will automatically recognize the new section and add it to the table of contents.