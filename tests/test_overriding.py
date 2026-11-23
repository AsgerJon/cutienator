"""
TestOverriding tests the functions Qt calls itself, as 'paintEvent',
written anew by a class of a program: Qt calls what the program wrote,
'super()' reaches Qt's own, and what is raised in such a function is
raised where Python was.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys
from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.work_test import BaseTest

import cutienator
from cutienator.QtCore import QItemSelectionModel, QMetaMethod, QMimeData
from cutienator.QtCore import QModelIndex, QObject, QSize, QStringListModel
from cutienator.QtCore import Qt
from cutienator.QtGui import QImage, QPaintDevice
from cutienator.QtWidgets import QSpacerItem, QVBoxLayout
from cutienator.cute import CuteMixin
from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List


class Sender(QObject):
  """Notes each signal something is connected to. Qt calls
  'connectNotify' itself, from 'QObject::connect'."""

  def connectNotify(self, signal: QMetaMethod) -> None:
    found = [*getattr(self, 'connected', []), signal.methodType()]
    self.connected = found
    super().connectNotify(signal)


class Paper(QImage):
  """Answers for its own resolution. Qt calls 'metric' itself, from
  'logicalDpiX', and hands it a member of an enum."""

  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    self.asked = [*getattr(self, 'asked', []), metric]
    if metric is QPaintDevice.PaintDeviceMetric.PdmDpiX:
      return 123
    return super().metric(metric)


class Rude(QImage):
  """Gives text where Qt's 'metric' gives a number."""

  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    return 'a lot'


class Failing(QImage):
  """Raises in a function Qt calls."""

  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    raise ValueError('the metric of Failing fails')


class Plain(QMimeData):
  """Answers for one format. Qt calls 'hasFormat' itself, from
  'hasText', and hands it a text."""

  def hasFormat(self, mimeType: str) -> bool:
    self.asked = [*getattr(self, 'asked', []), mimeType]
    return mimeType == 'text/plain'


class Tall(QSpacerItem):
  """Grows upwards. Qt calls 'expandingDirections' itself, from the
  layout the spacer is in, and takes flags back."""

  def expandingDirections(self) -> Qt.Orientation:
    return Qt.Orientation.Vertical


class Picky(QItemSelectionModel):
  """Notes what it is told to select. Qt calls 'select' itself, from
  'setCurrentIndex', and hands it flags."""

  def select(self, index: QModelIndex, command: Any) -> None:
    self.told = [*getattr(self, 'told', []), (type(index), command)]


class Formats(QMimeData):
  """Writes a function anew that cannot be handed to Python yet: Qt's
  'formats' gives a list of texts."""

  def formats(self) -> list:
    return ['text/plain']


