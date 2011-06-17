from tg import expose, request

from myapp.lib.base import BaseController
from myapp import model

__all__ = ['MovieController']

import tw2.core
import tw2.forms
import tw2.sqla

class MovieForm(tw2.sqla.DbFormPage):
    entity = model.Movie
    title = 'Movie'
    resources = [tw2.core.CSSLink(link='/css/myapp.css')]
    class child(tw2.forms.TableForm):
        action = '/tw2_controllers/movie_submit'
        id = tw2.forms.HiddenField()
        title = tw2.forms.TextField(validator=tw2.core.Required)
        director = tw2.forms.TextField()
        genres = tw2.sqla.DbCheckBoxList(entity=model.Genre)
        class cast(tw2.forms.GridLayout):
            extra_reps = 5
            character = tw2.forms.TextField()
            actor = tw2.forms.TextField()


class MovieIndex(tw2.sqla.DbListPage):
    entity = model.Movie
    title = 'Movies'
    newlink = tw2.forms.LinkField(link='/movie/movie', text='New', value=1)
    class child(tw2.forms.GridLayout):
        title = tw2.forms.LabelField()
        id = tw2.forms.LinkField(link='/movie/movie?id=$', text='Edit', label=None)


class MovieController(BaseController):

    @expose('myapp.templates.widget')
    def index(self, **kw):
        w = MovieIndex.req()
        w.fetch_data(request)
        return dict(widget=w, page='movie')

    @expose('myapp.templates.widget')
    def movie(self, *args, **kw):
        w = MovieForm(redirect='/movie/').req()
        w.fetch_data(request)
        mw = tw2.core.core.request_local()['middleware']
        mw.controllers.register(w, 'movie_submit')
        return dict(widget=w, page='movie')
