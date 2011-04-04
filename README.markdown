Kindled
=======

Kindled is a simple command line tool that controls the production of
Kindle MOBI files from Calibre recipes.

Configuration of Kindled involves specifying various different
components within the configuration file.

Kindled will automatically generate a default example configuration file
when first run. It is usually located in "~/.config/kindled/kindled.ini".

You will need to modify the configuration file before running again as
Kindled will detect the example configuration and will exit.

Apart from the general configuration parameters and the email server
configuration, Kindled comprises of four main items:

* Recipes
* Recipients
* Groups
* Subscriptions

Recipes
-------

You can add your favourite Calibre recipes within the configuration file
by simply adding the path and filename to it (along with a friendly unique
identifier).

Examples:

    the_times = ~/recipes/TheTimes.recipe
    the_guardian = ~/recipes/TheGuardian.recipe

Recipients
----------

Recipients are basically people (or destinations). A recipient would
primarily be a Kindle "free" email address (e.g. user@free.kindle.com).
As with other items, you will need to give each recipient a friendly
unique identifer.

Examples:

    me = me@free.kindle.com
    brother = my_brother@free.kindle.com
    best_friend = best_friend@free.kindle.com

Groups
------

Groups are one or more recipients. If you only want to publish to a
single recipient, you will still need to define a group and simply add
the single recipient to it. Groups are simply comma delimited lists
of recipient friendly names (not the email address). Groups also require
a friendly unique identifier.

Examples:

    me = me
    family = brother
    friends = best_friend
    everyone = me,brother,best_friend

Subscriptions
-------------

A subscription combines recipes with groups. It consists of a comma
delimited list of recipe friendly names, followed by a semi-colon and
then a comma delimited list of groups.

Examples:

    guardian_family = the_guardian;family
    times_friends_and_me = the_times;me,friends
    everything = the_guardian,the_times;everyone

