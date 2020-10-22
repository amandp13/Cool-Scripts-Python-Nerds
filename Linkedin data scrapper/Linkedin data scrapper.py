from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.chrome.chrome_profile import ChromeProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Proxy
from base64 import b64encode
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import numpy as np
import scipy.interpolate as si
import time
import pandas as pd
import unidecode
import re

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import zipfile,os
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def proxy_chrome(PROXY_HOST,PROXY_PORT,PROXY_USER,PROXY_PASS):
    manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy",
                    "tabs",
                    "unlimitedStorage",
                    "storage",
                    "<all_urls>",
                    "webRequest",
                    "webRequestBlocking"
                ],
                "background": {
                    "scripts": ["background.js"]
                },
                "minimum_chrome_version":"22.0.0"
            }
            """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "%(host)s",
                port: parseInt(%(port)d)
              },
              bypassList: ["foobar.com"]
            }
          };
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%(user)s",
                password: "%(pass)s"
            }
        };
    }
    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
        """ % {
            "host": PROXY_HOST,
            "port": PROXY_PORT,
            "user": PROXY_USER,
            "pass": PROXY_PASS,
        }


    pluginfile = 'extension\\proxy_auth_plugin.zip'

    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    co = Options()
    # extension support is not possible in incognito mode for now
    # co.add_argument('--incognito')
    co.add_argument('--disable-gpu')
    # disable infobars
    co.add_argument('--disable-infobars')
    co.add_argument("--start-maximized")
    ua = UserAgent()
    userAgent = ua.random
    co.add_argument('--user-agent="' + str(userAgent) + '"')
    co.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    # location of chromedriver, please change it according to your project.
    chromedriver = os.getcwd()+'\\Chromedriver\\chromedriver.exe'
    co.add_extension(pluginfile)
    driver = webdriver.Chrome(chromedriver,chrome_options=co)
    # return the driver with added proxy configuration.
    return driver


def switch_proxy(old_driver, port=5432, user="ffvpa", pwd="y4qdttpy"):
    old_driver.get("http://www.icanhazip.com/")
    ip = old_driver.find_element_by_xpath("html").text
    proxies = {"199.30.48.16": "199.30.48.254",
               "199.30.48.254": "199.30.49.52",
               "199.30.49.52": "199.30.48.16"}
    ip = proxies[ip]
    old_driver.close()
    new_driver = proxy_chrome(ip, port, user, pwd)
    return new_driver


def test_email(email):
    driver.get("http://mailtester.com")
    content = driver.find_element_by_id('content')
    email_input = content.find_element_by_xpath('./form/table/tbody/tr/td/input')
    email_input.clear()
    email_input.send_keys(email)
    email_input.submit()

    time.sleep(5)

    try:
        content = driver.find_element_by_id('content')
        domain = content.find_element_by_xpath('./table/tbody/tr[3]/td[5]').get_attribute('bgcolor')
        if domain == '#FF4444':
            return "Domain Invalid"
        address_color = content.find_element_by_xpath('./table/tbody/tr[5]/td[5]').get_attribute('bgcolor')
        address_text = content.find_element_by_xpath('./table/tbody/tr[5]/td[5]').text
    except StaleElementReferenceException:
        content = driver.find_element_by_id('content')
        domain = content.find_element_by_xpath('./table/tbody/tr[3]/td[5]').get_attribute('bgcolor')
        if domain == '#FF4444':
            return "Domain Invalid"
        address_color = content.find_element_by_xpath('./table/tbody/tr[5]/td[5]').get_attribute('bgcolor')
        address_text = content.find_element_by_xpath('./table/tbody/tr[5]/td[5]').text
    except NoSuchElementException: 
        time.sleep(10)
        content = driver.find_element_by_id('content')
        domain = content.find_element_by_xpath('./table/tbody/tr[3]/td[5]').get_attribute('bgcolor')
        if domain == '#FF4444':
            return "Domain Invalid"
        address_color = content.find_element_by_xpath('./table/tbody/tr[5]/td[5]').get_attribute('bgcolor')
        address_text = content.find_element_by_xpath('./table/tbody/tr[5]/td[5]').text

    if domain == address_color == '#00DD00':
        return "Verified"
    if domain == '#00DD00' and address_color == '#FFBB00':
        if 'status code: 450' in address_text:
            return "Verified"
        if address_text == "Server doesn't allow e-mail address verification":
            return "Unverified"
    return "Invalid"




