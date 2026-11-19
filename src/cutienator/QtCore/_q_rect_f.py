"""
QRectF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qrect.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_margins_f import QMarginsF
from ._q_point_f import QPointF
from ._q_rect import QRect
from ._q_size_f import QSizeF


class QRectF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRectF: a plain Python object standing in front of
  one C++ QRectF.

  C++ hands a QRectF around as a copy, so every C++ QRectF behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRectF that has a ritual and that Python can call so
  far, 56 names in all: 'isNull', 'isEmpty', 'isValid', 'normalized', 'left',
  'top', 'right', 'bottom', 'x', 'y', 'setLeft', 'setTop', 'setRight',
  'setBottom', 'setX', 'setY', 'topLeft', 'bottomRight', 'topRight',
  'bottomLeft', 'center', 'setTopLeft', 'setBottomRight', 'setTopRight',
  'setBottomLeft', 'moveLeft', 'moveTop', 'moveRight', 'moveBottom',
  'moveTopLeft', 'moveBottomRight', 'moveTopRight', 'moveBottomLeft',
  'moveCenter', 'translate', 'translated', 'transposed', 'moveTo', 'setRect',
  'setCoords', 'adjust', 'adjusted', 'size', 'width', 'height', 'setWidth',
  'setHeight', 'setSize', 'contains', 'united', 'intersected', 'intersects',
  'marginsAdded', 'marginsRemoved', 'toRect', 'toAlignedRect'. It can be made
  from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QRectF::getRect(qreal *x, qreal *y, qreal *w, qreal *h)
    const': takes a number to change where it is.
  - Qt's 'void QRectF::getCoords(qreal *x1, qreal *y1, qreal *x2, qreal *y2)
    const': takes a number to change where it is.
  - Qt's 'QRectF QRectF::operator|(const QRectF &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRectF QRectF::operator&(const QRectF &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRectF::~QRectF()': the destructor: Python removes its C++ QRectF
    by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 75 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QRectF is created at the first use, not by 'QRectF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRectF back gives a copy the ritual made for Python,
    in a new cute QRectF.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRectF'

  #  Qt's '~QRectF()'. Naming it makes this a value class: Python owns every
  #  C++ QRectF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QRectFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QRectF::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#isNull
    """
    #  bool QRectF::isNull() const
    return self.uglySide.call('ritual_ZNK6QRectF6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QRectF::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#isEmpty
    """
    #  bool QRectF::isEmpty() const
    return self.uglySide.call('ritual_ZNK6QRectF7isEmptyEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRectF::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#isValid
    """
    #  bool QRectF::isValid() const
    return self.uglySide.call('ritual_ZNK6QRectF7isValidEv')

  def normalized(self) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#normalized

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::normalized() const
    address = self.uglySide.call('ritual_ZNK6QRectF10normalizedEv')
    return QRectF._cuteOwning(address)

  def left(self) -> float:
    """
    Calls Qt's 'qreal QRectF::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#left
    """
    #  qreal QRectF::left() const
    return self.uglySide.call('ritual_ZNK6QRectF4leftEv')

  def top(self) -> float:
    """
    Calls Qt's 'qreal QRectF::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#top
    """
    #  qreal QRectF::top() const
    return self.uglySide.call('ritual_ZNK6QRectF3topEv')

  def right(self) -> float:
    """
    Calls Qt's 'qreal QRectF::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#right
    """
    #  qreal QRectF::right() const
    return self.uglySide.call('ritual_ZNK6QRectF5rightEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'qreal QRectF::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#bottom
    """
    #  qreal QRectF::bottom() const
    return self.uglySide.call('ritual_ZNK6QRectF6bottomEv')

  def x(self) -> float:
    """
    Calls Qt's 'qreal QRectF::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#x
    """
    #  qreal QRectF::x() const
    return self.uglySide.call('ritual_ZNK6QRectF1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QRectF::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#y
    """
    #  qreal QRectF::y() const
    return self.uglySide.call('ritual_ZNK6QRectF1yEv')

  def topLeft(self) -> QPointF:
    """
    Calls Qt's 'QPointF QRectF::topLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#topLeft

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QRectF::topLeft() const
    address = self.uglySide.call('ritual_ZNK6QRectF7topLeftEv')
    return QPointF._cuteOwning(address)

  def bottomRight(self) -> QPointF:
    """
    Calls Qt's 'QPointF QRectF::bottomRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#bottomRight

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QRectF::bottomRight() const
    address = self.uglySide.call('ritual_ZNK6QRectF11bottomRightEv')
    return QPointF._cuteOwning(address)

  def topRight(self) -> QPointF:
    """
    Calls Qt's 'QPointF QRectF::topRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#topRight

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QRectF::topRight() const
    address = self.uglySide.call('ritual_ZNK6QRectF8topRightEv')
    return QPointF._cuteOwning(address)

  def bottomLeft(self) -> QPointF:
    """
    Calls Qt's 'QPointF QRectF::bottomLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#bottomLeft

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QRectF::bottomLeft() const
    address = self.uglySide.call('ritual_ZNK6QRectF10bottomLeftEv')
    return QPointF._cuteOwning(address)

  def center(self) -> QPointF:
    """
    Calls Qt's 'QPointF QRectF::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#center

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QRectF::center() const
    address = self.uglySide.call('ritual_ZNK6QRectF6centerEv')
    return QPointF._cuteOwning(address)

  @overload(float, float)
  def translated(self, dx: float, dy: float) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::translated(qreal dx, qreal dy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#translated

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::translated(qreal dx, qreal dy) const
    address = self.uglySide.call('ritual_ZNK6QRectF10translatedEdd', dx, dy)
    return QRectF._cuteOwning(address)

  @overload(QPointF)
  def translated(self, p: QPointF) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::translated(const QPointF &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#translated

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::translated(const QPointF &p) const
    address = self.uglySide.call(
        'ritual_ZNK6QRectF10translatedERK7QPointF', self._valueOf(p),
    )
    return QRectF._cuteOwning(address)

  def transposed(self) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#transposed

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::transposed() const
    address = self.uglySide.call('ritual_ZNK6QRectF10transposedEv')
    return QRectF._cuteOwning(address)

  @overload(float, float, float, float)
  def adjusted(self, x1: float, y1: float, x2: float, y2: float) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::adjusted(qreal x1, qreal y1, qreal x2, qreal
    y2) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#adjusted

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

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::adjusted(qreal x1, qreal y1, qreal x2, qreal y2) const
    address = self.uglySide.call(
        'ritual_ZNK6QRectF8adjustedEdddd', x1, y1, x2, y2,
    )
    return QRectF._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QRectF::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QRectF::size() const
    address = self.uglySide.call('ritual_ZNK6QRectF4sizeEv')
    return QSizeF._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QRectF::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#width
    """
    #  qreal QRectF::width() const
    return self.uglySide.call('ritual_ZNK6QRectF5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QRectF::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#height
    """
    #  qreal QRectF::height() const
    return self.uglySide.call('ritual_ZNK6QRectF6heightEv')

  @overload(THIS)
  def contains(self, r: QRectF) -> bool:
    """
    Calls Qt's 'bool QRectF::contains(const QRectF &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#contains

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QRectF::contains(const QRectF &r) const
    return self.uglySide.call(
        'ritual_ZNK6QRectF8containsERKS_', self._valueOf(r),
    )

  @overload(QPointF)
  def contains(self, p: QPointF) -> bool:
    """
    Calls Qt's 'bool QRectF::contains(const QPointF &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#contains

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QRectF::contains(const QPointF &p) const
    return self.uglySide.call(
        'ritual_ZNK6QRectF8containsERK7QPointF', self._valueOf(p),
    )

  @overload(float, float)
  def contains(self, x: float, y: float) -> bool:
    """
    Calls Qt's 'bool QRectF::contains(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#contains

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  bool QRectF::contains(qreal x, qreal y) const
    return self.uglySide.call('ritual_ZNK6QRectF8containsEdd', x, y)

  @overload(THIS)
  def united(self, other: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::united(const QRectF &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#united

    Parameters
    ----------

    other : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::united(const QRectF &other) const
    address = self.uglySide.call(
        'ritual_ZNK6QRectF6unitedERKS_', self._valueOf(other),
    )
    return QRectF._cuteOwning(address)

  @overload(THIS)
  def intersected(self, other: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::intersected(const QRectF &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#intersected

    Parameters
    ----------

    other : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::intersected(const QRectF &other) const
    address = self.uglySide.call(
        'ritual_ZNK6QRectF11intersectedERKS_', self._valueOf(other),
    )
    return QRectF._cuteOwning(address)

  @overload(THIS)
  def intersects(self, r: QRectF) -> bool:
    """
    Calls Qt's 'bool QRectF::intersects(const QRectF &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#intersects

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QRectF::intersects(const QRectF &r) const
    return self.uglySide.call(
        'ritual_ZNK6QRectF10intersectsERKS_', self._valueOf(r),
    )

  @overload(QMarginsF)
  def marginsAdded(self, margins: QMarginsF) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::marginsAdded(const QMarginsF &margins) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#marginsAdded

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::marginsAdded(const QMarginsF &margins) const
    address = self.uglySide.call(
        'ritual_ZNK6QRectF12marginsAddedERK9QMarginsF',
        self._valueOf(margins),
    )
    return QRectF._cuteOwning(address)

  @overload(QMarginsF)
  def marginsRemoved(self, margins: QMarginsF) -> QRectF:
    """
    Calls Qt's 'QRectF QRectF::marginsRemoved(const QMarginsF &margins)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#marginsRemoved

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRectF::marginsRemoved(const QMarginsF &margins) const
    address = self.uglySide.call(
        'ritual_ZNK6QRectF14marginsRemovedERK9QMarginsF',
        self._valueOf(margins),
    )
    return QRectF._cuteOwning(address)

  def toRect(self) -> QRect:
    """
    Calls Qt's 'QRect QRectF::toRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#toRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRectF::toRect() const
    address = self.uglySide.call('ritual_ZNK6QRectF6toRectEv')
    return QRect._cuteOwning(address)

  def toAlignedRect(self) -> QRect:
    """
    Calls Qt's 'QRect QRectF::toAlignedRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#toAlignedRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRectF::toAlignedRect() const
    address = self.uglySide.call('ritual_ZNK6QRectF13toAlignedRectEv')
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLeft(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::setLeft(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setLeft

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::setLeft(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF7setLeftEd', pos)

  @overload(float)
  def setTop(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::setTop(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setTop

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::setTop(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF6setTopEd', pos)

  @overload(float)
  def setRight(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::setRight(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setRight

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::setRight(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF8setRightEd', pos)

  @overload(float)
  def setBottom(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::setBottom(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setBottom

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::setBottom(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF9setBottomEd', pos)

  @overload(float)
  def setX(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::setX(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setX

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::setX(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF4setXEd', pos)

  @overload(float)
  def setY(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::setY(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setY

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::setY(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF4setYEd', pos)

  @overload(QPointF)
  def setTopLeft(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::setTopLeft(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setTopLeft

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::setTopLeft(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF10setTopLeftERK7QPointF', self._valueOf(p),
    )

  @overload(QPointF)
  def setBottomRight(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::setBottomRight(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setBottomRight

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::setBottomRight(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF14setBottomRightERK7QPointF', self._valueOf(p),
    )

  @overload(QPointF)
  def setTopRight(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::setTopRight(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setTopRight

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::setTopRight(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF11setTopRightERK7QPointF', self._valueOf(p),
    )

  @overload(QPointF)
  def setBottomLeft(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::setBottomLeft(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setBottomLeft

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::setBottomLeft(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF13setBottomLeftERK7QPointF', self._valueOf(p),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QRectF::setRect(qreal x, qreal y, qreal w, qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QRectF::setRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call('ritual_ZN6QRectF7setRectEdddd', x, y, w, h)

  @overload(float, float, float, float)
  def setCoords(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QRectF::setCoords(qreal x1, qreal y1, qreal x2, qreal
    y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setCoords

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
    #  void QRectF::setCoords(qreal x1, qreal y1, qreal x2, qreal y2)
    self.uglySide.call('ritual_ZN6QRectF9setCoordsEdddd', x1, y1, x2, y2)

  @overload(float)
  def setWidth(self, w: float) -> None:
    """
    Calls Qt's 'void QRectF::setWidth(qreal w)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setWidth

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QRectF::setWidth(qreal w)
    self.uglySide.call('ritual_ZN6QRectF8setWidthEd', w)

  @overload(float)
  def setHeight(self, h: float) -> None:
    """
    Calls Qt's 'void QRectF::setHeight(qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setHeight

    Parameters
    ----------

    h : float
      Passed on as it is.
    """
    #  void QRectF::setHeight(qreal h)
    self.uglySide.call('ritual_ZN6QRectF9setHeightEd', h)

  @overload(QSizeF)
  def setSize(self, s: QSizeF) -> None:
    """
    Calls Qt's 'void QRectF::setSize(const QSizeF &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#setSize

    Parameters
    ----------

    s : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QRectF::setSize(const QSizeF &s)
    self.uglySide.call(
        'ritual_ZN6QRectF7setSizeERK6QSizeF', self._valueOf(s),
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
    Notes what was given, for Qt's 'QRectF::QRectF()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#QRectF
    """
    #  QRectF::QRectF()
    self._noteCreation(QRectF, lambda: Rituals.call('ritual_ZN6QRectFC1Ev'))

  @overload(QPointF, QSizeF)
  def __init__(self, topleft: QPointF, size: QSizeF) -> None:
    """
    Notes what was given, for Qt's 'QRectF::QRectF(const QPointF &topleft,
    const QSizeF &size)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#QRectF

    Parameters
    ----------

    topleft : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  QRectF::QRectF(const QPointF &topleft, const QSizeF &size)
    self._noteCreation(QRectF, lambda: Rituals.call(
        'ritual_ZN6QRectFC1ERK7QPointFRK6QSizeF',
        self._valueOf(topleft), self._valueOf(size),
    ))

  @overload(QPointF, QPointF)
  def __init__(self, topleft: QPointF, bottomRight: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QRectF::QRectF(const QPointF &topleft,
    const QPointF &bottomRight)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#QRectF

    Parameters
    ----------

    topleft : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    bottomRight : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QRectF::QRectF(const QPointF &topleft, const QPointF &bottomRight)
    self._noteCreation(QRectF, lambda: Rituals.call(
        'ritual_ZN6QRectFC1ERK7QPointFS2_',
        self._valueOf(topleft), self._valueOf(bottomRight),
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      left: float,
      top: float,
      width: float,
      height: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRectF::QRectF(qreal left, qreal top,
    qreal width, qreal height)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#QRectF

    Parameters
    ----------

    left : float
      Passed on as it is.

    top : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  QRectF::QRectF(qreal left, qreal top, qreal width, qreal height)
    self._noteCreation(QRectF, lambda: Rituals.call(
        'ritual_ZN6QRectFC1Edddd', left, top, width, height,
    ))

  @overload(QRect)
  def __init__(self, rect: QRect) -> None:
    """
    Notes what was given, for Qt's 'QRectF::QRectF(const QRect &rect)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#QRectF

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QRectF::QRectF(const QRect &rect)
    self._noteCreation(QRectF, lambda: Rituals.call(
        'ritual_ZN6QRectFC1ERK5QRect', self._valueOf(rect),
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

  @overload(float)
  def moveLeft(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::moveLeft(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveLeft

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::moveLeft(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF8moveLeftEd', pos)

  @overload(float)
  def moveTop(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::moveTop(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveTop

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::moveTop(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF7moveTopEd', pos)

  @overload(float)
  def moveRight(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::moveRight(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveRight

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::moveRight(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF9moveRightEd', pos)

  @overload(float)
  def moveBottom(self, pos: float) -> None:
    """
    Calls Qt's 'void QRectF::moveBottom(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveBottom

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QRectF::moveBottom(qreal pos)
    self.uglySide.call('ritual_ZN6QRectF10moveBottomEd', pos)

  @overload(QPointF)
  def moveTopLeft(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::moveTopLeft(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveTopLeft

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::moveTopLeft(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF11moveTopLeftERK7QPointF', self._valueOf(p),
    )

  @overload(QPointF)
  def moveBottomRight(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::moveBottomRight(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveBottomRight

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::moveBottomRight(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF15moveBottomRightERK7QPointF', self._valueOf(p),
    )

  @overload(QPointF)
  def moveTopRight(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::moveTopRight(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveTopRight

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::moveTopRight(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF12moveTopRightERK7QPointF', self._valueOf(p),
    )

  @overload(QPointF)
  def moveBottomLeft(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::moveBottomLeft(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveBottomLeft

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::moveBottomLeft(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF14moveBottomLeftERK7QPointF', self._valueOf(p),
    )

  @overload(QPointF)
  def moveCenter(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::moveCenter(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveCenter

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::moveCenter(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF10moveCenterERK7QPointF', self._valueOf(p),
    )

  @overload(float, float)
  def translate(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QRectF::translate(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#translate

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QRectF::translate(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN6QRectF9translateEdd', dx, dy)

  @overload(QPointF)
  def translate(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::translate(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#translate

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::translate(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF9translateERK7QPointF', self._valueOf(p),
    )

  @overload(float, float)
  def moveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QRectF::moveTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QRectF::moveTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN6QRectF6moveToEdd', x, y)

  @overload(QPointF)
  def moveTo(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QRectF::moveTo(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#moveTo

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRectF::moveTo(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN6QRectF6moveToERK7QPointF', self._valueOf(p),
    )

  @overload(float, float, float, float)
  def adjust(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QRectF::adjust(qreal x1, qreal y1, qreal x2, qreal y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qrectf.html#adjust

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
    #  void QRectF::adjust(qreal x1, qreal y1, qreal x2, qreal y2)
    self.uglySide.call('ritual_ZN6QRectF6adjustEdddd', x1, y1, x2, y2)
