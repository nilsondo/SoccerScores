try:
    import cPickle as pickle
except:
    import pickle
import os


class Annotator:

    '''
    Annotator class.
    '''

    __file = os.path.abspath(os.path.join(os.getcwd(), 'annotator.pickle'))

    def __init__(self):
        '''
        Constructor
        '''
        self.__matches = {}
        self.__views = set()

    @property
    def views(self):
        '''
        Getter for the view attribute.
        '''
        return self.__views

    @views.setter
    def views(self, value):
        '''
        Setter for the view attribute.
        '''
        self.__views = value

    def add_view(self, view):
        '''
        Add the given view to the views set.
        '''
        self.views.add(view)
        self.notify_annotator_change()

    def remove_view(self, view):
        '''
        Remove the given view of the views set.
        '''
        if len(self.views) > 0:
            try:
                self.views.remove(view)
            except:
                return None
        else:
            return None

    @classmethod
    def create(cls):
        '''
        Create a new instance of the class Annotator.
        '''
        return cls()

    @classmethod
    def load(cls):
        '''
        Load the already created Annotator object.
        '''
        try:
            handle = open(cls.__file, 'rb')
            obj = pickle.load(handle)

            if isinstance(obj, Annotator):
                return obj
            else:
                return cls.create()

            handle.close()
        except:
            return cls.create()

    def save(self):
        '''
        Save the current object state in a static location.
        '''
        with open(self.__file, 'wb') as handle:
            pickle.dump(self, handle)

    def add_match(self, match):
        '''
        Add the given match to the matches list.
        '''
        self.__matches[match.mid] = match
        self.notify_annotator_change()

    def remove_match(self, match):
        '''
        Remove the given match of the matches list.
        '''
        if len(self.__matches) > 0:
            try:
                del self.__matches[match.mid]
                self.notify_annotator_change()
            except:
                return None
        else:
            return None

    def get_match(self, mid):
        '''
        Returns the the Match object given a valid mid.
        '''
        if isinstance(mid, str):
            try:
                return self.__matches[mid]
            except:
                return None
        else:
            return None

    @property
    def matches(self):
        '''
        Getter for the matches attribute.
        '''
        return self.__matches

    def display(self):
        '''
        Return the string format description for the given match.
        '''
        str_matches = {}

        for mid, match in self.matches.iteritems():
            str_matches[mid] = match.display()

        return str_matches

    def notify_annotator_change(self):
        '''
        Notify any annotator change to a listed views.
        '''
        str_matches = self.display()

        for view in self.views:
            view.on_anotator_change(str_matches=str_matches)
