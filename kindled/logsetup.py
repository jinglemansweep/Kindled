import logging


class DefaultLogger(object):

    """ Logger Class """

    name = None
    default_verbosity = None


    def __init__(self, name="kindled", verbosity=3, log_file=None, default_verbosity=3):

        """ Constructor """

        self.name = name
        self.verbosity = verbosity
        self.log_file = log_file
        self.default_verbosity = default_verbosity
    

    def get_logger(self):

        """ Get Logger Instance """

        logger = logging.getLogger(self.name)
        help = ",".join(["%d=%s" % (4-x, logging.getLevelName((x+1)*10)) for x in xrange(5)])
        console_format = "%(message)s"
        file_format = "%(asctime)s %(name)s[%(process)d] %(levelname)10s %(message)s"
        log_levels = {1:50, 2:40, 3:20, 4:10, 5:1}

        verbosity = log_levels.get(int(self.verbosity), self.default_verbosity)

        if self.log_file is not None:

            log_filename = os.path.normpath(self.log_file)
            logging.basicConfig(level=verbosity, format=file_format, filename=log_filename, filemode="a")
            print >> sys.stderr, "Logging to %s" % log_filename

        else:

            logging.basicConfig(level=verbosity, format=console_format)

        return logger

