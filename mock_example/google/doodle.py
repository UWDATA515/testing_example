import requests
import re

# We use the "twitter title" tag to identify the name of the Doodle
doodle_re = re.compile('.*<meta content="(.+)" property="twitter:title">.*')

def load_google_doodle_title():
    """
    Loads the title of today's Google doodle from Google's
    webpage.

    Returns:
    string: the title of today's Google doodle, or None if no doodle
    """
    try:
        response = requests.get('https://google.com')
        match = re.match(doodle_re, response.text)
        if match:
            return match.group(1)
        else:
            return None
    except:
        return None

if __name__ == '__main__':
    doodle_title = load_google_doodle_title()
    if doodle_title:
        print(f"Today's Google Doodle is \"{doodle_title}\"")
    else:
        print(f"No Google Doodle today :(")
