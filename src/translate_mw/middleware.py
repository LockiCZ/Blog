from translate_mw.utils import load_translations, get_lang_id
from django.utils.functional import SimpleLazyObject

class TranslationMiddleware:
    async_capable = False
    sync_capable = True

    def __init__(self, get_response):
        self.get_response = get_response
        self.translations = load_translations()
    
    def get_lang_data(self, request):
        lang = get_lang_id(request)

        if lang in self.translations:
            if request.path in self.translations[lang]:    
                return self.translations[lang][request.path]
            else:
                return self.translations[lang]["."]
        else:
            if request.path in self.translations["en"]:    
                return self.translations["en"][request.path]
            else:
                return self.translations["en"]["."]

    def __call__(self, request):
        request.locals = SimpleLazyObject(lambda: self.get_lang_data(request))
        
        response = self.get_response(request)
    
        return response

    async def __acall__(self, request):
        pass # not implemented
