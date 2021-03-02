file_r = open('esenin.txt', mode='r', encoding='utf-8')
txt = file_r.read()
file_r.close()

file_w = open('esenin_pattern.html', mode='w', encoding='utf-8')
for lines in file_r.readlines():
    esenin.write("<p>" + lines + "</p> <br>\n")

file_w.close()