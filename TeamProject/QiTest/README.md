#Self note#

##Change bot token#
Change the bot token from Slack [Change tocken](https://273hotelchatbot.slack.com/services/278727458995?new_token=1).


*1.Update slack bot token:\n
Example: export SLACK_BOT_TOKEN='xoxb-278285234881-QOdpjXM9ZF8BQJPiv7eTXXXX'
```
export SLACK_BOT_TOKEN='PasteTockenHere'
```


*2. Run the print bot id python:\n
Copy the bot id from output.
```
python printbotid.py
```


*3. Set BOT_ID variable with the bot id that get from step 2:\n
Example: export BOT_ID='U868D6WRX'
```
export BOT_ID='bot id returned by script'
```


*4. Run the bot server:\n
```
python starterbot.py
```
