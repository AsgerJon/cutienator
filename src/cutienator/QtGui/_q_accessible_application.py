"""
QAccessibleApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessibleobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QAccessible, QAccessibleInterface, QAccessibleObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWindow

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleApplication(QAccessibleObject):
  """
  The cute side of Qt's QAccessibleApplication: a plain Python object
  standing in front of one C++ QAccessibleApplication.

  It is built on the cute 'QAccessibleObject', as Qt's QAccessibleApplication
  is built on Qt's QAccessibleObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleApplication that has a ritual and that
  Python can call so far, 9 names in all: 'window', 'childCount',
  'indexOfChild', 'focusChild', 'parent', 'child', 'text', 'role', 'state'.
  It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleApplication is created at the first use, not by
    'QAccessibleApplication(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleApplication.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleApplication'

  #  A C++ QAccessibleApplication Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleApplication'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QAccessibleApplication::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleapplication.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QAccessibleApplication::window() const
    ritual = 'ritual_ZNK22QAccessibleApplication6windowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleApplication6windowEv'
    address = self.uglySide.call(ritual)
    from . import QWindow
    return QWindow._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleApplication::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleapplication.html#childCount
    """
    #  int QAccessibleApplication::childCount() const
    ritual = 'ritual_ZNK22QAccessibleApplication10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleApplication10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleApplication::indexOfChild(const
    QAccessibleInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleapplication.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleApplication::indexOfChild(const QAccessibleInterface
    #      *a0) const
    ritual = (
        'ritual_ZNK22QAccessibleApplication12indexOfChildEPK20QAccessibleIn'
        'terface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QAccessibleApplication12indexOfChildEPK20QAccess'
          'ibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QAccessibleInterface'),
    )

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleApplication::focusChild()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleapplication.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleApplication::focusChild() const
    ritual = 'ritual_ZNK22QAccessibleApplication10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleApplication10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleApplication::parent()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleapplication.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleApplication::parent() const
    ritual = 'ritual_ZNK22QAccessibleApplication6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleApplication6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleApplication::child(int
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleapplication.html#child

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
    #  QAccessibleInterface *QAccessibleApplication::child(int index) const
    ritual = 'ritual_ZNK22QAccessibleApplication5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleApplication5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleApplication::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleapplication.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleApplication::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK22QAccessibleApplication4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QAccessibleApplication4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, t.value)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleApplication::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleapplication.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleApplication::role() const
    ritual = 'ritual_ZNK22QAccessibleApplication4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleApplication4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleApplication::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleapplication.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleApplication::state() const
    ritual = 'ritual_ZNK22QAccessibleApplication5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleApplication5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleApplication::QAccessibleApplication()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleapplication.html#QAccessibleApplication
    """
    #  QAccessibleApplication::QAccessibleApplication()
    self._noteCreation(QAccessibleApplication, lambda: Rituals.call(
        'ritual_ZN22QAccessibleApplicationC1Ev',
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
