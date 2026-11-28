"""
QV4::FunctionObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::FunctionObject to be private: it declares the class in a
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


class FunctionObject(QV4.Object):
  """
  The cute side of Qt's QV4::FunctionObject: a plain Python object standing
  in front of one C++ QV4::FunctionObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::FunctionObject is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::FunctionObject that has a ritual and that
  Python can call so far, 20 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'defaultPrototype', 'canBeTailCalled', 'name',
  'setName', 'createDefaultPrototypeProperty', 'callAsConstructor', 'call',
  'failCall', 'failCallAsConstructor', 'createScriptFunction',
  'createConstructorFunction', 'createMemberFunction', 'isConstructor',
  'getHomeObject', 'protoProperty', 'hasHasInstanceProperty'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::FunctionObject::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'void QV4::FunctionObject::call(QObject *thisObject, void **argv,
    const QMetaType *types, int argc) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QV4::FunctionObject::virtualConvertAndCall(const
    FunctionObject *f, QObject *thisObject, void **argv, const QMetaType
    *types, int argc)': takes a type Python has no way to hand over yet.
  - Qt's 'Heap::FunctionObject
    *QV4::FunctionObject::createBuiltinFunction(ExecutionEngine *engine,
    StringOrSymbol *nameOrSymbol, VTable::Call code, int argumentCount)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 32 functions Qt declares: 3 forbidden; 2 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::FunctionObject is created at the first use, not by
    'QV4::FunctionObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::FunctionObject.
  - Each name of Qt's QV4::FunctionObject that has no cute function yet,
    'createBuiltinFunction', 'isBinding', 'isBoundFunction',
    'virtualConvertAndCall', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    *QV4::FunctionObject::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#defaultInternalClass

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
    #      *QV4::FunctionObject::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV414FunctionObject20defaultInternalClassEPNS_10EngineBa'
        'seE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::FunctionObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#defaultPrototype

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
    #  QV4::Object
    #      *QV4::FunctionObject::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV414FunctionObject16defaultPrototypeEPNS_15ExecutionEng'
        'ineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'])
  @overload(WAIT['QV4.ExecutionContext'], NoneType)
  @overload(NoneType, WAIT['QV4.Function'])
  @overload(NoneType, NoneType)
  def createScriptFunction(
      scope: Optional[QV4.ExecutionContext],
      function: Optional[QV4.Function],
  ) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'Heap::FunctionObject
    *QV4::FunctionObject::createScriptFunction(ExecutionContext *scope,
    Function *function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#createScriptFunction

    Parameters
    ----------

    scope : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::FunctionObject
    #      *QV4::FunctionObject::createScriptFunction(ExecutionContext
    #      *scope, Function *function)
    address = Rituals.call(
        'ritual_ZN3QV414FunctionObject20createScriptFunctionEPNS_16Executio'
        'nContextEPNS_8FunctionE',
        CuteMixin._addressOf(scope), CuteMixin._addressOf(function),
    )
    return QV4.Heap.FunctionObject._cuteAt(address)

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], QV4.Object, bool,
  )
  @overload(
      WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], NoneType, bool,
  )
  @overload(WAIT['QV4.ExecutionContext'], NoneType, QV4.Object, bool)
  @overload(WAIT['QV4.ExecutionContext'], NoneType, NoneType, bool)
  @overload(NoneType, WAIT['QV4.Function'], QV4.Object, bool)
  @overload(NoneType, WAIT['QV4.Function'], NoneType, bool)
  @overload(NoneType, NoneType, QV4.Object, bool)
  @overload(NoneType, NoneType, NoneType, bool)
  def createConstructorFunction(
      scope: Optional[QV4.ExecutionContext],
      function: Optional[QV4.Function],
      homeObject: Optional[QV4.Object],
      isDerivedConstructor: bool,
  ) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'Heap::FunctionObject
    *QV4::FunctionObject::createConstructorFunction(ExecutionContext *scope,
    Function *function, Object *homeObject, bool isDerivedConstructor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#createConstructorFunction

    Parameters
    ----------

    scope : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    homeObject : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isDerivedConstructor : bool
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::FunctionObject
    #      *QV4::FunctionObject::createConstructorFunction(ExecutionContext
    #      *scope, Function *function, Object *homeObject, bool
    #      isDerivedConstructor)
    address = Rituals.call(
        'ritual_ZN3QV414FunctionObject25createConstructorFunctionEPNS_16Exe'
        'cutionContextEPNS_8FunctionEPNS_6ObjectEb',
        CuteMixin._addressOf(scope), CuteMixin._addressOf(function),
        CuteMixin._addressOf(homeObject), isDerivedConstructor,
    )
    return QV4.Heap.FunctionObject._cuteAt(address)

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], QV4.Object,
      WAIT['QV4.String'],
  )
  @overload(
      WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], QV4.Object,
      NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], NoneType,
      WAIT['QV4.String'],
  )
  @overload(
      WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], NoneType, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionContext'], NoneType, QV4.Object, WAIT['QV4.String'],
  )
  @overload(WAIT['QV4.ExecutionContext'], NoneType, QV4.Object, NoneType)
  @overload(
      WAIT['QV4.ExecutionContext'], NoneType, NoneType, WAIT['QV4.String'],
  )
  @overload(WAIT['QV4.ExecutionContext'], NoneType, NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.Function'], QV4.Object, WAIT['QV4.String'])
  @overload(NoneType, WAIT['QV4.Function'], QV4.Object, NoneType)
  @overload(NoneType, WAIT['QV4.Function'], NoneType, WAIT['QV4.String'])
  @overload(NoneType, WAIT['QV4.Function'], NoneType, NoneType)
  @overload(NoneType, NoneType, QV4.Object, WAIT['QV4.String'])
  @overload(NoneType, NoneType, QV4.Object, NoneType)
  @overload(NoneType, NoneType, NoneType, WAIT['QV4.String'])
  @overload(NoneType, NoneType, NoneType, NoneType)
  def createMemberFunction(
      scope: Optional[QV4.ExecutionContext],
      function: Optional[QV4.Function],
      homeObject: Optional[QV4.Object],
      name: Optional[QV4.String],
  ) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'Heap::FunctionObject
    *QV4::FunctionObject::createMemberFunction(ExecutionContext *scope,
    Function *function, Object *homeObject, String *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#createMemberFunction

    Parameters
    ----------

    scope : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    homeObject : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::FunctionObject
    #      *QV4::FunctionObject::createMemberFunction(ExecutionContext
    #      *scope, Function *function, Object *homeObject, String *name)
    address = Rituals.call(
        'ritual_ZN3QV414FunctionObject20createMemberFunctionEPNS_16Executio'
        'nContextEPNS_8FunctionEPNS_6ObjectEPNS_6StringE',
        CuteMixin._addressOf(scope), CuteMixin._addressOf(function),
        CuteMixin._addressOf(homeObject), CuteMixin._addressOf(name),
    )
    return QV4.Heap.FunctionObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::FunctionObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'QV4::Heap::FunctionObject *QV4::FunctionObject::d_unchecked()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::FunctionObject *QV4::FunctionObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject11d_uncheckedEv',
    )
    return QV4.Heap.FunctionObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'QV4::Heap::FunctionObject *QV4::FunctionObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionobject.html#d

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::FunctionObject *QV4::FunctionObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV414FunctionObject1dEv')
    return QV4.Heap.FunctionObject._cuteAt(address)

  def canBeTailCalled(self) -> bool:
    """
    Calls Qt's 'bool QV4::FunctionObject::canBeTailCalled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#canBeTailCalled
    """
    #  bool QV4::FunctionObject::canBeTailCalled() const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject15canBeTailCalledEv',
    )

  def name(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionobject.html#name
    """
    #  ReturnedValue QV4::FunctionObject::name() const
    return self.uglySide.call('ritual_ZNK3QV414FunctionObject4nameEv')

  @overload(QV4.Value, int)
  @overload(NoneType, int)
  @overload(QV4.Value, int, QV4.Value)
  @overload(QV4.Value, int, NoneType)
  @overload(NoneType, int, QV4.Value)
  @overload(NoneType, int, NoneType)
  def callAsConstructor(
      self,
      argv: Optional[QV4.Value],
      argc: int,
      newTarget: Optional[QV4.Value] = None,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::callAsConstructor(const
    Value *argv, int argc, const Value *newTarget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#callAsConstructor

    Parameters
    ----------

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    newTarget : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ReturnedValue QV4::FunctionObject::callAsConstructor(const Value
    #      *argv, int argc, const Value *newTarget) const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject17callAsConstructorEPKNS_5ValueEiS3_',
        self._addressOf(argv), argc, self._addressOf(newTarget),
    )

  @overload(WAIT['QV4.JSCallData'])
  def callAsConstructor(self, data: QV4.JSCallData) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::callAsConstructor(const
    JSCallData &data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#callAsConstructor

    Parameters
    ----------

    data : QV4.JSCallData
      Passed on as a value: Qt reads the C++ QV4::JSCallData, which stays
      Python's own.
    """
    #  ReturnedValue QV4::FunctionObject::callAsConstructor(const JSCallData
    #      &data) const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject17callAsConstructorERKNS_10JSCallDat'
        'aE',
        self._valueOf(data),
    )

  @overload(QV4.Value, QV4.Value, int)
  @overload(QV4.Value, NoneType, int)
  @overload(NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, int)
  def call(
      self,
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::call(const Value
    *thisObject, const Value *argv, int argc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionobject.html#call

    Parameters
    ----------

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::FunctionObject::call(const Value *thisObject, const
    #      Value *argv, int argc) const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject4callEPKNS_5ValueES3_i',
        self._addressOf(thisObject), self._addressOf(argv), argc,
    )

  @overload(WAIT['QV4.JSCallData'])
  def call(self, data: QV4.JSCallData) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::call(const JSCallData
    &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionobject.html#call

    Parameters
    ----------

    data : QV4.JSCallData
      Passed on as a value: Qt reads the C++ QV4::JSCallData, which stays
      Python's own.
    """
    #  ReturnedValue QV4::FunctionObject::call(const JSCallData &data) const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject4callERKNS_10JSCallDataE',
        self._valueOf(data),
    )

  def failCall(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::failCall() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionobject.html#failCall
    """
    #  ReturnedValue QV4::FunctionObject::failCall() const
    return self.uglySide.call('ritual_ZNK3QV414FunctionObject8failCallEv')

  def failCallAsConstructor(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::failCallAsConstructor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#failCallAsConstructor
    """
    #  ReturnedValue QV4::FunctionObject::failCallAsConstructor() const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject21failCallAsConstructorEv',
    )

  def isConstructor(self) -> bool:
    """
    Calls Qt's 'bool QV4::FunctionObject::isConstructor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#isConstructor
    """
    #  bool QV4::FunctionObject::isConstructor() const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject13isConstructorEv',
    )

  def getHomeObject(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::getHomeObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#getHomeObject
    """
    #  ReturnedValue QV4::FunctionObject::getHomeObject() const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject13getHomeObjectEv',
    )

  def protoProperty(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionObject::protoProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#protoProperty
    """
    #  ReturnedValue QV4::FunctionObject::protoProperty() const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject13protoPropertyEv',
    )

  def hasHasInstanceProperty(self) -> bool:
    """
    Calls Qt's 'bool QV4::FunctionObject::hasHasInstanceProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html#hasHasInstanceProperty
    """
    #  bool QV4::FunctionObject::hasHasInstanceProperty() const
    return self.uglySide.call(
        'ritual_ZNK3QV414FunctionObject22hasHasInstancePropertyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def setName(self, name: Optional[QV4.String]) -> None:
    """
    Calls Qt's 'void QV4::FunctionObject::setName(String *name)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionobject.html#setName

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::FunctionObject::setName(String *name)
    self.uglySide.call(
        'ritual_ZN3QV414FunctionObject7setNameEPNS_6StringE',
        self._addressOf(name),
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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::FunctionObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionobject.html#__dataTest
    """
    #  void QV4::FunctionObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV414FunctionObject10__dataTestEv')

  @overload(int)
  def createDefaultPrototypeProperty(
      self,
      protoConstructorSlot: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::FunctionObject::createDefaultPrototypeProperty(uint
    protoConstructorSlot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionobject.html

    Parameters
    ----------

    protoConstructorSlot : int
      Passed on as it is.
    """
    #  void QV4::FunctionObject::createDefaultPrototypeProperty(uint
    #      protoConstructorSlot)
    self.uglySide.call(
        'ritual_ZN3QV414FunctionObject30createDefaultPrototypePropertyEj',
        protoConstructorSlot,
    )

  @staticmethod
  def createBuiltinFunction(*__, **_) -> Never:
    """
    Qt's 'Heap::FunctionObject
    *QV4::FunctionObject::createBuiltinFunction(ExecutionEngine *engine,
    StringOrSymbol *nameOrSymbol, VTable::Call code, int argumentCount)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.FunctionObject.createBuiltinFunction' has no cute function "
        "yet. Qt's 'Heap::FunctionObject "
        "*QV4::FunctionObject::createBuiltinFunction(ExecutionEngine "
        "*engine, StringOrSymbol *nameOrSymbol, VTable::Call code, int "
        "argumentCount)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isBinding(*__, **_) -> Never:
    """
    Qt's 'bool QV4::FunctionObject::isBinding() const': leans on
    'QV4::QQmlBindingFunction::static_vtbl', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.FunctionObject.isBinding' has no cute function yet. Qt's "
        "'bool QV4::FunctionObject::isBinding() const': leans on "
        "'QV4::QQmlBindingFunction::static_vtbl', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def isBoundFunction(*__, **_) -> Never:
    """
    Qt's 'bool QV4::FunctionObject::isBoundFunction() const': leans on
    'QV4::BoundFunction::static_vtbl', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.FunctionObject.isBoundFunction' has no cute function yet. "
        "Qt's 'bool QV4::FunctionObject::isBoundFunction() const': leans on "
        "'QV4::BoundFunction::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def virtualConvertAndCall(*__, **_) -> Never:
    """
    Qt's 'void QV4::FunctionObject::virtualConvertAndCall(const
    FunctionObject *f, QObject *thisObject, void **argv, const QMetaType
    *types, int argc)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.FunctionObject.virtualConvertAndCall' has no cute function "
        "yet. Qt's 'void QV4::FunctionObject::virtualConvertAndCall(const "
        "FunctionObject *f, QObject *thisObject, void **argv, const "
        "QMetaType *types, int argc)': takes a type Python has no way to "
        "hand over yet.")
