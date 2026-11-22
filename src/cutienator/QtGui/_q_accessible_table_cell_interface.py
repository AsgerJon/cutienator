"""
QAccessibleTableCellInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAccessibleInterface


class QAccessibleTableCellInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleTableCellInterface: a plain Python object
  standing in front of one C++ QAccessibleTableCellInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleTableCellInterface that has a ritual and
  that Python can call so far, 8 names in all: 'isSelected',
  'columnHeaderCells', 'rowHeaderCells', 'columnIndex', 'rowIndex',
  'columnExtent', 'rowExtent', 'table'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTableCellInterface::~QAccessibleTableCellInterface()':
    the destructor: Python never removes a C++ QAccessibleTableCellInterface.

  What has no ritual
  ------------------

  5 of the 14 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one.

  What to expect
  --------------

  - The C++ QAccessibleTableCellInterface is created at the first use, not by
    'QAccessibleTableCellInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTableCellInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTableCellInterface'

  #  A C++ QAccessibleTableCellInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTableCellInterface'

  #  The functions Qt calls itself that QAccessibleTableCellInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'columnHeaderCells': (
          'QList<QAccessibleInterface *> '
          'QAccessibleTableCellInterface::columnHeaderCells() const',
      ),
      'rowHeaderCells': (
          'QList<QAccessibleInterface *> '
          'QAccessibleTableCellInterface::rowHeaderCells() const',
      ),
  }

  #  The functions Qt calls itself that QAccessibleTableCellInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isSelected': (
          ('_ZNK29QAccessibleTableCellInterface10isSelectedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'columnIndex': (
          ('_ZNK29QAccessibleTableCellInterface11columnIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'rowIndex': (
          ('_ZNK29QAccessibleTableCellInterface8rowIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'columnExtent': (
          ('_ZNK29QAccessibleTableCellInterface12columnExtentEv',
           ('int', 'number', ''),
           ()),
      ),
      'rowExtent': (
          ('_ZNK29QAccessibleTableCellInterface9rowExtentEv',
           ('int', 'number', ''),
           ()),
      ),
      'table': (
          ('_ZNK29QAccessibleTableCellInterface5tableEv',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
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

  def isSelected(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableCellInterface::isSelected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html#isSelected
    """
    #  bool QAccessibleTableCellInterface::isSelected() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface10isSelectedEv',
    )

  def columnHeaderCells(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleTableCellInterface::columnHeaderCells() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *>
    #      QAccessibleTableCellInterface::columnHeaderCells() const
    address = self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface17columnHeaderCellsEv',
    )
    from . import QAccessibleInterface
    return QList[QAccessibleInterface]._cuteOwning(address)

  def rowHeaderCells(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleTableCellInterface::rowHeaderCells() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html#rowHeaderCells

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *>
    #      QAccessibleTableCellInterface::rowHeaderCells() const
    address = self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface14rowHeaderCellsEv',
    )
    from . import QAccessibleInterface
    return QList[QAccessibleInterface]._cuteOwning(address)

  def columnIndex(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCellInterface::columnIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html#columnIndex
    """
    #  int QAccessibleTableCellInterface::columnIndex() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface11columnIndexEv',
    )

  def rowIndex(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCellInterface::rowIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html#rowIndex
    """
    #  int QAccessibleTableCellInterface::rowIndex() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface8rowIndexEv',
    )

  def columnExtent(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCellInterface::columnExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html#columnExtent
    """
    #  int QAccessibleTableCellInterface::columnExtent() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface12columnExtentEv',
    )

  def rowExtent(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCellInterface::rowExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html#rowExtent
    """
    #  int QAccessibleTableCellInterface::rowExtent() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface9rowExtentEv',
    )

  def table(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableCellInterface::table()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecellinterface.html#table

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCellInterface::table() const
    address = self.uglySide.call(
        'ritual_ZNK29QAccessibleTableCellInterface5tableEv',
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

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
