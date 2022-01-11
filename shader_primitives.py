### PRIMITIVE

class fixed2:
    def __init__(self, xu = 0.0, yv = 0.0):
        self.two = [xu, yv]
    def __copy__(self):
        return fixed2(*self.two[:])
    def __str__(self):
        return str(self.two)
    
    @property
    def x(self):
        return self.two[0]
    @x.setter
    def x(self, value):
        self.two[0] = value
    @property
    def u(self):
        return self.two[0]
    @u.setter
    def u(self, value):
        self.two[0] = value
    
    @property
    def y(self):
        return self.two[1]
    @y.setter
    def y(self, value):
        self.two[1] = value
    @property
    def v(self):
        return self.two[1]
    @v.setter
    def v(self, value):
        self.two[1] = value

    @property
    def xy(self):
        return self.two[:]
    @xy.setter
    def xy(self, value):
        self.two[:] = value[:]
    @property
    def uv(self):
        return self.two[:]
    @uv.setter
    def uv(self, value):
        self.two[:] = value[:]

class fixed4:
    def __init__(self, xr = 0.0, yg = 0.0, zb = 0.0, wa = 0.0):
        self.four = [xr, yg, zb, wa]
    def __copy__(self):
        return fixed4(*self.four[:])
    def __str__(self):
        return str(self.four)

    @property
    def x(self):
        return self.four[0]
    @x.setter
    def x(self, value):
        self.four[0] = value
    @property
    def r(self):
        return self.four[0]
    @r.setter
    def r(self, value):
        self.four[0] = value

    @property
    def y(self):
        return self.four[1]
    @y.setter
    def y(self, value):
        self.four[1] = value
    @property
    def g(self):
        return self.four[1]
    @g.setter
    def g(self, value):
        self.four[1] = value

    @property
    def z(self):
        return self.four[2]
    @z.setter
    def z(self, value):
        self.four[2] = value
    @property
    def b(self):
        return self.four[2]
    @b.setter
    def b(self, value):
        self.four[2] = value

    @property
    def w(self):
        return self.four[3]
    @w.setter
    def w(self, value):
        self.four[3] = value
    @property
    def a(self):
        return self.four[3]
    @a.setter
    def a(self, value):
        self.four[3] = value

    @property
    def rgb(self):
        return self.four[:3]
    @rgb.setter
    def rgb(self, value):
        self.four[:3] = value[:3]
    @property
    def xyz(self):
        return self.four[:3]
    @xyz.setter
    def xyz(self, value):
        self.four[:3] = value[:3]

    @property
    def rgba(self):
        return self.four[:]
    @rgba.setter
    def rgba(self, value):
        self.four[:] = value[:]
    @property
    def xyzw(self):
        return self.four[:]
    @xyzw.setter
    def xyzw(self, value):
        self.four[:] = value[:]

class shaderdata:
    def copy(self):
        newobj = self.__class__()
        for obj in dir(self):
            try:
                oldprop = getattr(self, obj)
                newprop = oldprop.__class__()
                if (hasattr(oldprop, "__copy__")):
                    newprop = oldprop.__copy__()
                setattr(newobj, obj, newprop)
            except Exception as error:
                #print(error) #Suppress non-writeable props error
                pass
        return newobj