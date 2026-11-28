"""
QNativeInterface::Private::QXcbWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformwindow_p.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals


class QXcbWindow(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::Private::QXcbWindow: a plain Python
  object standing in front of one C++ QNativeInterface::Private::QXcbWindow.

  What exists
  -----------

  Every function of Qt's QNativeInterface::Private::QXcbWindow that has a
  ritual and that Python can call so far, 4 names in all: 'setWindowType',
  'setWindowRole', 'setWindowIconText', 'visualId'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::Private::QXcbWindow::~QXcbWindow()': the
    destructor: Python never removes a C++
    QNativeInterface::Private::QXcbWindow.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QNativeInterface::Private::QXcbWindow is created at the first
    use, not by 'QNativeInterface::Private::QXcbWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::Private::QXcbWindow.
  """

  #  The enums Qt writes inside QNativeInterface::Private::QXcbWindow, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class WindowType(CuteFlags):
    """
    The flags enum 'QNativeInterface::Private::QXcbWindow::WindowType' of Qt,
    with the 16 names Qt gives in it. Qt names the type of its combinations
    'QNativeInterface::Private::QXcbWindow::WindowTypes'.
    """

    NULL = 0x0
    Normal = 0x1
    Desktop = 0x2
    Dock = 0x4
    Toolbar = 0x8
    Menu = 0x10
    Utility = 0x20
    Splash = 0x40
    Dialog = 0x80
    DropDownMenu = 0x100
    PopupMenu = 0x200
    Tooltip = 0x400
    Notification = 0x800
    Combo = 0x1000
    Dnd = 0x2000
    KdeOverride = 0x4000

  WindowTypes = WindowType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeInterface::Private::QXcbWindow'

  #  A C++ QNativeInterface::Private::QXcbWindow Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_Private_QXcbWindow'

  #  The functions Qt calls itself that QNativeInterface::Private::QXcbWindow
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setWindowType': (
          ('_ZN16QNativeInterface7Private10QXcbWindow13setWindowTypeE6QFlag'
           'sINS1_10WindowTypeEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtGui:QNativeInterface.Private.QXcbWindow.WindowType'),
           )),
      ),
      'setWindowRole': (
          ('_ZN16QNativeInterface7Private10QXcbWindow13setWindowRoleERK7QSt'
           'ring',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setWindowIconText': (
          ('_ZN16QNativeInterface7Private10QXcbWindow17setWindowIconTextERK'
           '7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'visualId': (
          ('_ZNK16QNativeInterface7Private10QXcbWindow8visualIdEv',
           ('unsigned int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def visualId(self) -> int:
    """
    Calls Qt's 'uint QNativeInterface::Private::QXcbWindow::visualId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qxcbwindow.html#visualId
    """
    #  uint QNativeInterface::Private::QXcbWindow::visualId() const
    return self.uglySide.call(
        'ritual_ZNK16QNativeInterface7Private10QXcbWindow8visualIdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WindowTypes)
  def setWindowType(self, type: WindowTypes) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QXcbWindow::setWindowType(WindowTypes type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qxcbwindow.html

    Parameters
    ----------

    type : WindowTypes
      Passed on as its number.
    """
    #  void QNativeInterface::Private::QXcbWindow::setWindowType(WindowTypes
    #      type)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private10QXcbWindow13setWindowTypeE6QF'
        'lagsINS1_10WindowTypeEE',
        type.value,
    )

  @overload(str)
  def setWindowRole(self, role: str) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QXcbWindow::setWindowRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qxcbwindow.html

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNativeInterface::Private::QXcbWindow::setWindowRole(const
    #      QString &role)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private10QXcbWindow13setWindowRoleERK7'
        'QString',
        role,
    )

  @overload(str)
  def setWindowIconText(self, text: str) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QXcbWindow::setWindowIconText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qxcbwindow.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNativeInterface::Private::QXcbWindow::setWindowIconText(const
    #      QString &text)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private10QXcbWindow17setWindowIconText'
        'ERK7QString',
        text,
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
    'QNativeInterface::Private::QXcbWindow::QXcbWindow()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qxcbwindow.html
    """
    #  QNativeInterface::Private::QXcbWindow::QXcbWindow()
    self._noteCreation(QXcbWindow, lambda: Rituals.call(
        'ritual_ZN16QNativeInterface7Private10QXcbWindowC1Ev',
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
