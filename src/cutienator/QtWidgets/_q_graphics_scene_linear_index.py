"""
QGraphicsSceneLinearIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscenelinearindex_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGraphicsSceneLinearIndex to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QList
from . import QGraphicsSceneIndex

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from . import QGraphicsItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSceneLinearIndex(QGraphicsSceneIndex):
  """
  The cute side of Qt's QGraphicsSceneLinearIndex: a plain Python object
  standing in front of one C++ QGraphicsSceneLinearIndex.

  It is built on the cute 'QGraphicsSceneIndex', as Qt's
  QGraphicsSceneLinearIndex is built on Qt's QGraphicsSceneIndex, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneLinearIndex that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'items',
  'estimateItems', 'clear', 'addItem', 'removeItem'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphicsSceneLinearIndex::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QGraphicsSceneLinearIndex::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 1 leans on
  'QGraphicsSceneLinearIndex; 1 leans on 'vtable for
  QGraphicsSceneLinearIndex', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QGraphicsSceneLinearIndex is created at the first use, not by
    'QGraphicsSceneLinearIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneLinearIndex.
  - Qt tells when it has removed the C++ QGraphicsSceneLinearIndex. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGraphicsSceneLinearIndex that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneLinearIndex'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsSceneLinearIndex::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenelinearindex.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsSceneLinearIndex::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsSceneLinearIndex10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(Qt.SortOrder)
  def items(
      self,
      order: Qt.SortOrder = Qt.SortOrder.DescendingOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneLinearIndex::items(Qt::SortOrder order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenelinearindex.html#items

    Parameters
    ----------

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.DescendingOrder.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneLinearIndex::items(Qt::SortOrder
    #      order) const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsSceneLinearIndex5itemsEN2Qt9SortOrderE',
        order.value,
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QRectF, Qt.SortOrder)
  def estimateItems(
      self,
      rect: QRectF,
      order: Qt.SortOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneLinearIndex::estimateItems(const QRectF &rect,
    Qt::SortOrder order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenelinearindex.html#estimateItems

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    order : Qt.SortOrder
      Passed on as its number.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneLinearIndex::estimateItems(const
    #      QRectF &rect, Qt::SortOrder order) const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsSceneLinearIndex13estimateItemsERK6QRectFN2Qt'
        '9SortOrderE',
        self._valueOf(rect), order.value,
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGraphicsSceneLinearIndex::QGraphicsSceneLinearIndex(QGraphicsScene
    *scene)': leans on 'vtable for QGraphicsSceneLinearIndex', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneLinearIndex.__init__' has no cute function yet. "
        "Qt's "
        "'QGraphicsSceneLinearIndex::QGraphicsSceneLinearIndex(QGraphicsScen"
        "e *scene)': leans on 'vtable for QGraphicsSceneLinearIndex', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def clear(self) -> None:
    """
    Calls Qt's 'void QGraphicsSceneLinearIndex::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenelinearindex.html#clear
    """
    #  void QGraphicsSceneLinearIndex::clear()
    ritual = 'ritual_ZN25QGraphicsSceneLinearIndex5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QGraphicsSceneLinearIndex5clearEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneLinearIndex::addItem(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenelinearindex.html#addItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneLinearIndex::addItem(QGraphicsItem *item)
    ritual = 'ritual_ZN25QGraphicsSceneLinearIndex7addItemEP13QGraphicsItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QGraphicsSceneLinearIndex7addItemEP13QGraphicsIte'
          'm')
    self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  @overload(QGraphicsItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneLinearIndex::removeItem(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenelinearindex.html#removeItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneLinearIndex::removeItem(QGraphicsItem *item)
    ritual = (
        'ritual_ZN25QGraphicsSceneLinearIndex10removeItemEP13QGraphicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QGraphicsSceneLinearIndex10removeItemEP13QGraphic'
          'sItem')
    self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))