#  The functions that need an application, in a Python of its own, since
#  Qt has one application for each program. Each line it prints is a
#  name, a colon and what was found.
WITH_AN_APPLICATION = """
import gc
import sys

from cutienator.QtCore import QEvent, QObject, QSize, QTimer
from cutienator.QtGui import QColor, QPainter
from cutienator.QtWidgets import QApplication, QPushButton, QSpinBox
from cutienator.QtWidgets import QTreeWidget, QWidget
from cutienator.occult import Rituals

calls = []


class Canvas(QWidget):

  def paintEvent(self, event):
    calls.append('paintEvent of Canvas, handed a %s' % type(event).__name__)
    painter = QPainter(self)
    painter.fillRect(0, 0, self.width(), self.height(), QColor(255, 0, 0))
    painter.end()


class Polite(QWidget):

  def paintEvent(self, event):
    calls.append('paintEvent of Polite')
    super().paintEvent(event)

  def sizeHint(self):
    return super().sizeHint()


class Broken(QWidget):

  def paintEvent(self, event):
    raise ValueError('the paintEvent of Broken is broken')


class Button(QPushButton):

  def sizeHint(self):
    calls.append('sizeHint of Button')
    return QSize(77, 33)


class Ticker(QObject):

  def event(self, event):
    calls.append('event of Ticker')
    return super().event(event)


class Numbered(QSpinBox):

  def textFromValue(self, value):
    return 'no. %d' % value


class Mute(QSpinBox):

  def textFromValue(self, value):
    return value


class Tree(QTreeWidget):

  def setModel(self, model):
    pass


def pixel(widget):
  widget.resize(40, 30)
  return hex(widget.grab().toImage().pixel(20, 15) & 0xffffffff)


app = QApplication(sys.argv)
plain = QWidget()
plainPixel = pixel(plain)
print('plain is ours:', plain.uglySide.isOurs())
print('plain asked Python:', calls)
canvas = Canvas()
print('canvas painted red:', pixel(canvas) == '0xffff0000')
print('canvas was asked:', calls)
calls.clear()
polite = Polite()
print('polite painted as plain:', pixel(polite) == plainPixel)
print('polite was asked:', calls)
print('polite sizeHint is of Qt:',
      polite.sizeHint().width() == plain.sizeHint().width())
calls.clear()
button = Button('text')
button.adjustSize()
print('button was asked:', 'sizeHint of Button' in calls)
print('button size:', button.width(), button.height())
calls.clear()
ticker = Ticker()
print('ticker took it:', app.sendEvent(ticker, QEvent(QEvent.Type.User)))
print('ticker was asked:', calls)
broken = Broken()
try:
  pixel(broken)
  print('grab raised:', None)
except ValueError as error:
  print('grab raised:', error)
print('kept after the raise:', Rituals.hasKeptException())
print('canvas paints again:', pixel(canvas) == '0xffff0000')
broken.show()
QTimer.singleShot(5000, app, '1quit()')
try:
  print('exec raised:', None, app.exec())
except ValueError as error:
  print('exec raised:', error)
broken.hide()
window = QWidget()
window.resize(60, 40)
child = Canvas(window)
child.resize(60, 40)
window.grab()
del child
gc.collect()
try:
  window.grab()
  print('let go raised:', None)
except RuntimeError as error:
  print('let go raised:', ' '.join(str(error).split()[:11]))
numbered = Numbered()
numbered.setValue(5)
print('numbered text:', numbered.text())
try:
  Mute().setValue(5)
  print('mute raised:', None)
except TypeError as error:
  print('mute raised:', ' '.join(str(error).split()[:5]))
try:
  Tree().show()
  print('tree raised:', None)
except TypeError as error:
  print('tree raised:', ' '.join(str(error).split()[:4]))
"""


