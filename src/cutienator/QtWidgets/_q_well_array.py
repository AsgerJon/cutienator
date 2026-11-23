"""
QWellArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QWellArray to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from ..QtGui import QFocusEvent, QKeyEvent, QMouseEvent, QPaintEvent
  from ..QtGui import QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFocusEvent = WAIT['QFocusEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWellArray(QWidget):
  """
  The cute side of Qt's QWellArray: a plain Python object standing in front
  of one C++ QWellArray.

  It is built on the cute 'QWidget', as Qt's QWellArray is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWellArray that has a ritual and that Python can
  call so far, 30 names in all: 'metaObject', 'currentColumn', 'currentRow',
  'selectedColumn', 'selectedRow', 'setCurrent', 'setSelected', 'sizeHint',
  'cellWidth', 'cellHeight', 'rowAt', 'columnAt', 'rowY', 'columnX',
  'numRows', 'numCols', 'index', 'cellRect', 'gridSize', 'cellGeometry',
  'updateCell', 'paintCell', 'paintCellContents', 'mousePressEvent',
  'mouseReleaseEvent', 'keyPressEvent', 'focusInEvent', 'focusOutEvent',
  'paintEvent', 'sendAccessibleChildFocusEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWellArray::~QWellArray()': the destructor: Python never removes a
    C++ QWellArray.

  What has no ritual
  ------------------

  14 of the 45 functions Qt declares: 5 leans on 'QWellArray; 3 a signal; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template;
  1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QWellArray is created at the first use, not by 'QWellArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWellArray.
  - Qt tells when it has removed the C++ QWellArray. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWellArray'

  #  A C++ QWellArray Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWellArray'

  #  The functions Qt calls itself that QWellArray is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setCurrent': (
          ('_ZN10QWellArray10setCurrentEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'setSelected': (
          ('_ZN10QWellArray11setSelectedEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'paintCell': (
          ('_ZN10QWellArray9paintCellEP8QPainteriiRK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'paintCellContents': (
          ('_ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QRect'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWellArray::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWellArray::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QWellArray10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentColumn(self) -> int:
    """
    Calls Qt's 'int QWellArray::currentColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#currentColumn
    """
    #  int QWellArray::currentColumn() const
    return self.uglySide.call('ritual_ZNK10QWellArray13currentColumnEv')

  def currentRow(self) -> int:
    """
    Calls Qt's 'int QWellArray::currentRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#currentRow
    """
    #  int QWellArray::currentRow() const
    return self.uglySide.call('ritual_ZNK10QWellArray10currentRowEv')

  def selectedColumn(self) -> int:
    """
    Calls Qt's 'int QWellArray::selectedColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#selectedColumn
    """
    #  int QWellArray::selectedColumn() const
    return self.uglySide.call('ritual_ZNK10QWellArray14selectedColumnEv')

  def selectedRow(self) -> int:
    """
    Calls Qt's 'int QWellArray::selectedRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#selectedRow
    """
    #  int QWellArray::selectedRow() const
    return self.uglySide.call('ritual_ZNK10QWellArray11selectedRowEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWellArray::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWellArray::sizeHint() const
    ritual = 'ritual_ZNK10QWellArray8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QWellArray8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def cellWidth(self) -> int:
    """
    Calls Qt's 'int QWellArray::cellWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#cellWidth
    """
    #  int QWellArray::cellWidth() const
    return self.uglySide.call('ritual_ZNK10QWellArray9cellWidthEv')

  def cellHeight(self) -> int:
    """
    Calls Qt's 'int QWellArray::cellHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#cellHeight
    """
    #  int QWellArray::cellHeight() const
    return self.uglySide.call('ritual_ZNK10QWellArray10cellHeightEv')

  @overload(int)
  def rowAt(self, y: int) -> int:
    """
    Calls Qt's 'int QWellArray::rowAt(int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#rowAt

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  int QWellArray::rowAt(int y) const
    return self.uglySide.call('ritual_ZNK10QWellArray5rowAtEi', y)

  @overload(int)
  def columnAt(self, x: int) -> int:
    """
    Calls Qt's 'int QWellArray::columnAt(int x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#columnAt

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  int QWellArray::columnAt(int x) const
    return self.uglySide.call('ritual_ZNK10QWellArray8columnAtEi', x)

  @overload(int)
  def rowY(self, row: int) -> int:
    """
    Calls Qt's 'int QWellArray::rowY(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#rowY

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QWellArray::rowY(int row) const
    return self.uglySide.call('ritual_ZNK10QWellArray4rowYEi', row)

  @overload(int)
  def columnX(self, column: int) -> int:
    """
    Calls Qt's 'int QWellArray::columnX(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#columnX

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QWellArray::columnX(int column) const
    return self.uglySide.call('ritual_ZNK10QWellArray7columnXEi', column)

  def numRows(self) -> int:
    """
    Calls Qt's 'int QWellArray::numRows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#numRows
    """
    #  int QWellArray::numRows() const
    return self.uglySide.call('ritual_ZNK10QWellArray7numRowsEv')

  def numCols(self) -> int:
    """
    Calls Qt's 'int QWellArray::numCols() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#numCols
    """
    #  int QWellArray::numCols() const
    return self.uglySide.call('ritual_ZNK10QWellArray7numColsEv')

  def cellRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWellArray::cellRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#cellRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWellArray::cellRect() const
    address = self.uglySide.call('ritual_ZNK10QWellArray8cellRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def gridSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWellArray::gridSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#gridSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWellArray::gridSize() const
    address = self.uglySide.call('ritual_ZNK10QWellArray8gridSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setCurrent(self, row: int, col: int) -> None:
    """
    Calls Qt's 'void QWellArray::setCurrent(int row, int col)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#setCurrent

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.
    """
    #  void QWellArray::setCurrent(int row, int col)
    self.uglySide.call('ritual_ZN10QWellArray10setCurrentEii', row, col)

  @overload(int, int)
  def setSelected(self, row: int, col: int) -> None:
    """
    Calls Qt's 'void QWellArray::setSelected(int row, int col)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#setSelected

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.
    """
    #  void QWellArray::setSelected(int row, int col)
    self.uglySide.call('ritual_ZN10QWellArray11setSelectedEii', row, col)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def index(self, row: int, col: int) -> int:
    """
    Calls Qt's 'int QWellArray::index(int row, int col)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.
    """
    #  int QWellArray::index(int row, int col)
    return self.uglySide.call('ritual_ZN10QWellArray5indexEii', row, col)

  @overload(int, int)
  def cellGeometry(self, row: int, column: int) -> QRect:
    """
    Calls Qt's 'QRect QWellArray::cellGeometry(int row, int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#cellGeometry

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWellArray::cellGeometry(int row, int column)
    address = self.uglySide.call(
        'ritual_ZN10QWellArray12cellGeometryEii', row, column,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int, int)
  def updateCell(self, row: int, column: int) -> None:
    """
    Calls Qt's 'void QWellArray::updateCell(int row, int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#updateCell

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QWellArray::updateCell(int row, int column)
    self.uglySide.call('ritual_ZN10QWellArray10updateCellEii', row, column)

  @overload(QPainter, int, int, QRect)
  @overload(NoneType, int, int, QRect)
  def paintCell(
      self,
      a0: Optional[QPainter],
      row: int,
      col: int,
      a3: QRect,
  ) -> None:
    """
    Calls Qt's 'void QWellArray::paintCell(QPainter *a0, int row, int col,
    const QRect &a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#paintCell

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.

    a3 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWellArray::paintCell(QPainter *a0, int row, int col, const QRect
    #      &a3)
    ritual = 'ritual_ZN10QWellArray9paintCellEP8QPainteriiRK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QWellArray9paintCellEP8QPainteriiRK5QRect'
    self.uglySide.call(
        ritual, self._addressOf(a0), row, col, self._valueOf(a3),
    )

  @overload(QPainter, int, int, QRect)
  @overload(NoneType, int, int, QRect)
  def paintCellContents(
      self,
      a0: Optional[QPainter],
      row: int,
      col: int,
      a3: QRect,
  ) -> None:
    """
    Calls Qt's 'void QWellArray::paintCellContents(QPainter *a0, int row, int
    col, const QRect &a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#paintCellContents

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.

    a3 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWellArray::paintCellContents(QPainter *a0, int row, int col,
    #      const QRect &a3)
    ritual = 'ritual_ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRect'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QWellArray17paintCellContentsEP8QPainteriiRK5QRec'
          't')
    self.uglySide.call(
        ritual, self._addressOf(a0), row, col, self._valueOf(a3),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWellArray::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWellArray::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QWellArray15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QWellArray15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWellArray::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWellArray::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QWellArray17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QWellArray17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWellArray::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWellArray::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN10QWellArray13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QWellArray13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QWellArray::focusInEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#focusInEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWellArray::focusInEvent(QFocusEvent *a0)
    self.uglySide.call(
        'ritual_ZN10QWellArray12focusInEventEP11QFocusEvent',
        self._addressOf(a0),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QWellArray::focusOutEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#focusOutEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWellArray::focusOutEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN10QWellArray13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QWellArray13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QWellArray::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwellarray.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWellArray::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN10QWellArray10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QWellArray10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  def sendAccessibleChildFocusEvent(self) -> None:
    """
    Calls Qt's 'void QWellArray::sendAccessibleChildFocusEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwellarray.html#sendAccessibleChildFocusEvent
    """
    #  void QWellArray::sendAccessibleChildFocusEvent()
    self.uglySide.call(
        'ritual_ZN10QWellArray29sendAccessibleChildFocusEventEv',
    )
