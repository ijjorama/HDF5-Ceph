import h5py, sys
import numpy as np

import timeit

def myvisit(name, obj):
    if isinstance(obj, h5py.Dataset):
         print "len(%s) = %d, shape = %s, type = %s.\n" % \
             (name, obj.len(), obj.shape, obj.dtype)

         if obj.dtype == np.float64:
             print "Dataset %s is float64\n" % (name)

             data = obj[0:,0:,0:]             
#             data = obj[0:10,0:53,0:18]
#             print data.shape # "Type(data) == %s.\n" % (data.shape)
             print "Data takes up %d bytes.\n" % (data.nbytes)
             print(type(data))

             t = timeit.Timer(lambda: obj[0:,0:,0:])
             N = 1000
             timeperfetch = t.timeit(number = N) / N

             print "Time per fetch = %f, B/W = %.3f MB/s.\n" % \
                 (timeperfetch, data.nbytes/timeperfetch / pow(10, 6) )

    elif isinstance(obj, h5py.Group):
         print "%s is a group.\n" % name


def main():
    filename = sys.argv[1]
    f = h5py.File(filename, 'r')
    f.visititems(myvisit)

if __name__ == "__main__":
    main()
