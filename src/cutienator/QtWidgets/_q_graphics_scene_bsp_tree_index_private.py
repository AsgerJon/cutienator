"""
QGraphicsSceneBspTreeIndexPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscenebsptreeindex_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGraphicsSceneBspTreeIndexPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QGraphicsSceneIndexPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGraphicsItem, QGraphicsScene, QGraphicsSceneBspTreeIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QGraphicsScene = WAIT['QGraphicsScene']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSceneBspTreeIndexPrivate(QGraphicsSceneIndexPrivate):
  """
  The cute side of Qt's QGraphicsSceneBspTreeIndexPrivate: a plain Python
  object standing in front of one C++ QGraphicsSceneBspTreeIndexPrivate.

  It is built on the cute 'QGraphicsSceneIndexPrivate', as Qt's
  QGraphicsSceneBspTreeIndexPrivate is built on Qt's
  QGraphicsSceneIndexPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneBspTreeIndexPrivate that has a ritual
  and that Python can call so far, 5 names in all: 'q_func',
  'purgeRemovedItems', 'invalidateSortCache', 'closestItemFirst_withCache',
  'closestItemLast_withCache'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsSceneBspTreeIndex
    *QGraphicsSceneBspTreeIndexPrivate::q_func() const': takes in Python what
    'QGraphicsSceneBspTreeIndex *QGraphicsSceneBspTreeIndexPrivate::q_func()'
    takes.
  - Qt's 'void QGraphicsSceneBspTreeIndexPrivate::climbTree(QGraphicsItem
    *item, int *stackingOrder)': takes a number to change where it is.
  - Qt's 'void
    QGraphicsSceneBspTreeIndexPrivate::sortItems(QList<QGraphicsItem *>
    *itemList, Qt::SortOrder order, bool cached, bool onlyTopLevelItems)':
    names 'QList<QGraphicsItem *>', which has no cute class yet.

  What has no ritual
  ------------------

  7 of the 16 functions Qt declares: 3 leans on
  'QGraphicsSceneBspTreeIndexPrivate; 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'void QGraphicsSceneBspTree.

  What to expect
  --------------

  - The C++ QGraphicsSceneBspTreeIndexPrivate is created at the first use,
    not by 'QGraphicsSceneBspTreeIndexPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneBspTreeIndexPrivate.
  - Each name of Qt's QGraphicsSceneBspTreeIndexPrivate that has no cute
    function yet, '_q_updateIndex', '_q_updateSortCache', 'addItem',
    'climbTree', 'estimateItems', 'removeItem', 'resetIndex', 'sortItems',
    'startIndexTimer', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGraphicsItem, QGraphicsItem)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def closestItemFirst_withCache(
      item1: Optional[QGraphicsItem],
      item2: Optional[QGraphicsItem],
  ) -> bool:
    """
    Calls Qt's 'bool
    QGraphicsSceneBspTreeIndexPrivate::closestItemFirst_withCache(const
    QGraphicsItem *item1, const QGraphicsItem *item2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindexprivate.html

    Parameters
    ----------

    item1 : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item2 : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsSceneBspTreeIndexPrivate::closestItemFirst_withCache(
    #      const QGraphicsItem *item1, const QGraphicsItem *item2)
    return Rituals.call(
        'ritual_ZN33QGraphicsSceneBspTreeIndexPrivate26closestItemFirst_wit'
        'hCacheEPK13QGraphicsItemS2_',
        CuteMixin._addressOf(item1, 'QGraphicsItem'),
        CuteMixin._addressOf(item2, 'QGraphicsItem'),
    )

  @staticmethod
  @overload(QGraphicsItem, QGraphicsItem)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def closestItemLast_withCache(
      item1: Optional[QGraphicsItem],
      item2: Optional[QGraphicsItem],
  ) -> bool:
    """
    Calls Qt's 'bool
    QGraphicsSceneBspTreeIndexPrivate::closestItemLast_withCache(const
    QGraphicsItem *item1, const QGraphicsItem *item2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindexprivate.html

    Parameters
    ----------

    item1 : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item2 : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      QGraphicsSceneBspTreeIndexPrivate::closestItemLast_withCache(const
    #      QGraphicsItem *item1, const QGraphicsItem *item2)
    return Rituals.call(
        'ritual_ZN33QGraphicsSceneBspTreeIndexPrivate25closestItemLast_with'
        'CacheEPK13QGraphicsItemS2_',
        CuteMixin._addressOf(item1, 'QGraphicsItem'),
        CuteMixin._addressOf(item2, 'QGraphicsItem'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneBspTreeIndexPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QGraphicsScene)
  @overload(NoneType)
  def __init__(self, scene: Optional[QGraphicsScene]) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsSceneBspTreeIndexPrivate::QGraphicsSceneBspTreeIndexPrivate(
    QGraphicsScene *scene)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindexprivate.html

    Parameters
    ----------

    scene : Optional[QGraphicsScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGraphicsSceneBspTreeIndexPrivate::
    #      QGraphicsSceneBspTreeIndexPrivate(QGraphicsScene *scene)
    self._noteCreation(
        QGraphicsSceneBspTreeIndexPrivate, lambda: Rituals.call(
            'ritual_ZN33QGraphicsSceneBspTreeIndexPrivateC1EP14QGraphicsSce'
            'ne',
            self._addressOf(scene),
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

  def q_func(self) -> Optional[QGraphicsSceneBspTreeIndex]:
    """
    Calls Qt's 'QGraphicsSceneBspTreeIndex
    *QGraphicsSceneBspTreeIndexPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindexprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsSceneBspTreeIndex]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsSceneBspTreeIndex
    #      *QGraphicsSceneBspTreeIndexPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN33QGraphicsSceneBspTreeIndexPrivate6q_funcEv',
    )
    from . import QGraphicsSceneBspTreeIndex
    return QGraphicsSceneBspTreeIndex._cuteAt(address)

  def purgeRemovedItems(self) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTreeIndexPrivate::purgeRemovedItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindexprivate.html
    """
    #  void QGraphicsSceneBspTreeIndexPrivate::purgeRemovedItems()
    self.uglySide.call(
        'ritual_ZN33QGraphicsSceneBspTreeIndexPrivate17purgeRemovedItemsEv',
    )

  def invalidateSortCache(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneBspTreeIndexPrivate::invalidateSortCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptreeindexprivate.html
    """
    #  void QGraphicsSceneBspTreeIndexPrivate::invalidateSortCache()
    self.uglySide.call(
        'ritual_ZN33QGraphicsSceneBspTreeIndexPrivate19invalidateSortCacheE'
        'v',
    )

  @staticmethod
  def _q_updateIndex(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndexPrivate::_q_updateIndex()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'intmaxlog'; did you
    mean 'intmax_t'?.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate._q_updateIndex' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::_q_updateIndex()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'intmaxlog'; did "
        "you mean 'intmax_t'?.")

  @staticmethod
  def _q_updateSortCache(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndexPrivate::_q_updateSortCache()':
    leans on 'void
    QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::insertItem(
    QGraphicsItem*, QRectF
    const&)::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree::
    insertItem(QGraphicsItem*, QRectF
    const&)::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate._q_updateSortCache' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::_q_updateSortCache()': leans on "
        "'void "
        "QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::insertItem("
        "QGraphicsItem*, QRectF "
        "const&)::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree:"
        ":insertItem(QGraphicsItem*, QRectF "
        "const&)::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def addItem(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndexPrivate::addItem(QGraphicsItem
    *item, bool recursive)': leans on
    'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate.addItem' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::addItem(QGraphicsItem *item, "
        "bool recursive)': leans on "
        "'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def climbTree(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndexPrivate::climbTree(QGraphicsItem
    *item, int *stackingOrder)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate.climbTree' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::climbTree(QGraphicsItem *item, "
        "int *stackingOrder)': takes a number to change where it is.")

  @staticmethod
  def estimateItems(*__, **_) -> Never:
    """
    Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneBspTreeIndexPrivate::estimateItems(const QRectF &a0,
    Qt::SortOrder a1, bool b)': leans on 'void
    QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::items(QRectF
    const&, bool)
    const::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree::items(
    QRectF const&, bool) const::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF
    const&, int) const', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate.estimateItems' has no cute "
        "function yet. Qt's 'QList<QGraphicsItem *> "
        "QGraphicsSceneBspTreeIndexPrivate::estimateItems(const QRectF &a0, "
        "Qt::SortOrder a1, bool b)': leans on 'void "
        "QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::items(QRect"
        "F const&, bool) "
        "const::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree::i"
        "tems(QRectF const&, bool) "
        "const::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def removeItem(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndexPrivate::removeItem(QGraphicsItem
    *item, bool recursive, bool moveToUnindexedItems)': leans on
    'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate.removeItem' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::removeItem(QGraphicsItem *item, "
        "bool recursive, bool moveToUnindexedItems)': leans on "
        "'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def resetIndex(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndexPrivate::resetIndex()': leans on
    'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate.resetIndex' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::resetIndex()': leans on "
        "'QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sortItems(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsSceneBspTreeIndexPrivate::sortItems(QList<QGraphicsItem *>
    *itemList, Qt::SortOrder order, bool cached, bool onlyTopLevelItems)':
    names 'QList<QGraphicsItem *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate.sortItems' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::sortItems(QList<QGraphicsItem "
        "*> *itemList, Qt::SortOrder order, bool cached, bool "
        "onlyTopLevelItems)': names 'QList<QGraphicsItem *>', which has no "
        "cute class yet.")

  @staticmethod
  def startIndexTimer(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int
    interval)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: no matching literal operator for
    call to 'operator""ms' with argument of type 'unsigned long long' or
    'const char *', and no matching literal operator template.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTreeIndexPrivate.startIndexTimer' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsSceneBspTreeIndexPrivate::startIndexTimer(int interval)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: no matching literal operator for "
        "call to 'operator\"\"ms' with argument of type 'unsigned long "
        "long' or 'const char *', and no matching literal operator template."
    )
