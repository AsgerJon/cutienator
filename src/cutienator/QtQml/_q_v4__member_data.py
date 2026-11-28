"""
QV4::MemberData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4memberdata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::MemberData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MemberData(QV4.Managed):
  """
  The cute side of Qt's QV4::MemberData: a plain Python object standing in
  front of one C++ QV4::MemberData.

  It is built on the cute 'QV4::Managed', as Qt's QV4::MemberData is built on
  Qt's QV4::Managed, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::MemberData that has a ritual and that Python
  can call so far, 8 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', '__getitem__', 'data', 'set', 'size'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  6 of the 15 functions Qt declares: 3 forbidden; 2 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::MemberData is created at the first use, not by
    'QV4::MemberData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::MemberData.
  - Each name of Qt's QV4::MemberData that has no cute function yet,
    'allocate', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::MemberData::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-memberdata.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::MemberData::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV410MemberData20defaultInternalClassEPNS_10EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::MemberData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.MemberData]:
    """
    Calls Qt's 'QV4::Heap::MemberData *QV4::MemberData::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.MemberData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::MemberData *QV4::MemberData::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410MemberData11d_uncheckedEv')
    return QV4.Heap.MemberData._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.MemberData]:
    """
    Calls Qt's 'QV4::Heap::MemberData *QV4::MemberData::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#d

    Returns
    -------

    Optional[QV4.Heap.MemberData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::MemberData *QV4::MemberData::d() const
    address = self.uglySide.call('ritual_ZNK3QV410MemberData1dEv')
    return QV4.Heap.MemberData._cuteAt(address)

  def data(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::MemberData::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#data

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::MemberData::data() const
    address = self.uglySide.call('ritual_ZNK3QV410MemberData4dataEv')
    return QV4.Value._cuteAt(address)

  def size(self) -> int:
    """
    Calls Qt's 'uint QV4::MemberData::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#size
    """
    #  uint QV4::MemberData::size() const
    return self.uglySide.call('ritual_ZNK3QV410MemberData4sizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, idx: int) -> QV4.Value:
    """
    Calls Qt's 'const Value &QV4::MemberData::operator[](uint idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#operator[]

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QV4.Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  const Value &QV4::MemberData::operator[](uint idx) const
    address = self.uglySide.call('ritual_ZNK3QV410MemberDataixEj', idx)
    return QV4.Value._cuteOwning(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::MemberData::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#__dataTest
    """
    #  void QV4::MemberData::__dataTest()
    self.uglySide.call('ritual_ZN3QV410MemberData10__dataTestEv')

  @overload(WAIT['QV4.EngineBase'], int, QV4.Value)
  @overload(NoneType, int, QV4.Value)
  def set(
      self,
      e: Optional[QV4.EngineBase],
      index: int,
      v: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::MemberData::set(EngineBase *e, uint index, Value
    v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#set

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::MemberData::set(EngineBase *e, uint index, Value v)
    self.uglySide.call(
        'ritual_ZN3QV410MemberData3setEPNS_10EngineBaseEjNS_5ValueE',
        self._addressOf(e), index, self._valueOf(v),
    )

  @overload(WAIT['QV4.EngineBase'], int, WAIT['QV4.Heap.Base'])
  @overload(WAIT['QV4.EngineBase'], int, NoneType)
  @overload(NoneType, int, WAIT['QV4.Heap.Base'])
  @overload(NoneType, int, NoneType)
  def set(
      self,
      e: Optional[QV4.EngineBase],
      index: int,
      b: Optional[QV4.Heap.Base],
  ) -> None:
    """
    Calls Qt's 'void QV4::MemberData::set(EngineBase *e, uint index,
    Heap::Base *b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-memberdata.html#set

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::MemberData::set(EngineBase *e, uint index, Heap::Base *b)
    self.uglySide.call(
        'ritual_ZN3QV410MemberData3setEPNS_10EngineBaseEjPNS_4Heap4BaseE',
        self._addressOf(e), index, self._addressOf(b),
    )

  @staticmethod
  def allocate(*__, **_) -> Never:
    """
    Qt's 'Heap::MemberData *QV4::MemberData::allocate(QV4::ExecutionEngine
    *e, uint n, Heap::MemberData *old)': leans on
    'QV4::MemberData::static_vtbl', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.MemberData.allocate' has no cute function yet. Qt's "
        "'Heap::MemberData *QV4::MemberData::allocate(QV4::ExecutionEngine "
        "*e, uint n, Heap::MemberData *old)': leans on "
        "'QV4::MemberData::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
