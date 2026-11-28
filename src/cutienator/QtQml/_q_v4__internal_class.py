"""
QV4::InternalClass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4managed_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::InternalClass to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class InternalClass(QV4.Managed):
  """
  The cute side of Qt's QV4::InternalClass: a plain Python object standing in
  front of one C++ QV4::InternalClass.

  It is built on the cute 'QV4::Managed', as Qt's QV4::InternalClass is built
  on Qt's QV4::Managed, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::InternalClass that has a ritual and that Python
  can call so far, 5 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'changePrototype'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Heap::InternalClass *QV4::InternalClass::changeVTable(const VTable
    *vt)': names 'QV4::VTable', which has no cute class yet.
  - Qt's 'void QV4::InternalClass::operator=(Heap::InternalClass *ic)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 4 leans on 'QV4; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::InternalClass is created at the first use, not by
    'QV4::InternalClass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::InternalClass.
  - Each name of Qt's QV4::InternalClass that has no cute function yet,
    'addMember', 'changeMember', 'changeVTable', 'virtualDestroy', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    *QV4::InternalClass::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-internalclass.html#defaultInternalClass

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
    #      *QV4::InternalClass::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV413InternalClass20defaultInternalClassEPNS_10EngineBas'
        'eE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::InternalClass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'QV4::Heap::InternalClass *QV4::InternalClass::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-internalclass.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::InternalClass *QV4::InternalClass::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV413InternalClass11d_uncheckedEv',
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'QV4::Heap::InternalClass *QV4::InternalClass::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-internalclass.html#d

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::InternalClass *QV4::InternalClass::d() const
    address = self.uglySide.call('ritual_ZNK3QV413InternalClass1dEv')
    return QV4.Heap.InternalClass._cuteAt(address)

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
    Calls Qt's 'void QV4::InternalClass::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-internalclass.html#__dataTest
    """
    #  void QV4::InternalClass::__dataTest()
    self.uglySide.call('ritual_ZN3QV413InternalClass10__dataTestEv')

  @overload(WAIT['QV4.Heap.Object'])
  @overload(NoneType)
  def changePrototype(
      self,
      proto: Optional[QV4.Heap.Object],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::InternalClass::changePrototype(Heap::Object *proto)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-internalclass.html#changePrototype

    Parameters
    ----------

    proto : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass *QV4::InternalClass::changePrototype(Heap::Object
    #      *proto)
    address = self.uglySide.call(
        'ritual_ZN3QV413InternalClass15changePrototypeEPNS_4Heap6ObjectE',
        self._addressOf(proto),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  def addMember(*__, **_) -> Never:
    """
    Qt's 'Heap::InternalClass *QV4::InternalClass::addMember(PropertyKey
    identifier, PropertyAttributes data, InternalClassEntry *entry)': leans
    on 'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigned
    int, QV4::PropertyKey)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.InternalClass.addMember' has no cute function yet. Qt's "
        "'Heap::InternalClass *QV4::InternalClass::addMember(PropertyKey "
        "identifier, PropertyAttributes data, InternalClassEntry *entry)': "
        "leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigne"
        "d int, QV4::PropertyKey)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def changeMember(*__, **_) -> Never:
    """
    Qt's 'Heap::InternalClass *QV4::InternalClass::changeMember(PropertyKey
    identifier, PropertyAttributes data, InternalClassEntry *entry)': leans
    on 'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigned
    int, QV4::PropertyKey)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.InternalClass.changeMember' has no cute function yet. Qt's "
        "'Heap::InternalClass *QV4::InternalClass::changeMember(PropertyKey "
        "identifier, PropertyAttributes data, InternalClassEntry *entry)': "
        "leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyKey>::set(unsigne"
        "d int, QV4::PropertyKey)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def changeVTable(*__, **_) -> Never:
    """
    Qt's 'Heap::InternalClass *QV4::InternalClass::changeVTable(const VTable
    *vt)': names 'QV4::VTable', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.InternalClass.changeVTable' has no cute function yet. Qt's "
        "'Heap::InternalClass *QV4::InternalClass::changeVTable(const "
        "VTable *vt)': names 'QV4::VTable', which has no cute class yet.")

  @staticmethod
  def virtualDestroy(*__, **_) -> Never:
    """
    Qt's 'void QV4::InternalClass::virtualDestroy(QV4::Heap::Base *b)': leans
    on 'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::
    ~SharedInternalClassDataPrivate()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.InternalClass.virtualDestroy' has no cute function yet. Qt's "
        "'void QV4::InternalClass::virtualDestroy(QV4::Heap::Base *b)': "
        "leans on "
        "'QV4::SharedInternalClassDataPrivate<QV4::PropertyAttributes>::~Sha"
        "redInternalClassDataPrivate()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
