# Financial Freedom Calculator

[Financial Freedom Calculator](https://github.com/Annibor/financial-freedom-calc)

# Introduction

Welcome to Financial Freedom Calculator! This is a python program designed to assiste users in planning their financial journey. This calculator provides two main functionalities:

1. **Calculate Years Until Financial Freedom:** This determine the number of years it takes to reach financial frredom based on the users initial savings, monthly savings thir financial goals. 
2. **Calculate Required Monthly Savings:** This calculates the monthly savings needed to achive the users financial goal within the a specified time frame.


![Am I Responsive Screenshot]()

## Table of Content

- [**Financial Freedom Calculator**](#financial-freedom-calculator)
  - [**Table of Content**](#table-of-content)
  - [**Planning & development**](#planning--developmnet)
    - [**Project Goals**](#project-goals)
    - [**Future Features**](#future-features)
  - [**Testing**](#testing)
  - [**Devtools**](#devtools)
  - [**Deployment**](#deployment)
  - [**Languages**](#languages)
  - [**Software**](#software)
  - [**Usage**](#usage)
  - [**Modification**](#modification)
  - [**Distribution**](#distrubition)
  - [**Private Use**](#private-use)
  - [**Liability**](#liability)
  - [**Credits**](#credits)
  - [**Content**](#content)
  - [**Special thanks**](#special-thanks)
  - [**What I've learned**](#what-ive-learned)

## Planning & developmnet


### Project Goals

The primary goals for the Financial Freedom Calculator are to:
- Provide users with a tool to calculate the number of years required to achive financial freedom.
- Assist the user in determining the monthly savings needed to reach financial freedom within a certain period of time.

### User-Centered Approach


#### As a General user

- Recive clear instructions for using the calculator.
- Easily understand the pourpose and benefits of the calculator.

#### As a New User

- Understand the outcomes of calculations.
- Recive infomation about each step in the calculation.

### Features

- **Years to Financial Freedom Calculation**:
  - Input your intiial savings, monthly savings and financial goal.
  - The calculator will provide the num,ber of years required to achive financial freedom for the user.
  - 

- **Required Monthly Savings Calculation**:
  - Input initial savings, target financial goals and the desired time frame. 
  - The calculator will determine the monthly savings needed to reach the users financial goal.

- **Exit**: 
  -The calculator will exit the program if user enters 'exit' in any of the inputs within the calculator. 

- **Option to rerun a calculation**: 
  - When a calculation is done, the calculator will ask the user if it would like to make another calculation. 
     - If yes, the user will make a new choise of what calculation it want to do. 
     - If no, the calculator will exit the program and thank the user for useing the calculator. 


### Future Features

Future features for the CLI are:
- Additional financial planning tools.
- Make calculations work if user wants to input yearly or monthly interest rates.
- Making it possible for user to save and send the calculations to their emails.
- Making a calculation that includes the aculat spenings for the user each month. 



## Testing

- Throughout the whole development of the webpage, I've made tests in:


### Manual testing

<table>
 <thead>
   <tr>
     <th>Testing Description</th>
     <th>Expected Action</th>
     <th>Actual Output</th>
     <th>Result</th>

   </tr>
 </thead>
  <tbody>
   <tr>
     <td>Start menu loads</td>
     <td>User is presentend with welcome text and input for entering name.</td>
     <td>User is presentend with welcome text and input for entering name.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Enters name</td>
     <td>User enters name and get followed by message of entering email address.</td>
     <td>User enters name and get followed by message of entering email address.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Enters email address</td>
     <td>User enters email address and get followed by message of entering age if email is valid.</td>
     <td>User enters email address and get followed by message of entering age if email is valid.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Invalid email address</td>
     <td>User enters invalid email address and get followed by message of Invalid email address. Please enter valid email.</td>
     <td>User enters invalid email address and get message of Invalid email address. Please enter valid email.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Enters age</td>
     <td>User enters age and get followed by welcome message and introduction for the calculation.</td>
     <td>User enters name and get followed by welcome message and introduction for the calculation.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Information and choises are showed</td>
     <td>User is presented with information about the calculations and presented with a choice</td>
     <td>Information about the calculations are showed and user is presented with a choice</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Enters a choice</td>
     <td>User inputs 1 and calculation 1 starts.</td>
     <td>When user inputs 1 the claculation 1 starts.</td>
     <td>Confirmed</td>
   </tr>
    <tr>
     <td>Calc. 1 inputs</td>
     <td>User inputs digits and the calculation runs until end.</td>
     <td>The caclulations runs until end when user inputs digits.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Calc. 1 inputs</td>
     <td>User inputs anything else than digits. User get error message.</td>
     <td>Error message shown when user inputs anything but digits.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Calc. 1 when error - restart</td>
     <td>Calulation restarts if user inputs anything but digits.</td>
     <td>Restart for user to rechoose whtat calculation to do.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Calc. 2 inputs</td>
     <td>User inputs digits and the calculation runs until end.</td>
     <td>The caclulations runs until end when user inputs digits.</td>
     <td>Confirmed</td>
   </tr>
   <td>Calc. 2 inputs</td>
     <td>User inputs anything else than digits. User get error message.</td>
     <td>Error message shown when user inputs anything but digits.</td>
     <td>Confirmed</td>
   </tr>
    <tr>
     <td>Calc. 2 when error - restart</td>
     <td>Calulation restarts if user inputs anything but digits.</td>
     <td>Restart for user to rechoose whtat calculation to do.</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Option to make another calculation</td>
     <td>When calculation is done, user will get option to make another calculation or not.</td>
     <td>Option to restart calculation when calculation is done.</td>
     <td>Confirmed</td>
   </tr>
    <tr>
     <td>Calc. 1 When user choose to make a new calculation</td>
     <td>If user inputs "yes", the option to choose what calculation to make appears.</td>
     <td>The program where the user choose what calculation do appears when typing "yes".</td>
     <td>Confirmed</td>
   </tr>
    <tr>
     <td>Calc. 2 When user choose to make a new calculation</td>
     <td>If user inputs "yes", the option to choose what calculation to make appears.</td>
     <td>The program where the user choose what calculation do appears when typing "yes".</td>
     <td>Confirmed</td>
   </tr>
    <tr>
     <td>Calc. 1 When user choose not to make another calculation</td>
     <td>If user inputs "no", the user gets a thank you message and the progam will end.</td>
     <td>The program ends with a thank you message when user inputs "no".</td>
     <td>Confirmed</td>
   </tr>
    <tr>
     <td>Calc. 2 When user choose not to make another calculation</td>
     <td>If user inputs "no", the user gets a thank you message and the progam will end.</td>
     <td>The program ends with a thank you message when user inputs "no".</td>
     <td>Confirmed</td>
   </tr>
   <tr>
     <td>Exit the program</td>
     <td>If typing exit in any input, the program will end.</td>
     <td>When input exit, the program will end with a thank you message.</td>
     <td>Confirmed</td>
   </tr>
  </tbody>
</table>

## Deployment

I deployed early to be able to test the website deployed during the development. Following step are a description of how to deploy a webpage on GitHub:

1. Open the []() and find the Settings tab.
2. The navigate to the tab called Pages on the left.
3. Choose to Deploy from a branch. For me it was the main branch.
4. Save it. It can take a few minutes, but then you will be able to find the link to the deployed website in the repository on the menu to the right, under []().
5. There you'll find the daployes website no top of the page under the heading Active deployments.

My link is: []()

## Languages

- This CLI was built using python.

## Software

- I've used Visual Studio Code to write the code.
- I've used Git to load and push my code to Github and for version control.
- I've used GitHub for repository management.
- I've used Chat GPT and google translate for some translations and questions.
- I've used CI Python Linter for testing the python code.

## Usage

- This project is available for viewing and can be used for educational purposes.

## Modification

- Any modification, transformation, or extension of this project for commercial or public purposes is not allowed without explicit permission.

## Distrubition

- The redistribution of this project, wheter in its original form or with modifications, is sricktly prohibited without prior consent.

## Private Use

- Feel free to use this project for private purposes, sush as personal reference or study.

## Liability

- The creator of this project shall not be held liable for any adverse outcomes or damages resulting from the use or misapplication of this project. Users are advised to exercise due care and discretion when utilizing the project's resources and functionalities.

## Credits

### Content

- This README is based upon two sourses for guidance: one by Davis Calikes, available at [GitHub](https://github.com/davidcalikes/portfolio-project-one#readme), and another authored by me, available at [GitHub](https://github.com/Annibor/EarthEcho-Studios/blob/main/README.md)
- Usage, Modification, Distrubition, Private Use and Liability Content: The guidelines pertaining to usage, modification, distribution, private use, and liability are directly derived from my project, accessible at [GitHub](https://github.com/Annibor/EarthEcho-Studios/blob/main/README.md)
- This project is based upon two sources for guidance: one by ismailmoufid47, available at [GitHub](https://github.com/ismailmoufid47/financial_calculator/blob/main/calculations/calculations.py) and one by Akash3121, available at [GitHub](https://github.com/tuomaskivioja/5-super-quick-automation-ideas/blob/main/wealth_calculator.py).
- The code for importing googlesheets, like SCOPE and Credentials are adapted from Code Institues [GitHub](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode).
The functions for adding data from the user to the gogglesheets are based on the [GitHub](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode)by Code Institute.

### Special Thanks

I would like to express my gratitude to the following individuals who have made a meaningful impact on this project:

- **Michel**: My wonderful boyfriend, whose unwavering support and encouragement have been my constant motivation.

- ****: 

## What I've Learned

During the development of this project, I've gained valuable insights and skills that have enriched my coding journey. Here are some of the key takeaways:

- ****: 