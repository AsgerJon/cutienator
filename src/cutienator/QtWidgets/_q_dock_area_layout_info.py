"""
QDockAreaLayoutInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDockAreaLayoutInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QRegion
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockAreaLayoutInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDockAreaLayoutInfo: a plain Python object standing
  in front of one C++ QDockAreaLayoutInfo.

  C++ hands a QDockAreaLayoutInfo around as a copy, so every C++
  QDockAreaLayoutInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDockAreaLayoutInfo that has a ritual and that
  Python can call so far, 13 names in all: 'size', 'info', 'expansive',
  'separatorRect', 'clear', 'isEmpty', 'onlyHasPlaceholders', 'next', 'prev',
  'separatorRegion', 'currentTabId', 'setCurrentTab', 'setCurrentTabId'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDockAreaLayoutInfo::QDockAreaLayoutInfo(const int *_sep,
    QInternal::DockPosition _dockPos, Qt::Orientation _o, int tbhape,
    QMainWindow *window)': names 'int', which has no cute class yet.
  - Qt's 'QRect QDockAreaLayoutInfo::separatorRect(const QList<int> &path)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QDockAreaLayoutInfo::hasGapItem(const QList<int> &path)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QList<int> QDockAreaLayoutInfo::indexOf(const QWidget *widget)
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<int> QDockAreaLayoutInfo::indexOfPlaceHolder(const QString
    &objectName) const': gives a type Python has no way to take yet.
  - Qt's 'QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) const':
    takes a number to change where it is.
  - Qt's 'QSet<QWidget *> QDockAreaLayoutInfo::usedSeparatorWidgets() const':
    gives a type Python has no way to take yet.
  - Qt's 'QDockAreaLayoutInfo::~QDockAreaLayoutInfo()': the destructor:
    Python removes its C++ QDockAreaLayoutInfo by it, and has no other use
    for it.

  What has no ritual
  ------------------

  41 of the 63 functions Qt declares: 15 leans on 'QDockAreaLayoutItem; 13
  leans on 'QDockWidgetGroupWindow; 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QToolBarLayout; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied; 1 leans on 'lcQpaDockWidgets()', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QDockAreaLayoutInfo is created at the first use, not by
    'QDockAreaLayoutInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDockAreaLayoutInfo back gives a copy the ritual made
    for Python, in a new cute QDockAreaLayoutInfo.
  - Each name of Qt's QDockAreaLayoutInfo that has no cute function yet,
    'add', 'apply', 'changeSize', 'deleteAllLayoutItems', 'findSeparator',
    'fitItems', 'gapIndex', 'hasFixedSize', 'hasGapItem', 'indexOf',
    'indexOfPlaceHolder', 'insertGap', 'item', 'itemAt', 'itemRect',
    'mainWindowLayout', 'maximumSize', 'minimumSize', 'moveTab',
    'paintSeparators', 'plug', 'remove', 'reparentWidgets', 'restoreState',
    'saveState', 'separatorMove', 'setTabBarShape', 'sizeHint', 'split',
    'tab', 'tabBarMinimumSize', 'tabBarSizeHint', 'tabContentRect',
    'tabIndexToListIndex', 'takeAt', 'takeWidgetItem', 'unnest', 'unplug',
    'updateSeparatorWidgets', 'updateTabBar', 'usedSeparatorWidgets',
    'usedTabBars', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QDockAreaLayoutInfo, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class TabMode(CuteNum):
    """
    The enum 'QDockAreaLayoutInfo::TabMode' of Qt, with the 3 names Qt gives
    in it.
    """

    NoTabs = Kee[int](0)
    AllowTabs = Kee[int](1)
    ForceTabs = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockAreaLayoutInfo'

  #  Qt's '~QDockAreaLayoutInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QDockAreaLayoutInfo behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDockAreaLayoutInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QDockAreaLayoutInfo::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutinfo.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockAreaLayoutInfo::size() const
    address = self.uglySide.call('ritual_ZNK19QDockAreaLayoutInfo4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(Qt.Orientation)
  def expansive(self, o: Qt.Orientation) -> bool:
    """
    Calls Qt's 'bool QDockAreaLayoutInfo::expansive(Qt::Orientation o)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutinfo.html#expansive

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.
    """
    #  bool QDockAreaLayoutInfo::expansive(Qt::Orientation o) const
    return self.uglySide.call(
        'ritual_ZNK19QDockAreaLayoutInfo9expansiveEN2Qt11OrientationE',
        o.value,
    )

  @overload(int)
  def separatorRect(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect QDockAreaLayoutInfo::separatorRect(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutinfo.html#separatorRect

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDockAreaLayoutInfo::separatorRect(int index) const
    address = self.uglySide.call(
        'ritual_ZNK19QDockAreaLayoutInfo13separatorRectEi', index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QDockAreaLayoutInfo::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutinfo.html#isEmpty
    """
    #  bool QDockAreaLayoutInfo::isEmpty() const
    return self.uglySide.call('ritual_ZNK19QDockAreaLayoutInfo7isEmptyEv')

  def onlyHasPlaceholders(self) -> bool:
    """
    Calls Qt's 'bool QDockAreaLayoutInfo::onlyHasPlaceholders() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutinfo.html#onlyHasPlaceholders
    """
    #  bool QDockAreaLayoutInfo::onlyHasPlaceholders() const
    return self.uglySide.call(
        'ritual_ZNK19QDockAreaLayoutInfo19onlyHasPlaceholdersEv',
    )

  @overload(int)
  def next(self, idx: int) -> int:
    """
    Calls Qt's 'int QDockAreaLayoutInfo::next(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutinfo.html#next

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  int QDockAreaLayoutInfo::next(int idx) const
    return self.uglySide.call('ritual_ZNK19QDockAreaLayoutInfo4nextEi', idx)

  @overload(int)
  def prev(self, idx: int) -> int:
    """
    Calls Qt's 'int QDockAreaLayoutInfo::prev(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutinfo.html#prev

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  int QDockAreaLayoutInfo::prev(int idx) const
    return self.uglySide.call('ritual_ZNK19QDockAreaLayoutInfo4prevEi', idx)

  def separatorRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QDockAreaLayoutInfo::separatorRegion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutinfo.html#separatorRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QDockAreaLayoutInfo::separatorRegion() const
    address = self.uglySide.call(
        'ritual_ZNK19QDockAreaLayoutInfo15separatorRegionEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def currentTabId(self) -> int:
    """
    Calls Qt's 'quintptr QDockAreaLayoutInfo::currentTabId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutinfo.html#currentTabId
    """
    #  quintptr QDockAreaLayoutInfo::currentTabId() const
    return self.uglySide.call(
        'ritual_ZNK19QDockAreaLayoutInfo12currentTabIdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setCurrentTab(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDockAreaLayoutInfo::setCurrentTab(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutinfo.html#setCurrentTab

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockAreaLayoutInfo::setCurrentTab(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN19QDockAreaLayoutInfo13setCurrentTabEP7QWidget',
        self._addressOf(widget),
    )

  @overload(int)
  def setCurrentTabId(self, id: int) -> None:
    """
    Calls Qt's 'void QDockAreaLayoutInfo::setCurrentTabId(quintptr id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutinfo.html#setCurrentTabId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QDockAreaLayoutInfo::setCurrentTabId(quintptr id)
    self.uglySide.call(
        'ritual_ZN19QDockAreaLayoutInfo15setCurrentTabIdEy', id,
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
    Notes what was given, for Qt's
    'QDockAreaLayoutInfo::QDockAreaLayoutInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutinfo.html#QDockAreaLayoutInfo
    """
    #  QDockAreaLayoutInfo::QDockAreaLayoutInfo()
    self._noteCreation(QDockAreaLayoutInfo, lambda: Rituals.call(
        'ritual_ZN19QDockAreaLayoutInfoC1Ev',
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

  @overload(QWidget)
  @overload(NoneType)
  def info(self, widget: Optional[QWidget]) -> Optional[QDockAreaLayoutInfo]:
    """
    Calls Qt's 'QDockAreaLayoutInfo *QDockAreaLayoutInfo::info(QWidget
    *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutinfo.html#info

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDockAreaLayoutInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockAreaLayoutInfo *QDockAreaLayoutInfo::info(QWidget *widget)
    address = self.uglySide.call(
        'ritual_ZN19QDockAreaLayoutInfo4infoEP7QWidget',
        self._addressOf(widget),
    )
    return QDockAreaLayoutInfo._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QDockAreaLayoutInfo::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutinfo.html#clear
    """
    #  void QDockAreaLayoutInfo::clear()
    self.uglySide.call('ritual_ZN19QDockAreaLayoutInfo5clearEv')

  @staticmethod
  def add(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::add(QWidget *widget)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.add' has no cute function yet. Qt's 'void "
        "QDockAreaLayoutInfo::add(QWidget *widget)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'QDockWidget
    *QDockAreaLayoutInfo::apply(QWidgetAnimator::AnimationRule rule)': leans
    on 'QToolBarLayout::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.apply' has no cute function yet. Qt's "
        "'QDockWidget "
        "*QDockAreaLayoutInfo::apply(QWidgetAnimator::AnimationRule rule)': "
        "leans on 'QToolBarLayout::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def changeSize(*__, **_) -> Never:
    """
    Qt's 'int QDockAreaLayoutInfo::changeSize(int index, int size, bool
    below)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.changeSize' has no cute function yet. Qt's "
        "'int QDockAreaLayoutInfo::changeSize(int index, int size, bool "
        "below)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def deleteAllLayoutItems(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::deleteAllLayoutItems()': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.deleteAllLayoutItems' has no cute function "
        "yet. Qt's 'void QDockAreaLayoutInfo::deleteAllLayoutItems()': "
        "leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def findSeparator(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayoutInfo::findSeparator(const QPoint &pos)
    const': leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.findSeparator' has no cute function yet. Qt's "
        "'QList<int> QDockAreaLayoutInfo::findSeparator(const QPoint &pos) "
        "const': leans on 'QDockWidgetGroupWindow::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def fitItems(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::fitItems()': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.fitItems' has no cute function yet. Qt's "
        "'void QDockAreaLayoutInfo::fitItems()': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def gapIndex(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayoutInfo::gapIndex(const QPoint &pos, bool
    nestingEnabled, TabMode tabMode) const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.gapIndex' has no cute function yet. Qt's "
        "'QList<int> QDockAreaLayoutInfo::gapIndex(const QPoint &pos, bool "
        "nestingEnabled, TabMode tabMode) const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def hasFixedSize(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayoutInfo::hasFixedSize() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.hasFixedSize' has no cute function yet. Qt's "
        "'bool QDockAreaLayoutInfo::hasFixedSize() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def hasGapItem(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayoutInfo::hasGapItem(const QList<int> &path)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.hasGapItem' has no cute function yet. Qt's "
        "'bool QDockAreaLayoutInfo::hasGapItem(const QList<int> &path) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def indexOf(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayoutInfo::indexOf(const QWidget *widget)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.indexOf' has no cute function yet. Qt's "
        "'QList<int> QDockAreaLayoutInfo::indexOf(const QWidget *widget) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def indexOfPlaceHolder(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayoutInfo::indexOfPlaceHolder(const QString
    &objectName) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.indexOfPlaceHolder' has no cute function yet. "
        "Qt's 'QList<int> QDockAreaLayoutInfo::indexOfPlaceHolder(const "
        "QString &objectName) const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def insertGap(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayoutInfo::insertGap(const QList<int> &path,
    QLayoutItem *dockWidgetItem)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'dockedGeometry'.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.insertGap' has no cute function yet. Qt's "
        "'bool QDockAreaLayoutInfo::insertGap(const QList<int> &path, "
        "QLayoutItem *dockWidgetItem)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'dockedGeometry'.")

  @staticmethod
  def item(*__, **_) -> Never:
    """
    Qt's 'QDockAreaLayoutItem &QDockAreaLayoutInfo::item(const QList<int>
    &path)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.item' has no cute function yet. Qt's "
        "'QDockAreaLayoutItem &QDockAreaLayoutInfo::item(const QList<int> "
        "&path)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def itemAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.itemAt' has no cute function yet. Qt's "
        "'QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) "
        "const': takes a number to change where it is.")

  @staticmethod
  def itemRect(*__, **_) -> Never:
    """
    - Qt's 'QRect QDockAreaLayoutInfo::itemRect(int index, bool isGap)
      const': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: use of undeclared identifier
      'tabId'.
    - Qt's 'QRect QDockAreaLayoutInfo::itemRect(const QList<int> &path)
      const': leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.itemRect' has no cute function yet. Qt's "
        "'QRect QDockAreaLayoutInfo::itemRect(int index, bool isGap) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'tabId'. Qt's 'QRect "
        "QDockAreaLayoutInfo::itemRect(const QList<int> &path) const': "
        "leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def mainWindowLayout(*__, **_) -> Never:
    """
    Qt's 'QMainWindowLayout *QDockAreaLayoutInfo::mainWindowLayout() const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.mainWindowLayout' has no cute function yet. "
        "Qt's 'QMainWindowLayout *QDockAreaLayoutInfo::mainWindowLayout() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qt_mainwindow_layout'.")

  @staticmethod
  def maximumSize(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutInfo::maximumSize() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.maximumSize' has no cute function yet. Qt's "
        "'QSize QDockAreaLayoutInfo::maximumSize() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def minimumSize(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutInfo::minimumSize() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.minimumSize' has no cute function yet. Qt's "
        "'QSize QDockAreaLayoutInfo::minimumSize() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def moveTab(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::moveTab(int from, int to)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.moveTab' has no cute function yet. Qt's 'void "
        "QDockAreaLayoutInfo::moveTab(int from, int to)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def paintSeparators(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::paintSeparators(QPainter *p, QWidget
    *widget, const QRegion &clip, const QPoint &mouse) const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.paintSeparators' has no cute function yet. "
        "Qt's 'void QDockAreaLayoutInfo::paintSeparators(QPainter *p, "
        "QWidget *widget, const QRegion &clip, const QPoint &mouse) const': "
        "leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def plug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayoutInfo::plug(const QList<int> &path)':
    leans on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.plug' has no cute function yet. Qt's "
        "'QLayoutItem *QDockAreaLayoutInfo::plug(const QList<int> &path)': "
        "leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    - Qt's 'void QDockAreaLayoutInfo::remove(const QList<int> &path)': leans
      on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    - Qt's 'void QDockAreaLayoutInfo::remove(QWidget *widget)': leans on
      'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.remove' has no cute function yet. Qt's 'void "
        "QDockAreaLayoutInfo::remove(const QList<int> &path)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's 'void "
        "QDockAreaLayoutInfo::remove(QWidget *widget)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def reparentWidgets(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::reparentWidgets(QWidget *p)': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.reparentWidgets' has no cute function yet. "
        "Qt's 'void QDockAreaLayoutInfo::reparentWidgets(QWidget *p)': "
        "leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def restoreState(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayoutInfo::restoreState(QDataStream &stream,
    QList<QDockWidget *> &widgets, QInternal::CallMode a2)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'StateMarkers'; did you mean
    'QMainWindowLayoutState::StateMarkers'?.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.restoreState' has no cute function yet. Qt's "
        "'bool QDockAreaLayoutInfo::restoreState(QDataStream &stream, "
        "QList<QDockWidget *> &widgets, QInternal::CallMode a2)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'StateMarkers'; did you mean "
        "'QMainWindowLayoutState::StateMarkers'?.")

  @staticmethod
  def saveState(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::saveState(QDataStream &stream) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'StateMarkers';
    did you mean 'QMainWindowLayoutState::StateMarkers'?.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.saveState' has no cute function yet. Qt's "
        "'void QDockAreaLayoutInfo::saveState(QDataStream &stream) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'StateMarkers'; did you mean "
        "'QMainWindowLayoutState::StateMarkers'?.")

  @staticmethod
  def separatorMove(*__, **_) -> Never:
    """
    - Qt's 'int QDockAreaLayoutInfo::separatorMove(int index, int delta)':
      Qt's library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'separatorMoveHelper'.
    - Qt's 'int QDockAreaLayoutInfo::separatorMove(const QList<int>
      &separator, const QPoint &origin, const QPoint &dest)': leans on
      'QToolBarLayout::staticMetaObject', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.separatorMove' has no cute function yet. Qt's "
        "'int QDockAreaLayoutInfo::separatorMove(int index, int delta)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'separatorMoveHelper'. Qt's 'int "
        "QDockAreaLayoutInfo::separatorMove(const QList<int> &separator, "
        "const QPoint &origin, const QPoint &dest)': leans on "
        "'QToolBarLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setTabBarShape(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::setTabBarShape(int shape)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.setTabBarShape' has no cute function yet. "
        "Qt's 'void QDockAreaLayoutInfo::setTabBarShape(int shape)': leans "
        "on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def sizeHint(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutInfo::sizeHint() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.sizeHint' has no cute function yet. Qt's "
        "'QSize QDockAreaLayoutInfo::sizeHint() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def split(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::split(int index, Qt::Orientation
    orientation, QLayoutItem *dockWidgetItem)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.split' has no cute function yet. Qt's 'void "
        "QDockAreaLayoutInfo::split(int index, Qt::Orientation orientation, "
        "QLayoutItem *dockWidgetItem)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def tab(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::tab(int index, QLayoutItem
    *dockWidgetItem)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.tab' has no cute function yet. Qt's 'void "
        "QDockAreaLayoutInfo::tab(int index, QLayoutItem *dockWidgetItem)': "
        "leans on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def tabBarMinimumSize(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutInfo::tabBarMinimumSize() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.tabBarMinimumSize' has no cute function yet. "
        "Qt's 'QSize QDockAreaLayoutInfo::tabBarMinimumSize() const': leans "
        "on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def tabBarSizeHint(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutInfo::tabBarSizeHint() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.tabBarSizeHint' has no cute function yet. "
        "Qt's 'QSize QDockAreaLayoutInfo::tabBarSizeHint() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def tabContentRect(*__, **_) -> Never:
    """
    Qt's 'QRect QDockAreaLayoutInfo::tabContentRect() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.tabContentRect' has no cute function yet. "
        "Qt's 'QRect QDockAreaLayoutInfo::tabContentRect() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def tabIndexToListIndex(*__, **_) -> Never:
    """
    Qt's 'int QDockAreaLayoutInfo::tabIndexToListIndex(int a0) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'tabId'.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.tabIndexToListIndex' has no cute function "
        "yet. Qt's 'int QDockAreaLayoutInfo::tabIndexToListIndex(int a0) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'tabId'.")

  @staticmethod
  def takeAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayoutInfo::takeAt(int *x, int index)': leans
    on 'lcQpaDockWidgets()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.takeAt' has no cute function yet. Qt's "
        "'QLayoutItem *QDockAreaLayoutInfo::takeAt(int *x, int index)': "
        "leans on 'lcQpaDockWidgets()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def takeWidgetItem(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QLayoutItem>
    QDockAreaLayoutInfo::takeWidgetItem(QWidget *widget)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.takeWidgetItem' has no cute function yet. "
        "Qt's 'std::unique_ptr<QLayoutItem> "
        "QDockAreaLayoutInfo::takeWidgetItem(QWidget *widget)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def unnest(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::unnest(int index)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.unnest' has no cute function yet. Qt's 'void "
        "QDockAreaLayoutInfo::unnest(int index)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def unplug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayoutInfo::unplug(const QList<int> &path)':
    leans on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.unplug' has no cute function yet. Qt's "
        "'QLayoutItem *QDockAreaLayoutInfo::unplug(const QList<int> "
        "&path)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def updateSeparatorWidgets(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayoutInfo::updateSeparatorWidgets() const': leans on
    'QToolBarLayout::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.updateSeparatorWidgets' has no cute function "
        "yet. Qt's 'void QDockAreaLayoutInfo::updateSeparatorWidgets() "
        "const': leans on 'QToolBarLayout::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateTabBar(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayoutInfo::updateTabBar() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'tabId'.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.updateTabBar' has no cute function yet. Qt's "
        "'bool QDockAreaLayoutInfo::updateTabBar() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'tabId'.")

  @staticmethod
  def usedSeparatorWidgets(*__, **_) -> Never:
    """
    Qt's 'QSet<QWidget *> QDockAreaLayoutInfo::usedSeparatorWidgets() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.usedSeparatorWidgets' has no cute function "
        "yet. Qt's 'QSet<QWidget *> "
        "QDockAreaLayoutInfo::usedSeparatorWidgets() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def usedTabBars(*__, **_) -> Never:
    """
    Qt's 'QSet<QTabBar *> QDockAreaLayoutInfo::usedTabBars() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutInfo.usedTabBars' has no cute function yet. Qt's "
        "'QSet<QTabBar *> QDockAreaLayoutInfo::usedTabBars() const': leans "
        "on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
