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
	bucket = conn.create_bucket(bucket_name)

	for b in conn.get_all_buckets():
		print "{name}\t{created}".format(
			name = b.name,
			created = b.creation_date,
		)




def listbucket(bucket):
	for key in bucket.list():
       		print "{name}\t{size}\t{modified}".format(
                	name = key.name,
	                size = key.size,
	                modified = key.last_modified,
       	         )

if __name__ == "__main__":
	main()
