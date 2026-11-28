"""
QQuickMouseEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickMouseEvent to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMouseEvent(QObject):
  """
  The cute side of Qt's QQuickMouseEvent: a plain Python object standing in
  front of one C++ QQuickMouseEvent.

  It is built on the cute 'QObject', as Qt's QQuickMouseEvent is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMouseEvent that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'reset', 'x', 'y',
  'button', 'buttons', 'modifiers', 'source', 'wasHeld', 'isClick', 'setX',
  'setY', 'setPosition', 'setSource', 'isAccepted', 'setAccepted', 'flags'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMouseEvent::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMouseEvent::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickMouseEvent::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickMouseEvent is created at the first use, not by
    'QQuickMouseEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMouseEvent.
  - Qt tells when it has removed the C++ QQuickMouseEvent. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickMouseEvent::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#tr

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
    #  QString QQuickMouseEvent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickMouseEvent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMouseEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMouseEvent::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMouseEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickMouseEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickMouseEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#x
    """
    #  qreal QQuickMouseEvent::x() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickMouseEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#y
    """
    #  qreal QQuickMouseEvent::y() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent1yEv')

  def button(self) -> int:
    """
    Calls Qt's 'int QQuickMouseEvent::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#button
    """
    #  int QQuickMouseEvent::button() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent6buttonEv')

  def buttons(self) -> int:
    """
    Calls Qt's 'int QQuickMouseEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#buttons
    """
    #  int QQuickMouseEvent::buttons() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent7buttonsEv')

  def modifiers(self) -> int:
    """
    Calls Qt's 'int QQuickMouseEvent::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#modifiers
    """
    #  int QQuickMouseEvent::modifiers() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent9modifiersEv')

  def source(self) -> int:
    """
    Calls Qt's 'int QQuickMouseEvent::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#source
    """
    #  int QQuickMouseEvent::source() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent6sourceEv')

  def wasHeld(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseEvent::wasHeld() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#wasHeld
    """
    #  bool QQuickMouseEvent::wasHeld() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent7wasHeldEv')

  def isClick(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseEvent::isClick() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#isClick
    """
    #  bool QQuickMouseEvent::isClick() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent7isClickEv')

  def flags(self) -> int:
    """
    Calls Qt's 'int QQuickMouseEvent::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#flags
    """
    #  int QQuickMouseEvent::flags() const
    return self.uglySide.call('ritual_ZNK16QQuickMouseEvent5flagsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickMouseEvent::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickMouseEvent::setX(qreal x)
    self.uglySide.call('ritual_ZN16QQuickMouseEvent4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickMouseEvent::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickMouseEvent::setY(qreal y)
    self.uglySide.call('ritual_ZN16QQuickMouseEvent4setYEd', y)

  @overload(QPointF)
  def setPosition(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QQuickMouseEvent::setPosition(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#setPosition

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickMouseEvent::setPosition(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN16QQuickMouseEvent11setPositionERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(Qt.MouseEventSource)
  def setSource(self, s: Qt.MouseEventSource) -> None:
    """
    Calls Qt's 'void QQuickMouseEvent::setSource(Qt::MouseEventSource s)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#setSource

    Parameters
    ----------

    s : Qt.MouseEventSource
      Passed on as its number.
    """
    #  void QQuickMouseEvent::setSource(Qt::MouseEventSource s)
    self.uglySide.call(
        'ritual_ZN16QQuickMouseEvent9setSourceEN2Qt16MouseEventSourceE',
        s.value,
    )

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickMouseEvent::setAccepted(bool accepted)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickMouseEvent::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN16QQuickMouseEvent11setAcceptedEb', accepted,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQuickMouseEvent::QQuickMouseEvent()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseevent.html#QQuickMouseEvent
    """
    #  QQuickMouseEvent::QQuickMouseEvent()
    self._noteCreation(QQuickMouseEvent, lambda: Rituals.call(
        'ritual_ZN16QQuickMouseEventC1Ev',
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

  @overload(
      float, float, Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers,
  )
  @overload(
      float, float, Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers,
      bool,
  )
  @overload(
      float, float, Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers,
      bool, bool,
  )
  @overload(
      float, float, Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers,
      bool, bool, Qt.MouseEventFlags,
  )
  def reset(
      self,
      x: float,
      y: float,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      isClick: bool = False,
      wasHeld: bool = False,
      flags: Qt.MouseEventFlags = Qt.MouseEventFlags(),
  ) -> None:
    """
    Calls Qt's 'void QQuickMouseEvent::reset(qreal x, qreal y,
    Qt::MouseButton button, Qt::MouseButtons buttons, Qt::KeyboardModifiers
    modifiers, bool isClick, bool wasHeld, Qt::MouseEventFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#reset

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    isClick : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    wasHeld : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    flags : Qt.MouseEventFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseEventFlags().
    """
    #  void QQuickMouseEvent::reset(qreal x, qreal y, Qt::MouseButton button,
    #      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, bool
    #      isClick, bool wasHeld, Qt::MouseEventFlags flags)
    self.uglySide.call(
        'ritual_ZN16QQuickMouseEvent5resetEddN2Qt11MouseButtonE6QFlagsIS1_E'
        'S2_INS0_16KeyboardModifierEEbbS2_INS0_14MouseEventFlagEE',
        x, y, button.value, buttons.value, modifiers.value, isClick, wasHeld,
        flags.value,
    )

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseEvent::isAccepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseevent.html#isAccepted
    """
    #  bool QQuickMouseEvent::isAccepted()
    return self.uglySide.call('ritual_ZN16QQuickMouseEvent10isAcceptedEv')
