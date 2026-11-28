"""
QV4::Sequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Sequence to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Sequence(QV4.ReferenceObject):
  """
  The cute side of Qt's QV4::Sequence: a plain Python object standing in
  front of one C++ QV4::Sequence.

  It is built on the cute 'QV4::ReferenceObject', as Qt's QV4::Sequence is
  built on Qt's QV4::ReferenceObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Sequence that has a ritual and that Python can
  call so far, 9 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'virtualDestroy', 'virtualGetLength', 'virtualPut',
  'virtualDeleteProperty', 'virtualIsEqualTo'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::Sequence::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'QV4::ReturnedValue QV4::Sequence::virtualGet(const QV4::Managed
    *that, PropertyKey id, const Value *receiver, bool *hasProperty)': takes
    a number to change where it is.
  - Qt's 'QV4::OwnPropertyKeyIterator
    *QV4::Sequence::virtualOwnPropertyKeys(const Object *m, Value *target)':
    gives 'QV4::OwnPropertyKeyIterator', which has no cute class yet.
  - Qt's 'int QV4::Sequence::virtualMetacall(Object *object,
    QMetaObject::Call call, int index, void **a)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::Sequence is created at the first use, not by
    'QV4::Sequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Sequence.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::Sequence::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object *QV4::Sequence::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV48Sequence16defaultPrototypeEPNS_15ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::Sequence::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Sequence::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV48Sequence14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetLength(m: Optional[QV4.Managed]) -> int:
    """
    Calls Qt's 'qint64 QV4::Sequence::virtualGetLength(const Managed *m)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#virtualGetLength

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QV4::Sequence::virtualGetLength(const Managed *m)
    return Rituals.call(
        'ritual_ZN3QV48Sequence16virtualGetLengthEPKNS_7ManagedE',
        CuteMixin._addressOf(m),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def virtualPut(
      that: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      value: QV4.Value,
      receiver: Optional[QV4.Value],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Sequence::virtualPut(Managed *that, PropertyKey id,
    const QV4::Value &value, Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#virtualPut

    Parameters
    ----------

    that : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    receiver : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Sequence::virtualPut(Managed *that, PropertyKey id, const
    #      QV4::Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV48Sequence10virtualPutEPNS_7ManagedENS_11PropertyKeyER'
        'KNS_5ValueEPS4_',
        CuteMixin._addressOf(that), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualDeleteProperty(
      that: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Sequence::virtualDeleteProperty(QV4::Managed *that,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequence.html#virtualDeleteProperty

    Parameters
    ----------

    that : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Sequence::virtualDeleteProperty(QV4::Managed *that,
    #      PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV48Sequence21virtualDeletePropertyEPNS_7ManagedENS_11Pr'
        'opertyKeyE',
        CuteMixin._addressOf(that), CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload(QV4.Managed, QV4.Managed)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Managed)
  @overload(NoneType, NoneType)
  def virtualIsEqualTo(
      that: Optional[QV4.Managed],
      other: Optional[QV4.Managed],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Sequence::virtualIsEqualTo(Managed *that, Managed
    *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#virtualIsEqualTo

    Parameters
    ----------

    that : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    other : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Sequence::virtualIsEqualTo(Managed *that, Managed *other)
    return Rituals.call(
        'ritual_ZN3QV48Sequence16virtualIsEqualToEPNS_7ManagedES2_',
        CuteMixin._addressOf(that), CuteMixin._addressOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Sequence'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.Sequence]:
    """
    Calls Qt's 'QV4::Heap::Sequence *QV4::Sequence::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.Sequence]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Sequence *QV4::Sequence::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV48Sequence11d_uncheckedEv')
    return QV4.Heap.Sequence._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.Sequence]:
    """
    Calls Qt's 'QV4::Heap::Sequence *QV4::Sequence::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#d

    Returns
    -------

    Optional[QV4.Heap.Sequence]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Sequence *QV4::Sequence::d() const
    address = self.uglySide.call('ritual_ZNK3QV48Sequence1dEv')
    return QV4.Heap.Sequence._cuteAt(address)

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
    Calls Qt's 'void QV4::Sequence::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequence.html#__dataTest
    """
    #  void QV4::Sequence::__dataTest()
    self.uglySide.call('ritual_ZN3QV48Sequence10__dataTestEv')
