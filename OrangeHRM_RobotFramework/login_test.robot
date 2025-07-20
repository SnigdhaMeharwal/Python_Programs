*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${URL}          https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${USERNAME}     admin
${PASSWORD}     admin123


*** Keywords ***
launch application on chrome browser
    open browser                ${URL}          chrome
    maximize browser window
    sleep                       3s


*** Test Cases ***
Valid Login to Application OrangeHRM Demo
    launch application on chrome browser
    input text                  xpath=//input[@name='username']         ${USERNAME}
    input text                  xpath=//input[@name='password']         ${PASSWORD}
    click button                xpath=//button[@type='submit']
    sleep                       3s
    ${title}=                   get title
#    should be equal             ${title}        OrangeHRM
    page should contain         Dashboard
    close all browsers