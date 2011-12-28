import urllib
import os
from threading import Thread

url_pattern = 'http://stdweb2.korean.go.kr/search/View.jsp?idx=%d'

def clip_thread(index, bucket):
	start = index * bucket + 1
	for n in range(start, start + bucket):
		urllib.urlretrieve(url_pattern % n, '%02d/%d.html' % (index, n))
		print '%02d/%d.html' % (index, n)

if __name__ == '__main__':
	index_count = 600000
	thread_count = 60
	bucket = index_count / thread_count
	for n in range(0, thread_count):
		os.makedirs("%02d" % n)
		Thread(target=clip_thread, args=(n, bucket)).start()
