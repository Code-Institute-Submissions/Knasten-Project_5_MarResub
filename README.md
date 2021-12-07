Problems occured: (1(Media not showing up )), (2(Some products imgs not working in cart)), (3(Problem with toast and/or collasible menus))
Solutions: ((1)change this line "[BASE_DIR / 'media']" for "os.path.join(BASE_DIR, 'media')"), (2(Spelling mistake on a url link instead of "." I had "_")),
(3(Had to import other versions of scripts and remove "bs" from collasible menus, example "data-bs-toggle" is now "data-toggle" This is beacuse I now import bootstrap 4 instead of 5 and they have changed the code for this.))

Other:
# https://django-allauth.readthedocs.io/en/latest/faq.html?highlight=EMAIL_BACKEND#when-i-sign-up-i-run-into-connectivity-errors-connection-refused-et-al
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



Non-Solved-Problems: When using arrows you are able to go beyond the qty limit set.

Credits:

Main bg pic = Photo by <a href="https://unsplash.com/@sadeqshahsvan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">sadeq shahsvan</a> on <a href="https://unsplash.com/s/photos/gaming?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Checkout html is mostly borrowed from Codeinstitute walkthrough project for E-Commerce, copied and then edited to suit my page better.
While writing this project code snippets have been borrowed from the walkthrough project, this because when trying to figure out alternative ways it would result in longer code snippets than actually warranted.

Allauth templates has been copied from CodeInsitute walkthrough project.
  