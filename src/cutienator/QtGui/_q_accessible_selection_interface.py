"""
QAccessibleSelectionInterface binding of the Qt C++
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

  from . import QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleInterface = WAIT['QAccessibleInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleSelectionInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleSelectionInterface: a plain Python object
  standing in front of one C++ QAccessibleSelectionInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleSelectionInterface that has a ritual and
  that Python can call so far, 7 names in all: 'selectedItemCount',
  'selectedItem', 'isSelected', 'select', 'unselect', 'selectAll', 'clear'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleSelectionInterface::~QAccessibleSelectionInterface()':
    the destructor: Python never removes a C++ QAccessibleSelectionInterface.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one; 1 takes or gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QAccessibleSelectionInterface is created at the first use, not by
    'QAccessibleSelectionInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleSelectionInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleSelectionInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def selectedItemCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleSelectionInterface::selectedItemCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleselectioninterface.html
    """
    #  int QAccessibleSelectionInterface::selectedItemCount() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleSelectionInterface17selectedItemCountEv',
    )

  @overload(int)
  def selectedItem(
      self,
      selectionIndex: int,
  ) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QAccessibleSelectionInterface::selectedItem(int selectionIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleselectioninterface.html#selectedItem

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleSelectionInterface::selectedItem(int
    #      selectionIndex) const
    address = self.uglySide.call(
        'ritual_ZNK29QAccessibleSelectionInterface12selectedItemEi',
        selectionIndex,
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def isSelected(self, childItem: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool
    QAccessibleSelectionInterface::isSelected(QAccessibleInterface
    *childItem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleselectioninterface.html#isSelected

    Parameters
    ----------

    childItem : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleSelectionInterface::isSelected(QAccessibleInterface
    #      *childItem) const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessib'
        'leInterface',
        self._addressOf(childItem),
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

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def select(self, childItem: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool
    QAccessibleSelectionInterface::select(QAccessibleInterface *childItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleselectioninterface.html#select

    Parameters
    ----------

    childItem : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleSelectionInterface::select(QAccessibleInterface
    #      *childItem)
    return self.uglySide.call(
        'ritual_ZN29QAccessibleSelectionInterface6selectEP20QAccessibleInte'
        'rface',
        self._addressOf(childItem),
    )

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def unselect(self, childItem: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool
    QAccessibleSelectionInterface::unselect(QAccessibleInterface
    *childItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleselectioninterface.html#unselect

    Parameters
    ----------

    childItem : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleSelectionInterface::unselect(QAccessibleInterface
    #      *childItem)
    return self.uglySide.call(
        'ritual_ZN29QAccessibleSelectionInterface8unselectEP20QAccessibleIn'
        'terface',
        self._addressOf(childItem),
    )

  def selectAll(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleSelectionInterface::selectAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleselectioninterface.html#selectAll
    """
    #  bool QAccessibleSelectionInterface::selectAll()
    return self.uglySide.call(
        'ritual_ZN29QAccessibleSelectionInterface9selectAllEv',
    )

  def clear(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleSelectionInterface::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleselectioninterface.html#clear
    """
    #  bool QAccessibleSelectionInterface::clear()
    return self.uglySide.call(
        'ritual_ZN29QAccessibleSelectionInterface5clearEv',
    )
