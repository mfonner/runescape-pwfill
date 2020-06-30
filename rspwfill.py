'''
A script to autofill your password into the RS3 client.
'''

import pyautogui
import argparse
import subprocess
import getpass

#TODO: Handle arguments
# Password manager or plaintext
# File path

# Gather args
parser = argparse.ArgumentParser()

parser.add_argument('-t',
        help='Target application/password to retrieve from pass')

args = parser.parse_args()

def get_pw(target):

    # Source for the below code:
    # https://github.com/kai-dg/linux-dotfiles-scripts/blob/master/scripts/passpy.py

    result = None

    if target and target != []:
        proc = subprocess.Popen("pass {} | head -n 1".format(target), shell=True, stdout=subprocess.PIPE)

        output = proc.communicate()[0]

        result = output.decode("utf-8").strip().split()

    if result and len(result) == 1:
        return result[0] # This returns a str if single password

    else:
        return result # This returns a list if multilined

def main():

    # alt-tab to change windows
    # RS3 must be the nex window when alt+tab is pressed
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pwd = get_pw(args.t)

    pyautogui.typewrite(pwd)

if __name__ == '__main__':
    main()