class TestOverriding(BaseTest):
  """
  Tests the functions of Qt a class of a program writes anew. Those
  that need no application run here, the others in a Python of their
  own, once for the whole class.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  The program with an application, as it ended, and what it printed,
  #  by name.
  __program_done__ = None  # type: Any
  __program_found__ = None  # type: Dict[str, str]

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer,
    and runs the program with an application."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.build()
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    environment['QT_QPA_PLATFORM'] = 'offscreen'
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', WITH_AN_APPLICATION),
        capture_output=True, text=True, env=environment, timeout=120,
    )
    found = dict()  # type: Dict[str, str]
    for line in done.stdout.strip().split('\n'):
      name, _, value = line.partition(': ')
      found[name] = value
    cls.__program_done__ = done
    cls.__program_found__ = found

  def _found(self, name: str) -> str:
    """Gives what the program with an application printed at a name."""
    done = self.__program_done__
    self.assertEqual(done.returncode, 0, done.stderr)
    return self.__program_found__[name]

  @staticmethod
  def _connect(sender: Any) -> List[Any]:
    """Connects a signal of a sender and gives what the sender noted."""
    receiver = QObject()
    QObject.connect(sender, '2destroyed()', receiver, '1deleteLater()')
    return getattr(sender, 'connected', [])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_qt_calls_what_the_program_wrote(self) -> None:
    """Qt calls 'connectNotify' itself as a signal is connected, and
    hands it the signal as a cute object."""
    sender = Sender()
    self.assertTrue(sender.uglySide.isOurs())
    signal = QMetaMethod.MethodType.Signal
    self.assertEqual(self._connect(sender), [signal])

  def test_a_class_built_on_a_class_of_a_program(self) -> None:
    """What a class of a program wrote goes for the classes built on
    it as well."""

    class Later(Sender):
      """Writes nothing anew itself."""

    signal = QMetaMethod.MethodType.Signal
    self.assertEqual(self._connect(Later()), [signal])

  def test_a_plain_object_is_not_asked(self) -> None:
    """An object of the cute class itself is of the C++ class of ours
    too, and no Python function is handed over for it."""
    plain = QObject()
    self.assertTrue(plain.uglySide.isOurs())
    self.assertEqual(self._connect(plain), [])
    self.assertIsNone(QObject.__dict__.get('__taken_calls__', None))
    self._connect(Sender())
    self.assertEqual([*Sender.__dict__['__taken_calls__']], [
        '_ZN7QObject13connectNotifyERK11QMetaMethod',
    ])

  def test_what_a_class_wrote_itself(self) -> None:
    """Every class has a function of its own at each overloaded name,
    so that the name is in a class does not say the class wrote it."""

    class Quiet(QObject):
      """Writes nothing anew."""

    class Typed(QObject):
      """Writes a function anew as an overload."""

      @overload(QMetaMethod)
      def connectNotify(self, signal: QMetaMethod) -> None:
        self.typed = True

    self.assertIn('connectNotify', Quiet.__dict__)
    self.assertFalse(CuteMixin._wroteItself(Quiet, 'connectNotify'))
    self.assertFalse(CuteMixin._wroteItself(Quiet, 'noSuchName'))
    self.assertTrue(CuteMixin._wroteItself(Sender, 'connectNotify'))
    self.assertTrue(CuteMixin._wroteItself(Typed, 'connectNotify'))
    typed = Typed()
    self._connect(typed)
    self.assertTrue(typed.typed)
    Quiet.connectNotify = lambda self, signal: None
    self.assertTrue(CuteMixin._wroteItself(Quiet, 'connectNotify'))

  def test_an_enum_handed_over_and_a_number_given(self) -> None:
    """Qt hands 'metric' a number, which arrives as the member, and
    takes the number given back. 'super()' reaches Qt's own."""
    paper = Paper(4, 4, QImage.Format.Format_RGB32)
    self.assertEqual(paper.logicalDpiX(), 123)
    self.assertIs(paper.asked[0], QPaintDevice.PaintDeviceMetric.PdmDpiX)
    plain = QImage(4, 4, QImage.Format.Format_RGB32)
    self.assertEqual(paper.logicalDpiY(), plain.logicalDpiY())
    self.assertIs(paper.asked[1], QPaintDevice.PaintDeviceMetric.PdmDpiY)

  def test_what_is_raised_is_raised_where_python_was(self) -> None:
    """An exception raised in a function Qt called comes out of the
    function of Qt that Python called."""
    failing = Failing(4, 4, QImage.Format.Format_RGB32)
    with self.assertRaises(ValueError) as context:
      failing.logicalDpiX()
    self.assertEqual(str(context.exception), 'the metric of Failing fails')
    self.assertFalse(Rituals.hasKeptException())

  def test_giving_what_qt_does_not_give(self) -> None:
    """A function that gives something else than Qt's own gives is
    refused, as it gives it."""
    rude = Rude(4, 4, QImage.Format.Format_RGB32)
    with self.assertRaises(TypeError) as context:
      rude.logicalDpiX()
    self.assertIn("'metric' has to give 'int'", str(context.exception))
    self.assertIn("but gave 'str'", str(context.exception))

  def test_the_first_exception_kept_is_the_one_raised(self) -> None:
    """While an exception is kept no further one is, and the next
    ritual to return raises it."""
    size = QSize(1, 2)
    self.assertEqual(size.width(), 1)
    self.assertFalse(Rituals.hasKeptException())
    Rituals.keepException(KeyError('first'))
    Rituals.keepException(ValueError('second'))
    self.assertTrue(Rituals.hasKeptException())
    with self.assertRaises(KeyError):
      size.width()
    self.assertFalse(Rituals.hasKeptException())
    self.assertEqual(size.width(), 1)

  def test_while_one_is_kept_python_is_not_asked(self) -> None:
    """Qt runs its own function while an exception is kept."""
    paper = Paper(4, 4, QImage.Format.Format_RGB32)
    self.assertTrue(paper.uglySide.isOurs())
    Rituals.keepException(KeyError('kept'))
    with self.assertRaises(KeyError):
      paper.logicalDpiX()
    self.assertEqual(getattr(paper, 'asked', []), [])
    self.assertEqual(paper.logicalDpiX(), 123)

  def test_text_handed_over(self) -> None:
    """Qt hands 'hasFormat' a text of its own, which arrives as a
    'str'."""
    plain = Plain()
    self.assertTrue(plain.hasText())
    self.assertEqual(plain.asked, ['text/plain'])
    self.assertFalse(QMimeData().hasText())

  def test_flags_given_back(self) -> None:
    """Qt takes the flags 'expandingDirections' gives, here one member
    of them. The spacer is kept for as long as the layout has it."""
    layout, tall = QVBoxLayout(), Tall(10, 10)
    layout.addItem(tall)
    vertical = Qt.Orientation.Vertical
    self.assertEqual(layout.expandingDirections(), vertical)
    plain = QVBoxLayout()
    plain.addItem(QSpacerItem(10, 10))
    self.assertNotEqual(plain.expandingDirections(), vertical)

  def test_a_spacer_python_let_go_of(self) -> None:
    """A layout calling a function of an item the program no longer
    holds raises, as for any object Python let go of."""
    layout = QVBoxLayout()
    layout.addItem(Tall(10, 10))
    with self.assertRaises(RuntimeError) as context:
      layout.expandingDirections()
    expected = "'expandingDirections' of a 'Tall'"
    self.assertIn(expected, str(context.exception))

  def test_flags_handed_over(self) -> None:
    """Qt hands 'select' its flags, which arrive as a value of the
    flags class."""
    picky = Picky(QStringListModel())
    select = QItemSelectionModel.SelectionFlag.Select
    picky.setCurrentIndex(QModelIndex(), select)
    self.assertEqual(picky.told, [(QModelIndex, select)])

  def test_a_function_that_cannot_be_handed_over_yet(self) -> None:
    """Writing one anew is refused when the object is first used, and
    at every use after."""
    formats = Formats()
    for _ in range(2):
      with self.assertRaises(NotImplementedError) as context:
        formats.hasText()
      info = str(context.exception)
      self.assertIn("'Formats' writes 'formats' anew", info)
      self.assertIn('QMimeData::formats() const', info)

  def test_a_word_no_python_function_takes(self) -> None:
    """Text cannot be handed to a Python function yet, and what is no
    word of a row never can."""
    for word in ('text', 'QString'):
      with self.subTest(word=word):
        with self.assertRaises(ValueError):
          Rituals.createCall('nothing', (word,), print)
        with self.assertRaises(ValueError):
          Rituals.createCall(word, (), print)

  def test_painting(self) -> None:
    """Qt calls the 'paintEvent' a widget wrote, with the event as its
    own class, and a widget that wrote none is not asked."""
    self.assertEqual(self._found('plain is ours'), 'True')
    self.assertEqual(self._found('plain asked Python'), '[]')
    self.assertEqual(self._found('canvas painted red'), 'True')
    expected = "['paintEvent of Canvas, handed a QPaintEvent']"
    self.assertEqual(self._found('canvas was asked'), expected)

  def test_super_runs_what_qt_has(self) -> None:
    """'super()' in a function written anew runs Qt's own, and not the
    function of Python once more."""
    self.assertEqual(self._found('polite painted as plain'), 'True')
    self.assertEqual(self._found('polite was asked'),
                     "['paintEvent of Polite']")
    self.assertEqual(self._found('polite sizeHint is of Qt'), 'True')

  def test_a_class_built_on_another_class_of_qt(self) -> None:
    """A QPushButton asks Python for its size, and a QObject for its
    events."""
    self.assertEqual(self._found('button was asked'), 'True')
    self.assertEqual(self._found('button size'), '77 33')
    self.assertEqual(self._found('ticker took it'), 'True')
    self.assertEqual(self._found('ticker was asked'), "['event of Ticker']")

  def test_raising_while_qt_paints(self) -> None:
    """What 'paintEvent' raises comes out of 'grab()', and out of
    'exec()', whose loop of events is stopped."""
    expected = 'the paintEvent of Broken is broken'
    self.assertEqual(self._found('grab raised'), expected)
    self.assertEqual(self._found('kept after the raise'), 'False')
    self.assertEqual(self._found('canvas paints again'), 'True')
    self.assertEqual(self._found('exec raised'), expected)

  def test_text_given_back(self) -> None:
    """Qt takes the 'str' that 'textFromValue' gives as its own text,
    and anything else is refused."""
    self.assertEqual(self._found('numbered text'), 'no. 5')
    expected = "'textFromValue' has to give 'str',"
    self.assertEqual(self._found('mute raised'), expected)

  def test_an_object_python_let_go_of(self) -> None:
    """Qt calling a function of an object the program no longer holds
    raises, and does not run Qt's own in its place."""
    expected = "Qt called 'paintEvent' of a 'Canvas' that Python has let go"
    self.assertEqual(self._found('let go raised'), expected)

  def test_a_function_qt_marks_private(self) -> None:
    """Qt's QTreeWidget marks 'setModel' private. A class built on it
    writes it anew all the same: C++ lets a class do that as well, and
    what C++ marks private is no concern of cutienator."""
    self.assertEqual(self._found('tree raised'), 'None')
