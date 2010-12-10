#! /usr/bin/env python
#
# Dump schedconfig on a per-queue basis into cache files
#
#


from cacheschedconfig import cacheSchedConfig
from optparse import OptionParser


def main():
    parser = OptionParser()
    parser.add_option("-o", "--output", dest="dirname",
                      help="write cache outputs to DIR", metavar="DIR")

    (options, args) = parser.parse_args()

    cacher = cacheSchedConfig()    
    cacher.init(panda_config.dbhost, panda_config.dbpasswd, panda_config.dbuser, panda_config.dbname)
    cacher.getQueueData()
    
    for queue in cacher.queueData:
        cacher.dumpSingleQueue(queue)
        cacher.dumpSingleQueue(queue, dest = options.dirname, outputSet='pilot', format='pilot')
        cacher.dumpSingleQueue(queue, dest = options.dirname, outputSet='pilot', format='json')
        cacher.dumpSingleQueue(queue, dest = options.dirname, outputSet='all', format='json')
        cacher.dumpSingleQueue(queue, dest = options.dirname, outputSet='factory', format='json')


if __name__ == "__main__":
    main()

