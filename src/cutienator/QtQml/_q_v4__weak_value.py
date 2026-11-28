"""
QV4::WeakValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::WeakValue to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class WeakValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::WeakValue: a plain Python object standing in
  front of one C++ QV4::WeakValue.

  C++ hands a QV4::WeakValue around as a copy, so every C++ QV4::WeakValue
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::WeakValue that has a ritual and that Python can
  call so far, 11 names in all: 'set', 'value', 'valueRef', 'asManaged',
  'engine', 'isUndefined', 'isNullOrUndefined', 'clear', 'markOnce',
  'allocVal', 'free'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'WeakValue &QV4::WeakValue::operator=(const WeakValue &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QV4::WeakValue::~WeakValue()': the destructor: Python removes its
    C++ QV4::WeakValue by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QV4::WeakValue is created at the first use, not by
    'QV4::WeakValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::WeakValue back gives a copy the ritual made for
    Python, in a new cute QV4::WeakValue.
  - Each name of Qt's QV4::WeakValue that has no cute function yet, 'as_',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::WeakValue'

  #  Qt's '~QV4::WeakValue()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::WeakValue behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV49WeakValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::WeakValue::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#value
    """
    #  ReturnedValue QV4::WeakValue::value() const
    return self.uglySide.call('ritual_ZNK3QV49WeakValue5valueEv')

  def valueRef(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::WeakValue::valueRef() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#valueRef

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::WeakValue::valueRef() const
    address = self.uglySide.call('ritual_ZNK3QV49WeakValue8valueRefEv')
    return QV4.Value._cuteAt(address)

  def asManaged(self) -> Optional[QV4.Managed]:
    """
    Calls Qt's 'Managed *QV4::WeakValue::asManaged() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#asManaged

    Returns
    -------

    Optional[QV4.Managed]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Managed *QV4::WeakValue::asManaged() const
    address = self.uglySide.call('ritual_ZNK3QV49WeakValue9asManagedEv')
    return QV4.Managed._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'ExecutionEngine *QV4::WeakValue::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionEngine *QV4::WeakValue::engine() const
    address = self.uglySide.call('ritual_ZNK3QV49WeakValue6engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::WeakValue::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#isUndefined
    """
    #  bool QV4::WeakValue::isUndefined() const
    return self.uglySide.call('ritual_ZNK3QV49WeakValue11isUndefinedEv')

  def isNullOrUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::WeakValue::isNullOrUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-weakvalue.html#isNullOrUndefined
    """
    #  bool QV4::WeakValue::isNullOrUndefined() const
    return self.uglySide.call(
        'ritual_ZNK3QV49WeakValue17isNullOrUndefinedEv',
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
    Notes what was given, for Qt's 'QV4::WeakValue::WeakValue()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#WeakValue
    """
    #  QV4::WeakValue::WeakValue()
    self._noteCreation(WeakValue, lambda: Rituals.call(
        'ritual_ZN3QV49WeakValueC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: WeakValue) -> None:
    """
    Notes what was given, for Qt's 'QV4::WeakValue::WeakValue(const WeakValue
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#WeakValue

    Parameters
    ----------

    other : WeakValue
      Passed on as a value: Qt reads the C++ QV4::WeakValue, which stays
      Python's own.
    """
    #  QV4::WeakValue::WeakValue(const WeakValue &other)
    self._noteCreation(WeakValue, lambda: Rituals.call(
        'ritual_ZN3QV49WeakValueC1ERKS0_', self._valueOf(other),
    ))

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      value: QV4.Value,
  ) -> None:
    """
    Notes what was given, for Qt's 'QV4::WeakValue::WeakValue(ExecutionEngine
    *engine, const Value &value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#WeakValue

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  QV4::WeakValue::WeakValue(ExecutionEngine *engine, const Value &value)
    self._noteCreation(WeakValue, lambda: Rituals.call(
        'ritual_ZN3QV49WeakValueC1EPNS_15ExecutionEngineERKNS_5ValueE',
        self._addressOf(engine), self._valueOf(value),
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
    Calls Qt's 'void QV4::WeakValue::set(ExecutionEngine *engine, const Value
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#set

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::WeakValue::set(ExecutionEngine *engine, const Value &value)
    self.uglySide.call(
        'ritual_ZN3QV49WeakValue3setEPNS_15ExecutionEngineERKNS_5ValueE',
        self._addressOf(engine), self._valueOf(value),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int)
  @overload(NoneType, int)
  def set(self, engine: Optional[QV4.ExecutionEngine], value: int) -> None:
    """
    Calls Qt's 'void QV4::WeakValue::set(ExecutionEngine *engine,
    ReturnedValue value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#set

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : int
      Passed on as it is.
    """
    #  void QV4::WeakValue::set(ExecutionEngine *engine, ReturnedValue value)
    self.uglySide.call(
        'ritual_ZN3QV49WeakValue3setEPNS_15ExecutionEngineEy',
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
    Calls Qt's 'void QV4::WeakValue::set(ExecutionEngine *engine, Heap::Base
    *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#set

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::WeakValue::set(ExecutionEngine *engine, Heap::Base *obj)
    self.uglySide.call(
        'ritual_ZN3QV49WeakValue3setEPNS_15ExecutionEngineEPNS_4Heap4BaseE',
        self._addressOf(engine), self._addressOf(obj),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QV4::WeakValue::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#clear
    """
    #  void QV4::WeakValue::clear()
    self.uglySide.call('ritual_ZN3QV49WeakValue5clearEv')

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def markOnce(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::WeakValue::markOnce(MarkStack *markStack)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#markOnce

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::WeakValue::markOnce(MarkStack *markStack)
    self.uglySide.call(
        'ritual_ZN3QV49WeakValue8markOnceEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def allocVal(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QV4::WeakValue::allocVal(ExecutionEngine *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#allocVal

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::WeakValue::allocVal(ExecutionEngine *engine)
    self.uglySide.call(
        'ritual_ZN3QV49WeakValue8allocValEPNS_15ExecutionEngineE',
        self._addressOf(engine),
    )

  def free(self) -> None:
    """
    Calls Qt's 'void QV4::WeakValue::free()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-weakvalue.html#free
    """
    #  void QV4::WeakValue::free()
    self.uglySide.call('ritual_ZN3QV49WeakValue4freeEv')

  @staticmethod
  def as_(*__, **_) -> Never:
    """
    Qt's 'QV4::WeakValue::as': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.WeakValue.as_' has no cute function yet. Qt's "
        "'QV4::WeakValue::as': a template: a pattern and no single function."
    )
