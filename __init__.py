from django.contrib.admin.options import ModelAdmin

def manager(self):
    """
    Returns a Manager to be queried in the admin site. This is used by
    queryset, changelist_view, and delete_view.
    """
    if not hasattr(self, 'model_admin_manager'):
        self.model_admin_manager = self.model._default_manager
    return self.model_admin_manager
ModelAdmin.manager = manager

def manager_patch(func):
    """
    Temporarily changes the default manager. UGLY. FIXME.
    """

    def _do(self, *args, **kwargs):
        current_manager = self.model._default_manager
        self.model._default_manager = self.manager()
        try:
            return func(self, *args, **kwargs)
        finally:
            self.model._default_manager = current_manager
    return _do
ModelAdmin.queryset = manager_patch(ModelAdmin.queryset)
ModelAdmin.delete_view = manager_patch(ModelAdmin.delete_view)
ModelAdmin.change_view = manager_patch(ModelAdmin.change_view)
