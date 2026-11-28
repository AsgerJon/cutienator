"""
QV4::DatePrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::DatePrototype to be private: it declares the class in a
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


class DatePrototype(QV4.Object):
  """
  The cute side of Qt's QV4::DatePrototype: a plain Python object standing in
  front of one C++ QV4::DatePrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::DatePrototype is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::DatePrototype that has a ritual and that Python
  can call so far, 4 names in all: 'defaultPrototype', 'method_now',
  'method_toJSON', 'method_symbolToPrimitive'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  49 of the 53 functions Qt declares: 40 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 9 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::DatePrototype is created at the first use, not by
    'QV4::DatePrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::DatePrototype.
  - Each name of Qt's QV4::DatePrototype that has no cute function yet,
    'getThisDate', 'init', 'method_UTC', 'method_getDate', 'method_getDay',
    'method_getFullYear', 'method_getHours', 'method_getMilliseconds',
    'method_getMinutes', 'method_getMonth', 'method_getSeconds',
    'method_getTime', 'method_getTimezoneOffset', 'method_getUTCDate',
    'method_getUTCDay', 'method_getUTCFullYear', 'method_getUTCHours',
    'method_getUTCMilliseconds', 'method_getUTCMinutes',
    'method_getUTCMonth', 'method_getUTCSeconds', 'method_getYear',
    'method_parse', 'method_setDate', 'method_setFullYear',
    'method_setHours', 'method_setMilliseconds', 'method_setMinutes',
    'method_setMonth', 'method_setSeconds', 'method_setTime',
    'method_setUTCDate', 'method_setUTCFullYear', 'method_setUTCHours',
    'method_setUTCMilliseconds', 'method_setUTCMinutes',
    'method_setUTCMonth', 'method_setUTCSeconds', 'method_setYear',
    'method_toDateString', 'method_toISOString', 'method_toLocaleDateString',
    'method_toLocaleString', 'method_toLocaleTimeString', 'method_toString',
    'method_toTimeString', 'method_toUTCString', 'method_valueOf',
    'timezoneUpdated', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    *QV4::DatePrototype::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-dateprototype.html#defaultPrototype

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
    #  QV4::Object *QV4::DatePrototype::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV413DatePrototype16defaultPrototypeEPNS_15ExecutionEngi'
        'neE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_now(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::DatePrototype::method_now(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-dateprototype.html#method_now

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
    #  ReturnedValue QV4::DatePrototype::method_now(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413DatePrototype10method_nowEPKNS_14FunctionObjectEPKN'
        'S_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_toJSON(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::DatePrototype::method_toJSON(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-dateprototype.html#method_toJSON

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
    #  ReturnedValue QV4::DatePrototype::method_toJSON(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413DatePrototype13method_toJSONEPKNS_14FunctionObjectE'
        'PKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_symbolToPrimitive(
      f: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      a2: Optional[QV4.Value],
      a3: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::DatePrototype::method_symbolToPrimitive(const FunctionObject *f,
    const Value *thisObject, const Value *a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-dateprototype.html#method_symbolToPrimitive

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a3 : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::DatePrototype::method_symbolToPrimitive(const
    #      FunctionObject *f, const Value *thisObject, const Value *a2, int
    #      a3)
    return Rituals.call(
        'ritual_ZN3QV413DatePrototype24method_symbolToPrimitiveEPKNS_14Func'
        'tionObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(a2), a3,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::DatePrototype'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def getThisDate(*__, **_) -> Never:
    """
    Qt's 'double QV4::DatePrototype::getThisDate(ExecutionEngine *v4, const
    Value *thisObject)': leans on 'QV4::Date::init(QDate)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.getThisDate' has no cute function yet. Qt's "
        "'double QV4::DatePrototype::getThisDate(ExecutionEngine *v4, const "
        "Value *thisObject)': leans on 'QV4::Date::init(QDate)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QV4::DatePrototype::init(ExecutionEngine *engine, Object
    *ctor)': leans on 'QV4::Date::init(QDate)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.init' has no cute function yet. Qt's 'void "
        "QV4::DatePrototype::init(ExecutionEngine *engine, Object *ctor)': "
        "leans on 'QV4::Date::init(QDate)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def method_UTC(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_UTC(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'MakeDate'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_UTC' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_UTC(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'MakeDate'.")

  @staticmethod
  def method_getDate(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getDate(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getDate' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_getDate(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_getDay(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getDay(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getDay' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_getDay(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_getFullYear(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getFullYear(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getFullYear' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getFullYear(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_getHours(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getHours(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getHours' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_getHours(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_getMilliseconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getMilliseconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getMilliseconds' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_getMilliseconds(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'LocalTime'.")

  @staticmethod
  def method_getMinutes(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getMinutes(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getMinutes' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getMinutes(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_getMonth(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getMonth(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getMonth' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_getMonth(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_getSeconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getSeconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getSeconds' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getSeconds(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_getTime(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getTime(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::Date::init(QDate)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getTime' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_getTime(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::Date::init(QDate)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def method_getTimezoneOffset(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getTimezoneOffset(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getTimezoneOffset' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_getTimezoneOffset(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'LocalTime'.")

  @staticmethod
  def method_getUTCDate(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCDate(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'DateFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCDate' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCDate(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'DateFromTime'.")

  @staticmethod
  def method_getUTCDay(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCDay(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::Date::init(QDate)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCDay' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCDay(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::Date::init(QDate)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def method_getUTCFullYear(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCFullYear(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'YearFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCFullYear' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_getUTCFullYear(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'YearFromTime'.")

  @staticmethod
  def method_getUTCHours(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCHours(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::Date::init(QDate)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCHours' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCHours(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::Date::init(QDate)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def method_getUTCMilliseconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCMilliseconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'msFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCMilliseconds' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_getUTCMilliseconds(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'msFromTime'.")

  @staticmethod
  def method_getUTCMinutes(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCMinutes(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::Date::init(QDate)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCMinutes' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCMinutes(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::Date::init(QDate)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def method_getUTCMonth(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCMonth(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'MonthFromTime'; did you mean 'MinFromTime'?.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCMonth' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCMonth(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'MonthFromTime'; did you mean 'MinFromTime'?.")

  @staticmethod
  def method_getUTCSeconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCSeconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::Date::init(QDate)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getUTCSeconds' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_getUTCSeconds(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::Date::init(QDate)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def method_getYear(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_getYear(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'YearFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_getYear' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_getYear(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'YearFromTime'.")

  @staticmethod
  def method_parse(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_parse(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'ParseString'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_parse' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_parse(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'ParseString'.")

  @staticmethod
  def method_setDate(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setDate(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setDate' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_setDate(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_setFullYear(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setFullYear(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setFullYear' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setFullYear(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_setHours(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setHours(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setHours' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_setHours(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_setMilliseconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setMilliseconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setMilliseconds' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_setMilliseconds(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'LocalTime'.")

  @staticmethod
  def method_setMinutes(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setMinutes(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setMinutes' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setMinutes(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_setMonth(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setMonth(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setMonth' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_setMonth(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_setSeconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setSeconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setSeconds' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setSeconds(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_setTime(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setTime(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::Date::encode(double)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setTime' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_setTime(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::Date::encode(double)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_setUTCDate(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCDate(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'YearFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setUTCDate' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCDate(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'YearFromTime'.")

  @staticmethod
  def method_setUTCFullYear(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCFullYear(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'MonthFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setUTCFullYear' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_setUTCFullYear(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'MonthFromTime'.")

  @staticmethod
  def method_setUTCHours(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCHours(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'MinFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setUTCHours' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCHours(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'MinFromTime'.")

  @staticmethod
  def method_setUTCMilliseconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCMilliseconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'MakeDate'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setUTCMilliseconds' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_setUTCMilliseconds(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'MakeDate'.")

  @staticmethod
  def method_setUTCMinutes(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCMinutes(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'SecFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setUTCMinutes' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCMinutes(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'SecFromTime'.")

  @staticmethod
  def method_setUTCMonth(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCMonth(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'DateFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setUTCMonth' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCMonth(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'DateFromTime'.")

  @staticmethod
  def method_setUTCSeconds(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCSeconds(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'msFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setUTCSeconds' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_setUTCSeconds(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'msFromTime'.")

  @staticmethod
  def method_setYear(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_setYear(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'LocalTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_setYear' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_setYear(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'LocalTime'.")

  @staticmethod
  def method_toDateString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toDateString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'ToDateString'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toDateString' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_toDateString(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'ToDateString'.")

  @staticmethod
  def method_toISOString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toISOString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'YearFromTime'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toISOString' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_toISOString(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'YearFromTime'.")

  @staticmethod
  def method_toLocaleDateString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toLocaleDateString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'ToLocaleDateString'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toLocaleDateString' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_toLocaleDateString(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ToLocaleDateString'.")

  @staticmethod
  def method_toLocaleString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toLocaleString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'ToLocaleString'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toLocaleString' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_toLocaleString(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ToLocaleString'.")

  @staticmethod
  def method_toLocaleTimeString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toLocaleTimeString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'ToLocaleTimeString'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toLocaleTimeString' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DatePrototype::method_toLocaleTimeString(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ToLocaleTimeString'.")

  @staticmethod
  def method_toString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'ToString';
    did you mean 'toString'?.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toString' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_toString(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'ToString'; did you mean 'toString'?.")

  @staticmethod
  def method_toTimeString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toTimeString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'ToTimeString'; did you mean 'DomString'?.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toTimeString' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_toTimeString(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'ToTimeString'; did you mean 'DomString'?.")

  @staticmethod
  def method_toUTCString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_toUTCString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'ToUTCString'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_toUTCString' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::DatePrototype::method_toUTCString(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'ToUTCString'.")

  @staticmethod
  def method_valueOf(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DatePrototype::method_valueOf(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::Date::init(QDate)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.method_valueOf' has no cute function yet. Qt's "
        "'ReturnedValue QV4::DatePrototype::method_valueOf(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::Date::init(QDate)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def timezoneUpdated(*__, **_) -> Never:
    """
    Qt's 'void QV4::DatePrototype::timezoneUpdated(ExecutionEngine *e)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'getLocalTZA'.
    """
    raise NotImplementedError(
        "'QV4.DatePrototype.timezoneUpdated' has no cute function yet. Qt's "
        "'void QV4::DatePrototype::timezoneUpdated(ExecutionEngine *e)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'getLocalTZA'.")
