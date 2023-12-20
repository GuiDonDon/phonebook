from application import phonebook

if __name__ == '__main__':
    db_path = "db/phonebook_raw.csv"
    contact_list = phonebook.get_contacts(db_path)
    phonebook.process_fio(contact_list)
    contact_list = phonebook.phone_data(contact_list)
    contact_list = phonebook.process_contact_list(contact_list)
    new_db_path = "db/phonebook.csv"
    phonebook.save_process_contacts(new_db_path, contact_list)