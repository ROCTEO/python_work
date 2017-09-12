friends = ['zjp','wmn','xxw','zqh','ym']
print(friends)
print(friends[3]+" can't attended")
friends[3] = 'qjl'
print(friends)
print("I have find a bigger table")
friends.insert(0,'wdd')
friends.insert(3,'hjy')
print(len(friends))
friends.append('oyzr')
num_list = [0,1,2,3,4,5,6,7]
for i in num_list:
    print("Hello! "+friends[i]+", chould you have a dinner with me?")
