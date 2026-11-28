"""
QMainWindowLayoutState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QMainWindowLayoutState to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMainWindowLayoutState(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMainWindowLayoutState: a plain Python object
  standing in front of one C++ QMainWindowLayoutState.

  C++ hands a QMainWindowLayoutState around as a copy, so every C++
  QMainWindowLayoutState behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMainWindowLayoutState that has a ritual and that
  Python can call so far, 6 names in all: 'deleteCentralWidgetItem',
  'contains', 'setCentralWidget', 'centralWidget', 'clear', 'isValid'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayoutItem *QMainWindowLayoutState::itemAt(int index, int *x)
    const': takes a number to change where it is.
  - Qt's 'QMainWindowLayoutState::~QMainWindowLayoutState()': the destructor:
    Python removes its C++ QMainWindowLayoutState by it, and has no other use
    for it.

  What has no ritual
  ------------------

  24 of the 32 functions Qt declares: 5 leans on 'QDockWidgetGroupWindow; 4
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 4 leans on 'QDockAreaLayoutItem; 3 leans on 'QDockAreaLayout; 3
  leans on 'QSize QDockAreaLayout; 2 leans on 'QToolBarAreaLayout; 1 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 1 leans on 'operator>>(QDataStream&,
  QMainWindowLayoutState; 1 leans on 'lcQpaDockWidgets()', which Qt's source
  does not mark for use from outside Qt and has no code for that could be
  taken.

  What to expect
  --------------

  - The C++ QMainWindowLayoutState is created at the first use, not by
    'QMainWindowLayoutState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMainWindowLayoutState back gives a copy the ritual
    made for Python, in a new cute QMainWindowLayoutState.
  - Each name of Qt's QMainWindowLayoutState that has no cute function yet,
    '__init__', 'apply', 'checkFormat', 'deleteAllLayoutItems', 'fitLayout',
    'fits', 'gapIndex', 'gapRect', 'indexOf', 'insertGap', 'item', 'itemAt',
    'itemRect', 'minimumSize', 'plug', 'remove', 'restoreState', 'saveState',
    'sizeHint', 'takeAt', 'unplug', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMainWindowLayoutState, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class StateMarkers(CuteNum, scoped=True):
    """
    The enum 'QMainWindowLayoutState::StateMarkers' of Qt, with the 7 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    FloatingDockWidgetTab = Kee[int](249)
    Tab = Kee[int](250)
    Widget = Kee[int](251)
    Sequence = Kee[int](252)
    ToolBarEx = Kee[int](252)
    DockWidget = Kee[int](253)
    ToolBar = Kee[int](254)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMainWindowLayoutState'

  #  Qt's '~QMainWindowLayoutState()'. Naming it makes this a value class:
  #  Python owns every C++ QMainWindowLayoutState behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QMainWindowLayoutStateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def contains(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QMainWindowLayoutState::contains(QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayoutstate.html#contains

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMainWindowLayoutState::contains(QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK22QMainWindowLayoutState8containsEP7QWidget',
        self._addressOf(widget),
    )

  def centralWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMainWindowLayoutState::centralWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayoutstate.html#centralWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMainWindowLayoutState::centralWidget() const
    address = self.uglySide.call(
        'ritual_ZNK22QMainWindowLayoutState13centralWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMainWindowLayoutState::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayoutstate.html#isValid
    """
    #  bool QMainWindowLayoutState::isValid() const
    return self.uglySide.call('ritual_ZNK22QMainWindowLayoutState7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setCentralWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QMainWindowLayoutState::setCentralWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayoutstate.html#setCentralWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayoutState::setCentralWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN22QMainWindowLayoutState16setCentralWidgetEP7QWidget',
        self._addressOf(widget),
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
    Qt's 'QMainWindowLayoutState::QMainWindowLayoutState(QMainWindow *win)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.__init__' has no cute function yet. Qt's "
        "'QMainWindowLayoutState::QMainWindowLayoutState(QMainWindow "
        "*win)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

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

  def deleteCentralWidgetItem(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayoutState::deleteCentralWidgetItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayoutstate.html
    """
    #  void QMainWindowLayoutState::deleteCentralWidgetItem()
    self.uglySide.call(
        'ritual_ZN22QMainWindowLayoutState23deleteCentralWidgetItemEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayoutState::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayoutstate.html#clear
    """
    #  void QMainWindowLayoutState::clear()
    self.uglySide.call('ritual_ZN22QMainWindowLayoutState5clearEv')

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayoutState::apply(QWidgetAnimator::AnimationRule
    rule)': leans on
    'QDockAreaLayout::apply(QWidgetAnimator::AnimationRule)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.apply' has no cute function yet. Qt's "
        "'void QMainWindowLayoutState::apply(QWidgetAnimator::AnimationRule "
        "rule)': leans on "
        "'QDockAreaLayout::apply(QWidgetAnimator::AnimationRule)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def checkFormat(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayoutState::checkFormat(QDataStream &stream)':
    leans on 'operator>>(QDataStream&,
    QMainWindowLayoutState::StateMarkers&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.checkFormat' has no cute function yet. "
        "Qt's 'bool QMainWindowLayoutState::checkFormat(QDataStream "
        "&stream)': leans on 'operator>>(QDataStream&, "
        "QMainWindowLayoutState::StateMarkers&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def deleteAllLayoutItems(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayoutState::deleteAllLayoutItems()': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.deleteAllLayoutItems' has no cute function "
        "yet. Qt's 'void QMainWindowLayoutState::deleteAllLayoutItems()': "
        "leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def fitLayout(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayoutState::fitLayout()': leans on
    'QDockAreaLayout::getGrid(QList<QLayoutStruct>*, QList<QLayoutStruct>*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.fitLayout' has no cute function yet. Qt's "
        "'void QMainWindowLayoutState::fitLayout()': leans on "
        "'QDockAreaLayout::getGrid(QList<QLayoutStruct>*, "
        "QList<QLayoutStruct>*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def fits(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayoutState::fits() const': leans on 'QSize
    QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const>(QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const) const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.fits' has no cute function yet. Qt's 'bool "
        "QMainWindowLayoutState::fits() const': leans on 'QSize "
        "QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() "
        "const, QSize (QLayoutItem::*)() const>(QSize "
        "(QDockAreaLayoutInfo::*)() const, QSize (QLayoutItem::*)() const) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def gapIndex(*__, **_) -> Never:
    """
    Qt's 'QList<int> QMainWindowLayoutState::gapIndex(QWidget *widget, const
    QPoint &pos) const': leans on 'QDockWidgetGroupWindow::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.gapIndex' has no cute function yet. Qt's "
        "'QList<int> QMainWindowLayoutState::gapIndex(QWidget *widget, "
        "const QPoint &pos) const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def gapRect(*__, **_) -> Never:
    """
    Qt's 'QRect QMainWindowLayoutState::gapRect(const QList<int> &path)
    const': leans on 'QDockAreaLayout::gapRect(QList<int> const&) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.gapRect' has no cute function yet. Qt's "
        "'QRect QMainWindowLayoutState::gapRect(const QList<int> &path) "
        "const': leans on 'QDockAreaLayout::gapRect(QList<int> const&) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def indexOf(*__, **_) -> Never:
    """
    Qt's 'QList<int> QMainWindowLayoutState::indexOf(QWidget *widget) const':
    leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.indexOf' has no cute function yet. Qt's "
        "'QList<int> QMainWindowLayoutState::indexOf(QWidget *widget) "
        "const': leans on 'QDockWidgetGroupWindow::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def insertGap(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayoutState::insertGap(const QList<int> &path,
    QLayoutItem *item)': leans on 'QDockWidgetGroupWindow::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.insertGap' has no cute function yet. Qt's "
        "'bool QMainWindowLayoutState::insertGap(const QList<int> &path, "
        "QLayoutItem *item)': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def item(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QMainWindowLayoutState::item(const QList<int> &path)':
    leans on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.item' has no cute function yet. Qt's "
        "'QLayoutItem *QMainWindowLayoutState::item(const QList<int> "
        "&path)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def itemAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QMainWindowLayoutState::itemAt(int index, int *x)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.itemAt' has no cute function yet. Qt's "
        "'QLayoutItem *QMainWindowLayoutState::itemAt(int index, int *x) "
        "const': takes a number to change where it is.")

  @staticmethod
  def itemRect(*__, **_) -> Never:
    """
    Qt's 'QRect QMainWindowLayoutState::itemRect(const QList<int> &path)
    const': leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.itemRect' has no cute function yet. Qt's "
        "'QRect QMainWindowLayoutState::itemRect(const QList<int> &path) "
        "const': leans on 'QDockWidgetGroupWindow::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def minimumSize(*__, **_) -> Never:
    """
    Qt's 'QSize QMainWindowLayoutState::minimumSize() const': leans on 'QSize
    QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const>(QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const) const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.minimumSize' has no cute function yet. "
        "Qt's 'QSize QMainWindowLayoutState::minimumSize() const': leans on "
        "'QSize QDockAreaLayout::size_helper<QSize "
        "(QDockAreaLayoutInfo::*)() const, QSize (QLayoutItem::*)() "
        "const>(QSize (QDockAreaLayoutInfo::*)() const, QSize "
        "(QLayoutItem::*)() const) const', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def plug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QMainWindowLayoutState::plug(const QList<int> &path)':
    leans on 'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.plug' has no cute function yet. Qt's "
        "'QLayoutItem *QMainWindowLayoutState::plug(const QList<int> "
        "&path)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    - Qt's 'void QMainWindowLayoutState::remove(const QList<int> &path)':
      leans on 'QToolBarAreaLayout::remove(QList<int> const&)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'void QMainWindowLayoutState::remove(QLayoutItem *item)': leans on
      'QToolBarAreaLayout::remove(QLayoutItem*)', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.remove' has no cute function yet. Qt's "
        "'void QMainWindowLayoutState::remove(const QList<int> &path)': "
        "leans on 'QToolBarAreaLayout::remove(QList<int> const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'void "
        "QMainWindowLayoutState::remove(QLayoutItem *item)': leans on "
        "'QToolBarAreaLayout::remove(QLayoutItem*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def restoreState(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayoutState::restoreState(QDataStream &stream,
    const QMainWindowLayoutState &oldState)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.restoreState' has no cute function yet. "
        "Qt's 'bool QMainWindowLayoutState::restoreState(QDataStream "
        "&stream, const QMainWindowLayoutState &oldState)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout'.")

  @staticmethod
  def saveState(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayoutState::saveState(QDataStream &stream) const':
    leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.saveState' has no cute function yet. Qt's "
        "'void QMainWindowLayoutState::saveState(QDataStream &stream) "
        "const': leans on 'QDockWidgetGroupWindow::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sizeHint(*__, **_) -> Never:
    """
    Qt's 'QSize QMainWindowLayoutState::sizeHint() const': leans on 'QSize
    QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const>(QSize (QDockAreaLayoutInfo::*)() const,
    QSize (QLayoutItem::*)() const) const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.sizeHint' has no cute function yet. Qt's "
        "'QSize QMainWindowLayoutState::sizeHint() const': leans on 'QSize "
        "QDockAreaLayout::size_helper<QSize (QDockAreaLayoutInfo::*)() "
        "const, QSize (QLayoutItem::*)() const>(QSize "
        "(QDockAreaLayoutInfo::*)() const, QSize (QLayoutItem::*)() const) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def takeAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QMainWindowLayoutState::takeAt(int index, int *x)':
    leans on 'lcQpaDockWidgets()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.takeAt' has no cute function yet. Qt's "
        "'QLayoutItem *QMainWindowLayoutState::takeAt(int index, int *x)': "
        "leans on 'lcQpaDockWidgets()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def unplug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QMainWindowLayoutState::unplug(const QList<int> &path,
    QMainWindowLayoutState *savedState)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayoutState.unplug' has no cute function yet. Qt's "
        "'QLayoutItem *QMainWindowLayoutState::unplug(const QList<int> "
        "&path, QMainWindowLayoutState *savedState)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
