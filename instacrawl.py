""" Downloads all pictures from an instagram account """
import instaloader

def find_posts(username):
    """ Returns an Instagram users posts """

    # Load instaloader
    IL = instaloader.Instaloader()
    # Login to Instagram
    IL.login("USERNAME", "PASSWORD")
    # Get profile from a username
    profile = instaloader.Profile.from_username(IL.context, username)

    # Return the profiles posts
    return profile.get_posts()


if __name__ == "__main__":
    posts = find_posts("USERNAME")

    for post in posts:
        print(post.url)
