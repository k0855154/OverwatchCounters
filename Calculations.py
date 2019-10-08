def MainCalculations(HeroList,OverwatchInfo,ListHeroes,ListCounters,ListOfListCounters,array_length,OverwatchCounters):
  for b in range(6):
    Hero = input("Find Data for what Hero: ")
    for i in range(array_length):
      if Hero == OverwatchInfo[i][0]:
        print(OverwatchInfo[i])
        print(i)
        ListHeroes.append(OverwatchInfo[i][0])
        ListCounters.append(OverwatchCounters[i])
      
        print(ListHeroes)
        print(ListCounters)
      else:
        i =+ 1
  print(OverwatchCounters)
  Hero1 = ListCounters[0]
  Hero2 = ListCounters[1]
  Hero3 = ListCounters[2]
  Hero4 = ListCounters[3]
  Hero5 = ListCounters[4]
  Hero6 = ListCounters[5]
  HeroSum1 = []
  HeroList = []
  c = 0
  d = 0
  for c in range(array_length):
     HeroSum1.append(Hero1[c] + Hero2[c] + Hero3[c] + Hero4[c] + Hero5[c] + Hero6[c])
     c =+ 1
  for d in range(HeroList):
    print(HeroList[d],":",HeroSum1[d])
    d =+ 1
