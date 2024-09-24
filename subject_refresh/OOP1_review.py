class NameOfClass():
    # A class attribute. This value is shared by all instances of the class.
    class_attribute = 'value'

    # The __init__ method is a special method that's called when an instance is created.
    # It's typically used to initialize instance attributes.
    def __init__ (self, param1, param2):
        # self refers to the instance of the class.
        # param1 and param2 are parameters passed to the __init__ method.
        # Here, we're setting them as instance attributes.
        self.param1 = param1
        self.param2 = param2

    # An instance method. These methods can modify the instance and its attributes.
    # They can also access the class through self.__class__ attribute.
    def method(self):
        # code
        pass

    # A class method. These methods can't modify instance state (because they don't have access to self).
    # But they can modify class state.
    # 'cls' parameter is a reference to the class, not the instance.
    @classmethod
    def cls_method(cls, param1, param2):
        # code
        pass

    # A static method. These methods can't modify the class or instance state (because they don't have access to either).
    # They're restricted in what data they can access - and they're primarily a way to namespace your methods.
    @staticmethod
    def stc_method (param1, param2):
        # code
        pass
