import requests
from flask import Flask, render_template

# Base Url for geocoding
url = "https://us1.locationiq.com/v1/search.php"

# address = input("Input the address: ")

#Your unique private_token should replace value of the private_token variable.
#To know how to obtain a unique private_token please refer the README file for this script.
private_token = "pk.4e6c299ad699975acbb1eb49c8ca8a0c"

data = {
    'key': private_token,
    'q': address,
    'format': 'json'
}

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template ("geocode.html")

@app.route('/address_lookup')




response = requests.get(url, params=data)

latitude = response.json()[0]['lat']
print(f"The latitude of the given address is: {latitude}")

longitude = response.json()[0]['lon']
print(f"The longitude of the given address is: {longitude}")


print("Thanks for using this script")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')