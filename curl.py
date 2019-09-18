# coding=utf-8
import requests

headers = {
    'Content-type': 'application/json',
}

all = ['{"query":"මට නව ගිණුමක් විවෘත කරන්න ඕන"}', '{"query":"මට ඕනි ඉතිරිකිරීමේ ගිණුමක්"}', '{"query":"යොවුන් ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"ඔව් ඔක්කොම නිවැරදියි"}'
       ,'{"query":"ඔව් ගිණුම විවෘත කිරීම තහවුරු කරනවා"}']

# data = '{"query":"මට ඕනි ඉතිරිකිරීමේ ගිණුමක්"}'
for data in all:
    data = data.encode('utf-8')
    response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
    print (response.json())