email_types = {"Firstname": 0,
               "Firstname.Lastname": 0,
               "Firstname_Lastname": 0,
               "FirstnameLastinitial": 0,
               "FirstinitialLastinitial": 0,
               "Lastname.Firstname": 0,
               "Lastname_Firstname": 0,
               "FirstinitialLastname": 0,
               "Firstinitial.Lastname": 0,
               "LastnameFirstinitial": 0,
               "Lastname.Firstinitial": 0,
               "Firstinitial": 0,
               "FirstnameLastname": 0}


def test_startup(startup):
    if startup["Startup Domain"] != "No Domain Found" and startup["Startup Domain"] != "":
        for num, rec in enumerate(startup["Recruiter(s)"]):
            print(rec)
            added = False
            if not rec:
                continue
            name = rec
            if "(" in name:
                name = name.split("(")[0].strip()
            if len(name.split()) < 2:
                continue
            first = unidecode.unidecode(name.split()[0].lower().replace("'", ""))
            last = unidecode.unidecode(name.split()[-1].lower().replace("'", ""))
            titl = startup["Title(s)"][num]
            if last == '' and unidecode.unidecode(name.split()[-2].lower().replace("'", "")) != first:
                last = unidecode.unidecode(name.split()[-2].lower().replace("'", ""))
            try:
                first_only = test_email(first + '@' + startup["Startup Domain"])
            except NoSuchElementException:
                first_only = test_email(first + '@' + startup["Startup Domain"])
            if first_only == "Unverified":
                keep_all(startup, status="Unverified")
                break
            elif first_only == "Domain Invalid":
                add_email(startup, first, last, "No Valid Email Found", "N/A", titl)
                continue
            elif first_only == "Verified":
                add_email(startup, first, last, first + '@' + startup["Startup Domain"], "Verified", titl)
                email_types["Firstname"] += 1
                added = True
            if test_email(first + '.' + last + '@' + startup["Startup Domain"]) == "Verified":
                add_email(startup, first, last, first + '.' + last + '@' + startup["Startup Domain"], "Verified", titl)
                email_types["Firstname.Lastname"] += 1
                added = True
            if test_email(first + '_' + last + '@' + startup["Startup Domain"]) == "Verified":
                add_email(startup, first, last, first + '_' + last + '@' + startup["Startup Domain"], "Verified", titl)
                email_types["Firstname_Lastname"] += 1
                added = True
             if test_email(first + last[0] + '@' + startup["Startup Domain"]) == "Verified":
               add_email(startup, first, last, first + last[0] + '@' + startup["Startup Domain"], "Verified")
                 email_types["FirstnameLastinitial"] += 1
                 continue
             if test_email(first[0] + last[0] + '@' + startup["Startup Domain"]) == "Verified":
                 add_email(startup, first, last, first[0] + last[0] + '@' + startup["Startup Domain"], "Verified")
                 email_types["FirstinitialLastinitial"] += 1
                 continue
            # if test_email(last + '.' + first + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, last + '.' + first + '@' + startup["Startup Domain"], "Verified")
            #     email_types["Lastname.Firstname"] += 1
            #     continue
            # if test_email(last + '_' + first + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, last + '_' + first + '@' + startup["Startup Domain"], "Verified")
            #     email_types["Lastname_Firstname"] += 1
            #     continue
            # if test_email(first[0] + last + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, first[0] + last + '@' + startup["Startup Domain"], "Verified")
            #     email_types["FirstinitialLastname"] += 1
            #     continue
            # if test_email(first[0] + '.' + last + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, first[0] + '.' + last + '@' + startup["Startup Domain"], "Verified")
            #     email_types["Firstinitial.Lastname"] += 1
            #     continue
            # if test_email(last + first[0] + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, last + first[0] + '@' + startup["Startup Domain"], "Verified")
            #     email_types["Lastname.Firstinitial"] += 1
            #     continue
            # if test_email(last + '.' + first[0] + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, last + '.' + first[0] + '@' + startup["Startup Domain"], "Verified")
            #     email_types["Lastname.Firstinitial"] += 1
            #     continue
            # if test_email(first[0] + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, first[0] + '@' + startup["Startup Domain"], "Verified")
            #     email_types["Firstinitial"] += 1
            #     continue
            # if test_email(first + last + '@' + startup["Startup Domain"]) == "Verified":
            #     add_email(startup, first, last, first + last + '@' + startup["Startup Domain"], "Verified")
            #     email_types["FirstnameLastname"] += 1
            #     continue
            if not added:
                add_email(startup, first, last, "No Valid Email Found", "N/A", titl)
    else:
        for rec in startup["Recruiter(s)"]:
            first = unidecode.unidecode(rec.split()[0].lower().replace("'", ""))
            last = unidecode.unidecode(rec.split()[-1].lower().replace("'", ""))
            add_email(startup, first, last, "No Valid Email Found", "N/A", "N/A")


