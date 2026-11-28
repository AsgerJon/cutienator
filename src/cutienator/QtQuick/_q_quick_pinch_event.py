"""
QQuickPinchEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPinchEvent to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

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


class QQuickPinchEvent(QObject):
  """
  The cute side of Qt's QQuickPinchEvent: a plain Python object standing in
  front of one C++ QQuickPinchEvent.

  It is built on the cute 'QObject', as Qt's QQuickPinchEvent is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPinchEvent that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'center',
  'startCenter', 'setStartCenter', 'previousCenter', 'setPreviousCenter',
  'scale', 'previousScale', 'setPreviousScale', 'angle', 'previousAngle',
  'setPreviousAngle', 'rotation', 'point1', 'setPoint1', 'startPoint1',
  'setStartPoint1', 'point2', 'setPoint2', 'startPoint2', 'setStartPoint2',
  'pointCount', 'setPointCount', 'accepted', 'setAccepted'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPinchEvent::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPinchEvent::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPinchEvent::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPinchEvent is created at the first use, not by
    'QQuickPinchEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPinchEvent.
  - Qt tells when it has removed the C++ QQuickPinchEvent. Every call on the
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
    Calls Qt's 'QString QQuickPinchEvent::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#tr

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
    #  QString QQuickPinchEvent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickPinchEvent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPinchEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPinchEvent::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPinchEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickPinchEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def center(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchEvent::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#center

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchEvent::center() const
    address = self.uglySide.call('ritual_ZNK16QQuickPinchEvent6centerEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startCenter(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchEvent::startCenter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#startCenter

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchEvent::startCenter() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickPinchEvent11startCenterEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def previousCenter(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchEvent::previousCenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#previousCenter

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchEvent::previousCenter() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickPinchEvent14previousCenterEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchEvent::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#scale
    """
    #  qreal QQuickPinchEvent::scale() const
    return self.uglySide.call('ritual_ZNK16QQuickPinchEvent5scaleEv')

  def previousScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchEvent::previousScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#previousScale
    """
    #  qreal QQuickPinchEvent::previousScale() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickPinchEvent13previousScaleEv',
    )

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchEvent::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#angle
    """
    #  qreal QQuickPinchEvent::angle() const
    return self.uglySide.call('ritual_ZNK16QQuickPinchEvent5angleEv')

  def previousAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchEvent::previousAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#previousAngle
    """
    #  qreal QQuickPinchEvent::previousAngle() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickPinchEvent13previousAngleEv',
    )

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchEvent::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#rotation
    """
    #  qreal QQuickPinchEvent::rotation() const
    return self.uglySide.call('ritual_ZNK16QQuickPinchEvent8rotationEv')

  def point1(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchEvent::point1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#point1

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchEvent::point1() const
    address = self.uglySide.call('ritual_ZNK16QQuickPinchEvent6point1Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startPoint1(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchEvent::startPoint1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#startPoint1

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchEvent::startPoint1() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickPinchEvent11startPoint1Ev',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def point2(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchEvent::point2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#point2

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchEvent::point2() const
    address = self.uglySide.call('ritual_ZNK16QQuickPinchEvent6point2Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startPoint2(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchEvent::startPoint2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#startPoint2

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchEvent::startPoint2() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickPinchEvent11startPoint2Ev',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pointCount(self) -> int:
    """
    Calls Qt's 'int QQuickPinchEvent::pointCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#pointCount
    """
    #  int QQuickPinchEvent::pointCount() const
    return self.uglySide.call('ritual_ZNK16QQuickPinchEvent10pointCountEv')

  def accepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickPinchEvent::accepted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#accepted
    """
    #  bool QQuickPinchEvent::accepted() const
    return self.uglySide.call('ritual_ZNK16QQuickPinchEvent8acceptedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setStartCenter(self, c: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setStartCenter(QPointF c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#setStartCenter

    Parameters
    ----------

    c : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPinchEvent::setStartCenter(QPointF c)
    self.uglySide.call(
        'ritual_ZN16QQuickPinchEvent14setStartCenterE7QPointF',
        self._valueOf(c, 'QPointF'),
    )

  @overload(QPointF)
  def setPreviousCenter(self, c: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setPreviousCenter(QPointF c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#setPreviousCenter

    Parameters
    ----------

    c : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPinchEvent::setPreviousCenter(QPointF c)
    self.uglySide.call(
        'ritual_ZN16QQuickPinchEvent17setPreviousCenterE7QPointF',
        self._valueOf(c, 'QPointF'),
    )

  @overload(float)
  def setPreviousScale(self, s: float) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setPreviousScale(qreal s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#setPreviousScale

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QQuickPinchEvent::setPreviousScale(qreal s)
    self.uglySide.call('ritual_ZN16QQuickPinchEvent16setPreviousScaleEd', s)

  @overload(float)
  def setPreviousAngle(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setPreviousAngle(qreal a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#setPreviousAngle

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickPinchEvent::setPreviousAngle(qreal a)
    self.uglySide.call('ritual_ZN16QQuickPinchEvent16setPreviousAngleEd', a)

  @overload(QPointF)
  def setPoint1(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setPoint1(QPointF p)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#setPoint1

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPinchEvent::setPoint1(QPointF p)
    self.uglySide.call(
        'ritual_ZN16QQuickPinchEvent9setPoint1E7QPointF',
        self._valueOf(p, 'QPointF'),
    )

  @overload(QPointF)
  def setStartPoint1(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setStartPoint1(QPointF p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#setStartPoint1

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPinchEvent::setStartPoint1(QPointF p)
    self.uglySide.call(
        'ritual_ZN16QQuickPinchEvent14setStartPoint1E7QPointF',
        self._valueOf(p, 'QPointF'),
    )

  @overload(QPointF)
  def setPoint2(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setPoint2(QPointF p)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#setPoint2

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPinchEvent::setPoint2(QPointF p)
    self.uglySide.call(
        'ritual_ZN16QQuickPinchEvent9setPoint2E7QPointF',
        self._valueOf(p, 'QPointF'),
    )

  @overload(QPointF)
  def setStartPoint2(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setStartPoint2(QPointF p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#setStartPoint2

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPinchEvent::setStartPoint2(QPointF p)
    self.uglySide.call(
        'ritual_ZN16QQuickPinchEvent14setStartPoint2E7QPointF',
        self._valueOf(p, 'QPointF'),
    )

  @overload(int)
  def setPointCount(self, count: int) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setPointCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#setPointCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickPinchEvent::setPointCount(int count)
    self.uglySide.call('ritual_ZN16QQuickPinchEvent13setPointCountEi', count)

  @overload(bool)
  def setAccepted(self, a: bool) -> None:
    """
    Calls Qt's 'void QQuickPinchEvent::setAccepted(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchevent.html#setAccepted

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QQuickPinchEvent::setAccepted(bool a)
    self.uglySide.call('ritual_ZN16QQuickPinchEvent11setAcceptedEb', a)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF, float, float, float)
  def __init__(self, c: QPointF, s: float, a: float, r: float) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPinchEvent::QQuickPinchEvent(QPointF c, qreal s, qreal a, qreal
    r)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchevent.html#QQuickPinchEvent

    Parameters
    ----------

    c : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    s : float
      Passed on as it is.

    a : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  QQuickPinchEvent::QQuickPinchEvent(QPointF c, qreal s, qreal a, qreal
    #      r)
    self._noteCreation(QQuickPinchEvent, lambda: Rituals.call(
        'ritual_ZN16QQuickPinchEventC1E7QPointFddd',
        self._valueOf(c, 'QPointF'), s, a, r,
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
