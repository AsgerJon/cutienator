"""
TestCuteCuteMixin tests 'CuteMixin', which every cute class is built
on: how a cute object makes and finds its C++ object, what it hands a
ritual, and the functions of a program that Qt calls itself.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import sys
import types
import weakref
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.dispatch import Dispatcher, overload
from worktoy.mcls import BaseObject
from worktoy.work_test import BaseTest

from cutienator.cute import CuteMixin, CuteSpace
from cutienator.occult import Rituals, Ugly

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Tuple

#  Addresses no real object has, one for each object that needs one.
_FAKE = 0x7eae0000

#  The ritual each made-up class of Qt names, by what it does.
_CAST = 'ritual_cast_Device'
_DELETE = 'ritual_delete_Value'
_TAKE = 'ritual_take_Widget'
_META = 'ritual_ZNK7QObject10metaObjectEv'
_NAME = 'ritual_ZNK11QMetaObject9classNameEv'
_SUPER = 'ritual_ZNK11QMetaObject10superClassEv'


class _Calls:
  """
  Stands in for 'Rituals.call': notes each ritual run, with what it was
  handed, and answers from a table by the name of the ritual. An answer
  that can be called is called with what the ritual was handed.
  """

  def __init__(self) -> None:
    """Nothing run yet, and no answers."""
    self.seen = []  # type: List[Tuple[Any, ...]]
    self.answers = dict()  # type: Dict[str, Any]

  def __call__(self, name: str, *args: Any) -> Any:
    """Notes the ritual and gives its answer, None when it has none."""
    self.seen.append((name, *args))
    answer = self.answers.get(name, None)
    return answer(*args) if callable(answer) else answer

  def names(self) -> List[str]:
    """The name of each ritual run, in order."""
    return [name for name, *_ in self.seen]


class _Mode:
  """Stands in for an enum or flags: made of a number, keeps it."""

  def __init__(self, value: int) -> None:
    """Keeps the number."""
    self.value = value


class _Root(CuteMixin):
  """A made-up class of Qt that another is built on."""
  __qt_class__ = 'Root'


class _Base(_Root):
  """A made-up class of Qt built on '_Root'."""
  __qt_class__ = 'Base'


class _DeviceRoot(CuteMixin):
  """A made-up class of Qt that '_Device' is built on."""
  __qt_class__ = 'DeviceRoot'


class _Device(_DeviceRoot):
  """A made-up class of Qt that others are built on beside another."""
  __qt_class__ = 'Device'


class _Widget(_Base, _Device):
  """A made-up class of Qt built on '_Base' and, beside it, '_Device',
  with functions Qt calls itself."""
  __qt_class__ = 'Widget'
  __cast_rituals__ = {'Device': _CAST, 'Elsewhere': 'ritual_cast_Away'}
  __take_ritual__ = _TAKE
  __virtual_functions__ = {
      'paintEvent': [('paint', ('void', 'nothing', ''),
                      (('address', 'address', 'QtFake:Base'),))],
      'sizeHint': [('size', ('int', 'number', ''), ())],
  }
  __virtual_left_out__ = {'setText': ['void setText(const QString &)']}


class _Value(CuteMixin):
  """A made-up class of Qt whose C++ objects are values."""
  __qt_class__ = 'Value'
  __delete_ritual__ = _DELETE


class _Watched(CuteMixin):
  """A made-up class of Qt whose C++ objects are QObjects."""
  __qt_class__ = 'Watched'
  __watched_by_qt__ = True


class _RealWatched(_Watched):
  """A made-up class of Qt built on '_Watched'."""
  __qt_class__ = 'RealWatched'


class _NoQt(CuteMixin):
  """A class of no class of Qt at all."""


class _Painter(_Widget):
  """A class of a program that writes a function Qt calls itself."""

  def paintEvent(self, event: object) -> None:
    """Painted."""
    self.painted = event


class TestCuteCuteMixin(BaseTest):
  """
  Tests 'CuteMixin' through made-up classes of Qt built on it: what is
  handed to a ritual for a cute object, text or a value, what a C++
  object hands back, making the C++ object at the first use, the parts
  of an object of a class built on two, and the functions of a program
  Qt calls itself.

  What to know before adding a test
  ---------------------------------

  - No ritual is run. 'Rituals.call' and 'Rituals.callFrom' are a
    '_Calls' for each test ('self.calls'), which notes each ritual and
    answers from 'self.calls.answers': a part of a '_Widget' is 8 and
    16 past its address, and the take ritual takes every function.
    Addresses are made up ('_address').
  - 'Rituals.createCall' keeps each Python function it is given in
    'self.kept', and gives a function of C that does nothing.
  - A class keeps the functions of C made for it. A test that counts
    them makes a class of its own.
  - An 'Ugly' made in a test holds the '_Calls' for what it runs when
    it goes, so it may outlive the test.
  - The record of Uglies by address is fresh for each test.
  - A part of Qt named 'QtFake' is found as the package
    'cutienator.QtFake', a module put in 'sys.modules' for the test.
  """

  __count__ = 0

  def setUp(self) -> None:
    """A '_Calls' for the rituals, a fresh record of Uglies, and the
    made-up part 'QtFake'."""
    super().setUp()
    self.calls = _Calls()
    calls = self.calls
    calls.answers[_CAST] = lambda at: at + 8
    calls.answers['ritual_cast_Away'] = lambda at: at + 16
    calls.answers[_TAKE] = True
    self.kept = []  # type: List[Tuple[str, tuple, Any]]
    kept = self.kept

    def callFrom(partName: str, name: str, *args: Any) -> Any:
      return calls(name, *args)

    fake = types.ModuleType('cutienator.QtFake')
    def createCall(gives: str, takes: tuple, function: Any) -> Any:
      kept.append((gives, takes, function))
      return ctypes.CFUNCTYPE(None)(lambda: None)

    fake = types.ModuleType('cutienator.QtFake')
    fake.Base, fake.Device, fake.Mode = _Base, _Device, _Mode
    fake.Value, fake.RealWatched, fake.helper = _Value, _RealWatched, len
    for patcher in (
        mock.patch.object(Rituals, 'call', calls),
        mock.patch.object(Rituals, 'callFrom', callFrom),
        mock.patch.object(Rituals, 'createCall', createCall),
        mock.patch.object(
            Ugly, '__by_address__', weakref.WeakValueDictionary()),
        mock.patch.dict(sys.modules, {'cutienator.QtFake': fake}),
    ):
      patcher.start()
      self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _address(cls) -> int:
    """A made-up address, another for each call."""
    cls.__count__ += 1
    return _FAKE + 64 * cls.__count__

  def _made(self, cls: type, cuteClass: type = None) -> Any:
    """An object of a class, with its C++ object made at a made-up
    address by the constructor of 'cuteClass', by default its class of
    Qt, or the class itself."""
    cute = cls()
    address = self._address()
    if cuteClass is None:
      cuteClass = cute._findWritten()[1] or cls
    cute._noteCreation(cuteClass, lambda: address)
    self.assertEqual(cute.uglySide.getAddress(), address)
    return cute

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT A RITUAL IS HANDED  # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_object_by_its_address(self) -> None:
    """None for None; else the address, and Python owns the C++ object
    no more; for a class of Qt named, the address of its part."""
    self.assertIsNone(CuteMixin._addressOf(None))
    value = self._made(_Value)
    self.assertIs(value.uglySide.isOwned(), True)
    address = value.uglySide.getAddress()
    self.assertEqual(CuteMixin._addressOf(value), address)
    self.assertIs(value.uglySide.isOwned(), False)
    widget = self._made(_Widget)
    at = widget.uglySide.getAddress()
    self.assertEqual(CuteMixin._addressOf(widget, 'Device'), at + 8)
    self.assertEqual(CuteMixin._addressOf(widget, 'Base'), at)

  def test_an_object_as_a_value(self) -> None:
    """The address, still owned by Python; for a class of Qt named, the
    address of its part."""
    value = self._made(_Value)
    address = value.uglySide.getAddress()
    self.assertEqual(CuteMixin._valueOf(value), address)
    self.assertIs(value.uglySide.isOwned(), True)
    widget = self._made(_Widget)
    at = widget.uglySide.getAddress()
    self.assertEqual(CuteMixin._valueOf(widget, 'Device'), at + 8)

  def test_text_and_the_start_texts(self) -> None:
    """Text as bytes, None for None; the start texts as 'Rituals' keeps
    them."""
    self.assertIsNone(CuteMixin._bytesOf(None))
    self.assertEqual(CuteMixin._bytesOf('blåbær'), 'blåbær'.encode())
    with mock.patch.object(Rituals, 'keepStartTexts',
                           return_value=(1, 2)) as keep:
      self.assertEqual(CuteMixin._startTextsOf(['run']), (1, 2))
    keep.assert_called_once_with(['run'])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FINDING CLASSES  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_finding_a_class_by_its_place(self) -> None:
    """A class or what is in it, in a part brought in by its name."""
    self.assertIs(CuteMixin._findNamed('cute:CuteMixin'), CuteMixin)
    self.assertIs(CuteMixin._findNamed('cute:CuteSpace.getHooks'),
                  CuteSpace.getHooks)
    self.assertIs(CuteMixin._findNamed('QtFake:Base'), _Base)

  def test_what_a_class_wrote_itself(self) -> None:
    """A name not held, held plainly, held as an overloaded name of its
    own, inherited, or as a dispatcher with no namespace of worktoy."""

    class Overloading(BaseObject):
      @overload(int)
      def size(self, n: int) -> int:
        return n

    class Inheriting(Overloading):
      pass

    class Bare:
      size = Dispatcher()

    wrote = CuteMixin._wroteItself
    self.assertIs(wrote(_Painter, 'sizeHint'), False)
    self.assertIs(wrote(_Painter, 'paintEvent'), True)
    self.assertIs(wrote(Overloading, 'size'), True)
    self.assertIsInstance(Inheriting.__dict__['size'], Dispatcher)
    self.assertIs(wrote(Inheriting, 'size'), False)
    self.assertIs(wrote(Bare, 'size'), True)

  def test_the_classes_of_a_program_and_of_qt(self) -> None:
    """The classes of the program, the nearest first, and the class of
    Qt they are built on."""

    class Mine(_Painter):
      pass

    self.assertEqual(Mine()._findWritten(), ((Mine, _Painter), _Widget))
    self.assertEqual(_Widget()._findWritten(), ((), _Widget))
    written, generated = _NoQt()._findWritten()
    self.assertIsNone(generated)
    self.assertEqual(written, _NoQt.__mro__)

  def test_the_part_of_qt_of_a_class(self) -> None:
    """The part of the first class lying in a package named after one;
    None when none does. An Ugly is told it."""

    class Parted(_Base):
      pass

    class Mine(Parted):
      pass

    class Short(_Base):
      pass

    class Other(_Base):
      pass

    #  worktoy keeps a body from binding '__module__', so it is put on
    #  each class once it is made.
    for cls, module in ((Parted, 'cutienator.QtFake._parted'),
                        (Mine, 'program'), (Short, 'cutienator.QtFake'),
                        (Other, 'cutienator.cute._other')):
      type.__setattr__(cls, '__module__', module)
    self.assertEqual(Mine._getPartName(), 'QtFake')
    for cls in (Short, Other, _Base):
      with self.subTest(cls=cls):
        self.assertIsNone(cls._getPartName())
    self.assertEqual(Mine._createUgly().getPartName(), 'QtFake')
    self.assertIsNone(_Base._createUgly().getPartName())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAKING THE C++ OBJECT  # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_made_at_the_first_use(self) -> None:
    """The C++ object is made at the first read of 'uglySide', once,
    and stands behind the object."""
    made = []
    cute = _Base()
    cute._noteCreation(_Base, lambda: made.append(1) or self._address())
    self.assertEqual(made, [])
    ugly = cute.uglySide
    self.assertIs(cute.uglySide, ugly)
    self.assertEqual(made, [1])
    self.assertIs(ugly.getCuteSide(), cute)
    self.assertIs(Ugly.at(ugly.getAddress()), ugly)
    self.assertIsNone(cute.__creation_call__)
    self.assertIs(ugly.isOwned(), False)
    self.assertIs(ugly.isWatched(), False)

  def test_a_value_is_owned_and_a_qobject_watched(self) -> None:
    """The C++ object of a value is Python's; that of a QObject Qt
    watches."""
    self.assertEqual(self._made(_Value).uglySide.getDeleteRitual(),
                     _DELETE)
    self.calls.answers[Ugly.__watch_make_ritual__] = self._address()
    self.assertIs(self._made(_Watched).uglySide.isWatched(), True)

  def test_made_with_the_constructor_of_another_class(self) -> None:
    """An object of a class of Qt made by the constructor of the class
    it is built on is refused; a class of a program, or one of no
    class of Qt, takes the constructor it is given."""
    with self.assertRaises(TypeError) as caught:
      _Base()._noteCreation(_Root, self._address)
    self.assertIn("A '_Base' cannot be made with what a '_Root'",
                  str(caught.exception))
    self._made(_Painter, _Widget)
    self._made(_NoQt, _Root)

  def test_nothing_makes_it(self) -> None:
    """With nothing noted, the object cannot be made."""
    with self.assertRaises(TypeError) as caught:
      _Base().uglySide
    self.assertIn('cannot be made from Python', str(caught.exception))

  def test_making_that_makes_nothing_does_not_loop(self) -> None:
    """When making the C++ object leaves none, reading raises."""
    with mock.patch.object(CuteMixin, '_createUglySide'):
      with self.assertRaises(RecursionError):
        _Base().uglySide

  def test_the_parts_of_an_object(self) -> None:
    """Each part beginning inside the object is noted, so its address
    leads back to the object."""
    widget = self._made(_Widget)
    at = widget.uglySide.getAddress()
    self.assertIs(Ugly.at(at + 8).getCuteSide(), widget)
    self.assertIs(Ugly.at(at + 16).getCuteSide(), widget)

  def test_the_cast_of_a_class_of_qt(self) -> None:
    """The ritual of a class beside the first, and of what that is built
    on; none for the first and what it is built on, nor for a class
    the object is not built on."""
    widget = _Widget()
    self.assertEqual(widget._findCast('Device'), _CAST)
    self.assertEqual(widget._findCast('DeviceRoot'), _CAST)
    for qtClass in ('Base', 'Root', 'Widget', 'Value'):
      with self.subTest(qtClass=qtClass):
        self.assertIsNone(widget._findCast(qtClass))
    self.assertIsNone(_Base()._findCast('Device'))

  def test_a_ritual_of_a_class_of_qt(self) -> None:
    """A ritual of a class beside the first is handed its part."""
    self.calls.answers['ritual_device'] = 'ran'
    widget = self._made(_Widget)
    at = widget.uglySide.getAddress()
    self.assertEqual(widget._callAs('Device', 'ritual_device', 3), 'ran')
    self.assertEqual(self.calls.seen[-1], ('ritual_device', at + 8, 3))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FUNCTIONS QT CALLS ITSELF  # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_function_written_anew_is_handed_over(self) -> None:
    """Each function of Qt a class of the program wrote is handed to
    C++ by the take ritual, and the C++ object is ours."""
    class Painter(_Painter):
      pass

    painter = self._made(Painter)
    self.assertIs(painter.uglySide.isOurs(), True)
    taken = [args for args in self.calls.seen if args[0] == _TAKE]
    self.assertEqual(len(taken), 1)
    self.assertEqual(taken[0][2], b'paint')
    self.assertEqual([(g, t) for g, t, _ in self.kept],
                     [('void', ('address',))])
    self.assertIn('paint', Painter.__dict__['__taken_calls__'])

  def test_no_function_is_handed_over_without_need(self) -> None:
    """An object of the class of Qt itself, of a class with no take
    ritual, or of no class of Qt, hands nothing over."""
    for cls in (_Widget, _Base, _NoQt):
      with self.subTest(cls=cls):
        cute = self._made(cls, _Root if cls is _NoQt else None)
        self.assertIs(cute.uglySide.isOurs(), cls is _Widget)
    self.assertNotIn(_TAKE, self.calls.names())

  def test_a_function_the_cpp_class_does_not_take(self) -> None:
    """When the take ritual takes no Python function, making the object
    is refused, and the next use raises the same."""
    self.calls.answers[_TAKE] = False
    painter = _Painter()
    painter._noteCreation(_Widget, self._address)
    for _ in range(2):
      with self.assertRaises(TypeError) as caught:
        painter.uglySide
      self.assertIn("'_Painter' writes 'paintEvent' anew",
                    str(caught.exception))

  def test_a_function_that_cannot_be_handed_over(self) -> None:
    """A class of the program writing a function left out is refused
    before the C++ object is made."""

    class Writer(_Widget):
      def setText(self, text: str) -> None:
        """Written anew."""

    cute = Writer()
    cute._noteCreation(_Widget, self._address)
    with self.assertRaises(NotImplementedError) as caught:
      cute.uglySide
    said = str(caught.exception)
    self.assertIn("'Writer' writes 'setText' anew", said)
    self.assertIn('void setText(const QString &)', said)

  def test_the_function_of_c_is_kept_on_the_class(self) -> None:
    """Made at the first asking, kept by its key, on each class of its
    own."""
    kept = self.kept
    gives, takes = ('void', 'nothing', ''), ()
    first = _Painter._getTakenCall('k', 'paintEvent', gives, takes)
    self.assertIs(_Painter._getTakenCall('k', 'paintEvent', gives, takes),
                  first)
    self.assertEqual(len(kept), 1)

    class Again(_Painter):
      pass

    self.assertIsNot(Again._getTakenCall('k', 'paintEvent', gives, takes),
                     first)
    self.assertEqual(len(kept), 2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHEN QT CALLS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _called(self, gives: tuple, takes: tuple) -> Any:
    """The Python function C++ would call for '_Painter.sizeHint' giving
    and taking as told, and the list each exception kept goes to."""
    raised = []
    for name, new in (
        ('hasKeptException', lambda: bool(raised)),
        ('keepException', raised.append),
    ):
      patcher = mock.patch.object(Rituals, name, new)
      patcher.start()
      self.addCleanup(patcher.stop)
    _Painter._createTakenCall('sizeHint', gives, takes)
    return self.kept[-1][2], raised

  def test_qt_calls_a_function_written_anew(self) -> None:
    """What C++ hands over is turned, the function of the object is
    called, what it gives is turned back, and the call is taken."""
    called, raised = self._called(
        ('int', 'number', ''), (('int', 'number', ''),))

    class Sized(_Painter):
      def sizeHint(self, n: int) -> int:
        """Twice what it is handed."""
        return 2 * n

    sized = self._made(Sized)
    wasTaken = [0]
    at = sized.uglySide.getAddress()
    self.assertEqual(called(at, 21, wasTaken), 42)
    self.assertEqual(wasTaken, [1])
    self.assertEqual(raised, [])

  def test_while_an_exception_is_kept_nothing_is_taken(self) -> None:
    """With an exception still to be raised, the call is left to Qt:
    0 for a function giving something, None for one giving nothing."""
    for gives, nothing in ((('int', 'number', ''), 0),
                           (('void', 'nothing', ''), None)):
      with self.subTest(gives=gives):
        called, raised = self._called(gives, ())
        raised.append(ValueError('kept'))
        wasTaken = [0]
        self.assertEqual(called(self._address(), wasTaken), nothing)
        self.assertEqual(wasTaken, [0])

  def test_qt_calls_an_object_python_let_go_of(self) -> None:
    """An object no Ugly stands for, or whose cute object is gone,
    keeps a RuntimeError saying so, and leaves the call to Qt."""
    called, raised = self._called(('int', 'number', ''), ())
    sized = self._made(_Painter)
    ugly = sized.uglySide
    at = ugly.getAddress()
    del sized
    for address, cause in ((self._address(), LookupError),
                           (at, RuntimeError)):
      with self.subTest(cause=cause):
        raised.clear()
        wasTaken = [0]
        self.assertEqual(called(address, wasTaken), 0)
        self.assertEqual(wasTaken, [0])
        error, = raised
        self.assertIsInstance(error, RuntimeError)
        self.assertIn("Qt called 'sizeHint' of a '_Painter'", str(error))
        self.assertIsInstance(error.__cause__, cause)
    self.assertIs(Ugly.at(at), ugly)

  def test_what_the_function_raises_is_kept(self) -> None:
    """What the function raises, or what it gives that Qt's would not,
    is kept, and the call is left to Qt."""
    called, raised = self._called(('int', 'number', ''), ())

    class Broken(_Painter):
      def sizeHint(self) -> int:
        """Gives no number."""
        return 'no number'

    broken = self._made(Broken)
    wasTaken = [0]
    self.assertEqual(called(broken.uglySide.getAddress(), wasTaken), 0)
    self.assertEqual(wasTaken, [0])
    error, = raised
    self.assertIsInstance(error, TypeError)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT C++ HANDS OVER  # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_number_text_and_members_handed_over(self) -> None:
    """A number as it is, text as Qt's, a member or flags made from its
    number."""
    handed = CuteMixin._cuteOfHanded
    self.assertEqual(handed('number', '', 7), 7)
    with mock.patch.object(Rituals, 'takeText', return_value='text'):
      self.assertEqual(handed('text', '', 99), 'text')
    for how in ('enum', 'flags'):
      with self.subTest(how=how):
        self.assertEqual(handed(how, 'QtFake:Mode', 3).value, 3)

  def test_an_object_handed_over(self) -> None:
    """None for no object; the cute object at the address when it is of
    the class; else a new one of the class around it."""
    handed = CuteMixin._cuteOfHanded
    self.assertIsNone(handed('address', 'QtFake:Base', None))
    base = self._made(_Base)
    at = base.uglySide.getAddress()
    self.assertIs(handed('address', 'QtFake:Base', at), base)
    device = self._made(_Device)
    at = device.uglySide.getAddress()
    anew = handed('address', 'QtFake:Base', at)
    self.assertIsInstance(anew, _Base)
    self.assertEqual(anew.uglySide.getAddress(), at)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IS HANDED BACK  # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_numbers_handed_back(self) -> None:
    """A number of the kind Qt's gives; a whole number for a 'float';
    anything else is refused, naming what was wanted."""
    back = CuteMixin._handBack
    self.assertIsNone(back('f', ('void', 'nothing', ''), 'whatever'))
    self.assertIs(back('f', ('bool', 'number', ''), True), True)
    self.assertEqual(back('f', ('float', 'number', ''), 2), 2)
    self.assertEqual(back('f', ('double', 'number', ''), 2.5), 2.5)
    self.assertEqual(back('f', ('int', 'number', ''), 3), 3)
    for word, given, wanted in (('bool', None, 'bool'),
                                ('double', 'x', 'float'),
                                ('int', 2.5, 'int')):
      with self.subTest(word=word):
        with self.assertRaises(TypeError) as caught:
          back('sizeHint', (word, 'number', ''), given)
        self.assertIn("'sizeHint' has to give '%s'" % wanted,
                      str(caught.exception))

  def test_text_and_members_handed_back(self) -> None:
    """Text as a text of Qt, a member or flags as their number."""
    back = CuteMixin._handBack
    with mock.patch.object(Rituals, 'giveText', return_value=77):
      self.assertEqual(back('f', ('text', 'text', ''), 'blå'), 77)
    with self.assertRaises(TypeError):
      back('f', ('text', 'text', ''), 1)
    for how in ('enum', 'flags'):
      with self.subTest(how=how):
        self.assertEqual(back('f', ('x', how, 'QtFake:Mode'), _Mode(5)), 5)
    with self.assertRaises(TypeError):
      back('f', ('x', 'enum', 'QtFake:Mode'), 5)

  def test_objects_handed_back(self) -> None:
    """A value is kept and handed by its address; an object by its
    address, Python owning it no more; None for no object. An object of
    another class is refused."""
    back = CuteMixin._handBack
    value = self._made(_Value)
    kept = []
    with mock.patch.object(Rituals, 'keepGiven', kept.append):
      self.assertEqual(back('f', ('x', 'value', 'QtFake:Value'), value),
                       value.uglySide.getAddress())
    self.assertEqual(kept, [value])
    kept.clear()
    base = self._made(_Base)
    self.assertEqual(back('f', ('x', 'address', 'QtFake:Base'), base),
                     base.uglySide.getAddress())
    self.assertIsNone(back('f', ('x', 'address', 'QtFake:Base'), None))
    with self.assertRaises(TypeError):
      back('f', ('x', 'value', 'QtFake:Base'), None)
    with self.assertRaises(TypeError):
      back('f', ('x', 'address', 'QtFake:Device'), base)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OBJECTS C++ MADE   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _metaChain(self, *names: str) -> None:
    """Has the made-up meta objects say the class names given, each
    built on the next, the last on none."""
    metas = [self._address() for _ in names]
    byMeta = dict(zip(metas, names))
    after = dict(zip(metas, [*metas[1:], 0]))
    self.calls.answers[_META] = lambda at: metas[0]
    self.calls.answers[_NAME] = lambda meta: byMeta[meta].encode()
    self.calls.answers[_SUPER] = lambda meta: after[meta]

  def test_the_real_class_of_a_qobject(self) -> None:
    """The class of the C++ class itself when it is one built on the
    class asked; else the nearest it is built on that has one; else the
    class asked."""
    with mock.patch.object(Rituals, 'getComponents',
                           return_value=('QtFake',)):
      for names, found in (
          (('RealWatched',), _RealWatched),
          (('NoSuch', 'helper', 'Base', 'RealWatched'), _RealWatched),
          (('_Watched',), _Watched),
          (('NoSuch',), _Watched),
      ):
        with self.subTest(names=names):
          self._metaChain(*names)
          self.assertIs(_Watched._findRealClass(self._address()), found)

  def test_a_new_object_around_an_address(self) -> None:
    """A new object of the class, its '__init__' not run, standing for
    the address; a QObject is of its real class and watched."""
    at = self._address()
    anew = _Base._cuteAnew(at)
    self.assertIs(type(anew), _Base)
    self.assertIs(Ugly.at(at).getCuteSide(), anew)
    self.assertIs(anew.uglySide.isWatched(), False)
    self._metaChain('RealWatched')
    self.calls.answers[Ugly.__watch_make_ritual__] = self._address()
    with mock.patch.object(Rituals, 'getComponents',
                           return_value=('QtFake',)):
      watched = _Watched._cuteAnew(self._address())
    self.assertIs(type(watched), _RealWatched)
    self.assertIs(watched.uglySide.isWatched(), True)

  def test_the_object_at_an_address(self) -> None:
    """None for None, the object standing there, or a new one."""
    self.assertIsNone(_Base._cuteAt(None))
    base = self._made(_Base)
    at = base.uglySide.getAddress()
    self.assertIs(_Base._cuteAt(at), base)
    self.assertIs(_Device._cuteAt(at), base)
    other = self._address()
    anew = _Base._cuteAt(other)
    self.assertEqual(anew.uglySide.getAddress(), other)

  def test_a_new_object_owning_a_copy(self) -> None:
    """A value class owns the copy, removed by its delete ritual;
    another class is refused."""
    at = self._address()
    value = _Value._cuteOwning(at)
    self.assertEqual(value.uglySide.getAddress(), at)
    self.assertEqual(value.uglySide.getDeleteRitual(), _DELETE)
    self.assertIs(Ugly.at(at).getCuteSide(), value)
    with self.assertRaises(TypeError) as caught:
      _Base._cuteOwning(self._address())
    self.assertIn("'_Base' names no '__delete_ritual__'",
                  str(caught.exception))
