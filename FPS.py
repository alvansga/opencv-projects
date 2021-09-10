import datetime
import time

class FPS:
	def __init__(self):
		self._start = 0
		self._end = 0
		self._numFrames = 0
		
	def start(self):
		self._start = time.time() #datetime.datetime.now()
		return self
		
	def stop(self):
		self._end = time.time() #datetime.datetime.now()
	
	def update(self):
		self._numFrames += 1
		
	def elapsed(self):
		return (self._end - self._start) #.total_second()
		
	def fps(self):
		return self._numFrames / self.elapsed()
