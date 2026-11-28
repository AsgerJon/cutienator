"""
QGraphicsSceneBspTreeIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscenebsptreeindex_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGraphicsSceneBspTreeIndex to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QList
from . import QGraphicsItem, QGraphicsSceneIndex

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from . import QGraphicsSceneBspTreeIndexPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSceneBspTreeIndex(QGraphicsSceneIndex):
  """
  The cute side of Qt's QGraphicsSceneBspTreeIndex: a plain Python object
  standing in front of one C++ QGraphicsSceneBspTreeIndex.

  It is built on the cute 'QGraphicsSceneIndex', as Qt's
  QGraphicsSceneBspTreeIndex is built on Qt's QGraphicsSceneIndex, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneBspTreeIndex that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject',
  'estimateItems', 'estimateTopLevelItems', 'items', 'bspTreeDepth',
  'updateSceneRect', 'event', 'clear', 'addItem', 'removeItem',
  'prepareBoundingRectChange', 'd_func'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphicsSceneBspTreeIndex::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QGraphicsSceneBspTreeIndex::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsSceneBspTreeIndex::~QGraphicsSceneBspTreeIndex()': the
    destructor: Python never removes a C++ QGraphicsSceneBspTreeIndex.
  - Qt's 'void QGraphicsSceneBspTreeIndex::itemChange(const QGraphicsItem
    *item, QGraphicsItem::GraphicsItemChange change, const void *const
    value)': takes a type Python has no way to hand over yet.
  - Qt's 'const QGraphicsSceneBspTreeIndexPrivate
    *QGraphicsSceneBspTreeIndex::d_func() const': takes in Python what
    'QGraphicsSceneBspTreeIndexPrivate *QGraphicsSceneBspTreeIndex::d_func()'
    takes.

  What has no ritual
  ------------------

  9 of the 26 functions Qt declares: 4 forbidden; 2 not a gap; 2 leans on
  'QGraphicsSceneBspTreeIndex; 1 leans on 'QGraphicsSceneBspTreeIndexPrivate.

  What to expect
  --------------

  - The C++ QGraphicsSceneBspTreeIndex is created at the first use, not by
    'QGraphicsSceneBspTreeIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneBspTreeIndex.
  - Qt tells when it has removed the C++ QGraphicsSceneBspTreeIndex. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGraphicsSceneBspTreeIndex that has no cute function
    yet, '__init__', 'setBspTreeDepth', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneBspTreeIndex'

  #  A C++ QGraphicsSceneBspTreeIndex Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneBspTreeIndex'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsSceneBspTreeIndex::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsSceneBspTreeIndex::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QGraphicsSceneBspTreeIndex10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QRectF, Qt.SortOrder)
  def estimateItems(
      self,
      rect: QRectF,
      order: Qt.SortOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneBspTreeIndex::estimateItems(const QRectF &rect,
    Qt::SortOrder order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#estimateItems

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
    #  QList<QGraphicsItem *> QGraphicsSceneBspTreeIndex::estimateItems(const
    #      QRectF &rect, Qt::SortOrder order) const
    address = self.uglySide.call(
        'ritual_ZNK26QGraphicsSceneBspTreeIndex13estimateItemsERK6QRectFN2Q'
        't9SortOrderE',
        self._valueOf(rect), order.value,
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QRectF, Qt.SortOrder)
  def estimateTopLevelItems(
      self,
      rect: QRectF,
      order: Qt.SortOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneBspTreeIndex::estimateTopLevelItems(const QRectF &rect,
    Qt::SortOrder order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html

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
    #  QList<QGraphicsItem *>
    #      QGraphicsSceneBspTreeIndex::estimateTopLevelItems(const QRectF
    #      &rect, Qt::SortOrder order) const
    address = self.uglySide.call(
        'ritual_ZNK26QGraphicsSceneBspTreeIndex21estimateTopLevelItemsERK6Q'
        'RectFN2Qt9SortOrderE',
        self._valueOf(rect), order.value,
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload()
  @overload(Qt.SortOrder)
  def items(
      self,
      order: Qt.SortOrder = Qt.SortOrder.DescendingOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneBspTreeIndex::items(Qt::SortOrder order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#items

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
    #  QList<QGraphicsItem *> QGraphicsSceneBspTreeIndex::items(Qt::SortOrder
    #      order) const
    address = self.uglySide.call(
        'ritual_ZNK26QGraphicsSceneBspTreeIndex5itemsEN2Qt9SortOrderE',
        order.value,
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  def bspTreeDepth(self) -> int:
    """
    Calls Qt's 'int QGraphicsSceneBspTreeIndex::bspTreeDepth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#bspTreeDepth
    """
    #  int QGraphicsSceneBspTreeIndex::bspTreeDepth() const
    return self.uglySide.call(
        'ritual_ZNK26QGraphicsSceneBspTreeIndex12bspTreeDepthEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QGraphicsSceneBspTreeIndex::QGraphicsSceneBspTreeIndex(QGraphicsScene
    *scene)': leans on
    'QGraphicsSceneBspTreeIndex::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndex.__init__' has no cute function yet. "
        "Qt's "
        "'QGraphicsSceneBspTreeIndex::QGraphicsSceneBspTreeIndex(QGraphicsSc"
        "ene *scene)': leans on "
        "'QGraphicsSceneBspTreeIndex::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QRectF)
  def updateSceneRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTreeIndex::updateSceneRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#updateSceneRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsSceneBspTreeIndex::updateSceneRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN26QGraphicsSceneBspTreeIndex15updateSceneRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsSceneBspTreeIndex::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsSceneBspTreeIndex::event(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN26QGraphicsSceneBspTreeIndex5eventEP6QEvent',
        self._addressOf(event),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTreeIndex::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#clear
    """
    #  void QGraphicsSceneBspTreeIndex::clear()
    ritual = 'ritual_ZN26QGraphicsSceneBspTreeIndex5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QGraphicsSceneBspTreeIndex5clearEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTreeIndex::addItem(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#addItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneBspTreeIndex::addItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN26QGraphicsSceneBspTreeIndex7addItemEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTreeIndex::removeItem(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#removeItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneBspTreeIndex::removeItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN26QGraphicsSceneBspTreeIndex10removeItemEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def prepareBoundingRectChange(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneBspTreeIndex::prepareBoundingRectChange(const QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneBspTreeIndex::prepareBoundingRectChange(const
    #      QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN26QGraphicsSceneBspTreeIndex25prepareBoundingRectChangeEP'
        'K13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  def d_func(self) -> Optional[QGraphicsSceneBspTreeIndexPrivate]:
    """
    Calls Qt's 'QGraphicsSceneBspTreeIndexPrivate
    *QGraphicsSceneBspTreeIndex::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindex.html#d_func

    Returns
    -------

    Optional[QGraphicsSceneBspTreeIndexPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsSceneBspTreeIndexPrivate
    #      *QGraphicsSceneBspTreeIndex::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QGraphicsSceneBspTreeIndex6d_funcEv',
    )
    from . import QGraphicsSceneBspTreeIndexPrivate
    return QGraphicsSceneBspTreeIndexPrivate._cuteAt(address)

  @staticmethod
  def setBspTreeDepth(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndex::setBspTreeDepth(int depth)': leans
    on 'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndex.setBspTreeDepth' has no cute function "
        "yet. Qt's 'void QGraphicsSceneBspTreeIndex::setBspTreeDepth(int "
        "depth)': leans on "
        "'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
