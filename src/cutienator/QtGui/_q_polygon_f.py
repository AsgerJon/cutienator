"""
QPolygonF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpolygon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QPointF
from ._q_polygon import QPolygon
from ..QtCore import QRectF


class QPolygonF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPolygonF: a plain Python object standing in front of
  one C++ QPolygonF.

  C++ hands a QPolygonF around as a copy, so every C++ QPolygonF behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPolygonF that has a ritual and that Python can call
  so far, 10 names in all: 'translate', 'translated', 'toPolygon',
  'isClosed', 'boundingRect', 'containsPoint', 'united', 'intersected',
  'subtracted', 'intersects'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant QPolygonF::operator QVariant() const': an operator, which
    is not reflected yet.
  - Qt's 'QPolygonF::~QPolygonF()': the destructor: Python removes its C++
    QPolygonF by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPolygonF is created at the first use, not by 'QPolygonF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPolygonF back gives a copy the ritual made for
    Python, in a new cute QPolygonF.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPolygonF'

  #  Qt's '~QPolygonF()'. Naming it makes this a value class: Python owns
  #  every C++ QPolygonF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QPolygonFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def translated(self, dx: float, dy: float) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QPolygonF::translated(qreal dx, qreal dy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#translated

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QPolygonF::translated(qreal dx, qreal dy) const
    address = self.uglySide.call(
        'ritual_ZNK9QPolygonF10translatedEdd', dx, dy,
    )
    return QPolygonF._cuteOwning(address)

  @overload(QPointF)
  def translated(self, offset: QPointF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QPolygonF::translated(const QPointF &offset)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#translated

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QPolygonF::translated(const QPointF &offset) const
    address = self.uglySide.call(
        'ritual_ZNK9QPolygonF10translatedERK7QPointF', self._valueOf(offset),
    )
    return QPolygonF._cuteOwning(address)

  def toPolygon(self) -> QPolygon:
    """
    Calls Qt's 'QPolygon QPolygonF::toPolygon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#toPolygon

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QPolygonF::toPolygon() const
    address = self.uglySide.call('ritual_ZNK9QPolygonF9toPolygonEv')
    return QPolygon._cuteOwning(address)

  def isClosed(self) -> bool:
    """
    Calls Qt's 'bool QPolygonF::isClosed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#isClosed
    """
    #  bool QPolygonF::isClosed() const
    return self.uglySide.call('ritual_ZNK9QPolygonF8isClosedEv')

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPolygonF::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPolygonF::boundingRect() const
    address = self.uglySide.call('ritual_ZNK9QPolygonF12boundingRectEv')
    return QRectF._cuteOwning(address)

  @overload(QPointF, Qt.FillRule)
  def containsPoint(self, pt: QPointF, fillRule: Qt.FillRule) -> bool:
    """
    Calls Qt's 'bool QPolygonF::containsPoint(const QPointF &pt, Qt::FillRule
    fillRule) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#containsPoint

    Parameters
    ----------

    pt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    fillRule : Qt.FillRule
      Passed on as its number.
    """
    #  bool QPolygonF::containsPoint(const QPointF &pt, Qt::FillRule
    #      fillRule) const
    return self.uglySide.call(
        'ritual_ZNK9QPolygonF13containsPointERK7QPointFN2Qt8FillRuleE',
        self._valueOf(pt), fillRule.value,
    )

  @overload(THIS)
  def united(self, r: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QPolygonF::united(const QPolygonF &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#united

    Parameters
    ----------

    r : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QPolygonF::united(const QPolygonF &r) const
    address = self.uglySide.call(
        'ritual_ZNK9QPolygonF6unitedERKS_', self._valueOf(r),
    )
    return QPolygonF._cuteOwning(address)

  @overload(THIS)
  def intersected(self, r: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QPolygonF::intersected(const QPolygonF &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#intersected

    Parameters
    ----------

    r : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QPolygonF::intersected(const QPolygonF &r) const
    address = self.uglySide.call(
        'ritual_ZNK9QPolygonF11intersectedERKS_', self._valueOf(r),
    )
    return QPolygonF._cuteOwning(address)

  @overload(THIS)
  def subtracted(self, r: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QPolygonF::subtracted(const QPolygonF &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#subtracted

    Parameters
    ----------

    r : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QPolygonF::subtracted(const QPolygonF &r) const
    address = self.uglySide.call(
        'ritual_ZNK9QPolygonF10subtractedERKS_', self._valueOf(r),
    )
    return QPolygonF._cuteOwning(address)

  @overload(THIS)
  def intersects(self, r: QPolygonF) -> bool:
    """
    Calls Qt's 'bool QPolygonF::intersects(const QPolygonF &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#intersects

    Parameters
    ----------

    r : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.
    """
    #  bool QPolygonF::intersects(const QPolygonF &r) const
    return self.uglySide.call(
        'ritual_ZNK9QPolygonF10intersectsERKS_', self._valueOf(r),
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPolygonF::QPolygonF()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#QPolygonF
    """
    #  QPolygonF::QPolygonF()
    self._noteCreation(QPolygonF, lambda: Rituals.call(
        'ritual_ZN9QPolygonFC1Ev',
    ))

  @overload(QRectF)
  def __init__(self, r: QRectF) -> None:
    """
    Notes what was given, for Qt's 'QPolygonF::QPolygonF(const QRectF &r)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#QPolygonF

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QPolygonF::QPolygonF(const QRectF &r)
    self._noteCreation(QPolygonF, lambda: Rituals.call(
        'ritual_ZN9QPolygonFC1ERK6QRectF', self._valueOf(r),
    ))

  @overload(QPolygon)
  def __init__(self, a: QPolygon) -> None:
    """
    Notes what was given, for Qt's 'QPolygonF::QPolygonF(const QPolygon &a)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#QPolygonF

    Parameters
    ----------

    a : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.
    """
    #  QPolygonF::QPolygonF(const QPolygon &a)
    self._noteCreation(QPolygonF, lambda: Rituals.call(
        'ritual_ZN9QPolygonFC1ERK8QPolygon', self._valueOf(a),
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

  @overload(float, float)
  def translate(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QPolygonF::translate(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#translate

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QPolygonF::translate(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN9QPolygonF9translateEdd', dx, dy)

  @overload(QPointF)
  def translate(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void QPolygonF::translate(const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolygonf.html#translate

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPolygonF::translate(const QPointF &offset)
    self.uglySide.call(
        'ritual_ZN9QPolygonF9translateERK7QPointF', self._valueOf(offset),
    )
