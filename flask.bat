:: This command will cd into the correct folder, activate your virtual environment,
:: set the correct commands for Flask and run it. 
:: So once it's set up, you will only have to double click it to start Flask.
:: No more command line tomfoolery!

:: You’ll still have to find the full file path to your Github folder. Hold down SHIFT, and click the folder.
:: Copy as Path will appear and you can paste this into the following command in place of [FILEPATH].

cmd /k "cd C:\Users\jacob\Desktop\physical-nfts && env\Scripts\activate.bat && set FLASK_APP=run.py && set FLASK_DEBUG=1 && py -m flask run"