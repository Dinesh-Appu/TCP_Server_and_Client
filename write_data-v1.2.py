import json

def create_new_user(Folder,Name,Uid,Password,Gender,Phone,Age):
 person ={"Users" : {Folder : {"Name": Name,"Uid": Uid ,"Gender": Gender ,"Phone": Phone ,"Age": Age}}}
 #person_dict = json.loads(person)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print(person_dict)
# Output: ['English', 'French']
 print(person['Users'])
 with open('w/dinesh9843474708@gmail.com.json','w') as f:
  #print(f.write(person))
  json.dump(person,f)

if __name__ == '__main__':
    create_new_user("left","dine","KNFNJSDN25452qDd","123435678","Male","3762843923","18")
    while True:
     exit()