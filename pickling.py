import pickle
cars=["audi","bmw","toyota","merc"]

f.open("Mycars.pkl",'wb')
pickle.dump(cars,f) # coverted into a byte stream & stored in file
f.close()


f1.open("Mycars.pkl",'rb')
pickle.load(f1) # convert back to normal list
f1.close()