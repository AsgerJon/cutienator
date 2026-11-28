"""
QListModeViewBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QListModeViewBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QAbstractItemView, QCommonListViewBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex, QPoint, QRect, QSize
  from ..QtGui import QDragMoveEvent
  from . import QListView, QListViewItem, QListViewLayoutInfo
  from . import QListViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QListView = WAIT['QListView']
  QListViewItem = WAIT['QListViewItem']
  QListViewLayoutInfo = WAIT['QListViewLayoutInfo']
  QListViewPrivate = WAIT['QListViewPrivate']
  QModelIndex = WAIT['QModelIndex']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QListModeViewBase(QCommonListViewBase):
  """
  The cute side of Qt's QListModeViewBase: a plain Python object standing in
  front of one C++ QListModeViewBase.

  It is built on the cute 'QCommonListViewBase', as Qt's QListModeViewBase is
  built on Qt's QCommonListViewBase, and has everything that class has.

  C++ hands a QListModeViewBase around as a copy, so every C++
  QListModeViewBase behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QListModeViewBase that has a ritual and that Python
  can call so far, 19 names in all: 'itemIndex', 'indexToListViewItem',
  'doBatchedItemLayout', 'clear', 'setRowCount', 'intersectingSet',
  'dataChanged', 'scrollContentsBy', 'mapToViewport', 'horizontalOffset',
  'verticalOffset', 'viewportSize', 'updateHorizontalScrollBar',
  'updateVerticalScrollBar', 'dragMoveEvent', 'initStaticLayout',
  'doStaticLayout', 'perItemScrollToValue', 'perItemScrollingPageSteps'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QListModeViewBase::horizontalScrollToValue(int index,
    QListView::ScrollHint hint, bool leftOf, bool rightOf, const QRect &area,
    const QRect &rect) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'int QListModeViewBase::verticalScrollToValue(int index,
    QListView::ScrollHint hint, bool above, bool below, const QRect &area,
    const QRect &rect) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QAbstractItemView::DropIndicatorPosition
    QListModeViewBase::position(const QPoint &pos, const QRect &rect, const
    QModelIndex &idx) const': gives the enum
    'QAbstractItemView::DropIndicatorPosition', whose class cannot be named
    here.
  - Qt's 'bool QListModeViewBase::dropOn(QDropEvent *event, int *row, int
    *col, QModelIndex *index)': takes a number to change where it is.
  - Qt's 'QListModeViewBase::~QListModeViewBase()': the destructor: Python
    removes its C++ QListModeViewBase by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QListModeViewBase is created at the first use, not by
    'QListModeViewBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QListModeViewBase back gives a copy the ritual made
    for Python, in a new cute QListModeViewBase.
  - Each name of Qt's QListModeViewBase that has no cute function yet,
    'dropOn', 'position', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAbstractItemView)
  @overload(NoneType)
  def viewportSize(v: Optional[QAbstractItemView]) -> QSize:
    """
    Calls Qt's 'QSize QListModeViewBase::viewportSize(const QAbstractItemView
    *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#viewportSize

    Parameters
    ----------

    v : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListModeViewBase::viewportSize(const QAbstractItemView *v)
    address = Rituals.call(
        'ritual_ZN17QListModeViewBase12viewportSizeEPK17QAbstractItemView',
        CuteMixin._addressOf(v),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QListModeViewBase'

  #  Qt's '~QListModeViewBase()'. Naming it makes this a value class: Python
  #  owns every C++ QListModeViewBase behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QListModeViewBaseD1Ev'

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
    Calls Qt's 'int QListModeViewBase::itemIndex(const QListViewItem &item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodeviewbase.html#itemIndex

    Parameters
    ----------

    item : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.
    """
    #  int QListModeViewBase::itemIndex(const QListViewItem &item) const
    ritual = 'ritual_ZNK17QListModeViewBase9itemIndexERK13QListViewItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QListModeViewBase9itemIndexERK13QListViewItem')
    return self.uglySide.call(ritual, self._valueOf(item))

  @overload(QModelIndex)
  def indexToListViewItem(self, index: QModelIndex) -> QListViewItem:
    """
    Calls Qt's 'QListViewItem QListModeViewBase::indexToListViewItem(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#indexToListViewItem

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
    #  QListViewItem QListModeViewBase::indexToListViewItem(const QModelIndex
    #      &index) const
    ritual = (
        'ritual_ZNK17QListModeViewBase19indexToListViewItemERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QListModeViewBase19indexToListViewItemERK11QMode'
          'lIndex')
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QListViewItem
    return QListViewItem._cuteOwning(address)

  @overload(QRect)
  def intersectingSet(self, area: QRect) -> QList[QModelIndex]:
    """
    Calls Qt's 'QList<QModelIndex> QListModeViewBase::intersectingSet(const
    QRect &area) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#intersectingSet

    Parameters
    ----------

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QModelIndex> QListModeViewBase::intersectingSet(const QRect
    #      &area) const
    address = self.uglySide.call(
        'ritual_ZNK17QListModeViewBase15intersectingSetERK5QRect',
        self._valueOf(area),
    )
    from ..QtCore import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  @overload(QRect)
  def mapToViewport(self, rect: QRect) -> QRect:
    """
    Calls Qt's 'QRect QListModeViewBase::mapToViewport(const QRect &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#mapToViewport

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListModeViewBase::mapToViewport(const QRect &rect) const
    ritual = 'ritual_ZNK17QListModeViewBase13mapToViewportERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QListModeViewBase13mapToViewportERK5QRect'
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QListModeViewBase::horizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#horizontalOffset
    """
    #  int QListModeViewBase::horizontalOffset() const
    ritual = 'ritual_ZNK17QListModeViewBase16horizontalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QListModeViewBase16horizontalOffsetEv'
    return self.uglySide.call(ritual)

  def verticalOffset(self) -> int:
    """
    Calls Qt's 'int QListModeViewBase::verticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#verticalOffset
    """
    #  int QListModeViewBase::verticalOffset() const
    ritual = 'ritual_ZNK17QListModeViewBase14verticalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QListModeViewBase14verticalOffsetEv'
    return self.uglySide.call(ritual)

  @overload(
      int, int, int, QAbstractItemView.ScrollHint, Qt.Orientation, bool, int,
  )
  def perItemScrollToValue(
      self,
      index: int,
      value: int,
      height: int,
      hint: QAbstractItemView.ScrollHint,
      orientation: Qt.Orientation,
      wrap: bool,
      extent: int,
  ) -> int:
    """
    Calls Qt's 'int QListModeViewBase::perItemScrollToValue(int index, int
    value, int height, QAbstractItemView::ScrollHint hint, Qt::Orientation
    orientation, bool wrap, int extent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#perItemScrollToValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : int
      Passed on as it is.

    height : int
      Passed on as it is.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.

    wrap : bool
      Passed on as it is.

    extent : int
      Passed on as it is.
    """
    #  int QListModeViewBase::perItemScrollToValue(int index, int value, int
    #      height, QAbstractItemView::ScrollHint hint, Qt::Orientation
    #      orientation, bool wrap, int extent) const
    return self.uglySide.call(
        'ritual_ZNK17QListModeViewBase20perItemScrollToValueEiiiN17QAbstrac'
        'tItemView10ScrollHintEN2Qt11OrientationEbi',
        index, value, height, hint.value, orientation.value, wrap, extent,
    )

  @overload(int, int, bool)
  def perItemScrollingPageSteps(
      self,
      length: int,
      bounds: int,
      wrap: bool,
  ) -> int:
    """
    Calls Qt's 'int QListModeViewBase::perItemScrollingPageSteps(int length,
    int bounds, bool wrap) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#perItemScrollingPageSteps

    Parameters
    ----------

    length : int
      Passed on as it is.

    bounds : int
      Passed on as it is.

    wrap : bool
      Passed on as it is.
    """
    #  int QListModeViewBase::perItemScrollingPageSteps(int length, int
    #      bounds, bool wrap) const
    return self.uglySide.call(
        'ritual_ZNK17QListModeViewBase25perItemScrollingPageStepsEiib',
        length, bounds, wrap,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRowCount(self, rowCount: int) -> None:
    """
    Calls Qt's 'void QListModeViewBase::setRowCount(int rowCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodeviewbase.html#setRowCount

    Parameters
    ----------

    rowCount : int
      Passed on as it is.
    """
    #  void QListModeViewBase::setRowCount(int rowCount)
    ritual = 'ritual_ZN17QListModeViewBase11setRowCountEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QListModeViewBase11setRowCountEi'
    self.uglySide.call(ritual, rowCount)

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
    'QListModeViewBase::QListModeViewBase(QListView *q, QListViewPrivate
    *d)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#QListModeViewBase

    Parameters
    ----------

    q : Optional[QListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : Optional[QListViewPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QListModeViewBase::QListModeViewBase(QListView *q, QListViewPrivate
    #      *d)
    self._noteCreation(QListModeViewBase, lambda: Rituals.call(
        'ritual_ZN17QListModeViewBaseC1EP9QListViewP16QListViewPrivate',
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
    Calls Qt's 'bool QListModeViewBase::doBatchedItemLayout(const
    QListViewLayoutInfo &info, int max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#doBatchedItemLayout

    Parameters
    ----------

    info : QListViewLayoutInfo
      Passed on as a value: Qt reads the C++ QListViewLayoutInfo, which stays
      Python's own.

    max : int
      Passed on as it is.
    """
    #  bool QListModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo
    #      &info, int max)
    ritual = (
        'ritual_ZN17QListModeViewBase19doBatchedItemLayoutERK19QListViewLay'
        'outInfoi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QListModeViewBase19doBatchedItemLayoutERK19QListV'
          'iewLayoutInfoi')
    return self.uglySide.call(ritual, self._valueOf(info), max)

  def clear(self) -> None:
    """
    Calls Qt's 'void QListModeViewBase::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodeviewbase.html#clear
    """
    #  void QListModeViewBase::clear()
    ritual = 'ritual_ZN17QListModeViewBase5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QListModeViewBase5clearEv'
    self.uglySide.call(ritual)

  @overload(QModelIndex, QModelIndex)
  def dataChanged(self, a0: QModelIndex, a1: QModelIndex) -> None:
    """
    Calls Qt's 'void QListModeViewBase::dataChanged(const QModelIndex &a0,
    const QModelIndex &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodeviewbase.html#dataChanged

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QListModeViewBase::dataChanged(const QModelIndex &a0, const
    #      QModelIndex &a1)
    ritual = 'ritual_ZN17QListModeViewBase11dataChangedERK11QModelIndexS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QListModeViewBase11dataChangedERK11QModelIndexS2_')
    self.uglySide.call(ritual, self._valueOf(a0), self._valueOf(a1))

  @overload(int, int, bool)
  def scrollContentsBy(
      self,
      dx: int,
      dy: int,
      scrollElasticBand: bool,
  ) -> None:
    """
    Calls Qt's 'void QListModeViewBase::scrollContentsBy(int dx, int dy, bool
    scrollElasticBand)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    scrollElasticBand : bool
      Passed on as it is.
    """
    #  void QListModeViewBase::scrollContentsBy(int dx, int dy, bool
    #      scrollElasticBand)
    ritual = 'ritual_ZN17QListModeViewBase16scrollContentsByEiib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QListModeViewBase16scrollContentsByEiib'
    self.uglySide.call(ritual, dx, dy, scrollElasticBand)

  @overload(QSize)
  def updateHorizontalScrollBar(self, step: QSize) -> None:
    """
    Calls Qt's 'void QListModeViewBase::updateHorizontalScrollBar(const QSize
    &step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#updateHorizontalScrollBar

    Parameters
    ----------

    step : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QListModeViewBase::updateHorizontalScrollBar(const QSize &step)
    ritual = (
        'ritual_ZN17QListModeViewBase25updateHorizontalScrollBarERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QListModeViewBase25updateHorizontalScrollBarERK5Q'
          'Size')
    self.uglySide.call(ritual, self._valueOf(step))

  @overload(QSize)
  def updateVerticalScrollBar(self, step: QSize) -> None:
    """
    Calls Qt's 'void QListModeViewBase::updateVerticalScrollBar(const QSize
    &step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#updateVerticalScrollBar

    Parameters
    ----------

    step : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QListModeViewBase::updateVerticalScrollBar(const QSize &step)
    ritual = 'ritual_ZN17QListModeViewBase23updateVerticalScrollBarERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QListModeViewBase23updateVerticalScrollBarERK5QSi'
          'ze')
    self.uglySide.call(ritual, self._valueOf(step))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, e: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QListModeViewBase::dragMoveEvent(QDragMoveEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#dragMoveEvent

    Parameters
    ----------

    e : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListModeViewBase::dragMoveEvent(QDragMoveEvent *e)
    self.uglySide.call(
        'ritual_ZN17QListModeViewBase13dragMoveEventEP14QDragMoveEvent',
        self._addressOf(e),
    )

  @overload(QListViewLayoutInfo)
  def initStaticLayout(self, info: QListViewLayoutInfo) -> QPoint:
    """
    Calls Qt's 'QPoint QListModeViewBase::initStaticLayout(const
    QListViewLayoutInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#initStaticLayout

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
    #  QPoint QListModeViewBase::initStaticLayout(const QListViewLayoutInfo
    #      &info)
    address = self.uglySide.call(
        'ritual_ZN17QListModeViewBase16initStaticLayoutERK19QListViewLayout'
        'Info',
        self._valueOf(info),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QListViewLayoutInfo)
  def doStaticLayout(self, info: QListViewLayoutInfo) -> None:
    """
    Calls Qt's 'void QListModeViewBase::doStaticLayout(const
    QListViewLayoutInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodeviewbase.html#doStaticLayout

    Parameters
    ----------

    info : QListViewLayoutInfo
      Passed on as a value: Qt reads the C++ QListViewLayoutInfo, which stays
      Python's own.
    """
    #  void QListModeViewBase::doStaticLayout(const QListViewLayoutInfo
    #      &info)
    self.uglySide.call(
        'ritual_ZN17QListModeViewBase14doStaticLayoutERK19QListViewLayoutIn'
        'fo',
        self._valueOf(info),
    )

  @staticmethod
  def dropOn(*__, **_) -> Never:
    """
    Qt's 'bool QListModeViewBase::dropOn(QDropEvent *event, int *row, int
    *col, QModelIndex *index)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QListModeViewBase.dropOn' has no cute function yet. Qt's 'bool "
        "QListModeViewBase::dropOn(QDropEvent *event, int *row, int *col, "
        "QModelIndex *index)': takes a number to change where it is.")

  @staticmethod
  def position(*__, **_) -> Never:
    """
    Qt's 'QAbstractItemView::DropIndicatorPosition
    QListModeViewBase::position(const QPoint &pos, const QRect &rect, const
    QModelIndex &idx) const': gives the enum
    'QAbstractItemView::DropIndicatorPosition', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QListModeViewBase.position' has no cute function yet. Qt's "
        "'QAbstractItemView::DropIndicatorPosition "
        "QListModeViewBase::position(const QPoint &pos, const QRect &rect, "
        "const QModelIndex &idx) const': gives the enum "
        "'QAbstractItemView::DropIndicatorPosition', whose class cannot be "
        "named here.")
