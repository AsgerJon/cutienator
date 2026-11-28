"""
QV4::QObjectMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::QObjectMethod to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlObjectOrGadget, QQmlPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlObjectOrGadget = WAIT['QQmlObjectOrGadget']
  QQmlPropertyData = WAIT['QQmlPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectMethod(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::QObjectMethod: a plain Python object standing in
  front of one C++ QV4::QObjectMethod.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::QObjectMethod
  is built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QObjectMethod that has a ritual and that Python
  can call so far, 13 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'create', 'methodIndex', 'object', 'method_toString',
  'method_destroy', 'virtualCall', 'callInternal', 'resolveOverloaded',
  'callPrecise'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QObjectMethod::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'void QV4::QObjectMethod::virtualCallWithMetaTypes(const
    FunctionObject *m, QObject *thisObject, void **argv, const QMetaType
    *types, int argc)': takes a type Python has no way to hand over yet.
  - Qt's 'void QV4::QObjectMethod::callInternalWithMetaTypes(QObject
    *thisObject, void **argv, const QMetaType *types, int argc) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'std::pair<QObject *, int> QV4::QObjectMethod::extractQtMethod(const
    QV4::FunctionObject *function)': gives a type Python has no way to take
    yet.
  - Qt's 'bool QV4::QObjectMethod::isExactMatch(const QMetaMethod &method,
    void **argv, int argc, const QMetaType *types)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QQmlPropertyData *QV4::QObjectMethod::resolveOverloaded(const
    QQmlPropertyData *methods, int methodCount, void **argv, int argc, const
    QMetaType *types)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::QObjectMethod is created at the first use, not by
    'QV4::QObjectMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QObjectMethod.
  - Each name of Qt's QV4::QObjectMethod that has no cute function yet,
    'callInternalWithMetaTypes', 'extractQtMethod', 'isExactMatch',
    'virtualCallWithMetaTypes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::QObjectMethod::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectmethod.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QObjectMethod::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV413QObjectMethod14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.Object'], int)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
  @overload(NoneType, WAIT['QV4.Heap.Object'], int)
  @overload(NoneType, NoneType, int)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      wrapper: Optional[QV4.Heap.Object],
      index: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectMethod::create(ExecutionEngine
    *engine, Heap::Object *wrapper, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wrapper : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::QObjectMethod::create(ExecutionEngine *engine,
    #      Heap::Object *wrapper, int index)
    return Rituals.call(
        'ritual_ZN3QV413QObjectMethod6createEPNS_15ExecutionEngineEPNS_4Hea'
        'p6ObjectEi',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(wrapper), index,
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QQmlValueTypeWrapper'],
      int,
  )
  @overload(NoneType, WAIT['QV4.Heap.QQmlValueTypeWrapper'], int)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      valueType: Optional[QV4.Heap.QQmlValueTypeWrapper],
      index: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectMethod::create(ExecutionEngine
    *engine, Heap::QQmlValueTypeWrapper *valueType, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    valueType : Optional[QV4.Heap.QQmlValueTypeWrapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::QObjectMethod::create(ExecutionEngine *engine,
    #      Heap::QQmlValueTypeWrapper *valueType, int index)
    return Rituals.call(
        'ritual_ZN3QV413QObjectMethod6createEPNS_15ExecutionEngineEPNS_4Hea'
        'p20QQmlValueTypeWrapperEi',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(valueType), index,
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QObjectMethod'],
      WAIT['QV4.Heap.Object'], WAIT['QV4.Heap.Object'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QObjectMethod'],
      WAIT['QV4.Heap.Object'], NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QObjectMethod'], NoneType,
      WAIT['QV4.Heap.Object'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QObjectMethod'], NoneType,
      NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Heap.Object'],
      WAIT['QV4.Heap.Object'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Heap.Object'],
      NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, NoneType,
      WAIT['QV4.Heap.Object'],
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType, NoneType)
  @overload(
      NoneType, WAIT['QV4.Heap.QObjectMethod'], WAIT['QV4.Heap.Object'],
      WAIT['QV4.Heap.Object'],
  )
  @overload(
      NoneType, WAIT['QV4.Heap.QObjectMethod'], WAIT['QV4.Heap.Object'],
      NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.Heap.QObjectMethod'], NoneType,
      WAIT['QV4.Heap.Object'],
  )
  @overload(NoneType, WAIT['QV4.Heap.QObjectMethod'], NoneType, NoneType)
  @overload(
      NoneType, NoneType, WAIT['QV4.Heap.Object'], WAIT['QV4.Heap.Object'],
  )
  @overload(NoneType, NoneType, WAIT['QV4.Heap.Object'], NoneType)
  @overload(NoneType, NoneType, NoneType, WAIT['QV4.Heap.Object'])
  @overload(NoneType, NoneType, NoneType, NoneType)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      cloneFrom: Optional[QV4.Heap.QObjectMethod],
      wrapper: Optional[QV4.Heap.Object],
      object: Optional[QV4.Heap.Object],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectMethod::create(ExecutionEngine
    *engine, Heap::QObjectMethod *cloneFrom, Heap::Object *wrapper,
    Heap::Object *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cloneFrom : Optional[QV4.Heap.QObjectMethod]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wrapper : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QObjectMethod::create(ExecutionEngine *engine,
    #      Heap::QObjectMethod *cloneFrom, Heap::Object *wrapper,
    #      Heap::Object *object)
    return Rituals.call(
        'ritual_ZN3QV413QObjectMethod6createEPNS_15ExecutionEngineEPNS_4Hea'
        'p13QObjectMethodEPNS3_6ObjectES7_',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(cloneFrom),
        CuteMixin._addressOf(wrapper), CuteMixin._addressOf(object),
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def virtualCall(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectMethod::virtualCall(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#virtualCall

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::QObjectMethod::virtualCall(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413QObjectMethod11virtualCallEPKNS_14FunctionObjectEPK'
        'NS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, int, WAIT['QV4.ExecutionEngine'],
      WAIT['QV4.CallData'],
  )
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, int, WAIT['QV4.ExecutionEngine'],
      NoneType,
  )
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, int, NoneType,
      WAIT['QV4.CallData'],
  )
  @overload(QQmlObjectOrGadget, QQmlPropertyData, int, NoneType, NoneType)
  @overload(
      QQmlObjectOrGadget, NoneType, int, WAIT['QV4.ExecutionEngine'],
      WAIT['QV4.CallData'],
  )
  @overload(
      QQmlObjectOrGadget, NoneType, int, WAIT['QV4.ExecutionEngine'],
      NoneType,
  )
  @overload(
      QQmlObjectOrGadget, NoneType, int, NoneType, WAIT['QV4.CallData'],
  )
  @overload(QQmlObjectOrGadget, NoneType, int, NoneType, NoneType)
  def resolveOverloaded(
      object: QQmlObjectOrGadget,
      methods: Optional[QQmlPropertyData],
      methodCount: int,
      engine: Optional[QV4.ExecutionEngine],
      callArgs: Optional[QV4.CallData],
  ) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData
    *QV4::QObjectMethod::resolveOverloaded(const QQmlObjectOrGadget &object,
    const QQmlPropertyData *methods, int methodCount, ExecutionEngine
    *engine, CallData *callArgs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectmethod.html#resolveOverloaded

    Parameters
    ----------

    object : QQmlObjectOrGadget
      Passed on as a value: Qt reads the C++ QQmlObjectOrGadget, which stays
      Python's own.

    methods : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    methodCount : int
      Passed on as it is.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    callArgs : Optional[QV4.CallData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QV4::QObjectMethod::resolveOverloaded(const
    #      QQmlObjectOrGadget &object, const QQmlPropertyData *methods, int
    #      methodCount, ExecutionEngine *engine, CallData *callArgs)
    address = Rituals.call(
        'ritual_ZN3QV413QObjectMethod17resolveOverloadedERK18QQmlObjectOrGa'
        'dgetPK16QQmlPropertyDataiPNS_15ExecutionEngineEPNS_8CallDataE',
        CuteMixin._valueOf(object), CuteMixin._addressOf(methods),
        methodCount, CuteMixin._addressOf(engine),
        CuteMixin._addressOf(callArgs),
    )
    from . import QQmlPropertyData
    return QQmlPropertyData._cuteAt(address)

  @staticmethod
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, WAIT['QV4.ExecutionEngine'],
      WAIT['QV4.CallData'],
  )
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, WAIT['QV4.ExecutionEngine'],
      NoneType,
  )
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, NoneType, WAIT['QV4.CallData'],
  )
  @overload(QQmlObjectOrGadget, QQmlPropertyData, NoneType, NoneType)
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, WAIT['QV4.ExecutionEngine'],
      WAIT['QV4.CallData'], QMetaObject.Call,
  )
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, WAIT['QV4.ExecutionEngine'],
      NoneType, QMetaObject.Call,
  )
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, NoneType, WAIT['QV4.CallData'],
      QMetaObject.Call,
  )
  @overload(
      QQmlObjectOrGadget, QQmlPropertyData, NoneType, NoneType,
      QMetaObject.Call,
  )
  def callPrecise(
      object: QQmlObjectOrGadget,
      data: QQmlPropertyData,
      engine: Optional[QV4.ExecutionEngine],
      callArgs: Optional[QV4.CallData],
      callType: QMetaObject.Call = QMetaObject.Call.InvokeMetaMethod,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectMethod::callPrecise(const
    QQmlObjectOrGadget &object, const QQmlPropertyData &data, ExecutionEngine
    *engine, CallData *callArgs, QMetaObject::Call callType)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#callPrecise

    Parameters
    ----------

    object : QQmlObjectOrGadget
      Passed on as a value: Qt reads the C++ QQmlObjectOrGadget, which stays
      Python's own.

    data : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    callArgs : Optional[QV4.CallData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    callType : QMetaObject.Call
      Passed on as its number. May be left out, as in Qt: it is then
      QMetaObject.Call.InvokeMetaMethod.
    """
    #  ReturnedValue QV4::QObjectMethod::callPrecise(const QQmlObjectOrGadget
    #      &object, const QQmlPropertyData &data, ExecutionEngine *engine,
    #      CallData *callArgs, QMetaObject::Call callType)
    return Rituals.call(
        'ritual_ZN3QV413QObjectMethod11callPreciseERK18QQmlObjectOrGadgetRK'
        '16QQmlPropertyDataPNS_15ExecutionEngineEPNS_8CallDataEN11QMetaObje'
        'ct4CallE',
        CuteMixin._valueOf(object), CuteMixin._valueOf(data),
        CuteMixin._addressOf(engine), CuteMixin._addressOf(callArgs),
        callType.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QObjectMethod'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QObjectMethod]:
    """
    Calls Qt's 'QV4::Heap::QObjectMethod *QV4::QObjectMethod::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QObjectMethod]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QObjectMethod *QV4::QObjectMethod::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV413QObjectMethod11d_uncheckedEv',
    )
    return QV4.Heap.QObjectMethod._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QObjectMethod]:
    """
    Calls Qt's 'QV4::Heap::QObjectMethod *QV4::QObjectMethod::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#d

    Returns
    -------

    Optional[QV4.Heap.QObjectMethod]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QObjectMethod *QV4::QObjectMethod::d() const
    address = self.uglySide.call('ritual_ZNK3QV413QObjectMethod1dEv')
    return QV4.Heap.QObjectMethod._cuteAt(address)

  def methodIndex(self) -> int:
    """
    Calls Qt's 'int QV4::QObjectMethod::methodIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#methodIndex
    """
    #  int QV4::QObjectMethod::methodIndex() const
    return self.uglySide.call('ritual_ZNK3QV413QObjectMethod11methodIndexEv')

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::QObjectMethod::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::QObjectMethod::object() const
    address = self.uglySide.call('ritual_ZNK3QV413QObjectMethod6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def method_toString(
      self,
      engine: Optional[QV4.ExecutionEngine],
      o: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QV4::QObjectMethod::method_toString(QV4::ExecutionEngine *engine, QObject
    *o) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectmethod.html#method_toString

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::ReturnedValue
    #      QV4::QObjectMethod::method_toString(QV4::ExecutionEngine *engine,
    #      QObject *o) const
    return self.uglySide.call(
        'ritual_ZNK3QV413QObjectMethod15method_toStringEPNS_15ExecutionEngi'
        'neEP7QObject',
        self._addressOf(engine), self._addressOf(o, 'QObject'),
    )

  @overload(WAIT['QV4.ExecutionEngine'], QObject, QV4.Value, int)
  @overload(WAIT['QV4.ExecutionEngine'], QObject, NoneType, int)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType, int)
  @overload(NoneType, QObject, QV4.Value, int)
  @overload(NoneType, QObject, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_destroy(
      self,
      ctx: Optional[QV4.ExecutionEngine],
      o: Optional[QObject],
      args: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QV4::QObjectMethod::method_destroy(QV4::ExecutionEngine *ctx, QObject *o,
    const Value *args, int argc) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectmethod.html#method_destroy

    Parameters
    ----------

    ctx : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    args : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue
    #      QV4::QObjectMethod::method_destroy(QV4::ExecutionEngine *ctx,
    #      QObject *o, const Value *args, int argc) const
    return self.uglySide.call(
        'ritual_ZNK3QV413QObjectMethod14method_destroyEPNS_15ExecutionEngin'
        'eEP7QObjectPKNS_5ValueEi',
        self._addressOf(ctx), self._addressOf(o, 'QObject'),
        self._addressOf(args), argc,
    )

  @overload(WAIT['QV4.ExecutionEngine'], QObject, int)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
  @overload(NoneType, QObject, int)
  @overload(NoneType, NoneType, int)
  def method_destroy(
      self,
      engine: Optional[QV4.ExecutionEngine],
      o: Optional[QObject],
      delay: int,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::QObjectMethod::method_destroy(QV4::ExecutionEngine
    *engine, QObject *o, int delay) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectmethod.html#method_destroy

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    delay : int
      Passed on as it is.
    """
    #  bool QV4::QObjectMethod::method_destroy(QV4::ExecutionEngine *engine,
    #      QObject *o, int delay) const
    return self.uglySide.call(
        'ritual_ZNK3QV413QObjectMethod14method_destroyEPNS_15ExecutionEngin'
        'eEP7QObjecti',
        self._addressOf(engine), self._addressOf(o, 'QObject'), delay,
    )

  @overload(QV4.Value, QV4.Value, int)
  @overload(QV4.Value, NoneType, int)
  @overload(NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, int)
  def callInternal(
      self,
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectMethod::callInternal(const Value
    *thisObject, const Value *argv, int argc) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectmethod.html#callInternal

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
    #  ReturnedValue QV4::QObjectMethod::callInternal(const Value
    #      *thisObject, const Value *argv, int argc) const
    return self.uglySide.call(
        'ritual_ZNK3QV413QObjectMethod12callInternalEPKNS_5ValueES3_i',
        self._addressOf(thisObject), self._addressOf(argv), argc,
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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::QObjectMethod::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectmethod.html#__dataTest
    """
    #  void QV4::QObjectMethod::__dataTest()
    self.uglySide.call('ritual_ZN3QV413QObjectMethod10__dataTestEv')

  @staticmethod
  def callInternalWithMetaTypes(*__, **_) -> Never:
    """
    Qt's 'void QV4::QObjectMethod::callInternalWithMetaTypes(QObject
    *thisObject, void **argv, const QMetaType *types, int argc) const': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.QObjectMethod.callInternalWithMetaTypes' has no cute function "
        "yet. Qt's 'void "
        "QV4::QObjectMethod::callInternalWithMetaTypes(QObject *thisObject, "
        "void **argv, const QMetaType *types, int argc) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def extractQtMethod(*__, **_) -> Never:
    """
    Qt's 'std::pair<QObject *, int> QV4::QObjectMethod::extractQtMethod(const
    QV4::FunctionObject *function)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QV4.QObjectMethod.extractQtMethod' has no cute function yet. Qt's "
        "'std::pair<QObject *, int> "
        "QV4::QObjectMethod::extractQtMethod(const QV4::FunctionObject "
        "*function)': gives a type Python has no way to take yet.")

  @staticmethod
  def isExactMatch(*__, **_) -> Never:
    """
    Qt's 'bool QV4::QObjectMethod::isExactMatch(const QMetaMethod &method,
    void **argv, int argc, const QMetaType *types)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.QObjectMethod.isExactMatch' has no cute function yet. Qt's "
        "'bool QV4::QObjectMethod::isExactMatch(const QMetaMethod &method, "
        "void **argv, int argc, const QMetaType *types)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def virtualCallWithMetaTypes(*__, **_) -> Never:
    """
    Qt's 'void QV4::QObjectMethod::virtualCallWithMetaTypes(const
    FunctionObject *m, QObject *thisObject, void **argv, const QMetaType
    *types, int argc)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.QObjectMethod.virtualCallWithMetaTypes' has no cute function "
        "yet. Qt's 'void QV4::QObjectMethod::virtualCallWithMetaTypes(const "
        "FunctionObject *m, QObject *thisObject, void **argv, const "
        "QMetaType *types, int argc)': takes a type Python has no way to "
        "hand over yet.")
