django-plans-i18n
=================

django-plans internationalization using django-modeltranslation.

Installation
============

Assuming you have correctly installed django-plans in your app you only need to add following apps to ``INSTALLED_APPS``::

    INSTALLED_APPS += ('modeltranslation', 'plans_i18n')

and you should also define your languages in django ``LANG`` variable, eg.::

    LANGUAGES = (
        ('pl', 'Polski'),
        ('en', 'English'),
        )

Please note that adding those to ``INSTALLED_APPS`` **changes** django models. Concretely it adds for every registered ``field`` that should translated, additional fields with name ``field_<lang_code>``, e.g. for given model::

    class MyModel(models.Model):
        name = models.CharField(max_length=10)

There will be generated fields: ``name``, ``name_en``, ``name_pl``.

You should migrate your database, using South is recommended::

    $ python manage.py schemamigration --auto plans
    $ python migrate plans

This app will also make all required adjustments in django admin.

For more info on how translation works in details please refer to
`django-modeltranslation docs
<https://django-modeltranslation.readthedocs.org/en/latest/>`_.
