"""
QPolygon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpolygon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QPoint
from ..QtCore import QRect


class QPolygon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPolygon: a plain Python object standing in front of
  one C++ QPolygon.

  C++ hands a QPolygon around as a copy, so every C++ QPolygon behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPolygon that has a ritual and that Python can call
  so far, 12 names in all: 'translate', 'translated', 'boundingRect',
  'point', 'setPoint', 'putPoints', 'containsPoint', 'united', 'intersected',
  'subtracted', 'intersects', 'toPolygonF'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant QPolygon::operator QVariant() const': an operator, which
    is not reflected yet.
  - Qt's 'void QPolygon::point(int i, int *x, int *y) const': takes a number
    to change where it is.
  - Qt's 'QPolygon::~QPolygon()': the destructor: Python removes its C++
    QPolygon by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 28 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 takes any number of arguments.

  What to expect
  --------------

  - The C++ QPolygon is created at the first use, not by 'QPolygon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPolygon back gives a copy the ritual made for
    Python, in a new cute QPolygon.
  """

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QPolygonF = WAIT['QPolygonF']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPolygon'

  #  Qt's '~QPolygon()'. Naming it makes this a value class: Python owns
  #  every C++ QPolygon behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QPolygonD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def translated(self, dx: int, dy: int) -> QPolygon:
    """
    Calls Qt's 'QPolygon QPolygon::translated(int dx, int dy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#translated

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QPolygon::translated(int dx, int dy) const
    address = self.uglySide.call(
        'ritual_ZNK8QPolygon10translatedEii', dx, dy,
    )
    return QPolygon._cuteOwning(address)

  @overload(QPoint)
  def translated(self, offset: QPoint) -> QPolygon:
    """
    Calls Qt's 'QPolygon QPolygon::translated(const QPoint &offset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#translated

    Parameters
    ----------

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QPolygon::translated(const QPoint &offset) const
    address = self.uglySide.call(
        'ritual_ZNK8QPolygon10translatedERK6QPoint', self._valueOf(offset),
    )
    return QPolygon._cuteOwning(address)

  def boundingRect(self) -> QRect:
    """
    Calls Qt's 'QRect QPolygon::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#boundingRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPolygon::boundingRect() const
    address = self.uglySide.call('ritual_ZNK8QPolygon12boundingRectEv')
    return QRect._cuteOwning(address)

  @overload(int)
  def point(self, i: int) -> QPoint:
    """
    Calls Qt's 'QPoint QPolygon::point(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#point

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPolygon::point(int i) const
    address = self.uglySide.call('ritual_ZNK8QPolygon5pointEi', i)
    return QPoint._cuteOwning(address)

  @overload(QPoint, Qt.FillRule)
  def containsPoint(self, pt: QPoint, fillRule: Qt.FillRule) -> bool:
    """
    Calls Qt's 'bool QPolygon::containsPoint(const QPoint &pt, Qt::FillRule
    fillRule) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#containsPoint

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    fillRule : Qt.FillRule
      Passed on as its number.
    """
    #  bool QPolygon::containsPoint(const QPoint &pt, Qt::FillRule fillRule)
    #      const
    return self.uglySide.call(
        'ritual_ZNK8QPolygon13containsPointERK6QPointN2Qt8FillRuleE',
        self._valueOf(pt), fillRule.value,
    )

  @overload(THIS)
  def united(self, r: QPolygon) -> QPolygon:
    """
    Calls Qt's 'QPolygon QPolygon::united(const QPolygon &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#united

    Parameters
    ----------

    r : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QPolygon::united(const QPolygon &r) const
    address = self.uglySide.call(
        'ritual_ZNK8QPolygon6unitedERKS_', self._valueOf(r),
    )
    return QPolygon._cuteOwning(address)

  @overload(THIS)
  def intersected(self, r: QPolygon) -> QPolygon:
    """
    Calls Qt's 'QPolygon QPolygon::intersected(const QPolygon &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#intersected

    Parameters
    ----------

    r : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QPolygon::intersected(const QPolygon &r) const
    address = self.uglySide.call(
        'ritual_ZNK8QPolygon11intersectedERKS_', self._valueOf(r),
    )
    return QPolygon._cuteOwning(address)

  @overload(THIS)
  def subtracted(self, r: QPolygon) -> QPolygon:
    """
    Calls Qt's 'QPolygon QPolygon::subtracted(const QPolygon &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#subtracted

    Parameters
    ----------

    r : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QPolygon::subtracted(const QPolygon &r) const
    address = self.uglySide.call(
        'ritual_ZNK8QPolygon10subtractedERKS_', self._valueOf(r),
    )
    return QPolygon._cuteOwning(address)

  @overload(THIS)
  def intersects(self, r: QPolygon) -> bool:
    """
    Calls Qt's 'bool QPolygon::intersects(const QPolygon &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#intersects

    Parameters
    ----------

    r : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.
    """
    #  bool QPolygon::intersects(const QPolygon &r) const
    return self.uglySide.call(
        'ritual_ZNK8QPolygon10intersectsERKS_', self._valueOf(r),
    )

  def toPolygonF(self) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QPolygon::toPolygonF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#toPolygonF

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QPolygon::toPolygonF() const
    address = self.uglySide.call('ritual_ZNK8QPolygon10toPolygonFEv')
    return self.QPolygonF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  def setPoint(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void QPolygon::setPoint(int index, int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#setPoint

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QPolygon::setPoint(int index, int x, int y)
    self.uglySide.call('ritual_ZN8QPolygon8setPointEiii', index, x, y)

  @overload(int, QPoint)
  def setPoint(self, index: int, p: QPoint) -> None:
    """
    Calls Qt's 'void QPolygon::setPoint(int index, const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#setPoint

    Parameters
    ----------

    index : int
      Passed on as it is.

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QPolygon::setPoint(int index, const QPoint &p)
    self.uglySide.call(
        'ritual_ZN8QPolygon8setPointEiRK6QPoint', index, self._valueOf(p),
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
    Notes what was given, for Qt's 'QPolygon::QPolygon()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#QPolygon
    """
    #  QPolygon::QPolygon()
    self._noteCreation(QPolygon, lambda: Rituals.call(
        'ritual_ZN8QPolygonC1Ev',
    ))

  @overload(QRect)
  @overload(QRect, bool)
  def __init__(self, r: QRect, closed: bool = False) -> None:
    """
    Notes what was given, for Qt's 'QPolygon::QPolygon(const QRect &r, bool
    closed)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#QPolygon

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    closed : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QPolygon::QPolygon(const QRect &r, bool closed)
    self._noteCreation(QPolygon, lambda: Rituals.call(
        'ritual_ZN8QPolygonC1ERK5QRectb', self._valueOf(r), closed,
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

  @overload(int, int)
  def translate(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QPolygon::translate(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#translate

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QPolygon::translate(int dx, int dy)
    self.uglySide.call('ritual_ZN8QPolygon9translateEii', dx, dy)

  @overload(QPoint)
  def translate(self, offset: QPoint) -> None:
    """
    Calls Qt's 'void QPolygon::translate(const QPoint &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#translate

    Parameters
    ----------

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QPolygon::translate(const QPoint &offset)
    self.uglySide.call(
        'ritual_ZN8QPolygon9translateERK6QPoint', self._valueOf(offset),
    )

  @overload(int, int, THIS)
  @overload(int, int, THIS, int)
  def putPoints(
      self,
      index: int,
      nPoints: int,
      from_: QPolygon,
      fromIndex: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QPolygon::putPoints(int index, int nPoints, const
    QPolygon &from, int fromIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygon.html#putPoints

    Parameters
    ----------

    index : int
      Passed on as it is.

    nPoints : int
      Passed on as it is.

    from_ : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    fromIndex : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QPolygon::putPoints(int index, int nPoints, const QPolygon &from,
    #      int fromIndex)
    self.uglySide.call(
        'ritual_ZN8QPolygon9putPointsEiiRKS_i',
        index, nPoints, self._valueOf(from_), fromIndex,
    )
