from instagrapi import Client
import os

# Instagram credentials
instagram_username = 'YOUR_INSTAGRAM_USERNAME'
instagram_password = 'YOUR_INSTAGRAM_PASSWORD'

# Local directory containing posts
posts_directory = r'Pictures\ASTRO'

# Caption for the posts
caption = '#explore #feed '

# Initialize instagrapi client
client = Client()
client.login(instagram_username, instagram_password)

# Iterate over files in the directory
for filename in os.listdir(posts_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Construct full path to the post
        post_path = os.path.join(posts_directory, filename)

        # Upload post to Instagram with caption
        media = client.photo_upload(post_path, caption=caption)
        if media:
            print(f"Successfully uploaded {filename} to Instagram.")
        else:
            print(f"Failed to upload {filename} to Instagram.")

# Logout from Instagram
client.logout()
