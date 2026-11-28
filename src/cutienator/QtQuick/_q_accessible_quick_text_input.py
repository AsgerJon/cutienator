"""
QAccessibleQuickTextInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qaccessiblequicktextinput_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleQuickTextInput to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleEditableTextInterface
from . import QAccessibleQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickTextInput
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTextInput = WAIT['QQuickTextInput']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickTextInput(QAccessibleQuickItem, QAccessibleEditableTextInterface):
  """
  The cute side of Qt's QAccessibleQuickTextInput: a plain Python object
  standing in front of one C++ QAccessibleQuickTextInput.

  It is built on the cute 'QAccessibleQuickItem', as Qt's
  QAccessibleQuickTextInput is built on Qt's QAccessibleQuickItem, and has
  everything that class has. It is built on the cute
  'QAccessibleEditableTextInterface' as well, as Qt's
  QAccessibleQuickTextInput is built on Qt's QAccessibleEditableTextInterface
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickTextInput that has a ritual and that
  Python can call so far, 6 names in all: 'removeSelection', 'setSelection',
  'deleteText', 'insertText', 'replaceText', 'textInput'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleQuickTextInput::interface_cast(QAccessible::InterfaceType
    a0)': gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickTextInput is created at the first use, not by
    'QAccessibleQuickTextInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickTextInput.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickTextInput'

  #  Qt's QAccessibleQuickTextInput is built on more than one class. The part
  #  of a C++ QAccessibleQuickTextInput that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleEditableTextInterface':
          'ritual_cast_QAccessibleQuickTextInput_QAccessibleEditableTextInterface',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textInput(self) -> Optional[QQuickTextInput]:
    """
    Calls Qt's 'QQuickTextInput *QAccessibleQuickTextInput::textInput()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicktextinput.html#textInput

    Returns
    -------

    Optional[QQuickTextInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextInput *QAccessibleQuickTextInput::textInput() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleQuickTextInput9textInputEv',
    )
    from . import QQuickTextInput
    return QQuickTextInput._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  def setSelection(
      self,
      selectionIndex: int,
      startOffset: int,
      endOffset: int,
  ) -> None:
    """
    Calls Qt's 'void QAccessibleQuickTextInput::setSelection(int
    selectionIndex, int startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicktextinput.html#setSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleQuickTextInput::setSelection(int selectionIndex, int
    #      startOffset, int endOffset)
    ritual = 'ritual_ZN25QAccessibleQuickTextInput12setSelectionEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QAccessibleQuickTextInput12setSelectionEiii'
    self.uglySide.call(ritual, selectionIndex, startOffset, endOffset)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickTextInput)
  @overload(NoneType)
  def __init__(self, textEdit: Optional[QQuickTextInput]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickTextInput::QAccessibleQuickTextInput(QQuickTextInput
    *textEdit)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicktextinput.html

    Parameters
    ----------

    textEdit : Optional[QQuickTextInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickTextInput::QAccessibleQuickTextInput(QQuickTextInput
    #      *textEdit)
    self._noteCreation(QAccessibleQuickTextInput, lambda: Rituals.call(
        'ritual_ZN25QAccessibleQuickTextInputC1EP15QQuickTextInput',
        self._addressOf(textEdit),
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

  @overload(int)
  def removeSelection(self, selectionIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleQuickTextInput::removeSelection(int
    selectionIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicktextinput.html#removeSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.
    """
    #  void QAccessibleQuickTextInput::removeSelection(int selectionIndex)
    ritual = 'ritual_ZN25QAccessibleQuickTextInput15removeSelectionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QAccessibleQuickTextInput15removeSelectionEi'
    self.uglySide.call(ritual, selectionIndex)

  @overload(int, int)
  def deleteText(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleQuickTextInput::deleteText(int startOffset,
    int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicktextinput.html#deleteText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleQuickTextInput::deleteText(int startOffset, int
    #      endOffset)
    ritual = 'ritual_ZN25QAccessibleQuickTextInput10deleteTextEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QAccessibleQuickTextInput10deleteTextEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int, str)
  def insertText(self, offset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleQuickTextInput::insertText(int offset, const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicktextinput.html#insertText

    Parameters
    ----------

    offset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleQuickTextInput::insertText(int offset, const QString
    #      &text)
    ritual = 'ritual_ZN25QAccessibleQuickTextInput10insertTextEiRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAccessibleQuickTextInput10insertTextEiRK7QString')
    self.uglySide.call(ritual, offset, text)

  @overload(int, int, str)
  def replaceText(self, startOffset: int, endOffset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleQuickTextInput::replaceText(int startOffset,
    int endOffset, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicktextinput.html#replaceText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleQuickTextInput::replaceText(int startOffset, int
    #      endOffset, const QString &text)
    ritual = 'ritual_ZN25QAccessibleQuickTextInput11replaceTextEiiRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAccessibleQuickTextInput11replaceTextEiiRK7QStri'
          'ng')
    self.uglySide.call(ritual, startOffset, endOffset, text)
