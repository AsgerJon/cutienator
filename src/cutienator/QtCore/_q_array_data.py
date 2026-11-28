"""
QArrayData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qarraydata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QArrayData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QArrayData: a plain Python object standing in front
  of one C++ QArrayData.

  What exists
  -----------

  Every function of Qt's QArrayData that has a ritual and that Python can
  call so far, 8 names in all: 'allocatedCapacity', 'constAllocatedCapacity',
  'ref', 'deref', 'isShared', 'needsDetach', 'detachCapacity', 'deallocate'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QArrayData::allocate(QArrayData **pdata, qsizetype
    objectSize, qsizetype alignment, qsizetype capacity, AllocationOption
    option)': takes a type Python has no way to hand over yet.
  - Qt's 'void *QArrayData::allocate1(QArrayData **pdata, qsizetype capacity,
    AllocationOption option)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void *QArrayData::allocate2(QArrayData **pdata, qsizetype capacity,
    AllocationOption option)': takes a type Python has no way to hand over
    yet.
  - Qt's 'std::pair<QArrayData *, void *>
    QArrayData::reallocateUnaligned(QArrayData *data, void *dataPointer,
    qsizetype objectSize, qsizetype newCapacity, AllocationOption option)':
    names 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QArrayData is created at the first use, not by 'QArrayData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QArrayData.
  - Each name of Qt's QArrayData that has no cute function yet, 'allocate',
    'allocate1', 'allocate2', 'reallocateUnaligned', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QArrayData, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AllocationOption(CuteNum):
    """
    The enum 'QArrayData::AllocationOption' of Qt, with the 2 names Qt gives
    in it.
    """

    Grow = Kee[int](0)
    KeepSize = Kee[int](1)

  class ArrayOption(CuteFlags):
    """
    The flags enum 'QArrayData::ArrayOption' of Qt, with the 2 names Qt gives
    in it. Qt names the type of its combinations 'QArrayData::ArrayOptions'.
    """

    ArrayOptionDefault = 0x0
    CapacityReserved = 0x1

  ArrayOptions = ArrayOption

  class GrowthPosition(CuteNum):
    """
    The enum 'QArrayData::GrowthPosition' of Qt, with the 2 names Qt gives in
    it.
    """

    GrowsAtEnd = Kee[int](0)
    GrowsAtBeginning = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, int, int)
  @overload(NoneType, int, int)
  def deallocate(
      data: Optional[QArrayData],
      objectSize: int,
      alignment: int,
  ) -> None:
    """
    Calls Qt's 'void QArrayData::deallocate(QArrayData *data, qsizetype
    objectSize, qsizetype alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qarraydata.html#deallocate

    Parameters
    ----------

    data : Optional[QArrayData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectSize : int
      Passed on as it is.

    alignment : int
      Passed on as it is.
    """
    #  void QArrayData::deallocate(QArrayData *data, qsizetype objectSize,
    #      qsizetype alignment)
    Rituals.call(
        'ritual_ZN10QArrayData10deallocateEPS_xx',
        CuteMixin._addressOf(data), objectSize, alignment,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QArrayData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def constAllocatedCapacity(self) -> int:
    """
    Calls Qt's 'qsizetype QArrayData::constAllocatedCapacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qarraydata.html#constAllocatedCapacity
    """
    #  qsizetype QArrayData::constAllocatedCapacity() const
    return self.uglySide.call(
        'ritual_ZNK10QArrayData22constAllocatedCapacityEv',
    )

  def isShared(self) -> bool:
    """
    Calls Qt's 'bool QArrayData::isShared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qarraydata.html#isShared
    """
    #  bool QArrayData::isShared() const
    return self.uglySide.call('ritual_ZNK10QArrayData8isSharedEv')

  @overload(int)
  def detachCapacity(self, newSize: int) -> int:
    """
    Calls Qt's 'qsizetype QArrayData::detachCapacity(qsizetype newSize)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qarraydata.html#detachCapacity

    Parameters
    ----------

    newSize : int
      Passed on as it is.
    """
    #  qsizetype QArrayData::detachCapacity(qsizetype newSize) const
    return self.uglySide.call(
        'ritual_ZNK10QArrayData14detachCapacityEx', newSize,
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

  def allocatedCapacity(self) -> int:
    """
    Calls Qt's 'qsizetype QArrayData::allocatedCapacity()'.

    Qt's own words: https://doc.qt.io/qt-6/qarraydata.html#allocatedCapacity
    """
    #  qsizetype QArrayData::allocatedCapacity()
    return self.uglySide.call('ritual_ZN10QArrayData17allocatedCapacityEv')

  def ref(self) -> bool:
    """
    Calls Qt's 'bool QArrayData::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qarraydata.html#ref
    """
    #  bool QArrayData::ref()
    return self.uglySide.call('ritual_ZN10QArrayData3refEv')

  def deref(self) -> bool:
    """
    Calls Qt's 'bool QArrayData::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qarraydata.html#deref
    """
    #  bool QArrayData::deref()
    return self.uglySide.call('ritual_ZN10QArrayData5derefEv')

  def needsDetach(self) -> bool:
    """
    Calls Qt's 'bool QArrayData::needsDetach()'.

    Qt's own words: https://doc.qt.io/qt-6/qarraydata.html#needsDetach
    """
    #  bool QArrayData::needsDetach()
    return self.uglySide.call('ritual_ZN10QArrayData11needsDetachEv')

  @staticmethod
  def allocate(*__, **_) -> Never:
    """
    Qt's 'void *QArrayData::allocate(QArrayData **pdata, qsizetype
    objectSize, qsizetype alignment, qsizetype capacity, AllocationOption
    option)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QArrayData.allocate' has no cute function yet. Qt's 'void "
        "*QArrayData::allocate(QArrayData **pdata, qsizetype objectSize, "
        "qsizetype alignment, qsizetype capacity, AllocationOption "
        "option)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def allocate1(*__, **_) -> Never:
    """
    Qt's 'void *QArrayData::allocate1(QArrayData **pdata, qsizetype capacity,
    AllocationOption option)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QArrayData.allocate1' has no cute function yet. Qt's 'void "
        "*QArrayData::allocate1(QArrayData **pdata, qsizetype capacity, "
        "AllocationOption option)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def allocate2(*__, **_) -> Never:
    """
    Qt's 'void *QArrayData::allocate2(QArrayData **pdata, qsizetype capacity,
    AllocationOption option)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QArrayData.allocate2' has no cute function yet. Qt's 'void "
        "*QArrayData::allocate2(QArrayData **pdata, qsizetype capacity, "
        "AllocationOption option)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def reallocateUnaligned(*__, **_) -> Never:
    """
    Qt's 'std::pair<QArrayData *, void *>
    QArrayData::reallocateUnaligned(QArrayData *data, void *dataPointer,
    qsizetype objectSize, qsizetype newCapacity, AllocationOption option)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QArrayData.reallocateUnaligned' has no cute function yet. Qt's "
        "'std::pair<QArrayData *, void *> "
        "QArrayData::reallocateUnaligned(QArrayData *data, void "
        "*dataPointer, qsizetype objectSize, qsizetype newCapacity, "
        "AllocationOption option)': names 'void', which has no cute class "
        "yet.")
