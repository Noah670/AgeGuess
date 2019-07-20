# age statistics guesser
print("Find out how long you have been alive in weeks, days, hours, minutes, and even seconds!")
user = raw_input("What is your name: ")
print("It is nice to meet you " + user)
age = int(input("Please tell me how old you are: "))

weeks = age * 52
days = age * 365
hours = age * 8760
minutes = age * 525600
seconds = age * 3153600
avatar = age * 3024
# The runtime of avatar is 162 minutes

print user + ' you have been alive for: \n'
print weeks, 'weeks \n'
print days, 'days \n'
print hours, 'hours \n'
print minutes, 'minutes \n'
print seconds, 'seconds \n'
print 'You also could have spent the entirety of your life watching the movie Avatar', avatar , 'times instead \n'
print 'Well', user, 'remember the passage of time stops for no one so try to make the most out of each day!'
