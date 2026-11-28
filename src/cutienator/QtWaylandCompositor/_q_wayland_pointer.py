"""
QWaylandPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandpointer.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QWaylandClient, QWaylandCompositor, QWaylandOutput
  from . import QWaylandSeat, QWaylandView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandView = WAIT['QWaylandView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandPointer(QWaylandObject):
  """
  The cute side of Qt's QWaylandPointer: a plain Python object standing in
  front of one C++ QWaylandPointer.

  It is built on the cute 'QWaylandObject', as Qt's QWaylandPointer is built
  on Qt's QWaylandObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandPointer that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'seat', 'compositor',
  'output', 'setOutput', 'sendMousePressEvent', 'sendMouseReleaseEvent',
  'sendMouseMoveEvent', 'sendMouseWheelEvent', 'mouseFocus',
  'currentLocalPosition', 'currentSpacePosition', 'isButtonPressed',
  'addClient', 'toWaylandButton', 'outputChanged', 'buttonPressedChanged',
  'pointerFocusChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandPointer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandPointer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandPointerPrivate *QWaylandPointer::d_func()': gives
    'QWaylandPointerPrivate', which has no cute class yet.
  - Qt's 'const QWaylandPointerPrivate *QWaylandPointer::d_func() const':
    gives 'QWaylandPointerPrivate', which has no cute class yet.
  - Qt's 'wl_resource *QWaylandPointer::focusResource() const': gives
    'wl_resource', which has no cute class yet.
  - Qt's 'uint QWaylandPointer::sendButton(struct wl_resource *resource,
    uint32_t time, Qt::MouseButton button, uint32_t state)': names 'struct
    wl_resource', which has no cute class yet.
  - Qt's 'void QWaylandPointer::enteredSurfaceDestroyed(void *data)': names
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandPointer is created at the first use, not by
    'QWaylandPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandPointer.
  - Qt tells when it has removed the C++ QWaylandPointer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandPointer that has no cute function yet,
    'enteredSurfaceDestroyed', 'focusResource', 'sendButton', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QWaylandPointer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandPointer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QWaylandPointer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(Qt.MouseButton)
  def toWaylandButton(button: Qt.MouseButton) -> int:
    """
    Calls Qt's 'uint32_t QWaylandPointer::toWaylandButton(Qt::MouseButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#toWaylandButton

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  uint32_t QWaylandPointer::toWaylandButton(Qt::MouseButton button)
    return Rituals.call(
        'ritual_ZN15QWaylandPointer15toWaylandButtonEN2Qt11MouseButtonE',
        button.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandPointer'

  #  The functions Qt calls itself that QWaylandPointer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'sendMousePressEvent': (
          ('_ZN15QWaylandPointer19sendMousePressEventEN2Qt11MouseButtonE',
           ('unsigned int', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.MouseButton'),
           )),
      ),
      'sendMouseReleaseEvent': (
          ('_ZN15QWaylandPointer21sendMouseReleaseEventEN2Qt11MouseButtonE',
           ('unsigned int', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.MouseButton'),
           )),
      ),
      'sendMouseMoveEvent': (
          ('_ZN15QWaylandPointer18sendMouseMoveEventEP12QWaylandViewRK7QPoi'
           'ntFS4_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandView'),
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'sendMouseWheelEvent': (
          ('_ZN15QWaylandPointer19sendMouseWheelEventEN2Qt11OrientationEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
               ('int', 'number', ''),
           )),
      ),
      'addClient': (
          ('_ZN15QWaylandPointer9addClientEP14QWaylandClientjj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandClient'),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandPointer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandPointer::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QWaylandPointer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def seat(self) -> Optional[QWaylandSeat]:
    """
    Calls Qt's 'QWaylandSeat *QWaylandPointer::seat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#seat

    Returns
    -------

    Optional[QWaylandSeat]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSeat *QWaylandPointer::seat() const
    address = self.uglySide.call('ritual_ZNK15QWaylandPointer4seatEv')
    from . import QWaylandSeat
    return QWaylandSeat._cuteAt(address)

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandPointer::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandPointer::compositor() const
    address = self.uglySide.call('ritual_ZNK15QWaylandPointer10compositorEv')
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

  def output(self) -> Optional[QWaylandOutput]:
    """
    Calls Qt's 'QWaylandOutput *QWaylandPointer::output() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#output

    Returns
    -------

    Optional[QWaylandOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandOutput *QWaylandPointer::output() const
    address = self.uglySide.call('ritual_ZNK15QWaylandPointer6outputEv')
    from . import QWaylandOutput
    return QWaylandOutput._cuteAt(address)

  def mouseFocus(self) -> Optional[QWaylandView]:
    """
    Calls Qt's 'QWaylandView *QWaylandPointer::mouseFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#mouseFocus

    Returns
    -------

    Optional[QWaylandView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandView *QWaylandPointer::mouseFocus() const
    address = self.uglySide.call('ritual_ZNK15QWaylandPointer10mouseFocusEv')
    from . import QWaylandView
    return QWaylandView._cuteAt(address)

  def currentLocalPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QWaylandPointer::currentLocalPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#currentLocalPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWaylandPointer::currentLocalPosition() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandPointer20currentLocalPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def currentSpacePosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QWaylandPointer::currentSpacePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#currentSpacePosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWaylandPointer::currentSpacePosition() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandPointer20currentSpacePositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def isButtonPressed(self) -> bool:
    """
    Calls Qt's 'bool QWaylandPointer::isButtonPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#isButtonPressed
    """
    #  bool QWaylandPointer::isButtonPressed() const
    return self.uglySide.call(
        'ritual_ZNK15QWaylandPointer15isButtonPressedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandOutput)
  @overload(NoneType)
  def setOutput(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandPointer::setOutput(QWaylandOutput *output)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#setOutput

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandPointer::setOutput(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN15QWaylandPointer9setOutputEP14QWaylandOutput',
        self._addressOf(output),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandSeat)
  @overload(NoneType)
  @overload(QWaylandSeat, QObject)
  @overload(QWaylandSeat, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      seat: Optional[QWaylandSeat],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandPointer::QWaylandPointer(QWaylandSeat *seat, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#QWaylandPointer

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandPointer::QWaylandPointer(QWaylandSeat *seat, QObject *parent)
    self._noteCreation(QWaylandPointer, lambda: Rituals.call(
        'ritual_ZN15QWaylandPointerC1EP12QWaylandSeatP7QObject',
        self._addressOf(seat), self._addressOf(parent, 'QObject'),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.MouseButton)
  def sendMousePressEvent(self, button: Qt.MouseButton) -> int:
    """
    Calls Qt's 'uint QWaylandPointer::sendMousePressEvent(Qt::MouseButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#sendMousePressEvent

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  uint QWaylandPointer::sendMousePressEvent(Qt::MouseButton button)
    ritual = (
        'ritual_ZN15QWaylandPointer19sendMousePressEventEN2Qt11MouseButtonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QWaylandPointer19sendMousePressEventEN2Qt11MouseB'
          'uttonE')
    return self.uglySide.call(ritual, button.value)

  @overload(Qt.MouseButton)
  def sendMouseReleaseEvent(self, button: Qt.MouseButton) -> int:
    """
    Calls Qt's 'uint QWaylandPointer::sendMouseReleaseEvent(Qt::MouseButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#sendMouseReleaseEvent

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  uint QWaylandPointer::sendMouseReleaseEvent(Qt::MouseButton button)
    ritual = (
        'ritual_ZN15QWaylandPointer21sendMouseReleaseEventEN2Qt11MouseButto'
        'nE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QWaylandPointer21sendMouseReleaseEventEN2Qt11Mous'
          'eButtonE')
    return self.uglySide.call(ritual, button.value)

  @overload(QWaylandView, QPointF, QPointF)
  @overload(NoneType, QPointF, QPointF)
  def sendMouseMoveEvent(
      self,
      view: Optional[QWaylandView],
      localPos: QPointF,
      outputSpacePos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QWaylandPointer::sendMouseMoveEvent(QWaylandView *view,
    const QPointF &localPos, const QPointF &outputSpacePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#sendMouseMoveEvent

    Parameters
    ----------

    view : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    outputSpacePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWaylandPointer::sendMouseMoveEvent(QWaylandView *view, const
    #      QPointF &localPos, const QPointF &outputSpacePos)
    ritual = (
        'ritual_ZN15QWaylandPointer18sendMouseMoveEventEP12QWaylandViewRK7Q'
        'PointFS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QWaylandPointer18sendMouseMoveEventEP12QWaylandVi'
          'ewRK7QPointFS4_')
    self.uglySide.call(
        ritual,
        self._addressOf(view), self._valueOf(localPos, 'QPointF'),
        self._valueOf(outputSpacePos, 'QPointF'),
    )

  @overload(Qt.Orientation, int)
  def sendMouseWheelEvent(
      self,
      orientation: Qt.Orientation,
      delta: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandPointer::sendMouseWheelEvent(Qt::Orientation
    orientation, int delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#sendMouseWheelEvent

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    delta : int
      Passed on as it is.
    """
    #  void QWaylandPointer::sendMouseWheelEvent(Qt::Orientation orientation,
    #      int delta)
    ritual = (
        'ritual_ZN15QWaylandPointer19sendMouseWheelEventEN2Qt11OrientationE'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QWaylandPointer19sendMouseWheelEventEN2Qt11Orient'
          'ationEi')
    self.uglySide.call(ritual, orientation.value, delta)

  @overload(QWaylandClient, int, int)
  @overload(NoneType, int, int)
  def addClient(
      self,
      client: Optional[QWaylandClient],
      id: int,
      version: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandPointer::addClient(QWaylandClient *client,
    uint32_t id, uint32_t version)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#addClient

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    version : int
      Passed on as it is.
    """
    #  void QWaylandPointer::addClient(QWaylandClient *client, uint32_t id,
    #      uint32_t version)
    ritual = 'ritual_ZN15QWaylandPointer9addClientEP14QWaylandClientjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QWaylandPointer9addClientEP14QWaylandClientjj'
    self.uglySide.call(ritual, self._addressOf(client), id, version)

  def outputChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandPointer::outputChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpointer.html#outputChanged
    """
    #  void QWaylandPointer::outputChanged()
    self.uglySide.call('ritual_ZN15QWaylandPointer13outputChangedEv')

  def buttonPressedChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandPointer::buttonPressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#buttonPressedChanged
    """
    #  void QWaylandPointer::buttonPressedChanged()
    self.uglySide.call('ritual_ZN15QWaylandPointer20buttonPressedChangedEv')

  @overload(QWaylandView, QWaylandView)
  @overload(QWaylandView, NoneType)
  @overload(NoneType, QWaylandView)
  @overload(NoneType, NoneType)
  def pointerFocusChanged(
      self,
      newFocus: Optional[QWaylandView],
      oldFocus: Optional[QWaylandView],
  ) -> None:
    """
    Calls Qt's 'void QWaylandPointer::pointerFocusChanged(QWaylandView
    *newFocus, QWaylandView *oldFocus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpointer.html#pointerFocusChanged

    Parameters
    ----------

    newFocus : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldFocus : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandPointer::pointerFocusChanged(QWaylandView *newFocus,
    #      QWaylandView *oldFocus)
    self.uglySide.call(
        'ritual_ZN15QWaylandPointer19pointerFocusChangedEP12QWaylandViewS1_',
        self._addressOf(newFocus), self._addressOf(oldFocus),
    )

  @staticmethod
  def enteredSurfaceDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QWaylandPointer::enteredSurfaceDestroyed(void *data)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandPointer.enteredSurfaceDestroyed' has no cute function "
        "yet. Qt's 'void QWaylandPointer::enteredSurfaceDestroyed(void "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def focusResource(*__, **_) -> Never:
    """
    Qt's 'wl_resource *QWaylandPointer::focusResource() const': gives
    'wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandPointer.focusResource' has no cute function yet. Qt's "
        "'wl_resource *QWaylandPointer::focusResource() const': gives "
        "'wl_resource', which has no cute class yet.")

  @staticmethod
  def sendButton(*__, **_) -> Never:
    """
    Qt's 'uint QWaylandPointer::sendButton(struct wl_resource *resource,
    uint32_t time, Qt::MouseButton button, uint32_t state)': names 'struct
    wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandPointer.sendButton' has no cute function yet. Qt's 'uint "
        "QWaylandPointer::sendButton(struct wl_resource *resource, uint32_t "
        "time, Qt::MouseButton button, uint32_t state)': names 'struct "
        "wl_resource', which has no cute class yet.")
