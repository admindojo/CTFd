from flask import render_template
import os
import markdown
from markdown.extensions import Extension


def load(app):

    def make_tree():
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pages' )
        tree = dict()
        try:
            lst = os.listdir(path)
        except OSError:
            pass  # ignore errors
        else:
            for name in lst:
                fn = name
                tree.update(dict(name=fn))
        return lst 

    app.jinja_env.globals.update(make_tree=make_tree)

    @app.route("/page_trainings/<string:training>")
    def page_trainings(training):
        """
        render page by python-markdown with md-extentions
        :return: template
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        content_path = os.path.join(dir_path, 'pages', training)
        mdextensions = ['pymdownx.details']
        md = markdown.Markdown(extensions=mdextensions)



        return render_template('page_content.html', content=md.convert(open(content_path).read()))
