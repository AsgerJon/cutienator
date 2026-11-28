"""
QQuickWheelEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickWheelEvent to be private: it declares the class in a header
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

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QPointingDevice, QWheelEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWheelEvent(QObject):
  """
  The cute side of Qt's QQuickWheelEvent: a plain Python object standing in
  front of one C++ QQuickWheelEvent.

  It is built on the cute 'QObject', as Qt's QQuickWheelEvent is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWheelEvent that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'reset',
  'pointingDevice', 'x', 'y', 'angleDelta', 'pixelDelta', 'buttons',
  'modifiers', 'phase', 'inverted', 'isAccepted', 'setAccepted'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWheelEvent::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickWheelEvent::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWheelEvent::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWheelEvent is created at the first use, not by
    'QQuickWheelEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWheelEvent.
  - Qt tells when it has removed the C++ QQuickWheelEvent. Every call on the
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
    Calls Qt's 'QString QQuickWheelEvent::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#tr

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
    #  QString QQuickWheelEvent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickWheelEvent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWheelEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWheelEvent::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWheelEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickWheelEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pointingDevice(self) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'const QPointingDevice *QQuickWheelEvent::pointingDevice()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelevent.html#pointingDevice

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPointingDevice *QQuickWheelEvent::pointingDevice() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickWheelEvent14pointingDeviceEv',
    )
    from ..QtGui import QPointingDevice
    return QPointingDevice._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickWheelEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#x
    """
    #  qreal QQuickWheelEvent::x() const
    return self.uglySide.call('ritual_ZNK16QQuickWheelEvent1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickWheelEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#y
    """
    #  qreal QQuickWheelEvent::y() const
    return self.uglySide.call('ritual_ZNK16QQuickWheelEvent1yEv')

  def angleDelta(self) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickWheelEvent::angleDelta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#angleDelta

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickWheelEvent::angleDelta() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickWheelEvent10angleDeltaEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def pixelDelta(self) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickWheelEvent::pixelDelta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#pixelDelta

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickWheelEvent::pixelDelta() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickWheelEvent10pixelDeltaEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def buttons(self) -> int:
    """
    Calls Qt's 'int QQuickWheelEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#buttons
    """
    #  int QQuickWheelEvent::buttons() const
    return self.uglySide.call('ritual_ZNK16QQuickWheelEvent7buttonsEv')

  def modifiers(self) -> int:
    """
    Calls Qt's 'int QQuickWheelEvent::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#modifiers
    """
    #  int QQuickWheelEvent::modifiers() const
    return self.uglySide.call('ritual_ZNK16QQuickWheelEvent9modifiersEv')

  def phase(self) -> Qt.ScrollPhase:
    """
    Calls Qt's 'Qt::ScrollPhase QQuickWheelEvent::phase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#phase

    Returns
    -------

    Qt.ScrollPhase
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ScrollPhase(number)'
      gives.
    """
    #  Qt::ScrollPhase QQuickWheelEvent::phase() const
    return Qt.ScrollPhase(self.uglySide.call(
        'ritual_ZNK16QQuickWheelEvent5phaseEv',
    ))

  def inverted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWheelEvent::inverted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#inverted
    """
    #  bool QQuickWheelEvent::inverted() const
    return self.uglySide.call('ritual_ZNK16QQuickWheelEvent8invertedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickWheelEvent::setAccepted(bool accepted)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickWheelEvent::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN16QQuickWheelEvent11setAcceptedEb', accepted,
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
    Notes what was given, for Qt's 'QQuickWheelEvent::QQuickWheelEvent()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelevent.html#QQuickWheelEvent
    """
    #  QQuickWheelEvent::QQuickWheelEvent()
    self._noteCreation(QQuickWheelEvent, lambda: Rituals.call(
        'ritual_ZN16QQuickWheelEventC1Ev',
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

  @overload(QWheelEvent)
  @overload(NoneType)
  def reset(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickWheelEvent::reset(const QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#reset

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWheelEvent::reset(const QWheelEvent *event)
    self.uglySide.call(
        'ritual_ZN16QQuickWheelEvent5resetEPK11QWheelEvent',
        self._addressOf(event),
    )

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWheelEvent::isAccepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelevent.html#isAccepted
    """
    #  bool QQuickWheelEvent::isAccepted()
    return self.uglySide.call('ritual_ZN16QQuickWheelEvent10isAcceptedEv')
