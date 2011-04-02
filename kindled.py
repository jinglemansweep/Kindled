#!/usr/bin/env python


import ConfigParser
import fcntl
import glob
import logging
import optparse
import os
import pprint
import shutil
import subprocess
import sys
from xdg import BaseDirectory

# Globals

project_id = "kindled"
project_name = "Kindle Daemon"
__revision__ = "0.10"
__docformat__ = "restructuredtext en"

# Base Configuration

logger = logging.getLogger(__name__)
LOG_HELP = ",".join(["%d=%s" % (4-x, logging.getLevelName((x+1)*10)) for x in xrange(5)])
LOG_FORMAT_CONS = "%(message)s"
LOG_FORMAT_FILE = "%(asctime)s %(name)s[%(process)d] %(levelname)10s %(message)s"
LOGLEVEL_DICT = {1:50, 2:40, 3:20, 4:10, 5:1}
DEFAULT_VERBOSITY = 3
LOG_DIVIDER = "=" * 70

cfg = ConfigParser.RawConfigParser()

# I18N

DEFAULT_LANGUAGE = "en"

STRINGS = {
    "en": {
        "NOTICE_CACHE_REMOVED": "Cache has been removed.",
        "NOTICE_PURGE_ALL": "All local configuration and cache data has been removed.",
    }
}

# MAIN FUNCTIONS ==============================

def read_configuration():

    DEFAULT_CONFIGURATION = {
        "general": {
            "ebookconvert_command": "ebook-convert"             
        },
        "mail": {
            "smtp_host": "smtp.gmail.com",
            "smtp_port": 25,
            "smtp_username": "user@gmail.com",
            "smtp_password": "password",
            "smtp_from_address": "user@gmail.com",
            "smtp_start_tls": True
        },
        "recipients": {
            "louis": "louis@free.kindle.com",
            "sarah": "sarah@free.kindle.com",
            "dewi": "dewi@free.kindle.com"
        },
        "groups": {
            "me": "louis",
            "family": "louis,sarah",
            "friends": "louis,sarah,dewi",
            "science_fans": "sarah,dewi"
        },
        "recipes": {
            "the_guardian": "/home/user/recipes/guardian.recipe",
            "the_times": "/home/user/recipes/times.recipe",
            "new_scientist": "/home/user/recipes/new_scientist.recipe"
        },
        "subscriptions": {
            "daily_news": "the_guardian,the_times;friends,family"
        }
    }

    config_folder = os.path.join(BaseDirectory.xdg_config_home, project_id)
    config_file = os.path.join(config_folder, "config.ini")
    cache_folder = os.path.join(config_folder, "cache")
        
    try: os.makedirs(config_folder)
    except OSError: pass
    try: os.makedirs(cache_folder)
    except OSError: pass
              
    if os.path.isfile(config_file):
        cfg.read(config_file)
    else:
        for section, options in DEFAULT_CONFIGURATION.iteritems():
            cfg.add_section(section)
            for k, v in options.iteritems():
                cfg.set(section, k, v)
        cfgfh = open(config_file, "wb")
        cfg.write(cfgfh)
        cfgfh.close()
        cfg.read(config_file) 

    cfg_general = dict(cfg.items("general"))
    cfg_mail = dict(cfg.items("mail"))
    cfg_recipients = dict(cfg.items("recipients"))
    cfg_recipes = dict(cfg.items("recipes"))
    raw_groups = dict(cfg.items("groups"))
    raw_subscriptions = dict(cfg.items("subscriptions"))
    cfg_groups = dict()
    for name, emails in raw_groups.iteritems():
        cfg_groups[name] = [email.strip() for email in emails.split(",")]
    cfg_subscriptions = dict()
    for name, opts in raw_subscriptions.iteritems():
        recipes = [recipe.strip() for recipe in opts.split(";")[0].split(",")]
        groups = [group.strip() for group in opts.split(";")[1].split(",")]
        cfg_subscriptions[name] = {"recipes": recipes, "groups": groups}

    config = {
        "general": cfg_general,
        "mail": cfg_mail,
        "recipients": cfg_recipients,
        "groups": cfg_groups,
        "recipes": cfg_recipes,
        "subscriptions": cfg_subscriptions
    }

    return config


def simple_shell(args, stdout=False):

    if stdout:
        rc = subprocess.call(args, shell=False)
    else:  
        rc = subprocess.call(args, shell=False, stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    return rc


# ARGUMENT PARSING

parser = optparse.OptionParser(usage="%prog or type %prog -h (--help) for help", description="", version=project_name+" v" + __revision__)

parser.add_option("-v", action="count", dest="verbosity", default=DEFAULT_VERBOSITY, help="Verbosity. Add more -v to be more verbose (%s) [default: %%default]" % LOG_HELP)
parser.add_option("-z", "--logfile", dest="logfile", default=None, help = "Log to file instead of console")

(options, args) = parser.parse_args()

# LOGGING

verbosity = LOGLEVEL_DICT.get(int(options.verbosity), DEFAULT_VERBOSITY)

if options.logfile is None:
    logging.basicConfig(level=verbosity, format=LOG_FORMAT_CONS)
else:
    logfilename = os.path.normpath(options.logfile)
    logging.basicConfig(level=verbosity, format=LOG_FORMAT_FILE, filename=logfilename, filemode="a")
    print >> sys.stderr, "Logging to %s" % logfilename

# MAIN EXECUTION

cfg = read_configuration()
cache_folder = cfg.get("cache_folder")



logger.info("Kindled")

cfg_groups = cfg.get("groups")
cfg_recipients = cfg.get("recipients")
cfg_recipes = cfg.get("recipes")
cfg_subs = cfg.get("subscriptions")

for sub_name, sub_opts in cfg_subs.iteritems():
    
    sent_recipients = []
    
    logger.info("Processing subscription '%s'..." % (sub_name))
    recipes, groups = sub_opts.get("recipes"), sub_opts.get("groups")
    
    for recipe_name in recipes:
        
        if not recipe_name in cfg_recipes:
            logger.warn("  Recipe '%s' not configured!" % (recipe_name))
            continue
            
        else:
            
            recipe_filename = cfg_recipes[recipe_name]
            logger.info("  Processing recipe '%s'..." % (recipe_name))
            
            if not os.path.exists(recipe_filename):
                logger.warn("    Recipe file '%s' does not exist!" % (recipe_filename))
                continue
            
            logger.info("    Generating recipe output...")
            
            ### Generation goes here
            
            for group_name in groups:
                
                if not group_name in cfg_groups:
                    logger.warn("      Group '%s' not configured!" % (group_name))
                    continue
                
                group_recipients = cfg_groups[group_name]
                logger.info("    Sending output to group '%s'..." % (group_name))
            
                for recipient_name in group_recipients:
                    
                    if not recipient_name in cfg_recipients:
                        logger.warn("      Recipient '%s' not configured!" % (recipient_name))
                        continue
                    
                    email_address = cfg_recipients[recipient_name]
                    
                    if email_address in sent_recipients:
                        logger.warn("      Already sent to recipient '%s'!" % (recipient_name))
                        continue
                    
                    logger.info("      Sending output to recipient '%s'..." % (recipient_name))
                        
                    ### Sending goes here
                    
                    sent_recipients.append(email_address)    
                    
        