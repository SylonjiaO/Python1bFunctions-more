#Temp Values

weeklytemp=[26.6,27.2,26.8,27.1,28.0,27.4]
nexttemp= lambda y: y+.5
nextweektemp=tuple(map(nexttemp, weeklytemp))
print(nextweektemp)
