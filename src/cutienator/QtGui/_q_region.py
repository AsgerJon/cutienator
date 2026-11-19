"""
QRegion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qregion.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QPoint
from ._q_polygon import QPolygon
from ..QtCore import QRect
from ._q_region_region_type import RegionType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRegion(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRegion: a plain Python object standing in front of
  one C++ QRegion.

  C++ hands a QRegion around as a copy, so every C++ QRegion behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRegion that has a ritual and that Python can call
  so far, 17 names in all: 'isEmpty', 'isNull', 'begin', 'cbegin', 'end',
  'cend', 'contains', 'translate', 'translated', 'united', 'intersected',
  'subtracted', 'xored', 'intersects', 'boundingRect', 'setRects',
  'rectCount'. It can be made from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRegion::~QRegion()': the destructor: Python removes its C++
    QRegion by it, and has no other use for it.
  - Qt's 'QRegion QRegion::operator|(const QRegion &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRegion QRegion::operator+(const QRegion &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRegion QRegion::operator+(const QRect &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRegion QRegion::operator&(const QRegion &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRegion QRegion::operator&(const QRect &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRegion QRegion::operator-(const QRegion &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QRegion QRegion::operator^(const QRegion &r) const': an operator,
    which is not reflected yet.
  - Qt's 'bool QRegion::operator==(const QRegion &r) const': an operator,
    which is not reflected yet.
  - Qt's 'bool QRegion::operator!=(const QRegion &r) const': an operator,
    which is not reflected yet.
  - Qt's 'QVariant QRegion::operator QVariant() const': an operator, which is
    not reflected yet.

  What has no ritual
  ------------------

  21 of the 61 functions Qt declares: 17 takes or gives a type that cannot be
  passed yet; 4 private.

  What to expect
  --------------

  - The C++ QRegion is created at the first use, not by 'QRegion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRegion back gives a copy the ritual made for Python,
    in a new cute QRegion.
  """

  #  The enums Qt writes inside QRegion, and the names Qt has for the
  #  combinations of its flags enums.
  RegionType = RegionType

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QBitmap = WAIT['QBitmap']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRegion'

  #  Qt's '~QRegion()'. Naming it makes this a value class: Python owns every
  #  C++ QRegion behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QRegionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QRegion::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#isEmpty
    """
    #  bool QRegion::isEmpty() const
    return self.uglySide.call('ritual_ZNK7QRegion7isEmptyEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QRegion::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#isNull
    """
    #  bool QRegion::isNull() const
    return self.uglySide.call('ritual_ZNK7QRegion6isNullEv')

  def begin(self) -> Optional[QRect]:
    """
    Calls Qt's 'const_iterator QRegion::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#begin

    Returns
    -------

    Optional[QRect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QRegion::begin() const
    address = self.uglySide.call('ritual_ZNK7QRegion5beginEv')
    return QRect._cuteAt(address)

  def cbegin(self) -> Optional[QRect]:
    """
    Calls Qt's 'const_iterator QRegion::cbegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#cbegin

    Returns
    -------

    Optional[QRect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QRegion::cbegin() const
    address = self.uglySide.call('ritual_ZNK7QRegion6cbeginEv')
    return QRect._cuteAt(address)

  def end(self) -> Optional[QRect]:
    """
    Calls Qt's 'const_iterator QRegion::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#end

    Returns
    -------

    Optional[QRect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QRegion::end() const
    address = self.uglySide.call('ritual_ZNK7QRegion3endEv')
    return QRect._cuteAt(address)

  def cend(self) -> Optional[QRect]:
    """
    Calls Qt's 'const_iterator QRegion::cend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#cend

    Returns
    -------

    Optional[QRect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QRegion::cend() const
    address = self.uglySide.call('ritual_ZNK7QRegion4cendEv')
    return QRect._cuteAt(address)

  @overload(QPoint)
  def contains(self, p: QPoint) -> bool:
    """
    Calls Qt's 'bool QRegion::contains(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#contains

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QRegion::contains(const QPoint &p) const
    return self.uglySide.call(
        'ritual_ZNK7QRegion8containsERK6QPoint', self._valueOf(p),
    )

  @overload(QRect)
  def contains(self, r: QRect) -> bool:
    """
    Calls Qt's 'bool QRegion::contains(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#contains

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QRegion::contains(const QRect &r) const
    return self.uglySide.call(
        'ritual_ZNK7QRegion8containsERK5QRect', self._valueOf(r),
    )

  @overload(int, int)
  def translated(self, dx: int, dy: int) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::translated(int dx, int dy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#translated

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::translated(int dx, int dy) const
    address = self.uglySide.call('ritual_ZNK7QRegion10translatedEii', dx, dy)
    return QRegion._cuteOwning(address)

  @overload(QPoint)
  def translated(self, p: QPoint) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::translated(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#translated

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::translated(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegion10translatedERK6QPoint', self._valueOf(p),
    )
    return QRegion._cuteOwning(address)

  @overload(THIS)
  def united(self, r: QRegion) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::united(const QRegion &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#united

    Parameters
    ----------

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::united(const QRegion &r) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegion6unitedERKS_', self._valueOf(r),
    )
    return QRegion._cuteOwning(address)

  @overload(QRect)
  def united(self, r: QRect) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::united(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#united

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::united(const QRect &r) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegion6unitedERK5QRect', self._valueOf(r),
    )
    return QRegion._cuteOwning(address)

  @overload(THIS)
  def intersected(self, r: QRegion) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::intersected(const QRegion &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#intersected

    Parameters
    ----------

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::intersected(const QRegion &r) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegion11intersectedERKS_', self._valueOf(r),
    )
    return QRegion._cuteOwning(address)

  @overload(QRect)
  def intersected(self, r: QRect) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::intersected(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#intersected

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::intersected(const QRect &r) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegion11intersectedERK5QRect', self._valueOf(r),
    )
    return QRegion._cuteOwning(address)

  @overload(THIS)
  def subtracted(self, r: QRegion) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::subtracted(const QRegion &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#subtracted

    Parameters
    ----------

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::subtracted(const QRegion &r) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegion10subtractedERKS_', self._valueOf(r),
    )
    return QRegion._cuteOwning(address)

  @overload(THIS)
  def xored(self, r: QRegion) -> QRegion:
    """
    Calls Qt's 'QRegion QRegion::xored(const QRegion &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#xored

    Parameters
    ----------

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QRegion::xored(const QRegion &r) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegion5xoredERKS_', self._valueOf(r),
    )
    return QRegion._cuteOwning(address)

  @overload(THIS)
  def intersects(self, r: QRegion) -> bool:
    """
    Calls Qt's 'bool QRegion::intersects(const QRegion &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#intersects

    Parameters
    ----------

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  bool QRegion::intersects(const QRegion &r) const
    return self.uglySide.call(
        'ritual_ZNK7QRegion10intersectsERKS_', self._valueOf(r),
    )

  @overload(QRect)
  def intersects(self, r: QRect) -> bool:
    """
    Calls Qt's 'bool QRegion::intersects(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#intersects

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QRegion::intersects(const QRect &r) const
    return self.uglySide.call(
        'ritual_ZNK7QRegion10intersectsERK5QRect', self._valueOf(r),
    )

  def boundingRect(self) -> QRect:
    """
    Calls Qt's 'QRect QRegion::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#boundingRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRegion::boundingRect() const
    address = self.uglySide.call('ritual_ZNK7QRegion12boundingRectEv')
    return QRect._cuteOwning(address)

  def rectCount(self) -> int:
    """
    Calls Qt's 'int QRegion::rectCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#rectCount
    """
    #  int QRegion::rectCount() const
    return self.uglySide.call('ritual_ZNK7QRegion9rectCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect, int)
  @overload(NoneType, int)
  def setRects(self, rect: Optional[QRect], num: int) -> None:
    """
    Calls Qt's 'void QRegion::setRects(const QRect *rect, int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#setRects

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    num : int
      Passed on as it is.
    """
    #  void QRegion::setRects(const QRect *rect, int num)
    self.uglySide.call(
        'ritual_ZN7QRegion8setRectsEPK5QRecti', self._addressOf(rect), num,
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
    Notes what was given, for Qt's 'QRegion::QRegion()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#QRegion
    """
    #  QRegion::QRegion()
    self._noteCreation(QRegion, lambda: Rituals.call(
        'ritual_ZN7QRegionC1Ev',
    ))

  @overload(int, int, int, int)
  @overload(int, int, int, int, RegionType)
  def __init__(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      t: RegionType = RegionType.Rectangle,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRegion::QRegion(int x, int y, int w, int
    h, RegionType t)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#QRegion

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    t : RegionType
      Passed on as its number. May be left out, as in Qt: it is then
      RegionType.Rectangle.
    """
    #  QRegion::QRegion(int x, int y, int w, int h, RegionType t)
    self._noteCreation(QRegion, lambda: Rituals.call(
        'ritual_ZN7QRegionC1EiiiiNS_10RegionTypeE', x, y, w, h, t.value,
    ))

  @overload(QRect)
  @overload(QRect, RegionType)
  def __init__(self, r: QRect, t: RegionType = RegionType.Rectangle) -> None:
    """
    Notes what was given, for Qt's 'QRegion::QRegion(const QRect &r,
    RegionType t)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#QRegion

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    t : RegionType
      Passed on as its number. May be left out, as in Qt: it is then
      RegionType.Rectangle.
    """
    #  QRegion::QRegion(const QRect &r, RegionType t)
    self._noteCreation(QRegion, lambda: Rituals.call(
        'ritual_ZN7QRegionC1ERK5QRectNS_10RegionTypeE',
        self._valueOf(r), t.value,
    ))

  @overload(QPolygon)
  @overload(QPolygon, Qt.FillRule)
  def __init__(
      self,
      pa: QPolygon,
      fillRule: Qt.FillRule = Qt.FillRule.OddEvenFill,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRegion::QRegion(const QPolygon &pa,
    Qt::FillRule fillRule)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#QRegion

    Parameters
    ----------

    pa : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    fillRule : Qt.FillRule
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FillRule.OddEvenFill.
    """
    #  QRegion::QRegion(const QPolygon &pa, Qt::FillRule fillRule)
    self._noteCreation(QRegion, lambda: Rituals.call(
        'ritual_ZN7QRegionC1ERK8QPolygonN2Qt8FillRuleE',
        self._valueOf(pa), fillRule.value,
    ))

  @overload(THIS)
  def __init__(self, region: QRegion) -> None:
    """
    Notes what was given, for Qt's 'QRegion::QRegion(const QRegion &region)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#QRegion

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  QRegion::QRegion(const QRegion &region)
    self._noteCreation(QRegion, lambda: Rituals.call(
        'ritual_ZN7QRegionC1ERKS_', self._valueOf(region),
    ))

  @overload(QBitmap)
  def __init__(self, bitmap: QBitmap) -> None:
    """
    Notes what was given, for Qt's 'QRegion::QRegion(const QBitmap &bitmap)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#QRegion

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    bitmap : QBitmap
      Passed on as a value: Qt reads the C++ QBitmap, which stays Python's
      own.
    """
    #  QRegion::QRegion(const QBitmap &bitmap)
    self._noteCreation(QRegion, lambda: Rituals.call(
        'ritual_ZN7QRegionC1ERK7QBitmap', self._valueOf(bitmap),
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
    Calls Qt's 'void QRegion::translate(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#translate

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QRegion::translate(int dx, int dy)
    self.uglySide.call('ritual_ZN7QRegion9translateEii', dx, dy)

  @overload(QPoint)
  def translate(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRegion::translate(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qregion.html#translate

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRegion::translate(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN7QRegion9translateERK6QPoint', self._valueOf(p),
    )
