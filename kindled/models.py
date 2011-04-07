
class Recipe(object):

    """ Recipe Class """

    name = None
    filename = None

    def __init__(self, name, filename):

        """ Constructor """

        self.name = name
        self.filename = filename


class Recipient(object):

    """ Recipient Class """

    name = None
    email_address = None


    def __init__(self, name, email_address):

        """ Constructor """

        self.name = name
        self.email_address = email_address


class Group(object):

    """ Group Class """

    name = None
    recipients = None


    def __init__(self, name, recipients=None):
        
        """ Constructor """

        self.name = name
        
        if recipients is None:
            self.recipients = [] 
        elif isinstance(recipients, list):
            self.recipients = recipients
        else:
            self.recipients = [recipients]


    def add_recipients(self, recipient):

        """ Adds Recipient To Group """

        if isinstance(recipients, list):
            self.recipients.extend(recipients)
        else:
            self.recipients.append(recipients)


class Subscription(object):

    """ Subscription Class """

    name = None
    groups = None
    recipes = None

    def __init__(self, name, groups=None, recipes=None):

        """ Constructor """

        self.name = name

        if groups is None:
            self.groups = []
        elif isinstance(groups, list):
            self.groups = groups
        else:
            self.groups = [groups]


    def add_groups(self, groups):

        """ Adds Groups To Subscription """

        if isinstance(groups, list):
            self.groups.extend(groups)
        else:
            self.groups.append(groups)  


    def add_recipes(self, recipes):

        """ Adds Recipes To Subscription """

        if isinstance(recipes, list):
            self.recipes.extend(recipes)
        else:
            self.recipes.append(recipes)  
