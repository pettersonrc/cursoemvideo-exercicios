m = float(input('Escreva o valor em metros: '))
dm = m*10
cm = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000
print('Em kilômetros: {:.0f}km\nEm hectômetros: {:.0f}hm\nEm decâmetros {:.0f}dam\nEm metros: {:.0f}m\nEm decímetros {:.0f}dm\nEm centímetros {:.0f}cm\nEm milímetros {:.0f}mm'.format(km, hm, dam, m, dm, cm, mm))