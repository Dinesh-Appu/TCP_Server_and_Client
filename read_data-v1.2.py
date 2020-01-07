import json

with open('w/dinesh9843474708@gmail.com.json') as f:
  data = json.load(f)
p = data['Users']
p2 = p['left']
print(p2['Name'])
  # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
   #print(data)