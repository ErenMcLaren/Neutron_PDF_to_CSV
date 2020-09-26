# Neutron_PDF_to_CSV
Purpose: convert PDF of important data about neutron scattering lengths and cross sections to CSV format.

## About
Comma-separated values (CSV) files are a text file that usually uses a comma to separate each unique value [[1]](#1). They are often used as data-storage and tabulation files.

The PDF in question is a 10-page, 110kb file available <a href = "http://www.ati.ac.at/~neutropt/scattering/Scattering_lengths_table_20010419.pdf">here</a>, provided by the Vienna University of Technology (<a href = "https://www.tuwien.at/en/">click</a> for English [[3]](#3)) [[2]](#2). The webpage on which this file is available was last updated 02/14/2001 [[2]](#2).

The column headers are described in the first paragraph of [[2]](#2), but to reiterate: <br />

ZSymbA: nuclide charge number Z, element symbol Symb, mass number A <br />
P or T_{1/2}: natural abundance OR "percent"/half-life (MIN: minutes, Y: years) <br />
I: nuclear spin <br /> 
b_{c}: bound-coherent scattering lengths, (fm, femptometers, 1e-15) <br /> 
b+: spin-dependent scattering lengths for I + 1/2 (fm, femptometers, 1e-15) <br /> 
b-: spin-dependent scattering lengths for I - 1/2 (fm, femptometers, 1e-15) <br />
c: ?? (if you know this, please contact me.) <br />
sigma_{coh}: coherent cross-section (barns, 1e-24 cm^-2) <br />
sigma_{inc}: incoherent cross-section (barns, 1e-24 cm^-2) <br />
sigma_{scatt}: scattering cross-section (barns, 1e-24 cm^-2) <br />
sigma_{abs}: absorption cross-section (barns, 1e-24 cm^-2) <br />

The purpose of this conversion of this PDF to CSV format is to obtain the exact information enclosed in the PDF in a more machine-readable format. The quickest method to perform this conversion was to look for existing Python packages that already had this capability. The first package that came up was <a href = "https://tabula.technology/">tabula</a>. tabula has two methods that were relevant for this task: `read_pdf` and `convert_into` [[4]](#4). Converting the PDF file into CSV was performed in two lines of code (#1, importing tabula, #2, using `convert_into`.)

Primarily, the parameter `pages` in `convert_into` was set to `"1"` just to test the efficacy of the method. After visually comfirming that the output CSV matched the input PDF data by comparing the numbers in each cell of five randomly-selecting rows, `pages` was changed to `"all"`. As a demonstration, the first six rows of the PDF file are:
|ZSymbA|p or T_{1/2}|I|b_{c}|b_{+}|b_{-}|c|\sigma_{coh}|\sigma_{inc}|\sigma_{scatt}|\sigma_{abs}|
|:---|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|---:|
|X|X|X|X|X|X|X|X|X|X|X|
|X|X|X|X|X|X|X|X|X|X|X|

Afterwards, the output CSV file was checked with the original PDF file. There remains no obvious method besides manually checking the numbers per row to verify that the conversion was successful. After verifying that the values in five rows randomly-selected from the CSV files matched exactly their counterparts in the PDF file, it was assumed that the rest of the CSV file copied all the information correctly. Empty cells in the PDF are empty in the corresponding CSV file, preserving the dimension of the data structure. Should there be a way to more rigorously approaching this problem, please contact me.

This project concludes with a reflection: consider storing experimental data both in a PDF format, for final copies, and a machine-readable format, like a CSV, to be used in data science applications.

## References
<li>
<a id = "1">[1]</a>
<a href = "https://tools.ietf.org/html/rfc4180#section-2">Definition of the CSV Format</a>. Internet Engineering Task Force. Retrieved September 25, 2020.
</li>

<li>
<a id = "2">[2]</a>
<a href = "http://www.ati.ac.at/~neutropt/scattering/table.html">Bound Coherent Neutron Scattering Lengths</a>. Vienna University of Technology. Retrieved September 25, 2020.
</li>

<li>
<a id = "3">[3]</a>
<a href = "https://ati.tuwien.ac.at/research_areas/neutron_quantum_physics/research/techniques_of_neutron_physics/table_of_neutron_scattering_lengths/EN/
">Neutron Scattering Lengths</a>. Vienna University of Technology. Retrieved September 26, 2020.
</li>

<li>
<a id = "4">[4]</a>
Ariga A. (2020) <a href = "https://github.com/chezou/tabula-py">tabula-py</a>. <i>github.com/chezou</i>. Retrieved September 25, 2020.
</li>

## Parenthetical:
For how to use tabula's method "read_pdf": https://stackoverflow.com/a/49562555 <br />
For how to resolve the issue "modules 'tabula' has no attribute 'read_pdf'": https://stackoverflow.com/a/60532664 <br />
For why method 'read_pdf' was not included in tabula: https://stackoverflow.com/a/49997114 <br />
For another reason why 'read_pdf' was not working with tabula: https://stackoverflow.com/a/54123725 <br />
For how to respond to 'y/n' prompts in Jupyter Notebook: https://stackoverflow.com/a/39841757 
