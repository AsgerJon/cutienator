"""
QAccessibleAbstractSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleAbstractSpinBox to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QAccessible, QAccessibleEditableTextInterface
from ..QtGui import QAccessibleInterface, QAccessibleTextInterface
from ..QtGui import QAccessibleValueInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect, QVariant
  from . import QAbstractSpinBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QVariant = WAIT['QVariant']


class QAccessibleAbstractSpinBox(QAccessibleWidgetV2, QAccessibleValueInterface, QAccessibleTextInterface, QAccessibleEditableTextInterface):
  """
  The cute side of Qt's QAccessibleAbstractSpinBox: a plain Python object
  standing in front of one C++ QAccessibleAbstractSpinBox.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleAbstractSpinBox is built on Qt's QAccessibleWidgetV2, and has
  everything that class has. It is built on the cute
  'QAccessibleValueInterface' as well, as Qt's QAccessibleAbstractSpinBox is
  built on Qt's QAccessibleValueInterface too, and has everything that class
  has. It is built on the cute 'QAccessibleTextInterface' as well, as Qt's
  QAccessibleAbstractSpinBox is built on Qt's QAccessibleTextInterface too,
  and has everything that class has. It is built on the cute
  'QAccessibleEditableTextInterface' as well, as Qt's
  QAccessibleAbstractSpinBox is built on Qt's
  QAccessibleEditableTextInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleAbstractSpinBox that has a ritual and
  that Python can call so far, 22 names in all: 'state', 'text',
  'currentValue', 'setCurrentValue', 'maximumValue', 'minimumValue',
  'minimumStepSize', 'addSelection', 'cursorPosition', 'characterRect',
  'selectionCount', 'offsetAtPoint', 'removeSelection', 'setCursorPosition',
  'setSelection', 'characterCount', 'scrollToSubstring', 'deleteText',
  'insertText', 'replaceText', 'abstractSpinBox', 'lineEditIface'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleAbstractSpinBox::~QAccessibleAbstractSpinBox()': the
    destructor: Python never removes a C++ QAccessibleAbstractSpinBox.
  - Qt's 'void
    *QAccessibleAbstractSpinBox::interface_cast(QAccessible::InterfaceType
    t)': gives 'void', which has no cute class yet.
  - Qt's 'QString QAccessibleAbstractSpinBox::attributes(int offset, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
  - Qt's 'void QAccessibleAbstractSpinBox::selection(int selectionIndex, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
  - Qt's 'QString QAccessibleAbstractSpinBox::textBeforeOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *endOffset, int
    *startOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleAbstractSpinBox::textAfterOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleAbstractSpinBox::textAtOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.

  What has no ritual
  ------------------

  1 of the 31 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleAbstractSpinBox.

  What to expect
  --------------

  - The C++ QAccessibleAbstractSpinBox is created at the first use, not by
    'QAccessibleAbstractSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleAbstractSpinBox.
  - Each name of Qt's QAccessibleAbstractSpinBox that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleAbstractSpinBox'

  #  Qt's QAccessibleAbstractSpinBox is built on more than one class. The
  #  part of a C++ QAccessibleAbstractSpinBox that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleValueInterface':
          'ritual_cast_QAccessibleAbstractSpinBox_QAccessibleValueInterface',
      'QAccessibleTextInterface':
          'ritual_cast_QAccessibleAbstractSpinBox_QAccessibleTextInterface',
      'QAccessibleEditableTextInterface':
          'ritual_cast_QAccessibleAbstractSpinBox_QAccessibleEditableTextInterface',
  }

  #  A C++ QAccessibleAbstractSpinBox Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleAbstractSpinBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleAbstractSpinBox::state()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleAbstractSpinBox::state() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleAbstractSpinBox::text(QAccessible::Text t)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleAbstractSpinBox::text(QAccessible::Text t) const
    ritual = (
        'ritual_ZNK26QAccessibleAbstractSpinBox4textEN11QAccessible4TextE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleAbstractSpinBox4textEN11QAccessible4T'
          'extE')
    return self.uglySide.call(ritual, t.value)

  @overload(int, int)
  def text(self, startOffset: int, endOffset: int) -> str:
    """
    Calls Qt's 'QString QAccessibleAbstractSpinBox::text(int startOffset, int
    endOffset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#text

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
    #  QString QAccessibleAbstractSpinBox::text(int startOffset, int
    #      endOffset) const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox4textEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox4textEii'
    return self.uglySide.call(ritual, startOffset, endOffset)

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSpinBox::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSpinBox::currentValue() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox12currentValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox12currentValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maximumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSpinBox::maximumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#maximumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSpinBox::maximumValue() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox12maximumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox12maximumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSpinBox::minimumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#minimumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSpinBox::minimumValue() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox12minimumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox12minimumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumStepSize(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSpinBox::minimumStepSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#minimumStepSize

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSpinBox::minimumStepSize() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox15minimumStepSizeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleAbstractSpinBox15minimumStepSizeEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleAbstractSpinBox::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#cursorPosition
    """
    #  int QAccessibleAbstractSpinBox::cursorPosition() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox14cursorPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox14cursorPositionEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def characterRect(self, offset: int) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleAbstractSpinBox::characterRect(int offset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#characterRect

    Parameters
    ----------

    offset : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleAbstractSpinBox::characterRect(int offset) const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox13characterRectEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox13characterRectEi'
    address = self.uglySide.call(ritual, offset)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def selectionCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleAbstractSpinBox::selectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#selectionCount
    """
    #  int QAccessibleAbstractSpinBox::selectionCount() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox14selectionCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox14selectionCountEv'
    return self.uglySide.call(ritual)

  @overload(QPoint)
  def offsetAtPoint(self, point: QPoint) -> int:
    """
    Calls Qt's 'int QAccessibleAbstractSpinBox::offsetAtPoint(const QPoint
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#offsetAtPoint

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QAccessibleAbstractSpinBox::offsetAtPoint(const QPoint &point)
    #      const
    ritual = (
        'ritual_ZNK26QAccessibleAbstractSpinBox13offsetAtPointERK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleAbstractSpinBox13offsetAtPointERK6QPo'
          'int')
    return self.uglySide.call(ritual, self._valueOf(point))

  def characterCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleAbstractSpinBox::characterCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#characterCount
    """
    #  int QAccessibleAbstractSpinBox::characterCount() const
    ritual = 'ritual_ZNK26QAccessibleAbstractSpinBox14characterCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleAbstractSpinBox14characterCountEv'
    return self.uglySide.call(ritual)

  def abstractSpinBox(self) -> Optional[QAbstractSpinBox]:
    """
    Calls Qt's 'QAbstractSpinBox
    *QAccessibleAbstractSpinBox::abstractSpinBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#abstractSpinBox

    Returns
    -------

    Optional[QAbstractSpinBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSpinBox *QAccessibleAbstractSpinBox::abstractSpinBox() const
    address = self.uglySide.call(
        'ritual_ZNK26QAccessibleAbstractSpinBox15abstractSpinBoxEv',
    )
    from . import QAbstractSpinBox
    return QAbstractSpinBox._cuteAt(address)

  def lineEditIface(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QAccessibleAbstractSpinBox::lineEditIface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#lineEditIface

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleAbstractSpinBox::lineEditIface()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QAccessibleAbstractSpinBox13lineEditIfaceEv',
    )
    return QAccessibleInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::setCurrentValue(const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#setCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAccessibleAbstractSpinBox::setCurrentValue(const QVariant
    #      &value)
    ritual = (
        'ritual_ZN26QAccessibleAbstractSpinBox15setCurrentValueERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAccessibleAbstractSpinBox15setCurrentValueERK8QV'
          'ariant')
    self.uglySide.call(ritual, self._valueOf(value))

  @overload(int)
  def setCursorPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::setCursorPosition(int
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#setCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAccessibleAbstractSpinBox::setCursorPosition(int position)
    ritual = 'ritual_ZN26QAccessibleAbstractSpinBox17setCursorPositionEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAccessibleAbstractSpinBox17setCursorPositionEi')
    self.uglySide.call(ritual, position)

  @overload(int, int, int)
  def setSelection(
      self,
      selectionIndex: int,
      startOffset: int,
      endOffset: int,
  ) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::setSelection(int
    selectionIndex, int startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#setSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleAbstractSpinBox::setSelection(int selectionIndex, int
    #      startOffset, int endOffset)
    ritual = 'ritual_ZN26QAccessibleAbstractSpinBox12setSelectionEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QAccessibleAbstractSpinBox12setSelectionEiii'
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
    Qt's 'QAccessibleAbstractSpinBox::QAccessibleAbstractSpinBox(QWidget
    *w)': leans on 'non-virtual thunk to
    QAccessibleAbstractSpinBox::attributes(int, int*, int*) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleAbstractSpinBox.__init__' has no cute function yet. "
        "Qt's "
        "'QAccessibleAbstractSpinBox::QAccessibleAbstractSpinBox(QWidget "
        "*w)': leans on 'non-virtual thunk to "
        "QAccessibleAbstractSpinBox::attributes(int, int*, int*) const', "
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

  @overload(int, int)
  def addSelection(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::addSelection(int
    startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#addSelection

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleAbstractSpinBox::addSelection(int startOffset, int
    #      endOffset)
    ritual = 'ritual_ZN26QAccessibleAbstractSpinBox12addSelectionEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QAccessibleAbstractSpinBox12addSelectionEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int)
  def removeSelection(self, selectionIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::removeSelection(int
    selectionIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#removeSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.
    """
    #  void QAccessibleAbstractSpinBox::removeSelection(int selectionIndex)
    ritual = 'ritual_ZN26QAccessibleAbstractSpinBox15removeSelectionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QAccessibleAbstractSpinBox15removeSelectionEi'
    self.uglySide.call(ritual, selectionIndex)

  @overload(int, int)
  def scrollToSubstring(self, startIndex: int, endIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::scrollToSubstring(int
    startIndex, int endIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#scrollToSubstring

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  void QAccessibleAbstractSpinBox::scrollToSubstring(int startIndex, int
    #      endIndex)
    ritual = 'ritual_ZN26QAccessibleAbstractSpinBox17scrollToSubstringEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAccessibleAbstractSpinBox17scrollToSubstringEii')
    self.uglySide.call(ritual, startIndex, endIndex)

  @overload(int, int)
  def deleteText(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::deleteText(int startOffset,
    int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#deleteText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleAbstractSpinBox::deleteText(int startOffset, int
    #      endOffset)
    ritual = 'ritual_ZN26QAccessibleAbstractSpinBox10deleteTextEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QAccessibleAbstractSpinBox10deleteTextEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int, str)
  def insertText(self, offset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::insertText(int offset, const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#insertText

    Parameters
    ----------

    offset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleAbstractSpinBox::insertText(int offset, const QString
    #      &text)
    ritual = 'ritual_ZN26QAccessibleAbstractSpinBox10insertTextEiRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAccessibleAbstractSpinBox10insertTextEiRK7QStrin'
          'g')
    self.uglySide.call(ritual, offset, text)

  @overload(int, int, str)
  def replaceText(self, startOffset: int, endOffset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSpinBox::replaceText(int startOffset,
    int endOffset, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractspinbox.html#replaceText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleAbstractSpinBox::replaceText(int startOffset, int
    #      endOffset, const QString &text)
    ritual = (
        'ritual_ZN26QAccessibleAbstractSpinBox11replaceTextEiiRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAccessibleAbstractSpinBox11replaceTextEiiRK7QStr'
          'ing')
    self.uglySide.call(ritual, startOffset, endOffset, text)
