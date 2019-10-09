def MainCalculations(HeroList,OverwatchInfo,ListHeroes,ListCounters,ListOfListCounters,array_length,OverwatchCounters,OverwatchSynergies):
  print(HeroList)
  ListSynergies = []
  TierList = []
  for b in range(6):
      def ClickedLucio():
        Hero = "Lucio"
      def ClickedReinhardt():
       Hero = "Reinhardt"
        for i in range(array_length):
          if Hero == OverwatchInfo[i][0]:
            print(OverwatchInfo[i])
            print(i)
            ListHeroes.append(OverwatchInfo[i][0])
            ListSynergies.append(OverwatchSynergies[i])
            ListCounters.append(OverwatchCounters[i])
            print(ListHeroes)
            print(ListCounters)
          else:
            i =+ 1
  #Get Tiers
  tierMode = input("Tier mode on? ")
  if tierMode == 1:
    for _ in range(array_length):
      TierList.append(OverwatchInfo[_][6])
      _ =+ 1
  else:
    for m in range(array_length):
       TierList.append(0)
       m =+ 1
  print(OverwatchCounters)
  Hero1C = ListCounters[0]
  Hero2C = ListCounters[1]
  Hero3C = ListCounters[2]
  Hero4C = ListCounters[3]
  Hero5C = ListCounters[4]
  Hero6C = ListCounters[5]
  Hero1S = ListSynergies[0]
  Hero2S = ListSynergies[1]
  Hero3S = ListSynergies[2]
  Hero4S = ListSynergies[3]
  Hero5S = ListSynergies[4]
  Hero6S = ListSynergies[5]

  HeroSum1 = []
  c = 0
  d = 0
  for c in range(array_length):
     HeroSum1.append(Hero1C[c] + Hero2C[c] + Hero3C[c] + Hero4C[c] + Hero5C[c] + Hero6C[c] + Hero1S[c] + Hero2S[c] + Hero3S[c] + Hero4S[c] + Hero5S[c] + Hero6S[c] + TierList[c])
     c =+ 1
  for d in range(array_length):
    print(HeroList[d],HeroSum1[d])
    d =+ 1
