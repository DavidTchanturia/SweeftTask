import requests
import sqlite3

conn = sqlite3.connect('link.sqlite')
cursor = conn.cursor()


def is_valid(url):
    response = requests.get(url)
    return response.status_code


def check_in_database(url):
    cursor.execute("SELECT * FROM link WHERE raw_link=:r", {'r': url})
    ans = len(cursor.fetchall())
    if ans >= 1:
        return True
    else:
        return False

premium_or_not = input('do you want custom link? (y/n): ')


if premium_or_not == 'n':
    url = input("please put your url here: ")
    if is_valid(url) != 200 or len(url) <= 250:
        key = '3fca14a6e2ed1a947e49109a99f5fdb5a85a7'
        api_url = f"https://cutt.ly/api/api.php?key={key}&short={url}"
        result = requests.get(api_url).json()['url']
        if check_in_database(url):
            cursor.execute("SELECT * FROM link WHERE raw_link=:r", {'r': url})
            link = cursor.fetchone()
            print(link[2])
        else:
            final_link = result['shortLink']
            cursor.execute("INSERT INTO link(raw_link, short_link) VALUES (?, ?)", (url, final_link))
            conn.commit()
            print(final_link)
    else:
        print('your link is invalid')

elif premium_or_not == 'y':
    try:
        url = input("please put your url here: ")
        if is_valid(url) == 200 and len(url) <= 250:
            name = input("please put your custom name for the link: ")
            key = '3fca14a6e2ed1a947e49109a99f5fdb5a85a7'
            api_url = f"https://cutt.ly/api/api.php?key={key}&short={url}&name={name}"
            result = requests.get(api_url).json()['url']
            final_link = result['shortLink']
            cursor.execute("INSERT INTO link(raw_link, short_link) VALUES (?, ?)", (url, final_link))
            conn.commit()
            print(final_link)
        else:
            print('your link is invalid')
    except KeyError:
        print("link with this name already exists")

conn.close()



