"""
QV4::Managed binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4managed_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Managed to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Managed(QV4.Value):
  """
  The cute side of Qt's QV4::Managed: a plain Python object standing in front
  of one C++ QV4::Managed.

  It is built on the cute 'QV4::Value', as Qt's QV4::Managed is built on Qt's
  QV4::Value, and has everything that class has. Qt's QV4::Managed is built
  on Qt's QV4::VTableBase as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QV4::Managed that has a ritual and that Python can
  call so far, 20 names in all: '__dataTest', 'd_unchecked', 'd',
  'typeToString', 'internalClass', 'engine', 'isV4SequenceType',
  'isV4QObjectWrapper', 'isQmlListPropertyType', 'isArrayLike',
  'isArrayObject', 'isStringObject', 'isSymbolObject', 'className',
  'isEqualTo', 'inUse', 'markBit', 'mark', 'heapObject', 'virtualIsEqualTo'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::Managed::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'const VTable *QV4::Managed::vtable() const': gives 'QV4::VTable',
    which has no cute class yet.

  What has no ritual
  ------------------

  7 of the 29 functions Qt declares: 3 forbidden; 2 not a gap; 2 a template.

  What to expect
  --------------

  - The C++ QV4::Managed is created at the first use, not by
    'QV4::Managed(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Managed.
  - Each name of Qt's QV4::Managed that has no cute function yet,
    'staticVTable', 'vtable', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Managed, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QV4::Managed::Type' of Qt, with the 37 names Qt gives in it.
    """

    Type_Invalid = Kee[int](0)
    Type_String = Kee[int](1)
    Type_Object = Kee[int](2)
    Type_Symbol = Kee[int](3)
    Type_ArrayObject = Kee[int](4)
    Type_FunctionObject = Kee[int](5)
    Type_GeneratorObject = Kee[int](6)
    Type_BooleanObject = Kee[int](7)
    Type_NumberObject = Kee[int](8)
    Type_StringObject = Kee[int](9)
    Type_SymbolObject = Kee[int](10)
    Type_DateObject = Kee[int](11)
    Type_RegExpObject = Kee[int](12)
    Type_ErrorObject = Kee[int](13)
    Type_ArgumentsObject = Kee[int](14)
    Type_JsonObject = Kee[int](15)
    Type_MathObject = Kee[int](16)
    Type_ProxyObject = Kee[int](17)
    Type_UrlObject = Kee[int](18)
    Type_UrlSearchParamsObject = Kee[int](19)
    Type_ExecutionContext = Kee[int](20)
    Type_InternalClass = Kee[int](21)
    Type_SetIteratorObject = Kee[int](22)
    Type_MapIteratorObject = Kee[int](23)
    Type_ArrayIteratorObject = Kee[int](24)
    Type_StringIteratorObject = Kee[int](25)
    Type_ForInIterator = Kee[int](26)
    Type_RegExp = Kee[int](27)
    Type_V4Sequence = Kee[int](28)
    Type_QmlListProperty = Kee[int](29)
    Type_V4QObjectWrapper = Kee[int](30)
    Type_QMLTypeWrapper = Kee[int](31)
    Type_V4ReferenceObject = Kee[int](32)
    Type_QMLValueTypeWrapper = Kee[int](33)
    Type_MemberData = Kee[int](34)
    Type_ArrayData = Kee[int](35)
    Type_StringOrSymbol = Kee[int](36)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Type)
  def typeToString(a0: Type) -> str:
    """
    Calls Qt's 'QString QV4::Managed::typeToString(Type a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#typeToString

    Parameters
    ----------

    a0 : Type
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Managed::typeToString(Type a0)
    return Rituals.call(
        'ritual_ZN3QV47Managed12typeToStringENS0_4TypeE', a0.value,
    )

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def virtualIsEqualTo(
      m: Optional[Managed],
      other: Optional[Managed],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::virtualIsEqualTo(Managed *m, Managed
    *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#virtualIsEqualTo

    Parameters
    ----------

    m : Optional[Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    other : Optional[Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Managed::virtualIsEqualTo(Managed *m, Managed *other)
    return Rituals.call(
        'ritual_ZN3QV47Managed16virtualIsEqualToEPS0_S1_',
        CuteMixin._addressOf(m), CuteMixin._addressOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Managed'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.Base]:
    """
    Calls Qt's 'QV4::Heap::Base *QV4::Managed::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.Base]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Base *QV4::Managed::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV47Managed11d_uncheckedEv')
    return QV4.Heap.Base._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.Base]:
    """
    Calls Qt's 'QV4::Heap::Base *QV4::Managed::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#d

    Returns
    -------

    Optional[QV4.Heap.Base]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Base *QV4::Managed::d() const
    address = self.uglySide.call('ritual_ZNK3QV47Managed1dEv')
    return QV4.Heap.Base._cuteAt(address)

  def internalClass(self) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass *QV4::Managed::internalClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#internalClass

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass *QV4::Managed::internalClass() const
    address = self.uglySide.call('ritual_ZNK3QV47Managed13internalClassEv')
    return QV4.Heap.InternalClass._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'ExecutionEngine *QV4::Managed::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionEngine *QV4::Managed::engine() const
    address = self.uglySide.call('ritual_ZNK3QV47Managed6engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  def isV4SequenceType(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isV4SequenceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#isV4SequenceType
    """
    #  bool QV4::Managed::isV4SequenceType() const
    return self.uglySide.call('ritual_ZNK3QV47Managed16isV4SequenceTypeEv')

  def isV4QObjectWrapper(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isV4QObjectWrapper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-managed.html#isV4QObjectWrapper
    """
    #  bool QV4::Managed::isV4QObjectWrapper() const
    return self.uglySide.call('ritual_ZNK3QV47Managed18isV4QObjectWrapperEv')

  def isQmlListPropertyType(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isQmlListPropertyType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-managed.html#isQmlListPropertyType
    """
    #  bool QV4::Managed::isQmlListPropertyType() const
    return self.uglySide.call(
        'ritual_ZNK3QV47Managed21isQmlListPropertyTypeEv',
    )

  def isArrayLike(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isArrayLike() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#isArrayLike
    """
    #  bool QV4::Managed::isArrayLike() const
    return self.uglySide.call('ritual_ZNK3QV47Managed11isArrayLikeEv')

  def isArrayObject(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isArrayObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#isArrayObject
    """
    #  bool QV4::Managed::isArrayObject() const
    return self.uglySide.call('ritual_ZNK3QV47Managed13isArrayObjectEv')

  def isStringObject(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isStringObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#isStringObject
    """
    #  bool QV4::Managed::isStringObject() const
    return self.uglySide.call('ritual_ZNK3QV47Managed14isStringObjectEv')

  def isSymbolObject(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isSymbolObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#isSymbolObject
    """
    #  bool QV4::Managed::isSymbolObject() const
    return self.uglySide.call('ritual_ZNK3QV47Managed14isSymbolObjectEv')

  def className(self) -> str:
    """
    Calls Qt's 'QString QV4::Managed::className() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#className

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Managed::className() const
    return self.uglySide.call('ritual_ZNK3QV47Managed9classNameEv')

  @overload(THIS)
  @overload(NoneType)
  def isEqualTo(self, other: Optional[Managed]) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::isEqualTo(const Managed *other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#isEqualTo

    Parameters
    ----------

    other : Optional[Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Managed::isEqualTo(const Managed *other) const
    return self.uglySide.call(
        'ritual_ZNK3QV47Managed9isEqualToEPKS0_', self._addressOf(other),
    )

  def inUse(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::inUse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#inUse
    """
    #  bool QV4::Managed::inUse() const
    return self.uglySide.call('ritual_ZNK3QV47Managed5inUseEv')

  def markBit(self) -> bool:
    """
    Calls Qt's 'bool QV4::Managed::markBit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#markBit
    """
    #  bool QV4::Managed::markBit() const
    return self.uglySide.call('ritual_ZNK3QV47Managed7markBitEv')

  def heapObject(self) -> Optional[QV4.Heap.Base]:
    """
    Calls Qt's 'Heap::Base *QV4::Managed::heapObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#heapObject

    Returns
    -------

    Optional[QV4.Heap.Base]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Base *QV4::Managed::heapObject() const
    address = self.uglySide.call('ritual_ZNK3QV47Managed10heapObjectEv')
    return QV4.Heap.Base._cuteAt(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::Managed::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#__dataTest
    """
    #  void QV4::Managed::__dataTest()
    self.uglySide.call('ritual_ZN3QV47Managed10__dataTestEv')

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def mark(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::Managed::mark(MarkStack *markStack)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-managed.html#mark

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Managed::mark(MarkStack *markStack)
    self.uglySide.call(
        'ritual_ZN3QV47Managed4markEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  @staticmethod
  def staticVTable(*__, **_) -> Never:
    """
    Qt's 'const QV4::VTable *QV4::Managed::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Managed.staticVTable' has no cute function yet. Qt's 'const "
        "QV4::VTable *QV4::Managed::staticVTable()': gives 'QV4::VTable', "
        "which has no cute class yet.")

  @staticmethod
  def vtable(*__, **_) -> Never:
    """
    Qt's 'const VTable *QV4::Managed::vtable() const': gives 'QV4::VTable',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Managed.vtable' has no cute function yet. Qt's 'const VTable "
        "*QV4::Managed::vtable() const': gives 'QV4::VTable', which has no "
        "cute class yet.")
