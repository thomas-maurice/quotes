# quotes 
A quote management system, because the office's whiteboard is too mainstream

## What is quotes ?
*quotes* is a webapp designed to be a quote management system. What for ?
Because at work, in your university promotion there are those guys who
keep saying cult phrases or random (but funny) stuff and the whiteboard
you use to store them has not an infinite memory. *quotes* is here to solve
the problem !

## How do I run it ?
You simply run `./quotes.py` in
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

## Functionnalities !
The webapp is split in several pages. The main pages displays five random
quotes on a pannel, and the five most recent on the other.

The second page display all the quotes.

The third allow you to add some quotes.

The fourth is not implemented yet, it's a surprise ;)

Finally the admin will se a "User" tab to manage them.

And then a "Profile" and "Logout" page.

As simple as that :)

## Which technologies does it use ?
*quotes* is a webapp deveopped in Python and using the framework cherrypy
and the templating language mako. It uses sqlite to store the datas and
is very light as a consequence since it does not require any heavy database
management system like MySQL or Postgres.

So the python dependecies for this project are :
 
 * python-cherrypy3
 * python-mako
 * python-sqlite3
 * python-sqlobject
 * python-yaml

For all the design stuff it uses [Bootstrap](http://getbootstrap.com/),
[jQuery](https://jquery.com/) [Chart.js](http://www.chartjs.org/)
[Font Awesome](https://fortawesome.github.io/Font-Awesome/)
and [Hint.css](http://kushagragour.in/lab/hint/)

## Running in a virtalenv
Normally, *quotes* is runnable within a VirtualEnv, so to install all the
needed dependencire just create your virtual environement and run within
it the command `pip install -r virtualenv.requirements` and it should do it.

Have fun :)
