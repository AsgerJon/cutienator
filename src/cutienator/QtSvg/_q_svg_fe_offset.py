"""
QSvgFeOffset binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgFeOffset to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMap
from . import QtSvg, QSvgFeFilterPrimitive, QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QImage, QPainter
  from . import QSvgRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QSvgRectF = WAIT['QSvgRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgFeOffset(QSvgFeFilterPrimitive):
  """
  The cute side of Qt's QSvgFeOffset: a plain Python object standing in front
  of one C++ QSvgFeOffset.

  It is built on the cute 'QSvgFeFilterPrimitive', as Qt's QSvgFeOffset is
  built on Qt's QSvgFeFilterPrimitive, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgFeOffset that has a ritual and that Python can
  call so far, 4 names in all: 'type', 'apply', 'dx', 'dy'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFeOffset::~QSvgFeOffset()': the destructor: Python never
    removes a C++ QSvgFeOffset.

  What to expect
  --------------

  - The C++ QSvgFeOffset is created at the first use, not by
    'QSvgFeOffset(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgFeOffset.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgFeOffset'

  #  A C++ QSvgFeOffset Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFeOffset'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgFeOffset::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeoffset.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgFeOffset::type() const
    ritual = 'ritual_ZNK12QSvgFeOffset4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QSvgFeOffset4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  @overload(
      QMap[str, QImage], QPainter, QRectF, QRectF, QtSvg.UnitTypes,
      QtSvg.UnitTypes,
  )
  @overload(
      QMap[str, QImage], NoneType, QRectF, QRectF, QtSvg.UnitTypes,
      QtSvg.UnitTypes,
  )
  def apply(
      self,
      sources: QMap[str, QImage],
      p: Optional[QPainter],
      itemBounds: QRectF,
      filterBounds: QRectF,
      primitiveUnits: QtSvg.UnitTypes,
      filterUnits: QtSvg.UnitTypes,
  ) -> QImage:
    """
    Calls Qt's 'QImage QSvgFeOffset::apply(const QMap<QString, QImage>
    &sources, QPainter *p, const QRectF &itemBounds, const QRectF
    &filterBounds, QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes
    filterUnits) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeoffset.html#apply

    Parameters
    ----------

    sources : QMap[str, QImage]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    itemBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    filterBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    primitiveUnits : QtSvg.UnitTypes
      Passed on as its number.

    filterUnits : QtSvg.UnitTypes
      Passed on as its number.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSvgFeOffset::apply(const QMap<QString, QImage> &sources,
    #      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
    #      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QSvgFeOffset5applyERK4QMapI7QString6QImageEP8QPainterR'
        'K6QRectFSA_N5QtSvg9UnitTypesESC_',
        self._valueOf(sources), self._addressOf(p),
        self._valueOf(itemBounds), self._valueOf(filterBounds),
        primitiveUnits.value, filterUnits.value,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def dx(self) -> float:
    """
    Calls Qt's 'qreal QSvgFeOffset::dx() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeoffset.html#dx
    """
    #  qreal QSvgFeOffset::dx() const
    return self.uglySide.call('ritual_ZNK12QSvgFeOffset2dxEv')

  def dy(self) -> float:
    """
    Calls Qt's 'qreal QSvgFeOffset::dy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeoffset.html#dy
    """
    #  qreal QSvgFeOffset::dy() const
    return self.uglySide.call('ritual_ZNK12QSvgFeOffset2dyEv')

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

  @overload(QSvgNode, str, str, QSvgRectF, float, float)
  @overload(NoneType, str, str, QSvgRectF, float, float)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      input: str,
      result: str,
      rect: QSvgRectF,
      dx: float,
      dy: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgFeOffset::QSvgFeOffset(QSvgNode
    *parent, const QString &input, const QString &result, const QSvgRectF
    &rect, qreal dx, qreal dy)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeoffset.html#QSvgFeOffset

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    input : str
      Passed on as it is: a QString is made of it for the call.

    result : str
      Passed on as it is: a QString is made of it for the call.

    rect : QSvgRectF
      Passed on as a value: Qt reads the C++ QSvgRectF, which stays Python's
      own.

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  QSvgFeOffset::QSvgFeOffset(QSvgNode *parent, const QString &input,
    #      const QString &result, const QSvgRectF &rect, qreal dx, qreal dy)
    self._noteCreation(QSvgFeOffset, lambda: Rituals.call(
        'ritual_ZN12QSvgFeOffsetC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFdd',
        self._addressOf(parent), input, result, self._valueOf(rect), dx, dy,
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
