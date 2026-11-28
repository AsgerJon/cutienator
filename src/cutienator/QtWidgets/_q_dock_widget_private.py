"""
QDockWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDockWidgetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QInternal
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QResizeEvent
  from . import QDockWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockWidgetPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QDockWidgetPrivate: a plain Python object standing in
  front of one C++ QDockWidgetPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QDockWidgetPrivate is
  built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDockWidgetPrivate that has a ritual and that Python
  can call so far, 5 names in all: 'q_func', 'toggleView', 'toggleTopLevel',
  'toDockWidgetArea', 'recalculatePressPos'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDockWidget *QDockWidgetPrivate::q_func() const': takes in
    Python what 'QDockWidget *QDockWidgetPrivate::q_func()' takes.

  What has no ritual
  ------------------

  18 of the 24 functions Qt declares: 13 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QDockWidgetPrivate; 1 leans on 'QDockWidgetGroupWindow; 1 leans on
  'QWidgetResizeHandler.

  What to expect
  --------------

  - The C++ QDockWidgetPrivate is created at the first use, not by
    'QDockWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDockWidgetPrivate.
  - Each name of Qt's QDockWidgetPrivate that has no cute function yet,
    'endDrag', 'initDrag', 'isAnimating', 'isTabbed',
    'mouseDoubleClickEvent', 'mouseMoveEvent', 'mousePressEvent',
    'mouseReleaseEvent', 'moveEvent', 'nonClientAreaMouseEvent', 'plug',
    'setFloating', 'setResizerActive', 'setWindowState', 'startDrag',
    'unplug', 'updateButtons', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDockWidgetPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DragScope(CuteNum, scoped=True):
    """
    The enum 'QDockWidgetPrivate::DragScope' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Group = Kee[int](0)
    Widget = Kee[int](1)

  class EndDragMode(CuteNum, scoped=True):
    """
    The enum 'QDockWidgetPrivate::EndDragMode' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    LocationChange = Kee[int](0)
    Abort = Kee[int](1)

  class WindowState(CuteFlags, scoped=True):
    """
    The flags enum 'QDockWidgetPrivate::WindowState' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QDockWidgetPrivate::WindowStates'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Unplug = 0x1
    Floating = 0x2

  WindowStates = WindowState

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QInternal.DockPosition)
  def toDockWidgetArea(pos: QInternal.DockPosition) -> Qt.DockWidgetArea:
    """
    Calls Qt's 'Qt::DockWidgetArea
    QDockWidgetPrivate::toDockWidgetArea(QInternal::DockPosition pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetprivate.html#toDockWidgetArea

    Parameters
    ----------

    pos : QInternal.DockPosition
      Passed on as its number.

    Returns
    -------

    Qt.DockWidgetArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.DockWidgetArea(number)' gives.
    """
    #  Qt::DockWidgetArea
    #      QDockWidgetPrivate::toDockWidgetArea(QInternal::DockPosition pos)
    return Qt.DockWidgetArea(Rituals.call(
        'ritual_ZN18QDockWidgetPrivate16toDockWidgetAreaEN9QInternal12DockP'
        'ositionE',
        pos.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockWidgetPrivate'

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

  def q_func(self) -> Optional[QDockWidget]:
    """
    Calls Qt's 'QDockWidget *QDockWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetprivate.html#q_func

    Returns
    -------

    Optional[QDockWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockWidget *QDockWidgetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QDockWidgetPrivate6q_funcEv')
    from . import QDockWidget
    return QDockWidget._cuteAt(address)

  @overload(bool)
  def toggleView(self, a0: bool) -> None:
    """
    Calls Qt's 'void QDockWidgetPrivate::toggleView(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetprivate.html#toggleView

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QDockWidgetPrivate::toggleView(bool a0)
    self.uglySide.call('ritual_ZN18QDockWidgetPrivate10toggleViewEb', a0)

  def toggleTopLevel(self) -> None:
    """
    Calls Qt's 'void QDockWidgetPrivate::toggleTopLevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetprivate.html#toggleTopLevel
    """
    #  void QDockWidgetPrivate::toggleTopLevel()
    self.uglySide.call('ritual_ZN18QDockWidgetPrivate14toggleTopLevelEv')

  @overload(QResizeEvent)
  @overload(NoneType)
  def recalculatePressPos(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QDockWidgetPrivate::recalculatePressPos(QResizeEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetprivate.html#recalculatePressPos

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidgetPrivate::recalculatePressPos(QResizeEvent *event)
    self.uglySide.call(
        'ritual_ZN18QDockWidgetPrivate19recalculatePressPosEP12QResizeEvent',
        self._addressOf(event),
    )

  @staticmethod
  def endDrag(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::endDrag(EndDragMode mode)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.endDrag' has no cute function yet. Qt's 'void "
        "QDockWidgetPrivate::endDrag(EndDragMode mode)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qt_mainwindow_layout'."
    )

  @staticmethod
  def initDrag(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::initDrag(const QPoint &pos, bool nca)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'qt_mainwindow_layout_from_dock'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.initDrag' has no cute function yet. Qt's 'void "
        "QDockWidgetPrivate::initDrag(const QPoint &pos, bool nca)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout_from_dock'.")

  @staticmethod
  def isAnimating(*__, **_) -> Never:
    """
    Qt's 'bool QDockWidgetPrivate::isAnimating() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qt_mainwindow_layout_from_dock'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.isAnimating' has no cute function yet. Qt's "
        "'bool QDockWidgetPrivate::isAnimating() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'qt_mainwindow_layout_from_dock'.")

  @staticmethod
  def isTabbed(*__, **_) -> Never:
    """
    Qt's 'bool QDockWidgetPrivate::isTabbed() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qt_mainwindow_layout_from_dock'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.isTabbed' has no cute function yet. Qt's 'bool "
        "QDockWidgetPrivate::isTabbed() const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier "
        "'qt_mainwindow_layout_from_dock'.")

  @staticmethod
  def mouseDoubleClickEvent(*__, **_) -> Never:
    """
    Qt's 'bool QDockWidgetPrivate::mouseDoubleClickEvent(QMouseEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'hasFeature'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.mouseDoubleClickEvent' has no cute function "
        "yet. Qt's 'bool "
        "QDockWidgetPrivate::mouseDoubleClickEvent(QMouseEvent *event)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'hasFeature'.")

  @staticmethod
  def mouseMoveEvent(*__, **_) -> Never:
    """
    Qt's 'bool QDockWidgetPrivate::mouseMoveEvent(QMouseEvent *event)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'qt_mainwindow_layout_from_dock'; did you mean 'mainwindow_from_dock'?.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.mouseMoveEvent' has no cute function yet. Qt's "
        "'bool QDockWidgetPrivate::mouseMoveEvent(QMouseEvent *event)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout_from_dock'; did you mean "
        "'mainwindow_from_dock'?.")

  @staticmethod
  def mousePressEvent(*__, **_) -> Never:
    """
    Qt's 'bool QDockWidgetPrivate::mousePressEvent(QMouseEvent *event)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'hasFeature'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.mousePressEvent' has no cute function yet. "
        "Qt's 'bool QDockWidgetPrivate::mousePressEvent(QMouseEvent "
        "*event)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'hasFeature'.")

  @staticmethod
  def mouseReleaseEvent(*__, **_) -> Never:
    """
    Qt's 'bool QDockWidgetPrivate::mouseReleaseEvent(QMouseEvent *event)':
    leans on 'QDockWidgetPrivate::endDrag(QDockWidgetPrivate::EndDragMode)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.mouseReleaseEvent' has no cute function yet. "
        "Qt's 'bool QDockWidgetPrivate::mouseReleaseEvent(QMouseEvent "
        "*event)': leans on "
        "'QDockWidgetPrivate::endDrag(QDockWidgetPrivate::EndDragMode)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def moveEvent(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::moveEvent(QMoveEvent *event)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'qt_mainwindow_layout_from_dock'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.moveEvent' has no cute function yet. Qt's "
        "'void QDockWidgetPrivate::moveEvent(QMoveEvent *event)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout_from_dock'.")

  @staticmethod
  def nonClientAreaMouseEvent(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::nonClientAreaMouseEvent(QMouseEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'hasFeature'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.nonClientAreaMouseEvent' has no cute function "
        "yet. Qt's 'void "
        "QDockWidgetPrivate::nonClientAreaMouseEvent(QMouseEvent *event)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'hasFeature'.")

  @staticmethod
  def plug(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::plug(const QRect &rect)': leans on
    'QDockWidgetPrivate::setWindowState(QFlags<QDockWidgetPrivate::
    WindowState>, QRect const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.plug' has no cute function yet. Qt's 'void "
        "QDockWidgetPrivate::plug(const QRect &rect)': leans on "
        "'QDockWidgetPrivate::setWindowState(QFlags<QDockWidgetPrivate::Wind"
        "owState>, QRect const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setFloating(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::setFloating(bool floating)': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.setFloating' has no cute function yet. Qt's "
        "'void QDockWidgetPrivate::setFloating(bool floating)': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setResizerActive(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::setResizerActive(bool active)': leans on
    'QWidgetResizeHandler::QWidgetResizeHandler(QWidget*, QWidget*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.setResizerActive' has no cute function yet. "
        "Qt's 'void QDockWidgetPrivate::setResizerActive(bool active)': "
        "leans on 'QWidgetResizeHandler::QWidgetResizeHandler(QWidget*, "
        "QWidget*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def setWindowState(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::setWindowState(WindowStates states, const
    QRect &rect)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'qt_mainwindow_layout_from_dock'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.setWindowState' has no cute function yet. Qt's "
        "'void QDockWidgetPrivate::setWindowState(WindowStates states, "
        "const QRect &rect)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qt_mainwindow_layout_from_dock'.")

  @staticmethod
  def startDrag(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::startDrag(DragScope scope)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier
    'qt_mainwindow_layout_from_dock'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.startDrag' has no cute function yet. Qt's "
        "'void QDockWidgetPrivate::startDrag(DragScope scope)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout_from_dock'.")

  @staticmethod
  def unplug(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::unplug(const QRect &rect)': leans on
    'QDockWidgetPrivate::setWindowState(QFlags<QDockWidgetPrivate::
    WindowState>, QRect const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.unplug' has no cute function yet. Qt's 'void "
        "QDockWidgetPrivate::unplug(const QRect &rect)': leans on "
        "'QDockWidgetPrivate::setWindowState(QFlags<QDockWidgetPrivate::Wind"
        "owState>, QRect const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateButtons(*__, **_) -> Never:
    """
    Qt's 'void QDockWidgetPrivate::updateButtons()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'hasFeature'.
    """
    raise NotImplementedError(
        "'QDockWidgetPrivate.updateButtons' has no cute function yet. Qt's "
        "'void QDockWidgetPrivate::updateButtons()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'hasFeature'.")
