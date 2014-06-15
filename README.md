# quotes 
## What is quotes ?
*quotes* is a webapp designed to be a quote management system. What for ?
Because at work, in your university promotion there are those guys who
keep saying cult phrases or random (but funny) stuff and the whiteboard
you use to store them has not an infinite memory. *quotes* is here to solve
the problem !

## How do I run it ?
*quotes* is a webapp deveopped in Python and using the framework cherrypy
and the templating language mako. It uses sqlite to store the datas and
is very light as a consequence since it does not require any heavy database
management system like MySQL or Postgres. You simply run `./quotes.py` in
the source folder and the application will start on the port 8080.

I would recommand to run it in a more premanent way behind Nginx or
Apache with [uWSGI](http://uwsgi-docs.readthedocs.org/en/latest/). I will
post a section of the documentation for that later on, don't worrie.

## How does it work ?
It provides quotes to people visiting the website, **but** since some quotes
may be sensitive it requires an identification to proceed. When you first
launch the software, there are no quote, no database and basically nothing
as a data. So the software will create the database file and insert a user
in it *admin* with the password *password*. Login and change it, then you
can start to create your users.

The permission system is quite basic. Anyone can create a quote, but only
the original authors (or *admin*) can delete or edit a quote. Don't spam,
a ban system will be implemented later on.

Have fun :)
