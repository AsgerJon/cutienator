"""
QAccessibleTextEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleTextEdit to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QAccessible
from . import QAccessibleTextWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint
  from ..QtGui import QTextCursor, QTextDocument
  from . import QTextEdit, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextCursor = WAIT['QTextCursor']


class QAccessibleTextEdit(QAccessibleTextWidget):
  """
  The cute side of Qt's QAccessibleTextEdit: a plain Python object standing
  in front of one C++ QAccessibleTextEdit.

  It is built on the cute 'QAccessibleTextWidget', as Qt's
  QAccessibleTextEdit is built on Qt's QAccessibleTextWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTextEdit that has a ritual and that
  Python can call so far, 10 names in all: 'text', 'setText', 'state',
  'scrollToSubstring', 'textEdit', 'scrollBarPosition', 'textCursor',
  'setTextCursor', 'textDocument', 'viewport'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleTextEdit::interface_cast(QAccessible::InterfaceType t)':
    gives 'void', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleTextWidget.

  What to expect
  --------------

  - The C++ QAccessibleTextEdit is created at the first use, not by
    'QAccessibleTextEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTextEdit.
  - Each name of Qt's QAccessibleTextEdit that has no cute function yet,
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
  __qt_class__ = 'QAccessibleTextEdit'

  #  A C++ QAccessibleTextEdit Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTextEdit'

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
    Calls Qt's 'QString QAccessibleTextEdit::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextedit.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTextEdit::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK19QAccessibleTextEdit4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAccessibleTextEdit4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, t.value)

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleTextEdit::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextedit.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleTextEdit::state() const
    ritual = 'ritual_ZNK19QAccessibleTextEdit5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleTextEdit5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def textEdit(self) -> Optional[QTextEdit]:
    """
    Calls Qt's 'QTextEdit *QAccessibleTextEdit::textEdit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextedit.html#textEdit

    Returns
    -------

    Optional[QTextEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextEdit *QAccessibleTextEdit::textEdit() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibleTextEdit8textEditEv',
    )
    from . import QTextEdit
    return QTextEdit._cuteAt(address)

  def scrollBarPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAccessibleTextEdit::scrollBarPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextedit.html#scrollBarPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAccessibleTextEdit::scrollBarPosition() const
    ritual = 'ritual_ZNK19QAccessibleTextEdit17scrollBarPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleTextEdit17scrollBarPositionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def textCursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QAccessibleTextEdit::textCursor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextedit.html#textCursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QAccessibleTextEdit::textCursor() const
    ritual = 'ritual_ZNK19QAccessibleTextEdit10textCursorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleTextEdit10textCursorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QTextCursor
    return QTextCursor._cuteOwning(address)

  def textDocument(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QAccessibleTextEdit::textDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextedit.html#textDocument

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QAccessibleTextEdit::textDocument() const
    ritual = 'ritual_ZNK19QAccessibleTextEdit12textDocumentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleTextEdit12textDocumentEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  def viewport(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAccessibleTextEdit::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextedit.html#viewport

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAccessibleTextEdit::viewport() const
    ritual = 'ritual_ZNK19QAccessibleTextEdit8viewportEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAccessibleTextEdit8viewportEv'
    address = self.uglySide.call(ritual)
    from . import QWidget
    return QWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, t: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleTextEdit::setText(QAccessible::Text t, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextedit.html#setText

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleTextEdit::setText(QAccessible::Text t, const QString
    #      &text)
    ritual = (
        'ritual_ZN19QAccessibleTextEdit7setTextEN11QAccessible4TextERK7QStr'
        'ing')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAccessibleTextEdit7setTextEN11QAccessible4TextER'
          'K7QString')
    self.uglySide.call(ritual, t.value, text)

  @overload(QTextCursor)
  def setTextCursor(self, textCursor: QTextCursor) -> None:
    """
    Calls Qt's 'void QAccessibleTextEdit::setTextCursor(const QTextCursor
    &textCursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextedit.html#setTextCursor

    Parameters
    ----------

    textCursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QAccessibleTextEdit::setTextCursor(const QTextCursor &textCursor)
    ritual = 'ritual_ZN19QAccessibleTextEdit13setTextCursorERK11QTextCursor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAccessibleTextEdit13setTextCursorERK11QTextCurso'
          'r')
    self.uglySide.call(ritual, self._valueOf(textCursor))

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
    Qt's 'QAccessibleTextEdit::QAccessibleTextEdit(QWidget *o)': leans on
    'non-virtual thunk to QAccessibleTextWidget::attributes(int, int*, int*)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleTextEdit.__init__' has no cute function yet. Qt's "
        "'QAccessibleTextEdit::QAccessibleTextEdit(QWidget *o)': leans on "
        "'non-virtual thunk to QAccessibleTextWidget::attributes(int, int*, "
        "int*) const', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

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
  def scrollToSubstring(self, startIndex: int, endIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextEdit::scrollToSubstring(int startIndex,
    int endIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextedit.html#scrollToSubstring

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  void QAccessibleTextEdit::scrollToSubstring(int startIndex, int
    #      endIndex)
    ritual = 'ritual_ZN19QAccessibleTextEdit17scrollToSubstringEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibleTextEdit17scrollToSubstringEii'
    self.uglySide.call(ritual, startIndex, endIndex)
