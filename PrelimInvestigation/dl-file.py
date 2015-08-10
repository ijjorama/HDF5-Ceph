import boto, boto.s3
from boto.s3.connection import S3Connection
import sys
from boto.s3.key import Key



def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def main():
	conn = boto.connect_s3(host='gdss605.gridpp.rl.ac.uk', is_secure=False, 
		calling_format = boto.s3.connection.OrdinaryCallingFormat(), proxy=False)

	bucket_name = 'ijj-bucket-01'
	bucket = conn.get_bucket(bucket_name)
	objname = sys.argv[1]
        fileout = sys.argv[2]
        if len(sys.argv) == 4:
		headers = 2
	print "No. args = %d\n" % len(sys.argv)

	key = bucket.get_key(objname)
	headers = {'Range': 'bytes=0-1000000000'}
#	headers = None	
	key.get_contents_to_filename(fileout, headers=headers, cb=percent_cb)

if __name__ == "__main__":
	main()
