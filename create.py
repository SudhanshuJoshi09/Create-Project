# pip3 install selenium.
from selenium import webdriver
# pip3 install webdriver_manager.
from webdriver_manager.chrome import ChromeDriverManager
# This is for command line arguments.
import sys

def parse_info(file_name):
    """ Parses the info to email and password. """

    cred = open(file_name, 'r')
    email = cred.readline().strip('\n')
    password = cred.readline().strip('\n')

    return email, password

def main(repo_name):
    """ The main funtion. """

    # Getting the personal details.
    email, password = parse_info('credfile')

    # Defining Web Browser.
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Login in to github account.
    login(driver, email, password)

    # Create a new repo.
    create_repo(driver, repo_name)

    # Getting the remote origin.
    remote_org(driver)

def create_repo(driver, name):
    """ Create's the new repo. """

    driver.get('https://github.com/new')
    repo_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
    repo_name.send_keys(name)
    python_button = driver.find_element_by_css_selector('button.first-in-line')
    python_button.submit()

def login(driver, email, password):
    """ Logs you into the github. """

    driver.get("https://github.com/login")
    web_email = driver.find_element_by_xpath('//*[@id="login_field"]')
    web_password = driver.find_element_by_xpath('//*[@id="password"]')
    web_email.send_keys(email)
    web_password.send_keys(password)
    submit = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
    submit.click()

def remote_org(driver):
    """ Outputs the remote origin """

    print(driver.find_element_by_xpath('//*[@id="empty-setup-push-repo-echo"]/span[1]/span').get_attribute('innerHTML'))

if __name__ == '__main__':
    main(sys.argv[1])