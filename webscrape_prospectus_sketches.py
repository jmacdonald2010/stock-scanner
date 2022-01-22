from requests_html import HTMLSession

session = HTMLSession()
base = 'https://fundresearch.fidelity.com/prospectus/funds'
mf = ' Fidelity U.S. Sustainability Index Fund'

site = session.get(base)

site.html.render(sleep=120)

print(site.html.find('tr', containing=mf))