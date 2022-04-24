#!/bin/python

import csv
import yaml
import os
import pypandoc

folder = "../projectyl.github.io/_data/summer/"
files = os.listdir(folder)
files = [file for file in files if ".csv" in file]

md_file = "../projectyl.github.io/_data/summer/summer.md"
pdf_file = "../projectyl.github.io/_pages/summer.pdf"

f = open(md_file, 'w')
f.close()
f = open(md_file, 'a')
pandoc_options = ['fontfamily: FiraSans', 'fontfamilyoptions: sfdefault', 'fontsize: 11pt', 'header-includes: |', '\t\\usepackage{hyperref,booktabs,colortbl,longtable,boldline,color,xcolor}', '\t\\usepackage[textheight=70cm,margin=2cm]{geometry}']
frontmatter = '---\n' + '\n'.join(pandoc_options) + '\n---\n'
f.write(frontmatter)

f.write('\\def\\arraystretch{1.6}\n')

f.write("# \\textcolor{blue}{Summer Internship Programs}\n")
f.write('\\vspace{-20pt}\n\\rule{\\textwidth}{2pt}\n\n')
f.write('The institute names in the left columns are hyperlinks to the respective webpages.\n')
titles = ['Active Programs', 'Currently Inactive/Closed', 'International Programs']
files = sorted(files)
assert len(titles) == len(files)

for title,file in zip(titles,files):
    f.write('\\vspace{10pt}\n')
    f.write('\\section{\\textcolor{purple}{' + title + '}}' + '\n\n')
    f.write('\\vspace{-10pt}\n')
    data = list(csv.reader(open(folder+file, 'r'), delimiter=','))
    ncols = len(data[0])
    f.write('\\begin{longtable}{V{4}l'+'V{4}c'*(ncols-2)+'V{4}}\n')
    f.write('\\hlineB{4}\n')
    head = ['\\textcolor{white}{\\textbf{'+datum+'}}' for datum in data[0]]
    f.write('\\rowcolor{black}\n')
    f.write(' & '.join(head[:-1]) + '\\\\\n')
    for row in data[1:]:
        f.write('\\hlineB{4}\n')
        if len(row) == 0: continue
        inst = row[0]
        link = row[-1]
        f.write('\href{' + link + '}{' + inst + '} & ' + ' & '.join(row[1:-1]) + ' \\\\\n')
    
    f.write('\\hlineB{4}\n')
    f.write('\\end{longtable}\n')


title = "Year-Round Programs"
file = "../projectyl.github.io/_data/year-round.yaml"
f.write('\\section*{\\textcolor{blue}{' + title + '}}' + '\n\n')
f.write('\\vspace{-15pt}\n\\rule{\\textwidth}{1.5pt}\n')
f.write('Many institutes offer year-round internships for interested students that are open throughout the year. UG/PG students are asked to send in their applications at any point of the year and participate in summer programs/research work for a certain amount of time. _Note that the headings are hyperlinks to the respective webpages_.\n')

for item in list(yaml.safe_load((open(file, 'r')))):
    f.write('\\section*{\\color{purple}{\\textbf{\\href{'+item['Link'] + '}{' + item['Institute'] + '}}}}' + '\n\n')
    f.write('\\textbf{Duration}: ' + item['Duration'] + '\n\n')
    f.write('\\textbf{Stipend}: ' + item['Stipend'] + '\n\n')
    if isinstance(item['Eligibility'], list):
        f.write('\\textbf{Eligibility}: ' + '\n')
        f.write('\\begin{itemize}\n')
        [f.write('\\item ' + elig + '\n') for elig in item['Eligibility']]
        f.write('\\end{itemize}\n')
    else:
        f.write('\\textbf{Eligibility}: ' + item['Eligibility'] + '\n')
    f.write('\n')

title = "Summer Schools"
file = "../projectyl.github.io/_data/summer/schools.yaml"
f.write('\\section*{\\textcolor{blue}{' + title + '}}' + '\n\n')
f.write('\\vspace{-15pt}\n\\rule{\\textwidth}{1.5pt}\n')
f.write('Many institutes offer year-round internships for interested students that are open throughout the year. UG/PG students are asked to send in their applications at any point of the year and participate in summer programs/research work for a certain amount of time. _Note that the headings are hyperlinks to the respective webpages_.\n')

for item in list(yaml.safe_load((open(file, 'r')))):
    f.write('\\section*{\\color{purple}{\\textbf{\\href{'+item['Link'] + '}{' + item['Name'] + '}}}}' + '\n\n')
    f.write('\\textbf{Institute}: ' + item['Institute'] + '\\hspace{\\fill}' + '\\textbf{Deadline}: ' + item['Deadline'] + '\\hspace{\\fill}\n\n')
    if isinstance(item['Topic'], list):
        f.write('\\textbf{Topic}: ' + '\n')
        f.write('\\begin{itemize}\n')
        [f.write('\\item ' + elig + '\n') for elig in item['Topic']]
        f.write('\\end{itemize}\n')
    else:
        f.write('\\textbf{Topic}: ' + item['Topic'] + '\n')
    f.write('\n')
    if isinstance(item['Target Audience'], list):
        f.write('\\textbf{Target Audience}: ' + '\n')
        f.write('\\begin{itemize}\n')
        [f.write('\\item ' + elig + '\n') for elig in item['Target Audience']]
        f.write('\\end{itemize}\n')
    else:
        f.write('\\textbf{Target Audience}: ' + item['Target Audience'] + '\n')
    f.write('\n')


f.write('\\rule{\\textwidth}{2pt}\n')
f.close()

out = os.system('pandoc ' + md_file + ' -t latex ' + ' -o ' + pdf_file)
assert out == 0
