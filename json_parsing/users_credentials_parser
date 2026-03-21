raw_json_data = """[{
  "metadata": {
    "batch_id": "EXP-2026-02",
    "source": "Legacy Database (Unstructured)"
  },
  "users": [
    {
      "id": "U-001",
      "personal": {
        "full_name": "Иван Иванов",
        "contacts": {
          "phone": "+7 (999) 123-45-67",
          "email": "ivan.ivanov@gmail.com",
          "social": "https://vk.com"
        }
      },
      "documents": "PASSPORT: 45#12 345678 (issued 2015)"
    },
    {
      "id": "U-002",
      "personal": {
        "full_name": "Sidorov Petr",
        "contacts": {
          "phone": "89001112233 (work only)",
          "email": "p.sidorov_2026!@company.ru",
          "social": "http://linkedin.com"
        }
      },
      "documents": "SERIES: 1234 NO: 999888"
    },
    {
      "id": "U-003",
      "personal": {
        "full_name": "Анна-Мария Смирнова",
        "contacts": {
          "phone": "invalid_number_123",
          "email": "anna-maria@domain",
          "social": "just_a_nickname"
        }
      },
      "documents": "None"
    },
    {
      "id": "U-004",
      "personal": {
        "full_name": "Alex J. Murphy",
        "contacts": {
          "phone": "   +7 911 000 11 22 (home), +7 922 333 44 55 (mobile)   ",
          "email": "OFFICER.MURPHY@DETROIT.PD",
          "social": "https://facebook.com"
        }
      },
      "documents": "ID-CARD #987654 (EXP: 2029)"
    },
    {
      "id": "U-005",
      "personal": {
        "full_name": "Елена",
        "contacts": {
          "phone": "8 (495) 777-77-77 доб. 123",
          "email": "elena_best_parsing@test.com.ru",
          "social": "https://inst.gr"
        }
      },
      "documents": "ПАСПОРТ РФ: 11-22 333444"
    }
  ]
}]"""
import re,json
users_data = json.loads(raw_json_data)
raw_phones = []
raw_emails = []
raw_documents = []
raw_socials = []
users = users_data[0]['users']
for unit in users:
    user_phone = unit['personal']['contacts']['phone']
    separated_user_phone = user_phone.split(',')
    raw_phones.append(separated_user_phone[0])

    user_email = unit['personal']['contacts']['email']
    raw_emails.append(user_email)

    user_document = unit['documents']
    raw_documents.append(user_document)

    user_social = unit['personal']['contacts']['social']
    raw_socials.append(user_social)

def sort_out_phone_numbers(phones):
    cleaned_phones = []
    for raw_phone in phones:
        if re.findall(r'(\d\s*\(?\d{3}\)?\s*\d{3}\s*-?\d{2}\s*-?\d{2}\s*)',raw_phone):
            raw_phone = re.sub(r'\D*','',raw_phone)
            if len(raw_phone) == 11:
                cleaned_phones.append(f'+{raw_phone}')
            else:
                raw_phone = ['INVALID_PHONE']
                cleaned_phones.append(raw_phone)
        else:
            raw_phone = 'INVALID_PHONE'
            cleaned_phones.append(raw_phone)
    return cleaned_phones
ready_numbers = sort_out_phone_numbers(raw_phones)

def sort_out_emails(emails):
    cleaned_emails = []
    for email in emails:
        if re.findall(r'^[\w.!#%$*-]+@\w+\.\w+$',email):
            email = re.sub(r'!','',email).lower()
            cleaned_emails.append(email)
        else:
            email = 'INVALID_EMAIL'
            cleaned_emails.append(email)
    return cleaned_emails
ready_emails = sort_out_emails(raw_emails)

def sort_out_documents(documents):
    cleaned_documents = []
    for document in documents:
        document = re.sub(r' !|#|&|\?|-|[a-zA-Z]|[а-яА-Я]|:|\(|\)','',document)
        if re.findall(r'\s*\d{4}\s*\d{6}',document):
            document = document.split()
            final_document = ' '.join(document[0:2])
            cleaned_documents.append(f'Russian Passport: {final_document}')
        else:
            document = 'INVALID_PASSPORT'
            cleaned_documents.append(document)
    return cleaned_documents
ready_documents = sort_out_documents(raw_documents)

def sort_out_socials(socials):
    cleaned_socials = []
    for social in socials:
        if re.findall(r'(https|http|ftp|ftps)://\w+(.com|.ru)',social):
            cleaned_socials.append(social)
        else:
            social = 'INVALID_SOCIAL'
            cleaned_socials.append(social)
    return cleaned_socials
ready_socials = sort_out_socials(raw_socials)

def update_data(phone_numbers,emails,documents,socials):
    for index , number in enumerate(phone_numbers):
        users_data[0]['users'][index]['personal']['contacts']['phone'] = number
    for index , email in enumerate(emails):
        users_data[0]['users'][index]['personal']['contacts']['email'] = email
    for index , document in enumerate(documents):
        users_data[0]['users'][index]['documents'] = document
    for index , social in enumerate(socials):
        users_data[0]['users'][index]['personal']['contacts']['social'] = social
    return users_data
update_data(ready_numbers,ready_emails,ready_documents,ready_socials)

def create_new_file():
    with open('cleaned_data.json','w',encoding='utf-8') as new_file:
        json.dump(users_data,new_file,indent = 3)
create_new_file()

