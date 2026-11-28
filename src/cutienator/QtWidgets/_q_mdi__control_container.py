"""
QMdi::ControlContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMdi::ControlContainer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QIcon
  from . import QMenuBar, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']


class ControlContainer(QObject):
  """
  The cute side of Qt's QMdi::ControlContainer: a plain Python object
  standing in front of one C++ QMdi::ControlContainer.

  It is built on the cute 'QObject', as Qt's QMdi::ControlContainer is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMdi::ControlContainer that has a ritual and that
  Python can call so far, 4 names in all: 'menuBar', 'updateWindowIcon',
  'controllerWidget', 'systemMenuLabel'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMdi::ControlContainer::~ControlContainer()': the destructor:
    Python never removes a C++ QMdi::ControlContainer.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QMdi.

  What to expect
  --------------

  - The C++ QMdi::ControlContainer is created at the first use, not by
    'QMdi::ControlContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMdi::ControlContainer.
  - Qt tells when it has removed the C++ QMdi::ControlContainer. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QMdi::ControlContainer that has no cute function yet,
    '__init__', 'removeButtonsFromMenuBar', 'showButtonsInMenuBar', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdi::ControlContainer'

  #  A C++ QMdi::ControlContainer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMdi_ControlContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def menuBar(self) -> Optional[QMenuBar]:
    """
    Calls Qt's 'QMenuBar *QMdi::ControlContainer::menuBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdi-controlcontainer.html#menuBar

    Returns
    -------

    Optional[QMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenuBar *QMdi::ControlContainer::menuBar() const
    address = self.uglySide.call(
        'ritual_ZNK4QMdi16ControlContainer7menuBarEv',
    )
    from . import QMenuBar
    return QMenuBar._cuteAt(address)

  def controllerWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMdi::ControlContainer::controllerWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdi-controlcontainer.html#controllerWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMdi::ControlContainer::controllerWidget() const
    address = self.uglySide.call(
        'ritual_ZNK4QMdi16ControlContainer16controllerWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def systemMenuLabel(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMdi::ControlContainer::systemMenuLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdi-controlcontainer.html#systemMenuLabel

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMdi::ControlContainer::systemMenuLabel() const
    address = self.uglySide.call(
        'ritual_ZNK4QMdi16ControlContainer15systemMenuLabelEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

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
    Qt's 'QMdi::ControlContainer::ControlContainer(QMdiSubWindow *mdiChild)':
    leans on 'QMdi::ControlLabel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMdi.ControlContainer.__init__' has no cute function yet. Qt's "
        "'QMdi::ControlContainer::ControlContainer(QMdiSubWindow "
        "*mdiChild)': leans on "
        "'QMdi::ControlLabel::qt_metacall(QMetaObject::Call, int, void**)', "
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

  @overload(QIcon)
  def updateWindowIcon(self, windowIcon: QIcon) -> None:
    """
    Calls Qt's 'void QMdi::ControlContainer::updateWindowIcon(const QIcon
    &windowIcon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdi-controlcontainer.html#updateWindowIcon

    Parameters
    ----------

    windowIcon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QMdi::ControlContainer::updateWindowIcon(const QIcon &windowIcon)
    self.uglySide.call(
        'ritual_ZN4QMdi16ControlContainer16updateWindowIconERK5QIcon',
        self._valueOf(windowIcon),
    )

  @staticmethod
  def removeButtonsFromMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QMdi::ControlContainer::removeButtonsFromMenuBar(QMenuBar
    *menuBar)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'ControllerWidget'.
    """
    raise NotImplementedError(
        "'QMdi.ControlContainer.removeButtonsFromMenuBar' has no cute "
        "function yet. Qt's 'void "
        "QMdi::ControlContainer::removeButtonsFromMenuBar(QMenuBar "
        "*menuBar)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'ControllerWidget'.")

  @staticmethod
  def showButtonsInMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QMdi::ControlContainer::showButtonsInMenuBar(QMenuBar
    *menuBar)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'ControllerWidget'; did you mean 'controllerWidget'?.
    """
    raise NotImplementedError(
        "'QMdi.ControlContainer.showButtonsInMenuBar' has no cute function "
        "yet. Qt's 'void "
        "QMdi::ControlContainer::showButtonsInMenuBar(QMenuBar *menuBar)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'ControllerWidget'; did you mean 'controllerWidget'?.")
