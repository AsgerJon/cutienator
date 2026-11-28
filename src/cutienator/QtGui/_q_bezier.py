"""
QBezier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qbezier_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QBezier to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLineF, QPointF, QRectF
  from . import QPolygonF, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPolygonF = WAIT['QPolygonF']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBezier(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBezier: a plain Python object standing in front of
  one C++ QBezier.

  C++ hands a QBezier around as a copy, so every C++ QBezier behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBezier that has a ritual and that Python can call
  so far, 24 names in all: 'fromPoints', 'pointAt', 'normalVector',
  'derivedAt', 'secondDerivedAt', 'toPolygon', 'addToPolygon', 'bounds',
  'length', 'tAtLength', 'tForY', 'pt1', 'pt2', 'pt3', 'pt4', 'mapBy',
  'midPoint', 'midTangent', 'startTangent', 'endTangent',
  'parameterSplitLeft', 'shifted', 'bezierOnInterval', 'getSubRange'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QBezier::coefficients(qreal t, qreal &a, qreal &b, qreal &c,
    qreal &d)': takes a number to change where it is.
  - Qt's 'void QBezier::addToPolygon(QDataBuffer<QPointF> &polygon, qreal
    bezier_flattening_threshold) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QBezier::addIfClose(qreal *length, qreal error) const': takes
    a number to change where it is.
  - Qt's 'int QBezier::stationaryYPoints(qreal &t0, qreal &t1) const': takes
    a number to change where it is.
  - Qt's 'std::pair<QBezier, QBezier> QBezier::split() const': gives a type
    Python has no way to take yet.
  - Qt's 'QBezier::~QBezier()': the destructor: Python removes its C++
    QBezier by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QBezier is created at the first use, not by 'QBezier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBezier back gives a copy the ritual made for Python,
    in a new cute QBezier.
  - Each name of Qt's QBezier that has no cute function yet, 'addIfClose',
    'coefficients', 'split', 'stationaryYPoints', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPointF, QPointF, QPointF, QPointF)
  def fromPoints(
      p1: QPointF,
      p2: QPointF,
      p3: QPointF,
      p4: QPointF,
  ) -> QBezier:
    """
    Calls Qt's 'QBezier QBezier::fromPoints(const QPointF &p1, const QPointF
    &p2, const QPointF &p3, const QPointF &p4)'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#fromPoints

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p3 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p4 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QBezier
      A new cute QBezier around the copy Qt gave back. Python owns it.
    """
    #  QBezier QBezier::fromPoints(const QPointF &p1, const QPointF &p2,
    #      const QPointF &p3, const QPointF &p4)
    address = Rituals.call(
        'ritual_ZN7QBezier10fromPointsERK7QPointFS2_S2_S2_',
        CuteMixin._valueOf(p1, 'QPointF'), CuteMixin._valueOf(p2, 'QPointF'),
        CuteMixin._valueOf(p3, 'QPointF'), CuteMixin._valueOf(p4, 'QPointF'),
    )
    return QBezier._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBezier'

  #  Qt's '~QBezier()'. Naming it makes this a value class: Python owns every
  #  C++ QBezier behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QBezierD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def pointAt(self, t: float) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::pointAt(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#pointAt

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::pointAt(qreal t) const
    address = self.uglySide.call('ritual_ZNK7QBezier7pointAtEd', t)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def normalVector(self, t: float) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::normalVector(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#normalVector

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::normalVector(qreal t) const
    address = self.uglySide.call('ritual_ZNK7QBezier12normalVectorEd', t)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def derivedAt(self, t: float) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::derivedAt(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#derivedAt

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::derivedAt(qreal t) const
    address = self.uglySide.call('ritual_ZNK7QBezier9derivedAtEd', t)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def secondDerivedAt(self, t: float) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::secondDerivedAt(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#secondDerivedAt

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::secondDerivedAt(qreal t) const
    address = self.uglySide.call('ritual_ZNK7QBezier15secondDerivedAtEd', t)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload()
  @overload(float)
  def toPolygon(self, bezier_flattening_threshold: float = 0.5) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QBezier::toPolygon(qreal
    bezier_flattening_threshold) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#toPolygon

    Parameters
    ----------

    bezier_flattening_threshold : float
      Passed on as it is. May be left out, as in Qt: it is then 0.5.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QBezier::toPolygon(qreal bezier_flattening_threshold) const
    address = self.uglySide.call(
        'ritual_ZNK7QBezier9toPolygonEd', bezier_flattening_threshold,
    )
    from . import QPolygonF
    return QPolygonF._cuteOwning(address)

  def bounds(self) -> QRectF:
    """
    Calls Qt's 'QRectF QBezier::bounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#bounds

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QBezier::bounds() const
    address = self.uglySide.call('ritual_ZNK7QBezier6boundsEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  @overload(float)
  def length(self, error: float = 0.01) -> float:
    """
    Calls Qt's 'qreal QBezier::length(qreal error) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#length

    Parameters
    ----------

    error : float
      Passed on as it is. May be left out, as in Qt: it is then 0.01.
    """
    #  qreal QBezier::length(qreal error) const
    return self.uglySide.call('ritual_ZNK7QBezier6lengthEd', error)

  @overload(float)
  def tAtLength(self, len: float) -> float:
    """
    Calls Qt's 'qreal QBezier::tAtLength(qreal len) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#tAtLength

    Parameters
    ----------

    len : float
      Passed on as it is.
    """
    #  qreal QBezier::tAtLength(qreal len) const
    return self.uglySide.call('ritual_ZNK7QBezier9tAtLengthEd', len)

  @overload(float, float, float)
  def tForY(self, t0: float, t1: float, y: float) -> float:
    """
    Calls Qt's 'qreal QBezier::tForY(qreal t0, qreal t1, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#tForY

    Parameters
    ----------

    t0 : float
      Passed on as it is.

    t1 : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  qreal QBezier::tForY(qreal t0, qreal t1, qreal y) const
    return self.uglySide.call('ritual_ZNK7QBezier5tForYEddd', t0, t1, y)

  def pt1(self) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::pt1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#pt1

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::pt1() const
    address = self.uglySide.call('ritual_ZNK7QBezier3pt1Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pt2(self) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::pt2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#pt2

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::pt2() const
    address = self.uglySide.call('ritual_ZNK7QBezier3pt2Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pt3(self) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::pt3() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#pt3

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::pt3() const
    address = self.uglySide.call('ritual_ZNK7QBezier3pt3Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pt4(self) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::pt4() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#pt4

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::pt4() const
    address = self.uglySide.call('ritual_ZNK7QBezier3pt4Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QTransform)
  def mapBy(self, transform: QTransform) -> QBezier:
    """
    Calls Qt's 'QBezier QBezier::mapBy(const QTransform &transform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#mapBy

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QBezier
      A new cute QBezier around the copy Qt gave back. Python owns it.
    """
    #  QBezier QBezier::mapBy(const QTransform &transform) const
    address = self.uglySide.call(
        'ritual_ZNK7QBezier5mapByERK10QTransform', self._valueOf(transform),
    )
    return QBezier._cuteOwning(address)

  def midPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QBezier::midPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#midPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QBezier::midPoint() const
    address = self.uglySide.call('ritual_ZNK7QBezier8midPointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def midTangent(self) -> QLineF:
    """
    Calls Qt's 'QLineF QBezier::midTangent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#midTangent

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QBezier::midTangent() const
    address = self.uglySide.call('ritual_ZNK7QBezier10midTangentEv')
    from ..QtCore import QLineF
    return QLineF._cuteOwning(address)

  def startTangent(self) -> QLineF:
    """
    Calls Qt's 'QLineF QBezier::startTangent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#startTangent

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QBezier::startTangent() const
    address = self.uglySide.call('ritual_ZNK7QBezier12startTangentEv')
    from ..QtCore import QLineF
    return QLineF._cuteOwning(address)

  def endTangent(self) -> QLineF:
    """
    Calls Qt's 'QLineF QBezier::endTangent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#endTangent

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QBezier::endTangent() const
    address = self.uglySide.call('ritual_ZNK7QBezier10endTangentEv')
    from ..QtCore import QLineF
    return QLineF._cuteOwning(address)

  @overload(THIS, int, float, float)
  @overload(NoneType, int, float, float)
  def shifted(
      self,
      curveSegments: Optional[QBezier],
      maxSegmets: int,
      offset: float,
      threshold: float,
  ) -> int:
    """
    Calls Qt's 'int QBezier::shifted(QBezier *curveSegments, int maxSegmets,
    qreal offset, float threshold) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#shifted

    Parameters
    ----------

    curveSegments : Optional[QBezier]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    maxSegmets : int
      Passed on as it is.

    offset : float
      Passed on as it is.

    threshold : float
      Passed on as it is.
    """
    #  int QBezier::shifted(QBezier *curveSegments, int maxSegmets, qreal
    #      offset, float threshold) const
    return self.uglySide.call(
        'ritual_ZNK7QBezier7shiftedEPS_idf',
        self._addressOf(curveSegments), maxSegmets, offset, threshold,
    )

  @overload(float, float)
  def bezierOnInterval(self, t0: float, t1: float) -> QBezier:
    """
    Calls Qt's 'QBezier QBezier::bezierOnInterval(qreal t0, qreal t1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#bezierOnInterval

    Parameters
    ----------

    t0 : float
      Passed on as it is.

    t1 : float
      Passed on as it is.

    Returns
    -------

    QBezier
      A new cute QBezier around the copy Qt gave back. Python owns it.
    """
    #  QBezier QBezier::bezierOnInterval(qreal t0, qreal t1) const
    address = self.uglySide.call(
        'ritual_ZNK7QBezier16bezierOnIntervalEdd', t0, t1,
    )
    return QBezier._cuteOwning(address)

  @overload(float, float)
  def getSubRange(self, t0: float, t1: float) -> QBezier:
    """
    Calls Qt's 'QBezier QBezier::getSubRange(qreal t0, qreal t1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#getSubRange

    Parameters
    ----------

    t0 : float
      Passed on as it is.

    t1 : float
      Passed on as it is.

    Returns
    -------

    QBezier
      A new cute QBezier around the copy Qt gave back. Python owns it.
    """
    #  QBezier QBezier::getSubRange(qreal t0, qreal t1) const
    address = self.uglySide.call(
        'ritual_ZNK7QBezier11getSubRangeEdd', t0, t1,
    )
    return QBezier._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QPolygonF)
  @overload(NoneType)
  @overload(QPolygonF, float)
  @overload(NoneType, float)
  def addToPolygon(
      self,
      p: Optional[QPolygonF],
      bezier_flattening_threshold: float = 0.5,
  ) -> None:
    """
    Calls Qt's 'void QBezier::addToPolygon(QPolygonF *p, qreal
    bezier_flattening_threshold) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#addToPolygon

    Parameters
    ----------

    p : Optional[QPolygonF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bezier_flattening_threshold : float
      Passed on as it is. May be left out, as in Qt: it is then 0.5.
    """
    #  void QBezier::addToPolygon(QPolygonF *p, qreal
    #      bezier_flattening_threshold) const
    self.uglySide.call(
        'ritual_ZNK7QBezier12addToPolygonEP9QPolygonFd',
        self._addressOf(p), bezier_flattening_threshold,
    )

  @overload(float, THIS)
  @overload(float, NoneType)
  def parameterSplitLeft(self, t: float, left: Optional[QBezier]) -> None:
    """
    Calls Qt's 'void QBezier::parameterSplitLeft(qreal t, QBezier *left)'.

    Qt's own words: https://doc.qt.io/qt-6/qbezier.html#parameterSplitLeft

    Parameters
    ----------

    t : float
      Passed on as it is.

    left : Optional[QBezier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBezier::parameterSplitLeft(qreal t, QBezier *left)
    self.uglySide.call(
        'ritual_ZN7QBezier18parameterSplitLeftEdPS_',
        t, self._addressOf(left),
    )

  @staticmethod
  def addIfClose(*__, **_) -> Never:
    """
    Qt's 'void QBezier::addIfClose(qreal *length, qreal error) const': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QBezier.addIfClose' has no cute function yet. Qt's 'void "
        "QBezier::addIfClose(qreal *length, qreal error) const': takes a "
        "number to change where it is.")

  @staticmethod
  def coefficients(*__, **_) -> Never:
    """
    Qt's 'void QBezier::coefficients(qreal t, qreal &a, qreal &b, qreal &c,
    qreal &d)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QBezier.coefficients' has no cute function yet. Qt's 'void "
        "QBezier::coefficients(qreal t, qreal &a, qreal &b, qreal &c, qreal "
        "&d)': takes a number to change where it is.")

  @staticmethod
  def split(*__, **_) -> Never:
    """
    Qt's 'std::pair<QBezier, QBezier> QBezier::split() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBezier.split' has no cute function yet. Qt's 'std::pair<QBezier, "
        "QBezier> QBezier::split() const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def stationaryYPoints(*__, **_) -> Never:
    """
    Qt's 'int QBezier::stationaryYPoints(qreal &t0, qreal &t1) const': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QBezier.stationaryYPoints' has no cute function yet. Qt's 'int "
        "QBezier::stationaryYPoints(qreal &t0, qreal &t1) const': takes a "
        "number to change where it is.")
