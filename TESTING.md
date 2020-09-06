### Manual Testing
#### All testing was done on multipule browsers and devices.

#### Register Page

- Test that all input fields require input.

- Test all input fields only accept vaild input.

- Test error page loads on duplicate username input.

- Test that after successful sign up directed to coin list page.

- Test that back arrow does not break the site or cause an error.


#### Sign In Page

- Test that all input fields require input.

- Test all input fields only accept vaild input.

- Test error page loads on unknown username input.

- Test error page loads on incorrect password input.

- Test that after successful sign in directed to coin list page.

- Test that back arrow does not break the site or cause an error.

- Test that after logging out, pressing back arrow in the browser results in error page display.


#### Coin List page

- Test that all nav element show responsive pionter.

- Test that Logo in nvabar loads coin list page.

- Test that coin list link in navbar loads coin list page.

- Test that My Crypto link points to My Cypto page.

- Test that Add Crypto link points to Add Cypto page.

- Test that Logout link points to Logout page.

- Test that back arrow does not break the site or cause an error.

- Test table sorting filter work.

- Test that after logging out, pressing back arrow in the browser results in error page display.


#### My Crypto page

- Test page loads holdings page without data.

- Test page loads holdings table with data  available.

- Test that pie chart of holdings is displyed when data is available.

- Test that all buttons (edit, update, delete) displayed in the table point to correct pages.

- Test that all navbar elements show responsive pionter.

- Test that Logo in nvabar loads coin list page.

- Test that coin list link in navbar loads coin list page.

- Test that My Crypto link points to My Cypto page.

- Test that Add Crypto link points to Add Cypto page.

- Test that Logout link points to Logout page.

- Test that back arrow does not break the site or cause an error.

- Test that after logging out, pressing back arrow in the browser results in error page display.

#### Add Crypto Page

- Test page loads Add Crypto form.

- Test all inputs only except availed inputs.

- Test that connot submit form without required fields data available.

- Test data is sent to MongoDb correctly and stored in correct data type.

- Test that all navbar elements show responsive pionter.

- Test that Logo in nvabar loads coin list page.

- Test that coin list link in navbar loads coin list page.

- Test that My Crypto link points to My Cypto page.

- Test that Add Crypto link points to Add Cypto page.

- Test that Logout link points to Logout page.

- Test that back arrow does not break the site or cause an error.

- Test that after logging out, pressing back arrow in the browser results in error page display.

#### Logout Link

- Test page loads Sign In form.

- Test link clears session.

- Test that all navbar elements show responsive pionter.

- Test that Logo in nvabar loads coin list page.

- Test that coin list link in navbar loads coin list page.

- Test that My Crypto link points to My Cypto page.

- Test that Add Crypto link points to Add Cypto page.

- Test that Logout link points to Logout page.

- Test that back arrow does not break the site or cause an error.

- Test that after logging out, pressing back arrow in the browser results in error page display.

#### Testing EDIT, UPDATE, DELETE Buttons in users My Crypto Page.

- Test Edit buttons displays edit_crypto form.

- Test Add buttons displays add_to form.

- Test to ensure that Add button increments the current value in the mongo DB

- Test Delete buttons points delete page.

- Test all inputs only except availed inputs.

- Test that connot submit form without required fields data available.

- Test data is sent to MongoDb correctly and stored in correct data type.

- Test that all navbar elements show responsive pionter.

- Test that Logo in nvabar loads coin list page.

- Test that coin list link in navbar loads coin list page.

- Test that My Crypto link points to My Cypto page.

- Test that Add Crypto link points to Add Cypto page.

- Test that Logout link points to Logout page.

- Test that back arrow does not break the site or cause an error.

- Test that after logging out, pressing back arrow in the browser results in error page display

#### Additional Testing

- Some Crypto prices are below 1 cent and so checking for price using Jinja and if statements to check the correct format is displyed. ie 0.001

- Tested manual entering of URLs without username to check error page display. All working.

- Tested to make sure that site works on popular borwsers. Chrome Ex Safari Firefox and Brave.

- Tested verious screens sizes

- Tested app routes all work and have valid outcomes



#### Issues
During production I came accross this error <TypeError: '>' not supported between instances of 'NoneType' and 'int'>
The biggest challenge for me in this build was learning the MongoDb syntax, in piticular pushing to an array and incrementing values in an array. There were some fiddly formatting and style issues as well. 
