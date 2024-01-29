from rest_framework.renderers import JSONRenderer

class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {
            'authored_by': 'PT. Awantech Solution',
            'version': '1.0.0',
            'status': 'success',
            'data': data
        }
        return super(CustomRenderer, self).render(response_data, accepted_media_type, renderer_context)
