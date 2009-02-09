django-admin-manager-monkey
===========================

Monkey patch the Django Admin system to allow specifying a manager that the
Admin system uses for accessing a model. This allows overriding the default
objects Manager to be more restrictive yet allowing the Admin system to show
everything via a non default manager.

Usage is simple. Add this app to your list of `INSTALLED_APPS`. In your
`admin.ModelAdmin` class, set `model_admin_manager` to a `models.Manager` and
it will get used instead.

    class MyModeAdmin(admin.ModelAdmin):
        model_admin_manager = MyModeAdmin.unfiltered
