import boto, boto.s3
from boto.s3.connection import S3Connection
import sys
from boto.s3.key import Key
import timeit

def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped

def getbytes(key, start, end):

	headers = {'Range': 'bytes={}-{}'.format(start, end) }
	key.get_contents_as_string(headers=headers)

def main():
	conn = boto.connect_s3(host='gdss605.gridpp.rl.ac.uk', is_secure=False, 
		calling_format = boto.s3.connection.OrdinaryCallingFormat(), proxy=False)

	bucket_name = 'ijj-bucket-01'
	bucket = conn.get_bucket(bucket_name)
	objname = sys.argv[1]
	key = bucket.get_key(objname)

	start = sys.argv[2]
	end = sys.argv[3]

	length = int(end) - int(start)
        from timeit import Timer
	t = Timer(lambda: getbytes(key, start, end))   

	n = 100
	timeperfetch =  t.timeit(number=n) / float(n) 
	print "%d\t%.3f\t%.2f\n" % (length, timeperfetch, length / timeperfetch / pow(10,6) )

if __name__ == "__main__":
	main()
