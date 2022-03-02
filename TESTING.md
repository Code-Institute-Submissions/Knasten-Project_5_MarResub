# Testing

## Navigation
-   All navigation links has been tested and works as intended including facebook, privacy and about link in footer.
-   On mobile header links shrink into a hamburger menu with dropdowns.
-   The correct cost of the shopping cart is being displayed and updated correctly.

## Product Listing
-   The pages listing products display the correct information, for each product.
-   Fixed header does not block any content, not on mobile or desktop
-   All products links are working as intended

-   If user is admin remove and update links are visible, and working as intended


### Search
-   The search functionality works as intended. It returns products whose name, producer and description contains the searched keyword
-   It has been tested over all product pages and works as intended on every single one


### Sorting
-   Sorting work as intended, it sort after price, name or category
-   This was tested on all product pages


## Product Details
-   The product pages display the correct information and image
-   If description is not available the customer is informed about this
-   Products can successfully be added to the cart using the button, and quantity can be selected to add more sets at once
-   Form for reviews has been tested and is being sent to approval of admin before being displayed
-   If approved reviews exist for a product it is being displayed as intended


## Shopping Cart
-   The shopping cart displays items added by customer
-   Updating quantity in cart works as intended
-   Removing a item from cart is working as intended
-   Clicking "Secure Checkout" redirects to checkout with products saved in cart.
-   Empty shopping cart is displayed as such and link back to shop is being displayed.


## Checkout and Payment
-   Checkout form is being displayed
-   If profile has saved data the checkout form comes prefilled
-   All items in shopping cart is being displayed properly
-   Grand total, total and delivery charges are being dislayed correctly
-   During checkout customer has the option to save his checkout data to his profile
-   Payment works correctly, stripe webhooks has been tested
-   An unsuccessful payment returns the reason for the failure
-   Verifications for orders are being sent by mail as intended
-   I have tested form submission both from webhooks and directly with javascript  
    This was tested by commenting out javascript form submission and then checking admin for orders
-   Webhooks have been tested by making purchases with and without form submit active.  
    This to make sure the webhook handles form validation in case of any unforseen mistakes from server or customer side.
-   Confirmation of working [Webhooks](readme-files/hook_control.png)


## Profile
-   The profile page displays the saved profile information
-   Upon entering profile page, profile form is displayed correctly with prefilled information
-   When submitting profile form it updates profile as intended
-   Order history for profile is displayed correctly
-   Clicking on an order takes you back to order confirmation and displays correctly.
-   Creating a user works as intended and mail is sent out to verify email.
-   Profile saving was tested by making a purchase then checking admin if profile updated



## About
-   Testimonial form is being displayed correctly
-   Testimonials displays correctly
-   Pagination is working as intended
-   Form works as intended when filled out it awaits approval from admin.


## Administrative Tools
-   Can only be accessed if user is admin
-   All tools work as intended.


### Product Management
-   Adding products works as intended.
-   If form is not correctly filled out submission will not work, if filled out correctly it works as intended
-   If a image is not uploaded with product a placeholder image will be used instead

#### Editing/Deleting a Product

-   Deleting products works as intended
-   Link for editing product works as intended, and form is being prefilled as it should
-   If form is correctly filled out, updating product works as intended

## Responsiveness

This application has been tested for responsiveness and any issues found has been sorted.
It has been tested on several different heights and widths.

-   Testing was done on chrome, explorer and firefox
-   Testing was also done with chrome dev tools to make sure it resizes as intended
-   Tested manually on an OnePlus 7 Pro and 27" screen and 24" screen


## Bugs Found

### Resolved

-   Question email template was using same template for customer and for siteowner. This was addressed and updated with new templates for the customer, and view code update 
    to use theese new templates to make sure it looks more professional (Resolved)

-   Rezise testimonials was not working on load, had to change the onload function to make it work (Resolved)

-   Non logged in users could submit tesimonial, this created an error since it has to connect to a user. Added condtionals to check for authenticated user (Resolved)

-   Resposiveness on smaller screens was poor, this was found to be beacuse of to wide search bar (Resolved)

-   Phone field on question form was required, this was resolved by changing the model to blank=true (Resolved)

-   Question form not showing up in base.html, this was resolved by adding a context_processor to about app (Resolved)

-   Media was not showing up when I first started out the project
    After reading and checking the code I found it was this line "[BASE_DIR / 'media']".
    I had to change it to os.path.join(BASE_DIR, 'media) and it started working. Though the static files were still able to use 'BASE_DIR /' syntax

-   Products images not showing up in cart: This was beacuse of spelling mistake on the url link.
    Accidentally wrote: "." instead of "_"

-   Collasible menu not working and if it worked the toast would not work.
    This was caused by mixing newer and older versions of bootstrap, removing 'bs' from data-toggle attr solved this problem

### Non Resolved

-   Message on submitting testimonial is not being displayed, have not been able to resolve this bug more testing is to be done (Not resolved)


**This is however doublechecked by the form submission**
-   When using the keyboard arrows you are able to go beyond the qty limit set, when adding products to the cart
-   You can write in any number in the qty field by keyboard input
