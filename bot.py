from threading import Thread
from selenium.webdriver import Chrome
from time import sleep

""""
Сюда нужно вводить ваши данные эмейл и пароль, примерно так:
data_user = {'mygmail1': 'mypassword',
             'mygmail2': 'mypassword',
             'mygmail3': 'mypassword',
             'mygmail4': 'mypassword',
             'mygmail5': 'mypassword',}
Вводите нужное вам количество акаунтов
"""
data_user = {'эмейл': 'пароль',
             'эмейл': 'пароль',
             'эмейл': 'пароль'}


def my_bot(email, password):
    while True:
        # browser = Chrome(os.path.join(os.getcwd(), 'chromedriver')) Ubuntu
        browser = Chrome('chromedriver')
        try:
            # Авторизация на сайте
            link = 'http://freelikes.online/'
            browser.get(link)
            browser.set_window_size(500, 800)
            sleep(5)
            next_page = browser.find_elements_by_xpath('//*[@id="uLogin"]/a[3]')
            browser.get(next_page[0].get_attribute('href'))
            sleep(5)
            auz = browser.find_element_by_id('identifierId')
            auz.send_keys(email)  # Ваш эмейл в gmail
            sleep(5)
            browser.find_element_by_id('identifierNext').click()
            sleep(5)
            auz = browser.find_elements_by_name('password')[0]
            auz.send_keys(password)  # Ваш пароль в gmail
            browser.find_element_by_id('passwordNext').click()
            sleep(5)

            my_window = browser.current_window_handle
            stop = True
            iteration = 0
            while iteration < 10:
                iteration += 1
                sleep(10)
                # Заработок на подписках
                browser.get('http://freelikes.online/earn/youtube/ytsub')
                sleep(2)
                print(email, ': Подписка страниц')
                while stop:
                    points = browser.find_element_by_xpath(
                        "//*[@class='do do-task btn btn-primary btn-block']").text
                    sleep(2)
                    points = points.replace('баллов', '').replace(' ', '')
                    if int(points) < 4:
                        break
                    browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").click()
                    sleep(3)
                    browser.switch_to.window(browser.window_handles[1])
                    browser.set_window_size(300, 400)
                    sleep(3)
                    trust = browser.find_element_by_xpath(
                        "//*[@class='style-scope ytd-subscribe-button-renderer']").text
                    trust = str(trust).lower()
                    if 'вы подписаны' in trust or 'підписалися' in trust:
                        print(email, ': Вы подписаны')
                        sleep(2)
                        browser.find_element_by_xpath(
                            "//*[@class='style-scope ytd-subscribe-button-renderer']").click()
                        try:
                            sleep(2)
                            title = browser.find_element_by_xpath(
                                "/html/body/ytd-app/ytd-popup-container/paper-dialog").text
                            sleep(2)
                            if 'ошибка' in str(title).lower() or 'жаль' in str(title).lower():
                                print(email, ':Ограничение по подпискам')
                                stop = False
                                sleep(2)
                                browser.close()
                                browser.switch_to.window(my_window)
                                break
                        except Exception as a:
                            pass
                        sleep(2)
                        browser.find_element_by_xpath(
                            "//*[@class='style-scope yt-button-renderer style-blue-text size-default']").click()
                        sleep(2)
                        browser.find_element_by_xpath(
                            "//*[@class='style-scope ytd-subscribe-button-renderer']").click()
                        sleep(2)
                        print(email, ':Переподписались +', points)
                    else:
                        browser.find_element_by_xpath(
                            "//*[@class='style-scope ytd-subscribe-button-renderer']").click()
                        sleep(2)
                        try:
                            sleep(2)
                            title = browser.find_element_by_xpath(
                                "/html/body/ytd-app/ytd-popup-container/paper-dialog").text
                            sleep(2)
                            if 'ошибка' in str(title).lower() or 'жаль' in str(title).lower():
                                print(email, ':Ограничение по подпискам')
                                stop = False
                                sleep(2)
                                browser.close()
                                browser.switch_to.window(my_window)
                                break
                        except Exception as a:
                            pass
                        print(email, ':Подписались +', points)
                    sleep(10)
                    browser.close()
                    browser.switch_to.window(my_window)
                    sleep(3)
                    browser.refresh()
                    sleep(4)

                sleep(10)
                browser.get('http://freelikes.online/earn/youtube/ytlike')
                sleep(3)
                print(email, ':Лайки')
                # Заработок на Лайках
                while True:
                    points = browser.find_element_by_xpath(
                        "//*[@class='do do-task btn btn-primary btn-block']").text
                    points = int(points.replace('баллов', '').replace(' ', ''))
                    if points < 3:
                        print(email, ':Закончил Лайкать')
                        break
                    browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").click()
                    sleep(3)
                    browser.switch_to.window(browser.window_handles[1])
                    browser.set_window_size(300, 400)
                    sleep(4)
                    try:
                        browser.find_element_by_xpath(
                            '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
                        print(email, ':Лайкнул запись +', points)
                        sleep(10)
                    except Exception as a:
                        print(email, ':129: ', a)
                    browser.close()
                    browser.switch_to.window(my_window)
                    sleep(3)
                    browser.refresh()
                    sleep(4)

                sleep(10)
                browser.get('http://freelikes.online/earn/youtube/ytview')
                sleep(3)
                print(email, ':Просмотры')
                # Заработок на Просмотрах
                while True:
                    points = browser.find_element_by_xpath(
                        "//*[@class='do do-task btn btn-primary btn-block']").text
                    points = int(points.replace('баллов', '').replace(' ', ''))
                    if points < 3:
                        print(email, ':Закончил просмотр')
                        break
                    browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").click()
                    sleep(3)
                    browser.switch_to.window(browser.window_handles[1])
                    browser.set_window_size(300, 400)
                    sleep(35)
                    print(email, ':Посмотрел видео +', points)
                    browser.close()
                    browser.switch_to.window(my_window)
                    sleep(3)
                    browser.refresh()
                    sleep(4)
        except Exception as a:  # Это говно-код на случай непредвиденных обстоятельств
            print(email, ':171: ', a)
            browser.close()

        try:  # А это вообще жопа
            browser.close()
        except Exception as a:
            print(email, ':179: ', a)


class DownloadThread(Thread):
    def __init__(self, email, password):
        Thread.__init__(self)
        self.email = email
        self.password = password

    def run(self):
        my_bot(email, password)


if __name__ == "__main__":
    for email, password in data_user.items():
        print('Start bot: ', email)
        thread = DownloadThread(email, password)
        thread.start()
