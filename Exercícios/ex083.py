contparenteseabre = contparentesefecha = 0
expressao = str(input('Digite uma expressão: ')).replace('', ' ').split()
for v in expressao:
    if '(' in v:
        contparenteseabre += 1
    if ')' in v:
        contparentesefecha += 1
if contparentesefecha == contparenteseabre:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
