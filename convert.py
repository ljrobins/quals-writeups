import subprocess
import os

def rst_to_tex(input_file, output_file):
    try:
        subprocess.run(["pandoc", 
                        '--template=mytemplate.tex', 
                        '--pdf-engine=pdflatex', 
                        "--standalone", 
                        # "--toc",
                        "-N",
                        '-s', input_file, 
                        "-o", output_file], 
                        check=True)
        print(f"Conversion successful: {output_file} created.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def tex_to_pdf(input_file, output_file, clean: bool = True):
    try:
        subprocess.run(["pdflatex", input_file, "-o", output_file], check=True)
        print(f"Conversion successful: {output_file} created.")
        if clean:
            os.system("rm -f *.aux *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml *.snm *.nav")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def pdf_preview(input_file):
    try:
        subprocess.run(["open", input_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def make_sphinx(root_dir: str = "docs"):
    try:
        subprocess.run(["make", "html"], cwd=root_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def rst_to_pdf(rst, tex, pdf, open: bool = False, clean: bool = True):
    rst_to_tex(rst, tex)
    tex_to_pdf(tex, pdf, clean)
    if open:
        pdf_preview(pdf)

def tex_to_rst(input_file, output_file):
    try:
        subprocess.run(["pandoc", input_file, "-o", output_file], check=True)
        print(f"Conversion successful: {output_file} created.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def clean_rst(dir):
    for file in os.listdir(dir):
        if file.endswith(".rst"):
            os.remove(os.path.join(dir, file))

def make_index():
    preamble = """Astrodynamics and Space Applications Qualifying Exam Notes
============================================================

.. toctree::
    :maxdepth: 3
    :caption: Contents:

    """
    with open("docs/source/index.rst", "w") as f:
        f.write(preamble)
        tex_files = sorted(os.listdir("tex"))
        for tex in tex_files:
            f.write(f"\n    {tex[:-4]}\n")

        for tex in tex_files:
            f.write(f'.. include:: {tex[:-4]}.rst \n')

# Example usage
rst = "docs/source/index.rst"

clean_rst("docs/source")
make_index()
for tex in os.listdir("tex"):
    tex_to_rst(os.path.join('tex', tex), f"docs/source/{tex[:-4]}.rst")
make_sphinx()
rst_to_pdf(rst, 'out.tex', 'out.pdf', open=False)