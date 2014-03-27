dial-a-dpla
===

*dial-a-dpla* is a Twilio-based telephone client that provides access to sound
recordings available from the [Digital Public Library of America](http://dp.la). This was created for a lightning talk [(slides)](http://matienzo.org/storage/2014/2014Mar-code4lib-lightning-talk/) at the [code4lib 2014](http://code4lib.org/conference/2014/) conference

To deploy on Heroku, you will need a Twilio account, a Twilio app, and a DPLA API key.

* Create a new app on Heroku: `heroku create`
* Add your settings:
```
heroku config:set TWILIO_ACCOUNT_SID=YOUR_ACCOUNT_SID
heroku config:set TWILIO_AUTH_TOKEN=YOUR_AUTH_TOKEN
heroku config:set DPLA_API_KEY=YOUR_DPLA_API_KEY
heroku config:set TWILIO_APP_SID=YOUR_APP_SID
```

* Deploy to Heroku: `git push heroku master`
* Add the URL of your Heroku app to your app on the Twilio dashboard.

License: MIT