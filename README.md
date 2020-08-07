# dive-in-client
In using [Pocket](https://app.getpocket.com/), I had faced the issue of picking from only the items at the top of my collection, and the ones below were often forgotten/ignored.<br>
dive-in-client aims to level the playing field by retreiving a random article from the user's Pocket collection. 

# Prerequisites
* Python 3.8+ [Download](https://www.python.org/downloads/)

# How to use dive-in-client
Please note that dive-in-client is a CLI-based tool, although it is on the roadmap to eventually port it to a web app.<br> 

Here are the steps on getting started with dive-in:
* Download the program from Github as a zip-file and unzip it to a directory of your choice
* Launch CMD/Terminal and navigate to said directory (i.e. the one where you unzipped the .zip file you downloaded from Github)
* To invoke the script, type `python dive-in.py`
* If this is your first time using dive-in, a browser window will open asking you to allow the dive-in app read-only access (Read the privacy policy below) to your Pocket collection. Once you allow the app, you should be redirected [here](www.google.com)
* Go back to the terminal window and type in 'y' if you allowed dive-in access to your Pocket collection
* A random article from your collection will now open up in Chrome
* If this is _not_ your first time using the app, simply typing `python dive-in.py` will open a chrome tab with a random article from your collection
* Please do not modify with the .access_token.txt file. The contents of that file are what will authenticate you to use dive-in.  

# Help, the script is redirecting me to this page 
If you ran the script and landed here, chances are there is something wrong with the authentication mechanism. Nothing to worry about :) <br> Please try the following steps: 
* Delete the .access_token.txt file that is in the same folder as the script
* Run the script as `python dive-in.py`. Either of two things will happen: 
   * A Pocket webpage will open up asking you to auhtorize the app. Click on 'Authorize', go back to the terminal and hit 'y'. A random article should now open up in your default browser
   * You will automatically be redirected to [Google](www.google.com). Go back to the terminal and hit 'y'. A random article should now open up in your default browser

If the issue persists after trying these steps, please open an issue/contact me. I'd be happy to troubleshoot with you.

# Privacy policy
The privacy policy of dive-in is simple: No user-data is collected. Ever.
The programs collect no metrics whatsoever, and no data about your Pocket collection is ever logged. The program does one thing, and one thing only, retreive a random article and open it up for you.
If however, you still want to stop using dive-in, you can simply go to your [connected applications](https://getpocket.com/connected_applications) and remove access for dive-in 

# The Architecture
From an architectural perspective, dive-in-client is really just a client that makes API calls to a serverless [AWS Lambda](https://aws.amazon.com/lambda/) function. This lambda function retreives the user's article list and sends it back to the client. The client program then simply picks a random article and opens it up in a browser window.  
