"""
QV4::Heap::SimpleArrayData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Heap::SimpleArrayData to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SimpleArrayData(QV4.Heap.ArrayData):
  """
  The cute side of Qt's QV4::Heap::SimpleArrayData: a plain Python object
  standing in front of one C++ QV4::Heap::SimpleArrayData.

  It is built on the cute 'QV4::Heap::ArrayData', as Qt's
  QV4::Heap::SimpleArrayData is built on Qt's QV4::Heap::ArrayData, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::SimpleArrayData that has a ritual and
  that Python can call so far, 4 names in all: 'mappedIndex', 'data',
  'setData', 'attributes'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::SimpleArrayData is created at the first use, not by
    'QV4::Heap::SimpleArrayData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::SimpleArrayData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::SimpleArrayData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def mappedIndex(self, index: int) -> int:
    """
    Calls Qt's 'uint QV4::Heap::SimpleArrayData::mappedIndex(uint index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-simplearraydata.html#mappedIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  uint QV4::Heap::SimpleArrayData::mappedIndex(uint index) const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15SimpleArrayData11mappedIndexEj', index,
    )

  @overload(int)
  def data(self, index: int) -> QV4.Value:
    """
    Calls Qt's 'const Value &QV4::Heap::SimpleArrayData::data(uint index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-simplearraydata.html#data

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QV4.Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  const Value &QV4::Heap::SimpleArrayData::data(uint index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15SimpleArrayData4dataEj', index,
    )
    return QV4.Value._cuteOwning(address)

  @overload(int)
  def attributes(self, i: int) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes
    QV4::Heap::SimpleArrayData::attributes(uint i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-simplearraydata.html#attributes

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes QV4::Heap::SimpleArrayData::attributes(uint i)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15SimpleArrayData10attributesEj', i,
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.EngineBase'], int, WAIT['QV4.Value'])
  @overload(NoneType, int, WAIT['QV4.Value'])
  def setData(
      self,
      e: Optional[QV4.EngineBase],
      index: int,
      newVal: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::SimpleArrayData::setData(EngineBase *e, uint
    index, Value newVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-simplearraydata.html#setData

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    newVal : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Heap::SimpleArrayData::setData(EngineBase *e, uint index,
    #      Value newVal)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15SimpleArrayData7setDataEPNS_10EngineBaseEjNS_5'
        'ValueE',
        self._addressOf(e), index, self._valueOf(newVal),
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
