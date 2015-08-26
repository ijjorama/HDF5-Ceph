
import boto, boto.s3
from boto.s3.connection import S3Connection
import sys
from boto.s3.key import Key

import timeit

def percent_cb(complete, total):
	sys.stdout.write('.')
	sys.stdout.flush()

def main():

	conn = boto.connect_s3(host='gdss605.gridpp.rl.ac.uk', is_secure=False, 
		calling_format = boto.s3.connection.OrdinaryCallingFormat(), proxy=False)

	bucket_name = 'ijj-bucket-01'
	bucket = conn.get_bucket(bucket_name)


	file = sys.argv[1]
	objname = sys.argv[2]

	k = Key(bucket)
	k.key = objname
        
	from timeit import Timer
# Really want to set contents from string, that is read file contents into string before starting timer

	t = Timer(lambda: k.set_contents_from_filename(file)) 

	print t.timeit(number=1)

def listbucket(bucket):
	for key in bucket.list():
       		print "{name}\t{size}\t{modified}\n".format(
                	name = key.name,
	                size = key.size,
	                modified = key.last_modified,
       	         )

if __name__ == "__main__":
	main()
