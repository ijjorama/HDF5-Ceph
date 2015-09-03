import boto, boto.s3
from boto.s3.connection import S3Connection
import sys
from boto.s3.key import Key

import timeit

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


def getbytes(key, start, end):

	headers = {'Range': 'bytes={}-{}'.format(start, end) }
	return key.get_contents_as_string(headers=headers)

def main():
	conn = boto.connect_s3(host='gdss605.gridpp.rl.ac.uk', is_secure=False, 
		calling_format = boto.s3.connection.OrdinaryCallingFormat(), proxy=False)

	bucket_name = 'ijj-bucket-01'
	bucket = conn.get_bucket(bucket_name)
	
	objname = sys.argv[1]
	key = bucket.get_key(objname)

	start = sys.argv[2]
	end = sys.argv[3]

#	key.get_contents_to_filename(fileout, headers=headers, cb=percent_cb)

	contents = getbytes(key, start, end)   # key.get_contents_as_string(headers=headers)


	if len(contents) != int(end)-int(start)+1: # But range requested could be larger than size of whole file...
		print "Summat's gone wrong. Length is %d, should be %d\n" % (len(contents), end-start+1)

if __name__ == "__main__":
	main()
