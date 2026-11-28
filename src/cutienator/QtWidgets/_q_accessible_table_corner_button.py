"""
QAccessibleTableCornerButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleTableCornerButton to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QRect
  from . import QAbstractItemView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemView = WAIT['QAbstractItemView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTableCornerButton(QAccessibleInterface):
  """
  The cute side of Qt's QAccessibleTableCornerButton: a plain Python object
  standing in front of one C++ QAccessibleTableCornerButton.

  It is built on the cute 'QAccessibleInterface', as Qt's
  QAccessibleTableCornerButton is built on Qt's QAccessibleInterface, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTableCornerButton that has a ritual and
  that Python can call so far, 12 names in all: 'object', 'role', 'state',
  'rect', 'isValid', 'childAt', 'childCount', 'indexOfChild', 'text',
  'setText', 'parent', 'child'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleTableCornerButton is created at the first use, not by
    'QAccessibleTableCornerButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTableCornerButton.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTableCornerButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAccessibleTableCornerButton::object() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAccessibleTableCornerButton::object() const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton6objectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton6objectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleTableCornerButton::role()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleTableCornerButton::role() const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleTableCornerButton::state()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleTableCornerButton::state() const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleTableCornerButton::rect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleTableCornerButton::rect() const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableCornerButton::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#isValid
    """
    #  bool QAccessibleTableCornerButton::isValid() const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton7isValidEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def childAt(self, a0: int, a1: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QAccessibleTableCornerButton::childAt(int a0, int a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#childAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCornerButton::childAt(int a0,
    #      int a1) const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton7childAtEii'
    address = self.uglySide.call(ritual, a0, a1)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCornerButton::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#childCount
    """
    #  int QAccessibleTableCornerButton::childCount() const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleTableCornerButton::indexOfChild(const
    QAccessibleInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleTableCornerButton::indexOfChild(const
    #      QAccessibleInterface *a0) const
    ritual = (
        'ritual_ZNK28QAccessibleTableCornerButton12indexOfChildEPK20QAccess'
        'ibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QAccessibleTableCornerButton12indexOfChildEPK20Q'
          'AccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QAccessibleInterface'),
    )

  @overload(QAccessible.Text)
  def text(self, a0: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleTableCornerButton::text(QAccessible::Text
    a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#text

    Parameters
    ----------

    a0 : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTableCornerButton::text(QAccessible::Text a0) const
    ritual = (
        'ritual_ZNK28QAccessibleTableCornerButton4textEN11QAccessible4TextE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QAccessibleTableCornerButton4textEN11QAccessible'
          '4TextE')
    return self.uglySide.call(ritual, a0.value)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableCornerButton::parent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCornerButton::parent() const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, a0: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableCornerButton::child(int
    a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#child

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCornerButton::child(int a0)
    #      const
    ritual = 'ritual_ZNK28QAccessibleTableCornerButton5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QAccessibleTableCornerButton5childEi'
    address = self.uglySide.call(ritual, a0)
    return QAccessibleInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, a0: QAccessible.Text, a1: str) -> None:
    """
    Calls Qt's 'void QAccessibleTableCornerButton::setText(QAccessible::Text
    a0, const QString &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html#setText

    Parameters
    ----------

    a0 : QAccessible.Text
      Passed on as its number.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleTableCornerButton::setText(QAccessible::Text a0, const
    #      QString &a1)
    ritual = (
        'ritual_ZN28QAccessibleTableCornerButton7setTextEN11QAccessible4Tex'
        'tERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QAccessibleTableCornerButton7setTextEN11QAccessib'
          'le4TextERK7QString')
    self.uglySide.call(ritual, a0.value, a1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemView)
  @overload(NoneType)
  def __init__(self, view_: Optional[QAbstractItemView]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTableCornerButton::QAccessibleTableCornerButton(
    QAbstractItemView *view_)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecornerbutton.html

    Parameters
    ----------

    view_ : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleTableCornerButton::QAccessibleTableCornerButton(
    #      QAbstractItemView *view_)
    self._noteCreation(QAccessibleTableCornerButton, lambda: Rituals.call(
        'ritual_ZN28QAccessibleTableCornerButtonC1EP17QAbstractItemView',
        self._addressOf(view_),
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
