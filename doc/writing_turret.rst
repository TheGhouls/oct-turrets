Writing your own turret
=======================

The turret configuration
------------------------

As you can see in the python-turret example (in the GitHub repository), a turret must be able to read and understand this
type of configuration file :

.. code-block:: json

    {
        "name": "navigation",
        "cannons": 50,
        "rampup": 10,
        "script": "v_user.py",
        "turret_class": "my_module.MyTurret",
        "cannon_class": "my_module.MyCannon"
    }

For a full list of the available options see *`Writing your own turret`_*.
A Python turret comes with the following options:


* ``turret_class``: Full Python path to the a subclass of `oct_turrets.turret.Turret`
* ``cannon_class``: Full Python path to the a subclass of `oct_turrets.cannon.Cannon`

.. _Writing your own turret: http://oct.readthedocs.io/en/latest/writing_turret.html


Document your turret
--------------------

Simply put: please, document your turret !

We expect to create a list to reference all available turrets, and if your turrets doesn't have a documentation, we will refuse
to list it.

But keep in mind that for many case, a simple README is enough. At the very least, tell your users how to install and start your turret.
