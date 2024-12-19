
# numbers={1: "one", 2:"two"}
# numbers.clear()
# print(numbers)

# alphabets={'a','b','c'}
# number=1
# dictionary=dict.fromkeys(alphabets,number)
# print(dictionary)
# print(type(alphabets))

# city={"new york":18,"texas":18}
# print("dictionary before clear()",city)
# city.clear()
# print("dictionary after clear():",city)

# original_marks={'physics':67,'maths':87}
# copied_marks=original_marks.copy()
# print('origiinal marks:',original_marks)
# print('copied marks:',copied_marks)

# original={1:'one',2:'two'}
# new=original.copy()
# print('original:',original)
# print('new"',new)

# keys={'a','e','i','o','u'}
# value='vowel'
# vowels=dict.fromkeys(keys,value)
# print(vowels)
# print(type(keys))

# scores={'pysics':67,
#         'maths':87,
#         'history':75
# }
# result=scores.get('physics')
# print(result)

# person={'name':'sakthi','age':22}
# print("name:",person.get('name'))
# print('age:',person.get('age'))
# print('salary:',person.get('salary'))
# print('salary:',person.get('salary',0.0))

# marks={'physics':67,'maths':87}
# print(marks.items())

# person={'name':'abi','age':22,'salry':3500.0}
# result=person.popitem()
# print('return value=',result)
# print('person=',person)
# person['profession']='plumber'
# result=person.popitem()
# print('return value=',result)
# print('person=',person)

# person={'name':'nisha','age':15}
# age=person.setdefault('age')
# print('person=',person)

# person={'name':'kasi'}
# salary=person.setdefault('salary',20000)
# print('person=',person)
# age=person.setdefault('age',45)
# print('person=',person)

# marks={'physics':67,'maths':87}
# internal_marks={'practical':48}
# marks.update(internal_marks)
# print(marks)

# d={1:'one',2:'three'}
# d1={2:'two'}
# d.update(d1)
# print(d)
# d1={3:'three'}
# d.update(d1)
# print(d)

# a={5:'five',6:'six',7:'eight'}
# b={7:'seven'}
# a.update(b)
# print(a)
# b={8:'eight'}
# a.update(b)
# print(a)

# dictionary={'x':2}
# dictionary.update([('y',3),('z',0)])
# print(dictionary)

# marks={'physics':67,'maths':87}
# print(marks.values())

# sales={'apple':2,'orange':3,'grapes':4}
# values=sales.values()
# print('original items:',values)
# del[sales['apple']]
# print('updated items:',values)

# student_id={112,114,116,118,115}
# print("student id:",student_id)
# vowel_letters={'a','e','i','o','u'}
# print("vowel letters:",vowel_letters)
# mixed_set={'hello',101,-2,'bye'}
# print('set of mixed data types:',mixed_set)

# empty_set=set()
# empty_dictionary={}
# print('data type of empty_set:',type(empty_set))
# print('data type of empty_dictionary:',type(empty_dictionary))

# numbers={21,34,54,12}
# print('initial set:',numbers)
# numbers.add(32)
# print('updated set:',numbers)

# companies={'locaste','ralph lauren'}
# tech_companies=['apple','google','apple']
# companies.update(tech_companies)
# print(companies)

# even_numbers={2,4,6,8}
# print('set:',even_numbers)
# print('total elements:',len(even_numbers))

# a={1,3,5}
# b={0,2,4}
# print('union using|:',a|b)
# print('union using union():',a.union(b))

# translation={97:None,98:None,99:105}
# string="abcdef"
# print("Original string:",string)
# print("Translated string:",string.translate(translation))