def move_mouse(driver, points, startElement):
    # Curve base:

    #
    # points = [[0, 0], [0, 2], [2, 3], [4, 0], [6, 3], [8, 2], [8, 0]]
    # for x in points:
    #     x[0] += np.random.normal()
    #     x[1] += np.random.normal()
    # points = np.array(points)

    x = points[:, 0]
    y = points[:, 1]

    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)

    x_tup = si.splrep(t, x, k=3)
    y_tup = si.splrep(t, y, k=3)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    x_i = si.splev(ipl_t, x_list)  # x interpolate values
    y_i = si.splev(ipl_t, y_list)  # y interpolate values

    # url = "https://codepen.io/falldowngoboone/pen/PwzPYv"
    # driver = webdriver.Chrome(executable_path=os.getcwd()+'\\Chromedriver\\chromedriver.exe')
    # driver.get(url)

    action = ActionChains(driver)
    #
    # try:
    #     startElement = driver.find_element_by_xpath("//div")
    # except NoSuchElementException:
    #     raise Exception("HTML Structure Changed on iteration " + str(n))



    # First, go to your start point or Element:
    action.move_to_element(startElement)
    try:
        action.perform()
    except MoveTargetOutOfBoundsException:
        print("wtf")

    for n, xy in enumerate(zip(x_i, y_i)):
        mouse_x, mouse_y = xy
        if n > 0:
            mouse_x -= x_i[n - 1]
            mouse_y -= y_i[n - 1]
        action.move_by_offset(mouse_x, mouse_y)
        # print(mouse_x, mouse_y)
        # try:
        #     action.perform()
        # # print(mouse_x, mouse_y)
        # except MoveTargetOutOfBoundsException:
        #     print(mouse_x, mouse_y)
    action.click()
    action.perform()


r_words = pd.read_csv("random_words.csv").drop_duplicates()
#r_phrases = pd.read_csv("random_phrases.csv").drop_duplicates()[::2].reset_index(drop=True)
#r_sents = pd.read_csv("random_sentences.csv").drop_duplicates()
#randos = pd.concat([r_words, r_phrases, r_sents]).reset_index(drop=True)


