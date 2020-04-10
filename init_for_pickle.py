# Записи

tom = {'name': 'Tom Farell', 'age': 32, 'job': 'software engineer', 'pay': 30000}
bob = {'name': 'Bob Smith', 'age': 34, 'job': 'software engineer', 'pay': 40000}
sue = {'name': 'Sue Jones', 'age': 40, 'job': 'software engineer', 'pay': 50000}
bill = {'name': 'Bill Morgan', 'age': 50, 'job': 'developer', 'pay': 60000}

db = {}
db['tom'] = tom
db['bob'] = bob
db['sue'] = sue
db['bill'] = bill

if __name__ == '__main__':
    for key in db:
        print(key, '=>', db[key])

