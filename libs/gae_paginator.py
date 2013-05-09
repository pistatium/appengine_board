# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, Page

'''
Django Paginator for AppEngine
 cf. http://stackoverflow.com/questions/2679370/extend-django-core-paginator-paginator-to-work-with-google-app-engine

db:  fetch(self.per_page, offset)
=>
ndb: fetch(self.per_page, offset= offset)
'''
class GAEPaginator(Paginator):
    def page(self, number):
      number = self.validate_number(number)
      offset = (number - 1) * self.per_page
      if offset+self.per_page + self.orphans >= self.count:
        top = self.count
      return Page(self.object_list.fetch(self.per_page, offset = offset), number, self)
