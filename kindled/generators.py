
class CalibreEbookConvertGenerator(object):

    """ Calibre 'ebook-convert' Generator """
    
    _DESCRIPTION = "Calibre 'ebook-convert' Generator"

    format = None
    use_cache = None
    verbose = None
    logger = None


    def __init__(self, format="mobi", use_cache=False, verbose=False, logger=None):

        """ Constructor """

        self.format = format
        self.use_cache = use_cache
        self.verbose = verbose
        self.logger = logger

        self.logger.debug(self._DESCRIPTION)


    def generate(self, cfg):

        """ Generate """

        self.logger.debug("Generating...")
