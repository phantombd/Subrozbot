#  Subroz Bot 

<p align="center">
<img src="logo.jpg" alt="Subrozbot">

Best User Bot To Manage Your Telegram Account 😉               
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Subroz/Subrozbot)

## GET STRING SESSION FROM REPL RUN 

[![Repl.it](https://img.shields.io/badge/REPL%20RUN-Run%20Online-blue.svg)](https://userbot.subro.repl.run)
...With The Help Of This U can Skip Termux Part And Make String Sessions Easily

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/Subroz/Subrozbot
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

## By Subrozbot

For any query or want to know how it works contact 👇👇
### <a href="https://t.me/Subroz"><img src="https://telegra.ph/file/e29a7b37178dca48b535e.jpg?logo=Telegram"></a>



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
