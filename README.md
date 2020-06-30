# runescape-pwfill
Automates filling your password into the RS3 client

If you're like me and use a password manager (which you really should be doing these days), having to manually type those generated passwords can be a real annoyance. Most sites/applications allow you to copy/paste EXCEPT the Runescape NXT client. 

Enter rspwfill.py

This tool will allow you to read your password from a file or password manager and autofill this into the RS3 client.

### Requirements
rspwfill requires [pyautogui](https://pyautogui.readthedocs.io/en/latest/) which has it's own requirements based on the OS your running this script from. Please check the link to make sure those are satisfied. You can install pyautogui via 

```pip install -r requirements.txt```

or

``` pip install pyautogui```

#### Known limitations
* This tool only supports [pass](https://www.passwordstore.org/)
  * File support and other managers will be coming shortly
* This only works if the RS3 client is the next window that is opened when "alt+tab" is pressed
  * Yes, that's a little hacky, but I'm working on trying to find a better way to do this.
