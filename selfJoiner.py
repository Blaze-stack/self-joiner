from gevent import killall
import undetected_chromedriver.v2 as uc
from time import sleep
from selenium import webdriver
from colorama import init, Fore
init(convert=True, autoreset=True)
def join(token, url):
    token = token
    url = url
    driver = uc.Chrome(use_subprocess=True)
    script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }
                """
    driver.get(url)
    driver.execute_script(script + f'\nlogin("{token}")')
    sleep(5)
    driver.get(url)
    sleep(3)
    print(Fore.GREEN + "Please do captcha, Then click enter.", end='')
    input()
    forp = url.replace('https://discord.gg/', '')
    print(Fore.YELLOW+"Joined server: "+ forp )
    killall()

if __name__ == '__main__':    
    print(Fore.GREEN + "Token: ", end='')
    token = input()
    print(Fore.GREEN + "Invite link: ", end='')
    url = input()
    join(token=token, url=url)
