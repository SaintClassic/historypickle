

import pickle

def rate_wins(dict, player):
    rate = dict[player][1]/dict[player][0]
    return print("The rate of winning for player", player ,'is ', round(rate, 2))

#Key = Name of player, Value is a tuple( # games played, # victories)
history = {'Archy':(12,4), 'Betty':(10,6)}

# file_p3 = open('historypickle,p', 'wb')
# pickle.dump(history, file_p3)
# file_p3.close()
#
# #open the history pickle file and read from it
#
file_p3 = open('historypickle,p', 'rb')
history = pickle.load(file_p3)
file_p3.close()
# print(history)
# history['Cora'] = (100,80)
# print(history)

for key in history.keys():
    rate_wins(history, key)