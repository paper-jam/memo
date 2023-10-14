import lxml

# ------- starting a web server in one line
# python -m http.server



# -- ===== HTML : récupération de valeur selon clé XPATH
from lxml import etree

html = requests.get(url).text
dom = etree.HTML(html)
valeur = dom.xpath('/html/body/div[6]/div[2]/div[1]/p[4]')


