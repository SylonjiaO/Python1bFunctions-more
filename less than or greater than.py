migrationspeed=[4.3,6.3,2.4,5.1,3.8,3.5,4.1,2.7,3.9]
standard=3.8
below=filter(lambda x: x <= standard,migrationspeed)
above=filter(lambda x: x >standard,migrationspeed)
print(list(above))
print(list(below))
