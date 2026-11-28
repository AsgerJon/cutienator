"""
QAccessibleLineEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleLineEdit to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QAccessible, QAccessibleEditableTextInterface
from ..QtGui import QAccessibleTextInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect
  from . import QLineEdit
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QAccessibleLineEdit(QAccessibleWidgetV2, QAccessibleTextInterface, QAccessibleEditableTextInterface):
  """
  The cute side of Qt's QAccessibleLineEdit: a plain Python object standing
  in front of one C++ QAccessibleLineEdit.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleLineEdit
  is built on Qt's QAccessibleWidgetV2, and has everything that class has. It
  is built on the cute 'QAccessibleTextInterface' as well, as Qt's
  QAccessibleLineEdit is built on Qt's QAccessibleTextInterface too, and has
  everything that class has. It is built on the cute
  'QAccessibleEditableTextInterface' as well, as Qt's QAccessibleLineEdit is
  built on Qt's QAccessibleEditableTextInterface too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QAccessibleLineEdit that has a ritual and that
  Python can call so far, 17 names in all: 'text', 'setText', 'state',
  'addSelection', 'cursorPosition', 'characterRect', 'selectionCount',
  'offsetAtPoint', 'removeSelection', 'setCursorPosition', 'setSelection',
  'characterCount', 'scrollToSubstring', 'deleteText', 'insertText',
  'replaceText', 'lineEdit'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleLineEdit::interface_cast(QAccessible::InterfaceType t)':
    gives 'void', which has no cute class yet.
  - Qt's 'QString QAccessibleLineEdit::attributes(int offset, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
  - Qt's 'void QAccessibleLineEdit::selection(int selectionIndex, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
  - Qt's 'QString QAccessibleLineEdit::textBeforeOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleLineEdit::textAfterOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleLineEdit::textAtOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.

  What has no ritual
  ------------------

  1 of the 25 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleLineEdit.

  What to expect
  --------------

  - The C++ QAccessibleLineEdit is created at the first use, not by
    'QAccessibleLineEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleLineEdit.
  - Each name of Qt's QAccessibleLineEdit that has no cute function yet,
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
  __qt_class__ = 'QAccessibleLineEdit'

  #  Qt's QAccessibleLineEdit is built on more than one class. The part of a
  #  C++ QAccessibleLineEdit that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleTextInterface':
          'ritual_cast_QAccessibleLineEdit_QAccessibleTextInterface',
      'QAccessibleEditableTextInterface':
          'ritual_cast_QAccessibleLineEdit_QAccessibleEditableTextInterface',
  }

  #  A C++ QAccessibleLineEdit Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleLineEdit'

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
    Calls Qt's 'QString QAccessibleLineEdit::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelineedit.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleLineEdit::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK19QAccessibleLineEdit4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAccessibleLineEdit4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, t.value)

  @overload(int, int)
  def text(self, startOffset: int, endOffset: int) -> str:
    """
    Calls Qt's 'QString QAccessibleLineEdit::text(int startOffset, int
    endOffset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelineedit.html#text

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleLineEdit::text(int startOffset, int endOffset)
    #      const
    ritual = 'ritual_ZNK19QAccessibleLineEdit4textEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleLineEdit4textEii'
    return self.uglySide.call(ritual, startOffset, endOffset)

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleLineEdit::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelineedit.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleLineEdit::state() const
    ritual = 'ritual_ZNK19QAccessibleLineEdit5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleLineEdit5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleLineEdit::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#cursorPosition
    """
    #  int QAccessibleLineEdit::cursorPosition() const
    ritual = 'ritual_ZNK19QAccessibleLineEdit14cursorPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleLineEdit14cursorPositionEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def characterRect(self, offset: int) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleLineEdit::characterRect(int offset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#characterRect

    Parameters
    ----------

    offset : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleLineEdit::characterRect(int offset) const
    ritual = 'ritual_ZNK19QAccessibleLineEdit13characterRectEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleLineEdit13characterRectEi'
    address = self.uglySide.call(ritual, offset)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def selectionCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleLineEdit::selectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#selectionCount
    """
    #  int QAccessibleLineEdit::selectionCount() const
    ritual = 'ritual_ZNK19QAccessibleLineEdit14selectionCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleLineEdit14selectionCountEv'
    return self.uglySide.call(ritual)

  @overload(QPoint)
  def offsetAtPoint(self, point: QPoint) -> int:
    """
    Calls Qt's 'int QAccessibleLineEdit::offsetAtPoint(const QPoint &point)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#offsetAtPoint

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QAccessibleLineEdit::offsetAtPoint(const QPoint &point) const
    ritual = 'ritual_ZNK19QAccessibleLineEdit13offsetAtPointERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleLineEdit13offsetAtPointERK6QPoint'
    return self.uglySide.call(ritual, self._valueOf(point))

  def characterCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleLineEdit::characterCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#characterCount
    """
    #  int QAccessibleLineEdit::characterCount() const
    ritual = 'ritual_ZNK19QAccessibleLineEdit14characterCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleLineEdit14characterCountEv'
    return self.uglySide.call(ritual)

  def lineEdit(self) -> Optional[QLineEdit]:
    """
    Calls Qt's 'QLineEdit *QAccessibleLineEdit::lineEdit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelineedit.html#lineEdit

    Returns
    -------

    Optional[QLineEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineEdit *QAccessibleLineEdit::lineEdit() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleLineEdit8lineEditEv',
    )
    from . import QLineEdit
    return QLineEdit._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, t: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::setText(QAccessible::Text t, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelineedit.html#setText

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleLineEdit::setText(QAccessible::Text t, const QString
    #      &text)
    ritual = (
        'ritual_ZN19QAccessibleLineEdit7setTextEN11QAccessible4TextERK7QStr'
        'ing')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAccessibleLineEdit7setTextEN11QAccessible4TextER'
          'K7QString')
    self.uglySide.call(ritual, t.value, text)

  @overload(int)
  def setCursorPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::setCursorPosition(int position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#setCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAccessibleLineEdit::setCursorPosition(int position)
    ritual = 'ritual_ZN19QAccessibleLineEdit17setCursorPositionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit17setCursorPositionEi'
    self.uglySide.call(ritual, position)

  @overload(int, int, int)
  def setSelection(
      self,
      selectionIndex: int,
      startOffset: int,
      endOffset: int,
  ) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::setSelection(int selectionIndex,
    int startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#setSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleLineEdit::setSelection(int selectionIndex, int
    #      startOffset, int endOffset)
    ritual = 'ritual_ZN19QAccessibleLineEdit12setSelectionEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit12setSelectionEiii'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAccessibleLineEdit::QAccessibleLineEdit(QWidget *o, const QString
    &name)': leans on 'non-virtual thunk to
    QAccessibleLineEdit::attributes(int, int*, int*) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleLineEdit.__init__' has no cute function yet. Qt's "
        "'QAccessibleLineEdit::QAccessibleLineEdit(QWidget *o, const "
        "QString &name)': leans on 'non-virtual thunk to "
        "QAccessibleLineEdit::attributes(int, int*, int*) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(int, int)
  def addSelection(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::addSelection(int startOffset, int
    endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#addSelection

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleLineEdit::addSelection(int startOffset, int endOffset)
    ritual = 'ritual_ZN19QAccessibleLineEdit12addSelectionEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit12addSelectionEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int)
  def removeSelection(self, selectionIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::removeSelection(int
    selectionIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#removeSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.
    """
    #  void QAccessibleLineEdit::removeSelection(int selectionIndex)
    ritual = 'ritual_ZN19QAccessibleLineEdit15removeSelectionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit15removeSelectionEi'
    self.uglySide.call(ritual, selectionIndex)

  @overload(int, int)
  def scrollToSubstring(self, startIndex: int, endIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::scrollToSubstring(int startIndex,
    int endIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#scrollToSubstring

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  void QAccessibleLineEdit::scrollToSubstring(int startIndex, int
    #      endIndex)
    ritual = 'ritual_ZN19QAccessibleLineEdit17scrollToSubstringEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit17scrollToSubstringEii'
    self.uglySide.call(ritual, startIndex, endIndex)

  @overload(int, int)
  def deleteText(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::deleteText(int startOffset, int
    endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#deleteText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleLineEdit::deleteText(int startOffset, int endOffset)
    ritual = 'ritual_ZN19QAccessibleLineEdit10deleteTextEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit10deleteTextEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int, str)
  def insertText(self, offset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::insertText(int offset, const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#insertText

    Parameters
    ----------

    offset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleLineEdit::insertText(int offset, const QString &text)
    ritual = 'ritual_ZN19QAccessibleLineEdit10insertTextEiRK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit10insertTextEiRK7QString'
    self.uglySide.call(ritual, offset, text)

  @overload(int, int, str)
  def replaceText(self, startOffset: int, endOffset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleLineEdit::replaceText(int startOffset, int
    endOffset, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelineedit.html#replaceText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleLineEdit::replaceText(int startOffset, int endOffset,
    #      const QString &text)
    ritual = 'ritual_ZN19QAccessibleLineEdit11replaceTextEiiRK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleLineEdit11replaceTextEiiRK7QString'
    self.uglySide.call(ritual, startOffset, endOffset, text)
