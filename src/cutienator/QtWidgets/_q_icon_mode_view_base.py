"""
QIconModeViewBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QIconModeViewBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QCommonListViewBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex, QPoint, QRect, QSize
  from ..QtGui import QDragLeaveEvent, QDragMoveEvent, QDropEvent
  from . import QListView, QListViewItem, QListViewLayoutInfo
  from . import QListViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QListView = WAIT['QListView']
  QListViewItem = WAIT['QListViewItem']
  QListViewLayoutInfo = WAIT['QListViewLayoutInfo']
  QListViewPrivate = WAIT['QListViewPrivate']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIconModeViewBase(QCommonListViewBase):
  """
  The cute side of Qt's QIconModeViewBase: a plain Python object standing in
  front of one C++ QIconModeViewBase.

  It is built on the cute 'QCommonListViewBase', as Qt's QIconModeViewBase is
  built on Qt's QCommonListViewBase, and has everything that class has.

  C++ hands a QIconModeViewBase around as a copy, so every C++
  QIconModeViewBase behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QIconModeViewBase that has a ritual and that Python
  can call so far, 24 names in all: 'itemIndex', 'indexToListViewItem',
  'doBatchedItemLayout', 'clear', 'setRowCount', 'intersectingSet',
  'scrollContentsBy', 'dataChanged', 'appendHiddenRow', 'removeHiddenRow',
  'setPositionForIndex', 'filterDragMoveEvent', 'filterDragLeaveEvent',
  'filterDropEvent', 'filterStartDrag', 'initBspTree', 'initDynamicLayout',
  'doDynamicLayout', 'itemsRect', 'draggedItemsRect', 'snapToGrid',
  'updateContentsSize', 'draggedItemsDelta', 'moveItem'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QIconModeViewBase::addLeaf(QList<int> &leaf, const QRect
    &area, uint visited, QBspTree::Data data)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QIconModeViewBase::~QIconModeViewBase()': the destructor: Python
    removes its C++ QIconModeViewBase by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 28 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QIconModeViewBase is created at the first use, not by
    'QIconModeViewBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QIconModeViewBase back gives a copy the ritual made
    for Python, in a new cute QIconModeViewBase.
  - Each name of Qt's QIconModeViewBase that has no cute function yet,
    'addLeaf', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconModeViewBase'

  #  Qt's '~QIconModeViewBase()'. Naming it makes this a value class: Python
  #  owns every C++ QIconModeViewBase behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QIconModeViewBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QListViewItem)
  def itemIndex(self, item: QListViewItem) -> int:
    """
    Calls Qt's 'int QIconModeViewBase::itemIndex(const QListViewItem &item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#itemIndex

    Parameters
    ----------

    item : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.
    """
    #  int QIconModeViewBase::itemIndex(const QListViewItem &item) const
    ritual = 'ritual_ZNK17QIconModeViewBase9itemIndexERK13QListViewItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QIconModeViewBase9itemIndexERK13QListViewItem')
    return self.uglySide.call(ritual, self._valueOf(item))

  @overload(QModelIndex)
  def indexToListViewItem(self, index: QModelIndex) -> QListViewItem:
    """
    Calls Qt's 'QListViewItem QIconModeViewBase::indexToListViewItem(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#indexToListViewItem

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QListViewItem
      A new cute QListViewItem around the copy Qt gave back. Python owns it.
    """
    #  QListViewItem QIconModeViewBase::indexToListViewItem(const QModelIndex
    #      &index) const
    ritual = (
        'ritual_ZNK17QIconModeViewBase19indexToListViewItemERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QIconModeViewBase19indexToListViewItemERK11QMode'
          'lIndex')
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QListViewItem
    return QListViewItem._cuteOwning(address)

  @overload(QRect)
  def intersectingSet(self, area: QRect) -> QList[QModelIndex]:
    """
    Calls Qt's 'QList<QModelIndex> QIconModeViewBase::intersectingSet(const
    QRect &area) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#intersectingSet

    Parameters
    ----------

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QModelIndex> QIconModeViewBase::intersectingSet(const QRect
    #      &area) const
    address = self.uglySide.call(
        'ritual_ZNK17QIconModeViewBase15intersectingSetERK5QRect',
        self._valueOf(area),
    )
    from ..QtCore import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  @overload(QList[QModelIndex])
  def itemsRect(self, indexes: QList[QModelIndex]) -> QRect:
    """
    Calls Qt's 'QRect QIconModeViewBase::itemsRect(const QList<QModelIndex>
    &indexes) const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#itemsRect

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QIconModeViewBase::itemsRect(const QList<QModelIndex> &indexes)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QIconModeViewBase9itemsRectERK5QListI11QModelIndexE',
        self._valueOf(indexes),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def draggedItemsRect(self) -> QRect:
    """
    Calls Qt's 'QRect QIconModeViewBase::draggedItemsRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#draggedItemsRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QIconModeViewBase::draggedItemsRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QIconModeViewBase16draggedItemsRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def snapToGrid(self, pos: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QIconModeViewBase::snapToGrid(const QPoint &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#snapToGrid

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QIconModeViewBase::snapToGrid(const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK17QIconModeViewBase10snapToGridERK6QPoint',
        self._valueOf(pos),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def draggedItemsDelta(self) -> QPoint:
    """
    Calls Qt's 'QPoint QIconModeViewBase::draggedItemsDelta() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#draggedItemsDelta

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QIconModeViewBase::draggedItemsDelta() const
    address = self.uglySide.call(
        'ritual_ZNK17QIconModeViewBase17draggedItemsDeltaEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRowCount(self, rowCount: int) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::setRowCount(int rowCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#setRowCount

    Parameters
    ----------

    rowCount : int
      Passed on as it is.
    """
    #  void QIconModeViewBase::setRowCount(int rowCount)
    ritual = 'ritual_ZN17QIconModeViewBase11setRowCountEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QIconModeViewBase11setRowCountEi'
    self.uglySide.call(ritual, rowCount)

  @overload(QPoint, QModelIndex)
  def setPositionForIndex(
      self,
      position: QPoint,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::setPositionForIndex(const QPoint
    &position, const QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#setPositionForIndex

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QIconModeViewBase::setPositionForIndex(const QPoint &position,
    #      const QModelIndex &index)
    ritual = (
        'ritual_ZN17QIconModeViewBase19setPositionForIndexERK6QPointRK11QMo'
        'delIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconModeViewBase19setPositionForIndexERK6QPointR'
          'K11QModelIndex')
    self.uglySide.call(ritual, self._valueOf(position), self._valueOf(index))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QListView, QListViewPrivate)
  @overload(QListView, NoneType)
  @overload(NoneType, QListViewPrivate)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QListView],
      d: Optional[QListViewPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QIconModeViewBase::QIconModeViewBase(QListView *q, QListViewPrivate
    *d)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#QIconModeViewBase

    Parameters
    ----------

    q : Optional[QListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : Optional[QListViewPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QIconModeViewBase::QIconModeViewBase(QListView *q, QListViewPrivate
    #      *d)
    self._noteCreation(QIconModeViewBase, lambda: Rituals.call(
        'ritual_ZN17QIconModeViewBaseC1EP9QListViewP16QListViewPrivate',
        self._addressOf(q), self._addressOf(d),
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

  @overload(QListViewLayoutInfo, int)
  def doBatchedItemLayout(self, info: QListViewLayoutInfo, max: int) -> bool:
    """
    Calls Qt's 'bool QIconModeViewBase::doBatchedItemLayout(const
    QListViewLayoutInfo &info, int max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#doBatchedItemLayout

    Parameters
    ----------

    info : QListViewLayoutInfo
      Passed on as a value: Qt reads the C++ QListViewLayoutInfo, which stays
      Python's own.

    max : int
      Passed on as it is.
    """
    #  bool QIconModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo
    #      &info, int max)
    ritual = (
        'ritual_ZN17QIconModeViewBase19doBatchedItemLayoutERK19QListViewLay'
        'outInfoi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconModeViewBase19doBatchedItemLayoutERK19QListV'
          'iewLayoutInfoi')
    return self.uglySide.call(ritual, self._valueOf(info), max)

  def clear(self) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#clear
    """
    #  void QIconModeViewBase::clear()
    ritual = 'ritual_ZN17QIconModeViewBase5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QIconModeViewBase5clearEv'
    self.uglySide.call(ritual)

  @overload(int, int, bool)
  def scrollContentsBy(
      self,
      dx: int,
      dy: int,
      scrollElasticBand: bool,
  ) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::scrollContentsBy(int dx, int dy, bool
    scrollElasticBand)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    scrollElasticBand : bool
      Passed on as it is.
    """
    #  void QIconModeViewBase::scrollContentsBy(int dx, int dy, bool
    #      scrollElasticBand)
    ritual = 'ritual_ZN17QIconModeViewBase16scrollContentsByEiib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QIconModeViewBase16scrollContentsByEiib'
    self.uglySide.call(ritual, dx, dy, scrollElasticBand)

  @overload(QModelIndex, QModelIndex)
  def dataChanged(
      self,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::dataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#dataChanged

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QIconModeViewBase::dataChanged(const QModelIndex &topLeft, const
    #      QModelIndex &bottomRight)
    ritual = 'ritual_ZN17QIconModeViewBase11dataChangedERK11QModelIndexS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconModeViewBase11dataChangedERK11QModelIndexS2_')
    self.uglySide.call(
        ritual, self._valueOf(topLeft), self._valueOf(bottomRight),
    )

  @overload(int)
  def appendHiddenRow(self, row: int) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::appendHiddenRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#appendHiddenRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QIconModeViewBase::appendHiddenRow(int row)
    ritual = 'ritual_ZN17QIconModeViewBase15appendHiddenRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QIconModeViewBase15appendHiddenRowEi'
    self.uglySide.call(ritual, row)

  @overload(int)
  def removeHiddenRow(self, row: int) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::removeHiddenRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#removeHiddenRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QIconModeViewBase::removeHiddenRow(int row)
    ritual = 'ritual_ZN17QIconModeViewBase15removeHiddenRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QIconModeViewBase15removeHiddenRowEi'
    self.uglySide.call(ritual, row)

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def filterDragMoveEvent(self, a0: Optional[QDragMoveEvent]) -> bool:
    """
    Calls Qt's 'bool QIconModeViewBase::filterDragMoveEvent(QDragMoveEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#filterDragMoveEvent

    Parameters
    ----------

    a0 : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QIconModeViewBase::filterDragMoveEvent(QDragMoveEvent *a0)
    ritual = (
        'ritual_ZN17QIconModeViewBase19filterDragMoveEventEP14QDragMoveEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconModeViewBase19filterDragMoveEventEP14QDragMo'
          'veEvent')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def filterDragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) -> bool:
    """
    Calls Qt's 'bool QIconModeViewBase::filterDragLeaveEvent(QDragLeaveEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#filterDragLeaveEvent

    Parameters
    ----------

    a0 : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QIconModeViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)
    ritual = (
        'ritual_ZN17QIconModeViewBase20filterDragLeaveEventEP15QDragLeaveEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconModeViewBase20filterDragLeaveEventEP15QDragL'
          'eaveEvent')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDropEvent)
  @overload(NoneType)
  def filterDropEvent(self, e: Optional[QDropEvent]) -> bool:
    """
    Calls Qt's 'bool QIconModeViewBase::filterDropEvent(QDropEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#filterDropEvent

    Parameters
    ----------

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QIconModeViewBase::filterDropEvent(QDropEvent *e)
    ritual = 'ritual_ZN17QIconModeViewBase15filterDropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconModeViewBase15filterDropEventEP10QDropEvent')
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(Qt.DropActions)
  def filterStartDrag(self, a0: Qt.DropActions) -> bool:
    """
    Calls Qt's 'bool QIconModeViewBase::filterStartDrag(Qt::DropActions a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#filterStartDrag

    Parameters
    ----------

    a0 : Qt.DropActions
      Passed on as its number.
    """
    #  bool QIconModeViewBase::filterStartDrag(Qt::DropActions a0)
    ritual = (
        'ritual_ZN17QIconModeViewBase15filterStartDragE6QFlagsIN2Qt10DropAc'
        'tionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QIconModeViewBase15filterStartDragE6QFlagsIN2Qt10'
          'DropActionEE')
    return self.uglySide.call(ritual, a0.value)

  @overload(QSize)
  def initBspTree(self, contents: QSize) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::initBspTree(const QSize &contents)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#initBspTree

    Parameters
    ----------

    contents : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QIconModeViewBase::initBspTree(const QSize &contents)
    self.uglySide.call(
        'ritual_ZN17QIconModeViewBase11initBspTreeERK5QSize',
        self._valueOf(contents),
    )

  @overload(QListViewLayoutInfo)
  def initDynamicLayout(self, info: QListViewLayoutInfo) -> QPoint:
    """
    Calls Qt's 'QPoint QIconModeViewBase::initDynamicLayout(const
    QListViewLayoutInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#initDynamicLayout

    Parameters
    ----------

    info : QListViewLayoutInfo
      Passed on as a value: Qt reads the C++ QListViewLayoutInfo, which stays
      Python's own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QIconModeViewBase::initDynamicLayout(const QListViewLayoutInfo
    #      &info)
    address = self.uglySide.call(
        'ritual_ZN17QIconModeViewBase17initDynamicLayoutERK19QListViewLayou'
        'tInfo',
        self._valueOf(info),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QListViewLayoutInfo)
  def doDynamicLayout(self, info: QListViewLayoutInfo) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::doDynamicLayout(const
    QListViewLayoutInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#doDynamicLayout

    Parameters
    ----------

    info : QListViewLayoutInfo
      Passed on as a value: Qt reads the C++ QListViewLayoutInfo, which stays
      Python's own.
    """
    #  void QIconModeViewBase::doDynamicLayout(const QListViewLayoutInfo
    #      &info)
    self.uglySide.call(
        'ritual_ZN17QIconModeViewBase15doDynamicLayoutERK19QListViewLayoutI'
        'nfo',
        self._valueOf(info),
    )

  def updateContentsSize(self) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::updateContentsSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconmodeviewbase.html#updateContentsSize
    """
    #  void QIconModeViewBase::updateContentsSize()
    self.uglySide.call('ritual_ZN17QIconModeViewBase18updateContentsSizeEv')

  @overload(int, QPoint)
  def moveItem(self, index: int, dest: QPoint) -> None:
    """
    Calls Qt's 'void QIconModeViewBase::moveItem(int index, const QPoint
    &dest)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconmodeviewbase.html#moveItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    dest : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QIconModeViewBase::moveItem(int index, const QPoint &dest)
    self.uglySide.call(
        'ritual_ZN17QIconModeViewBase8moveItemEiRK6QPoint',
        index, self._valueOf(dest),
    )

  @staticmethod
  def addLeaf(*__, **_) -> Never:
    """
    Qt's 'void QIconModeViewBase::addLeaf(QList<int> &leaf, const QRect
    &area, uint visited, QBspTree::Data data)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QIconModeViewBase.addLeaf' has no cute function yet. Qt's 'void "
        "QIconModeViewBase::addLeaf(QList<int> &leaf, const QRect &area, "
        "uint visited, QBspTree::Data data)': takes a type Python has no "
        "way to hand over yet.")
