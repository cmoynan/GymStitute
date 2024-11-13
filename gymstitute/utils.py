from allauth.account.template_loader import TemplateLoader as AllAuthTemplateLoader
from django.template.loaders.filesystem import Loader as FilesystemLoader
from django.template.utils import get_app_template_dirs

class TemplateLoader(AllAuthTemplateLoader):
    def get_template_sources(self, template_name, template_dirs=None):
        if template_name.startswith('account/') or template_name.startswith('socialaccount/'):
            # Add your base template directory to the search path
            template_dirs = list(get_app_template_dirs('templates')) + (template_dirs or [])

        # Call the parent class's get_template_sources method
        return super().get_template_sources(template_name, template_dirs)