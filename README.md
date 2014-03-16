agiliq-app
==========

Inside is my code to apply to Agiliq.

What it does:

1. Build the payload to get the access_token and fire it through the Request.
2. Get the access_token in the response JSON object.
3. Build the final payload consisting of info and resume file.
4. Fire a multipart request (Requests lib handles quite easily!) and confirm it is done.
