# 🤖 𝗞𝗔𝗥𝗠𝗔 𝗕𝗢𝗧 🤖

<p align="center">
<img src="logo.jpg" alt="KarmaBot">

Best User Bot To Manage Your Telegram Account 😉               
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Karma-goku/KarmaBot)


### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/Karma-goku/KarmaBot
cd Karmabot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

## Most PowerFul And Better And Secure !

## By KarmaBot

For any query or want to know how it works contact 👇👇
### <a href="@KarmaBoii"><img src="https://telegra.ph/file/8ef5ff8acca6c6e4c7dd7.jpg?logo=Telegram"></a>



## FORK AT YOUR OWN RISK !
## Don't Forget To Give A Star ⭐

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
