import abc

class Subject(object):
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)


class Observer(metaclass=abc.ABCMeta):
    observers = []
    def __init__(self):
        self._subject = None
        self._observer_state = None
        __class__.observers.append(self)

    @abc.abstractmethod
    def update(self, arg):
        pass