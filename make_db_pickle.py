from init_for_pickle import db
import pickle
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()