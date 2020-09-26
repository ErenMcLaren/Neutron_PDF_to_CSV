import tabula

""" 
    Helpful StackOverflow stuff:
# https://stackoverflow.com/a/49562555
# https://stackoverflow.com/a/60532664
# https://stackoverflow.com/a/49997114
# https://stackoverflow.com/a/54123725
# https://stackoverflow.com/a/39841757
"""

tabula.convert_into(
    "stuff/stuff2/Scattering_lengths_table.pdf", 
    "tu_wien_ait_neutron_scattering_lengths_and_cross_sections.csv", 
    output_format = "csv", 
    pages = "all")