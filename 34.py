#
def notas(*num, sit):
   r = dict()
   r['total'] = len(num)
   r['maior'] = max(num)
   r['menor'] = min(num)
   r['media'] = sum(num)/len(num)
   return r
#    if sit:
#       if r['media'] >= 7:
#          r['situaçao'] = 'BOA'
#       elif r['media'] >= 5:
#          r['situaçao'] = 'RAZOAVEL'
#       else:
#          r['situaçao'] = 'RUIM'
#     return r
resp = notas(5, 6, 5, sit=True)
print(resp)