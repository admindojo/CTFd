from flask import render_template, send_from_directory, request
import os
import markdown
from markdown.extensions import Extension
from CTFd.cache import cache, make_cache_key
import re


def load(app):

    def get_training_instructions():
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'instructions')
        reg = re.compile(r'^\.')
        try:

            lst = [x for x in os.listdir(path) if not reg.match(x)]
        except OSError:
            pass  # ignore errors

        return lst 

    app.jinja_env.globals.update(get_training_instructions=get_training_instructions)

    @app.route("/instructions/<string:training>")
    @cache.cached(timeout=60)
    def page_trainings(training):
        """
        render page by python-markdown with md-extentions
        :return: template
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        content_path = os.path.join(dir_path, 'instructions', os.path.join(training + os.path.extsep + 'md'))
        mdextensions = ['pymdownx.details']
        md = markdown.Markdown(extensions=mdextensions)

        return render_template('page_content.html', content=md.convert(open(content_path).read()))


    @app.route("/about")
    def page_about():
        """
        render page by python-markdown with md-extentions
        :return: template
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        content_path = os.path.join(dir_path, 'pages', 'about.md')
        mdextensions = ['pymdownx.details']
        md = markdown.Markdown(extensions=mdextensions)

        return render_template('page_content.html', content=md.convert(open(content_path).read()))

    @app.route("/faq")
    def page_faq():
        """
        render page by python-markdown with md-extentions
        :return: template
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        content_path = os.path.join(dir_path, 'pages', 'faq.md')
        mdextensions = ['pymdownx.details']
        md = markdown.Markdown(extensions=mdextensions)

        return render_template('page_content.html', content=md.convert(open(content_path).read()))

    @app.route("/getting-started")
    def page_gettingstarted():
        """
        render page by python-markdown with md-extentions
        :return: template
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        content_path = os.path.join(dir_path, 'pages', 'getting-started.md')
        mdextensions = ['pymdownx.details']
        md = markdown.Markdown(extensions=mdextensions)

        return render_template('page_content.html', content=md.convert(open(content_path).read()))

    @app.route('/robots.txt')
    def static_from_root():
        """
        return robot.txt
        :return: robot.txt
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))

        return send_from_directory(dir_path, request.path[1:])
