from django.conf.urls import url
from polls.views import PollListView, PollDetailView

class PollsApphook(CMSApp):
    # ...
    def get_urls(self, page=None, language=None, **kwargs):
        return [
            url(r'^$', PollListView.as_view()),
            url(r'^(?P<slug>[\w-]+)/?$', PollDetailView.as_view()),
        ]