"""
QAccessibleTableInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAccessibleInterface, QAccessibleTableModelChangeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleTableModelChangeEvent = WAIT['QAccessibleTableModelChangeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTableInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleTableInterface: a plain Python object
  standing in front of one C++ QAccessibleTableInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleTableInterface that has a ritual and that
  Python can call so far, 17 names in all: 'caption', 'summary', 'cellAt',
  'selectedCellCount', 'columnDescription', 'rowDescription',
  'selectedColumnCount', 'selectedRowCount', 'columnCount', 'rowCount',
  'isColumnSelected', 'isRowSelected', 'selectRow', 'selectColumn',
  'unselectRow', 'unselectColumn', 'modelChange'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTableInterface::~QAccessibleTableInterface()': the
    destructor: Python never removes a C++ QAccessibleTableInterface.

  What has no ritual
  ------------------

  8 of the 26 functions Qt declares: 4 forbidden; 3 takes or gives a type
  that cannot be passed yet; 1 the class is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QAccessibleTableInterface is created at the first use, not by
    'QAccessibleTableInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTableInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTableInterface'

  #  A C++ QAccessibleTableInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTableInterface'

  #  The functions Qt calls itself that QAccessibleTableInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'selectedCells': (
          'QList<QAccessibleInterface *> '
          'QAccessibleTableInterface::selectedCells() const',
      ),
      'columnDescription': (
          'QString QAccessibleTableInterface::columnDescription(int) const',
      ),
      'rowDescription': (
          'QString QAccessibleTableInterface::rowDescription(int) const',
      ),
      'selectedColumns': (
          'QList<int> QAccessibleTableInterface::selectedColumns() const',
      ),
      'selectedRows': (
          'QList<int> QAccessibleTableInterface::selectedRows() const',
      ),
  }

  #  The functions Qt calls itself that QAccessibleTableInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'caption': (
          ('_ZNK25QAccessibleTableInterface7captionEv',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           ()),
      ),
      'summary': (
          ('_ZNK25QAccessibleTableInterface7summaryEv',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           ()),
      ),
      'cellAt': (
          ('_ZNK25QAccessibleTableInterface6cellAtEii',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'selectedCellCount': (
          ('_ZNK25QAccessibleTableInterface17selectedCellCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'selectedColumnCount': (
          ('_ZNK25QAccessibleTableInterface19selectedColumnCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'selectedRowCount': (
          ('_ZNK25QAccessibleTableInterface16selectedRowCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'columnCount': (
          ('_ZNK25QAccessibleTableInterface11columnCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'rowCount': (
          ('_ZNK25QAccessibleTableInterface8rowCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'isColumnSelected': (
          ('_ZNK25QAccessibleTableInterface16isColumnSelectedEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isRowSelected': (
          ('_ZNK25QAccessibleTableInterface13isRowSelectedEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'selectRow': (
          ('_ZN25QAccessibleTableInterface9selectRowEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'selectColumn': (
          ('_ZN25QAccessibleTableInterface12selectColumnEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'unselectRow': (
          ('_ZN25QAccessibleTableInterface11unselectRowEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'unselectColumn': (
          ('_ZN25QAccessibleTableInterface14unselectColumnEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'modelChange': (
          ('_ZN25QAccessibleTableInterface11modelChangeEP32QAccessibleTable'
           'ModelChangeEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtGui:QAccessibleTableModelChangeEvent'),
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

  def caption(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableInterface::caption()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#caption

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableInterface::caption() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface7captionEv',
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  def summary(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableInterface::summary()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#summary

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableInterface::summary() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface7summaryEv',
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  @overload(int, int)
  def cellAt(self, row: int, column: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableInterface::cellAt(int
    row, int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#cellAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableInterface::cellAt(int row, int
    #      column) const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface6cellAtEii', row, column,
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  def selectedCellCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableInterface::selectedCellCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#selectedCellCount
    """
    #  int QAccessibleTableInterface::selectedCellCount() const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface17selectedCellCountEv',
    )

  @overload(int)
  def columnDescription(self, column: int) -> str:
    """
    Calls Qt's 'QString QAccessibleTableInterface::columnDescription(int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#columnDescription

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTableInterface::columnDescription(int column) const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface17columnDescriptionEi', column,
    )

  @overload(int)
  def rowDescription(self, row: int) -> str:
    """
    Calls Qt's 'QString QAccessibleTableInterface::rowDescription(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#rowDescription

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTableInterface::rowDescription(int row) const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface14rowDescriptionEi', row,
    )

  def selectedColumnCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableInterface::selectedColumnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#selectedColumnCount
    """
    #  int QAccessibleTableInterface::selectedColumnCount() const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface19selectedColumnCountEv',
    )

  def selectedRowCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableInterface::selectedRowCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#selectedRowCount
    """
    #  int QAccessibleTableInterface::selectedRowCount() const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface16selectedRowCountEv',
    )

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableInterface::columnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#columnCount
    """
    #  int QAccessibleTableInterface::columnCount() const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface11columnCountEv',
    )

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableInterface::rowCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#rowCount
    """
    #  int QAccessibleTableInterface::rowCount() const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface8rowCountEv',
    )

  @overload(int)
  def isColumnSelected(self, column: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableInterface::isColumnSelected(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#isColumnSelected

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QAccessibleTableInterface::isColumnSelected(int column) const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface16isColumnSelectedEi', column,
    )

  @overload(int)
  def isRowSelected(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableInterface::isRowSelected(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#isRowSelected

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTableInterface::isRowSelected(int row) const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleTableInterface13isRowSelectedEi', row,
    )

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
  def selectRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableInterface::selectRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#selectRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTableInterface::selectRow(int row)
    return self.uglySide.call(
        'ritual_ZN25QAccessibleTableInterface9selectRowEi', row,
    )

  @overload(int)
  def selectColumn(self, column: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableInterface::selectColumn(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#selectColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QAccessibleTableInterface::selectColumn(int column)
    return self.uglySide.call(
        'ritual_ZN25QAccessibleTableInterface12selectColumnEi', column,
    )

  @overload(int)
  def unselectRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableInterface::unselectRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#unselectRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTableInterface::unselectRow(int row)
    return self.uglySide.call(
        'ritual_ZN25QAccessibleTableInterface11unselectRowEi', row,
    )

  @overload(int)
  def unselectColumn(self, column: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableInterface::unselectColumn(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#unselectColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QAccessibleTableInterface::unselectColumn(int column)
    return self.uglySide.call(
        'ritual_ZN25QAccessibleTableInterface14unselectColumnEi', column,
    )

  @overload(QAccessibleTableModelChangeEvent)
  @overload(NoneType)
  def modelChange(
      self,
      event: Optional[QAccessibleTableModelChangeEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibleTableInterface::modelChange(QAccessibleTableModelChangeEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableinterface.html#modelChange

    Parameters
    ----------

    event : Optional[QAccessibleTableModelChangeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessibleTableInterface::modelChange(
    #      QAccessibleTableModelChangeEvent *event)
    self.uglySide.call(
        'ritual_ZN25QAccessibleTableInterface11modelChangeEP32QAccessibleTa'
        'bleModelChangeEvent',
        self._addressOf(event),
    )
