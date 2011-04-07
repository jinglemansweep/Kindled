from kindled.configurators import DefaultConfigurator
from kindled.generators import CalibreEbookConvertGenerator
from kindled.logsetup import DefaultLogger
from kindled.publishers import SmtpEmailPublisher


class DefaultController(object):

    """ Default Controller """

    _DESCRIPTION = "Default Controller"

    options = None
    args = None
    logger = None
    configurator = None
    generator = None
    publisher = None


    def __init__(self, options, args):

        """ Constructor """

        self.options = options
        self.args = args
        self.logger = DefaultLogger(name="kindled", verbosity=options.verbosity).get_logger()
        self.configurator = DefaultConfigurator(logger=self.logger)
        self.generator = CalibreEbookConvertGenerator(logger=self.logger)
        self.publisher = SmtpEmailPublisher(logger=self.logger)

        self.logger.debug(self._DESCRIPTION)


    def execute(self):

        """ Main Controller Execution """

        cfg = self.configurator.get_configuration()
        
        self.logger.debug("Starting...")

        self.generator.generate(cfg)
        self.publisher.publish(cfg)


