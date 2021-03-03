with open ('esenin.txt', 'r', encoding='utf-8') as file1:
    txt_lines = file1.read().split('\n')
    file1.close()

with open('esenin_main.html', mode='r', encoding='utf-8') as file2:
    html_lines = file2.read().split('\n')
    file2.close()

txt_lines.append('</p>')
txt_lines.insert(0, '<p>')


for id, item in enumerate(txt_lines):
    if id == 0 or id == len(txt_lines) - 1:
        html_lines.insert(html_lines.index(''), txt_lines[id])
    elif txt_lines[id] != '':
        txt_lines[id] = txt_lines[id] + '<br>'
    elif txt_lines[id] == '':
        txt_lines[id] += '</p>  <p>'

    html_lines.insert(html_lines.index(''),txt_lines[id])


with open('esenin_main.html', 'w', encoding='utf8') as out:
    for elm in html_lines:
        out.write(elm + '\n')

    out.close()
