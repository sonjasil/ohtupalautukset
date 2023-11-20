*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Invalid Password
    Set Username  ville
    Set Password  villeville
    Set Password Confirmation  villeville
    Submit Credentials
    Register Should Fail With Message  Invalid password


Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville124
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  heli
    Set Password  heli1234
    Set Password Confirmation  heli1234
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Logout Should Succeed
    Set Username  heli
    Set Password  heli1234
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  anni
    Set Password  anni1
    Set Password Confirmation  anni1
    Submit Credentials
    Register Should Fail With Message  Invalid password
    Go To Login Page
    Set Username  anni
    Set Password  anni1
    Submit Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Logout Should Succeed
    Click Button  Logout
    Login Page Should Be Open
