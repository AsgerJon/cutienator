"""
QAccessibleQuickWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qaccessiblequickview_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleQuickWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QAccessible, QAccessibleInterface, QAccessibleObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from . import QQuickItem, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickWindow(QAccessibleObject):
  """
  The cute side of Qt's QAccessibleQuickWindow: a plain Python object
  standing in front of one C++ QAccessibleQuickWindow.

  It is built on the cute 'QAccessibleObject', as Qt's QAccessibleQuickWindow
  is built on Qt's QAccessibleObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickWindow that has a ritual and that
  Python can call so far, 12 names in all: 'parent', 'child', 'focusChild',
  'role', 'state', 'rect', 'childCount', 'indexOfChild', 'text', 'childAt',
  'window', 'rootItems'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleQuickWindow is created at the first use, not by
    'QAccessibleQuickWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickWindow.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickWindow::parent()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwindow.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleQuickWindow::parent() const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickWindow::child(int
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwindow.html#child

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
    #  QAccessibleInterface *QAccessibleQuickWindow::child(int index) const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickWindow::focusChild()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwindow.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleQuickWindow::focusChild() const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleQuickWindow::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwindow.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleQuickWindow::role() const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleQuickWindow::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwindow.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleQuickWindow::state() const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleQuickWindow::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwindow.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleQuickWindow::rect() const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleQuickWindow::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwindow.html#childCount
    """
    #  int QAccessibleQuickWindow::childCount() const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleQuickWindow::indexOfChild(const
    QAccessibleInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwindow.html#indexOfChild

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleQuickWindow::indexOfChild(const QAccessibleInterface
    #      *iface) const
    ritual = (
        'ritual_ZNK22QAccessibleQuickWindow12indexOfChildEPK20QAccessibleIn'
        'terface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QAccessibleQuickWindow12indexOfChildEPK20QAccess'
          'ibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(iface, 'QAccessibleInterface'),
    )

  @overload(QAccessible.Text)
  def text(self, text: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleQuickWindow::text(QAccessible::Text text)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwindow.html#text

    Parameters
    ----------

    text : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleQuickWindow::text(QAccessible::Text text) const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QAccessibleQuickWindow4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, text.value)

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickWindow::childAt(int x,
    int y) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwindow.html#childAt

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
    #  QAccessibleInterface *QAccessibleQuickWindow::childAt(int x, int y)
    #      const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QAccessibleQuickWindow::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwindow.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QAccessibleQuickWindow::window() const
    ritual = 'ritual_ZNK22QAccessibleQuickWindow6windowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWindow6windowEv'
    address = self.uglySide.call(ritual)
    from . import QQuickWindow
    return QQuickWindow._cuteAt(address)

  def rootItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *> QAccessibleQuickWindow::rootItems()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwindow.html#rootItems

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QAccessibleQuickWindow::rootItems() const
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleQuickWindow9rootItemsEv',
    )
    from . import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

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

  @overload(QQuickWindow)
  @overload(NoneType)
  def __init__(self, object: Optional[QQuickWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickWindow::QAccessibleQuickWindow(QQuickWindow *object)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwindow.html#QAccessibleQuickWindow

    Parameters
    ----------

    object : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickWindow::QAccessibleQuickWindow(QQuickWindow *object)
    self._noteCreation(QAccessibleQuickWindow, lambda: Rituals.call(
        'ritual_ZN22QAccessibleQuickWindowC1EP12QQuickWindow',
        self._addressOf(object),
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
