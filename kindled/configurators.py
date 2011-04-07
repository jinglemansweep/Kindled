import ConfigParser
import os

from xdg import BaseDirectory


class DefaultConfigurator(object):

    """ Configurator Class """

    configuration = {}
    config_name = None
    config_filename = None
    logger = None


    def __init__(self, config_name="kindled", config_filename=None, logger=None):

        """ Constructor """

        self.configuration = {}
        self.config_name = config_name
        self.config_filename = config_filename
        self.logger = logger


    def get_configuration(self):
        
        """ Perform Configuration """

        config_folder = os.path.join(BaseDirectory.xdg_config_home, self.config_name)
        config_file = os.path.join(config_folder, "config.ini")
            
        try: os.makedirs(config_folder)
        except OSError: pass

        cfg = ConfigParser.RawConfigParser()

        if not os.path.isfile(config_file):

            default_config = self.get_default_configuration()

            for section, options in default_config.iteritems():
                cfg.add_section(section)
                for k, v in options.iteritems():
                    cfg.set(section, k, v)

            cfgfh = open(config_file, "wb")
            cfg.write(cfgfh)
            cfgfh.close()
 
            self.logger.warn("No configuration found.")
            self.logger.warn("Generated default configuration at '%s'." % (config_file))
            return False

        else:

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

            if cfg_mail.get("smtp_from_address") == "user@gmail.com":
                
                self.logger.warn("Default example configuration found.")
                self.logger.warn("Please configure by modifying '%s'." % (config_file))
                return False

            try: os.makedirs(cfg_general.get("cache_folder"))
            except OSError: pass

            config = {
                "general": cfg_general,
                "mail": cfg_mail,
                "recipients": cfg_recipients,
                "groups": cfg_groups,
                "recipes": cfg_recipes,
                "subscriptions": cfg_subscriptions
            }

            return config


    def get_default_configuration(self):

        """ Gets Default Example Configuration Values """

        cfg = {
            "general": {
                "cache_folder": os.path.join(BaseDirectory.xdg_cache_home, self.config_name),
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

        return cfg


