"""
QAccessibleGroupBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleGroupBox to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QStringList
from ..QtGui import QAccessible
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGroupBox


class QAccessibleGroupBox(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleGroupBox: a plain Python object standing
  in front of one C++ QAccessibleGroupBox.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleGroupBox
  is built on Qt's QAccessibleWidgetV2, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleGroupBox that has a ritual and that
  Python can call so far, 7 names in all: 'state', 'role', 'text',
  'actionNames', 'doAction', 'keyBindingsForAction', 'groupBox'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<std::pair<QAccessibleInterface *, QAccessible::Relation>>
    QAccessibleGroupBox::relations(QAccessible::Relation match) const': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 leans on 'QAccessibleGroupBox.

  What to expect
  --------------

  - The C++ QAccessibleGroupBox is created at the first use, not by
    'QAccessibleGroupBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleGroupBox.
  - Each name of Qt's QAccessibleGroupBox that has no cute function yet,
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
  __qt_class__ = 'QAccessibleGroupBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleGroupBox::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblegroupbox.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleGroupBox::state() const
    ritual = 'ritual_ZNK19QAccessibleGroupBox5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleGroupBox5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleGroupBox::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblegroupbox.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleGroupBox::role() const
    ritual = 'ritual_ZNK19QAccessibleGroupBox4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleGroupBox4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleGroupBox::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblegroupbox.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleGroupBox::text(QAccessible::Text t) const
    return self.uglySide.call(
        'ritual_ZNK19QAccessibleGroupBox4textEN11QAccessible4TextE', t.value,
    )

  def actionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleGroupBox::actionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblegroupbox.html#actionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleGroupBox::actionNames() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleGroupBox11actionNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def keyBindingsForAction(self, a0: str) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleGroupBox::keyBindingsForAction(const
    QString &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblegroupbox.html#keyBindingsForAction

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleGroupBox::keyBindingsForAction(const QString
    #      &a0) const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleGroupBox20keyBindingsForActionERK7QString',
        a0,
    )
    return QStringList._cuteOwning(address)

  def groupBox(self) -> Optional[QGroupBox]:
    """
    Calls Qt's 'QGroupBox *QAccessibleGroupBox::groupBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblegroupbox.html#groupBox

    Returns
    -------

    Optional[QGroupBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGroupBox *QAccessibleGroupBox::groupBox() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleGroupBox8groupBoxEv',
    )
    from . import QGroupBox
    return QGroupBox._cuteAt(address)

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
    Qt's 'QAccessibleGroupBox::QAccessibleGroupBox(QWidget *w)': leans on
    'QAccessibleGroupBox::text(QAccessible::Text) const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QAccessibleGroupBox.__init__' has no cute function yet. Qt's "
        "'QAccessibleGroupBox::QAccessibleGroupBox(QWidget *w)': leans on "
        "'QAccessibleGroupBox::text(QAccessible::Text) const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
    Calls Qt's 'void QAccessibleGroupBox::doAction(const QString
    &actionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblegroupbox.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleGroupBox::doAction(const QString &actionName)
    ritual = 'ritual_ZN19QAccessibleGroupBox8doActionERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleGroupBox8doActionERK7QString'
    self.uglySide.call(ritual, actionName)
