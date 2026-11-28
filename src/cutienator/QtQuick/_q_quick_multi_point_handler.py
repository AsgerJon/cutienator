"""
QQuickMultiPointHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickmultipointhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickMultiPointHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QPointingDevice
from . import QQuickPointerDeviceHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QEventPoint, QPointerEvent
  from . import QQuickHandlerPoint, QQuickItem
  from . import QQuickMultiPointHandlerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMultiPointHandler(QQuickPointerDeviceHandler):
  """
  The cute side of Qt's QQuickMultiPointHandler: a plain Python object
  standing in front of one C++ QQuickMultiPointHandler.

  It is built on the cute 'QQuickPointerDeviceHandler', as Qt's
  QQuickMultiPointHandler is built on Qt's QQuickPointerDeviceHandler, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMultiPointHandler that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'tr',
  'minimumPointCount', 'setMinimumPointCount', 'maximumPointCount',
  'setMaximumPointCount', 'centroid', 'minimumPointCountChanged',
  'maximumPointCountChanged', 'centroidChanged', 'wantsPointerEvent',
  'handlePointerEventImpl', 'onActiveChanged', 'hasCurrentPoints',
  'eligiblePoints', 'averageTouchPointDistance', 'averageStartingDistance',
  'acceptPoints', 'grabPoints', 'moveTarget', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMultiPointHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickMultiPointHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickMultiPointHandler::onGrabChanged(QQuickPointerHandler
    *grabber, QPointingDevice::GrabTransition transition, QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QList<QQuickHandlerPoint>
    &QQuickMultiPointHandler::currentPoints()': gives a type Python has no
    way to take yet.
  - Qt's 'QQuickHandlerPoint &QQuickMultiPointHandler::mutableCentroid()':
    gives a type Python has no way to take yet.
  - Qt's 'QList<PointData> QQuickMultiPointHandler::angles(const QPointF
    &ref) const': gives a type Python has no way to take yet.
  - Qt's 'qreal QQuickMultiPointHandler::averageAngleDelta(const
    QList<PointData> &old, const QList<PointData> &newAngles)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QQuickMultiPointHandlerPrivate
    *QQuickMultiPointHandler::d_func() const': takes in Python what
    'QQuickMultiPointHandlerPrivate *QQuickMultiPointHandler::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickMultiPointHandler is created at the first use, not by
    'QQuickMultiPointHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMultiPointHandler.
  - Qt tells when it has removed the C++ QQuickMultiPointHandler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMultiPointHandler that has no cute function yet,
    'angles', 'averageAngleDelta', 'averageStartingAngle',
    'averageTouchPointAngle', 'currentPoints', 'mutableCentroid', holds a
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
    Calls Qt's 'QString QQuickMultiPointHandler::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultipointhandler.html#tr

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
    #  QString QQuickMultiPointHandler::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickMultiPointHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMultiPointHandler'

  #  A C++ QQuickMultiPointHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMultiPointHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMultiPointHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMultiPointHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickMultiPointHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimumPointCount(self) -> int:
    """
    Calls Qt's 'int QQuickMultiPointHandler::minimumPointCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#minimumPointCount
    """
    #  int QQuickMultiPointHandler::minimumPointCount() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickMultiPointHandler17minimumPointCountEv',
    )

  def maximumPointCount(self) -> int:
    """
    Calls Qt's 'int QQuickMultiPointHandler::maximumPointCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#maximumPointCount
    """
    #  int QQuickMultiPointHandler::maximumPointCount() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickMultiPointHandler17maximumPointCountEv',
    )

  def centroid(self) -> QQuickHandlerPoint:
    """
    Calls Qt's 'const QQuickHandlerPoint &QQuickMultiPointHandler::centroid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#centroid

    Returns
    -------

    QQuickHandlerPoint
      A new cute QQuickHandlerPoint around the copy Qt gave back. Python owns
      it.
    """
    #  const QQuickHandlerPoint &QQuickMultiPointHandler::centroid() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickMultiPointHandler8centroidEv',
    )
    from . import QQuickHandlerPoint
    return QQuickHandlerPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMinimumPointCount(self, c: int) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::setMinimumPointCount(int c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#setMinimumPointCount

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QQuickMultiPointHandler::setMinimumPointCount(int c)
    self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler20setMinimumPointCountEi', c,
    )

  @overload(int)
  def setMaximumPointCount(self, maximumPointCount: int) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::setMaximumPointCount(int
    maximumPointCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#setMaximumPointCount

    Parameters
    ----------

    maximumPointCount : int
      Passed on as it is.
    """
    #  void QQuickMultiPointHandler::setMaximumPointCount(int
    #      maximumPointCount)
    self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler20setMaximumPointCountEi',
        maximumPointCount,
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
  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, int)
  @overload(NoneType, int)
  @overload(QQuickItem, int, int)
  @overload(NoneType, int, int)
  def __init__(
      self,
      parent: Optional[QQuickItem] = None,
      minimumPointCount: int = 2,
      maximumPointCount: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMultiPointHandler::QQuickMultiPointHandler(QQuickItem *parent, int
    minimumPointCount, int maximumPointCount)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    minimumPointCount : int
      Passed on as it is. May be left out, as in Qt: it is then 2.

    maximumPointCount : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QQuickMultiPointHandler::QQuickMultiPointHandler(QQuickItem *parent,
    #      int minimumPointCount, int maximumPointCount)
    self._noteCreation(QQuickMultiPointHandler, lambda: Rituals.call(
        'ritual_ZN23QQuickMultiPointHandlerC1EP10QQuickItemii',
        self._addressOf(parent), minimumPointCount, maximumPointCount,
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

  def minimumPointCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::minimumPointCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html
    """
    #  void QQuickMultiPointHandler::minimumPointCountChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler24minimumPointCountChangedEv',
    )

  def maximumPointCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::maximumPointCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html
    """
    #  void QQuickMultiPointHandler::maximumPointCountChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler24maximumPointCountChangedEv',
    )

  def centroidChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::centroidChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#centroidChanged
    """
    #  void QQuickMultiPointHandler::centroidChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler15centroidChangedEv',
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickMultiPointHandler::wantsPointerEvent(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMultiPointHandler::wantsPointerEvent(QPointerEvent *event)
    ritual = (
        'ritual_ZN23QQuickMultiPointHandler17wantsPointerEventEP13QPointerE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickMultiPointHandler17wantsPointerEventEP13QPo'
          'interEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPointerEvent)
  @overload(NoneType)
  def handlePointerEventImpl(self, event: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickMultiPointHandler::handlePointerEventImpl(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointHandler::handlePointerEventImpl(QPointerEvent
    #      *event)
    ritual = (
        'ritual_ZN23QQuickMultiPointHandler22handlePointerEventImplEP13QPoi'
        'nterEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickMultiPointHandler22handlePointerEventImplEP'
          '13QPointerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def onActiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::onActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#onActiveChanged
    """
    #  void QQuickMultiPointHandler::onActiveChanged()
    ritual = 'ritual_ZN23QQuickMultiPointHandler15onActiveChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickMultiPointHandler15onActiveChangedEv'
    self.uglySide.call(ritual)

  @overload(QPointerEvent)
  @overload(NoneType)
  def hasCurrentPoints(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickMultiPointHandler::hasCurrentPoints(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#hasCurrentPoints

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMultiPointHandler::hasCurrentPoints(QPointerEvent *event)
    return self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler16hasCurrentPointsEP13QPointerEv'
        'ent',
        self._addressOf(event),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def eligiblePoints(
      self,
      event: Optional[QPointerEvent],
  ) -> QList[QEventPoint]:
    """
    Calls Qt's 'QList<QEventPoint>
    QQuickMultiPointHandler::eligiblePoints(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#eligiblePoints

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QEventPoint]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QEventPoint>
    #      QQuickMultiPointHandler::eligiblePoints(QPointerEvent *event)
    address = self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler14eligiblePointsEP13QPointerEven'
        't',
        self._addressOf(event),
    )
    from ..QtGui import QEventPoint
    return QList[QEventPoint]._cuteOwning(address)

  @overload(QPointF)
  def averageTouchPointDistance(self, ref: QPointF) -> float:
    """
    Calls Qt's 'qreal
    QQuickMultiPointHandler::averageTouchPointDistance(const QPointF &ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html

    Parameters
    ----------

    ref : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QQuickMultiPointHandler::averageTouchPointDistance(const QPointF
    #      &ref)
    return self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler25averageTouchPointDistanceERK7Q'
        'PointF',
        self._valueOf(ref, 'QPointF'),
    )

  @overload(QPointF)
  def averageStartingDistance(self, ref: QPointF) -> float:
    """
    Calls Qt's 'qreal QQuickMultiPointHandler::averageStartingDistance(const
    QPointF &ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html

    Parameters
    ----------

    ref : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QQuickMultiPointHandler::averageStartingDistance(const QPointF
    #      &ref)
    return self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler23averageStartingDistanceERK7QPo'
        'intF',
        self._valueOf(ref, 'QPointF'),
    )

  @overload(QList[QEventPoint])
  def acceptPoints(self, points: QList[QEventPoint]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::acceptPoints(const
    QList<QEventPoint> &points)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#acceptPoints

    Parameters
    ----------

    points : QList[QEventPoint]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickMultiPointHandler::acceptPoints(const QList<QEventPoint>
    #      &points)
    self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler12acceptPointsERK5QListI11QEvent'
        'PointE',
        self._valueOf(points),
    )

  @overload(QPointerEvent, QList[QEventPoint])
  @overload(NoneType, QList[QEventPoint])
  def grabPoints(
      self,
      event: Optional[QPointerEvent],
      points: QList[QEventPoint],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickMultiPointHandler::grabPoints(QPointerEvent
    *event, const QList<QEventPoint> &points)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#grabPoints

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    points : QList[QEventPoint]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QQuickMultiPointHandler::grabPoints(QPointerEvent *event, const
    #      QList<QEventPoint> &points)
    return self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler10grabPointsEP13QPointerEventRK5'
        'QListI11QEventPointE',
        self._addressOf(event), self._valueOf(points),
    )

  @overload(QPointF)
  def moveTarget(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickMultiPointHandler::moveTarget(QPointF pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#moveTarget

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickMultiPointHandler::moveTarget(QPointF pos)
    self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler10moveTargetE7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  def d_func(self) -> Optional[QQuickMultiPointHandlerPrivate]:
    """
    Calls Qt's 'QQuickMultiPointHandlerPrivate
    *QQuickMultiPointHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandler.html#d_func

    Returns
    -------

    Optional[QQuickMultiPointHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMultiPointHandlerPrivate *QQuickMultiPointHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickMultiPointHandler6d_funcEv',
    )
    from . import QQuickMultiPointHandlerPrivate
    return QQuickMultiPointHandlerPrivate._cuteAt(address)

  @staticmethod
  def angles(*__, **_) -> Never:
    """
    Qt's 'QList<PointData> QQuickMultiPointHandler::angles(const QPointF
    &ref) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandler.angles' has no cute function yet. Qt's "
        "'QList<PointData> QQuickMultiPointHandler::angles(const QPointF "
        "&ref) const': gives a type Python has no way to take yet.")

  @staticmethod
  def averageAngleDelta(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickMultiPointHandler::averageAngleDelta(const
    QList<PointData> &old, const QList<PointData> &newAngles)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandler.averageAngleDelta' has no cute function "
        "yet. Qt's 'qreal QQuickMultiPointHandler::averageAngleDelta(const "
        "QList<PointData> &old, const QList<PointData> &newAngles)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def averageStartingAngle(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickMultiPointHandler::averageStartingAngle(const QPointF
    &ref)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandler.averageStartingAngle' has no cute "
        "function yet. Qt's 'qreal "
        "QQuickMultiPointHandler::averageStartingAngle(const QPointF "
        "&ref)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def averageTouchPointAngle(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickMultiPointHandler::averageTouchPointAngle(const QPointF
    &ref)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandler.averageTouchPointAngle' has no cute "
        "function yet. Qt's 'qreal "
        "QQuickMultiPointHandler::averageTouchPointAngle(const QPointF "
        "&ref)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def currentPoints(*__, **_) -> Never:
    """
    Qt's 'QList<QQuickHandlerPoint>
    &QQuickMultiPointHandler::currentPoints()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandler.currentPoints' has no cute function yet. "
        "Qt's 'QList<QQuickHandlerPoint> "
        "&QQuickMultiPointHandler::currentPoints()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def mutableCentroid(*__, **_) -> Never:
    """
    Qt's 'QQuickHandlerPoint &QQuickMultiPointHandler::mutableCentroid()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandler.mutableCentroid' has no cute function "
        "yet. Qt's 'QQuickHandlerPoint "
        "&QQuickMultiPointHandler::mutableCentroid()': gives a type Python "
        "has no way to take yet.")
