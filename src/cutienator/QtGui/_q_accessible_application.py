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
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication6windowEv',
    )
    from . import QWindow
    return QWindow._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleApplication::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleapplication.html#childCount
    """
    #  int QAccessibleApplication::childCount() const
    return self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication10childCountEv',
    )

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
    return self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication12indexOfChildEPK20QAccessibleIn'
        'terface',
        self._addressOf(a0),
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
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication10focusChildEv',
    )
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
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication6parentEv',
    )
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
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication5childEi', index,
    )
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
    return self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication4textEN11QAccessible4TextE',
        t.value,
    )

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
    return QAccessible.Role(self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication4roleEv',
    ))

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
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleApplication5stateEv',
    )
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