def do_random_search():
    driver.get("https://google.com/")

    try:
        search_box = driver.find_element_by_class_name("gLFyf.gsfi")
    except NoSuchElementException:
        try:
            search_box = driver.find_elements_by_xpath("//input[@class='lst']")[0]
        except IndexError:
            switch_proxy(driver)
            driver.get("https://google.com/")

            try:
                search_box = driver.find_element_by_class_name("gLFyf.gsfi")
            except NoSuchElementException:
                try:
                    search_box = driver.find_elements_by_xpath("//input[@class='lst']")[0]
                except IndexError:
                    raise Exception("bad html on iteration {}".format(x))

    search_box.send_keys(np.random.choice(randos["Phrases"]))
    time.sleep(5)
    suggestions = driver.find_elements_by_class_name("sbtc")
    suggestions.extend(driver.find_elements_by_class_name("gNO89b"))
    suggestions.extend(driver.find_elements_by_xpath("//tr[@class='mssb_e']"))
    if not suggestions:
        suggestions.extend(driver.find_elements_by_class_name("gssb_i"))
        suggestions.append(driver.find_elements_by_xpath("//input[@value='Google Search']")[0])
    suggestion = np.random.choice(suggestions)
    search_rect = search_box.rect
    sugg_rect = suggestion.rect
    mouse_start_x = np.random.uniform(search_rect["x"], search_rect["x"] + search_rect["width"])
    mouse_start_y = np.random.uniform(search_rect["y"], search_rect["y"] + search_rect["height"])
    mouse_mid_x1 = np.random.uniform(search_rect["x"], sugg_rect["x"] + sugg_rect["width"])
    mouse_mid_y1 = np.random.uniform(search_rect["y"], sugg_rect["y"] + sugg_rect["height"])
    mouse_mid_x2 = np.random.uniform(search_rect["x"], sugg_rect["x"] + sugg_rect["width"])
    mouse_mid_y2 = np.random.uniform(search_rect["y"], sugg_rect["y"] + sugg_rect["height"])
    mouse_mid_x3 = np.random.uniform(search_rect["x"], sugg_rect["x"] + sugg_rect["width"])
    mouse_mid_y3 = np.random.uniform(search_rect["y"], sugg_rect["y"] + sugg_rect["height"])
    mouse_end_x = np.random.uniform(sugg_rect["x"], sugg_rect["x"] + sugg_rect["width"])
    mouse_end_y = np.random.uniform(sugg_rect["y"], sugg_rect["y"] + sugg_rect["height"])
    # mouse_start_x = np.random.uniform(0, 30)
    # mouse_start_y = np.random.uniform(0, 30)
    # mouse_mid_x1 = np.random.uniform(0, 30)
    # mouse_mid_y1 = np.random.uniform(0, 30)
    # mouse_mid_x2 = np.random.uniform(0, 30)
    # mouse_mid_y2 = np.random.uniform(0, 30)
    # mouse_mid_x3 = np.random.uniform(0, 30)
    # mouse_mid_y3 = np.random.uniform(0, 30)
    # mouse_end_x = np.random.uniform(0, 30)
    # mouse_end_y = np.random.uniform(0, 30)

    xs = [mouse_start_x, mouse_mid_x1, mouse_mid_x2, mouse_mid_x3, mouse_end_x]
    ys = [mouse_start_y, mouse_mid_y1, mouse_mid_y2, mouse_mid_y3, mouse_end_y]

    points = np.array(list(zip(xs, ys)))
    points[:, 0] -= search_rect["x"]
    points[:, 1] -= search_rect["y"]

    move_mouse(driver, points, search_box)

    wait = np.abs(np.random.normal(40, 10))
    time.sleep(wait)
    # TODO random choice of possibly mouse movement to click on a link


def do_random_searches():
    num = np.random.randint(3)
    for search in np.arange(num):
        do_random_search()


def get_garys_comps():
    driver = proxy_chrome("199.30.48.16", 5432, "ffvpa", "y4qdttpy")
    # driver = switch_proxy(driver)
    # driver.get("http://www.icanhazip.com/")
    # driver.get("https://www.whatsmyua.info/")

    driver.get("https://www.garysguide.com/jobs?region=newyork")

    companies = driver.find_elements_by_xpath("//b")
    companies = [comp.text for comp in companies]
    # TODO verify that this remains correct over time
    # TODO exclude already scraped companies
    comp_names = list(set(companies[5::2]))

    pd.Series(comp_names).to_excel("garysguide_comp_names_9_6_19.xlsx")
    comp_names = list(pd.read_excel("garysguide_comp_names_9_6_19.xlsx")[0])
    return comp_names


