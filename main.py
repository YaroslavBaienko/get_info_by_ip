import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            '[IP]': response.get('query'),
            '[Org.]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Latitude]': response.get('lat'),
            '[Longitude]': response.get('lon')
        }
        for k, v in data.items():
            print(k, v)

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print("!!! CHECK YOUR CONNECTION FIRST !!!")


def main():
    pre_text = Figlet(font='slant')
    print(pre_text.renderText('IP ---> INFO'))
    ip = input("Input IP to check: ")
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
