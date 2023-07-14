   Easy CAPTCHA API Documentation \* { box-sizing: border-box; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; } body { padding: 20px; max-width: 1200px; margin: auto; } p { word-break: break-all; } .code { font-family: monospace; font-size: 110%; }

Easy CAPTCHA API Documentation
==============================

* * *

* * *

Welcome to the CAPTCHA API documentation! This document provides an overview of the CAPTCHA API, its endpoints, request/response formats, and usage guidelines. The CAPTCHA API is designed to integrate CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) functionality into your applications to protect against automated bots and spam.

* * *

Base URL
--------

https://api.example.com/api/captcha

* * *

API Endpoints
-------------

### Generate a CAPTCHA Image

#### Endpoint: /api/captcha

#### Method: POST

This endpoint generates a new CAPTCHA image and returns its details, including the base64 image data and associated token.

#### Request Parameters: None

#### Response:

*   token: The unique token associated with the generated CAPTCHA image.
*   image\_data: The data to the generated CAPTCHA image.

#### Example Request:

POST /api/captcha

Content-Type: application/json

#### Example Response:

{  
    "token": "w6PCusOBw495",  
    "image": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAI..."  
}

#### Display image

<!-- html -->  
<img id="cptImg" alt="captcha-image" token="none">  
  
//Javascript  
const captImage = document.getElementById("cptImg");  
function showCaptchaImage(){  
    // After requesting captcha api, assuming the response  
    // response = {  
            "token": "w6PCusOBw495",  
            "image": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAI..."  
        }  
    response = JSON.parse(response);  
    captImage.src = \`data:image/jpeg;charset=utf-8;base64,${response.image}\`;  
    captImage.token = response.token;  
}

### Verify a CAPTCHA

#### Endpoint: /api/captcha/token,value

#### Method: POST

This endpoint verifies the user's input for a specific CAPTCHA.

#### Request Parameters: None

#### Response:

{"response": false}  
     OR  
{"response": true}

#### Example Request:

POST /api/captcha/w6PCusOBw495,GH7Fj

Content-Type: application/json

#### Example Response:

{"response": true}

* * *

Error Handling
--------------

In case of an error, the API will respond: {"response": false} excluding network/http errors.

* * *

Usage Guidelines
----------------

*   CAPTCHA tokens are unique for each CAPTCHA image and should be stored and used for verification.
*   The CAPTCHA image URLs have a unlimited validity period. Please ensure you fetch and display the image promptly.
*   To avoid excessive usage and potential abuse, it is recommended to implement rate limiting on your side.

Remember, while CAPTCHAs serve as an effective security measure, they should be implemented alongside other security measures to ensure comprehensive protection against bots and malicious activities.

* * *

Conclusion
----------

This concludes the documentation for the CAPTCHA API. By integrating this API into your application, you can effectively protect against automated bots and ensure the security and integrity of your platform. If you have any further questions or need assistance, please contact me at _acharyabidhan2003@gmail.com_

* * *

\*\*\*