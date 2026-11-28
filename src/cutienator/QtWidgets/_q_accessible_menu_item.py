"""
QAccessibleMenuItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleMenuItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QStringList
from ..QtGui import QAccessible, QAccessibleActionInterface
from ..QtGui import QAccessibleInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRect
  from ..QtGui import QAction, QWindow
  from . import QWidget

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleMenuItem(QAccessibleInterface, QAccessibleActionInterface):
  """
  The cute side of Qt's QAccessibleMenuItem: a plain Python object standing
  in front of one C++ QAccessibleMenuItem.

  It is built on the cute 'QAccessibleInterface', as Qt's QAccessibleMenuItem
  is built on Qt's QAccessibleInterface, and has everything that class has.
  It is built on the cute 'QAccessibleActionInterface' as well, as Qt's
  QAccessibleMenuItem is built on Qt's QAccessibleActionInterface too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleMenuItem that has a ritual and that
  Python can call so far, 18 names in all: 'childCount', 'childAt',
  'isValid', 'indexOfChild', 'parent', 'child', 'object', 'window', 'rect',
  'role', 'setText', 'state', 'text', 'actionNames', 'doAction',
  'keyBindingsForAction', 'owner', 'action'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleMenuItem::~QAccessibleMenuItem()': the destructor:
    Python never removes a C++ QAccessibleMenuItem.
  - Qt's 'void
    *QAccessibleMenuItem::interface_cast(QAccessible::InterfaceType t)':
    gives 'void', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleMenuItem.

  What to expect
  --------------

  - The C++ QAccessibleMenuItem is created at the first use, not by
    'QAccessibleMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleMenuItem.
  - Each name of Qt's QAccessibleMenuItem that has no cute function yet,
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
  __qt_class__ = 'QAccessibleMenuItem'

  #  Qt's QAccessibleMenuItem is built on more than one class. The part of a
  #  C++ QAccessibleMenuItem that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleActionInterface':
          'ritual_cast_QAccessibleMenuItem_QAccessibleActionInterface',
  }

  #  A C++ QAccessibleMenuItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleMenuItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleMenuItem::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemenuitem.html#childCount
    """
    #  int QAccessibleMenuItem::childCount() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMenuItem::childAt(int x, int
    y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#childAt

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
    #  QAccessibleInterface *QAccessibleMenuItem::childAt(int x, int y) const
    ritual = 'ritual_ZNK19QAccessibleMenuItem7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleMenuItem::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#isValid
    """
    #  bool QAccessibleMenuItem::isValid() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem7isValidEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleMenuItem::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemenuitem.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleMenuItem::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK19QAccessibleMenuItem12indexOfChildEPK20QAccessibleInter'
        'face')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAccessibleMenuItem12indexOfChildEPK20QAccessibl'
          'eInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMenuItem::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleMenuItem::parent() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMenuItem::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#child

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
    #  QAccessibleInterface *QAccessibleMenuItem::child(int index) const
    ritual = 'ritual_ZNK19QAccessibleMenuItem5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAccessibleMenuItem::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAccessibleMenuItem::object() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem6objectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem6objectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QAccessibleMenuItem::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QAccessibleMenuItem::window() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem6windowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem6windowEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleMenuItem::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleMenuItem::rect() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleMenuItem::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleMenuItem::role() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleMenuItem::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleMenuItem::state() const
    ritual = 'ritual_ZNK19QAccessibleMenuItem5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleMenuItem5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleMenuItem::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleMenuItem::text(QAccessible::Text t) const
    return self.uglySide.call(
        'ritual_ZNK19QAccessibleMenuItem4textEN11QAccessible4TextE', t.value,
    )

  def actionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleMenuItem::actionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemenuitem.html#actionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleMenuItem::actionNames() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleMenuItem11actionNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def keyBindingsForAction(self, actionName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleMenuItem::keyBindingsForAction(const
    QString &actionName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemenuitem.html#keyBindingsForAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleMenuItem::keyBindingsForAction(const QString
    #      &actionName) const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleMenuItem20keyBindingsForActionERK7QString',
        actionName,
    )
    return QStringList._cuteOwning(address)

  def owner(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAccessibleMenuItem::owner() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#owner

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAccessibleMenuItem::owner() const
    address = self.uglySide.call('ritual_ZNK19QAccessibleMenuItem5ownerEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def action(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QAccessibleMenuItem::action() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#action

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QAccessibleMenuItem::action() const
    address = self.uglySide.call('ritual_ZNK19QAccessibleMenuItem6actionEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, t: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleMenuItem::setText(QAccessible::Text t, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#setText

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleMenuItem::setText(QAccessible::Text t, const QString
    #      &text)
    ritual = (
        'ritual_ZN19QAccessibleMenuItem7setTextEN11QAccessible4TextERK7QStr'
        'ing')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAccessibleMenuItem7setTextEN11QAccessible4TextER'
          'K7QString')
    self.uglySide.call(ritual, t.value, text)

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
    Qt's 'QAccessibleMenuItem::QAccessibleMenuItem(QWidget *owner, QAction
    *w)': leans on 'non-virtual thunk to
    QAccessibleMenuItem::doAction(QString const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleMenuItem.__init__' has no cute function yet. Qt's "
        "'QAccessibleMenuItem::QAccessibleMenuItem(QWidget *owner, QAction "
        "*w)': leans on 'non-virtual thunk to "
        "QAccessibleMenuItem::doAction(QString const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'void QAccessibleMenuItem::doAction(const QString
    &actionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenuitem.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleMenuItem::doAction(const QString &actionName)
    ritual = 'ritual_ZN19QAccessibleMenuItem8doActionERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleMenuItem8doActionERK7QString'
    self.uglySide.call(ritual, actionName)
