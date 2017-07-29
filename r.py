class R:
    def __init__(self, **kw):
        self.update(**kw)

    def update(self, **kw):
        self.__dict__.update(kw)

    def copy(self):
        return R(**self.__dict__)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getattr__(self, attr):
        return None

    def __setattr__(self, attr, value):
        if value is not None:
            object.__setattr__(self, attr, value)
        elif attr in self.__dict__:
            del self.__dict__[attr]

    def __str__(self):
        s = ''
        for k, v in self.__dict__.items():
            if s != '':
                s += ', '
            s += str(k) + '=' + repr(v)
        return self.__class__.__name__ + '(' + s + ')'

    def __repr__(self):
        return str(self)
