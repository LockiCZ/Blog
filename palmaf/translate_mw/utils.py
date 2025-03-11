import os
import json


def load_language(lang, dir_name):
    out = dict()
    for root, _, files in os.walk(dir_name):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    lang_data = json.load(f)
                    lang_data["lang"] = lang
                    out["/" + file_name[:-len(".json")]] = lang_data
                    
    if "/index" in out:
        out["/"] = out["/index"]
    return out


def load_translations():
    if os.getenv("TRANSLATIONS_DIR"):
        base_dir = os.getenv("TRANSLATIONS_DIR")
    else:
        base_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "locals")

    out = dict()
    for dir_name in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, dir_name)):
            out[dir_name] = load_language(dir_name, os.path.join(base_dir, dir_name))
    return out


def get_lang_id(request):
    if request.COOKIES.get("lang"):
        return request.COOKIES.get("lang")
    
    if "HTTP_ACCEPT_LANGUAGE" in request.META:
        return request.META["HTTP_ACCEPT_LANGUAGE"][:2]
    
    return "en"

