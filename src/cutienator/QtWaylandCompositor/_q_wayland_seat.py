"""
QWaylandSeat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandseat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QInputEvent, QKeyEvent, QTouchEvent
  from . import QWaylandClient, QWaylandCompositor, QWaylandDrag
  from . import QWaylandKeyboard, QWaylandKeymap, QWaylandPointer
  from . import QWaylandSurface, QWaylandTouch, QWaylandView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputEvent = WAIT['QInputEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QPointF = WAIT['QPointF']
  QTouchEvent = WAIT['QTouchEvent']
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandCompositor = WAIT['QWaylandCompositor']
  QWaylandSurface = WAIT['QWaylandSurface']
  QWaylandView = WAIT['QWaylandView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandSeat(QWaylandObject):
  """
  The cute side of Qt's QWaylandSeat: a plain Python object standing in front
  of one C++ QWaylandSeat.

  It is built on the cute 'QWaylandObject', as Qt's QWaylandSeat is built on
  Qt's QWaylandObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandSeat that has a ritual and that Python can
  call so far, 39 names in all: 'metaObject', 'tr', 'initialize',
  'isInitialized', 'sendMousePressEvent', 'sendMouseReleaseEvent',
  'sendMouseMoveEvent', 'sendMouseWheelEvent', 'sendKeyPressEvent',
  'sendKeyReleaseEvent', 'sendFullKeyEvent', 'sendKeyEvent',
  'sendUnicodeKeyPressEvent', 'sendUnicodeKeyReleaseEvent',
  'sendTouchPointEvent', 'sendTouchPointPressed', 'sendTouchPointReleased',
  'sendTouchPointMoved', 'sendTouchFrameEvent', 'sendTouchCancelEvent',
  'sendFullTouchEvent', 'pointer', 'mouseFocus', 'setMouseFocus', 'keyboard',
  'keyboardFocus', 'setKeyboardFocus', 'keymap', 'touch', 'compositor',
  'drag', 'capabilities', 'isOwner', 'mouseFocusChanged',
  'keyboardFocusChanged', 'cursorSurfaceRequest', 'cursorSurfaceRequested',
  'sendUnicodeKeyEvent', 'handleMouseFocusDestroyed'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandSeat::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandSeat::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandSeatPrivate *QWaylandSeat::d_func()': gives
    'QWaylandSeatPrivate', which has no cute class yet.
  - Qt's 'const QWaylandSeatPrivate *QWaylandSeat::d_func() const': gives
    'QWaylandSeatPrivate', which has no cute class yet.
  - Qt's 'void QWaylandSeat::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QWaylandSeat::~QWaylandSeat()': the destructor: Python never
    removes a C++ QWaylandSeat.
  - Qt's 'QWaylandSeat *QWaylandSeat::fromSeatResource(struct ::wl_resource
    *resource)': names 'struct ::wl_resource', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 49 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandSeat is created at the first use, not by
    'QWaylandSeat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandSeat.
  - Qt tells when it has removed the C++ QWaylandSeat. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QWaylandSeat that has no cute function yet,
    'fromSeatResource', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QWaylandSeat, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CapabilityFlag(CuteFlags):
    """
    The flags enum 'QWaylandSeat::CapabilityFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QWaylandSeat::CapabilityFlags'.
    """

    Pointer = 0x1
    Keyboard = 0x2
    Touch = 0x4
    DefaultCapabilities = 0x7

  CapabilityFlags = CapabilityFlag

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
    Calls Qt's 'QString QWaylandSeat::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#tr

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
    #  QString QWaylandSeat::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QWaylandSeat2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandSeat'

  #  A C++ QWaylandSeat Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandSeat'

  #  The functions Qt calls itself that QWaylandSeat is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN12QWaylandSeat10initializeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isOwner': (
          ('_ZNK12QWaylandSeat7isOwnerEP11QInputEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QInputEvent'),
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
    Calls Qt's 'const QMetaObject *QWaylandSeat::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandSeat::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QWaylandSeat::isInitialized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#isInitialized
    """
    #  bool QWaylandSeat::isInitialized() const
    return self.uglySide.call('ritual_ZNK12QWaylandSeat13isInitializedEv')

  def pointer(self) -> Optional[QWaylandPointer]:
    """
    Calls Qt's 'QWaylandPointer *QWaylandSeat::pointer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#pointer

    Returns
    -------

    Optional[QWaylandPointer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandPointer *QWaylandSeat::pointer() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat7pointerEv')
    from . import QWaylandPointer
    return QWaylandPointer._cuteAt(address)

  def mouseFocus(self) -> Optional[QWaylandView]:
    """
    Calls Qt's 'QWaylandView *QWaylandSeat::mouseFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#mouseFocus

    Returns
    -------

    Optional[QWaylandView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandView *QWaylandSeat::mouseFocus() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat10mouseFocusEv')
    from . import QWaylandView
    return QWaylandView._cuteAt(address)

  def keyboard(self) -> Optional[QWaylandKeyboard]:
    """
    Calls Qt's 'QWaylandKeyboard *QWaylandSeat::keyboard() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#keyboard

    Returns
    -------

    Optional[QWaylandKeyboard]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandKeyboard *QWaylandSeat::keyboard() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat8keyboardEv')
    from . import QWaylandKeyboard
    return QWaylandKeyboard._cuteAt(address)

  def keyboardFocus(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandSeat::keyboardFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#keyboardFocus

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandSeat::keyboardFocus() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat13keyboardFocusEv')
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def touch(self) -> Optional[QWaylandTouch]:
    """
    Calls Qt's 'QWaylandTouch *QWaylandSeat::touch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#touch

    Returns
    -------

    Optional[QWaylandTouch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandTouch *QWaylandSeat::touch() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat5touchEv')
    from . import QWaylandTouch
    return QWaylandTouch._cuteAt(address)

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandSeat::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandSeat::compositor() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat10compositorEv')
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

  def drag(self) -> Optional[QWaylandDrag]:
    """
    Calls Qt's 'QWaylandDrag *QWaylandSeat::drag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#drag

    Returns
    -------

    Optional[QWaylandDrag]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandDrag *QWaylandSeat::drag() const
    address = self.uglySide.call('ritual_ZNK12QWaylandSeat4dragEv')
    from . import QWaylandDrag
    return QWaylandDrag._cuteAt(address)

  def capabilities(self) -> CapabilityFlags:
    """
    Calls Qt's 'QWaylandSeat::CapabilityFlags QWaylandSeat::capabilities()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#capabilities

    Returns
    -------

    CapabilityFlags
      The value standing for the combination Qt gave back.
    """
    #  QWaylandSeat::CapabilityFlags QWaylandSeat::capabilities() const
    return QWaylandSeat.CapabilityFlags(self.uglySide.call(
        'ritual_ZNK12QWaylandSeat12capabilitiesEv',
    ))

  @overload(QInputEvent)
  @overload(NoneType)
  def isOwner(self, inputEvent: Optional[QInputEvent]) -> bool:
    """
    Calls Qt's 'bool QWaylandSeat::isOwner(QInputEvent *inputEvent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#isOwner

    Parameters
    ----------

    inputEvent : Optional[QInputEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWaylandSeat::isOwner(QInputEvent *inputEvent) const
    ritual = 'ritual_ZNK12QWaylandSeat7isOwnerEP11QInputEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QWaylandSeat7isOwnerEP11QInputEvent'
    return self.uglySide.call(ritual, self._addressOf(inputEvent))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandView)
  @overload(NoneType)
  def setMouseFocus(self, view: Optional[QWaylandView]) -> None:
    """
    Calls Qt's 'void QWaylandSeat::setMouseFocus(QWaylandView *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#setMouseFocus

    Parameters
    ----------

    view : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::setMouseFocus(QWaylandView *view)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat13setMouseFocusEP12QWaylandView',
        self._addressOf(view),
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def setKeyboardFocus(self, surface: Optional[QWaylandSurface]) -> bool:
    """
    Calls Qt's 'bool QWaylandSeat::setKeyboardFocus(QWaylandSurface
    *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#setKeyboardFocus

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWaylandSeat::setKeyboardFocus(QWaylandSurface *surface)
    return self.uglySide.call(
        'ritual_ZN12QWaylandSeat16setKeyboardFocusEP15QWaylandSurface',
        self._addressOf(surface),
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

  @overload(QWaylandCompositor)
  @overload(NoneType)
  @overload(QWaylandCompositor, CapabilityFlags)
  @overload(NoneType, CapabilityFlags)
  def __init__(
      self,
      compositor: Optional[QWaylandCompositor],
      capabilityFlags: CapabilityFlags = CapabilityFlags.DefaultCapabilities,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandSeat::QWaylandSeat(QWaylandCompositor *compositor,
    CapabilityFlags capabilityFlags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#QWaylandSeat

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    capabilityFlags : CapabilityFlags
      Passed on as its number. May be left out, as in Qt: it is then
      CapabilityFlags.DefaultCapabilities.
    """
    #  QWaylandSeat::QWaylandSeat(QWaylandCompositor *compositor,
    #      CapabilityFlags capabilityFlags)
    self._noteCreation(QWaylandSeat, lambda: Rituals.call(
        'ritual_ZN12QWaylandSeatC1EP18QWaylandCompositor6QFlagsINS_14Capabi'
        'lityFlagEE',
        self._addressOf(compositor), capabilityFlags.value,
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandSeat::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#initialize
    """
    #  void QWaylandSeat::initialize()
    ritual = 'ritual_ZN12QWaylandSeat10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QWaylandSeat10initializeEv'
    self.uglySide.call(ritual)

  @overload(Qt.MouseButton)
  def sendMousePressEvent(self, button: Qt.MouseButton) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendMousePressEvent(Qt::MouseButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendMousePressEvent

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void QWaylandSeat::sendMousePressEvent(Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat19sendMousePressEventEN2Qt11MouseButtonE',
        button.value,
    )

  @overload(Qt.MouseButton)
  def sendMouseReleaseEvent(self, button: Qt.MouseButton) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendMouseReleaseEvent(Qt::MouseButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendMouseReleaseEvent

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void QWaylandSeat::sendMouseReleaseEvent(Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat21sendMouseReleaseEventEN2Qt11MouseButtonE',
        button.value,
    )

  @overload(QWaylandView, QPointF)
  @overload(NoneType, QPointF)
  @overload(QWaylandView, QPointF, QPointF)
  @overload(NoneType, QPointF, QPointF)
  def sendMouseMoveEvent(
      self,
      surface: Optional[QWaylandView],
      localPos: QPointF,
      outputSpacePos: Optional[QPointF] = None,
  ) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendMouseMoveEvent(QWaylandView *surface,
    const QPointF &localPos, const QPointF &outputSpacePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendMouseMoveEvent

    Parameters
    ----------

    surface : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    outputSpacePos : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.
    """
    #  void QWaylandSeat::sendMouseMoveEvent(QWaylandView *surface, const
    #      QPointF &localPos, const QPointF &outputSpacePos)
    if outputSpacePos is None:
      from ..QtCore import QPointF
      outputSpacePos = QPointF()
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat18sendMouseMoveEventEP12QWaylandViewRK7QPoi'
        'ntFS4_',
        self._addressOf(surface), self._valueOf(localPos, 'QPointF'),
        self._valueOf(outputSpacePos, 'QPointF'),
    )

  @overload(Qt.Orientation, int)
  def sendMouseWheelEvent(
      self,
      orientation: Qt.Orientation,
      delta: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendMouseWheelEvent(Qt::Orientation
    orientation, int delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendMouseWheelEvent

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    delta : int
      Passed on as it is.
    """
    #  void QWaylandSeat::sendMouseWheelEvent(Qt::Orientation orientation,
    #      int delta)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat19sendMouseWheelEventEN2Qt11OrientationEi',
        orientation.value, delta,
    )

  @overload(int)
  def sendKeyPressEvent(self, code: int) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendKeyPressEvent(uint code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendKeyPressEvent

    Parameters
    ----------

    code : int
      Passed on as it is.
    """
    #  void QWaylandSeat::sendKeyPressEvent(uint code)
    self.uglySide.call('ritual_ZN12QWaylandSeat17sendKeyPressEventEj', code)

  @overload(int)
  def sendKeyReleaseEvent(self, code: int) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendKeyReleaseEvent(uint code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendKeyReleaseEvent

    Parameters
    ----------

    code : int
      Passed on as it is.
    """
    #  void QWaylandSeat::sendKeyReleaseEvent(uint code)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat19sendKeyReleaseEventEj', code,
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def sendFullKeyEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendFullKeyEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#sendFullKeyEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::sendFullKeyEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat16sendFullKeyEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(int, bool)
  def sendKeyEvent(self, qtKey: int, pressed: bool) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendKeyEvent(int qtKey, bool pressed)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#sendKeyEvent

    Parameters
    ----------

    qtKey : int
      Passed on as it is.

    pressed : bool
      Passed on as it is.
    """
    #  void QWaylandSeat::sendKeyEvent(int qtKey, bool pressed)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat12sendKeyEventEib', qtKey, pressed,
    )

  @overload(int)
  def sendUnicodeKeyPressEvent(self, unicode: int) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendUnicodeKeyPressEvent(uint unicode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendUnicodeKeyPressEvent

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  void QWaylandSeat::sendUnicodeKeyPressEvent(uint unicode)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat24sendUnicodeKeyPressEventEj', unicode,
    )

  @overload(int)
  def sendUnicodeKeyReleaseEvent(self, unicode: int) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendUnicodeKeyReleaseEvent(uint unicode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendUnicodeKeyReleaseEvent

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  void QWaylandSeat::sendUnicodeKeyReleaseEvent(uint unicode)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat26sendUnicodeKeyReleaseEventEj', unicode,
    )

  @overload(QWaylandSurface, int, QPointF, Qt.TouchPointState)
  @overload(NoneType, int, QPointF, Qt.TouchPointState)
  def sendTouchPointEvent(
      self,
      surface: Optional[QWaylandSurface],
      id: int,
      point: QPointF,
      state: Qt.TouchPointState,
  ) -> int:
    """
    Calls Qt's 'uint QWaylandSeat::sendTouchPointEvent(QWaylandSurface
    *surface, int id, const QPointF &point, Qt::TouchPointState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendTouchPointEvent

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    state : Qt.TouchPointState
      Passed on as its number.
    """
    #  uint QWaylandSeat::sendTouchPointEvent(QWaylandSurface *surface, int
    #      id, const QPointF &point, Qt::TouchPointState state)
    return self.uglySide.call(
        'ritual_ZN12QWaylandSeat19sendTouchPointEventEP15QWaylandSurfaceiRK'
        '7QPointFN2Qt15TouchPointStateE',
        self._addressOf(surface), id, self._valueOf(point, 'QPointF'),
        state.value,
    )

  @overload(QWaylandSurface, int, QPointF)
  @overload(NoneType, int, QPointF)
  def sendTouchPointPressed(
      self,
      surface: Optional[QWaylandSurface],
      id: int,
      position: QPointF,
  ) -> int:
    """
    Calls Qt's 'uint QWaylandSeat::sendTouchPointPressed(QWaylandSurface
    *surface, int id, const QPointF &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendTouchPointPressed

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  uint QWaylandSeat::sendTouchPointPressed(QWaylandSurface *surface, int
    #      id, const QPointF &position)
    return self.uglySide.call(
        'ritual_ZN12QWaylandSeat21sendTouchPointPressedEP15QWaylandSurfacei'
        'RK7QPointF',
        self._addressOf(surface), id, self._valueOf(position, 'QPointF'),
    )

  @overload(QWaylandSurface, int, QPointF)
  @overload(NoneType, int, QPointF)
  def sendTouchPointReleased(
      self,
      surface: Optional[QWaylandSurface],
      id: int,
      position: QPointF,
  ) -> int:
    """
    Calls Qt's 'uint QWaylandSeat::sendTouchPointReleased(QWaylandSurface
    *surface, int id, const QPointF &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendTouchPointReleased

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  uint QWaylandSeat::sendTouchPointReleased(QWaylandSurface *surface,
    #      int id, const QPointF &position)
    return self.uglySide.call(
        'ritual_ZN12QWaylandSeat22sendTouchPointReleasedEP15QWaylandSurface'
        'iRK7QPointF',
        self._addressOf(surface), id, self._valueOf(position, 'QPointF'),
    )

  @overload(QWaylandSurface, int, QPointF)
  @overload(NoneType, int, QPointF)
  def sendTouchPointMoved(
      self,
      surface: Optional[QWaylandSurface],
      id: int,
      position: QPointF,
  ) -> int:
    """
    Calls Qt's 'uint QWaylandSeat::sendTouchPointMoved(QWaylandSurface
    *surface, int id, const QPointF &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendTouchPointMoved

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  uint QWaylandSeat::sendTouchPointMoved(QWaylandSurface *surface, int
    #      id, const QPointF &position)
    return self.uglySide.call(
        'ritual_ZN12QWaylandSeat19sendTouchPointMovedEP15QWaylandSurfaceiRK'
        '7QPointF',
        self._addressOf(surface), id, self._valueOf(position, 'QPointF'),
    )

  @overload(QWaylandClient)
  @overload(NoneType)
  def sendTouchFrameEvent(self, client: Optional[QWaylandClient]) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendTouchFrameEvent(QWaylandClient
    *client)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendTouchFrameEvent

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::sendTouchFrameEvent(QWaylandClient *client)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat19sendTouchFrameEventEP14QWaylandClient',
        self._addressOf(client),
    )

  @overload(QWaylandClient)
  @overload(NoneType)
  def sendTouchCancelEvent(self, client: Optional[QWaylandClient]) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendTouchCancelEvent(QWaylandClient
    *client)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendTouchCancelEvent

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::sendTouchCancelEvent(QWaylandClient *client)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat20sendTouchCancelEventEP14QWaylandClient',
        self._addressOf(client),
    )

  @overload(QWaylandSurface, QTouchEvent)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def sendFullTouchEvent(
      self,
      surface: Optional[QWaylandSurface],
      event: Optional[QTouchEvent],
  ) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendFullTouchEvent(QWaylandSurface
    *surface, QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendFullTouchEvent

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::sendFullTouchEvent(QWaylandSurface *surface,
    #      QTouchEvent *event)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat18sendFullTouchEventEP15QWaylandSurfaceP11Q'
        'TouchEvent',
        self._addressOf(surface), self._addressOf(event),
    )

  def keymap(self) -> Optional[QWaylandKeymap]:
    """
    Calls Qt's 'QWaylandKeymap *QWaylandSeat::keymap()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandseat.html#keymap

    Returns
    -------

    Optional[QWaylandKeymap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandKeymap *QWaylandSeat::keymap()
    address = self.uglySide.call('ritual_ZN12QWaylandSeat6keymapEv')
    from . import QWaylandKeymap
    return QWaylandKeymap._cuteAt(address)

  @overload(QWaylandView, QWaylandView)
  @overload(QWaylandView, NoneType)
  @overload(NoneType, QWaylandView)
  @overload(NoneType, NoneType)
  def mouseFocusChanged(
      self,
      newFocus: Optional[QWaylandView],
      oldFocus: Optional[QWaylandView],
  ) -> None:
    """
    Calls Qt's 'void QWaylandSeat::mouseFocusChanged(QWaylandView *newFocus,
    QWaylandView *oldFocus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#mouseFocusChanged

    Parameters
    ----------

    newFocus : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldFocus : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::mouseFocusChanged(QWaylandView *newFocus,
    #      QWaylandView *oldFocus)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat17mouseFocusChangedEP12QWaylandViewS1_',
        self._addressOf(newFocus), self._addressOf(oldFocus),
    )

  @overload(QWaylandSurface, QWaylandSurface)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QWaylandSurface)
  @overload(NoneType, NoneType)
  def keyboardFocusChanged(
      self,
      newFocus: Optional[QWaylandSurface],
      oldFocus: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandSeat::keyboardFocusChanged(QWaylandSurface
    *newFocus, QWaylandSurface *oldFocus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#keyboardFocusChanged

    Parameters
    ----------

    newFocus : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldFocus : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::keyboardFocusChanged(QWaylandSurface *newFocus,
    #      QWaylandSurface *oldFocus)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat20keyboardFocusChangedEP15QWaylandSurfaceS1'
        '_',
        self._addressOf(newFocus), self._addressOf(oldFocus),
    )

  @overload(QWaylandSurface, int, int)
  @overload(NoneType, int, int)
  def cursorSurfaceRequest(
      self,
      surface: Optional[QWaylandSurface],
      hotspotX: int,
      hotspotY: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandSeat::cursorSurfaceRequest(QWaylandSurface
    *surface, int hotspotX, int hotspotY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#cursorSurfaceRequest

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hotspotX : int
      Passed on as it is.

    hotspotY : int
      Passed on as it is.
    """
    #  void QWaylandSeat::cursorSurfaceRequest(QWaylandSurface *surface, int
    #      hotspotX, int hotspotY)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat20cursorSurfaceRequestEP15QWaylandSurfaceii',
        self._addressOf(surface), hotspotX, hotspotY,
    )

  @overload(QWaylandSurface, int, int, QWaylandClient)
  @overload(QWaylandSurface, int, int, NoneType)
  @overload(NoneType, int, int, QWaylandClient)
  @overload(NoneType, int, int, NoneType)
  def cursorSurfaceRequested(
      self,
      surface: Optional[QWaylandSurface],
      hotspotX: int,
      hotspotY: int,
      client: Optional[QWaylandClient],
  ) -> None:
    """
    Calls Qt's 'void QWaylandSeat::cursorSurfaceRequested(QWaylandSurface
    *surface, int hotspotX, int hotspotY, QWaylandClient *client)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#cursorSurfaceRequested

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hotspotX : int
      Passed on as it is.

    hotspotY : int
      Passed on as it is.

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSeat::cursorSurfaceRequested(QWaylandSurface *surface,
    #      int hotspotX, int hotspotY, QWaylandClient *client)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat22cursorSurfaceRequestedEP15QWaylandSurface'
        'iiP14QWaylandClient',
        self._addressOf(surface), hotspotX, hotspotY,
        self._addressOf(client),
    )

  @overload(int, QEvent.Type)
  def sendUnicodeKeyEvent(self, unicode: int, type: QEvent.Type) -> None:
    """
    Calls Qt's 'void QWaylandSeat::sendUnicodeKeyEvent(uint unicode,
    QEvent::Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#sendUnicodeKeyEvent

    Parameters
    ----------

    unicode : int
      Passed on as it is.

    type : QEvent.Type
      Passed on as its number.
    """
    #  void QWaylandSeat::sendUnicodeKeyEvent(uint unicode, QEvent::Type
    #      type)
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat19sendUnicodeKeyEventEjN6QEvent4TypeE',
        unicode, type.value,
    )

  def handleMouseFocusDestroyed(self) -> None:
    """
    Calls Qt's 'void QWaylandSeat::handleMouseFocusDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandseat.html#handleMouseFocusDestroyed
    """
    #  void QWaylandSeat::handleMouseFocusDestroyed()
    self.uglySide.call(
        'ritual_ZN12QWaylandSeat25handleMouseFocusDestroyedEv',
    )

  @staticmethod
  def fromSeatResource(*__, **_) -> Never:
    """
    Qt's 'QWaylandSeat *QWaylandSeat::fromSeatResource(struct ::wl_resource
    *resource)': names 'struct ::wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandSeat.fromSeatResource' has no cute function yet. Qt's "
        "'QWaylandSeat *QWaylandSeat::fromSeatResource(struct ::wl_resource "
        "*resource)': names 'struct ::wl_resource', which has no cute class "
        "yet.")
