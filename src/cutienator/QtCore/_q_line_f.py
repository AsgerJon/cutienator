"""
QLineF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qline.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_line import QLine
from ._q_point_f import QPointF
from ._q_line_f_intersection_type import IntersectionType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLineF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLineF: a plain Python object standing in front of
  one C++ QLineF.

  C++ hands a QLineF around as a copy, so every C++ QLineF behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLineF that has a ritual and that Python can call so
  far, 27 names in all: 'fromPolar', 'isNull', 'p1', 'p2', 'x1', 'y1', 'x2',
  'y2', 'dx', 'dy', 'length', 'setLength', 'angle', 'setAngle', 'angleTo',
  'unitVector', 'normalVector', 'intersects', 'pointAt', 'translate',
  'translated', 'center', 'setP1', 'setP2', 'setPoints', 'setLine', 'toLine'.
  It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLineF::~QLineF()': the destructor: Python removes its C++ QLineF
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLineF is created at the first use, not by 'QLineF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLineF back gives a copy the ritual made for Python,
    in a new cute QLineF.
  """

  #  The enums Qt writes inside QLineF, and the names Qt has for the
  #  combinations of its flags enums.
  IntersectionType = IntersectionType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float, float)
  def fromPolar(length: float, angle: float) -> QLineF:
    """
    Calls Qt's 'QLineF QLineF::fromPolar(qreal length, qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#fromPolar

    Parameters
    ----------

    length : float
      Passed on as it is.

    angle : float
      Passed on as it is.

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QLineF::fromPolar(qreal length, qreal angle)
    address = Rituals.call('ritual_ZN6QLineF9fromPolarEdd', length, angle)
    return QLineF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLineF'

  #  Qt's '~QLineF()'. Naming it makes this a value class: Python owns every
  #  C++ QLineF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QLineFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QLineF::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#isNull
    """
    #  bool QLineF::isNull() const
    return self.uglySide.call('ritual_ZNK6QLineF6isNullEv')

  def p1(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLineF::p1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#p1

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLineF::p1() const
    address = self.uglySide.call('ritual_ZNK6QLineF2p1Ev')
    return QPointF._cuteOwning(address)

  def p2(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLineF::p2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#p2

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLineF::p2() const
    address = self.uglySide.call('ritual_ZNK6QLineF2p2Ev')
    return QPointF._cuteOwning(address)

  def x1(self) -> float:
    """
    Calls Qt's 'qreal QLineF::x1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#x1
    """
    #  qreal QLineF::x1() const
    return self.uglySide.call('ritual_ZNK6QLineF2x1Ev')

  def y1(self) -> float:
    """
    Calls Qt's 'qreal QLineF::y1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#y1
    """
    #  qreal QLineF::y1() const
    return self.uglySide.call('ritual_ZNK6QLineF2y1Ev')

  def x2(self) -> float:
    """
    Calls Qt's 'qreal QLineF::x2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#x2
    """
    #  qreal QLineF::x2() const
    return self.uglySide.call('ritual_ZNK6QLineF2x2Ev')

  def y2(self) -> float:
    """
    Calls Qt's 'qreal QLineF::y2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#y2
    """
    #  qreal QLineF::y2() const
    return self.uglySide.call('ritual_ZNK6QLineF2y2Ev')

  def dx(self) -> float:
    """
    Calls Qt's 'qreal QLineF::dx() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#dx
    """
    #  qreal QLineF::dx() const
    return self.uglySide.call('ritual_ZNK6QLineF2dxEv')

  def dy(self) -> float:
    """
    Calls Qt's 'qreal QLineF::dy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#dy
    """
    #  qreal QLineF::dy() const
    return self.uglySide.call('ritual_ZNK6QLineF2dyEv')

  def length(self) -> float:
    """
    Calls Qt's 'qreal QLineF::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#length
    """
    #  qreal QLineF::length() const
    return self.uglySide.call('ritual_ZNK6QLineF6lengthEv')

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QLineF::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#angle
    """
    #  qreal QLineF::angle() const
    return self.uglySide.call('ritual_ZNK6QLineF5angleEv')

  @overload(THIS)
  def angleTo(self, l: QLineF) -> float:
    """
    Calls Qt's 'qreal QLineF::angleTo(const QLineF &l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#angleTo

    Parameters
    ----------

    l : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  qreal QLineF::angleTo(const QLineF &l) const
    return self.uglySide.call(
        'ritual_ZNK6QLineF7angleToERKS_', self._valueOf(l),
    )

  def unitVector(self) -> QLineF:
    """
    Calls Qt's 'QLineF QLineF::unitVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#unitVector

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QLineF::unitVector() const
    address = self.uglySide.call('ritual_ZNK6QLineF10unitVectorEv')
    return QLineF._cuteOwning(address)

  def normalVector(self) -> QLineF:
    """
    Calls Qt's 'QLineF QLineF::normalVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#normalVector

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QLineF::normalVector() const
    address = self.uglySide.call('ritual_ZNK6QLineF12normalVectorEv')
    return QLineF._cuteOwning(address)

  @overload(THIS)
  @overload(THIS, QPointF)
  @overload(THIS, NoneType)
  def intersects(
      self,
      l: QLineF,
      intersectionPoint: Optional[QPointF] = None,
  ) -> IntersectionType:
    """
    Calls Qt's 'IntersectionType QLineF::intersects(const QLineF &l, QPointF
    *intersectionPoint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#intersects

    Parameters
    ----------

    l : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.

    intersectionPoint : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    IntersectionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'IntersectionType(number)'
      gives.
    """
    #  IntersectionType QLineF::intersects(const QLineF &l, QPointF
    #      *intersectionPoint) const
    return IntersectionType(self.uglySide.call(
        'ritual_ZNK6QLineF10intersectsERKS_P7QPointF',
        self._valueOf(l), self._addressOf(intersectionPoint),
    ))

  @overload(float)
  def pointAt(self, t: float) -> QPointF:
    """
    Calls Qt's 'QPointF QLineF::pointAt(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#pointAt

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLineF::pointAt(qreal t) const
    address = self.uglySide.call('ritual_ZNK6QLineF7pointAtEd', t)
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  def translated(self, p: QPointF) -> QLineF:
    """
    Calls Qt's 'QLineF QLineF::translated(const QPointF &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#translated

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QLineF::translated(const QPointF &p) const
    address = self.uglySide.call(
        'ritual_ZNK6QLineF10translatedERK7QPointF', self._valueOf(p),
    )
    return QLineF._cuteOwning(address)

  @overload(float, float)
  def translated(self, dx: float, dy: float) -> QLineF:
    """
    Calls Qt's 'QLineF QLineF::translated(qreal dx, qreal dy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#translated

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QLineF::translated(qreal dx, qreal dy) const
    address = self.uglySide.call('ritual_ZNK6QLineF10translatedEdd', dx, dy)
    return QLineF._cuteOwning(address)

  def center(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLineF::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#center

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLineF::center() const
    address = self.uglySide.call('ritual_ZNK6QLineF6centerEv')
    return QPointF._cuteOwning(address)

  def toLine(self) -> QLine:
    """
    Calls Qt's 'QLine QLineF::toLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#toLine

    Returns
    -------

    QLine
      A new cute QLine around the copy Qt gave back. Python owns it.
    """
    #  QLine QLineF::toLine() const
    address = self.uglySide.call('ritual_ZNK6QLineF6toLineEv')
    return QLine._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLength(self, len: float) -> None:
    """
    Calls Qt's 'void QLineF::setLength(qreal len)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#setLength

    Parameters
    ----------

    len : float
      Passed on as it is.
    """
    #  void QLineF::setLength(qreal len)
    self.uglySide.call('ritual_ZN6QLineF9setLengthEd', len)

  @overload(float)
  def setAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QLineF::setAngle(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#setAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QLineF::setAngle(qreal angle)
    self.uglySide.call('ritual_ZN6QLineF8setAngleEd', angle)

  @overload(QPointF)
  def setP1(self, p1: QPointF) -> None:
    """
    Calls Qt's 'void QLineF::setP1(const QPointF &p1)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#setP1

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLineF::setP1(const QPointF &p1)
    self.uglySide.call(
        'ritual_ZN6QLineF5setP1ERK7QPointF', self._valueOf(p1),
    )

  @overload(QPointF)
  def setP2(self, p2: QPointF) -> None:
    """
    Calls Qt's 'void QLineF::setP2(const QPointF &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#setP2

    Parameters
    ----------

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLineF::setP2(const QPointF &p2)
    self.uglySide.call(
        'ritual_ZN6QLineF5setP2ERK7QPointF', self._valueOf(p2),
    )

  @overload(QPointF, QPointF)
  def setPoints(self, p1: QPointF, p2: QPointF) -> None:
    """
    Calls Qt's 'void QLineF::setPoints(const QPointF &p1, const QPointF
    &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#setPoints

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLineF::setPoints(const QPointF &p1, const QPointF &p2)
    self.uglySide.call(
        'ritual_ZN6QLineF9setPointsERK7QPointFS2_',
        self._valueOf(p1), self._valueOf(p2),
    )

  @overload(float, float, float, float)
  def setLine(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QLineF::setLine(qreal x1, qreal y1, qreal x2, qreal
    y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#setLine

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.
    """
    #  void QLineF::setLine(qreal x1, qreal y1, qreal x2, qreal y2)
    self.uglySide.call('ritual_ZN6QLineF7setLineEdddd', x1, y1, x2, y2)

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
    Notes what was given, for Qt's 'QLineF::QLineF()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#QLineF
    """
    #  QLineF::QLineF()
    self._noteCreation(QLineF, lambda: Rituals.call('ritual_ZN6QLineFC1Ev'))

  @overload(QPointF, QPointF)
  def __init__(self, pt1: QPointF, pt2: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QLineF::QLineF(const QPointF &pt1, const
    QPointF &pt2)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#QLineF

    Parameters
    ----------

    pt1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pt2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QLineF::QLineF(const QPointF &pt1, const QPointF &pt2)
    self._noteCreation(QLineF, lambda: Rituals.call(
        'ritual_ZN6QLineFC1ERK7QPointFS2_',
        self._valueOf(pt1), self._valueOf(pt2),
    ))

  @overload(float, float, float, float)
  def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Notes what was given, for Qt's 'QLineF::QLineF(qreal x1, qreal y1, qreal
    x2, qreal y2)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#QLineF

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.
    """
    #  QLineF::QLineF(qreal x1, qreal y1, qreal x2, qreal y2)
    self._noteCreation(QLineF, lambda: Rituals.call(
        'ritual_ZN6QLineFC1Edddd', x1, y1, x2, y2,
    ))

  @overload(QLine)
  def __init__(self, line: QLine) -> None:
    """
    Notes what was given, for Qt's 'QLineF::QLineF(const QLine &line)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#QLineF

    Parameters
    ----------

    line : QLine
      Passed on as a value: Qt reads the C++ QLine, which stays Python's own.
    """
    #  QLineF::QLineF(const QLine &line)
    self._noteCreation(QLineF, lambda: Rituals.call(
        'ritual_ZN6QLineFC1ERK5QLine', self._valueOf(line),
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

  @overload(QPointF)
  def translate(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QLineF::translate(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#translate

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLineF::translate(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QLineF9translateERK7QPointF', self._valueOf(p),
    )

  @overload(float, float)
  def translate(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QLineF::translate(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qlinef.html#translate

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QLineF::translate(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN6QLineF9translateEdd', dx, dy)
