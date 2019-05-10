from flask import render_template
import os
import markdown
from markdown.extensions import Extension


def load(app):

    def get_training_instructions():
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'instructions')
        try:
            lst = os.listdir(path)
        except OSError:
            pass  # ignore errors

        return lst 

    app.jinja_env.globals.update(get_training_instructions=get_training_instructions)

    @app.route("/page_trainings/<string:training>")
    def page_trainings(training):
        """
        render page by python-markdown with md-extentions
        :return: template
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        content_path = os.path.join(dir_path, 'instructions', training)
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