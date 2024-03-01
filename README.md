# SELENIUM PAGE OBJECT MODEL PROJECT

## Introduction
In this project, we will examine the Page Object Model design pattern, which is frequently used in UI test automations.
"Page Object Model (POM)" is a design pattern widely used in the field of software test automation. This pattern makes test cases and test code more organized, maintainable and reusable. Essentially, it represents each page in a web application as an object and collects all interactions and functions on that page into that object. Using the POM structure allows the separation of test objects and test scripts.

## WHAT ARE WE DOING?
First, we defined all the operations we will perform in the TestPom Violation class on a single page. First, you can run and examine this class. But there is a violation of the Page Object Model (POM) pattern in this code. The POM pattern aims to separate page objects from test logic for better maintainability and readability. In the current implementation, test logic and page interactions are tightly coupled. To refactor the code to fit the POM layout, we will create separate page object classes that encapsulate interaction with web elements on the page.

## Project Structure
The project structure is organized as follows:

  -	base: Contains base classes for setting up the test environment and defining common functionalities. 
  - pages: Contains page classes representing different pages of the web application under test. 
  - tests: Contains test scripts implementing test cases using the POM pattern. 
  - drivers: Contains WebDriver executables for different browsers.

### Test Implementation

Prerequisites:
  -	Python 3.x
  -	Selenium WebDriver
  - Web browser drivers (Chrome, Firefox, Safari, etc.)

## Test Scenarios

Test Name:<br/> Add Product to Cart and Redirect to Cart Page

Objective:<br/> To test adding a product to the cart and redirecting to the cart page after logging in.

Steps:

-	Open the browser and navigate to the tested website.<br/>
- Log in with user credentials.<br/>
- Select a product from the list on the home page.<br/>
- Open the page of the selected product.<br/>
- Click on the "Add to Cart" button on the product page.<br/>
- User is redirected to the cart page.<br/>
- Verify that the added product is listed on the cart page.<br/><br/>

Expected Results:<br/>
-	The user is successfully redirected to the cart page.<br/>
-	The product listed in the cart matches the added product.

## Notes
-	All test code is available in the respective classes in the repository.
-	Ensure that the required libraries and drivers are set up before running the tests.
-   Medium blog link: https://medium.com/@humeyrakoseogluu/page-object-model-pom-ile-selenium-web-otomasyon-test-projesi-fc88a3a62679 
