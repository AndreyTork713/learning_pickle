import pickle

dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()