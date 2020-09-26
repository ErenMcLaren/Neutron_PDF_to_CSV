# Neutron_PDF_to_CSV
Purpose: convert PDF of important data about neutron scattering lengths and cross sections to more-convenient CSV format.

## About
Comma-separated values (CSV) files are a text file that usually uses a comma to separate each unique value [[1]](#1). They are often used as data-storage and tabulation files.

The PDF in question is a 10-page, 110kb file available <a href = "http://www.ati.ac.at/~neutropt/scattering/Scattering_lengths_table_20010419.pdf">here</a>, provided by the Vienna University of Technology (click <a href = "https://www.tuwien.at/en/"></a> for English) [[2]](#2).

The purpose of this conversion of this PDF to CSV format is to obtain the exact information enclosed in the PDF in a more machine-readable format. The quickest method to perform this conversion was to look for existing Python packages that already had this capability. The first package that came up was <a href = "https://tabula.technology/">tabula</a>. tabula has two methods that were relevant for this task: `read_pdf` and `convert_into` [[3]](#3). Converting the PDF file into CSV was performed in two lines of code (#1, importing tabula, #2, using `convert_into`.)

Afterwards, the output CSV file was checked with the original PDF file. There remains no obvious method besides manually checking the numbers per row to verify that the conversion was successful. After verifying that the values in five rows randomly-selected from the CSV files matched exactly their counterparts in the PDF file, it was assumed that the rest of the CSV file copied all the information correctly. Empty cells in the PDF are empty in the corresponding CSV file, preserving the dimension of the data structure. Should there be a way to more rigorously approaching this problem, please contact me.

This project concludes with a reflection: consider storing experimental data both in a PDF format, for final copies, and a machine-readable format like a CSV, to be used in data science applications.

## References
<li>
<a id = "1">[1]</a>
<a href = "https://tools.ietf.org/html/rfc4180#section-2">Definition of the CSV Format</a>. Internet Engineering Task Force. Retrieved September 25, 2020.
</li>

<li>
<a id = "2">[2]</a>
<a href = "http://www.ati.ac.at/~neutropt/scattering/table.html">Neutron Scattering Lengths</a>. Vienna University of Technology. Retrieved September 25, 2020.
</li>

<li>
<a id = "3">[3]</a>
Ariga A. <a href = "https://github.com/chezou/tabula-py">tabula-py</a>. <i>github.com/chezou</i>. Retrieved September 25, 2020.
</li>

## Parenthetical:
For how to use tabula's method "read_pdf": https://stackoverflow.com/a/49562555 \n
For how to resolve the issue "modules 'tabula' has no attribute 'read_pdf'": https://stackoverflow.com/a/60532664
For why method 'read_pdf' was not included in tabula: https://stackoverflow.com/a/49997114
For another reason why 'read_pdf' was not working with tabula: https://stackoverflow.com/a/54123725
For how to respond to 'y/n' prompts in Jupyter Notebook: https://stackoverflow.com/a/39841757
