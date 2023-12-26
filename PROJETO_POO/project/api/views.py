'''teste = open('/home/jose/Documentos/IFRN_POO/projeto_poo_e/project/api/packets.json','r')
teste = teste.read()
print(teste)'''

from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def getData(request):
    with open('/home/jose/Documentos/IFRN_POO/projeto_poo_e/project/api/packets.json','r') as f:
        data = json.load(f)
    return Response(data)