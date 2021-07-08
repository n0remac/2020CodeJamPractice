# 2020CodeJamPractice
A practice project for Python Discord code jam

## Setup
Make sure you have python3.9 installed

Tested on Linux:

Create env:<br />
`python3.9 -m venv venv`<br />
Activate env:<br />
`source venv/bin/activate`<br />
The first time you activate update pip:<br />
`python -m pip install --upgrade pip`<br />
Install requirements:<br />
`pip install -r requirements.txt`<br />
Run app:<br />
`python app.py`<br />

## Creating new panel
When creating a new panel add a file to the panels directory then import it in app.py. Add it to the layout in the setup function. The update function can be used to update_layout function will eventually be used to make the app animate or be interactive.