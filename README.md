# Neutron_PDF_to_CSV
Purpose: convert PDF of important data about neutron scattering lengths and cross sections to CSV format. $$\Sigma_{i=0}^{N}$$

## About
Comma-separated values (CSV) files are a text file that usually uses a comma to separate each unique value [[1]](#1). They are often used as data-storage and tabulation files.

The PDF in question is a 10-page, 110kb file available <a href = "http://www.ati.ac.at/~neutropt/scattering/Scattering_lengths_table_20010419.pdf">here</a>, provided by the Vienna University of Technology (<a href = "https://www.tuwien.at/en/">click</a> for English [[3]](#3)) [[2]](#2). The webpage on which this file is available was last updated 02/14/2001 [[2]](#2).

The majority of the column headers are described in the first paragraph of [[2]](#2) and in Table 1 in [[5]](#5), but to reiterate: <br />

ZSymbA: nuclide charge number Z, element symbol Symb, mass number A <br />
P or T_{1/2}: natural abundance OR "percent"/half-life (MIN: minutes, Y: years) <br />
I: nuclear spin <br /> 
b_{c}: bound-coherent scattering lengths, (fm, femptometers, 1e-15) <br /> 
b_{+}: spin-dependent scattering lengths for I + 1/2 (fm, femptometers, 1e-15) <br /> 
b_{-}: spin-dependent scattering lengths for I - 1/2 (fm, femptometers, 1e-15) <br />
c: ?? (if you know this, please contact me.) <br />
sigma_{coh}: coherent cross-section (barns, 1e-24 cm^-2) <br />
sigma_{inc}: incoherent cross-section (barns, 1e-24 cm^-2) <br />
sigma_{scatt}: scattering cross-section (barns, 1e-24 cm^-2) <br />
sigma_{abs}: absorption cross-section (barns, 1e-24 cm^-2) <br />

The purpose of this conversion of this PDF to CSV format is to obtain the exact information enclosed in the PDF in a more machine-readable format. The quickest method to perform this conversion was to look for existing Python packages that already had this capability. The first package that came up was <a href = "https://tabula.technology/">tabula</a>. tabula has two methods that were relevant for this task: `read_pdf` and `convert_into` [[4]](#4). Converting the PDF file into CSV was performed in two lines of code (#1, importing tabula, #2, using `convert_into`.)

Primarily, the parameter `pages` in `convert_into` was set to `"1"` just to test the efficacy of the method. It was confirmed that the output CSV matched the input PDF data by comparing the numbers in each cell of five randomly-selecting rows. As a demonstration, the first six rows of the PDF file are:

|ZSymbA|p or T_{1/2}|I|b_{c}|b_{+}|b_{-}|c|\sigma_{coh}|\sigma_{inc}|\sigma_{scatt}|\sigma_{abs}|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|<b>0-N-1</b>|<b>10.3 MIN</b>|<b>1/2</b>|<b>-37.0(6)</b>|<b>0</b>|<b>-37.0(6)</b>||<b>43.01(2)</b>||<b>43.01(2)</b>|<b>0</b>|
|<b>1-H</b>|||<b>-3.7409(11)</b>||||<b>1.7568(10)</b>|<b>80.26(6)</b>|<b>82.02(6)</b>|<b>0.3326(7)</b>|
|1-H-1|99.985|1/2|-3.7423(12)|10.817(5)|-47.420(14)|+/-|1.7583(10)|80.27(6)|82.03(6)|0.3326(7)|
|1-N-2|0.0149|1|6.674(6)|9.53(3)|0.975(60)||5.592(7)|2.05(3)|7.64(3)|0.000519(7)|
|1-H-3</b>|12.26 Y|1/2|4.792(27)|4.18(15)|6.56(37)||2.89(3)|0.14(4)|3.03(5)|< 6.0E-6|
                                                                                     
and the first six rows of the CSV file are:

`ZSymbA,p or T1/2,I,bc,b+,b-,c,σcoh,σ inc,σscatt,σabs` <br />
`0-N-1,10.3 MIN,1/2,-37.0(6),0,-37.0(6),,43.01(2),,43.01(2),0` <br />
`1-H,,,-3.7409(11),,,,1.7568(10),80.26(6),82.02(6),0.3326(7)` <br />
`1-H-1,99.985,1/2,-3.7423(12),10.817(5),-47.420(14),+/-,1.7583(10),80.27(6),82.03(6),0.3326(7)` <br />
`1-H-2,0.0149,1,6.674(6),9.53(3),0.975(60),,5.592(7),2.05(3),7.64(3),0.000519(7)` <br />
`1-H-3,12.26 Y,1/2,4.792(27),4.18(15),6.56(37),,2.89(3),0.14(4),3.03(5),< 6.0E-6` <br />
                                                                                                                                                         
At this point, `pages` was changed to `"all"`, and the final CSV file was obtained. Once again, the final CSV file was checked with the original PDF file. There remains no obvious method besides manually checking the numbers per row to verify that all the values in all 10 pages of the PDF remain the exact same. After verifying that the values in five rows randomly-selected from the final CSV file matched exactly their counterparts in the PDF file, it was assumed that the rest of the CSV file copied all the information correctly. Empty cells in the PDF are empty in the corresponding CSV file, preserving the dimension of the data structure. Should there be a way to more rigorously approaching this problem, please contact me.

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
Ariga A. (2020) <a href = "https://www.tandfonline.com/doi/abs/10.1080/10448639208218770">tabula-py</a>. <i>github.com/chezou</i>. Retrieved September 25, 2020.
</li>

<li>
<a id = "5">[5]</a>
Varley F. Sears (1992) <a href = "10.1080/10448639208218770">Neutron scattering lengths and cross sections</a>. Neutron scattering lengths and cross sections, <i>Neutron News</i>,<b>3:3</b>, 26-37. Retrieved September 27, 2020.
</li>

## Parenthetical:
For how to use tabula's method "read_pdf": https://stackoverflow.com/a/49562555 <br />
For how to resolve the issue "modules 'tabula' has no attribute 'read_pdf'": https://stackoverflow.com/a/60532664 <br />
For why method 'read_pdf' was not included in tabula: https://stackoverflow.com/a/49997114 <br />
For another reason why 'read_pdf' was not working with tabula: https://stackoverflow.com/a/54123725 <br />
For how to respond to 'y/n' prompts in Jupyter Notebook: https://stackoverflow.com/a/39841757 

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
