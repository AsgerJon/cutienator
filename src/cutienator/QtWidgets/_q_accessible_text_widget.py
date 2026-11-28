"""
QAccessibleTextWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleTextWidget to be private: it declares the class in a
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
  from ..QtGui import QTextCursor, QTextDocument
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QTextCursor = WAIT['QTextCursor']


class QAccessibleTextWidget(QAccessibleWidgetV2, QAccessibleTextInterface, QAccessibleEditableTextInterface):
  """
  The cute side of Qt's QAccessibleTextWidget: a plain Python object standing
  in front of one C++ QAccessibleTextWidget.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleTextWidget is built on Qt's QAccessibleWidgetV2, and has
  everything that class has. It is built on the cute
  'QAccessibleTextInterface' as well, as Qt's QAccessibleTextWidget is built
  on Qt's QAccessibleTextInterface too, and has everything that class has. It
  is built on the cute 'QAccessibleEditableTextInterface' as well, as Qt's
  QAccessibleTextWidget is built on Qt's QAccessibleEditableTextInterface
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTextWidget that has a ritual and that
  Python can call so far, 20 names in all: 'state', 'selectionCount',
  'addSelection', 'removeSelection', 'setSelection', 'cursorPosition',
  'setCursorPosition', 'text', 'characterCount', 'characterRect',
  'offsetAtPoint', 'deleteText', 'insertText', 'replaceText',
  'textCursorForRange', 'scrollBarPosition', 'textCursor', 'setTextCursor',
  'textDocument', 'viewport'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QAccessibleTextWidget::selection(int selectionIndex, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
  - Qt's 'QString QAccessibleTextWidget::textBeforeOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleTextWidget::textAfterOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleTextWidget::textAtOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleTextWidget::attributes(int offset, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.

  What has no ritual
  ------------------

  1 of the 26 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleTextWidget.

  What to expect
  --------------

  - The C++ QAccessibleTextWidget is created at the first use, not by
    'QAccessibleTextWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTextWidget.
  - Each name of Qt's QAccessibleTextWidget that has no cute function yet,
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
  __qt_class__ = 'QAccessibleTextWidget'

  #  Qt's QAccessibleTextWidget is built on more than one class. The part of
  #  a C++ QAccessibleTextWidget that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleTextInterface':
          'ritual_cast_QAccessibleTextWidget_QAccessibleTextInterface',
      'QAccessibleEditableTextInterface':
          'ritual_cast_QAccessibleTextWidget_QAccessibleEditableTextInterface',
  }

  #  A C++ QAccessibleTextWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTextWidget'

  #  The functions Qt calls itself that QAccessibleTextWidget is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'scrollBarPosition': (
          ('_ZNK21QAccessibleTextWidget17scrollBarPositionEv',
           ('address', 'value', 'QtCore:QPoint'),
           ()),
      ),
      'textCursor': (
          ('_ZNK21QAccessibleTextWidget10textCursorEv',
           ('address', 'value', 'QtGui:QTextCursor'),
           ()),
      ),
      'setTextCursor': (
          ('_ZN21QAccessibleTextWidget13setTextCursorERK11QTextCursor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextCursor'),
           )),
      ),
      'textDocument': (
          ('_ZNK21QAccessibleTextWidget12textDocumentEv',
           ('address', 'address', 'QtGui:QTextDocument'),
           ()),
      ),
      'viewport': (
          ('_ZNK21QAccessibleTextWidget8viewportEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleTextWidget::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextwidget.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleTextWidget::state() const
    ritual = 'ritual_ZNK21QAccessibleTextWidget5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleTextWidget5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def selectionCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextWidget::selectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#selectionCount
    """
    #  int QAccessibleTextWidget::selectionCount() const
    ritual = 'ritual_ZNK21QAccessibleTextWidget14selectionCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleTextWidget14selectionCountEv'
    return self.uglySide.call(ritual)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextWidget::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#cursorPosition
    """
    #  int QAccessibleTextWidget::cursorPosition() const
    ritual = 'ritual_ZNK21QAccessibleTextWidget14cursorPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleTextWidget14cursorPositionEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def text(self, startOffset: int, endOffset: int) -> str:
    """
    Calls Qt's 'QString QAccessibleTextWidget::text(int startOffset, int
    endOffset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextwidget.html#text

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
    #  QString QAccessibleTextWidget::text(int startOffset, int endOffset)
    #      const
    ritual = 'ritual_ZNK21QAccessibleTextWidget4textEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleTextWidget4textEii'
    return self.uglySide.call(ritual, startOffset, endOffset)

  def characterCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextWidget::characterCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#characterCount
    """
    #  int QAccessibleTextWidget::characterCount() const
    ritual = 'ritual_ZNK21QAccessibleTextWidget14characterCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleTextWidget14characterCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def characterRect(self, offset: int) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleTextWidget::characterRect(int offset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#characterRect

    Parameters
    ----------

    offset : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleTextWidget::characterRect(int offset) const
    ritual = 'ritual_ZNK21QAccessibleTextWidget13characterRectEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleTextWidget13characterRectEi'
    address = self.uglySide.call(ritual, offset)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def offsetAtPoint(self, point: QPoint) -> int:
    """
    Calls Qt's 'int QAccessibleTextWidget::offsetAtPoint(const QPoint &point)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#offsetAtPoint

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QAccessibleTextWidget::offsetAtPoint(const QPoint &point) const
    ritual = 'ritual_ZNK21QAccessibleTextWidget13offsetAtPointERK6QPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAccessibleTextWidget13offsetAtPointERK6QPoint')
    return self.uglySide.call(ritual, self._valueOf(point))

  @overload(int, int)
  def textCursorForRange(
      self,
      startOffset: int,
      endOffset: int,
  ) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QAccessibleTextWidget::textCursorForRange(int
    startOffset, int endOffset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#textCursorForRange

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QAccessibleTextWidget::textCursorForRange(int startOffset,
    #      int endOffset) const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleTextWidget18textCursorForRangeEii',
        startOffset, endOffset,
    )
    from ..QtGui import QTextCursor
    return QTextCursor._cuteOwning(address)

  def scrollBarPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAccessibleTextWidget::scrollBarPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#scrollBarPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAccessibleTextWidget::scrollBarPosition() const
    ritual = 'ritual_ZNK21QAccessibleTextWidget17scrollBarPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleTextWidget17scrollBarPositionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def textCursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QAccessibleTextWidget::textCursor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#textCursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QAccessibleTextWidget::textCursor() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleTextWidget10textCursorEv',
    )
    from ..QtGui import QTextCursor
    return QTextCursor._cuteOwning(address)

  def textDocument(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QAccessibleTextWidget::textDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#textDocument

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QAccessibleTextWidget::textDocument() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleTextWidget12textDocumentEv',
    )
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  def viewport(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAccessibleTextWidget::viewport() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#viewport

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAccessibleTextWidget::viewport() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleTextWidget8viewportEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

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
    Calls Qt's 'void QAccessibleTextWidget::setSelection(int selectionIndex,
    int startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#setSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleTextWidget::setSelection(int selectionIndex, int
    #      startOffset, int endOffset)
    ritual = 'ritual_ZN21QAccessibleTextWidget12setSelectionEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAccessibleTextWidget12setSelectionEiii'
    self.uglySide.call(ritual, selectionIndex, startOffset, endOffset)

  @overload(int)
  def setCursorPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextWidget::setCursorPosition(int position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#setCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAccessibleTextWidget::setCursorPosition(int position)
    ritual = 'ritual_ZN21QAccessibleTextWidget17setCursorPositionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAccessibleTextWidget17setCursorPositionEi'
    self.uglySide.call(ritual, position)

  @overload(QTextCursor)
  def setTextCursor(self, a0: QTextCursor) -> None:
    """
    Calls Qt's 'void QAccessibleTextWidget::setTextCursor(const QTextCursor
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#setTextCursor

    Parameters
    ----------

    a0 : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QAccessibleTextWidget::setTextCursor(const QTextCursor &a0)
    self.uglySide.call(
        'ritual_ZN21QAccessibleTextWidget13setTextCursorERK11QTextCursor',
        self._valueOf(a0),
    )

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
    Qt's 'QAccessibleTextWidget::QAccessibleTextWidget(QWidget *o,
    QAccessible::Role r, const QString &name)': leans on 'non-virtual thunk
    to QAccessibleTextWidget::attributes(int, int*, int*) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleTextWidget.__init__' has no cute function yet. Qt's "
        "'QAccessibleTextWidget::QAccessibleTextWidget(QWidget *o, "
        "QAccessible::Role r, const QString &name)': leans on 'non-virtual "
        "thunk to QAccessibleTextWidget::attributes(int, int*, int*) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'void QAccessibleTextWidget::addSelection(int startOffset, int
    endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#addSelection

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleTextWidget::addSelection(int startOffset, int
    #      endOffset)
    ritual = 'ritual_ZN21QAccessibleTextWidget12addSelectionEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAccessibleTextWidget12addSelectionEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int)
  def removeSelection(self, selectionIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextWidget::removeSelection(int
    selectionIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#removeSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.
    """
    #  void QAccessibleTextWidget::removeSelection(int selectionIndex)
    ritual = 'ritual_ZN21QAccessibleTextWidget15removeSelectionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAccessibleTextWidget15removeSelectionEi'
    self.uglySide.call(ritual, selectionIndex)

  @overload(int, int)
  def deleteText(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextWidget::deleteText(int startOffset, int
    endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#deleteText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleTextWidget::deleteText(int startOffset, int endOffset)
    ritual = 'ritual_ZN21QAccessibleTextWidget10deleteTextEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAccessibleTextWidget10deleteTextEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int, str)
  def insertText(self, offset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleTextWidget::insertText(int offset, const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#insertText

    Parameters
    ----------

    offset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleTextWidget::insertText(int offset, const QString
    #      &text)
    ritual = 'ritual_ZN21QAccessibleTextWidget10insertTextEiRK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAccessibleTextWidget10insertTextEiRK7QString'
    self.uglySide.call(ritual, offset, text)

  @overload(int, int, str)
  def replaceText(self, startOffset: int, endOffset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleTextWidget::replaceText(int startOffset, int
    endOffset, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextwidget.html#replaceText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleTextWidget::replaceText(int startOffset, int
    #      endOffset, const QString &text)
    ritual = 'ritual_ZN21QAccessibleTextWidget11replaceTextEiiRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAccessibleTextWidget11replaceTextEiiRK7QString')
    self.uglySide.call(ritual, startOffset, endOffset, text)
