from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import os
import re

os.chdir(r'C:\netology\phonebook')

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


for i in range(len(contacts_list)):
    fio = " ".join(contacts_list[i][:2]).rstrip().split(" ")
    try:
        for j in range(3):
            contacts_list[i][j] = fio[j]
    except IndexError:
        continue

    
my_list = []  
for m in contacts_list:
  s = ','.join(m)
  
  pattern = r"((\+7|8)\s*)(\D*?)(\d{3})(\D*?)(\d{3})(\D*?)(\d{2})(\D*?)(\d{2})"
  replace = r"+7(\4)\6-\8-\10"
  result = re.sub(pattern, replace, s)

  pattern = r"\(?(\bдоб.)(\s)(\d{4})\)?"
  replace = r"\1\3"
  result = re.sub(pattern, replace, result)

  my_list.append(result.split(',')) 

  



with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  datawriter.writerows(my_list)

#   def process_phone(data):
#     contact_list = list()
#     for contact in data:
#         contact_db = ",".join(contact)
#         contact_db = re.sub(phone_pattern, phone_sub, contact_db).rstrip().split(",")
#         contact_list.append(contact_db)
#     return contact_list

# def merge_doubles(contact_one, contact_two):
#     contact = list()
#     for index in range(len(contact_one)):
#         contact.append(contact_one[index]) if contact_one[index] else contact.append(contact_two[index])
#     return contact

# def process_contact_list(data):
#     contact_list = dict()
#     for item in data:
#         contact_list[" ".join(item[:2])] = merge_doubles(item, contact_list[" ".join(item[:2])]) if " ".join(item[:2]) in contact_list else item
#     return list(contact_list.values())
  



#   from application import phonebook

# if __name__ == '__main__':
#     db_path = "db/phonebook_raw.csv"
#     contact_list = phonebook.get_contacts(db_path)
#     phonebook.process_fio(contact_list)
#     contact_list = phonebook.process_phone(contact_list)
#     contact_list = phonebook.process_contact_list(contact_list)
#     new_db_path = "db/phonebook.csv"
#     phonebook.save_process_contacts(new_db_path, contact_list)