.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

==========================
 Auto Sign Up Event guest
==========================

The modules creates ``res.user`` from every ``event.registration`` (*attendee*)
and calls ``signup_prepare()`` method to allow to send an email with signup url to access the portal.

The modules adds email template ``Event: Signup``, which can be used directly or as an example to modify other email template.

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* `Ivan Yelizariev <https://it-projects.info/team/yelizariev>`__


Further information
===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/12.0/website_event_attendee_signup/


Tested on `Odoo 12.0 <https://github.com/odoo/odoo/commit/0aef3724c7772c99abdf8e9f850fc5289201ac6f>`_
