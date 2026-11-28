"""
QAccessibleMainWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleMainWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMainWindow

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleMainWindow(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleMainWindow: a plain Python object standing
  in front of one C++ QAccessibleMainWindow.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleMainWindow is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleMainWindow that has a ritual and that
  Python can call so far, 5 names in all: 'child', 'childCount',
  'indexOfChild', 'childAt', 'mainWindow'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'QAccessibleMainWindow.

  What to expect
  --------------

  - The C++ QAccessibleMainWindow is created at the first use, not by
    'QAccessibleMainWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleMainWindow.
  - Each name of Qt's QAccessibleMainWindow that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleMainWindow'

  #  A C++ QAccessibleMainWindow Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleMainWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMainWindow::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemainwindow.html#child

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleMainWindow::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleMainWindow5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleMainWindow::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemainwindow.html#childCount
    """
    #  int QAccessibleMainWindow::childCount() const
    ritual = 'ritual_ZNK21QAccessibleMainWindow10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleMainWindow10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleMainWindow::indexOfChild(const
    QAccessibleInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemainwindow.html#indexOfChild

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleMainWindow::indexOfChild(const QAccessibleInterface
    #      *iface) const
    return self.uglySide.call(
        'ritual_ZNK21QAccessibleMainWindow12indexOfChildEPK20QAccessibleInt'
        'erface',
        self._addressOf(iface, 'QAccessibleInterface'),
    )

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMainWindow::childAt(int x,
    int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemainwindow.html#childAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleMainWindow::childAt(int x, int y)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleMainWindow7childAtEii', x, y,
    )
    return QAccessibleInterface._cuteAt(address)

  def mainWindow(self) -> Optional[QMainWindow]:
    """
    Calls Qt's 'QMainWindow *QAccessibleMainWindow::mainWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemainwindow.html#mainWindow

    Returns
    -------

    Optional[QMainWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMainWindow *QAccessibleMainWindow::mainWindow() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleMainWindow10mainWindowEv',
    )
    from . import QMainWindow
    return QMainWindow._cuteAt(address)

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
    Qt's 'QAccessibleMainWindow::QAccessibleMainWindow(QWidget *widget)':
    leans on 'QAccessibleMainWindow::indexOfChild(QAccessibleInterface
    const*) const', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleMainWindow.__init__' has no cute function yet. Qt's "
        "'QAccessibleMainWindow::QAccessibleMainWindow(QWidget *widget)': "
        "leans on 'QAccessibleMainWindow::indexOfChild(QAccessibleInterface "
        "const*) const', which Qt's source does not mark for use from "
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
