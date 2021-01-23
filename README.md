# Requirements
#### ** You should have Python 3.X installed on your machine
#### ** The input csv file should contain columns of `x` and `y` in lowercase and/or other columns
#### ** Make sure columns of `x` and `y` have proper WGS84 longitudes and latitudes values
#### ** The code will not work and raise an error if any of the conditions with columns of `x` and `y` are not met

# How to use the code?

1) In order for this code to work, you need to get two API keys from:
  * [Open Weather Map API](https://home.openweathermap.org/users/sign_up)
  * [Google Elevation API](https://developers.google.com/maps/documentation/elevation/get-api-key)
  
2) Then create two enviroment variables in your operating system with the API keys you got from `Open Weather Map` and `Google`:
  * OWM_API_KEY='xxxxxxxxx'
  * GOOG_API_KEY='xxxxxxxxx'
 
3) Once you have the API keys ready on your operating system, you need to create a virtual environment to install the required packages. This example is for macos:
  * Download the files and folder from the repo
  * Open terminal and navigate to the folder where you downloaded the repo content
  * Type `python3 -m venv {virtual-env-name-you-want}`
  * Activate the env by typing `source {virtual-env-name-you-chose}/bin/activate`
  * Update pip by typing `pip install --upgrade pip`
  * Install the packges inside the virtual environment by typing `pip install -r requirements.txt`

4) Now the environment is ready and you can run the code. To do so, type in:
  * `python3 get_weather_data.py {input-coords-csv-file} {results-csv-file}`
  * As an example, you can use the sample csv file  `./input/coords.csv` and an output as `./output/results.csv`:
    * `python3 get_weather_data.py ./input/coords.csv ./output/results.csv`
