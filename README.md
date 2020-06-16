## Minimal blogging system

### Design considerations

- Simple, easy to use, extendable
- Write articles in Markdown, and generate content in HTML. Simple styling options
- see example at [https://saadatqadri.com](https://saadatqadri.com)

Only tested on Python 3.7

### Installation

- Clone repo into `{{your code folder}}/blog`
- Create `virtualenv`
- Run `pip install -r requirements.txt`

### Generating site

- Run `python3 generate.py`

This will output files into a `/public` folder.

Any article with a `status` tag "published" in the Markdown file will be generated, everything else is ignored.

For local testing, `cd public` and then run `python3 -m http.server 8000 --directory /public/`, and then point your browser to `127.0.0.1:8000` or `localhost:8000`.

### Deploying 

#### Github pages

Follow the instructions [here](https://help.github.com/en/github/working-with-github-pages/getting-started-with-github-pages).

Configure the publishing source to `/public` as described [here](https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) 

#### Gitlab pages

Coming soon.


### TODOs

Warning: this is hacky and sad code, it was optimized for haste to put something out there. Needs an insane amount of work before it can be considered `production grade`.

- Tests
- Static folder
- CI/CD pipeline
- Official python packaging
- Home should be generated from Markdown file
- Make *everything* configurable
- SEO fundamentals


