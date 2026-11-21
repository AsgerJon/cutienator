"""
QAbstractGraphicsShapeItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QBrush, QPainterPath, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QPen = WAIT['QPen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractGraphicsShapeItem(QGraphicsItem):
  """
  The cute side of Qt's QAbstractGraphicsShapeItem: a plain Python object
  standing in front of one C++ QAbstractGraphicsShapeItem.

  It is built on the cute 'QGraphicsItem', as Qt's QAbstractGraphicsShapeItem
  is built on Qt's QGraphicsItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractGraphicsShapeItem that has a ritual and
  that Python can call so far, 6 names in all: 'pen', 'setPen', 'brush',
  'setBrush', 'isObscuredBy', 'opaqueArea'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractGraphicsShapeItem::~QAbstractGraphicsShapeItem()': the
    destructor: Python never removes a C++ QAbstractGraphicsShapeItem.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 2 forbidden; 2 private; 1 the class is
  abstract, so C++ cannot make one; 1 protected.

  What to expect
  --------------

  - The C++ QAbstractGraphicsShapeItem is created at the first use, not by
    'QAbstractGraphicsShapeItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractGraphicsShapeItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractGraphicsShapeItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QAbstractGraphicsShapeItem::pen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgraphicsshapeitem.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QAbstractGraphicsShapeItem::pen() const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractGraphicsShapeItem3penEv',
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QAbstractGraphicsShapeItem::brush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgraphicsshapeitem.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QAbstractGraphicsShapeItem::brush() const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractGraphicsShapeItem5brushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QAbstractGraphicsShapeItem::isObscuredBy(const
    QGraphicsItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgraphicsshapeitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractGraphicsShapeItem::isObscuredBy(const QGraphicsItem
    #      *item) const
    return self.uglySide.call(
        'ritual_ZNK26QAbstractGraphicsShapeItem12isObscuredByEPK13QGraphics'
        'Item',
        self._addressOf(item, 'QGraphicsItem'),
    )

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QAbstractGraphicsShapeItem::opaqueArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgraphicsshapeitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QAbstractGraphicsShapeItem::opaqueArea() const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractGraphicsShapeItem10opaqueAreaEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractGraphicsShapeItem::setPen(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgraphicsshapeitem.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractGraphicsShapeItem::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN26QAbstractGraphicsShapeItem6setPenERK4QPen',
        self._valueOf(pen),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAbstractGraphicsShapeItem::setBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgraphicsshapeitem.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAbstractGraphicsShapeItem::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN26QAbstractGraphicsShapeItem8setBrushERK6QBrush',
        self._valueOf(brush),
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
