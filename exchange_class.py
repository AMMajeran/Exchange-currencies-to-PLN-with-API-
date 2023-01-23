import requests

class Exchange:
    """A class created for converting currencies into Polish zlotys 
    and displaying the current exchange rate according to the National Bank of Poland"""
    
    def __init__(self, currency=input("Podaj kod waluty, którą chcesz wymienić (EUR/CHF/USD itd): "), amount=int(input("Podaj w cyfrach kwotę, jaką chcesz przeliczyć: "))):
        self.currency = currency
        self.amount = amount 
        

    def calculate(self):
        """Displays the amount of PLN after exchanging a certain amount of the selected currency"""

        url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
        r = requests.get(url)
        print(f"Code status: {r.status_code}")

        currencies_table = r.json()
         
        for rate in currencies_table[0]['rates']:
            if self.currency == rate['code']:
                result = self.amount * round(rate['mid'], 2)
                print('*' * 10)
                print(f"Po wymianie otrzymasz {result} PLN")
                print('\n' + '*' * 10)
                break 
    

    def display_rate(self):
        """Displays the current exchange rate as indicated by the National Bank of Poland"""

        url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
        r = requests.get(url)
        # print(f"Code status: {r.status_code}")

        currencies_table= r.json()
         
        for rate in currencies_table[0]['rates']:
            if self.currency == rate['code']:
                result = (rate['mid'])
                print(f"Kurs {self.currency} to {result}")
                break 

