Problems occured: (1(Media not showing up )), (2(Some products imgs not working in cart))
Solutions: ((1)change this line "[BASE_DIR / 'media']" for "os.path.join(BASE_DIR, 'media')"), (2(Spelling mistake on a url link instead of "." I had "_"))

Other:
# https://django-allauth.readthedocs.io/en/latest/faq.html?highlight=EMAIL_BACKEND#when-i-sign-up-i-run-into-connectivity-errors-connection-refused-et-al
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Main bg pic = Photo by <a href="https://unsplash.com/@sadeqshahsvan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">sadeq shahsvan</a> on <a href="https://unsplash.com/s/photos/gaming?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Non-Solved-Problems: When using arrows you are able to go beyond the qty limit set.
  