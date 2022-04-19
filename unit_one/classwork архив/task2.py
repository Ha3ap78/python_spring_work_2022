#todo: Задан массив
surname = ['Электроник','Сыроежкин', 'Чижиков', 'Кукушкина']

# Код на выходе должен выдавать выпадающий список следующего вида.
"""
<select>
	<option>Электроник</option>
	<option>Сыроежкин</option>
	<option>Чижиков</option>
	<option>Кукушкина</option>
</select>
"""
print("<select>")
for i in surname:
    print("    <option>", i, "</option>")
print("<select>")