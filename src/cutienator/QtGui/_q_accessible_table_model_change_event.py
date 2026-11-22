"""
QAccessibleTableModelChangeEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QAccessibleEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleInterface = WAIT['QAccessibleInterface']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTableModelChangeEvent(QAccessibleEvent):
  """
  The cute side of Qt's QAccessibleTableModelChangeEvent: a plain Python
  object standing in front of one C++ QAccessibleTableModelChangeEvent.

  It is built on the cute 'QAccessibleEvent', as Qt's
  QAccessibleTableModelChangeEvent is built on Qt's QAccessibleEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTableModelChangeEvent that has a ritual
  and that Python can call so far, 10 names in all: 'setModelChangeType',
  'modelChangeType', 'setFirstRow', 'setFirstColumn', 'setLastRow',
  'setLastColumn', 'firstRow', 'firstColumn', 'lastRow', 'lastColumn'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QAccessibleTableModelChangeEvent::~QAccessibleTableModelChangeEvent()':
    the destructor: Python never removes a C++
    QAccessibleTableModelChangeEvent.

  What to expect
  --------------

  - The C++ QAccessibleTableModelChangeEvent is created at the first use, not
    by 'QAccessibleTableModelChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTableModelChangeEvent.
  """

  #  The enums Qt writes inside QAccessibleTableModelChangeEvent, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ModelChangeType(CuteNum):
    """
    The enum 'QAccessibleTableModelChangeEvent::ModelChangeType' of Qt, with
    the 6 names Qt gives in it.
    """

    ModelReset = Kee[int](0)
    DataChanged = Kee[int](1)
    RowsInserted = Kee[int](2)
    ColumnsInserted = Kee[int](3)
    RowsRemoved = Kee[int](4)
    ColumnsRemoved = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTableModelChangeEvent'

  #  A C++ QAccessibleTableModelChangeEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTableModelChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def modelChangeType(self) -> ModelChangeType:
    """
    Calls Qt's 'ModelChangeType
    QAccessibleTableModelChangeEvent::modelChangeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html

    Returns
    -------

    ModelChangeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ModelChangeType(number)'
      gives.
    """
    #  ModelChangeType QAccessibleTableModelChangeEvent::modelChangeType()
    #      const
    return QAccessibleTableModelChangeEvent.ModelChangeType(
        self.uglySide.call(
            'ritual_ZNK32QAccessibleTableModelChangeEvent15modelChangeTypeE'
            'v',
        ))

  def firstRow(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableModelChangeEvent::firstRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html#firstRow
    """
    #  int QAccessibleTableModelChangeEvent::firstRow() const
    return self.uglySide.call(
        'ritual_ZNK32QAccessibleTableModelChangeEvent8firstRowEv',
    )

  def firstColumn(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableModelChangeEvent::firstColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html#firstColumn
    """
    #  int QAccessibleTableModelChangeEvent::firstColumn() const
    return self.uglySide.call(
        'ritual_ZNK32QAccessibleTableModelChangeEvent11firstColumnEv',
    )

  def lastRow(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableModelChangeEvent::lastRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html#lastRow
    """
    #  int QAccessibleTableModelChangeEvent::lastRow() const
    return self.uglySide.call(
        'ritual_ZNK32QAccessibleTableModelChangeEvent7lastRowEv',
    )

  def lastColumn(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableModelChangeEvent::lastColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html#lastColumn
    """
    #  int QAccessibleTableModelChangeEvent::lastColumn() const
    return self.uglySide.call(
        'ritual_ZNK32QAccessibleTableModelChangeEvent10lastColumnEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ModelChangeType)
  def setModelChangeType(self, changeType: ModelChangeType) -> None:
    """
    Calls Qt's 'void
    QAccessibleTableModelChangeEvent::setModelChangeType(ModelChangeType
    changeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html

    Parameters
    ----------

    changeType : ModelChangeType
      Passed on as its number.
    """
    #  void QAccessibleTableModelChangeEvent::setModelChangeType(
    #      ModelChangeType changeType)
    self.uglySide.call(
        'ritual_ZN32QAccessibleTableModelChangeEvent18setModelChangeTypeENS'
        '_15ModelChangeTypeE',
        changeType.value,
    )

  @overload(int)
  def setFirstRow(self, row: int) -> None:
    """
    Calls Qt's 'void QAccessibleTableModelChangeEvent::setFirstRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html#setFirstRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QAccessibleTableModelChangeEvent::setFirstRow(int row)
    self.uglySide.call(
        'ritual_ZN32QAccessibleTableModelChangeEvent11setFirstRowEi', row,
    )

  @overload(int)
  def setFirstColumn(self, col: int) -> None:
    """
    Calls Qt's 'void QAccessibleTableModelChangeEvent::setFirstColumn(int
    col)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html

    Parameters
    ----------

    col : int
      Passed on as it is.
    """
    #  void QAccessibleTableModelChangeEvent::setFirstColumn(int col)
    self.uglySide.call(
        'ritual_ZN32QAccessibleTableModelChangeEvent14setFirstColumnEi', col,
    )

  @overload(int)
  def setLastRow(self, row: int) -> None:
    """
    Calls Qt's 'void QAccessibleTableModelChangeEvent::setLastRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html#setLastRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QAccessibleTableModelChangeEvent::setLastRow(int row)
    self.uglySide.call(
        'ritual_ZN32QAccessibleTableModelChangeEvent10setLastRowEi', row,
    )

  @overload(int)
  def setLastColumn(self, col: int) -> None:
    """
    Calls Qt's 'void QAccessibleTableModelChangeEvent::setLastColumn(int
    col)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html

    Parameters
    ----------

    col : int
      Passed on as it is.
    """
    #  void QAccessibleTableModelChangeEvent::setLastColumn(int col)
    self.uglySide.call(
        'ritual_ZN32QAccessibleTableModelChangeEvent13setLastColumnEi', col,
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

  @overload(QObject, ModelChangeType)
  @overload(NoneType, ModelChangeType)
  def __init__(
      self,
      obj: Optional[QObject],
      changeType: ModelChangeType,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTableModelChangeEvent::QAccessibleTableModelChangeEvent(
    QObject *obj, ModelChangeType changeType)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    changeType : ModelChangeType
      Passed on as its number.
    """
    #  QAccessibleTableModelChangeEvent::
    #      QAccessibleTableModelChangeEvent(QObject *obj, ModelChangeType
    #      changeType)
    self._noteCreation(
        QAccessibleTableModelChangeEvent, lambda: Rituals.call(
            'ritual_ZN32QAccessibleTableModelChangeEventC1EP7QObjectNS_15Mo'
            'delChangeTypeE',
            self._addressOf(obj), changeType.value,
        ))

  @overload(QAccessibleInterface, ModelChangeType)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      changeType: ModelChangeType,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTableModelChangeEvent::QAccessibleTableModelChangeEvent(
    QAccessibleInterface *iface, ModelChangeType changeType)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablemodelchangeevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    changeType : ModelChangeType
      Passed on as its number.
    """
    #  QAccessibleTableModelChangeEvent::
    #      QAccessibleTableModelChangeEvent(QAccessibleInterface *iface,
    #      ModelChangeType changeType)
    self._noteCreation(
        QAccessibleTableModelChangeEvent, lambda: Rituals.call(
            'ritual_ZN32QAccessibleTableModelChangeEventC1EP20QAccessibleIn'
            'terfaceNS_15ModelChangeTypeE',
            self._addressOf(iface), changeType.value,
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
