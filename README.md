# California House Pricing Prediction
[Live link](https://california-housing-price-1-eca5f99daca4.herokuapp.com/)  
A linear regression web app with API built with Flask, scikit-learn, pickle, and containerized for deployment to Heroku through GitHub Actions CI/CD Pipeline.
## Endpoints
- GET
    - /
- POST
    - /predict
    - /predict_api
## Stack
- **Framework**: Flask, Gunicorn
## Modifications
#### `fetch_california_housing` Instead of `load_boston`
Even though the Boston housing dataset is available in `fetch_openml()`, it being deprecated due to ethical concerns lead me to use the California housing dataset instead. To ensure models are fair, the training data should be without bias.
#### Jinja  with Bootstrap
Instead of using a single HTML page, Jinja was used to create a `layout.html` for new web pages to inherit along with Bootstrap for frontend styling. The `flash()` function is used to show prediction results on top of the page.
#### Added Input Validation
To prevent `HTTP 500 Internal Server Error`s and improper prediction results, key-value pairs are validated and ordered for model prediction. Since JSON data from `/predict_api` may come in an incorrect order or form data due to modified client-side HTML elements, keys are ordered server-side. Values are also check to ensure they are numeric even if received as `str`. Otherwise, a `HTTP 400 Bad Request` is raised.
#### Updated `.yml` for Deployment to Heroku
[Deploy to Heroku - GitHub Marketplace](https://github.com/marketplace/actions/deploy-to-heroku)
The original `.yml` script from [link](https://github.com/marketplace/actions/build-push-and-release-a-docker-container-to-heroku) 
failed to push the docker container to Heroku which I originally believed was due to Node.js 20 being deprecated. Heroku now requires their CLI be installed which wasn't the way the original script executed. Upon finding a more recently updated script, I ran into issues pushing to Heroku as the web app was originally deployed via a buildpack. The only way to change from buildpack to a container is to include `stack: container` in the script.
## Setup & Installation
**1. Clone Repository**
```
git clone https://github.com/hastyv-3/cali-house-pricing
cd cali-house-pricing
```
**2. Create Virtual Environment**
```
python -m venv venv
venv\Scripts\activate
```
**3. Install dependencies**
```
pip install -r requirements.txt
```
***4. Start Development Server**
```
Flask run
```
**5. Explore API Locally**
To test API calls, download and install [Postman](https://www.postman.com/).
## Acknowledgements
Adapted from https://www.youtube.com/watch?v=MJ1vWb1rGwM