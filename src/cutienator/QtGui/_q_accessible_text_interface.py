"""
QAccessibleTextInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QAccessible

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPoint, QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QAccessibleTextInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleTextInterface: a plain Python object
  standing in front of one C++ QAccessibleTextInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleTextInterface that has a ritual and that
  Python can call so far, 11 names in all: 'selectionCount', 'addSelection',
  'removeSelection', 'setSelection', 'cursorPosition', 'setCursorPosition',
  'text', 'characterCount', 'characterRect', 'offsetAtPoint',
  'scrollToSubstring'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTextInterface::~QAccessibleTextInterface()': the
    destructor: Python never removes a C++ QAccessibleTextInterface.
  - Qt's 'void QAccessibleTextInterface::selection(int selectionIndex, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
  - Qt's 'QString QAccessibleTextInterface::textBeforeOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleTextInterface::textAfterOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleTextInterface::textAtOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleTextInterface::attributes(int offset, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.

  What has no ritual
  ------------------

  5 of the 22 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QAccessibleTextInterface is created at the first use, not by
    'QAccessibleTextInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTextInterface.
  - Each name of Qt's QAccessibleTextInterface that has no cute function yet,
    '__init__', 'attributes', 'selection', 'textAfterOffset', 'textAtOffset',
    'textBeforeOffset', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTextInterface'

  #  A C++ QAccessibleTextInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTextInterface'

  #  The functions Qt calls itself that QAccessibleTextInterface is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'selection': (
          'void QAccessibleTextInterface::selection(int, int *, int *) '
          'const',
      ),
      'textBeforeOffset': (
          'QString QAccessibleTextInterface::textBeforeOffset(int, '
          'QAccessible::TextBoundaryType, int *, int *) const',
      ),
      'textAfterOffset': (
          'QString QAccessibleTextInterface::textAfterOffset(int, '
          'QAccessible::TextBoundaryType, int *, int *) const',
      ),
      'textAtOffset': (
          'QString QAccessibleTextInterface::textAtOffset(int, '
          'QAccessible::TextBoundaryType, int *, int *) const',
      ),
      'attributes': (
          'QString QAccessibleTextInterface::attributes(int, int *, int *) '
          'const',
      ),
  }

  #  The functions Qt calls itself that QAccessibleTextInterface is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'selectionCount': (
          ('_ZNK24QAccessibleTextInterface14selectionCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'addSelection': (
          ('_ZN24QAccessibleTextInterface12addSelectionEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'removeSelection': (
          ('_ZN24QAccessibleTextInterface15removeSelectionEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setSelection': (
          ('_ZN24QAccessibleTextInterface12setSelectionEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'cursorPosition': (
          ('_ZNK24QAccessibleTextInterface14cursorPositionEv',
           ('int', 'number', ''),
           ()),
      ),
      'setCursorPosition': (
          ('_ZN24QAccessibleTextInterface17setCursorPositionEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'text': (
          ('_ZNK24QAccessibleTextInterface4textEii',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'characterCount': (
          ('_ZNK24QAccessibleTextInterface14characterCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'characterRect': (
          ('_ZNK24QAccessibleTextInterface13characterRectEi',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'number', ''),
           )),
      ),
      'offsetAtPoint': (
          ('_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'scrollToSubstring': (
          ('_ZN24QAccessibleTextInterface17scrollToSubstringEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def selectionCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextInterface::selectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#selectionCount
    """
    #  int QAccessibleTextInterface::selectionCount() const
    return self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZNK24QAccessibleTextInterface14selectionCountEv',
    )

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextInterface::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#cursorPosition
    """
    #  int QAccessibleTextInterface::cursorPosition() const
    return self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZNK24QAccessibleTextInterface14cursorPositionEv',
    )

  @overload(int, int)
  def text(self, startOffset: int, endOffset: int) -> str:
    """
    Calls Qt's 'QString QAccessibleTextInterface::text(int startOffset, int
    endOffset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletextinterface.html#text

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
    #  QString QAccessibleTextInterface::text(int startOffset, int endOffset)
    #      const
    return self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZNK24QAccessibleTextInterface4textEii',
        startOffset, endOffset,
    )

  def characterCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextInterface::characterCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#characterCount
    """
    #  int QAccessibleTextInterface::characterCount() const
    return self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZNK24QAccessibleTextInterface14characterCountEv',
    )

  @overload(int)
  def characterRect(self, offset: int) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleTextInterface::characterRect(int offset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#characterRect

    Parameters
    ----------

    offset : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleTextInterface::characterRect(int offset) const
    address = self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZNK24QAccessibleTextInterface13characterRectEi',
        offset,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def offsetAtPoint(self, point: QPoint) -> int:
    """
    Calls Qt's 'int QAccessibleTextInterface::offsetAtPoint(const QPoint
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#offsetAtPoint

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QAccessibleTextInterface::offsetAtPoint(const QPoint &point) const
    return self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint',
        self._valueOf(point),
    )

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
    Calls Qt's 'void QAccessibleTextInterface::setSelection(int
    selectionIndex, int startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#setSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleTextInterface::setSelection(int selectionIndex, int
    #      startOffset, int endOffset)
    self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZN24QAccessibleTextInterface12setSelectionEiii',
        selectionIndex, startOffset, endOffset,
    )

  @overload(int)
  def setCursorPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextInterface::setCursorPosition(int
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#setCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAccessibleTextInterface::setCursorPosition(int position)
    self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZN24QAccessibleTextInterface17setCursorPositionEi',
        position,
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
    Qt's 'QAccessibleTextInterface::QAccessibleTextInterface()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAccessibleTextInterface.__init__' has no cute function yet. Qt's "
        "'QAccessibleTextInterface::QAccessibleTextInterface()': the class "
        "is abstract, so C++ cannot make one, and the C++ class of ours "
        "does not fill in every function it leaves open.")

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
    Calls Qt's 'void QAccessibleTextInterface::addSelection(int startOffset,
    int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#addSelection

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleTextInterface::addSelection(int startOffset, int
    #      endOffset)
    self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZN24QAccessibleTextInterface12addSelectionEii',
        startOffset, endOffset,
    )

  @overload(int)
  def removeSelection(self, selectionIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextInterface::removeSelection(int
    selectionIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#removeSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.
    """
    #  void QAccessibleTextInterface::removeSelection(int selectionIndex)
    self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZN24QAccessibleTextInterface15removeSelectionEi',
        selectionIndex,
    )

  @overload(int, int)
  def scrollToSubstring(self, startIndex: int, endIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextInterface::scrollToSubstring(int
    startIndex, int endIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinterface.html#scrollToSubstring

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  void QAccessibleTextInterface::scrollToSubstring(int startIndex, int
    #      endIndex)
    self._callAs(
        'QAccessibleTextInterface',
        'ritual_ZN24QAccessibleTextInterface17scrollToSubstringEii',
        startIndex, endIndex,
    )

  @staticmethod
  def attributes(*__, **_) -> Never:
    """
    Qt's 'QString QAccessibleTextInterface::attributes(int offset, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QAccessibleTextInterface.attributes' has no cute function yet. "
        "Qt's 'QString QAccessibleTextInterface::attributes(int offset, int "
        "*startOffset, int *endOffset) const': takes a number to change "
        "where it is.")

  @staticmethod
  def selection(*__, **_) -> Never:
    """
    Qt's 'void QAccessibleTextInterface::selection(int selectionIndex, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QAccessibleTextInterface.selection' has no cute function yet. "
        "Qt's 'void QAccessibleTextInterface::selection(int selectionIndex, "
        "int *startOffset, int *endOffset) const': takes a number to change "
        "where it is.")

  @staticmethod
  def textAfterOffset(*__, **_) -> Never:
    """
    Qt's 'QString QAccessibleTextInterface::textAfterOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAccessibleTextInterface.textAfterOffset' has no cute function "
        "yet. Qt's 'QString QAccessibleTextInterface::textAfterOffset(int "
        "offset, QAccessible::TextBoundaryType boundaryType, int "
        "*startOffset, int *endOffset) const': takes a number to change "
        "where it is.")

  @staticmethod
  def textAtOffset(*__, **_) -> Never:
    """
    Qt's 'QString QAccessibleTextInterface::textAtOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAccessibleTextInterface.textAtOffset' has no cute function yet. "
        "Qt's 'QString QAccessibleTextInterface::textAtOffset(int offset, "
        "QAccessible::TextBoundaryType boundaryType, int *startOffset, int "
        "*endOffset) const': takes a number to change where it is.")

  @staticmethod
  def textBeforeOffset(*__, **_) -> Never:
    """
    Qt's 'QString QAccessibleTextInterface::textBeforeOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAccessibleTextInterface.textBeforeOffset' has no cute function "
        "yet. Qt's 'QString QAccessibleTextInterface::textBeforeOffset(int "
        "offset, QAccessible::TextBoundaryType boundaryType, int "
        "*startOffset, int *endOffset) const': takes a number to change "
        "where it is.")
