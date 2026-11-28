"""
QV4::JsonObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::JsonObject to be private: it declares the class in a header
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

  from ..QtCore import QJsonArray, QJsonObject, QJsonValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']
  QJsonValue = WAIT['QJsonValue']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JsonObject(QV4.Object):
  """
  The cute side of Qt's QV4::JsonObject: a plain Python object standing in
  front of one C++ QV4::JsonObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::JsonObject is built on
  Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::JsonObject that has a ritual and that Python
  can call so far, 9 names in all: '__dataTest', 'd_unchecked', 'd',
  'fromJsonValue', 'fromJsonObject', 'fromJsonArray', 'toJsonValue',
  'toJsonObject', 'toJsonArray'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonValue QV4::JsonObject::toJsonValue(const QV4::Value &value,
    V4ObjectSet &visitedObjects)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QJsonObject QV4::JsonObject::toJsonObject(const Object *o,
    V4ObjectSet &visitedObjects)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QJsonArray QV4::JsonObject::toJsonArray(const Object *o,
    V4ObjectSet &visitedObjects)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  7 of the 19 functions Qt declares: 3 forbidden; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  not a gap; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::JsonObject is created at the first use, not by
    'QV4::JsonObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::JsonObject.
  - Each name of Qt's QV4::JsonObject that has no cute function yet,
    'method_parse', 'method_stringify', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QJsonValue)
  @overload(NoneType, QJsonValue)
  def fromJsonValue(
      engine: Optional[QV4.ExecutionEngine],
      value: QJsonValue,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::JsonObject::fromJsonValue(ExecutionEngine
    *engine, const QJsonValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#fromJsonValue

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  ReturnedValue QV4::JsonObject::fromJsonValue(ExecutionEngine *engine,
    #      const QJsonValue &value)
    return Rituals.call(
        'ritual_ZN3QV410JsonObject13fromJsonValueEPNS_15ExecutionEngineERK1'
        '0QJsonValue',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QJsonObject)
  @overload(NoneType, QJsonObject)
  def fromJsonObject(
      engine: Optional[QV4.ExecutionEngine],
      object: QJsonObject,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::JsonObject::fromJsonObject(ExecutionEngine
    *engine, const QJsonObject &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#fromJsonObject

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  ReturnedValue QV4::JsonObject::fromJsonObject(ExecutionEngine *engine,
    #      const QJsonObject &object)
    return Rituals.call(
        'ritual_ZN3QV410JsonObject14fromJsonObjectEPNS_15ExecutionEngineERK'
        '11QJsonObject',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QJsonArray)
  @overload(NoneType, QJsonArray)
  def fromJsonArray(
      engine: Optional[QV4.ExecutionEngine],
      array: QJsonArray,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::JsonObject::fromJsonArray(ExecutionEngine
    *engine, const QJsonArray &array)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#fromJsonArray

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    array : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  ReturnedValue QV4::JsonObject::fromJsonArray(ExecutionEngine *engine,
    #      const QJsonArray &array)
    return Rituals.call(
        'ritual_ZN3QV410JsonObject13fromJsonArrayEPNS_15ExecutionEngineERK1'
        '0QJsonArray',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(array),
    )

  @staticmethod
  @overload(QV4.Value)
  def toJsonValue(value: QV4.Value) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QV4::JsonObject::toJsonValue(const QV4::Value
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#toJsonValue

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QV4::JsonObject::toJsonValue(const QV4::Value &value)
    address = Rituals.call(
        'ritual_ZN3QV410JsonObject11toJsonValueERKNS_5ValueE',
        CuteMixin._valueOf(value),
    )
    from ..QtCore import QJsonValue
    return QJsonValue._cuteOwning(address)

  @staticmethod
  @overload(QV4.Object)
  @overload(NoneType)
  def toJsonObject(o: Optional[QV4.Object]) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QV4::JsonObject::toJsonObject(const QV4::Object
    *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#toJsonObject

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QV4::JsonObject::toJsonObject(const QV4::Object *o)
    address = Rituals.call(
        'ritual_ZN3QV410JsonObject12toJsonObjectEPKNS_6ObjectE',
        CuteMixin._addressOf(o),
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  @staticmethod
  @overload(QV4.Object)
  @overload(NoneType)
  def toJsonArray(o: Optional[QV4.Object]) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QV4::JsonObject::toJsonArray(const QV4::Object
    *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#toJsonArray

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QV4::JsonObject::toJsonArray(const QV4::Object *o)
    address = Rituals.call(
        'ritual_ZN3QV410JsonObject11toJsonArrayEPKNS_6ObjectE',
        CuteMixin._addressOf(o),
    )
    from ..QtCore import QJsonArray
    return QJsonArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::JsonObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.JsonObject]:
    """
    Calls Qt's 'QV4::Heap::JsonObject *QV4::JsonObject::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.JsonObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::JsonObject *QV4::JsonObject::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410JsonObject11d_uncheckedEv')
    return QV4.Heap.JsonObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.JsonObject]:
    """
    Calls Qt's 'QV4::Heap::JsonObject *QV4::JsonObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#d

    Returns
    -------

    Optional[QV4.Heap.JsonObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::JsonObject *QV4::JsonObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV410JsonObject1dEv')
    return QV4.Heap.JsonObject._cuteAt(address)

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
    Calls Qt's 'void QV4::JsonObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonobject.html#__dataTest
    """
    #  void QV4::JsonObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV410JsonObject10__dataTestEv')

  @staticmethod
  def method_parse(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::JsonObject::method_parse(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'DEBUG'.
    """
    raise NotImplementedError(
        "'QV4.JsonObject.method_parse' has no cute function yet. Qt's "
        "'ReturnedValue QV4::JsonObject::method_parse(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'DEBUG'.")

  @staticmethod
  def method_stringify(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::JsonObject::method_stringify(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no member named 'replacerFunction' in
    'QV4::String'.
    """
    raise NotImplementedError(
        "'QV4.JsonObject.method_stringify' has no cute function yet. Qt's "
        "'ReturnedValue QV4::JsonObject::method_stringify(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no member named "
        "'replacerFunction' in 'QV4::String'.")
