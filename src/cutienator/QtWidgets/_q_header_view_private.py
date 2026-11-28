"""
QHeaderViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qheaderview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QHeaderViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QList
from . import QAbstractItemView, QAbstractItemViewPrivate, QHeaderView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QBitArray, QModelIndex, QPersistentModelIndex
  from . import QScrollBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBitArray = WAIT['QBitArray']
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QScrollBar = WAIT['QScrollBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHeaderViewPrivate(QAbstractItemViewPrivate):
  """
  The cute side of Qt's QHeaderViewPrivate: a plain Python object standing in
  front of one C++ QHeaderViewPrivate.

  It is built on the cute 'QAbstractItemViewPrivate', as Qt's
  QHeaderViewPrivate is built on Qt's QAbstractItemViewPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHeaderViewPrivate that has a ritual and that Python
  can call so far, 66 names in all: 'q_func', 'lastVisibleVisualIndex',
  'restoreSizeOnPrevLastSection', 'setNewLastSection',
  'maybeRestorePrevLastSectionAndStretchLast', 'sectionHandleAt',
  'setupSectionIndicator', 'updateSectionIndicator', 'updateHiddenSections',
  'resizeSections', 'sectionsRemoved', 'sectionsAboutToBeMoved',
  'sectionsMoved', 'sectionsAboutToBeChanged', 'sectionsChanged',
  'isSectionSelected', 'isFirstVisibleSection', 'isLastVisibleSection',
  'rowIntersectsSelection', 'columnIntersectsSelection',
  'sectionIntersectsSelection', 'isRowSelected', 'isColumnSelected',
  'prepareSectionSelected', 'sectionCount', 'reverse', 'logicalIndex',
  'visualIndex', 'setDefaultValues', 'isVisualIndexHidden',
  'setVisualIndexHidden', 'hasAutoResizeSections',
  'invalidateCachedSizeHint', 'initializeIndexMapping',
  'clearCascadingSections', 'saveCascadingSectionSize',
  'sectionIsCascadable', 'modelSectionCount', 'doDelayedResizeSections',
  'executePostedResize', 'disconnectModel', 'clear',
  'defaultSortOrderForSection', 'cascadingResize', 'noSectionMemoryUsage',
  'switchToFlexibleModeWithSectionMemoryUsage',
  'updateCountInNoSectionItemsMode', 'createSectionItems',
  'removeSectionsFromSectionItems', 'resizeSectionItem',
  'setDefaultSectionSize', 'updateDefaultSectionSizeFromStyle',
  'recalcSectionStartPos', 'headerLength', 'sectionsHiddenToBitVector',
  'setHiddenSectionsFromBitVector', 'headerSectionSize',
  'headerSectionPosition', 'headerVisualIndexAt',
  'setHeaderSectionResizeMode', 'headerSectionResizeMode',
  'setGlobalHeaderResizeMode', 'viewSectionSizeHint', 'adjustedVisualIndex',
  'setScrollOffset', 'updateSectionsBeforeAfter'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHeaderView *QHeaderViewPrivate::q_func() const': takes in
    Python what 'QHeaderView *QHeaderViewPrivate::q_func()' takes.
  - Qt's 'void QHeaderViewPrivate::setHeaderMode(HeaderMode mode)': names the
    enum 'HeaderMode', whose class cannot be named here.

  What has no ritual
  ------------------

  5 of the 73 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied; 1
  leans on 'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QHeaderViewPrivate is created at the first use, not by
    'QHeaderViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHeaderViewPrivate.
  - Each name of Qt's QHeaderViewPrivate that has no cute function yet,
    '__init__', 'flipSortIndicator', 'getStyleOption', 'read',
    'setHeaderMode', 'write', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHeaderViewPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QHeaderViewPrivate::State' of Qt, with the 5 names Qt gives in
    it.
    """

    NoState = Kee[int](0)
    ResizeSection = Kee[int](1)
    MoveSection = Kee[int](2)
    SelectSections = Kee[int](3)
    NoClear = Kee[int](4)

  class StateVersion(CuteNum):
    """
    The enum 'QHeaderViewPrivate::StateVersion' of Qt, with the 1 names Qt
    gives in it.
    """

    VersionMarker = Kee[int](255)

  #  The classes Qt writes inside QHeaderViewPrivate, each a class in here as
  #  in C++.

  class LayoutChangeItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHeaderViewPrivate::LayoutChangeItem: a plain
    Python object standing in front of one C++
    QHeaderViewPrivate::LayoutChangeItem.

    C++ hands a QHeaderViewPrivate::LayoutChangeItem around as a copy, so
    every C++ QHeaderViewPrivate::LayoutChangeItem behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QHeaderViewPrivate::LayoutChangeItem yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHeaderViewPrivate::LayoutChangeItem::~LayoutChangeItem()': the
      destructor: Python removes its C++ QHeaderViewPrivate::LayoutChangeItem
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QHeaderViewPrivate::LayoutChangeItem is created at the first
      use, not by 'QHeaderViewPrivate::LayoutChangeItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHeaderViewPrivate::LayoutChangeItem back gives a
      copy the ritual made for Python, in a new cute
      QHeaderViewPrivate::LayoutChangeItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHeaderViewPrivate::LayoutChangeItem'

    #  Qt's '~QHeaderViewPrivate::LayoutChangeItem()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QHeaderViewPrivate::LayoutChangeItem behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN18QHeaderViewPrivate16LayoutChangeItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  class SectionItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHeaderViewPrivate::SectionItem: a plain Python
    object standing in front of one C++ QHeaderViewPrivate::SectionItem.

    C++ hands a QHeaderViewPrivate::SectionItem around as a copy, so every
    C++ QHeaderViewPrivate::SectionItem behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QHeaderViewPrivate::SectionItem that has a ritual
    and that Python can call so far, 2 names in all: 'sectionSize',
    'calculatedEndPos'. It can be made from Python, in 2 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'void QHeaderViewPrivate::SectionItem::write(QDataStream &out)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'void QHeaderViewPrivate::SectionItem::read(QDataStream &in)':
      takes a type Python has no way to hand over yet.
    - Qt's 'QHeaderViewPrivate::SectionItem::~SectionItem()': the destructor:
      Python removes its C++ QHeaderViewPrivate::SectionItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QHeaderViewPrivate::SectionItem is created at the first use,
      not by 'QHeaderViewPrivate::SectionItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHeaderViewPrivate::SectionItem back gives a copy
      the ritual made for Python, in a new cute
      QHeaderViewPrivate::SectionItem.
    - Each name of Qt's QHeaderViewPrivate::SectionItem that has no cute
      function yet, 'read', 'write', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHeaderViewPrivate::SectionItem'

    #  Qt's '~QHeaderViewPrivate::SectionItem()'. Naming it makes this a
    #  value class: Python owns every C++ QHeaderViewPrivate::SectionItem
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QHeaderViewPrivate11SectionItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def sectionSize(self) -> int:
      """
      Calls Qt's 'int QHeaderViewPrivate::SectionItem::sectionSize() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qheaderviewprivate-sectionitem.html#sectionSize
      """
      #  int QHeaderViewPrivate::SectionItem::sectionSize() const
      return self.uglySide.call(
          'ritual_ZNK18QHeaderViewPrivate11SectionItem11sectionSizeEv',
      )

    def calculatedEndPos(self) -> int:
      """
      Calls Qt's 'int QHeaderViewPrivate::SectionItem::calculatedEndPos()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qheaderviewprivate-sectionitem.html
      """
      #  int QHeaderViewPrivate::SectionItem::calculatedEndPos() const
      return self.uglySide.call(
          'ritual_ZNK18QHeaderViewPrivate11SectionItem16calculatedEndPosEv',
      )

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
      'QHeaderViewPrivate::SectionItem::SectionItem()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qheaderviewprivate-sectionitem.html#SectionItem
      """
      #  QHeaderViewPrivate::SectionItem::SectionItem()
      self._noteCreation(
          QHeaderViewPrivate.SectionItem, lambda: Rituals.call(
              'ritual_ZN18QHeaderViewPrivate11SectionItemC1Ev',
          ))

    @overload(int, QHeaderView.ResizeMode)
    def __init__(self, length: int, mode: QHeaderView.ResizeMode) -> None:
      """
      Notes what was given, for Qt's
      'QHeaderViewPrivate::SectionItem::SectionItem(int length,
      QHeaderView::ResizeMode mode)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qheaderviewprivate-sectionitem.html#SectionItem

      Parameters
      ----------

      length : int
        Passed on as it is.

      mode : QHeaderView.ResizeMode
        Passed on as its number.
      """
      #  QHeaderViewPrivate::SectionItem::SectionItem(int length,
      #      QHeaderView::ResizeMode mode)
      self._noteCreation(
          QHeaderViewPrivate.SectionItem, lambda: Rituals.call(
              'ritual_ZN18QHeaderViewPrivate11SectionItemC1EiN11QHeaderView'
              '10ResizeModeE',
              length, mode.value,
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

    @staticmethod
    def read(*__, **_) -> Never:
      """
      Qt's 'void QHeaderViewPrivate::SectionItem::read(QDataStream &in)':
      takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QHeaderViewPrivate.SectionItem.read' has no cute function yet. "
          "Qt's 'void QHeaderViewPrivate::SectionItem::read(QDataStream "
          "&in)': takes a type Python has no way to hand over yet.")

    @staticmethod
    def write(*__, **_) -> Never:
      """
      Qt's 'void QHeaderViewPrivate::SectionItem::write(QDataStream &out)
      const': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QHeaderViewPrivate.SectionItem.write' has no cute function yet. "
          "Qt's 'void QHeaderViewPrivate::SectionItem::write(QDataStream "
          "&out) const': takes a type Python has no way to hand over yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHeaderViewPrivate'

  #  A C++ QHeaderViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHeaderViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lastVisibleVisualIndex(self) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::lastVisibleVisualIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#lastVisibleVisualIndex
    """
    #  int QHeaderViewPrivate::lastVisibleVisualIndex() const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate22lastVisibleVisualIndexEv',
    )

  @overload(int)
  def isSectionSelected(self, section: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::isSectionSelected(int section)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#isSectionSelected

    Parameters
    ----------

    section : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::isSectionSelected(int section) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate17isSectionSelectedEi', section,
    )

  @overload(int)
  def isFirstVisibleSection(self, section: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::isFirstVisibleSection(int section)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#isFirstVisibleSection

    Parameters
    ----------

    section : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::isFirstVisibleSection(int section) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate21isFirstVisibleSectionEi', section,
    )

  @overload(int)
  def isLastVisibleSection(self, section: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::isLastVisibleSection(int section)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#isLastVisibleSection

    Parameters
    ----------

    section : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::isLastVisibleSection(int section) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate20isLastVisibleSectionEi', section,
    )

  @overload(int)
  def rowIntersectsSelection(self, row: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::rowIntersectsSelection(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#rowIntersectsSelection

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::rowIntersectsSelection(int row) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate22rowIntersectsSelectionEi', row,
    )

  @overload(int)
  def columnIntersectsSelection(self, column: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::columnIntersectsSelection(int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#columnIntersectsSelection

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::columnIntersectsSelection(int column) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate25columnIntersectsSelectionEi',
        column,
    )

  @overload(int)
  def sectionIntersectsSelection(self, logical: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::sectionIntersectsSelection(int
    logical) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionIntersectsSelection

    Parameters
    ----------

    logical : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::sectionIntersectsSelection(int logical) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate26sectionIntersectsSelectionEi',
        logical,
    )

  @overload(int)
  def isRowSelected(self, row: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::isRowSelected(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#isRowSelected

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::isRowSelected(int row) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate13isRowSelectedEi', row,
    )

  @overload(int)
  def isColumnSelected(self, column: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::isColumnSelected(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#isColumnSelected

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::isColumnSelected(int column) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate16isColumnSelectedEi', column,
    )

  def sectionCount(self) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::sectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionCount
    """
    #  int QHeaderViewPrivate::sectionCount() const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate12sectionCountEv',
    )

  def reverse(self) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::reverse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderviewprivate.html#reverse
    """
    #  bool QHeaderViewPrivate::reverse() const
    return self.uglySide.call('ritual_ZNK18QHeaderViewPrivate7reverseEv')

  @overload(int)
  def logicalIndex(self, visualIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::logicalIndex(int visualIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#logicalIndex

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::logicalIndex(int visualIndex) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate12logicalIndexEi', visualIndex,
    )

  @overload(int)
  def visualIndex(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::visualIndex(int logicalIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#visualIndex

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::visualIndex(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate11visualIndexEi', logicalIndex,
    )

  @overload(int)
  def isVisualIndexHidden(self, visual: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::isVisualIndexHidden(int visual)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#isVisualIndexHidden

    Parameters
    ----------

    visual : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::isVisualIndexHidden(int visual) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate19isVisualIndexHiddenEi', visual,
    )

  def hasAutoResizeSections(self) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::hasAutoResizeSections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#hasAutoResizeSections
    """
    #  bool QHeaderViewPrivate::hasAutoResizeSections() const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate21hasAutoResizeSectionsEv',
    )

  @overload(int)
  def sectionIsCascadable(self, visual: int) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::sectionIsCascadable(int visual)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionIsCascadable

    Parameters
    ----------

    visual : int
      Passed on as it is.
    """
    #  bool QHeaderViewPrivate::sectionIsCascadable(int visual) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate19sectionIsCascadableEi', visual,
    )

  def modelSectionCount(self) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::modelSectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#modelSectionCount
    """
    #  int QHeaderViewPrivate::modelSectionCount() const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate17modelSectionCountEv',
    )

  @overload(int)
  def defaultSortOrderForSection(self, section: int) -> Qt.SortOrder:
    """
    Calls Qt's 'Qt::SortOrder
    QHeaderViewPrivate::defaultSortOrderForSection(int section) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#defaultSortOrderForSection

    Parameters
    ----------

    section : int
      Passed on as it is.

    Returns
    -------

    Qt.SortOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.SortOrder(number)'
      gives.
    """
    #  Qt::SortOrder QHeaderViewPrivate::defaultSortOrderForSection(int
    #      section) const
    return Qt.SortOrder(self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate26defaultSortOrderForSectionEi',
        section,
    ))

  def noSectionMemoryUsage(self) -> bool:
    """
    Calls Qt's 'bool QHeaderViewPrivate::noSectionMemoryUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#noSectionMemoryUsage
    """
    #  bool QHeaderViewPrivate::noSectionMemoryUsage() const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate20noSectionMemoryUsageEv',
    )

  def headerLength(self) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::headerLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#headerLength
    """
    #  int QHeaderViewPrivate::headerLength() const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate12headerLengthEv',
    )

  def sectionsHiddenToBitVector(self) -> QBitArray:
    """
    Calls Qt's 'QBitArray QHeaderViewPrivate::sectionsHiddenToBitVector()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionsHiddenToBitVector

    Returns
    -------

    QBitArray
      A new cute QBitArray around the copy Qt gave back. Python owns it.
    """
    #  QBitArray QHeaderViewPrivate::sectionsHiddenToBitVector() const
    address = self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate25sectionsHiddenToBitVectorEv',
    )
    from ..QtCore import QBitArray
    return QBitArray._cuteOwning(address)

  @overload(int)
  def headerSectionSize(self, visual: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::headerSectionSize(int visual) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#headerSectionSize

    Parameters
    ----------

    visual : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::headerSectionSize(int visual) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate17headerSectionSizeEi', visual,
    )

  @overload(int)
  def headerSectionPosition(self, visual: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::headerSectionPosition(int visual)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#headerSectionPosition

    Parameters
    ----------

    visual : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::headerSectionPosition(int visual) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate21headerSectionPositionEi', visual,
    )

  @overload(int)
  def headerVisualIndexAt(self, position: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::headerVisualIndexAt(int position)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#headerVisualIndexAt

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::headerVisualIndexAt(int position) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate19headerVisualIndexAtEi', position,
    )

  @overload(int)
  def headerSectionResizeMode(self, visual: int) -> QHeaderView.ResizeMode:
    """
    Calls Qt's 'QHeaderView::ResizeMode
    QHeaderViewPrivate::headerSectionResizeMode(int visual) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#headerSectionResizeMode

    Parameters
    ----------

    visual : int
      Passed on as it is.

    Returns
    -------

    QHeaderView.ResizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QHeaderView.ResizeMode(number)' gives.
    """
    #  QHeaderView::ResizeMode
    #      QHeaderViewPrivate::headerSectionResizeMode(int visual) const
    return QHeaderView.ResizeMode(self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate23headerSectionResizeModeEi', visual,
    ))

  @overload(int)
  def viewSectionSizeHint(self, logical: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::viewSectionSizeHint(int logical)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#viewSectionSizeHint

    Parameters
    ----------

    logical : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::viewSectionSizeHint(int logical) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate19viewSectionSizeHintEi', logical,
    )

  @overload(int)
  def adjustedVisualIndex(self, visualIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::adjustedVisualIndex(int visualIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#adjustedVisualIndex

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::adjustedVisualIndex(int visualIndex) const
    return self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate19adjustedVisualIndexEi', visualIndex,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setNewLastSection(self, visualIndexForLastSection: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setNewLastSection(int
    visualIndexForLastSection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setNewLastSection

    Parameters
    ----------

    visualIndexForLastSection : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::setNewLastSection(int
    #      visualIndexForLastSection)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate17setNewLastSectionEi',
        visualIndexForLastSection,
    )

  @overload(Qt.Orientation)
  def setDefaultValues(self, o: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setDefaultValues(Qt::Orientation
    o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setDefaultValues

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.
    """
    #  void QHeaderViewPrivate::setDefaultValues(Qt::Orientation o)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate16setDefaultValuesEN2Qt11OrientationE',
        o.value,
    )

  @overload(int, bool)
  def setVisualIndexHidden(self, visual: int, hidden: bool) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setVisualIndexHidden(int visual,
    bool hidden)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setVisualIndexHidden

    Parameters
    ----------

    visual : int
      Passed on as it is.

    hidden : bool
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::setVisualIndexHidden(int visual, bool hidden)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate20setVisualIndexHiddenEib',
        visual, hidden,
    )

  @overload(int)
  def setDefaultSectionSize(self, size: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setDefaultSectionSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setDefaultSectionSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::setDefaultSectionSize(int size)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate21setDefaultSectionSizeEi', size,
    )

  @overload(QBitArray)
  def setHiddenSectionsFromBitVector(self, sectionHidden: QBitArray) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setHiddenSectionsFromBitVector(const
    QBitArray &sectionHidden)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html

    Parameters
    ----------

    sectionHidden : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  void QHeaderViewPrivate::setHiddenSectionsFromBitVector(const
    #      QBitArray &sectionHidden)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate30setHiddenSectionsFromBitVectorERK9Q'
        'BitArray',
        self._valueOf(sectionHidden),
    )

  @overload(int, QHeaderView.ResizeMode)
  def setHeaderSectionResizeMode(
      self,
      visual: int,
      mode: QHeaderView.ResizeMode,
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setHeaderSectionResizeMode(int
    visual, QHeaderView::ResizeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setHeaderSectionResizeMode

    Parameters
    ----------

    visual : int
      Passed on as it is.

    mode : QHeaderView.ResizeMode
      Passed on as its number.
    """
    #  void QHeaderViewPrivate::setHeaderSectionResizeMode(int visual,
    #      QHeaderView::ResizeMode mode)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate26setHeaderSectionResizeModeEiN11QHea'
        'derView10ResizeModeE',
        visual, mode.value,
    )

  @overload(QHeaderView.ResizeMode)
  def setGlobalHeaderResizeMode(self, mode: QHeaderView.ResizeMode) -> None:
    """
    Calls Qt's 'void
    QHeaderViewPrivate::setGlobalHeaderResizeMode(QHeaderView::ResizeMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setGlobalHeaderResizeMode

    Parameters
    ----------

    mode : QHeaderView.ResizeMode
      Passed on as its number.
    """
    #  void QHeaderViewPrivate::setGlobalHeaderResizeMode(QHeaderView::
    #      ResizeMode mode)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate25setGlobalHeaderResizeModeEN11QHeade'
        'rView10ResizeModeE',
        mode.value,
    )

  @overload(QScrollBar, QAbstractItemView.ScrollMode)
  @overload(NoneType, QAbstractItemView.ScrollMode)
  def setScrollOffset(
      self,
      scrollBar: Optional[QScrollBar],
      scrollMode: QAbstractItemView.ScrollMode,
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setScrollOffset(const QScrollBar
    *scrollBar, QAbstractItemView::ScrollMode scrollMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setScrollOffset

    Parameters
    ----------

    scrollBar : Optional[QScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scrollMode : QAbstractItemView.ScrollMode
      Passed on as its number.
    """
    #  void QHeaderViewPrivate::setScrollOffset(const QScrollBar *scrollBar,
    #      QAbstractItemView::ScrollMode scrollMode)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate15setScrollOffsetEPK10QScrollBarN17QA'
        'bstractItemView10ScrollModeE',
        self._addressOf(scrollBar), scrollMode.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QHeaderViewPrivate::QHeaderViewPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHeaderViewPrivate.__init__' has no cute function yet. Qt's "
        "'QHeaderViewPrivate::QHeaderViewPrivate()': leans on "
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

  def q_func(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QHeaderViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderviewprivate.html#q_func

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QHeaderViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QHeaderViewPrivate6q_funcEv')
    return QHeaderView._cuteAt(address)

  def restoreSizeOnPrevLastSection(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::restoreSizeOnPrevLastSection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html
    """
    #  void QHeaderViewPrivate::restoreSizeOnPrevLastSection()
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate28restoreSizeOnPrevLastSectionEv',
    )

  def maybeRestorePrevLastSectionAndStretchLast(self) -> None:
    """
    Calls Qt's 'void
    QHeaderViewPrivate::maybeRestorePrevLastSectionAndStretchLast()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html
    """
    #  void QHeaderViewPrivate::maybeRestorePrevLastSectionAndStretchLast()
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate41maybeRestorePrevLastSectionAndStret'
        'chLastEv',
    )

  @overload(int)
  def sectionHandleAt(self, position: int) -> int:
    """
    Calls Qt's 'int QHeaderViewPrivate::sectionHandleAt(int position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionHandleAt

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  int QHeaderViewPrivate::sectionHandleAt(int position)
    return self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate15sectionHandleAtEi', position,
    )

  @overload(int, int)
  def setupSectionIndicator(self, section: int, position: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::setupSectionIndicator(int section,
    int position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#setupSectionIndicator

    Parameters
    ----------

    section : int
      Passed on as it is.

    position : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::setupSectionIndicator(int section, int
    #      position)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate21setupSectionIndicatorEii',
        section, position,
    )

  @overload(int, int)
  def updateSectionIndicator(self, section: int, position: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::updateSectionIndicator(int section,
    int position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#updateSectionIndicator

    Parameters
    ----------

    section : int
      Passed on as it is.

    position : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::updateSectionIndicator(int section, int
    #      position)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate22updateSectionIndicatorEii',
        section, position,
    )

  @overload(int, int)
  def updateHiddenSections(
      self,
      logicalFirst: int,
      logicalLast: int,
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::updateHiddenSections(int
    logicalFirst, int logicalLast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#updateHiddenSections

    Parameters
    ----------

    logicalFirst : int
      Passed on as it is.

    logicalLast : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::updateHiddenSections(int logicalFirst, int
    #      logicalLast)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate20updateHiddenSectionsEii',
        logicalFirst, logicalLast,
    )

  @overload(QHeaderView.ResizeMode)
  @overload(QHeaderView.ResizeMode, bool)
  def resizeSections(
      self,
      globalMode: QHeaderView.ResizeMode,
      useGlobalMode: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QHeaderViewPrivate::resizeSections(QHeaderView::ResizeMode globalMode,
    bool useGlobalMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#resizeSections

    Parameters
    ----------

    globalMode : QHeaderView.ResizeMode
      Passed on as its number.

    useGlobalMode : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QHeaderViewPrivate::resizeSections(QHeaderView::ResizeMode
    #      globalMode, bool useGlobalMode)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate14resizeSectionsEN11QHeaderView10Resi'
        'zeModeEb',
        globalMode.value, useGlobalMode,
    )

  @overload(QModelIndex, int, int)
  def sectionsRemoved(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::sectionsRemoved(const QModelIndex
    &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionsRemoved

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
    #  void QHeaderViewPrivate::sectionsRemoved(const QModelIndex &a0, int
    #      a1, int a2)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate15sectionsRemovedERK11QModelIndexii',
        self._valueOf(a0), a1, a2,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def sectionsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      logicalStart: int,
      logicalEnd: int,
      destinationParent: QModelIndex,
      logicalDestination: int,
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::sectionsAboutToBeMoved(const
    QModelIndex &sourceParent, int logicalStart, int logicalEnd, const
    QModelIndex &destinationParent, int logicalDestination)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionsAboutToBeMoved

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    logicalStart : int
      Passed on as it is.

    logicalEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    logicalDestination : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::sectionsAboutToBeMoved(const QModelIndex
    #      &sourceParent, int logicalStart, int logicalEnd, const QModelIndex
    #      &destinationParent, int logicalDestination)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate22sectionsAboutToBeMovedERK11QModelIn'
        'dexiiS2_i',
        self._valueOf(sourceParent), logicalStart, logicalEnd,
        self._valueOf(destinationParent), logicalDestination,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def sectionsMoved(
      self,
      sourceParent: QModelIndex,
      logicalStart: int,
      logicalEnd: int,
      destinationParent: QModelIndex,
      logicalDestination: int,
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::sectionsMoved(const QModelIndex
    &sourceParent, int logicalStart, int logicalEnd, const QModelIndex
    &destinationParent, int logicalDestination)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionsMoved

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    logicalStart : int
      Passed on as it is.

    logicalEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    logicalDestination : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::sectionsMoved(const QModelIndex
    #      &sourceParent, int logicalStart, int logicalEnd, const QModelIndex
    #      &destinationParent, int logicalDestination)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate13sectionsMovedERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), logicalStart, logicalEnd,
        self._valueOf(destinationParent), logicalDestination,
    )

  @overload(QList[QPersistentModelIndex])
  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def sectionsAboutToBeChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint = (
          QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint),
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::sectionsAboutToBeChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionsAboutToBeChanged

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint.
    """
    #  void QHeaderViewPrivate::sectionsAboutToBeChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate24sectionsAboutToBeChangedERK5QListI2'
        '1QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(parents), hint.value,
    )

  @overload(QList[QPersistentModelIndex])
  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def sectionsChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint = (
          QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint),
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::sectionsChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#sectionsChanged

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint.
    """
    #  void QHeaderViewPrivate::sectionsChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate15sectionsChangedERK5QListI21QPersist'
        'entModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(parents), hint.value,
    )

  def prepareSectionSelected(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::prepareSectionSelected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#prepareSectionSelected
    """
    #  void QHeaderViewPrivate::prepareSectionSelected()
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate22prepareSectionSelectedEv',
    )

  def invalidateCachedSizeHint(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::invalidateCachedSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#invalidateCachedSizeHint
    """
    #  void QHeaderViewPrivate::invalidateCachedSizeHint() const
    self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate24invalidateCachedSizeHintEv',
    )

  def initializeIndexMapping(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::initializeIndexMapping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#initializeIndexMapping
    """
    #  void QHeaderViewPrivate::initializeIndexMapping() const
    self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate22initializeIndexMappingEv',
    )

  def clearCascadingSections(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::clearCascadingSections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#clearCascadingSections
    """
    #  void QHeaderViewPrivate::clearCascadingSections()
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate22clearCascadingSectionsEv',
    )

  @overload(int, int)
  def saveCascadingSectionSize(self, visual: int, size: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::saveCascadingSectionSize(int visual,
    int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#saveCascadingSectionSize

    Parameters
    ----------

    visual : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::saveCascadingSectionSize(int visual, int
    #      size)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate24saveCascadingSectionSizeEii',
        visual, size,
    )

  def doDelayedResizeSections(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::doDelayedResizeSections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#doDelayedResizeSections
    """
    #  void QHeaderViewPrivate::doDelayedResizeSections()
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate23doDelayedResizeSectionsEv',
    )

  def executePostedResize(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::executePostedResize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#executePostedResize
    """
    #  void QHeaderViewPrivate::executePostedResize() const
    self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate19executePostedResizeEv',
    )

  def disconnectModel(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::disconnectModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#disconnectModel
    """
    #  void QHeaderViewPrivate::disconnectModel()
    self.uglySide.call('ritual_ZN18QHeaderViewPrivate15disconnectModelEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderviewprivate.html#clear
    """
    #  void QHeaderViewPrivate::clear()
    self.uglySide.call('ritual_ZN18QHeaderViewPrivate5clearEv')

  @overload(int, int)
  def cascadingResize(self, visual: int, newSize: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::cascadingResize(int visual, int
    newSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#cascadingResize

    Parameters
    ----------

    visual : int
      Passed on as it is.

    newSize : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::cascadingResize(int visual, int newSize)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate15cascadingResizeEii', visual, newSize,
    )

  def switchToFlexibleModeWithSectionMemoryUsage(self) -> None:
    """
    Calls Qt's 'void
    QHeaderViewPrivate::switchToFlexibleModeWithSectionMemoryUsage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html
    """
    #  void QHeaderViewPrivate::switchToFlexibleModeWithSectionMemoryUsage()
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate42switchToFlexibleModeWithSectionMemo'
        'ryUsageEv',
    )

  @overload(int)
  def updateCountInNoSectionItemsMode(self, newCount: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::updateCountInNoSectionItemsMode(int
    newCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html

    Parameters
    ----------

    newCount : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::updateCountInNoSectionItemsMode(int newCount)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate31updateCountInNoSectionItemsModeEi',
        newCount,
    )

  @overload(int, int, int, QHeaderView.ResizeMode)
  def createSectionItems(
      self,
      start: int,
      end: int,
      sectionSize: int,
      mode: QHeaderView.ResizeMode,
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::createSectionItems(int start, int
    end, int sectionSize, QHeaderView::ResizeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#createSectionItems

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    sectionSize : int
      Passed on as it is.

    mode : QHeaderView.ResizeMode
      Passed on as its number.
    """
    #  void QHeaderViewPrivate::createSectionItems(int start, int end, int
    #      sectionSize, QHeaderView::ResizeMode mode)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate18createSectionItemsEiiiN11QHeaderVie'
        'w10ResizeModeE',
        start, end, sectionSize, mode.value,
    )

  @overload(int, int)
  def removeSectionsFromSectionItems(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::removeSectionsFromSectionItems(int
    start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::removeSectionsFromSectionItems(int start, int
    #      end)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate30removeSectionsFromSectionItemsEii',
        start, end,
    )

  @overload(int, int, int)
  def resizeSectionItem(
      self,
      visualIndex: int,
      oldSize: int,
      newSize: int,
  ) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::resizeSectionItem(int visualIndex,
    int oldSize, int newSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#resizeSectionItem

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.

    oldSize : int
      Passed on as it is.

    newSize : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::resizeSectionItem(int visualIndex, int
    #      oldSize, int newSize)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate17resizeSectionItemEiii',
        visualIndex, oldSize, newSize,
    )

  def updateDefaultSectionSizeFromStyle(self) -> None:
    """
    Calls Qt's 'void
    QHeaderViewPrivate::updateDefaultSectionSizeFromStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html
    """
    #  void QHeaderViewPrivate::updateDefaultSectionSizeFromStyle()
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate33updateDefaultSectionSizeFromStyleEv',
    )

  def recalcSectionStartPos(self) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::recalcSectionStartPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#recalcSectionStartPos
    """
    #  void QHeaderViewPrivate::recalcSectionStartPos() const
    self.uglySide.call(
        'ritual_ZNK18QHeaderViewPrivate21recalcSectionStartPosEv',
    )

  @overload(int)
  def updateSectionsBeforeAfter(self, logical: int) -> None:
    """
    Calls Qt's 'void QHeaderViewPrivate::updateSectionsBeforeAfter(int
    logical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderviewprivate.html#updateSectionsBeforeAfter

    Parameters
    ----------

    logical : int
      Passed on as it is.
    """
    #  void QHeaderViewPrivate::updateSectionsBeforeAfter(int logical)
    self.uglySide.call(
        'ritual_ZN18QHeaderViewPrivate25updateSectionsBeforeAfterEi',
        logical,
    )

  @staticmethod
  def flipSortIndicator(*__, **_) -> Never:
    """
    Qt's 'void QHeaderViewPrivate::flipSortIndicator(int section)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'flipOrder'.
    """
    raise NotImplementedError(
        "'QHeaderViewPrivate.flipSortIndicator' has no cute function yet. "
        "Qt's 'void QHeaderViewPrivate::flipSortIndicator(int section)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'flipOrder'.")

  @staticmethod
  def getStyleOption(*__, **_) -> Never:
    """
    Qt's 'QStyleOptionHeader QHeaderViewPrivate::getStyleOption() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QHeaderViewPrivate.getStyleOption' has no cute function yet. Qt's "
        "'QStyleOptionHeader QHeaderViewPrivate::getStyleOption() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'bool QHeaderViewPrivate::read(QDataStream &in)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: invalid operands to binary expression ('QDataStream' and
    'QList<SectionItem>').
    """
    raise NotImplementedError(
        "'QHeaderViewPrivate.read' has no cute function yet. Qt's 'bool "
        "QHeaderViewPrivate::read(QDataStream &in)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: invalid operands to binary expression "
        "('QDataStream' and 'QList<SectionItem>').")

  @staticmethod
  def setHeaderMode(*__, **_) -> Never:
    """
    Qt's 'void QHeaderViewPrivate::setHeaderMode(HeaderMode mode)': names the
    enum 'HeaderMode', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QHeaderViewPrivate.setHeaderMode' has no cute function yet. Qt's "
        "'void QHeaderViewPrivate::setHeaderMode(HeaderMode mode)': names "
        "the enum 'HeaderMode', whose class cannot be named here.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void QHeaderViewPrivate::write(QDataStream &out) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: invalid operands to binary expression ('QDataStream'
    and 'QList<SectionItem>').
    """
    raise NotImplementedError(
        "'QHeaderViewPrivate.write' has no cute function yet. Qt's 'void "
        "QHeaderViewPrivate::write(QDataStream &out) const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: invalid operands to binary expression "
        "('QDataStream' and 'QList<SectionItem>').")
