
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        # 排除掉对Model类的修改；
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s' % name)

        # 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，
        # 就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，
        # 否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings
        attrs['__table__']=name
        return type.__new__(cls,name,bases,attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise Attribute(r"'Modal' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value

    def save(self):
        fields=[]
        params=[]
        args=[]
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))



class User(Model):
    id=IntegerField('id')
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')

# u=User(id=12345,name='Bianlin',email='biantest@orm.rgs',password='my-pwd')
