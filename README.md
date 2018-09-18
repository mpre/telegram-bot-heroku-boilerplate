# Telegram Python Bot + Heroku Boilerplate

Simple boilerplate for building telegram bots in python and hosting them on Heroku.

## How to run

1) Retrieve the bot's token from [@botfather](https://telegram.me/BotFather)

2) Create a new app on Heroku

3) Export the bot's token and the app URL as env variables on Heroku
```bash
$ heroku config:set BOT_TELEGRAM_TOKEN=<YOUR-API-TOKEN>
$ heroku config:set HEROKU_APP_URL=<YOUR-HEROKU-APP-URL>
```

4) Push the code on heroku
```bash
$ git remote add heroku <HEROKU-GIT-REPO>
$ git push heroku master
$ heroku ps:scale web=1
```

Enjoy your new bot!
