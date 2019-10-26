""" Downloads all pictures from an instagram account """
import instaloader
from InstagramAPI import InstagramAPI

def find_posts(username):
    """ Returns an Instagram users posts """

    # Load instaloader
    IL = instaloader.Instaloader()
    # Login to Instagram
    #IL.login("USERNAME", "PASSWORD")
    # Get profile from a username
    profile = instaloader.Profile.from_username(IL.context, username)

    # Return the profiles posts
    return profile.get_posts()

def message_users(user_ids: list, message):
    I_API = InstagramAPI("its_ian_costa", "1qaz2wsx")
    I_API.login()  # login
    I_API.direct_message(message, user_ids)


if __name__ == "__main__":
    posts = find_posts("donniefinn")
    id = None

    for post in posts:
        print(post.url)
        id = post.owner_id

    message_users([id], "Hey Donnie what's up")
