from pprint import pprint

#zadanie 1
lipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

#zadanie 2
name = "Maksymilian"
last_name = "Wróbel"
char_1 = name[:2]
char_2 = last_name[:3]
char = (char_1+char_2)
char = list(char)
num_of_the_chars = sum([lipsum.count(x) for x in char])
print(num_of_the_chars)


#zadanie 3
print('{:{align}{width}}'.format('Lorem', align='^', width='10'))
print('{:.{prec}} = {:.{prec}f}'.format('Float', 2.7182, prec=3))
person = {'first': 'Max', 'last': 'Wróbel'}
print('{p[first]} {p[last]}'.format(p=person))
print('{: d}'.format((- 23)))
print('{:.5}'.format('Lorem Ipsum jest tekstem stosowanym'))

#zadanie 4
zmienna_typu_string = "Lorem Ipsum"
#print(dir(zmienna_typu_string))
#help(zmienna_typu_string.join)

#zadanie 5
extended_slice = name[::-1].capitalize() + " " + last_name[::-1].capitalize()
print(extended_slice)

#zadanie 6
my_list = list(range(1,11))
new_list = []
for x in range(5):
    new_list.append(my_list.pop())
new_list.reverse()
print(my_list)
print(new_list)

#zadanie7
combined_list = [0] + my_list + new_list
combined_list.sort(reverse=True)
print(combined_list)

#zadanie8
students = [(1234, "Jan", "Kowalski"), (1235, "Kazimierz", "Dejna"), (1236, "Karolina", "Gałąź"), (1237, "Maksymilian", "Wróbel")]

print(students)
#zadanie9
students_dict = dict()

for index, name, last_name in students:
    students_dict[index] = name + " " + last_name

other_data = [(22, "adres@costam.pl", 1996, "Boczna 15"), (31, "adres@costam.pl", 1996, "Jagiellońska 5"), (24, "adres@costam.pl", 1996, "Dworcowa 51"), (20, "adres@costam.pl", 1999, "OstatniTupel 51")]
counter = 0
for key in students_dict.keys():
    for age, email, year, adress in other_data[counter:]:
        students_dict[key] += " " + str(age) + " " + email + " " + str(year) + " " + adress
        counter += 1
        break
        
pprint(students_dict)

#zadanie10
numbers = [501211311, 501211311, 412333111, 412333111, 888999000, 888999000]

numbers = set(numbers)
numbers = list(numbers)
print(numbers)

#zadanie11
print([x for x in range(1, 11)])

#zadanie12
print([x for x in range(100, 19, -5)])

#zadanie13
list_of_dicts = [{1: 'one', 2: 'two'}, {3: 'three', 4: 'four'}, {5: 'five', 6: 'six'}]
my_str = ""
for item in list_of_dicts:
    for key, value in item.items():
        my_str += f"{key}: {value}\n"

print(my_str)
print("The end")

        
      
    
    



