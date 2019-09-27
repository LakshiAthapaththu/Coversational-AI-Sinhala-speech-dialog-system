# coding=utf-8
import requests

headers = {
    'Content-type': 'application/json',
}
all1 = ['{"query":"මට නව ගිණුමක් විවෘත කරන්න ඕන"}','{"query":"මට ඕනි ඉතිරිකිරීමේ ගිණුමක්"}','{"query":"යොවුන් ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"ඔව් ඔක්කොම නිවැරදියි"}'
       ,'{"query":"ඔව් ගිණුම විවෘත කිරීම තහවුරු කරනවා"}']

for data in all1:
    print("User: ", data)
    data = data.encode('utf-8')
    response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
    print (response.json())



# story 1

# all1 = ['{"query":"මට නව ගිණුමක් විවෘත කරන්න ඕන"}', '{"query":"මට ඕනි ඉතිරිකිරීමේ ගිණුමක්"}', '{"query":"යොවුන් ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"ඔව් ඔක්කොම නිවැරදියි"}'
#        ,'{"query":"ඔව් ගිණුම විවෘත කිරීම තහවුරු කරනවා"}']
#
# for data in all1:

#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print (response.json())

# #story 2
# all1 = ['{"query":"ගිණුමක් විවෘත කරන්න ඕන"}', '{"query":"ඉතුරුම් ගිණුමක් හදන්න"}', '{"query":"ජේයෂ්ට පුරවැසි ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"මේ ඩීටේයිල්ස් හරි"}',
#        '{"query":"ගිණුම විවෘත කිරීම නතර කරන්න"}','{"query":"මට ආපහු ට්‍රයි කරන්න ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())
#
# # story 3
# all1 = ['{"query":"ගිණුමක් විවෘත කරන්න ඕන"}', '{"query":"ඉතුරුම් ගිණුමක් හදන්න"}', '{"query":"ජේයෂ්ට පුරවැසි ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"මේ ඩීටේයිල්ස් හරි"}',
#        '{"query":"ගිණුම විවෘත කිරීම නතර කරන්න"}','{"query":"නෑ ඕන නෑ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 4 -- not worked
#
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"ඉතුරුම් ගිණුමක්"}', '{"query":"සාමානය ඉතුරුම් ගිණුමක්"}', '{"query":"හතර"}','{"query":"තොරතුරු වැරදි බව සනාථ කරන්න ඕන"}',
#        '{"query":"තව පාරක් කරලා බලන්න"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())
#
# #story 5
# #
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඉතිරිකිරීමේ ගිණුමක්"}', '{"query":"සාමානය ඉතුරුම් ගිණුමක්"}', '{"query":"හතර"}','{"query":"ඩීටේයිල්ස් වල වැරැද්දක් තියනවා"}',
#        '{"query":"නෑ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())
#
# # story 6 - not working
#
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුන"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"හතර"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/111/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())
#
# # story 7 - no
#
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 8
#
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"මට නවත්තන්න ඕන"}', '{"query":"මට ආපහු ට්‍රයි කරන්න ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/10000/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 9
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"තව ට්‍රයි එකක් ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 10
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"ආයෙත් උත්සහ කරන්න ඕන නැහැ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 11

# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුන"}','{"query":"මාසිකව ගන්නවා"}', '{"query":"හතර"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/111/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 11

# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"පොළිය මාසිකව ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 12
#
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"මට නවත්තන්න ඕන"}', '{"query":"ආයෙත් උත්සහ කරන්න ඕන නැහැ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())



#story 13
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"මට නවත්තන්න ඕන"}', '{"query":"තව පාරක් කරලා බලන්න"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 14
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"තව ට්‍රයි එකක් ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 15
# all1 = ['{"query":"අලුත් එකව්න්ට් එකක් ඕපන් කරන්න ඕනි"}', '{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"ආයෙත් උත්සහ කරන්න ඕන නැහැ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())


##################################################################################################################

# #story 16
# all1 = ['{"query":"මට ඕනි ඉතිරිකිරීමේ ගිණුමක්"}', '{"query":"යොවුන් ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"ඔව් ඔක්කොම නිවැරදියි"}'
#        ,'{"query":"ඔව් ගිණුම විවෘත කිරීම තහවුරු කරනවා"}']
#
# for data in all1:
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print (response.json())
#
# print()
#
# # story 17
# all1 = ['{"query":"ඉතුරුම් ගිණුමක් හදන්න"}', '{"query":"ජේයෂ්ට පුරවැසි ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"මේ ඩීටේයිල්ස් හරි"}',
#        '{"query":"ගිණුම විවෘත කිරීම නතර කරන්න"}','{"query":"මට ආපහු ට්‍රයි කරන්න ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 18
# all1 = ['{"query":"ඉතුරුම් ගිණුමක් හදන්න"}', '{"query":"ජේයෂ්ට පුරවැසි ඉතුරුම් ගිණුමක්"}', '{"query":"එක"}','{"query":"මේ ඩීටේයිල්ස් හරි"}',
#        '{"query":"ගිණුම විවෘත කිරීම නතර කරන්න"}','{"query":"නෑ ඕන නෑ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())
#
# print()

#story 19

# all1 = ['{"query":"ඉතුරුම් ගිණුමක්"}', '{"query":"සාමානය ඉතුරුම් ගිණුමක්"}', '{"query":"හතර"}','{"query":"තොරතුරු වැරදි බව සනාථ කරන්න ඕන"}',
#        '{"query":"තව පාරක් කරලා බලන්න"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 20

# all1 = ['{"query":"මට ඕන ඉතිරිකිරීමේ ගිණුමක්"}', '{"query":"සාමානය ඉතුරුම් ගිණුමක්"}', '{"query":"හතර"}','{"query":"ඩීටේයිල්ස් වල වැරැද්දක් තියනවා"}',
#        '{"query":"නෑ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/2/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 21

# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුන"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"හතර"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 22
#
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 23
#
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"මට නවත්තන්න ඕන"}', '{"query":"මට ආපහු ට්‍රයි කරන්න ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 24
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"තව ට්‍රයි එකක් ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 25
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"කල් පිරීමේදී ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"ආයෙත් උත්සහ කරන්න ඕන නැහැ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 26

# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුන"}','{"query":"මාසිකව ගන්නවා"}', '{"query":"හතර"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/111/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 27

# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"පොළිය මාසිකව ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"ඔව් තහවුරු කරනවා"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

#story 28
#
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"මට නවත්තන්න ඕන"}', '{"query":"ආයෙත් උත්සහ කරන්න ඕන නැහැ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())



#story 29
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව ලබා ගන්නවා"}', '{"query":"එක"}','{"query":"ඉහත තොරතුරු නිවැරදියි"}',
#        '{"query":"මට නවත්තන්න ඕන"}', '{"query":"තව පාරක් කරලා බලන්න"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 30
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"තව ට්‍රයි එකක් ඕන"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())

# #story 31
# all1 = ['{"query":"මට ඕන ඵෆ්ඩි එකක්"}', '{"query":"මාස තුනයි"}','{"query":"මාසිකව"}', '{"query":"එක"}','{"query":"තොරතුරු වැරදියි"}',
#         '{"query":"ආයෙත් උත්සහ කරන්න ඕන නැහැ"}']
#
# for data in all1:
#     print("User: ", data)
#     data = data.encode('utf-8')
#     response = requests.post('http://localhost:5005/conversations/11/respond', headers=headers, data=data)
#     print ("Bot: ", response.json())
