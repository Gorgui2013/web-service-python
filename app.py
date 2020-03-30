from flask import Flask, render_template, request
from zeep import Client
import typing
import json

app = Flask(__name__)

client = Client(wsdl = 'http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')

@app.route('/', methods=['GET', 'POST'])
def index():

  fullInfos = client.service.FullCountryInfoAllCountries()
  if request.method == 'POST':
    for pay in fullInfos:
      if pay['sName'] == request.form.get('pay'):
        infos = pay
        langs = pay['Languages']

    return render_template('index.jinja2', infos = infos, langs = langs, fullInfos = fullInfos)

  return render_template('index.jinja2', infos='', langs = '', fullInfos = fullInfos)

if __name__=='__main__':
  app.run(debug=True)
