"""
QToolBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtoolbar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QToolBarPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from . import QToolBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']


class QToolBarPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QToolBarPrivate: a plain Python object standing in
  front of one C++ QToolBarPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QToolBarPrivate is built
  on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolBarPrivate that has a ritual and that Python
  can call so far, 7 names in all: 'q_func', '_q_toggleView',
  '_q_updateIconSize', '_q_updateToolButtonStyle', 'updateWindowFlags',
  'setWindowState', 'plug'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QToolBar *QToolBarPrivate::q_func() const': takes in Python
    what 'QToolBar *QToolBarPrivate::q_func()' takes.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QToolBarPrivate; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied; 1 leans on 'vtable for QToolBarLayout',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken; 1 leans on 'QToolBarLayout.

  What to expect
  --------------

  - The C++ QToolBarPrivate is created at the first use, not by
    'QToolBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolBarPrivate.
  - Each name of Qt's QToolBarPrivate that has no cute function yet,
    'actionTriggered', 'endDrag', 'initDrag', 'mouseMoveEvent',
    'mousePressEvent', 'mouseReleaseEvent', 'startDrag', 'unplug', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QToolBarPrivate, each a class in here as in
  #  C++.

  class DragState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QToolBarPrivate::DragState: a plain Python object
    standing in front of one C++ QToolBarPrivate::DragState.

    C++ hands a QToolBarPrivate::DragState around as a copy, so every C++
    QToolBarPrivate::DragState behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QToolBarPrivate::DragState yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QToolBarPrivate::DragState::~DragState()': the destructor: Python
      removes its C++ QToolBarPrivate::DragState by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QToolBarPrivate::DragState is created at the first use, not by
      'QToolBarPrivate::DragState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QToolBarPrivate::DragState back gives a copy the
      ritual made for Python, in a new cute QToolBarPrivate::DragState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QToolBarPrivate::DragState'

    #  Qt's '~QToolBarPrivate::DragState()'. Naming it makes this a value
    #  class: Python owns every C++ QToolBarPrivate::DragState behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QToolBarPrivate9DragStateD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBarPrivate'

  #  A C++ QToolBarPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QToolBarPrivate'

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

  @overload(bool)
  @overload(bool, bool)
  @overload(bool, bool, QRect)
  def setWindowState(
      self,
      floating: bool,
      unplug: bool = False,
      rect: Optional[QRect] = None,
  ) -> None:
    """
    Calls Qt's 'void QToolBarPrivate::setWindowState(bool floating, bool
    unplug, const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarprivate.html#setWindowState

    Parameters
    ----------

    floating : bool
      Passed on as it is.

    unplug : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void QToolBarPrivate::setWindowState(bool floating, bool unplug, const
    #      QRect &rect)
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    self.uglySide.call(
        'ritual_ZN15QToolBarPrivate14setWindowStateEbbRK5QRect',
        floating, unplug, self._valueOf(rect),
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
    Notes what was given, for Qt's 'QToolBarPrivate::QToolBarPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarprivate.html#QToolBarPrivate
    """
    #  QToolBarPrivate::QToolBarPrivate()
    self._noteCreation(QToolBarPrivate, lambda: Rituals.call(
        'ritual_ZN15QToolBarPrivateC1Ev',
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

  def q_func(self) -> Optional[QToolBar]:
    """
    Calls Qt's 'QToolBar *QToolBarPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarprivate.html#q_func

    Returns
    -------

    Optional[QToolBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QToolBar *QToolBarPrivate::q_func()
    address = self.uglySide.call('ritual_ZN15QToolBarPrivate6q_funcEv')
    from . import QToolBar
    return QToolBar._cuteAt(address)

  @overload(bool)
  def _q_toggleView(self, b: bool) -> None:
    """
    Calls Qt's 'void QToolBarPrivate::_q_toggleView(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarprivate.html#_q_toggleView

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QToolBarPrivate::_q_toggleView(bool b)
    self.uglySide.call('ritual_ZN15QToolBarPrivate13_q_toggleViewEb', b)

  @overload(QSize)
  def _q_updateIconSize(self, sz: QSize) -> None:
    """
    Calls Qt's 'void QToolBarPrivate::_q_updateIconSize(const QSize &sz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarprivate.html#_q_updateIconSize

    Parameters
    ----------

    sz : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QToolBarPrivate::_q_updateIconSize(const QSize &sz)
    self.uglySide.call(
        'ritual_ZN15QToolBarPrivate17_q_updateIconSizeERK5QSize',
        self._valueOf(sz),
    )

  @overload(Qt.ToolButtonStyle)
  def _q_updateToolButtonStyle(self, style: Qt.ToolButtonStyle) -> None:
    """
    Calls Qt's 'void
    QToolBarPrivate::_q_updateToolButtonStyle(Qt::ToolButtonStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarprivate.html#_q_updateToolButtonStyle

    Parameters
    ----------

    style : Qt.ToolButtonStyle
      Passed on as its number.
    """
    #  void QToolBarPrivate::_q_updateToolButtonStyle(Qt::ToolButtonStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN15QToolBarPrivate24_q_updateToolButtonStyleEN2Qt15ToolBut'
        'tonStyleE',
        style.value,
    )

  @overload(bool)
  @overload(bool, bool)
  def updateWindowFlags(self, floating: bool, unplug: bool = False) -> None:
    """
    Calls Qt's 'void QToolBarPrivate::updateWindowFlags(bool floating, bool
    unplug)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarprivate.html#updateWindowFlags

    Parameters
    ----------

    floating : bool
      Passed on as it is.

    unplug : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QToolBarPrivate::updateWindowFlags(bool floating, bool unplug)
    self.uglySide.call(
        'ritual_ZN15QToolBarPrivate17updateWindowFlagsEbb', floating, unplug,
    )

  @overload(QRect)
  def plug(self, r: QRect) -> None:
    """
    Calls Qt's 'void QToolBarPrivate::plug(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarprivate.html#plug

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QToolBarPrivate::plug(const QRect &r)
    self.uglySide.call(
        'ritual_ZN15QToolBarPrivate4plugERK5QRect', self._valueOf(r),
    )

  @staticmethod
  def actionTriggered(*__, **_) -> Never:
    """
    Qt's 'void QToolBarPrivate::actionTriggered()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.actionTriggered' has no cute function yet. Qt's "
        "'void QToolBarPrivate::actionTriggered()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def endDrag(*__, **_) -> Never:
    """
    Qt's 'void QToolBarPrivate::endDrag()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.endDrag' has no cute function yet. Qt's 'void "
        "QToolBarPrivate::endDrag()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'qt_mainwindow_layout'.")

  @staticmethod
  def initDrag(*__, **_) -> Never:
    """
    Qt's 'void QToolBarPrivate::initDrag(const QPoint &pos)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.initDrag' has no cute function yet. Qt's 'void "
        "QToolBarPrivate::initDrag(const QPoint &pos)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qt_mainwindow_layout'."
    )

  @staticmethod
  def mouseMoveEvent(*__, **_) -> Never:
    """
    Qt's 'bool QToolBarPrivate::mouseMoveEvent(QMouseEvent *e)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.mouseMoveEvent' has no cute function yet. Qt's "
        "'bool QToolBarPrivate::mouseMoveEvent(QMouseEvent *e)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout'.")

  @staticmethod
  def mousePressEvent(*__, **_) -> Never:
    """
    Qt's 'bool QToolBarPrivate::mousePressEvent(QMouseEvent *e)': leans on
    'QToolBarPrivate::initDrag(QPoint const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.mousePressEvent' has no cute function yet. Qt's "
        "'bool QToolBarPrivate::mousePressEvent(QMouseEvent *e)': leans on "
        "'QToolBarPrivate::initDrag(QPoint const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mouseReleaseEvent(*__, **_) -> Never:
    """
    Qt's 'bool QToolBarPrivate::mouseReleaseEvent(QMouseEvent *e)': leans on
    'QToolBarPrivate::endDrag()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.mouseReleaseEvent' has no cute function yet. Qt's "
        "'bool QToolBarPrivate::mouseReleaseEvent(QMouseEvent *e)': leans "
        "on 'QToolBarPrivate::endDrag()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def startDrag(*__, **_) -> Never:
    """
    Qt's 'void QToolBarPrivate::startDrag(bool moving)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.startDrag' has no cute function yet. Qt's 'void "
        "QToolBarPrivate::startDrag(bool moving)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qt_mainwindow_layout'.")

  @staticmethod
  def unplug(*__, **_) -> Never:
    """
    Qt's 'void QToolBarPrivate::unplug(const QRect &r)': leans on
    'QToolBarLayout::setExpanded(bool)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarPrivate.unplug' has no cute function yet. Qt's 'void "
        "QToolBarPrivate::unplug(const QRect &r)': leans on "
        "'QToolBarLayout::setExpanded(bool)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
