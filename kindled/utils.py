import optparse
import subprocess

from kindled.controllers import DefaultController


def bootstrap():

    """ Command Line Bootstrap Function """

    usage = "%prog or type %prog -h (--help) for help"
    description = "Kindled"
    version = "v0.1"

    parser = optparse.OptionParser(usage=usage, description=description, version=version)

    parser.add_option("-v", 
                      action="count", 
                      dest="verbosity", 
                      default=3, 
                      help="Verbosity. Add more -v to be more verbose (%s)")

    parser.add_option("-z", 
                      "--logfile", 
                      dest="logfile", 
                      default=None, 
                      help="Log to file instead of console")

    parser.add_option("-f", 
                      "--force", 
                      dest="force", 
                      action="store_true",
                      default=False, 
                      help="Force generation of content, ignoring cached content")

    parser.add_option("-t", 
                      "--test", 
                      dest="test", 
                      action="store_true", 
                      default=False,    
                      help="Perform test run (disables email sending)")

    parser.add_option("-d", 
                      "--debug", 
                      dest="debug", 
                      action="store_true", 
                      default=False, 
                      help="Run in debug mode (outputs Calibre messages)")

    (options, args) = parser.parse_args()
    
    controller = DefaultController(options=options, args=args)
    controller.execute()


def simple_shell(args, stdout=False):

    """ Simple Subprocess Shell Helper Function """

    if stdout:
        rc = subprocess.call(args, shell=False)
    else:  
        rc = subprocess.call(args, shell=False, stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    return rc