def get_builtinnyc_comps():
    driver = proxy_chrome("199.30.48.16", 5432, "ffvpa", "y4qdttpy")
    # driver = switch_proxy(driver)
    # driver.get("http://www.icanhazip.com/")
    # driver.get("https://www.whatsmyua.info/")

    driver.get("https://www.builtinnyc.com/jobs")
    comp_names = set()

    for n in np.arange(120):
        companies = driver.find_elements_by_class_name("company-title")
        companies = [comp.text for comp in companies]
        comp_names = comp_names.union(set(companies))

        time.sleep(10)

        next_button = driver.find_element_by_class_name("pager__item.pager__item--next")
        next_button.click()

    master_comp_names = set(pd.read_excel("garysguide_comp_names_9_6_19.xlsx")[0].str.lower())
    comp_names = set(pd.Series(list(comp_names)).str.lower())
    comp_names = comp_names.difference(master_comp_names)

    comp_names = list(comp_names)

    pd.Series(comp_names).to_excel("builtnyc_comp_names_9_17_19.xlsx")
    return comp_names


def get_simply_hired_comps():
    driver = proxy_chrome("199.30.48.16", 5432, "ffvpa", "y4qdttpy")
    # driver = switch_proxy(driver)
    # driver.get("http://www.icanhazip.com/")
    # driver.get("https://www.whatsmyua.info/")

    queries = ["social+media+marketing", "digital+marketing"]
    query = queries[1]
    driver.get("https://www.simplyhired.com/search?q={}&l=New+York%2C+NY&job=BF_hTXJ3Jax-IMaIu-_t4Fb0RFLI8XvjZ4tvSYVtdSx39H3J6qHHTA".format(query))
    comp_names = set()

    for n in np.arange(100):
        companies = driver.find_elements_by_class_name("jobposting-company")
        companies = [comp.text.lower() for comp in companies]
        comp_names = comp_names.union(set(companies))

        time.sleep(10)

        next_button = driver.find_element_by_class_name("next-pagination")
        next_button.click()

    master_comp_names = set(pd.read_excel("builtnyc_comp_names_9_17_19.xlsx")[0].str.lower())
    comp_names = set(pd.Series(list(comp_names)).str.lower())
    comp_names = comp_names.difference(master_comp_names)

    comp_names = list(comp_names)

    pd.Series(comp_names).to_excel("simplyhired_comp_names_9_24_19.xlsx")
    return comp_names
def start_random_proxy():
    rando = np.random.randint(2)
    if rando == 0:
        driver = proxy_chrome("199.30.48.16", 5432, "ffvpa", "y4qdttpy")
    elif rando == 1:
        driver = proxy_chrome("199.30.48.254", 5432, "ffvpa", "y4qdttpy")
    else:
        driver = proxy_chrome("199.30.49.52", 5432, "ffvpa", "y4qdttpy")
    time.sleep(5)
    return driver

def get_venture_loop_comps():
    driver = start_random_proxy()

    driver.get("https://www.ventureloop.com/ventureloop/job_search.php?g=1&jcat=%&ldata=New%20York%20City,%20NY,%20US&jt=1&jc=1&jd=1&fb=1&d=5&btn=1")
    page_tot = int(driver.find_element_by_class_name("pag_txt_tot").text)
    comp_names = []
    for n in np.arange(page_tot):
        time.sleep(10)
        jobs = driver.find_elements_by_xpath("//tbody/tr")

        comps = [job.find_element_by_xpath('./td[3]/a').text for job in jobs[1:]]
        comp_names.extend(comps)
        next = driver.find_elements_by_class_name("nav.pagnav")
        ind = 0
        for x in next:
            if x.text == '›':
                break
            else:
                ind += 1
        if n < page_tot - 1:
            next[ind].click()
    return list(set(comp_names))


