"""
TestQObject tests the cute 'QObject' against Qt itself, through the
rituals.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

from cutienator import MetaCute, Ugly
from cutienator.QtCore import QObject, QEvent, QThread, QMetaObject
from cutienator.QtCore import QBindingStorage
from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Callable


class TestQObject(BaseTest):
  """
  Tests the cute 'QObject': every function of it that has a ritual, and
  what it needs of 'QEvent', 'QMetaObject', 'QThread' and
  'QBindingStorage'. Nothing is faked. Each test makes real C++ objects
  and calls real Qt functions, and says what Qt answered.

  Run with the source folder on the path:

    PYTHONPATH=src python -m unittest discover -s tests

  What to know before adding a test
  ---------------------------------

  - The rituals are called for real, so the shared object of rituals
    has to be built. 'setUpClass' builds it when a ritual file is newer
    than it, which takes some seconds the first time.
  - No Qt application runs during the tests. Qt starts no timer without
    one, so 'startTimer' gives 0 here.
  - Python removes no C++ QObject. What a test makes stays until the
    run ends, unless the test has Qt remove it, by the ritual of Qt's
    '~QObject()'.
  - A wrong argument is refused by worktoy, with 'DispatchException',
    before Qt sees it. A wrong address that did reach Qt would end the
    whole run, so no test passes one.
  - No test makes a cute class of its own here. 'MetaCute' knows a class
    by its name alone, and a second class named 'QThread' would be taken
    for the real one.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.build()

  def _raisedBy(self, make: Callable) -> BaseException:
    """
    Calls 'make', which is expected to raise, and gives what it raised.

    Parameters
    ----------

    make : Callable
      Called with nothing.
    """
    try:
      make()
    except Exception as exception:
      return exception
    self.fail('nothing was raised')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAKING ONE   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_made_with_nothing_with_none_or_with_a_parent(self) -> None:
    """A 'QObject' is made with nothing, with None or with a parent."""
    mother = QObject()
    self.assertIsNone(mother.parent())
    self.assertIsNone(QObject(None).parent())
    self.assertIs(QObject(mother).parent(), mother)

  def test_the_address_is_a_number_and_stays(self) -> None:
    """The C++ object has one address, the same at every read."""
    cute = QObject()
    address = cute.uglySide.getAddress()
    self.assertIsInstance(address, int)
    self.assertNotEqual(address, 0)
    self.assertEqual(cute.uglySide.getAddress(), address)

  def test_two_objects_are_two_cpp_objects(self) -> None:
    """Each cute 'QObject' stands for a C++ object of its own."""
    first, second = QObject(), QObject()
    firstAddress = first.uglySide.getAddress()
    self.assertNotEqual(firstAddress, second.uglySide.getAddress())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT AND CHILD   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_parent_gives_the_very_cute_object(self) -> None:
    """'parent' gives the cute object that was given, not a new one."""
    mother = QObject()
    child = QObject(mother)
    self.assertIs(child.parent(), mother)
    self.assertIs(child.parent(), child.parent())

  def test_set_parent_to_none_and_back(self) -> None:
    """'setParent' takes None and a 'QObject', and Qt remembers it."""
    mother, other = QObject(), QObject()
    child = QObject(mother)
    self.assertIsNone(child.setParent(None))
    self.assertIsNone(child.parent())
    child.setParent(other)
    self.assertIs(child.parent(), other)
    child.setParent(mother)
    self.assertIs(child.parent(), mother)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT ANSWERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_meta_object_names_the_qt_class(self) -> None:
    """'metaObject' gives a 'QMetaObject' that knows the name 'QObject'."""
    cute = QObject()
    metaObject = cute.metaObject()
    self.assertIsInstance(metaObject, QMetaObject)
    self.assertEqual(metaObject.className(), 'QObject')
    self.assertIs(cute.metaObject(), metaObject)
    self.assertIs(QObject().metaObject(), metaObject)

  def test_thread_gives_a_qthread(self) -> None:
    """'thread' gives a 'QThread', the class the body waited for."""
    cute = QObject()
    thread = cute.thread()
    self.assertIs(type(thread), QThread)
    self.assertIsInstance(thread, QObject)
    self.assertEqual(thread.metaObject().className(), 'QThread')
    self.assertTrue(thread.inherits('QThread'))
    self.assertIsNone(thread.parent())
    self.assertIs(QObject().thread(), thread)

  def test_the_late_class_was_named(self) -> None:
    """'QObject.QThread' holds the class 'QThread', and nothing waits."""
    self.assertIs(QObject.QThread, QThread)
    self.assertIs(QObject().QThread, QThread)
    self.assertNotIn('QThread', MetaCute.getStillWaiting())

  def test_a_given_object_serves_as_a_parent(self) -> None:
    """An object Qt gave, as the thread, is taken where one is asked."""
    thread = QObject().thread()
    child = QObject(thread)
    self.assertIs(child.parent(), thread)
    child.setParent(None)

  def test_inherits_asks_qt_by_name(self) -> None:
    """'inherits' answers for the name of a Qt class."""
    cute = QObject()
    answers = (('QObject', True), ('QWidget', False), ('', False))
    for classname, answer in answers:
      with self.subTest(classname=classname):
        self.assertIs(cute.inherits(classname), answer)

  def test_the_five_questions(self) -> None:
    """A plain 'QObject' answers no to all five yes or no questions."""
    cute = QObject()
    questions = (
      'isWidgetType', 'isWindowType', 'isQuickItemType', 'isQmlExposed',
      'signalsBlocked',
    )
    for question in questions:
      with self.subTest(question=question):
        self.assertIs(getattr(cute, question)(), False)

  def test_binding_storage(self) -> None:
    """'bindingStorage' gives a 'QBindingStorage', the same each time."""
    cute = QObject()
    bindingStorage = cute.bindingStorage()
    self.assertIsInstance(bindingStorage, QBindingStorage)
    self.assertIs(cute.bindingStorage(), bindingStorage)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT DOES   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_block_signals_gives_what_it_was_before(self) -> None:
    """'blockSignals' sets the state and gives the one before."""
    cute = QObject()
    self.assertIs(cute.blockSignals(True), False)
    self.assertIs(cute.signalsBlocked(), True)
    self.assertIs(cute.blockSignals(False), True)
    self.assertIs(cute.signalsBlocked(), False)

  def test_event_and_event_filter(self) -> None:
    """A plain 'QObject' takes no event and filters none."""
    mother, child = QObject(), QObject()
    event = QEvent(0)
    self.assertIs(child.event(event), False)
    self.assertIs(child.eventFilter(mother, event), False)
    self.assertIsNone(child.installEventFilter(mother))
    self.assertIs(child.event(event), False)
    self.assertIsNone(child.removeEventFilter(mother))

  def test_disconnect_with_nothing_connected(self) -> None:
    """'disconnect' answers False when nothing was connected."""
    mother, child = QObject(), QObject()
    self.assertIs(child.disconnect(None, None, None), False)
    self.assertIs(child.disconnect(None, mother, None), False)
    self.assertIs(child.disconnect(mother, None), False)

  def test_timers_without_a_qt_application(self) -> None:
    """'startTimer' gives a number, and 'killTimer' takes it back."""
    cute = QObject()
    timerId = cute.startTimer(1000, 1)
    self.assertIs(type(timerId), int)
    self.assertIsNone(cute.killTimer(timerId))

  def test_functions_that_give_nothing(self) -> None:
    """The two dumps and 'deleteLater' run and give None."""
    cute = QObject()
    for name in ('dumpObjectTree', 'dumpObjectInfo', 'deleteLater'):
      with self.subTest(name=name):
        self.assertIsNone(getattr(cute, name)())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT WORKTOY CASTS ON THE WAY  # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_whole_number_for_a_bool(self) -> None:
    """1 is taken for True where Qt takes a bool."""
    cute = QObject()
    self.assertIs(cute.blockSignals(1), False)
    self.assertIs(cute.signalsBlocked(), True)

  def test_bytes_for_text(self) -> None:
    """Bytes are taken where Qt takes text."""
    self.assertIs(QObject().inherits(b'QObject'), True)

  def test_whole_floats_for_whole_numbers(self) -> None:
    """A float with nothing behind the point is taken for an int."""
    self.assertIs(type(QObject().startTimer(1000.0, 1.0)), int)
    self.assertEqual(QEvent(0.0).type(), 0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REFUSALS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_wrong_arguments_never_reach_qt(self) -> None:
    """A call no signature takes is refused with 'DispatchException'."""
    mother, child = QObject(), QObject()
    event = QEvent(0)
    wrongCalls = (
      ('a number as parent', lambda: QObject(7)),
      ('text as parent', lambda: child.setParent('mother')),
      ('no parent at all', lambda: child.setParent()),
      ('the parent by keyword', lambda: child.setParent(parent=None)),
      ('an object as event', lambda: child.event(mother)),
      ('an event to watch', lambda: child.eventFilter(event, event)),
      ('a number as class name', lambda: child.inherits(7)),
      ('text as bool', lambda: child.blockSignals('yes')),
      ('2 as bool', lambda: child.blockSignals(2)),
      ('half a millisecond', lambda: child.startTimer(0.5, 1)),
      ('one argument of two', lambda: child.startTimer(1000)),
      ('text as timer', lambda: child.killTimer('0')),
      ('two of three', lambda: child.disconnect(None, None)),
      ('text as event type', lambda: QEvent('0')),
    )
    for wrongCall, call in wrongCalls:
      with self.subTest(wrongCall=wrongCall):
        self.assertIs(type(self._raisedBy(call)), DispatchException)

  def test_classes_python_cannot_make_yet(self) -> None:
    """A class with no ritual for making one refuses at its first use."""
    firstUses = (
      ('QThread', lambda: QThread().parent()),
      ('QMetaObject', lambda: QMetaObject().className()),
    )
    for className, firstUse in firstUses:
      with self.subTest(className=className):
        raised = self._raisedBy(firstUse)
        self.assertIs(type(raised), TypeError)
        self.assertIn(className, str(raised))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE NEIGHBOURS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_event_keeps_its_type(self) -> None:
    """A 'QEvent' gives back the number of the type it was made with."""
    for eventType in (0, 1, 7):
      with self.subTest(eventType=eventType):
        self.assertEqual(QEvent(eventType).type(), eventType)

  def test_event_is_accepted_until_ignored(self) -> None:
    """Qt makes an event accepted; 'ignore' and 'accept' change that."""
    event = QEvent(0)
    self.assertIs(event.isAccepted(), True)
    self.assertIsNone(event.ignore())
    self.assertIs(event.isAccepted(), False)
    self.assertIsNone(event.accept())
    self.assertIs(event.isAccepted(), True)

  def test_object_name_is_a_plain_str(self) -> None:
    """'setObjectName' takes a 'str' and 'objectName' gives it back."""
    cuteObject = QObject()
    self.assertEqual(cuteObject.objectName(), '')
    for name in ('cutie', '', 'smile \U0001F600', 'nul\x00inside'):
      with self.subTest(name=name):
        self.assertIsNone(cuteObject.setObjectName(name))
        self.assertEqual(cuteObject.objectName(), name)
        self.assertIs(type(cuteObject.objectName()), str)

  def test_object_name_refuses_what_is_no_text(self) -> None:
    """A number, None and nothing at all never reach Qt as a name."""
    cuteObject = QObject()
    cuteObject.setObjectName('kept')
    for wrong in ((5,), (None,), (), ('one', 'two')):
      with self.subTest(wrong=wrong):
        raised = self._raisedBy(lambda: cuteObject.setObjectName(*wrong))
        self.assertIsInstance(raised, DispatchException)
    self.assertEqual(cuteObject.objectName(), 'kept')

  def test_tr_gives_the_text_back_untranslated(self) -> None:
    """With no translation loaded, 'tr' gives the text it was given."""
    self.assertEqual(QObject.tr('hello', None, -1), 'hello')
    self.assertEqual(QObject().tr('hello', 'context', -1), 'hello')
    raised = self._raisedBy(lambda: QObject.tr('hello'))
    self.assertIsInstance(raised, DispatchException)

  def test_qt_watches_every_cute_qobject(self) -> None:
    """One made in Python and one Qt handed out are both watched."""
    cuteObject = QObject()
    self.assertIs(cuteObject.uglySide.isWatched(), True)
    self.assertIs(cuteObject.uglySide.isGone(), False)
    thread = cuteObject.thread()
    self.assertIs(thread.uglySide.isWatched(), True)
    self.assertIs(thread.uglySide.isGone(), False)

  def test_a_call_on_what_qt_removed_is_refused(self) -> None:
    """Qt removes the children with their parent. A call on any of
    them, and passing one on, then raises and never reaches C++."""
    mother = QObject()
    child = QObject(mother)
    child.setObjectName('kid')
    other = QObject()
    #  Qt's '~QObject()', as Qt itself runs it on an object it removes.
    Rituals.call('ritual_ZN7QObjectD1Ev', mother.uglySide.getAddress())
    self.assertIs(mother.uglySide.isGone(), True)
    self.assertIs(child.uglySide.isGone(), True)
    attempts = (
        lambda: child.objectName(), lambda: mother.parent(),
        lambda: child.deleteLater(), lambda: other.setParent(child),
        lambda: other.installEventFilter(mother),
    )
    for index, attempt in enumerate(attempts):
      with self.subTest(index=index):
        self.assertIsInstance(self._raisedBy(attempt), RuntimeError)
    self.assertIs(other.uglySide.isGone(), False)
    self.assertIsNone(other.parent())

  def test_what_qt_removed_is_found_by_its_address_no_more(self) -> None:
    """Another object may be at the address by then."""
    cuteObject = QObject()
    address = cuteObject.uglySide.getAddress()
    self.assertIs(QObject._cuteAt(address), cuteObject)
    Rituals.call('ritual_ZN7QObjectD1Ev', address)
    with self.assertRaises(LookupError):
      Ugly.at(address)

  def test_every_listed_ritual_is_offered(self) -> None:
    """The shared object offers each ritual 'Rituals' lists."""
    opened = Rituals.getOpened()
    for ritualName in Rituals.getRitualNames():
      with self.subTest(ritualName=ritualName):
        self.assertTrue(hasattr(opened, ritualName))
