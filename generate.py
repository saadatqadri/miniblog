import os
import sys
import shutil
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown

POSTS = {}

for markdown_post in os.listdir('content'):
    file_path = os.path.join('content', markdown_post)

    with open(file_path, 'r') as file:
        # read metadata, skip over drafts:
        post = markdown(file.read(), extras=['metadata'])
        if not post.metadata['status'] == 'draft':
            POSTS[markdown_post] = post

POSTS = {
    post: POSTS[post] for post in sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
}

env = Environment(loader=PackageLoader('generate', 'templates'))
home_template = env.get_template('home.html')
post_template = env.get_template('post.html')

posts_metadata = [POSTS[post].metadata for post in POSTS]

tags = [post['tags'] for post in posts_metadata]
home_html = home_template.render(posts=posts_metadata, tags=tags)

# TODO: deal with static assets, copy from static folder to public


# delete current public folder
PATH = 'public' # TODO: move to config

try:
    shutil.rmtree(PATH)
except OSError as e:
    print("Error: {} - {}".format(e.filename, e.strerror))

try:
    os.mkdir(PATH)
except OSError:
    print ("Creation of the directory %s failed" % PATH)
else:
    print ("Successfully created the directory %s " % PATH)


with open('public/index.html', 'w') as file:
    file.write(home_html)

for post in POSTS:
    post_metadata = POSTS[post].metadata

    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date']
    }

    post_html = post_template.render(post=post_data)
    post_file_path = 'public/posts/{slug}.html'.format(slug=post_metadata['slug'])

    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html)


# copy static files
shutil.copy('static/styles.css', PATH)

"""lightcms

Easy to use CMS, based on Markdown

Usage: 
lightcms generate --skeleton
lightcms new 
""" 
