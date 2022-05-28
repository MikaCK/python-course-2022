import re

folder_name = "python-course-2022/posta.html"

with open(folder_name, encoding='utf-8') as vstup:
    web = vstup.read()
    
#print(web)


replacement = web.replace("\n", " ")
replacement = re.sub(" +", " ", replacement)
#print(replacement)

#psc = re.compile(r'\d{3} \d{2} \w+(?: \w+)*(?: [0-9]+?')
psc = re.compile(r"\d{3} \d{2} \w+(?:..) \w+(?:.{7})")
print(psc.findall(replacement))
results = psc.findall(replacement)
for result in results:
  print(result)