"""
QAccessibleButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleButton to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtGui import QAccessible
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from . import QAbstractButton

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleButton(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleButton: a plain Python object standing in
  front of one C++ QAccessibleButton.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleButton is
  built on Qt's QAccessibleWidgetV2, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleButton that has a ritual and that Python
  can call so far, 9 names in all: 'tr', 'text', 'state', 'rect', 'role',
  'actionNames', 'doAction', 'keyBindingsForAction', 'button'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleButton.

  What to expect
  --------------

  - The C++ QAccessibleButton is created at the first use, not by
    'QAccessibleButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleButton.
  - Each name of Qt's QAccessibleButton that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QAccessibleButton::tr(const char *sourceText, const
    char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleButton::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN17QAccessibleButton2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleButton'

  #  A C++ QAccessibleButton Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleButton::text(QAccessible::Text t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleButton::text(QAccessible::Text t) const
    return self.uglySide.call(
        'ritual_ZNK17QAccessibleButton4textEN11QAccessible4TextE', t.value,
    )

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleButton::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleButton::state() const
    ritual = 'ritual_ZNK17QAccessibleButton5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleButton5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleButton::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleButton::rect() const
    ritual = 'ritual_ZNK17QAccessibleButton4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleButton4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleButton::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleButton::role() const
    ritual = 'ritual_ZNK17QAccessibleButton4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleButton4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def actionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleButton::actionNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#actionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleButton::actionNames() const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleButton11actionNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def keyBindingsForAction(self, actionName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleButton::keyBindingsForAction(const
    QString &actionName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblebutton.html#keyBindingsForAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleButton::keyBindingsForAction(const QString
    #      &actionName) const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleButton20keyBindingsForActionERK7QString',
        actionName,
    )
    return QStringList._cuteOwning(address)

  def button(self) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QAccessibleButton::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#button

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QAccessibleButton::button() const
    address = self.uglySide.call('ritual_ZNK17QAccessibleButton6buttonEv')
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

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
    Qt's 'QAccessibleButton::QAccessibleButton(QWidget *w)': leans on
    'non-virtual thunk to QAccessibleButton::actionNames() const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleButton.__init__' has no cute function yet. Qt's "
        "'QAccessibleButton::QAccessibleButton(QWidget *w)': leans on "
        "'non-virtual thunk to QAccessibleButton::actionNames() const', "
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
    Calls Qt's 'void QAccessibleButton::doAction(const QString &actionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblebutton.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleButton::doAction(const QString &actionName)
    ritual = 'ritual_ZN17QAccessibleButton8doActionERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAccessibleButton8doActionERK7QString'
    self.uglySide.call(ritual, actionName)