comp_names = get_venture_loop_comps()
comp_names = pd.Series(comp_names)
comp_names.to_excel("venture_loop_10_7_19.xlsx")
# comp_names = pd.read_excel("venture_loop_10_7_19.xlsx")[0]

bad_domains = []





driver = start_random_proxy()

# went through 638 of Simply Hired comp_names

x = 0
while x < len(comp_names):
    try:
        driver = switch_proxy(driver)

        do_random_searches()

        search = "site:www.linkedin.com AND inurl:linkedin.com/pub/ OR inurl:linkedin.com/in/ {} recruiter&num=20"

        driver.get("https://www.google.com/search?q={}".format(search.format(comp_names[x])))

        # TODO add check to avoid already scraped leads

        people = driver.find_elements_by_class_name("ellip")
        people.extend(driver.find_elements_by_xpath("//h3"))
        people.extend(driver.find_elements_by_class_name("BNeawe.vvjwJb.AP7Wnd"))
        people.extend(driver.find_elements_by_class_name("fuLhoc"))
        people = [result.text for result in people]

        if not people:
            raise Exception("HTML Structure Changed people search on iteration " + str(x))

        if len(people) < 5:
            x -= 1
            continue

        # move_mouse(driver, x)

        time.sleep(np.abs(np.random.normal(30, 10)))

        do_random_searches()

        # TODO add several random mouse movements
        # TODO add several safe clicks

        comp_names[x] = comp_names[x].replace("#", "")
        driver.get("https://www.google.com/search?q={}".format(comp_names[x]))
        domains = driver.find_elements_by_class_name("iUh30")
        domains.extend(driver.find_elements_by_class_name("hJND5c"))
        domains.extend(driver.find_elements_by_class_name("BNeawe.UPmit.AP7Wnd"))
        domains.extend(driver.find_elements_by_class_name("fYyStc"))
        if not domains:
            raise Exception("HTML Structure Changed on domain search on iteration " + str(x))
        domain = ''
        for n in np.arange(len(domains)):
            domain = domains[n].text
            # print(domain)
            if 'wiki' not in domain and 'webster' not in domain and 'tv' not in domain and domain and 'imdb' not in domain \
                    and 'youtube' not in domain and 'thesaurus' not in domain and 'vimeo' not in domain \
                    and 'dictionary' not in domain and 'britannica' not in domain and 'linkedin' not in domain \
                    and 'glassdoor' not in domain and 'indeed' not in domain and 'libertyjobs' not in domain:
                break
        if "www" in domain:
            domain = domain.split("www.")[1].replace("/", "")
        if "http://" in domain:
            domain = domain.split("http://")[1].replace("/", "")
        if "https://" in domain:
            domain = domain.split("https://")[1].replace("/", "")
        if "/" in domain:
            domain = domain.replace("/", "")
        if " " in domain:
            domain = domain.split(" ")[0]

        time.sleep(np.abs(np.random.normal(30, 10)))

        do_random_searches()

        try:
            # TODO deal with emojis in name
            recruiters = list(set([person for person in people if "Talent" in person or "Recruit"
                                   in person or "recruit" in person or "talent" in person
                                   or "COO" in person or " coo " in person or "Chief Operating Officer" in person
                                   or "CEO" in person or "Chief Executive Officer" in person or "Co-Founder" in person
                                   or "Founder" in person or " cto " in person or "CTO" in person
                                   or "Chief Technology Officer" in person or " cmo " in person or "CMO" in person
                                   or "Chief Marketing Officer" in person or "Administrative Assistant" in person
                                   or "HR" in person or "human resources" in person or "office manager" in person
                                   or "Office Manager" in person or "Human Resources" in person
                                   or "vp - product" in person or "VP - Product" in person
                                   or "vp product" in person or "VP Product" in person
                                   or "vp of product" in person or "VP of Product" in person
                                   or "Director of people operations" in person
                                   or "Director of People Operations" in person
                                   or "director of people operations" in person or "Director of operations" in person
                                   or "Director of Operations" in person or "director of operations" in person
                                   or "Human resources" in person or "Vice president brand management" in person
                                   or "Vice President Brand Management" in person
                                   or "VP brand management" in person or "VP Brand Management" in person
                                   or "VP of brand management" in person or "VP of Brand Management" in person
                                   or "vp - brand management" in person or "VP - brand management" in person
                                   or "vp - Brand Management" in person or "VP - Brand Management" in person
                                   or "chief of staff" in person or "Chief of Staff" in person
                                   or "Cofounder" in person
                                   or "vp - engineering" in person or "VP - Engineering" in person
                                   or "vp engineering" in person or "VP Engineering" in person
                                   or "vp of engineering" in person or "VP of Engineering" in person
                                   or "Director of people" in person or "Director of People" in person
                                   or "director of people" in person or "Sales Development Representative" in person
                                   or "Sales Development representative" in person
                                   or "sales development representative" in person or "Sales Director" in person
                                   or "Sales director" in person or "sales director" in person
                                   or "Director of product" in person
                                   or "Director of Product" in person or "director of product" in person
                                   ]))

            recruiters = [person for person in recruiters if "LinkedIn" not in person]

            recruiters = [person.split(" - ")[0] for person in recruiters]
            titles = [person.split(" - ")[1] for person in recruiters]

            startup = {"Startup Domain": domain,
                       "Recruiter(s)": recruiters,
                       "Title(s)": titles,
                       "Startup Name": comp_names[x]}

            # TODO modify test_startup so that based on the correct format of the first valid recruiter it tests that
            #  format against the rest first
            try:
                test_startup(startup)
            except NoSuchElementException:
                print(domain)
                bad_domains.append(startup)
        except NoSuchElementException:
            print(domain)
            startup = {"Startup Domain": domain,
                       "Recruiter(s)": recruiters,
                       "Title(s)": titles,
                       "Startup Name": comp_names[x]}
            bad_domains.append(startup)
            continue
        if time.localtime().tm_hour >= 19 or time.localtime().tm_hour <= 6:
            print("Script waiting due to time constraint. Finished iteration {}".format(x))

            output = pd.DataFrame(output_data)

            output = output[output.Validity == "Verified"].drop_duplicates(subset=['Email'])

            garysguide_emails = set(output.Email.str.lower())

            master = pd.read_excel('leads_master_list.xlsx')

            master_emails = set(master.Email.str.lower())

            output = output[~output.Email.isin(garysguide_emails.intersection(master_emails))]

            output.to_excel("VentureLoop_10_9_19.xlsx")
            # while time.localtime().tm_hour >= 19 or time.localtime().tm_hour <= 6:
            #     print(str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min))
            #     time.sleep(1800)
            break
        x += 1
    except InvalidSessionIdException:
        print("Invalid Session ID: Trying again")
        driver = start_random_proxy()

for startup in bad_domains:
    if " " in startup["Startup Domain"]:
        startup["Startup Domain"] = startup["Startup Domain"].split(" ")[0]
    test_startup(startup)

bad_domains = []

output = pd.DataFrame(output_data)

output = output[output.Validity == "Verified"].drop_duplicates(subset=['Email'])

garysguide_emails = set(output.Email.str.lower())

master = pd.read_excel('leads_master_list.xlsx')

master_emails = set(master.Email.str.lower())

output = output[~output.Email.isin(garysguide_emails.intersection(master_emails))]

# TODO Check for doubled up emails, I guess concatenate names because we don't know which is correct? Theoretically
#  they should all have the same first name? Check with Abby is that's all he needs.

output.to_excel("Venture_Loop_10_19_19.xlsx")

output_to_master = output[['Recruiter Name', 'Email']]
output_to_master.columns = ['Name', 'Email']

master = pd.concat([master, output_to_master]).reset_index(drop=True)
master.to_excel("leads_master_list.xlsx")
