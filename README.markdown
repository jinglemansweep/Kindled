Kindled
=======

[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=jinglemansweep&url=https://github.com/jingleman/Kindled&title=Kindled&language=&tags=github&category=software)

Kindled is a simple command line tool that controls the production of
Kindle MOBI files from Calibre recipes.

Installation
------------

Kindled is now available on [PyPI](http://pypi.python.org/pypi/kindled/).
You can install Kindled via **easy_install** as follows:

    sudo easy_install kindled
    
If you do not have **easy_install** installed, it can be installed using
your package manager. For example, using Ubuntu/Debian:

    sudo aptitude install python-setuptools

The [Calibre](http://calibre-ebook.com/) ebook conversion suite is required
for Kindled to operate. However, Kindled is designed to run headless without
a GUI as it uses the `ebook-convert` command line tool that is supplied with
Calibre.

To install Calibre on Ubuntu, you can simply install the package from
the official repositories:

    sudo aptitude install calibre

To install Kindled manually, simply copy the `bin/kindled` script somewhere
on your configured PATH and run it.

Configuration
-------------

Configuration of Kindled involves specifying various different
components within the configuration file.
Kindled will automatically generate a default example configuration file
when first run. It is usually located in `~/.config/kindled/kindled.ini`.
You will need to modify the configuration file before running again as
Kindled will detect the example configuration and will exit.

Apart from the general configuration parameters and the email server
configuration, Kindled comprises of four main items:

* Recipes
* Recipients
* Groups
* Subscriptions

### Recipes

You can add your favourite Calibre recipes within the configuration file
by simply adding the path and filename to it (along with a friendly unique
identifier).

Examples:

    the_times = ~/recipes/TheTimes.recipe
    the_guardian = ~/recipes/TheGuardian.recipe

### Recipients

Recipients are basically people (or destinations). A recipient would
primarily be a Kindle "free" email address (e.g. user@free.kindle.com).
As with other items, you will need to give each recipient a friendly
unique identifer.

Examples:

    me = me@free.kindle.com
    brother = my_brother@free.kindle.com
    best_friend = best_friend@free.kindle.com

### Groups

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

### Subscriptions

A subscription combines recipes with groups. It consists of a comma
delimited list of recipe friendly names, followed by a semi-colon and
then a comma delimited list of groups.

Examples:

    guardian_family = the_guardian;family
    times_friends_and_me = the_times;me,friends
    everything = the_guardian,the_times;everyone

Usage
-----

By default, if you just run Kindled as normal, it will process all
configured subscriptions. However, if you only want to process specific
subscriptions, you can simply add the friendly names of the subscriptions
you want to process as arguments (separated by a space).

Processed all subscriptions:

    kindled
    
Processes only `guardian_family` and `times_friends_and_me` subscriptions:

    kindled guardian_family times_friends_and_me
    
Specifying certain subscriptions is useful for scheduled (cron) tasks.
For example, you can have Kindled appear in your crontab more than once
on different schedules, but processing different subscriptions.

By default, Kindled will cache all produced content in the configured
cache folder, which is by default `~/.cache/kindled`. If you want to
override the cache, you can either clear the contents of the cache folder
or run Kindled with the `-f` or `--force`` option.

If you want to test Kindled and not actually send any emails to your
recipients, run Kindled with the `-t` or `--test` option.
Also, if you want to see the output of the Calibre conversion process,
run Kindled with the `-d` or `--debug` option. All options and arguments
can be obtained by using the `--help` option.
