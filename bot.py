from selenium.webdriver import Chrome
from time import sleep

while True:
    # browser = Chrome(os.path.join(os.getcwd(), 'chromedriver')) Ubuntu
    browser = Chrome('chromedriver')
    try:
        # Авторизация на сайте
        link = 'http://freelikes.online/'
        browser.get(link)
        browser.set_window_size(300, 400)
        sleep(5)
        next_page = browser.find_elements_by_xpath('//*[@id="uLogin"]/a[3]')
        browser.get(next_page[0].get_attribute('href'))
        sleep(5)
        auz = browser.find_element_by_id('identifierId')
        auz.send_keys('')  # Ваш эмейл в gmail
        sleep(5)
        browser.find_element_by_id('identifierNext').click()
        sleep(5)
        auz = browser.find_elements_by_name('password')[0]
        auz.send_keys('')  # Ваш пароль в gmail
        browser.find_element_by_id('passwordNext').click()
        sleep(5)

        my_window = browser.current_window_handle
        stop = True

        for abq in range(10):
            sleep(10)
            # Заработок на подписках
            browser.get('http://freelikes.online/earn/youtube/ytsub')
            sleep(2)
            print('Подписка страниц')
            while stop:
                points = browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").text
                sleep(2)
                points = points.replace('баллов', '').replace(' ', '')
                if int(points) < 4:
                    break
                browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").click()
                sleep(3)
                browser.switch_to.window(browser.window_handles[1])
                browser.set_window_size(300, 400)
                sleep(3)
                trust = browser.find_element_by_xpath("//*[@class='style-scope ytd-subscribe-button-renderer']").text
                trust = str(trust).lower()
                if 'вы подписаны' in trust or 'підписалися' in trust:
                    print('Вы подписаны')
                    sleep(2)
                    browser.find_element_by_xpath("//*[@class='style-scope ytd-subscribe-button-renderer']").click()
                    try:
                        sleep(2)
                        title = browser.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/paper-dialog").text
                        sleep(2)
                        if 'ошибка' in str(title).lower() or 'жаль' in str(title).lower():
                            print('Ограничение по подпискам')
                            stop = False
                            sleep(2)
                            browser.close()
                            browser.switch_to.window(my_window)
                            break
                    except Exception as a:
                        print('71: ', a)
                    sleep(2)
                    browser.find_element_by_xpath(
                        "//*[@class='style-scope yt-button-renderer style-blue-text size-default']").click()
                    sleep(2)
                    browser.find_element_by_xpath("//*[@class='style-scope ytd-subscribe-button-renderer']").click()
                    sleep(2)
                    print('Переподписались +', points)
                else:
                    browser.find_element_by_xpath("//*[@class='style-scope ytd-subscribe-button-renderer']").click()
                    sleep(2)
                    try:
                        title = browser.find_element_by_xpath(
                            "/html/body/ytd-app/ytd-popup-container/paper-dialog").text
                        sleep(2)
                        if 'ошибка' in str(title).lower() or 'жаль' in str(title).lower():
                            print('Ограничение по подпискам')
                            stop = False
                            sleep(2)
                            browser.close()
                            browser.switch_to.window(my_window)
                            break
                    except Exception as a:
                        print('93: ', a)
                    print('Подписались +', points)
                sleep(10)
                browser.close()
                browser.switch_to.window(my_window)
                sleep(3)
                browser.refresh()
                sleep(4)

            sleep(10)
            browser.get('http://freelikes.online/earn/youtube/ytlike')
            sleep(3)
            print('Лайки')
            # Заработок на Лайках
            while True:
                points = browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").text
                points = int(points.replace('баллов', '').replace(' ', ''))
                if points < 3:
                    print('Закончил Лайкать')
                    break
                browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").click()
                sleep(3)
                browser.switch_to.window(browser.window_handles[1])
                browser.set_window_size(300, 400)
                sleep(4)
                try:
                    browser.find_element_by_xpath(
                        '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button').click()
                    print('Лайкнул запись +', points)
                    sleep(10)
                except:
                    try:
                        browser.find_element_by_xpath(
                            '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
                        print('Лайкнул запись +', points)
                        sleep(10)
                    except Exception as a:
                        print('129: ', a)
                browser.close()
                browser.switch_to.window(my_window)
                sleep(3)
                browser.refresh()
                sleep(4)

            sleep(10)
            browser.get('http://freelikes.online/earn/youtube/ytview')
            sleep(3)
            print('Просмотры')
            # Заработок на Просмотрах
            while True:
                points = browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").text
                points = int(points.replace('баллов', '').replace(' ', ''))
                if points < 3:
                    print('Закончил просмотр')
                    break
                browser.find_element_by_xpath("//*[@class='do do-task btn btn-primary btn-block']").click()
                sleep(3)
                browser.switch_to.window(browser.window_handles[1])
                browser.set_window_size(300, 400)
                sleep(35)
                print('Посмотрел видео +', points)
                browser.close()
                browser.switch_to.window(my_window)
                sleep(3)
                browser.refresh()
                sleep(4)
    except Exception as a:  # Это говно-код на случай непредвиденных обстоятельств
        print('171: ', a)
        browser.close()
        try:
            browser.close()
        except Exception as a:
            print('176: ', a)
    try:  # А это вообще жопа
        browser.close()
    except Exception as a:
        print('179: ', a)
