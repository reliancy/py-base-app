"""
We will use this script to perform measurements on the library.
Also maybe we can use it to implement certain managmenet tasks.
"""
from rfeature import types
from rfeature import util
import argparse


def init_args():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-v","--verbose",required=False,help="level of verbosity",default="debug",choices=["debug","warning","warn","info","error"])
    ap.add_argument("--log-dir",required=False,help="log directory to write")
    #ap.add_argument("-bs","--batch_size",required=True,help="size of each batch",type=int)
    #ap.add_argument("-d","--directory",required=True,help="drectory which should be chunked")
    #ap.add_argument("-o","--output",required=False,help="output directory for chunks")
    args=ap.parse_args()
    util.put(util.LOG_LEVEL,args.verbose)
    util.put(util.LOG_DIR,args.log_dir)
    pass

if __name__=='__main__':
    util.init(argparser=init_args)    
    path=util.data_path("watch.jpg")
    util.log_info(f"file:{path}")
    print(types.capital_case("car"))
    pass