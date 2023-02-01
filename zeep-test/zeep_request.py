from zeep import Client

# client = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')
# result = client.service.NumberToWords(100)
# print(result)


# wsdl_url = "http://www.dneonline.com/calculator.asmx?wsdl"
# client = Client(wsdl=wsdl_url)
# result = client.service.Subtract(100, 90)
# print(result)

wsdl_url = "http://www.dneonline.com/calculator.asmx?wsdl"
client = Client(wsdl=wsdl_url)
data = {"intA": 6, "intB": 3}
result = client.service.Subtract(**data)
print(result)


