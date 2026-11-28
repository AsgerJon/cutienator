"""
QAccessibleQuickWidgetOffscreenWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickWidgets/6.12.0/QtQuickWidgets/private/qaccessiblequickwidget_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAccessibleQuickWidgetOffscreenWindow to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessibleInterface
from ..QtQuick import QAccessibleQuickWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickWidgetOffscreenWindow(QAccessibleQuickWindow):
  """
  The cute side of Qt's QAccessibleQuickWidgetOffscreenWindow: a plain Python
  object standing in front of one C++ QAccessibleQuickWidgetOffscreenWindow.

  It is built on the cute 'QAccessibleQuickWindow', as Qt's
  QAccessibleQuickWidgetOffscreenWindow is built on Qt's
  QAccessibleQuickWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickWidgetOffscreenWindow that has a
  ritual and that Python can call so far, 4 names in all: 'child',
  'childCount', 'indexOfChild', 'childAt'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on
  'QAccessibleQuickWidgetOffscreenWindow.

  What to expect
  --------------

  - The C++ QAccessibleQuickWidgetOffscreenWindow is created at the first
    use, not by 'QAccessibleQuickWidgetOffscreenWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickWidgetOffscreenWindow.
  - Each name of Qt's QAccessibleQuickWidgetOffscreenWindow that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QAccessibleQuickWidgetOffscreenWindow'

  #  A C++ QAccessibleQuickWidgetOffscreenWindow Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleQuickWidgetOffscreenWindow'

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
    Calls Qt's 'QAccessibleInterface
    *QAccessibleQuickWidgetOffscreenWindow::child(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidgetoffscreenwindow.html#child

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
    #  QAccessibleInterface *QAccessibleQuickWidgetOffscreenWindow::child(int
    #      index) const
    ritual = 'ritual_ZNK37QAccessibleQuickWidgetOffscreenWindow5childEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK37QAccessibleQuickWidgetOffscreenWindow5childEi')
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleQuickWidgetOffscreenWindow::childCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidgetoffscreenwindow.html
    """
    #  int QAccessibleQuickWidgetOffscreenWindow::childCount() const
    ritual = (
        'ritual_ZNK37QAccessibleQuickWidgetOffscreenWindow10childCountEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK37QAccessibleQuickWidgetOffscreenWindow10childCoun'
          'tEv')
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleQuickWidgetOffscreenWindow::indexOfChild(const
    QAccessibleInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidgetoffscreenwindow.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleQuickWidgetOffscreenWindow::indexOfChild(const
    #      QAccessibleInterface *iface) const
    ritual = (
        'ritual_ZNK37QAccessibleQuickWidgetOffscreenWindow12indexOfChildEPK'
        '20QAccessibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK37QAccessibleQuickWidgetOffscreenWindow12indexOfCh'
          'ildEPK20QAccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(iface, 'QAccessibleInterface'),
    )

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QAccessibleQuickWidgetOffscreenWindow::childAt(int x, int y) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidgetoffscreenwindow.html#childAt

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
    #  QAccessibleInterface
    #      *QAccessibleQuickWidgetOffscreenWindow::childAt(int x, int y)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37QAccessibleQuickWidgetOffscreenWindow7childAtEii', x, y,
    )
    return QAccessibleInterface._cuteAt(address)

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
    Qt's 'QAccessibleQuickWidgetOffscreenWindow::
    QAccessibleQuickWidgetOffscreenWindow(QQuickWindow *window)': leans on
    'QAccessibleQuickWidgetOffscreenWindow::childAt(int, int) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleQuickWidgetOffscreenWindow.__init__' has no cute "
        "function yet. Qt's "
        "'QAccessibleQuickWidgetOffscreenWindow::QAccessibleQuickWidgetOffsc"
        "reenWindow(QQuickWindow *window)': leans on "
        "'QAccessibleQuickWidgetOffscreenWindow::childAt(int, int) const', "
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
