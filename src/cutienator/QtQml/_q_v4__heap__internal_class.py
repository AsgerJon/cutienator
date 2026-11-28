"""
QV4::Heap::InternalClass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::InternalClass to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InternalClass(QV4.Heap.Base):
  """
  The cute side of Qt's QV4::Heap::InternalClass: a plain Python object
  standing in front of one C++ QV4::Heap::InternalClass.

  It is built on the cute 'QV4::Heap::Base', as Qt's QV4::Heap::InternalClass
  is built on Qt's QV4::Heap::Base, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::InternalClass that has a ritual and that
  Python can call so far, 20 names in all: 'isExtensible', 'isSealed',
  'isFrozen', 'isUsedAsProto', 'isLocked', 'init', 'keyAt', 'nonExtensible',
  'locked', 'findEntry', 'find', 'findValueOrGetter', 'findValueOrSetter',
  'indexOfValueOrGetter', 'verifyIndex', 'isImplicitlyFrozen',
  'asProtoClass', 'changePrototype', 'changePrototypeImpl',
  'removeChildEntry'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'InternalClassTransition
    &QV4::Heap::InternalClass::lookupOrInsertTransition(const
    InternalClassTransition &t)': gives a type Python has no way to take yet.
  - Qt's 'InternalClass *QV4::Heap::InternalClass::changeVTable(const VTable
    *vt)': names 'QV4::VTable', which has no cute class yet.
  - Qt's 'InternalClass *QV4::Heap::InternalClass::changeVTableImpl(const
    VTable *vt)': names 'QV4::VTable', which has no cute class yet.

  What has no ritual
  ------------------

  14 of the 37 functions Qt declares: 12 leans on 'QV4; 2 Qt's library has no
  name for it, and its code in Qt's source does not compile apart from its
  file.

  What to expect
  --------------

  - The C++ QV4::Heap::InternalClass is created at the first use, not by
    'QV4::Heap::InternalClass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::InternalClass.
  - Each name of Qt's QV4::Heap::InternalClass that has no cute function yet,
    'addMember', 'addMemberImpl', 'canned', 'changeMember', 'changeVTable',
    'changeVTableImpl', 'cryopreserved', 'frozen',
    'lookupOrInsertTransition', 'removeMember', 'sealed', 'updateProtoUsage',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QV4::Heap::InternalClass, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flag(CuteNum):
    """
    The enum 'QV4::Heap::InternalClass::Flag' of Qt, with the 5 names Qt
    gives in it.
    """

    NotExtensible = Kee[int](1)
    Sealed = Kee[int](2)
    Frozen = Kee[int](4)
    UsedAsProto = Kee[int](8)
    Locked = Kee[int](16)

  #  The classes Qt writes inside QV4::Heap::InternalClass, each a class in
  #  here as in C++.

  class IndexAndAttribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Heap::InternalClass::IndexAndAttribute: a
    plain Python object standing in front of one C++
    QV4::Heap::InternalClass::IndexAndAttribute.

    C++ hands a QV4::Heap::InternalClass::IndexAndAttribute around as a copy,
    so every C++ QV4::Heap::InternalClass::IndexAndAttribute behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Heap::InternalClass::IndexAndAttribute that
    has a ritual and that Python can call so far, 1 name in all: 'isValid'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QV4::Heap::InternalClass::IndexAndAttribute::~IndexAndAttribute()':
      the destructor: Python removes its C++
      QV4::Heap::InternalClass::IndexAndAttribute by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Heap::InternalClass::IndexAndAttribute is created at the
      first use, not by 'QV4::Heap::InternalClass::IndexAndAttribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Heap::InternalClass::IndexAndAttribute back
      gives a copy the ritual made for Python, in a new cute
      QV4::Heap::InternalClass::IndexAndAttribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Heap::InternalClass::IndexAndAttribute'

    #  Qt's '~QV4::Heap::InternalClass::IndexAndAttribute()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Heap::InternalClass::IndexAndAttribute behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV44Heap13InternalClass17IndexAndAttributeD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QV4::Heap::InternalClass::IndexAndAttribute::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-heap-internalclass-indexandattribute.html
      """
      #  bool QV4::Heap::InternalClass::IndexAndAttribute::isValid() const
      return self.uglySide.call(
          'ritual_ZNK3QV44Heap13InternalClass17IndexAndAttribute7isValidEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::InternalClass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isExtensible(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::InternalClass::isExtensible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#isExtensible
    """
    #  bool QV4::Heap::InternalClass::isExtensible() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13InternalClass12isExtensibleEv',
    )

  def isSealed(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::InternalClass::isSealed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#isSealed
    """
    #  bool QV4::Heap::InternalClass::isSealed() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13InternalClass8isSealedEv',
    )

  def isFrozen(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::InternalClass::isFrozen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#isFrozen
    """
    #  bool QV4::Heap::InternalClass::isFrozen() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13InternalClass8isFrozenEv',
    )

  def isUsedAsProto(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::InternalClass::isUsedAsProto() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#isUsedAsProto
    """
    #  bool QV4::Heap::InternalClass::isUsedAsProto() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13InternalClass13isUsedAsProtoEv',
    )

  def isLocked(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::InternalClass::isLocked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#isLocked
    """
    #  bool QV4::Heap::InternalClass::isLocked() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13InternalClass8isLockedEv',
    )

  @overload(int)
  def keyAt(self, index: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Heap::InternalClass::keyAt(uint index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-internalclass.html#keyAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::Heap::InternalClass::keyAt(uint index) const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13InternalClass5keyAtEj', index,
    )

  def isImplicitlyFrozen(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::InternalClass::isImplicitlyFrozen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#isImplicitlyFrozen
    """
    #  bool QV4::Heap::InternalClass::isImplicitlyFrozen() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13InternalClass18isImplicitlyFrozenEv',
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

  @overload(THIS)
  @overload(NoneType)
  def init(self, other: Optional[InternalClass]) -> None:
    """
    Calls Qt's 'void QV4::Heap::InternalClass::init(InternalClass *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-internalclass.html#init

    Parameters
    ----------

    other : Optional[InternalClass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::InternalClass::init(InternalClass *other)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass4initEPS1_',
        self._addressOf(other),
    )

  def nonExtensible(self) -> Optional[InternalClass]:
    """
    Calls Qt's 'InternalClass *QV4::Heap::InternalClass::nonExtensible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#nonExtensible

    Returns
    -------

    Optional[InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InternalClass *QV4::Heap::InternalClass::nonExtensible()
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass13nonExtensibleEv',
    )
    return InternalClass._cuteAt(address)

  def locked(self) -> Optional[InternalClass]:
    """
    Calls Qt's 'InternalClass *QV4::Heap::InternalClass::locked()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-internalclass.html#locked

    Returns
    -------

    Optional[InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InternalClass *QV4::Heap::InternalClass::locked()
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass6lockedEv',
    )
    return InternalClass._cuteAt(address)

  @overload(WAIT['QV4.PropertyKey'])
  def findEntry(
      self,
      id: QV4.PropertyKey,
  ) -> Optional[QV4.PropertyHash.Entry]:
    """
    Calls Qt's 'PropertyHash::Entry
    *QV4::Heap::InternalClass::findEntry(const PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#findEntry

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    Optional[QV4.PropertyHash.Entry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PropertyHash::Entry *QV4::Heap::InternalClass::findEntry(const
    #      PropertyKey id)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass9findEntryENS_11PropertyKeyE',
        self._valueOf(id),
    )
    return QV4.PropertyHash.Entry._cuteAt(address)

  @overload(WAIT['QV4.PropertyKey'])
  def find(self, id: QV4.PropertyKey) -> QV4.InternalClassEntry:
    """
    Calls Qt's 'InternalClassEntry QV4::Heap::InternalClass::find(const
    PropertyKey id)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-internalclass.html#find

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    QV4.InternalClassEntry
      A new cute QV4::InternalClassEntry around the copy Qt gave back. Python
      owns it.
    """
    #  InternalClassEntry QV4::Heap::InternalClass::find(const PropertyKey
    #      id)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass4findENS_11PropertyKeyE',
        self._valueOf(id),
    )
    return QV4.InternalClassEntry._cuteOwning(address)

  @overload(WAIT['QV4.PropertyKey'])
  def findValueOrGetter(self, id: QV4.PropertyKey) -> IndexAndAttribute:
    """
    Calls Qt's 'IndexAndAttribute
    QV4::Heap::InternalClass::findValueOrGetter(const PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#findValueOrGetter

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    IndexAndAttribute
      A new cute QV4::Heap::InternalClass::IndexAndAttribute around the copy
      Qt gave back. Python owns it.
    """
    #  IndexAndAttribute QV4::Heap::InternalClass::findValueOrGetter(const
    #      PropertyKey id)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass17findValueOrGetterENS_11Property'
        'KeyE',
        self._valueOf(id),
    )
    return QV4.Heap.InternalClass.IndexAndAttribute._cuteOwning(address)

  @overload(WAIT['QV4.PropertyKey'])
  def findValueOrSetter(self, id: QV4.PropertyKey) -> IndexAndAttribute:
    """
    Calls Qt's 'IndexAndAttribute
    QV4::Heap::InternalClass::findValueOrSetter(const PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#findValueOrSetter

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    IndexAndAttribute
      A new cute QV4::Heap::InternalClass::IndexAndAttribute around the copy
      Qt gave back. Python owns it.
    """
    #  IndexAndAttribute QV4::Heap::InternalClass::findValueOrSetter(const
    #      PropertyKey id)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass17findValueOrSetterENS_11Property'
        'KeyE',
        self._valueOf(id),
    )
    return QV4.Heap.InternalClass.IndexAndAttribute._cuteOwning(address)

  @overload(WAIT['QV4.PropertyKey'])
  def indexOfValueOrGetter(self, id: QV4.PropertyKey) -> int:
    """
    Calls Qt's 'uint QV4::Heap::InternalClass::indexOfValueOrGetter(const
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#indexOfValueOrGetter

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  uint QV4::Heap::InternalClass::indexOfValueOrGetter(const PropertyKey
    #      id)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass20indexOfValueOrGetterENS_11Prope'
        'rtyKeyE',
        self._valueOf(id),
    )

  @overload(WAIT['QV4.PropertyKey'], int)
  def verifyIndex(self, id: QV4.PropertyKey, index: int) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::InternalClass::verifyIndex(const PropertyKey
    id, uint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#verifyIndex

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    index : int
      Passed on as it is.
    """
    #  bool QV4::Heap::InternalClass::verifyIndex(const PropertyKey id, uint
    #      index)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass11verifyIndexENS_11PropertyKeyEj',
        self._valueOf(id), index,
    )

  def asProtoClass(self) -> Optional[InternalClass]:
    """
    Calls Qt's 'InternalClass *QV4::Heap::InternalClass::asProtoClass()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#asProtoClass

    Returns
    -------

    Optional[InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InternalClass *QV4::Heap::InternalClass::asProtoClass()
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass12asProtoClassEv',
    )
    return InternalClass._cuteAt(address)

  @overload(WAIT['QV4.Heap.Object'])
  @overload(NoneType)
  def changePrototype(
      self,
      proto: Optional[QV4.Heap.Object],
  ) -> Optional[InternalClass]:
    """
    Calls Qt's 'InternalClass
    *QV4::Heap::InternalClass::changePrototype(Heap::Object *proto)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#changePrototype

    Parameters
    ----------

    proto : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InternalClass *QV4::Heap::InternalClass::changePrototype(Heap::Object
    #      *proto)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass15changePrototypeEPNS0_6ObjectE',
        self._addressOf(proto),
    )
    return InternalClass._cuteAt(address)

  @overload(WAIT['QV4.Heap.Object'])
  @overload(NoneType)
  def changePrototypeImpl(
      self,
      proto: Optional[QV4.Heap.Object],
  ) -> Optional[InternalClass]:
    """
    Calls Qt's 'InternalClass
    *QV4::Heap::InternalClass::changePrototypeImpl(Heap::Object *proto)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#changePrototypeImpl

    Parameters
    ----------

    proto : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InternalClass
    #      *QV4::Heap::InternalClass::changePrototypeImpl(Heap::Object
    #      *proto)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass19changePrototypeImplEPNS0_6Objec'
        'tE',
        self._addressOf(proto),
    )
    return InternalClass._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def removeChildEntry(self, child: Optional[InternalClass]) -> None:
    """
    Calls Qt's 'void QV4::Heap::InternalClass::removeChildEntry(InternalClass
    *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-internalclass.html#removeChildEntry

    Parameters
    ----------

    child : Optional[InternalClass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::InternalClass::removeChildEntry(InternalClass *child)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13InternalClass16removeChildEntryEPS1_',
        self._addressOf(child),
    )

  @staticmethod
  def addMember(*__, **_) -> Never:
    """
    - Qt's 'void QV4::Heap::InternalClass::addMember(QV4::Object *object,
      PropertyKey id, PropertyAttributes data, InternalClassEntry *entry)':
      leans on
      'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigned
      int, QV4::PropertyKey)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'InternalClass *QV4::Heap::InternalClass::addMember(PropertyKey
      identifier, PropertyAttributes data, InternalClassEntry *entry)': leans
      on 'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigned
      int, QV4::PropertyKey)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.addMember' has no cute function yet. Qt's "
        "'void QV4::Heap::InternalClass::addMember(QV4::Object *object, "
        "PropertyKey id, PropertyAttributes data, InternalClassEntry "
        "*entry)': leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigne"
        "d int, QV4::PropertyKey)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken. Qt's "
        "'InternalClass *QV4::Heap::InternalClass::addMember(PropertyKey "
        "identifier, PropertyAttributes data, InternalClassEntry *entry)': "
        "leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigne"
        "d int, QV4::PropertyKey)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def addMemberImpl(*__, **_) -> Never:
    """
    Qt's 'InternalClass *QV4::Heap::InternalClass::addMemberImpl(PropertyKey
    identifier, PropertyAttributes data, InternalClassEntry *entry)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'addDummyEntry'.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.addMemberImpl' has no cute function yet. "
        "Qt's 'InternalClass "
        "*QV4::Heap::InternalClass::addMemberImpl(PropertyKey identifier, "
        "PropertyAttributes data, InternalClassEntry *entry)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'addDummyEntry'.")

  @staticmethod
  def canned(*__, **_) -> Never:
    """
    Qt's 'InternalClass *QV4::Heap::InternalClass::canned()': leans on
    'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::
    SharedInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4::
    PropertyAttributes> const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.canned' has no cute function yet. Qt's "
        "'InternalClass *QV4::Heap::InternalClass::canned()': leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::Shar"
        "edInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4:"
        ":PropertyAttributes> const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def changeMember(*__, **_) -> Never:
    """
    - Qt's 'InternalClass *QV4::Heap::InternalClass::changeMember(PropertyKey
      identifier, PropertyAttributes data, InternalClassEntry *entry)': leans
      on 'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigned
      int, QV4::PropertyKey)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'void QV4::Heap::InternalClass::changeMember(QV4::Object *object,
      PropertyKey id, PropertyAttributes data, InternalClassEntry *entry)':
      leans on
      'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigned
      int, QV4::PropertyKey)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.changeMember' has no cute function yet. "
        "Qt's 'InternalClass "
        "*QV4::Heap::InternalClass::changeMember(PropertyKey identifier, "
        "PropertyAttributes data, InternalClassEntry *entry)': leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigne"
        "d int, QV4::PropertyKey)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken. Qt's "
        "'void QV4::Heap::InternalClass::changeMember(QV4::Object *object, "
        "PropertyKey id, PropertyAttributes data, InternalClassEntry "
        "*entry)': leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigne"
        "d int, QV4::PropertyKey)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def changeVTable(*__, **_) -> Never:
    """
    Qt's 'InternalClass *QV4::Heap::InternalClass::changeVTable(const VTable
    *vt)': names 'QV4::VTable', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.changeVTable' has no cute function yet. "
        "Qt's 'InternalClass *QV4::Heap::InternalClass::changeVTable(const "
        "VTable *vt)': names 'QV4::VTable', which has no cute class yet.")

  @staticmethod
  def changeVTableImpl(*__, **_) -> Never:
    """
    Qt's 'InternalClass *QV4::Heap::InternalClass::changeVTableImpl(const
    VTable *vt)': names 'QV4::VTable', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.changeVTableImpl' has no cute function "
        "yet. Qt's 'InternalClass "
        "*QV4::Heap::InternalClass::changeVTableImpl(const VTable *vt)': "
        "names 'QV4::VTable', which has no cute class yet.")

  @staticmethod
  def cryopreserved(*__, **_) -> Never:
    """
    Qt's 'InternalClass *QV4::Heap::InternalClass::cryopreserved()': leans on
    'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::
    SharedInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4::
    PropertyAttributes> const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.cryopreserved' has no cute function yet. "
        "Qt's 'InternalClass *QV4::Heap::InternalClass::cryopreserved()': "
        "leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::Shar"
        "edInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4:"
        ":PropertyAttributes> const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def frozen(*__, **_) -> Never:
    """
    Qt's 'InternalClass *QV4::Heap::InternalClass::frozen()': leans on
    'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::
    SharedInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4::
    PropertyAttributes> const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.frozen' has no cute function yet. Qt's "
        "'InternalClass *QV4::Heap::InternalClass::frozen()': leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::Shar"
        "edInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4:"
        ":PropertyAttributes> const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def lookupOrInsertTransition(*__, **_) -> Never:
    """
    Qt's 'InternalClassTransition
    &QV4::Heap::InternalClass::lookupOrInsertTransition(const
    InternalClassTransition &t)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.lookupOrInsertTransition' has no cute "
        "function yet. Qt's 'InternalClassTransition "
        "&QV4::Heap::InternalClass::lookupOrInsertTransition(const "
        "InternalClassTransition &t)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def removeMember(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::InternalClass::removeMember(QV4::Object *object,
    PropertyKey identifier)': leans on
    'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigned int,
    QV4::PropertyKey)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.removeMember' has no cute function yet. "
        "Qt's 'void QV4::Heap::InternalClass::removeMember(QV4::Object "
        "*object, PropertyKey identifier)': leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigne"
        "d int, QV4::PropertyKey)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def sealed(*__, **_) -> Never:
    """
    Qt's 'InternalClass *QV4::Heap::InternalClass::sealed()': leans on
    'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::
    SharedInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4::
    PropertyAttributes> const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.sealed' has no cute function yet. Qt's "
        "'InternalClass *QV4::Heap::InternalClass::sealed()': leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::Shar"
        "edInternalClassDataPrivate(QV4::SharedInternalClassDataPrivate<QV4:"
        ":PropertyAttributes> const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateProtoUsage(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::InternalClass::updateProtoUsage(Heap::Object *o)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: no member named 'updateProtoUsage' in
    namespace 'QV4::Heap'; did you mean simply 'updateProtoUsage'?.
    """
    raise NotImplementedError(
        "'QV4.Heap.InternalClass.updateProtoUsage' has no cute function "
        "yet. Qt's 'void "
        "QV4::Heap::InternalClass::updateProtoUsage(Heap::Object *o)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no member named 'updateProtoUsage' in "
        "namespace 'QV4::Heap'; did you mean simply 'updateProtoUsage'?.")
