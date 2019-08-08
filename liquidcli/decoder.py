from .data import Page


def decoder_shallowObject(decoded: object):
    def as_obj(raw: dict):
        for key in raw.keys():
            if hasattr(decoded, key):
                decoded.__setattr__(key, raw.get(key))
        return decoded
    return as_obj


def decoder_shallowList(cls):
    def a(raw: dict):
        decoded = cls()
        if type(raw) == list:
            decoded = raw
        for key in raw.keys():
            if hasattr(decoded, key):
                decoded.__setattr__(key, raw.get(key))
        return decoded
    return a


def decoder_Page(cls):
    def a(raw: dict):
        decoded = cls()
        if 'models' in raw:
            decoded = Page()
        for key in raw.keys():
            if hasattr(decoded, key):
                decoded.__setattr__(key, raw.get(key))
        return decoded
    return a
