from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#função para pegar o trecho onde se encontra a informação
def get_json(url):
  try:
    resposta_http = urlopen(url)
  except HTTPError:
    return None
  try:
    html = BeautifulSoup(resposta_http.read(), features = "html.parser")
    dicionario = html.body.find("script", {"type":"text/javascript"})
    dicionario = dicionario.get_text()
  except AttributeError:
    return None
  return dicionario

#função para coletar o número
def get_followers_count(name):
  s = get_json("https://www.instagram.com/{}/".format(name))
  efb_index = s.find('"edge_followed_by":{"count":')
  dict_count = s[efb_index:efb_index+38]
  for i in dict_count:
    if(i=='}'):
      dict_count = dict_count[0:dict_count.index(i)+1]
      break
  count = [i for i in dict_count if i.isdigit()]
  count = ''.join(count)
  s = "O número de seguidores de @{0} é: {1}".format(name, count)
  return s