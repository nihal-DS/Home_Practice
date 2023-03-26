# https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-23.php
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
new = {}
for d in item_list:
    if d['item'] not in new:
        new[d['item']] = d['amount']
    else:
        new[d['item']] += d['amount']
print(new)