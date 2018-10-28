import sys
import datetime
import locale as locale
from itertools import repeat
error = valueerror


class illegalmontherror(valueerror):
	def init (self,month):
		self.month = month
		def str(self):
			return "bad month number %r; must be 1-12" % self.month
