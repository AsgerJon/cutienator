"""
QDockAreaLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDockAreaLayout to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from . import QMainWindow, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMainWindow = WAIT['QMainWindow']
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockAreaLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDockAreaLayout: a plain Python object standing in
  front of one C++ QDockAreaLayout.

  C++ hands a QDockAreaLayout around as a copy, so every C++ QDockAreaLayout
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDockAreaLayout that has a ritual and that Python
  can call so far, 4 names in all: 'isValid', 'constrainedRect',
  'separatorRect', 'clear'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> QDockAreaLayout::indexOfPlaceHolder(const QString
    &objectName) const': gives a type Python has no way to take yet.
  - Qt's 'QList<int> QDockAreaLayout::indexOf(const QWidget *dockWidget)
    const': gives a type Python has no way to take yet.
  - Qt's 'QLayoutItem *QDockAreaLayout::itemAt(int *x, int index) const':
    takes a number to change where it is.
  - Qt's 'QSet<QWidget *> QDockAreaLayout::usedSeparatorWidgets() const':
    gives a type Python has no way to take yet.
  - Qt's 'QDockAreaLayout::~QDockAreaLayout()': the destructor: Python
    removes its C++ QDockAreaLayout by it, and has no other use for it.

  What has no ritual
  ------------------

  39 of the 49 functions Qt declares: 16 leans on 'QDockAreaLayoutInfo; 6
  leans on 'QDockAreaLayoutItem; 4 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file; 3 leans on
  'lcQpaDockWidgets()', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken; 3 leans on 'QSize
  QDockAreaLayout; 2 leans on 'QDockWidgetGroupWindow; 2 leans on
  'QDockAreaLayout; 1 a template; 1 leans on 'operator<<(QDataStream&,
  QMainWindowLayoutState; 1 leans on 'QMainWindowLayout.

  What to expect
  --------------

  - The C++ QDockAreaLayout is created at the first use, not by
    'QDockAreaLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDockAreaLayout back gives a copy the ritual made for
    Python, in a new cute QDockAreaLayout.
  - Each name of Qt's QDockAreaLayout that has no cute function yet,
    'addDockWidget', 'apply', 'deleteAllLayoutItems', 'findSeparator',
    'fitLayout', 'gapIndex', 'gapRect', 'getGrid', 'indexOf',
    'indexOfPlaceHolder', 'info', 'insertGap', 'item', 'itemAt', 'itemRect',
    'keepSize', 'minimumSize', 'minimumStableSize', 'paintSeparators',
    'plug', 'remove', 'removePlaceHolder', 'resizeDocks',
    'restoreDockWidget', 'restoreState', 'saveState', 'separatorMove',
    'separatorRegion', 'setGrid', 'sizeHint', 'size_helper',
    'splitDockWidget', 'styleChangedEvent', 'tabifyDockWidget', 'takeAt',
    'unplug', 'updateSeparatorWidgets', 'usedSeparatorWidgets',
    'usedTabBars', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRect, QWidget)
  @overload(QRect, NoneType)
  def constrainedRect(rect: QRect, widget: Optional[QWidget]) -> QRect:
    """
    Calls Qt's 'QRect QDockAreaLayout::constrainedRect(QRect rect, QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayout.html#constrainedRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDockAreaLayout::constrainedRect(QRect rect, QWidget *widget)
    address = Rituals.call(
        'ritual_ZN15QDockAreaLayout15constrainedRectE5QRectP7QWidget',
        CuteMixin._valueOf(rect), CuteMixin._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockAreaLayout'

  #  Qt's '~QDockAreaLayout()'. Naming it makes this a value class: Python
  #  owns every C++ QDockAreaLayout behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDockAreaLayoutD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDockAreaLayout::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayout.html#isValid
    """
    #  bool QDockAreaLayout::isValid() const
    return self.uglySide.call('ritual_ZNK15QDockAreaLayout7isValidEv')

  @overload(int)
  def separatorRect(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect QDockAreaLayout::separatorRect(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayout.html#separatorRect

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDockAreaLayout::separatorRect(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QDockAreaLayout13separatorRectEi', index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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

  @overload(QMainWindow)
  @overload(NoneType)
  def __init__(self, win: Optional[QMainWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QDockAreaLayout::QDockAreaLayout(QMainWindow *win)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayout.html#QDockAreaLayout

    Parameters
    ----------

    win : Optional[QMainWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDockAreaLayout::QDockAreaLayout(QMainWindow *win)
    self._noteCreation(QDockAreaLayout, lambda: Rituals.call(
        'ritual_ZN15QDockAreaLayoutC1EP11QMainWindow', self._addressOf(win),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QDockAreaLayout::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayout.html#clear
    """
    #  void QDockAreaLayout::clear()
    self.uglySide.call('ritual_ZN15QDockAreaLayout5clearEv')

  @staticmethod
  def addDockWidget(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::addDockWidget(QInternal::DockPosition pos,
    QDockWidget *dockWidget, Qt::Orientation orientation)': leans on
    'QDockAreaLayoutInfo::remove(QList<int> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.addDockWidget' has no cute function yet. Qt's "
        "'void QDockAreaLayout::addDockWidget(QInternal::DockPosition pos, "
        "QDockWidget *dockWidget, Qt::Orientation orientation)': leans on "
        "'QDockAreaLayoutInfo::remove(QList<int> const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::apply(QWidgetAnimator::AnimationRule rule)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.apply' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::apply(QWidgetAnimator::AnimationRule rule)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout'.")

  @staticmethod
  def deleteAllLayoutItems(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::deleteAllLayoutItems()': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.deleteAllLayoutItems' has no cute function yet. "
        "Qt's 'void QDockAreaLayout::deleteAllLayoutItems()': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def findSeparator(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayout::findSeparator(const QPoint &pos)
    const': leans on 'QDockAreaLayoutInfo::separatorRect(int) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.findSeparator' has no cute function yet. Qt's "
        "'QList<int> QDockAreaLayout::findSeparator(const QPoint &pos) "
        "const': leans on 'QDockAreaLayoutInfo::separatorRect(int) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def fitLayout(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::fitLayout()': leans on
    'QDockAreaLayout::getGrid(QList<QLayoutStruct>*, QList<QLayoutStruct>*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.fitLayout' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::fitLayout()': leans on "
        "'QDockAreaLayout::getGrid(QList<QLayoutStruct>*, "
        "QList<QLayoutStruct>*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def gapIndex(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayout::gapIndex(const QPoint &pos, bool
    disallowTabs) const': leans on 'lcQpaDockWidgets()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.gapIndex' has no cute function yet. Qt's "
        "'QList<int> QDockAreaLayout::gapIndex(const QPoint &pos, bool "
        "disallowTabs) const': leans on 'lcQpaDockWidgets()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def gapRect(*__, **_) -> Never:
    """
    - Qt's 'QRect QDockAreaLayout::gapRect(const QList<int> &path) const':
      leans on 'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'QRect QDockAreaLayout::gapRect(QInternal::DockPosition dockPos)
      const': leans on 'lcQpaDockWidgets()', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.gapRect' has no cute function yet. Qt's 'QRect "
        "QDockAreaLayout::gapRect(const QList<int> &path) const': leans on "
        "'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken. Qt's 'QRect "
        "QDockAreaLayout::gapRect(QInternal::DockPosition dockPos) const': "
        "leans on 'lcQpaDockWidgets()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def getGrid(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::getGrid(QList<QLayoutStruct>
    *ver_struct_list, QList<QLayoutStruct> *hor_struct_list)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: no matching function for call to 'qMax'.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.getGrid' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::getGrid(QList<QLayoutStruct> *ver_struct_list, "
        "QList<QLayoutStruct> *hor_struct_list)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: no matching function for call to 'qMax'.")

  @staticmethod
  def indexOf(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayout::indexOf(const QWidget *dockWidget)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.indexOf' has no cute function yet. Qt's "
        "'QList<int> QDockAreaLayout::indexOf(const QWidget *dockWidget) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def indexOfPlaceHolder(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDockAreaLayout::indexOfPlaceHolder(const QString
    &objectName) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.indexOfPlaceHolder' has no cute function yet. "
        "Qt's 'QList<int> QDockAreaLayout::indexOfPlaceHolder(const QString "
        "&objectName) const': gives a type Python has no way to take yet.")

  @staticmethod
  def info(*__, **_) -> Never:
    """
    - Qt's 'QDockAreaLayoutInfo *QDockAreaLayout::info(const QList<int>
      &path)': leans on 'QDockAreaLayoutInfo::info(QList<int> const&)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'const QDockAreaLayoutInfo *QDockAreaLayout::info(const QList<int>
      &path) const': leans on 'QDockAreaLayoutInfo::info(QList<int> const&)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'QDockAreaLayoutInfo *QDockAreaLayout::info(QWidget *widget)':
      leans on 'QDockAreaLayoutInfo::info(QWidget*)', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.info' has no cute function yet. Qt's "
        "'QDockAreaLayoutInfo *QDockAreaLayout::info(const QList<int> "
        "&path)': leans on 'QDockAreaLayoutInfo::info(QList<int> const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's 'const QDockAreaLayoutInfo "
        "*QDockAreaLayout::info(const QList<int> &path) const': leans on "
        "'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken. Qt's 'QDockAreaLayoutInfo "
        "*QDockAreaLayout::info(QWidget *widget)': leans on "
        "'QDockAreaLayoutInfo::info(QWidget*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def insertGap(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayout::insertGap(const QList<int> &path, QLayoutItem
    *dockWidgetItem)': leans on 'QDockAreaLayoutInfo::insertGap(QList<int>
    const&, QLayoutItem*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.insertGap' has no cute function yet. Qt's 'bool "
        "QDockAreaLayout::insertGap(const QList<int> &path, QLayoutItem "
        "*dockWidgetItem)': leans on "
        "'QDockAreaLayoutInfo::insertGap(QList<int> const&, QLayoutItem*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def item(*__, **_) -> Never:
    """
    Qt's 'QDockAreaLayoutItem &QDockAreaLayout::item(const QList<int>
    &path)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.item' has no cute function yet. Qt's "
        "'QDockAreaLayoutItem &QDockAreaLayout::item(const QList<int> "
        "&path)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def itemAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayout::itemAt(int *x, int index) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.itemAt' has no cute function yet. Qt's "
        "'QLayoutItem *QDockAreaLayout::itemAt(int *x, int index) const': "
        "takes a number to change where it is.")

  @staticmethod
  def itemRect(*__, **_) -> Never:
    """
    Qt's 'QRect QDockAreaLayout::itemRect(const QList<int> &path) const':
    leans on 'QMainWindowLayout::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.itemRect' has no cute function yet. Qt's 'QRect "
        "QDockAreaLayout::itemRect(const QList<int> &path) const': leans on "
        "'QMainWindowLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def keepSize(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::keepSize(QDockWidget *w)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.keepSize' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::keepSize(QDockWidget *w)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def minimumSize(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayout::minimumSize() const': leans on 'QSize
    QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const>(QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const) const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.minimumSize' has no cute function yet. Qt's "
        "'QSize QDockAreaLayout::minimumSize() const': leans on 'QSize "
        "QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() "
        "const, QSize (QLayoutItem::*)() const>(QSize "
        "(QDockAreaLayoutInfo::*)() const, QSize (QLayoutItem::*)() const) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def minimumStableSize(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayout::minimumStableSize() const': leans on 'QSize
    QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const>(QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const) const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.minimumStableSize' has no cute function yet. Qt's "
        "'QSize QDockAreaLayout::minimumStableSize() const': leans on "
        "'QSize QDockAreaLayout::size_helper<QSize "
        "(QDockAreaLayoutInfo::*)() const, QSize (QLayoutItem::*)() "
        "const>(QSize (QDockAreaLayoutInfo::*)() const, QSize "
        "(QLayoutItem::*)() const) const', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def paintSeparators(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::paintSeparators(QPainter *p, QWidget *widget,
    const QRegion &clip, const QPoint &mouse) const': leans on
    'QDockAreaLayoutInfo::separatorRect(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.paintSeparators' has no cute function yet. Qt's "
        "'void QDockAreaLayout::paintSeparators(QPainter *p, QWidget "
        "*widget, const QRegion &clip, const QPoint &mouse) const': leans "
        "on 'QDockAreaLayoutInfo::separatorRect(int) const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def plug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayout::plug(const QList<int> &path)': leans
    on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.plug' has no cute function yet. Qt's 'QLayoutItem "
        "*QDockAreaLayout::plug(const QList<int> &path)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::remove(const QList<int> &path)': leans on
    'QDockAreaLayoutInfo::remove(QList<int> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.remove' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::remove(const QList<int> &path)': leans on "
        "'QDockAreaLayoutInfo::remove(QList<int> const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def removePlaceHolder(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::removePlaceHolder(const QString &name)':
    leans on 'QDockAreaLayoutInfo::remove(QList<int> const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.removePlaceHolder' has no cute function yet. Qt's "
        "'void QDockAreaLayout::removePlaceHolder(const QString &name)': "
        "leans on 'QDockAreaLayoutInfo::remove(QList<int> const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def resizeDocks(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::resizeDocks(const QList<QDockWidget *>
    &docks, const QList<int> &sizes, Qt::Orientation o)': leans on
    'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.resizeDocks' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::resizeDocks(const QList<QDockWidget *> &docks, "
        "const QList<int> &sizes, Qt::Orientation o)': leans on "
        "'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def restoreDockWidget(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayout::restoreDockWidget(QDockWidget *dockWidget)':
    leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.restoreDockWidget' has no cute function yet. Qt's "
        "'bool QDockAreaLayout::restoreDockWidget(QDockWidget "
        "*dockWidget)': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def restoreState(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayout::restoreState(QDataStream &stream, const
    QList<QDockWidget *> &_dockWidgets, QInternal::CallMode callMode)': leans
    on 'QDockAreaLayoutInfo::restoreState(QDataStream&, QList<QDockWidget*>&,
    QInternal::CallMode)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.restoreState' has no cute function yet. Qt's "
        "'bool QDockAreaLayout::restoreState(QDataStream &stream, const "
        "QList<QDockWidget *> &_dockWidgets, QInternal::CallMode "
        "callMode)': leans on "
        "'QDockAreaLayoutInfo::restoreState(QDataStream&, "
        "QList<QDockWidget*>&, QInternal::CallMode)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def saveState(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::saveState(QDataStream &stream) const': leans
    on 'operator<<(QDataStream&, QMainWindowLayoutState::StateMarkers)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.saveState' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::saveState(QDataStream &stream) const': leans on "
        "'operator<<(QDataStream&, QMainWindowLayoutState::StateMarkers)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def separatorMove(*__, **_) -> Never:
    """
    Qt's 'int QDockAreaLayout::separatorMove(const QList<int> &separator,
    const QPoint &origin, const QPoint &dest)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'separatorMoveHelper'.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.separatorMove' has no cute function yet. Qt's "
        "'int QDockAreaLayout::separatorMove(const QList<int> &separator, "
        "const QPoint &origin, const QPoint &dest)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'separatorMoveHelper'.")

  @staticmethod
  def separatorRegion(*__, **_) -> Never:
    """
    Qt's 'QRegion QDockAreaLayout::separatorRegion() const': leans on
    'QDockAreaLayoutInfo::separatorRect(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.separatorRegion' has no cute function yet. Qt's "
        "'QRegion QDockAreaLayout::separatorRegion() const': leans on "
        "'QDockAreaLayoutInfo::separatorRect(int) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setGrid(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::setGrid(QList<QLayoutStruct>
    *ver_struct_list, QList<QLayoutStruct> *hor_struct_list)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.setGrid' has no cute function yet. Qt's 'void "
        "QDockAreaLayout::setGrid(QList<QLayoutStruct> *ver_struct_list, "
        "QList<QLayoutStruct> *hor_struct_list)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def sizeHint(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayout::sizeHint() const': leans on 'QSize
    QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const>(QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const) const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.sizeHint' has no cute function yet. Qt's 'QSize "
        "QDockAreaLayout::sizeHint() const': leans on 'QSize "
        "QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() "
        "const, QSize (QLayoutItem::*)() const>(QSize "
        "(QDockAreaLayoutInfo::*)() const, QSize (QLayoutItem::*)() const) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def size_helper(*__, **_) -> Never:
    """
    Qt's 'QDockAreaLayout::size_helper': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.size_helper' has no cute function yet. Qt's "
        "'QDockAreaLayout::size_helper': a template: a pattern and no "
        "single function.")

  @staticmethod
  def splitDockWidget(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::splitDockWidget(QDockWidget *after,
    QDockWidget *dockWidget, Qt::Orientation orientation)': leans on
    'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.splitDockWidget' has no cute function yet. Qt's "
        "'void QDockAreaLayout::splitDockWidget(QDockWidget *after, "
        "QDockWidget *dockWidget, Qt::Orientation orientation)': leans on "
        "'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def styleChangedEvent(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::styleChangedEvent()': leans on
    'QDockAreaLayout::getGrid(QList<QLayoutStruct>*, QList<QLayoutStruct>*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.styleChangedEvent' has no cute function yet. Qt's "
        "'void QDockAreaLayout::styleChangedEvent()': leans on "
        "'QDockAreaLayout::getGrid(QList<QLayoutStruct>*, "
        "QList<QLayoutStruct>*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def tabifyDockWidget(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::tabifyDockWidget(QDockWidget *first,
    QDockWidget *second)': leans on 'QDockAreaLayoutInfo::info(QList<int>
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.tabifyDockWidget' has no cute function yet. Qt's "
        "'void QDockAreaLayout::tabifyDockWidget(QDockWidget *first, "
        "QDockWidget *second)': leans on "
        "'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def takeAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayout::takeAt(int *x, int index)': leans on
    'lcQpaDockWidgets()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.takeAt' has no cute function yet. Qt's "
        "'QLayoutItem *QDockAreaLayout::takeAt(int *x, int index)': leans "
        "on 'lcQpaDockWidgets()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def unplug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QDockAreaLayout::unplug(const QList<int> &path)':
    leans on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.unplug' has no cute function yet. Qt's "
        "'QLayoutItem *QDockAreaLayout::unplug(const QList<int> &path)': "
        "leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def updateSeparatorWidgets(*__, **_) -> Never:
    """
    Qt's 'void QDockAreaLayout::updateSeparatorWidgets() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.updateSeparatorWidgets' has no cute function yet. "
        "Qt's 'void QDockAreaLayout::updateSeparatorWidgets() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout'.")

  @staticmethod
  def usedSeparatorWidgets(*__, **_) -> Never:
    """
    Qt's 'QSet<QWidget *> QDockAreaLayout::usedSeparatorWidgets() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.usedSeparatorWidgets' has no cute function yet. "
        "Qt's 'QSet<QWidget *> QDockAreaLayout::usedSeparatorWidgets() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def usedTabBars(*__, **_) -> Never:
    """
    Qt's 'QSet<QTabBar *> QDockAreaLayout::usedTabBars() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayout.usedTabBars' has no cute function yet. Qt's "
        "'QSet<QTabBar *> QDockAreaLayout::usedTabBars() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
