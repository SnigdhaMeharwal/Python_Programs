*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${URL}                      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${USERNAME}                 admin
${PASSWORD}                 admin123
${employee_firstname}       TestUser_FirstName1
${employee_lastname}        TestUser_LastName1
${employee_username}        TestUser_UserName4
${EMPLOYEE_ID}
${user_password}            Password123


*** Keywords ***
launch application on chrome browser
    open browser                ${URL}          chrome
    maximize browser window
    sleep                       3s


*** Test Cases ***
Verify a new employee is created
    [Documentation]    creating a new employee and verifying that employee is created
    # Login as admin
    launch application on chrome browser
    input text          name=username                           ${USERNAME}
    input text          name=password                           ${PASSWORD}
    click button        xpath=//button[text()=" Login "]
    sleep               3s


    # add a new employee
    click link          css=a[href="/web/index.php/pim/viewPimModule"]
    sleep               1s
    click link          xpath=//a[text()='Add Employee']
    sleep               1s
    input text          xpath=//input[@placeholder='First Name']                        ${employee_firstname}
    input text          xpath=//input[@name="lastName"]                                 ${employee_lastname}

    ${EMPLOYEE_ID}=     get text            xpath=(//input[@class="oxd-input oxd-input--active"])[2]
    Log     Newly created employee id is ${EMPLOYEE_ID}

    # assign login credentials
    click element       xpath=//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]
    input text          xpath=(//input[@class="oxd-input oxd-input--active"])[3]                        ${employee_username}
    input text          xpath=(//input[@type="password"])[1]                                            ${user_password}
    input text          xpath=(//input[@type="password"])[2]                                            ${user_password}
    sleep               1s
    click button        xpath=//button[@type="submit"]
    sleep               2s


    # serach the employee and verify
    click link              xpath=//a[text()='Employee List']
    sleep                   2s
#    click button            xapath=(//button[@class="oxd-icon-button"])[2]
    input text              xpath=(//input[@class="oxd-input oxd-input--active"])[2]                        ${employee_id}
    click button            xpath=//button[@type='submit']
    page should contain     (1) Record Found

    # logout and login as the new employee


# update profile details

# logout

# login as admin and terminate the employee

# verify employee is terminated

