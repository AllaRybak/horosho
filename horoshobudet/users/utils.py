from horoshobudet import settings


class DataMixin:
    default_image = None
    page_title = None
    extra_context = {}
    paginate_by = 5

    def __init__(self):
        if self.default_image:
            self.extra_context['default_image'] = self.default_image
        else:
            self.extra_context['default_image'] = settings.DEFAULT_USER_IMAGE
        if self.page_title:
            self.extra_context['title'] = self.page_title
        else:
            self.extra_context['title'] = 'Всё будет хорошо'

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context
