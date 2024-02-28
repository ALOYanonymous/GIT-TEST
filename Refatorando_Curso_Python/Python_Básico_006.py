omnitrix = ['HeatBlast', 'Four Arms', 'DiamondHead', 'XLR8', 'GhostFreak']
print(omnitrix)
prototype_omnitrix = ('SwampFire', 'Humungousaur', 'Brainstorm', 'Echo Echo', 'Big Chill')
print(prototype_omnitrix)

aliens1 = 'Upgrade'
omnitrix[1] = aliens1
print(omnitrix)

aliens2 = ['Four Arms', 'RipJaws']
omnitrix.extend(aliens2)
print(omnitrix)

aliens3 = 'Wildmutt'
aliens4 = 'StinkFly'
omnitrix.append(aliens4)
omnitrix.insert(8, aliens3)
print(omnitrix)

delet = omnitrix.pop()
#omnitrix.remove('Four Arms')
#omnitrix.clear()
print(delet)

indice = omnitrix.index('XLR8')
print(indice)

quantidade = omnitrix.count('Four Arms')
print(quantidade)

idade = [70, 10, 12]
print(idade)

idade.reverse()
print(idade)

idade.sort()
print(idade)

idade.reverse()
print(idade)

omnitrix_albedo = omnitrix.copy
omnitrix.remove('HeatBlast')
print(omnitrix_albedo)