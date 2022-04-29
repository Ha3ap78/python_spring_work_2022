#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML> 
<html> 
 <head> 
  <title> ? </title> 
  <meta charset=?> 
 </head> 
 <body onload="alert(?)"> 

  <p>?</p> 

 </body> 
</html> 
"""
count = 0
template_new = list(template)

for key, value in page.items():
        count = 0
        for i in template_new:
                count += 1
                if i == "?":
                        template_new[count - 1] = value
                        break

string = ''.join(template_new)
f = open('index.html', 'wt', encoding="UTF8")
f.write(string)
print(string)

f.close()






