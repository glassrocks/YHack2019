import instaloader as insta
import wget
import subprocess
import os

def get_posts(user):
    IL = insta.Instaloader()
    IL.login('its_ian_costa', '1qaz2wsx')
    profile = insta.Profile.from_username(IL.context, user)
    return profile.get_posts()

def download(posts):
    iterator = 0
    for post in posts:
        url = post
        print(f'At post {iterator}')
        wget.download(url.url, str(iterator) +  '.jpg')
        iterator += 1
    print('Done')

def main():
    download(get_posts('yungjesusofficial'))
    print('Prog done')

if __name__ == '__main__':
    main()

