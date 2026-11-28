"""
QV4::PersistentValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::PersistentValue to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PersistentValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::PersistentValue: a plain Python object standing
  in front of one C++ QV4::PersistentValue.

  C++ hands a QV4::PersistentValue around as a copy, so every C++
  QV4::PersistentValue behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::PersistentValue that has a ritual and that
  Python can call so far, 9 names in all: 'set', 'value', 'valueRef',
  'asManaged', 'engine', 'isUndefined', 'isNullOrUndefined', 'clear',
  'isEmpty'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'PersistentValue &QV4::PersistentValue::operator=(const
    PersistentValue &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QV4::PersistentValue::PersistentValue(PersistentValue &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QV4::PersistentValue::swap(PersistentValue &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'PersistentValue &QV4::PersistentValue::operator=(PersistentValue
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QV4::PersistentValue::~PersistentValue()': the destructor: Python
    removes its C++ QV4::PersistentValue by it, and has no other use for it.
  - Qt's 'PersistentValue &QV4::PersistentValue::operator=(const WeakValue
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'PersistentValue &QV4::PersistentValue::operator=(Object *object)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  1 of the 24 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QV4::PersistentValue is created at the first use, not by
    'QV4::PersistentValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::PersistentValue back gives a copy the ritual
    made for Python, in a new cute QV4::PersistentValue.
  - Each name of Qt's QV4::PersistentValue that has no cute function yet,
    'as_', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::PersistentValue'

  #  Qt's '~QV4::PersistentValue()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::PersistentValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV415PersistentValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::PersistentValue::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#value
    """
    #  ReturnedValue QV4::PersistentValue::value() const
    return self.uglySide.call('ritual_ZNK3QV415PersistentValue5valueEv')

  def valueRef(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::PersistentValue::valueRef() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#valueRef

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::PersistentValue::valueRef() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415PersistentValue8valueRefEv',
    )
    return QV4.Value._cuteAt(address)

  def asManaged(self) -> Optional[QV4.Managed]:
    """
    Calls Qt's 'Managed *QV4::PersistentValue::asManaged() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#asManaged

    Returns
    -------

    Optional[QV4.Managed]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Managed *QV4::PersistentValue::asManaged() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415PersistentValue9asManagedEv',
    )
    return QV4.Managed._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'ExecutionEngine *QV4::PersistentValue::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionEngine *QV4::PersistentValue::engine() const
    address = self.uglySide.call('ritual_ZNK3QV415PersistentValue6engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::PersistentValue::isUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvalue.html#isUndefined
    """
    #  bool QV4::PersistentValue::isUndefined() const
    return self.uglySide.call(
        'ritual_ZNK3QV415PersistentValue11isUndefinedEv',
    )

  def isNullOrUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::PersistentValue::isNullOrUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvalue.html#isNullOrUndefined
    """
    #  bool QV4::PersistentValue::isNullOrUndefined() const
    return self.uglySide.call(
        'ritual_ZNK3QV415PersistentValue17isNullOrUndefinedEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::PersistentValue::PersistentValue()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvalue.html#PersistentValue
    """
    #  QV4::PersistentValue::PersistentValue()
    self._noteCreation(PersistentValue, lambda: Rituals.call(
        'ritual_ZN3QV415PersistentValueC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: PersistentValue) -> None:
    """
    Notes what was given, for Qt's
    'QV4::PersistentValue::PersistentValue(const PersistentValue &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvalue.html#PersistentValue

    Parameters
    ----------

    other : PersistentValue
      Passed on as a value: Qt reads the C++ QV4::PersistentValue, which
      stays Python's own.
    """
    #  QV4::PersistentValue::PersistentValue(const PersistentValue &other)
    self._noteCreation(PersistentValue, lambda: Rituals.call(
        'ritual_ZN3QV415PersistentValueC1ERKS0_', self._valueOf(other),
    ))

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      value: QV4.Value,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::PersistentValue::PersistentValue(ExecutionEngine *engine, const
    Value &value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvalue.html#PersistentValue

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  QV4::PersistentValue::PersistentValue(ExecutionEngine *engine, const
    #      Value &value)
    self._noteCreation(PersistentValue, lambda: Rituals.call(
        'ritual_ZN3QV415PersistentValueC1EPNS_15ExecutionEngineERKNS_5Value'
        'E',
        self._addressOf(engine), self._valueOf(value),
    ))

  @overload(WAIT['QV4.ExecutionEngine'], int)
  @overload(NoneType, int)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      value: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::PersistentValue::PersistentValue(ExecutionEngine *engine,
    ReturnedValue value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvalue.html#PersistentValue

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : int
      Passed on as it is.
    """
    #  QV4::PersistentValue::PersistentValue(ExecutionEngine *engine,
    #      ReturnedValue value)
    self._noteCreation(PersistentValue, lambda: Rituals.call(
        'ritual_ZN3QV415PersistentValueC1EPNS_15ExecutionEngineEy',
        self._addressOf(engine), value,
    ))

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Object'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.Object'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QV4.Object],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::PersistentValue::PersistentValue(ExecutionEngine *engine, Object
    *object)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvalue.html#PersistentValue

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::PersistentValue::PersistentValue(ExecutionEngine *engine, Object
    #      *object)
    self._noteCreation(PersistentValue, lambda: Rituals.call(
        'ritual_ZN3QV415PersistentValueC1EPNS_15ExecutionEngineEPNS_6Object'
        'E',
        self._addressOf(engine), self._addressOf(object),
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

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def set(
      self,
      engine: Optional[QV4.ExecutionEngine],
      value: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::PersistentValue::set(ExecutionEngine *engine, const
    Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#set

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::PersistentValue::set(ExecutionEngine *engine, const Value
    #      &value)
    self.uglySide.call(
        'ritual_ZN3QV415PersistentValue3setEPNS_15ExecutionEngineERKNS_5Val'
        'ueE',
        self._addressOf(engine), self._valueOf(value),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int)
  @overload(NoneType, int)
  def set(self, engine: Optional[QV4.ExecutionEngine], value: int) -> None:
    """
    Calls Qt's 'void QV4::PersistentValue::set(ExecutionEngine *engine,
    ReturnedValue value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#set

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : int
      Passed on as it is.
    """
    #  void QV4::PersistentValue::set(ExecutionEngine *engine, ReturnedValue
    #      value)
    self.uglySide.call(
        'ritual_ZN3QV415PersistentValue3setEPNS_15ExecutionEngineEy',
        self._addressOf(engine), value,
    )

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.Base'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.Heap.Base'])
  @overload(NoneType, NoneType)
  def set(
      self,
      engine: Optional[QV4.ExecutionEngine],
      obj: Optional[QV4.Heap.Base],
  ) -> None:
    """
    Calls Qt's 'void QV4::PersistentValue::set(ExecutionEngine *engine,
    Heap::Base *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#set

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::PersistentValue::set(ExecutionEngine *engine, Heap::Base
    #      *obj)
    self.uglySide.call(
        'ritual_ZN3QV415PersistentValue3setEPNS_15ExecutionEngineEPNS_4Heap'
        '4BaseE',
        self._addressOf(engine), self._addressOf(obj),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QV4::PersistentValue::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#clear
    """
    #  void QV4::PersistentValue::clear()
    self.uglySide.call('ritual_ZN3QV415PersistentValue5clearEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QV4::PersistentValue::isEmpty()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-persistentvalue.html#isEmpty
    """
    #  bool QV4::PersistentValue::isEmpty()
    return self.uglySide.call('ritual_ZN3QV415PersistentValue7isEmptyEv')

  @staticmethod
  def as_(*__, **_) -> Never:
    """
    Qt's 'QV4::PersistentValue::as': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.PersistentValue.as_' has no cute function yet. Qt's "
        "'QV4::PersistentValue::as': a template: a pattern and no single "
        "function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QV4::PersistentValue::swap(PersistentValue &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.PersistentValue.swap' has no cute function yet. Qt's 'void "
        "QV4::PersistentValue::swap(PersistentValue &other)': takes a type "
        "Python has no way to hand over yet.")
