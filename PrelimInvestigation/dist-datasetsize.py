import h5py
import sys
import numpy as np

#import h5pyd

import timeit


def myvisit(name, obj):
    if isinstance(obj, h5py.Dataset):
         print "len(%s) = %d, shape = %s, type = %s.\n" % \
             (name, obj.len(), obj.shape, obj.dtype)

         if obj.dtype == np.float64 or obj.dtype == np.float32:
             thresh = 5*pow(10,6)

             data = obj[:] # 0:,0:,0:]             
#             data = obj[0:10,0:53,0:18]
#             print data.shape # "Type(data) == %s.\n" % (data.shape)



             if data.nbytes > thresh:

                 t = timeit.Timer(lambda: obj[:])
                 N = 10 # 000
                 timeperfetch = t.timeit(number = N) / N

                 print "\t%s: size = %d,  Time per fetch = %f, B/W = %.3f MB/s.\n" % \
                     (name, data.nbytes, timeperfetch, data.nbytes/timeperfetch / pow(10, 6) )

    elif isinstance(obj, h5py.Group):
         print "%s is a group.\n" % name

def getFile(filename, mode, endpoint=None):
    
    if endpoint is None: # Could poss use conditional assignment here, apart from import?
        file = h5py.File(filename, mode)
    else:
        import h5pyd
        file = h5pyd.File(filename, mode, endpoint)
    return file

def fetchds(f, dsetname):
    d = f[dsetname]
    
def main():
    if len(sys.argv) < 1:
        sys.exit("Must supply at least <filename> [<endpoint>]")
    filename = sys.argv[1]
    if len(sys.argv) == 3:
        endpoint = sys.argv[2] 
    else: 
        endpoint = None
    f = getFile(filename, 'r', endpoint)
        
    t = timeit.Timer(lambda: fetchds(f, name))
    
    name = 'inhomogeneity_in_latitude'
       

    N = 10
    timeperfetch = t.timeit(number = N)/N
    
    d = f[name]
    data = d[:]
    
    typ = d.dtype
    # @type data 
    dsize = data.nbytes
    
    
    print "\t%s: size = %d, type = %s,  Time per fetch = %f, B/W = %.3f KB/s.\n" % \
                     (name, dsize, typ, timeperfetch, d.len()/timeperfetch / pow(10, 3) )
    
#    f.visititems(myvisit)

if __name__ == "__main__":
    main()
