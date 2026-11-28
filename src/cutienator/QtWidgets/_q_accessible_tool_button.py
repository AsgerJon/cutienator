"""
QAccessibleToolButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleToolButton to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QStringList
from ..QtGui import QAccessible, QAccessibleInterface
from . import QAccessibleButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMenu, QToolButton


class QAccessibleToolButton(QAccessibleButton):
  """
  The cute side of Qt's QAccessibleToolButton: a plain Python object standing
  in front of one C++ QAccessibleToolButton.

  It is built on the cute 'QAccessibleButton', as Qt's QAccessibleToolButton
  is built on Qt's QAccessibleButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleToolButton that has a ritual and that
  Python can call so far, 9 names in all: 'state', 'role', 'childCount',
  'child', 'actionNames', 'doAction', 'toolButton', 'isSplitButton', 'menu'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleButton.

  What to expect
  --------------

  - The C++ QAccessibleToolButton is created at the first use, not by
    'QAccessibleToolButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleToolButton.
  - Each name of Qt's QAccessibleToolButton that has no cute function yet,
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
  __qt_class__ = 'QAccessibleToolButton'

  #  A C++ QAccessibleToolButton Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleToolButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleToolButton::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletoolbutton.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleToolButton::state() const
    ritual = 'ritual_ZNK21QAccessibleToolButton5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleToolButton5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleToolButton::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletoolbutton.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleToolButton::role() const
    ritual = 'ritual_ZNK21QAccessibleToolButton4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleToolButton4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleToolButton::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletoolbutton.html#childCount
    """
    #  int QAccessibleToolButton::childCount() const
    ritual = 'ritual_ZNK21QAccessibleToolButton10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleToolButton10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleToolButton::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletoolbutton.html#child

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
    #  QAccessibleInterface *QAccessibleToolButton::child(int index) const
    ritual = 'ritual_ZNK21QAccessibleToolButton5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleToolButton5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def actionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleToolButton::actionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletoolbutton.html#actionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleToolButton::actionNames() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleToolButton11actionNamesEv',
    )
    return QStringList._cuteOwning(address)

  def toolButton(self) -> Optional[QToolButton]:
    """
    Calls Qt's 'QToolButton *QAccessibleToolButton::toolButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletoolbutton.html#toolButton

    Returns
    -------

    Optional[QToolButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QToolButton *QAccessibleToolButton::toolButton() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleToolButton10toolButtonEv',
    )
    from . import QToolButton
    return QToolButton._cuteAt(address)

  def isSplitButton(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleToolButton::isSplitButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletoolbutton.html#isSplitButton
    """
    #  bool QAccessibleToolButton::isSplitButton() const
    return self.uglySide.call(
        'ritual_ZNK21QAccessibleToolButton13isSplitButtonEv',
    )

  def menu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QAccessibleToolButton::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletoolbutton.html#menu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QAccessibleToolButton::menu() const
    address = self.uglySide.call('ritual_ZNK21QAccessibleToolButton4menuEv')
    from . import QMenu
    return QMenu._cuteAt(address)

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
    Qt's 'QAccessibleToolButton::QAccessibleToolButton(QWidget *w)': leans on
    'non-virtual thunk to QAccessibleButton::keyBindingsForAction(QString
    const&) const', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleToolButton.__init__' has no cute function yet. Qt's "
        "'QAccessibleToolButton::QAccessibleToolButton(QWidget *w)': leans "
        "on 'non-virtual thunk to "
        "QAccessibleButton::keyBindingsForAction(QString const&) const', "
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

  @overload(str)
  def doAction(self, actionName: str) -> None:
    """
    Calls Qt's 'void QAccessibleToolButton::doAction(const QString
    &actionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletoolbutton.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleToolButton::doAction(const QString &actionName)
    ritual = 'ritual_ZN21QAccessibleToolButton8doActionERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAccessibleToolButton8doActionERK7QString'
    self.uglySide.call(ritual, actionName)
