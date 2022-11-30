import requests
# aaaa
dados = {
    'ctl00$ContentPlaceHolder1$dpdTipoBusca' : '0',
    'ctl00$ContentPlaceHolder1$txtValor' : '47472500852',
    'ctl00$ContentPlaceHolder1$btnPesquisar.x' : '3',
    'ctl00$ContentPlaceHolder1$btnPesquisar.y' : '9'
}
response = requests.get('http://srvaplic2.famema.br/ProcessoSeletivoDRH/Status.aspx')#, data=dados)


'''
POST /ProcessoSeletivoDRH/Status.aspx HTTP/1.1
Host: srvaplic2.famema.br
Connection: keep-alive
Content-Length: 1145
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
Origin: http://srvaplic2.famema.br
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://srvaplic2.famema.br/ProcessoSeletivoDRH/Status.aspx
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: ASP.NET_SessionId=i3stbhn4ml1iy3msdaqnzuzs; _ga=GA1.2.1045115149.1588119572; _gid=GA1.2.246877123.1588119572

'''