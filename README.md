Installation Guide
==================

Dependencies:

- Python 3.9+
- [Pandoc](https://pandoc.org/installing.html)
- [TeX Live](https://www.tug.org/texlive/quickinstall.html) (for PDF generation. You should be fine if `pdflatex --version` in the command line works.)

Clone the repository and run the following commands to install the dependencies:

```bash
git clone https://github.com/liamrobinson1/quals-writeups.git
cd quals-writeups
python -m venv .
source bin/activate # or Scripts/activate.bat on Windows
pip install -r requirements.txt
```

To build the writeups to HTML and PDF simultaneously, run:

```bash
python convert.py
```

Contributing
------------

To add a new problem writeup, navigate to the relevant course `.tex` file in the `tex/` directory and add a new `\section{}` with the problem name. `convert.py` will automatically recognize the new section and add it to the table of contents.