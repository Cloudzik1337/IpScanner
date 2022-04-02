import os,requests,sys,ctypes,subprocess

SCRIPTNAME = os.path.basename(__file__)
FILENAME = 'scanner.py'
PATH = 'C:\Windows\System32'
os.system('cls')
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if not isAdmin():
    print('\u001b[31m[-] Error Run {} as administrator\u001b[0m'.format(SCRIPTNAME))
    quit()

print('[+] Getting Script')
script = requests.get('https://raw.githubusercontent.com/Cloudzik1337/IpScanner/main/scanner.py')
if script.status_code == 200:
    print('[+] Got Script')
else:
    sys.exit(1)
print('[+] Saving as {}'.format(FILENAME))
with open(FILENAME, 'a+') as file:
    file.write(script.text.replace('\n', ''))
    print('[+] Saved Succesyfully.')
print('[+] Moving {} to {}'.format(FILENAME, PATH))
os.popen('move {} {}'.format(FILENAME, PATH))
if os.path.exists('scanner.py'):
    print('\u001b[42m[+] Installed Succesyfully.\u001b[0m')
    print('[+] Now you can use scanner -s')