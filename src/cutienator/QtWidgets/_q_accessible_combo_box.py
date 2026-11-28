"""
QAccessibleComboBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleComboBox to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QStringList
from ..QtGui import QAccessible, QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QComboBox

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleComboBox(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleComboBox: a plain Python object standing
  in front of one C++ QAccessibleComboBox.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleComboBox
  is built on Qt's QAccessibleWidgetV2, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleComboBox that has a ritual and that
  Python can call so far, 12 names in all: 'childCount', 'childAt',
  'indexOfChild', 'child', 'focusChild', 'text', 'state', 'actionNames',
  'localizedActionDescription', 'doAction', 'keyBindingsForAction',
  'comboBox'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleComboBox.

  What to expect
  --------------

  - The C++ QAccessibleComboBox is created at the first use, not by
    'QAccessibleComboBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleComboBox.
  - Each name of Qt's QAccessibleComboBox that has no cute function yet,
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
  __qt_class__ = 'QAccessibleComboBox'

  #  A C++ QAccessibleComboBox Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleComboBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleComboBox::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecombobox.html#childCount
    """
    #  int QAccessibleComboBox::childCount() const
    ritual = 'ritual_ZNK19QAccessibleComboBox10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleComboBox10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleComboBox::childAt(int x, int
    y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecombobox.html#childAt

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
    #  QAccessibleInterface *QAccessibleComboBox::childAt(int x, int y) const
    ritual = 'ritual_ZNK19QAccessibleComboBox7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleComboBox7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleComboBox::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecombobox.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleComboBox::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK19QAccessibleComboBox12indexOfChildEPK20QAccessibleInter'
        'face')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAccessibleComboBox12indexOfChildEPK20QAccessibl'
          'eInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleComboBox::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecombobox.html#child

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
    #  QAccessibleInterface *QAccessibleComboBox::child(int index) const
    ritual = 'ritual_ZNK19QAccessibleComboBox5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleComboBox5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleComboBox::focusChild()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecombobox.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleComboBox::focusChild() const
    ritual = 'ritual_ZNK19QAccessibleComboBox10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleComboBox10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleComboBox::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecombobox.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleComboBox::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK19QAccessibleComboBox4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAccessibleComboBox4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, t.value)

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleComboBox::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecombobox.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleComboBox::state() const
    ritual = 'ritual_ZNK19QAccessibleComboBox5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleComboBox5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def actionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleComboBox::actionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecombobox.html#actionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleComboBox::actionNames() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleComboBox11actionNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def localizedActionDescription(self, actionName: str) -> str:
    """
    Calls Qt's 'QString QAccessibleComboBox::localizedActionDescription(const
    QString &actionName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecombobox.html

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleComboBox::localizedActionDescription(const QString
    #      &actionName) const
    ritual = (
        'ritual_ZNK19QAccessibleComboBox26localizedActionDescriptionERK7QSt'
        'ring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAccessibleComboBox26localizedActionDescriptionE'
          'RK7QString')
    return self.uglySide.call(ritual, actionName)

  @overload(str)
  def keyBindingsForAction(self, actionName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleComboBox::keyBindingsForAction(const
    QString &actionName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecombobox.html#keyBindingsForAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleComboBox::keyBindingsForAction(const QString
    #      &actionName) const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleComboBox20keyBindingsForActionERK7QString',
        actionName,
    )
    return QStringList._cuteOwning(address)

  def comboBox(self) -> Optional[QComboBox]:
    """
    Calls Qt's 'QComboBox *QAccessibleComboBox::comboBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecombobox.html#comboBox

    Returns
    -------

    Optional[QComboBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QComboBox *QAccessibleComboBox::comboBox() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleComboBox8comboBoxEv',
    )
    from . import QComboBox
    return QComboBox._cuteAt(address)

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
    Qt's 'QAccessibleComboBox::QAccessibleComboBox(QWidget *w)': leans on
    'non-virtual thunk to QAccessibleComboBox::actionNames() const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleComboBox.__init__' has no cute function yet. Qt's "
        "'QAccessibleComboBox::QAccessibleComboBox(QWidget *w)': leans on "
        "'non-virtual thunk to QAccessibleComboBox::actionNames() const', "
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
    Calls Qt's 'void QAccessibleComboBox::doAction(const QString
    &actionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecombobox.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleComboBox::doAction(const QString &actionName)
    ritual = 'ritual_ZN19QAccessibleComboBox8doActionERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleComboBox8doActionERK7QString'
    self.uglySide.call(ritual, actionName)
