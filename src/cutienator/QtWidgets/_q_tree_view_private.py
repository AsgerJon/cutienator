"""
QTreeViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtreeview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTreeViewPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractAnimation, QItemSelectionModel, QList
from ..QtCore import QVariantAnimation
from . import QAbstractItemViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex, QPersistentModelIndex, QPoint, QRect
  from ..QtCore import QVariant
  from ..QtGui import QPainter, QPixmap
  from . import QItemViewPaintPair, QStyleOptionViewItem, QTreeView
  from . import QTreeViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QTreeViewItem = WAIT['QTreeViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeViewPrivate(QAbstractItemViewPrivate):
  """
  The cute side of Qt's QTreeViewPrivate: a plain Python object standing in
  front of one C++ QTreeViewPrivate.

  It is built on the cute 'QAbstractItemViewPrivate', as Qt's
  QTreeViewPrivate is built on Qt's QAbstractItemViewPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QTreeViewPrivate that has a ritual and that Python
  can call so far, 55 names in all: 'q_func', 'initialize',
  'clearConnections', 'logicalIndexForTree', 'isTreePosition',
  'draggablePaintPairs', 'adjustViewOptionsForIndex',
  'beginAnimatedOperation', 'drawAnimatedOperation',
  'renderTreeToPixmapForAnimation', 'endAnimatedOperation', 'expand',
  'collapse', 'columnsAboutToBeRemoved', 'columnsRemoved',
  'modelAboutToBeReset', 'sortIndicatorChanged', 'modelDestroyed',
  'intersectedRect', 'layout', 'doItemsLayout', 'pageUp', 'pageDown',
  'itemForKeyHome', 'itemForKeyEnd', 'itemHeight', 'indentationForItem',
  'coordinateForItem', 'itemAtCoordinate', 'viewIndex', 'modelIndex',
  'insertViewItems', 'removeViewItems', 'lastVisibleItem', 'columnAt',
  'hasVisibleChildren', 'expandOrCollapseItemAtPos', 'updateScrollBars',
  'itemDecorationAt', 'itemDecorationRect', 'select',
  'paintAlternatingRowColors', 'widthHintForIndex', 'visualRect',
  'storeExpanded', 'isIndexExpanded', 'isRowHidden',
  'isItemHiddenOrDisabled', 'above', 'below', 'invalidateHeightCache',
  'accessibleTable2Index', 'accessibleChildIndex',
  'updateIndentationFromStyle', 'updateAccessibility'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTreeView *QTreeViewPrivate::q_func() const': takes in Python
    what 'QTreeView *QTreeViewPrivate::q_func()' takes.
  - Qt's 'QTreeViewPrivate::~QTreeViewPrivate()': the destructor: Python
    never removes a C++ QTreeViewPrivate.
  - Qt's 'void QTreeViewPrivate::prepareAnimatedOperation(int item,
    QVariantAnimation::Direction d)': takes a type Python has no way to hand
    over yet.
  - Qt's 'int QTreeViewPrivate::firstVisibleItem(int *offset) const': takes a
    number to change where it is.
  - Qt's 'QList<std::pair<int, int>> QTreeViewPrivate::columnRanges(const
    QModelIndex &topIndex, const QModelIndex &bottomIndex) const': gives a
    type Python has no way to take yet.
  - Qt's 'std::pair<int, int> QTreeViewPrivate::startAndEndColumns(const
    QRect &rect) const': gives a type Python has no way to take yet.
  - Qt's 'void QTreeViewPrivate::calcLogicalIndices(QList<int>
    *logicalIndices, QList<QStyleOptionViewItem::ViewItemPosition>
    *itemPositions, int left, int right) const': names 'QList<int>', which
    has no cute class yet.

  What has no ritual
  ------------------

  2 of the 65 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 leans on
  'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QTreeViewPrivate is created at the first use, not by
    'QTreeViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTreeViewPrivate.
  - Each name of Qt's QTreeViewPrivate that has no cute function yet,
    '__init__', 'calcLogicalIndices', 'columnRanges', 'firstVisibleItem',
    'prepareAnimatedOperation', 'startAndEndColumns', 'updateChildCount',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QTreeViewPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ExpandItems(CuteNum, scoped=True):
    """
    The enum 'QTreeViewPrivate::ExpandItems' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    AllLevels = Kee[int](0)
    RootOnly = Kee[int](1)

  class InitializeNewItems(CuteNum, scoped=True):
    """
    The enum 'QTreeViewPrivate::InitializeNewItems' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Initialize = Kee[int](0)
    DontInitialize = Kee[int](1)

  class RectRule(CuteNum):
    """
    The enum 'QTreeViewPrivate::RectRule' of Qt, with the 3 names Qt gives in
    it.
    """

    FullRow = Kee[int](0)
    SingleSection = Kee[int](1)
    AddRowIndicatorToFirstSection = Kee[int](2)

  #  The classes Qt writes inside QTreeViewPrivate, each a class in here as
  #  in C++.

  class AnimatedOperation(QVariantAnimation):
    """
    The cute side of Qt's QTreeViewPrivate::AnimatedOperation: a plain Python
    object standing in front of one C++ QTreeViewPrivate::AnimatedOperation.

    It is built on the cute 'QVariantAnimation', as Qt's
    QTreeViewPrivate::AnimatedOperation is built on Qt's QVariantAnimation,
    and has everything that class has.

    What exists
    -----------

    Every function of Qt's QTreeViewPrivate::AnimatedOperation that has a
    ritual and that Python can call so far, 4 names in all: 'top', 'rect',
    'updateCurrentValue', 'updateState'. It can be made from Python, in 1
    way; see '__init__'.

    What to expect
    --------------

    - The C++ QTreeViewPrivate::AnimatedOperation is created at the first
      use, not by 'QTreeViewPrivate::AnimatedOperation(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QTreeViewPrivate::AnimatedOperation.
    - Qt tells when it has removed the C++
      QTreeViewPrivate::AnimatedOperation. Every call on the cute object, and
      every use of it as an argument, then raises 'RuntimeError', and nothing
      reaches C++.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTreeViewPrivate::AnimatedOperation'

    #  A C++ QTreeViewPrivate::AnimatedOperation Python makes is of a C++
    #  class of ours, in which Python can take functions over. This ritual
    #  hands one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QTreeViewPrivate_AnimatedOperation'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def top(self) -> int:
      """
      Calls Qt's 'int QTreeViewPrivate::AnimatedOperation::top() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtreeviewprivate-animatedoperation.html#top
      """
      #  int QTreeViewPrivate::AnimatedOperation::top() const
      return self.uglySide.call(
          'ritual_ZNK16QTreeViewPrivate17AnimatedOperation3topEv',
      )

    def rect(self) -> QRect:
      """
      Calls Qt's 'QRect QTreeViewPrivate::AnimatedOperation::rect() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtreeviewprivate-animatedoperation.html#rect

      Returns
      -------

      QRect
        A new cute QRect around the copy Qt gave back. Python owns it.
      """
      #  QRect QTreeViewPrivate::AnimatedOperation::rect() const
      address = self.uglySide.call(
          'ritual_ZNK16QTreeViewPrivate17AnimatedOperation4rectEv',
      )
      from ..QtCore import QRect
      return QRect._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QTreeViewPrivate::AnimatedOperation::AnimatedOperation()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtreeviewprivate-animatedoperation.html
      """
      #  QTreeViewPrivate::AnimatedOperation::AnimatedOperation()
      self._noteCreation(
          QTreeViewPrivate.AnimatedOperation, lambda: Rituals.call(
              'ritual_ZN16QTreeViewPrivate17AnimatedOperationC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QVariant)
    def updateCurrentValue(self, a0: QVariant) -> None:
      """
      Calls Qt's 'void
      QTreeViewPrivate::AnimatedOperation::updateCurrentValue(const QVariant
      &a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtreeviewprivate-animatedoperation.html

      Parameters
      ----------

      a0 : QVariant
        Passed on as a value: Qt reads the C++ QVariant, which stays Python's
        own.
      """
      #  void QTreeViewPrivate::AnimatedOperation::updateCurrentValue(const
      #      QVariant &a0)
      ritual = (
          'ritual_ZN16QTreeViewPrivate17AnimatedOperation18updateCurrentVal'
          'ueERK8QVariant')
      if self.uglySide.isOurs():
        ritual = (
            'ritual_own_ZN16QTreeViewPrivate17AnimatedOperation18updateCurr'
            'entValueERK8QVariant')
      self.uglySide.call(ritual, self._valueOf(a0))

    @overload(QAbstractAnimation.State, QAbstractAnimation.State)
    def updateState(
        self,
        state: QAbstractAnimation.State,
        a1: QAbstractAnimation.State,
    ) -> None:
      """
      Calls Qt's 'void QTreeViewPrivate::AnimatedOperation::updateState(State
      state, State a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtreeviewprivate-animatedoperation.html

      Parameters
      ----------

      state : QAbstractAnimation.State
        Passed on as its number.

      a1 : QAbstractAnimation.State
        Passed on as its number.
      """
      #  void QTreeViewPrivate::AnimatedOperation::updateState(State state,
      #      State a1)
      ritual = (
          'ritual_ZN16QTreeViewPrivate17AnimatedOperation11updateStateEN18Q'
          'AbstractAnimation5StateES2_')
      if self.uglySide.isOurs():
        ritual = (
            'ritual_own_ZN16QTreeViewPrivate17AnimatedOperation11updateStat'
            'eEN18QAbstractAnimation5StateES2_')
      self.uglySide.call(ritual, state.value, a1.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeViewPrivate'

  #  A C++ QTreeViewPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTreeViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def logicalIndexForTree(self) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::logicalIndexForTree() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#logicalIndexForTree
    """
    #  int QTreeViewPrivate::logicalIndexForTree() const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate19logicalIndexForTreeEv',
    )

  @overload(int)
  def isTreePosition(self, logicalIndex: int) -> bool:
    """
    Calls Qt's 'bool QTreeViewPrivate::isTreePosition(int logicalIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#isTreePosition

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  bool QTreeViewPrivate::isTreePosition(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate14isTreePositionEi', logicalIndex,
    )

  @overload(QList[QModelIndex], QRect)
  @overload(QList[QModelIndex], NoneType)
  def draggablePaintPairs(
      self,
      indexes: QList[QModelIndex],
      r: Optional[QRect],
  ) -> QList[QItemViewPaintPair]:
    """
    Calls Qt's 'QItemViewPaintPairs
    QTreeViewPrivate::draggablePaintPairs(const QModelIndexList &indexes,
    QRect *r) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#draggablePaintPairs

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    r : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QItemViewPaintPair]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QItemViewPaintPairs QTreeViewPrivate::draggablePaintPairs(const
    #      QModelIndexList &indexes, QRect *r) const
    address = self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate19draggablePaintPairsERK5QListI11QMode'
        'lIndexEP5QRect',
        self._valueOf(indexes), self._addressOf(r),
    )
    from . import QItemViewPaintPair
    return QList[QItemViewPaintPair]._cuteOwning(address)

  @overload(QRect)
  def renderTreeToPixmapForAnimation(self, rect: QRect) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    QTreeViewPrivate::renderTreeToPixmapForAnimation(const QRect &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QTreeViewPrivate::renderTreeToPixmapForAnimation(const QRect
    #      &rect) const
    address = self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate30renderTreeToPixmapForAnimationERK5QR'
        'ect',
        self._valueOf(rect),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QRect, QModelIndex, QModelIndex)
  def intersectedRect(
      self,
      rect: QRect,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> QRect:
    """
    Calls Qt's 'QRect QTreeViewPrivate::intersectedRect(const QRect rect,
    const QModelIndex &topLeft, const QModelIndex &bottomRight) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#intersectedRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTreeViewPrivate::intersectedRect(const QRect rect, const
    #      QModelIndex &topLeft, const QModelIndex &bottomRight) const
    ritual = (
        'ritual_ZNK16QTreeViewPrivate15intersectedRectE5QRectRK11QModelInde'
        'xS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QTreeViewPrivate15intersectedRectE5QRectRK11QMod'
          'elIndexS3_')
    address = self.uglySide.call(
        ritual,
        self._valueOf(rect), self._valueOf(topLeft),
        self._valueOf(bottomRight),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def pageUp(self, item: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::pageUp(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#pageUp

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::pageUp(int item) const
    return self.uglySide.call('ritual_ZNK16QTreeViewPrivate6pageUpEi', item)

  @overload(int)
  def pageDown(self, item: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::pageDown(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#pageDown

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::pageDown(int item) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate8pageDownEi', item,
    )

  def itemForKeyHome(self) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::itemForKeyHome() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#itemForKeyHome
    """
    #  int QTreeViewPrivate::itemForKeyHome() const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate14itemForKeyHomeEv',
    )

  def itemForKeyEnd(self) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::itemForKeyEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#itemForKeyEnd
    """
    #  int QTreeViewPrivate::itemForKeyEnd() const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate13itemForKeyEndEv',
    )

  @overload(int)
  def itemHeight(self, item: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::itemHeight(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#itemHeight

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::itemHeight(int item) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate10itemHeightEi', item,
    )

  @overload(int)
  def indentationForItem(self, item: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::indentationForItem(int item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#indentationForItem

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::indentationForItem(int item) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate18indentationForItemEi', item,
    )

  @overload(int)
  def coordinateForItem(self, item: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::coordinateForItem(int item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#coordinateForItem

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::coordinateForItem(int item) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate17coordinateForItemEi', item,
    )

  @overload(int)
  def itemAtCoordinate(self, coordinate: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::itemAtCoordinate(int coordinate)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#itemAtCoordinate

    Parameters
    ----------

    coordinate : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::itemAtCoordinate(int coordinate) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate16itemAtCoordinateEi', coordinate,
    )

  @overload(QModelIndex)
  def viewIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::viewIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#viewIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QTreeViewPrivate::viewIndex(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate9viewIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(int)
  @overload(int, int)
  def modelIndex(self, i: int, column: int = 0) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeViewPrivate::modelIndex(int i, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#modelIndex

    Parameters
    ----------

    i : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeViewPrivate::modelIndex(int i, int column) const
    address = self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate10modelIndexEii', i, column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(int)
  @overload(int, int)
  def lastVisibleItem(self, firstVisual: int = -1, offset: int = -1) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::lastVisibleItem(int firstVisual, int
    offset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#lastVisibleItem

    Parameters
    ----------

    firstVisual : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QTreeViewPrivate::lastVisibleItem(int firstVisual, int offset)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate15lastVisibleItemEii',
        firstVisual, offset,
    )

  @overload(int)
  def columnAt(self, x: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::columnAt(int x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#columnAt

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::columnAt(int x) const
    return self.uglySide.call('ritual_ZNK16QTreeViewPrivate8columnAtEi', x)

  @overload(QModelIndex)
  def hasVisibleChildren(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeViewPrivate::hasVisibleChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#hasVisibleChildren

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeViewPrivate::hasVisibleChildren(const QModelIndex &parent)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate18hasVisibleChildrenERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QPoint)
  def itemDecorationAt(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::itemDecorationAt(const QPoint &pos)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#itemDecorationAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QTreeViewPrivate::itemDecorationAt(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate16itemDecorationAtERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QModelIndex)
  def itemDecorationRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QTreeViewPrivate::itemDecorationRect(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#itemDecorationRect

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTreeViewPrivate::itemDecorationRect(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate18itemDecorationRectERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QModelIndex, int, QStyleOptionViewItem, int)
  def widthHintForIndex(
      self,
      index: QModelIndex,
      hint: int,
      option: QStyleOptionViewItem,
      i: int,
  ) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::widthHintForIndex(const QModelIndex
    &index, int hint, const QStyleOptionViewItem &option, int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#widthHintForIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hint : int
      Passed on as it is.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    i : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::widthHintForIndex(const QModelIndex &index, int
    #      hint, const QStyleOptionViewItem &option, int i) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate17widthHintForIndexERK11QModelIndexiRK'
        '20QStyleOptionViewItemi',
        self._valueOf(index), hint, self._valueOf(option), i,
    )

  @overload(QModelIndex)
  def visualRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QTreeViewPrivate::visualRect(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#visualRect

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTreeViewPrivate::visualRect(const QModelIndex &index) const
    ritual = 'ritual_ZNK16QTreeViewPrivate10visualRectERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QTreeViewPrivate10visualRectERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QModelIndex, RectRule)
  def visualRect(self, index: QModelIndex, rule: RectRule) -> QRect:
    """
    Calls Qt's 'QRect QTreeViewPrivate::visualRect(const QModelIndex &index,
    RectRule rule) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#visualRect

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    rule : RectRule
      Passed on as its number.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTreeViewPrivate::visualRect(const QModelIndex &index, RectRule
    #      rule) const
    address = self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate10visualRectERK11QModelIndexNS_8RectRu'
        'leE',
        self._valueOf(index), rule.value,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QModelIndex)
  def isIndexExpanded(self, idx: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeViewPrivate::isIndexExpanded(const QModelIndex
    &idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#isIndexExpanded

    Parameters
    ----------

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeViewPrivate::isIndexExpanded(const QModelIndex &idx) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate15isIndexExpandedERK11QModelIndex',
        self._valueOf(idx),
    )

  @overload(QModelIndex)
  def isRowHidden(self, idx: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeViewPrivate::isRowHidden(const QModelIndex &idx)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#isRowHidden

    Parameters
    ----------

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeViewPrivate::isRowHidden(const QModelIndex &idx) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate11isRowHiddenERK11QModelIndex',
        self._valueOf(idx),
    )

  @overload(int)
  def isItemHiddenOrDisabled(self, i: int) -> bool:
    """
    Calls Qt's 'bool QTreeViewPrivate::isItemHiddenOrDisabled(int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#isItemHiddenOrDisabled

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QTreeViewPrivate::isItemHiddenOrDisabled(int i) const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate22isItemHiddenOrDisabledEi', i,
    )

  @overload(int)
  def above(self, item: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::above(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#above

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::above(int item) const
    return self.uglySide.call('ritual_ZNK16QTreeViewPrivate5aboveEi', item)

  @overload(int)
  def below(self, item: int) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::below(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#below

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTreeViewPrivate::below(int item) const
    return self.uglySide.call('ritual_ZNK16QTreeViewPrivate5belowEi', item)

  @overload(QModelIndex)
  def accessibleTable2Index(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::accessibleTable2Index(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#accessibleTable2Index

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QTreeViewPrivate::accessibleTable2Index(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate21accessibleTable2IndexERK11QModelInde'
        'x',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def accessibleChildIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QTreeViewPrivate::accessibleChildIndex(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#accessibleChildIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QTreeViewPrivate::accessibleChildIndex(const QModelIndex &index)
    #      const
    ritual = (
        'ritual_ZNK16QTreeViewPrivate20accessibleChildIndexERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QTreeViewPrivate20accessibleChildIndexERK11QMode'
          'lIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

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
    Qt's 'QTreeViewPrivate::QTreeViewPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeViewPrivate.__init__' has no cute function yet. Qt's "
        "'QTreeViewPrivate::QTreeViewPrivate()': leans on "
        "'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex "
        "const&, int, int)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QTreeView]:
    """
    Calls Qt's 'QTreeView *QTreeViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#q_func

    Returns
    -------

    Optional[QTreeView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeView *QTreeViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QTreeViewPrivate6q_funcEv')
    from . import QTreeView
    return QTreeView._cuteAt(address)

  def initialize(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#initialize
    """
    #  void QTreeViewPrivate::initialize()
    self.uglySide.call('ritual_ZN16QTreeViewPrivate10initializeEv')

  def clearConnections(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::clearConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#clearConnections
    """
    #  void QTreeViewPrivate::clearConnections()
    self.uglySide.call('ritual_ZN16QTreeViewPrivate16clearConnectionsEv')

  @overload(QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QModelIndex)
  def adjustViewOptionsForIndex(
      self,
      option: Optional[QStyleOptionViewItem],
      current: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QTreeViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewItem *option,
    const QModelIndex &current) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#adjustViewOptionsForIndex

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QTreeViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewItem
    #      *option, const QModelIndex &current) const
    ritual = (
        'ritual_ZNK16QTreeViewPrivate25adjustViewOptionsForIndexEP20QStyleO'
        'ptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QTreeViewPrivate25adjustViewOptionsForIndexEP20Q'
          'StyleOptionViewItemRK11QModelIndex')
    self.uglySide.call(
        ritual, self._addressOf(option), self._valueOf(current),
    )

  def beginAnimatedOperation(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::beginAnimatedOperation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#beginAnimatedOperation
    """
    #  void QTreeViewPrivate::beginAnimatedOperation()
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate22beginAnimatedOperationEv',
    )

  @overload(QPainter)
  @overload(NoneType)
  def drawAnimatedOperation(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::drawAnimatedOperation(QPainter
    *painter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#drawAnimatedOperation

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeViewPrivate::drawAnimatedOperation(QPainter *painter) const
    self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate21drawAnimatedOperationEP8QPainter',
        self._addressOf(painter),
    )

  def endAnimatedOperation(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::endAnimatedOperation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#endAnimatedOperation
    """
    #  void QTreeViewPrivate::endAnimatedOperation()
    self.uglySide.call('ritual_ZN16QTreeViewPrivate20endAnimatedOperationEv')

  @overload(int, bool)
  def expand(self, item: int, emitSignal: bool) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::expand(int item, bool emitSignal)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#expand

    Parameters
    ----------

    item : int
      Passed on as it is.

    emitSignal : bool
      Passed on as it is.
    """
    #  void QTreeViewPrivate::expand(int item, bool emitSignal)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate6expandEib', item, emitSignal,
    )

  @overload(int, bool)
  def collapse(self, item: int, emitSignal: bool) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::collapse(int item, bool emitSignal)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#collapse

    Parameters
    ----------

    item : int
      Passed on as it is.

    emitSignal : bool
      Passed on as it is.
    """
    #  void QTreeViewPrivate::collapse(int item, bool emitSignal)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate8collapseEib', item, emitSignal,
    )

  @overload(QModelIndex, int, int)
  def columnsAboutToBeRemoved(
      self,
      a0: QModelIndex,
      a1: int,
      a2: int,
  ) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::columnsAboutToBeRemoved(const
    QModelIndex &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#columnsAboutToBeRemoved

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QTreeViewPrivate::columnsAboutToBeRemoved(const QModelIndex &a0,
    #      int a1, int a2)
    ritual = (
        'ritual_ZN16QTreeViewPrivate23columnsAboutToBeRemovedERK11QModelInd'
        'exii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QTreeViewPrivate23columnsAboutToBeRemovedERK11QMo'
          'delIndexii')
    self.uglySide.call(ritual, self._valueOf(a0), a1, a2)

  @overload(QModelIndex, int, int)
  def columnsRemoved(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::columnsRemoved(const QModelIndex &a0,
    int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#columnsRemoved

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QTreeViewPrivate::columnsRemoved(const QModelIndex &a0, int a1,
    #      int a2)
    ritual = 'ritual_ZN16QTreeViewPrivate14columnsRemovedERK11QModelIndexii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QTreeViewPrivate14columnsRemovedERK11QModelIndexi'
          'i')
    self.uglySide.call(ritual, self._valueOf(a0), a1, a2)

  def modelAboutToBeReset(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::modelAboutToBeReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#modelAboutToBeReset
    """
    #  void QTreeViewPrivate::modelAboutToBeReset()
    self.uglySide.call('ritual_ZN16QTreeViewPrivate19modelAboutToBeResetEv')

  @overload(int, Qt.SortOrder)
  def sortIndicatorChanged(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::sortIndicatorChanged(int column,
    Qt::SortOrder order)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#sortIndicatorChanged

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTreeViewPrivate::sortIndicatorChanged(int column, Qt::SortOrder
    #      order)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate20sortIndicatorChangedEiN2Qt9SortOrderE',
        column, order.value,
    )

  def modelDestroyed(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::modelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#modelDestroyed
    """
    #  void QTreeViewPrivate::modelDestroyed()
    ritual = 'ritual_ZN16QTreeViewPrivate14modelDestroyedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QTreeViewPrivate14modelDestroyedEv'
    self.uglySide.call(ritual)

  @overload(int, ExpandItems, InitializeNewItems)
  def layout(
      self,
      item: int,
      expandItems: ExpandItems,
      initializeNewItems: InitializeNewItems,
  ) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::layout(int item, ExpandItems
    expandItems, InitializeNewItems initializeNewItems)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#layout

    Parameters
    ----------

    item : int
      Passed on as it is.

    expandItems : ExpandItems
      Passed on as its number.

    initializeNewItems : InitializeNewItems
      Passed on as its number.
    """
    #  void QTreeViewPrivate::layout(int item, ExpandItems expandItems,
    #      InitializeNewItems initializeNewItems)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate6layoutEiNS_11ExpandItemsENS_18Initiali'
        'zeNewItemsE',
        item, expandItems.value, initializeNewItems.value,
    )

  @overload(ExpandItems, InitializeNewItems)
  def doItemsLayout(
      self,
      expandItems: ExpandItems,
      initializeNewItems: InitializeNewItems,
  ) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::doItemsLayout(ExpandItems expandItems,
    InitializeNewItems initializeNewItems)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#doItemsLayout

    Parameters
    ----------

    expandItems : ExpandItems
      Passed on as its number.

    initializeNewItems : InitializeNewItems
      Passed on as its number.
    """
    #  void QTreeViewPrivate::doItemsLayout(ExpandItems expandItems,
    #      InitializeNewItems initializeNewItems)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate13doItemsLayoutENS_11ExpandItemsENS_18I'
        'nitializeNewItemsE',
        expandItems.value, initializeNewItems.value,
    )

  @overload(int, int, QTreeViewItem)
  def insertViewItems(
      self,
      pos: int,
      count: int,
      viewItem: QTreeViewItem,
  ) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::insertViewItems(int pos, int count,
    const QTreeViewItem &viewItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#insertViewItems

    Parameters
    ----------

    pos : int
      Passed on as it is.

    count : int
      Passed on as it is.

    viewItem : QTreeViewItem
      Passed on as a value: Qt reads the C++ QTreeViewItem, which stays
      Python's own.
    """
    #  void QTreeViewPrivate::insertViewItems(int pos, int count, const
    #      QTreeViewItem &viewItem)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate15insertViewItemsEiiRK13QTreeViewItem',
        pos, count, self._valueOf(viewItem),
    )

  @overload(int, int)
  def removeViewItems(self, pos: int, count: int) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::removeViewItems(int pos, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#removeViewItems

    Parameters
    ----------

    pos : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QTreeViewPrivate::removeViewItems(int pos, int count)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate15removeViewItemsEii', pos, count,
    )

  @overload(QPoint)
  def expandOrCollapseItemAtPos(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QTreeViewPrivate::expandOrCollapseItemAtPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#expandOrCollapseItemAtPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QTreeViewPrivate::expandOrCollapseItemAtPos(const QPoint &pos)
    return self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate25expandOrCollapseItemAtPosERK6QPoint',
        self._valueOf(pos),
    )

  def updateScrollBars(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::updateScrollBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#updateScrollBars
    """
    #  void QTreeViewPrivate::updateScrollBars()
    self.uglySide.call('ritual_ZN16QTreeViewPrivate16updateScrollBarsEv')

  @overload(QModelIndex, QModelIndex, QItemSelectionModel.SelectionFlags)
  def select(
      self,
      start: QModelIndex,
      stop: QModelIndex,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::select(const QModelIndex &start, const
    QModelIndex &stop, QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeviewprivate.html#select

    Parameters
    ----------

    start : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    stop : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QTreeViewPrivate::select(const QModelIndex &start, const
    #      QModelIndex &stop, QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate6selectERK11QModelIndexS2_6QFlagsIN19QI'
        'temSelectionModel13SelectionFlagEE',
        self._valueOf(start), self._valueOf(stop), command.value,
    )

  @overload(QPainter, QStyleOptionViewItem, int, int)
  @overload(QPainter, NoneType, int, int)
  @overload(NoneType, QStyleOptionViewItem, int, int)
  @overload(NoneType, NoneType, int, int)
  def paintAlternatingRowColors(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionViewItem],
      y: int,
      bottom: int,
  ) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::paintAlternatingRowColors(QPainter
    *painter, QStyleOptionViewItem *option, int y, int bottom) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#paintAlternatingRowColors

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    y : int
      Passed on as it is.

    bottom : int
      Passed on as it is.
    """
    #  void QTreeViewPrivate::paintAlternatingRowColors(QPainter *painter,
    #      QStyleOptionViewItem *option, int y, int bottom) const
    self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate25paintAlternatingRowColorsEP8QPainter'
        'P20QStyleOptionViewItemii',
        self._addressOf(painter), self._addressOf(option), y, bottom,
    )

  @overload(QPersistentModelIndex)
  def storeExpanded(self, idx: QPersistentModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeViewPrivate::storeExpanded(const
    QPersistentModelIndex &idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#storeExpanded

    Parameters
    ----------

    idx : QPersistentModelIndex
      Passed on as a value: Qt reads the C++ QPersistentModelIndex, which
      stays Python's own.
    """
    #  bool QTreeViewPrivate::storeExpanded(const QPersistentModelIndex &idx)
    return self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate13storeExpandedERK21QPersistentModelInd'
        'ex',
        self._valueOf(idx),
    )

  @overload(int)
  def invalidateHeightCache(self, item: int) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::invalidateHeightCache(int item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#invalidateHeightCache

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  void QTreeViewPrivate::invalidateHeightCache(int item) const
    self.uglySide.call(
        'ritual_ZNK16QTreeViewPrivate21invalidateHeightCacheEi', item,
    )

  def updateIndentationFromStyle(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::updateIndentationFromStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#updateIndentationFromStyle
    """
    #  void QTreeViewPrivate::updateIndentationFromStyle()
    self.uglySide.call(
        'ritual_ZN16QTreeViewPrivate26updateIndentationFromStyleEv',
    )

  def updateAccessibility(self) -> None:
    """
    Calls Qt's 'void QTreeViewPrivate::updateAccessibility()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeviewprivate.html#updateAccessibility
    """
    #  void QTreeViewPrivate::updateAccessibility()
    self.uglySide.call('ritual_ZN16QTreeViewPrivate19updateAccessibilityEv')

  @staticmethod
  def calcLogicalIndices(*__, **_) -> Never:
    """
    Qt's 'void QTreeViewPrivate::calcLogicalIndices(QList<int>
    *logicalIndices, QList<QStyleOptionViewItem::ViewItemPosition>
    *itemPositions, int left, int right) const': names 'QList<int>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QTreeViewPrivate.calcLogicalIndices' has no cute function yet. "
        "Qt's 'void QTreeViewPrivate::calcLogicalIndices(QList<int> "
        "*logicalIndices, QList<QStyleOptionViewItem::ViewItemPosition> "
        "*itemPositions, int left, int right) const': names 'QList<int>', "
        "which has no cute class yet.")

  @staticmethod
  def columnRanges(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<int, int>> QTreeViewPrivate::columnRanges(const
    QModelIndex &topIndex, const QModelIndex &bottomIndex) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTreeViewPrivate.columnRanges' has no cute function yet. Qt's "
        "'QList<std::pair<int, int>> QTreeViewPrivate::columnRanges(const "
        "QModelIndex &topIndex, const QModelIndex &bottomIndex) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def firstVisibleItem(*__, **_) -> Never:
    """
    Qt's 'int QTreeViewPrivate::firstVisibleItem(int *offset) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QTreeViewPrivate.firstVisibleItem' has no cute function yet. Qt's "
        "'int QTreeViewPrivate::firstVisibleItem(int *offset) const': takes "
        "a number to change where it is.")

  @staticmethod
  def prepareAnimatedOperation(*__, **_) -> Never:
    """
    Qt's 'void QTreeViewPrivate::prepareAnimatedOperation(int item,
    QVariantAnimation::Direction d)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QTreeViewPrivate.prepareAnimatedOperation' has no cute function "
        "yet. Qt's 'void QTreeViewPrivate::prepareAnimatedOperation(int "
        "item, QVariantAnimation::Direction d)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def startAndEndColumns(*__, **_) -> Never:
    """
    Qt's 'std::pair<int, int> QTreeViewPrivate::startAndEndColumns(const
    QRect &rect) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTreeViewPrivate.startAndEndColumns' has no cute function yet. "
        "Qt's 'std::pair<int, int> "
        "QTreeViewPrivate::startAndEndColumns(const QRect &rect) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def updateChildCount(*__, **_) -> Never:
    """
    Qt's 'void QTreeViewPrivate::updateChildCount(const int parentItem, const
    int delta)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QTreeViewPrivate.updateChildCount' has no cute function yet. Qt's "
        "'void QTreeViewPrivate::updateChildCount(const int parentItem, "
        "const int delta)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
