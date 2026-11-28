"""
QDockWidgetGroupWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDockWidgetGroupWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChildEvent, QEvent, QMetaObject
  from ..QtGui import QPaintEvent
  from . import QDockAreaLayoutInfo, QDockWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChildEvent = WAIT['QChildEvent']
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockWidgetGroupWindow(QWidget):
  """
  The cute side of Qt's QDockWidgetGroupWindow: a plain Python object
  standing in front of one C++ QDockWidgetGroupWindow.

  It is built on the cute 'QWidget', as Qt's QDockWidgetGroupWindow is built
  on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDockWidgetGroupWindow that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'layoutInfo',
  'tabLayoutInfo', 'activeTabbedDockWidget', 'hasVisibleDockWidgets',
  'hasNativeDecos', 'childEvent', 'dockWidgets', 'resized', 'event',
  'eventFilter', 'paintEvent'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDockWidgetGroupWindow::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDockWidgetGroupWindow::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  12 of the 26 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QDockWidgetGroupWindow; 1 leans on 'vtable for
  QDockWidgetGroupWindow', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'QDockAreaLayoutInfo.

  What to expect
  --------------

  - The C++ QDockWidgetGroupWindow is created at the first use, not by
    'QDockWidgetGroupWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDockWidgetGroupWindow.
  - Qt tells when it has removed the C++ QDockWidgetGroupWindow. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDockWidgetGroupWindow that has no cute function yet,
    '__init__', 'adjustFlags', 'apply', 'destroyIfSingleItemLeft',
    'destroyOrHideIfEmpty', 'hover', 'reparentToMainWindow', 'restore',
    'updateCurrentGapRect', holds a function that raises
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
  __qt_class__ = 'QDockWidgetGroupWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDockWidgetGroupWindow::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDockWidgetGroupWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def layoutInfo(self) -> Optional[QDockAreaLayoutInfo]:
    """
    Calls Qt's 'QDockAreaLayoutInfo *QDockWidgetGroupWindow::layoutInfo()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#layoutInfo

    Returns
    -------

    Optional[QDockAreaLayoutInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockAreaLayoutInfo *QDockWidgetGroupWindow::layoutInfo() const
    address = self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow10layoutInfoEv',
    )
    from . import QDockAreaLayoutInfo
    return QDockAreaLayoutInfo._cuteAt(address)

  def tabLayoutInfo(self) -> Optional[QDockAreaLayoutInfo]:
    """
    Calls Qt's 'const QDockAreaLayoutInfo
    *QDockWidgetGroupWindow::tabLayoutInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#tabLayoutInfo

    Returns
    -------

    Optional[QDockAreaLayoutInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDockAreaLayoutInfo *QDockWidgetGroupWindow::tabLayoutInfo()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow13tabLayoutInfoEv',
    )
    from . import QDockAreaLayoutInfo
    return QDockAreaLayoutInfo._cuteAt(address)

  def activeTabbedDockWidget(self) -> Optional[QDockWidget]:
    """
    Calls Qt's 'QDockWidget *QDockWidgetGroupWindow::activeTabbedDockWidget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#activeTabbedDockWidget

    Returns
    -------

    Optional[QDockWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockWidget *QDockWidgetGroupWindow::activeTabbedDockWidget() const
    address = self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow22activeTabbedDockWidgetEv',
    )
    from . import QDockWidget
    return QDockWidget._cuteAt(address)

  def hasVisibleDockWidgets(self) -> bool:
    """
    Calls Qt's 'bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#hasVisibleDockWidgets
    """
    #  bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const
    return self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow21hasVisibleDockWidgetsEv',
    )

  def hasNativeDecos(self) -> bool:
    """
    Calls Qt's 'bool QDockWidgetGroupWindow::hasNativeDecos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#hasNativeDecos
    """
    #  bool QDockWidgetGroupWindow::hasNativeDecos() const
    return self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow14hasNativeDecosEv',
    )

  def dockWidgets(self) -> QList[QDockWidget]:
    """
    Calls Qt's 'QList<QDockWidget *> QDockWidgetGroupWindow::dockWidgets()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#dockWidgets

    Returns
    -------

    QList[QDockWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDockWidget *> QDockWidgetGroupWindow::dockWidgets() const
    address = self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow11dockWidgetsEv',
    )
    from . import QDockWidget
    return QList[QDockWidget]._cuteOwning(address)

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
    Qt's 'QDockWidgetGroupWindow::QDockWidgetGroupWindow(QWidget *parent,
    Qt::WindowFlags f)': leans on 'vtable for QDockWidgetGroupWindow', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.__init__' has no cute function yet. Qt's "
        "'QDockWidgetGroupWindow::QDockWidgetGroupWindow(QWidget *parent, "
        "Qt::WindowFlags f)': leans on 'vtable for QDockWidgetGroupWindow', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QChildEvent)
  @overload(NoneType)
  def childEvent(self, event: Optional[QChildEvent]) -> None:
    """
    Calls Qt's 'void QDockWidgetGroupWindow::childEvent(QChildEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#childEvent

    Parameters
    ----------

    event : Optional[QChildEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidgetGroupWindow::childEvent(QChildEvent *event)
    self.uglySide.call(
        'ritual_ZN22QDockWidgetGroupWindow10childEventEP11QChildEvent',
        self._addressOf(event),
    )

  def resized(self) -> None:
    """
    Calls Qt's 'void QDockWidgetGroupWindow::resized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#resized
    """
    #  void QDockWidgetGroupWindow::resized()
    self.uglySide.call('ritual_ZN22QDockWidgetGroupWindow7resizedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QDockWidgetGroupWindow::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDockWidgetGroupWindow::event(QEvent *a0)
    return self.uglySide.call(
        'ritual_ZN22QDockWidgetGroupWindow5eventEP6QEvent',
        self._addressOf(a0),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      obj: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#eventFilter

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN22QDockWidgetGroupWindow11eventFilterEP7QObjectP6QEvent',
        self._addressOf(obj, 'QObject'), self._addressOf(event),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QDockWidgetGroupWindow::paintEvent(QPaintEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidgetGroupWindow::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN22QDockWidgetGroupWindow10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QDockWidgetGroupWindow10paintEventEP11QPaintEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def adjustFlags(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetGroupWindow::adjustFlags()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'QDockWidgetGroupLayout'; did you mean
    'QDockWidgetLayout'?.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.adjustFlags' has no cute function yet. "
        "Qt's 'void QDockWidgetGroupWindow::adjustFlags()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'QDockWidgetGroupLayout'; "
        "did you mean 'QDockWidgetLayout'?.")

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetGroupWindow::apply()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'QDockWidgetGroupLayout'; did you mean
    'QDockWidgetLayout'?.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.apply' has no cute function yet. Qt's "
        "'void QDockWidgetGroupWindow::apply()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: unknown type name 'QDockWidgetGroupLayout'; did you mean "
        "'QDockWidgetLayout'?.")

  @staticmethod
  def destroyIfSingleItemLeft(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetGroupWindow::destroyIfSingleItemLeft()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.destroyIfSingleItemLeft' has no cute "
        "function yet. Qt's 'void "
        "QDockWidgetGroupWindow::destroyIfSingleItemLeft()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout'.")

  @staticmethod
  def destroyOrHideIfEmpty(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetGroupWindow::destroyOrHideIfEmpty()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.destroyOrHideIfEmpty' has no cute function "
        "yet. Qt's 'void QDockWidgetGroupWindow::destroyOrHideIfEmpty()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout'.")

  @staticmethod
  def hover(*__, **_) -> Never:
    """
    Qt's 'bool QDockWidgetGroupWindow::hover(QLayoutItem *widgetItem, const
    QPoint &mousePos)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'QDockWidgetGroupLayout'; did you mean 'QDockWidgetLayout'?.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.hover' has no cute function yet. Qt's "
        "'bool QDockWidgetGroupWindow::hover(QLayoutItem *widgetItem, const "
        "QPoint &mousePos)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: unknown type "
        "name 'QDockWidgetGroupLayout'; did you mean 'QDockWidgetLayout'?.")

  @staticmethod
  def reparentToMainWindow(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetGroupWindow::reparentToMainWindow(QDockWidget
    *dockWidget)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.reparentToMainWindow' has no cute function "
        "yet. Qt's 'void "
        "QDockWidgetGroupWindow::reparentToMainWindow(QDockWidget "
        "*dockWidget)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qt_mainwindow_layout'.")

  @staticmethod
  def restore(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetGroupWindow::restore()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'QDockWidgetGroupLayout'; did you mean
    'QDockWidgetLayout'?.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.restore' has no cute function yet. Qt's "
        "'void QDockWidgetGroupWindow::restore()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: unknown type name 'QDockWidgetGroupLayout'; did you mean "
        "'QDockWidgetLayout'?.")

  @staticmethod
  def updateCurrentGapRect(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetGroupWindow::updateCurrentGapRect()': leans on
    'QDockAreaLayoutInfo::info(QList<int> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockWidgetGroupWindow.updateCurrentGapRect' has no cute function "
        "yet. Qt's 'void QDockWidgetGroupWindow::updateCurrentGapRect()': "
        "leans on 'QDockAreaLayoutInfo::info(QList<int> const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
