'''
Created on Sep 20, 2016

@author: KEVIN
'''
from django.contrib.syndication.views import Feed
from django.urls.base import reverse
from django.utils.feedgenerator import Atom1Feed

from results.models import Student


class RssSiteNewsFeed(Feed):
    name="name"
    city="city"
    link = "/sitenews/"
    address="look at me"
    def items(self):
        return Student.objects.order_by('-name')[:5]
    
    
    def item_name(self, item):
        return item.title
    def item_description(self, item):
        return item.address
# item_link is only needed if NewsItem has no get_absolute_url method.
    #def item_link(self, item):
        #return reverse('student', args=[item.pk])
    
class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.address
    
    