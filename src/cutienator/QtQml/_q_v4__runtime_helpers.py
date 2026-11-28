"""
QV4::RuntimeHelpers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4runtime_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::RuntimeHelpers to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RuntimeHelpers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::RuntimeHelpers: a plain Python object standing
  in front of one C++ QV4::RuntimeHelpers.

  C++ hands a QV4::RuntimeHelpers around as a copy, so every C++
  QV4::RuntimeHelpers behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::RuntimeHelpers that has a ritual and that
  Python can call so far, 12 names in all: 'objectDefaultValue',
  'toPrimitive', 'ordinaryToPrimitive', 'stringToNumber', 'stringFromNumber',
  'toNumber', 'numberToString', 'convertToString', 'convertToObject',
  'equalHelper', 'strictEqual', 'addHelper'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::RuntimeHelpers::~RuntimeHelpers()': the destructor: Python
    removes its C++ QV4::RuntimeHelpers by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::RuntimeHelpers is created at the first use, not by
    'QV4::RuntimeHelpers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::RuntimeHelpers back gives a copy the ritual made
    for Python, in a new cute QV4::RuntimeHelpers.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Object'], int)
  @overload(NoneType, int)
  def objectDefaultValue(object: Optional[QV4.Object], typeHint: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RuntimeHelpers::objectDefaultValue(const
    Object *object, int typeHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#objectDefaultValue

    Parameters
    ----------

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeHint : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RuntimeHelpers::objectDefaultValue(const Object
    #      *object, int typeHint)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers18objectDefaultValueEPKNS_6ObjectEi',
        CuteMixin._addressOf(object), typeHint,
    )

  @staticmethod
  @overload(WAIT['QV4.Value'], QV4.TypeHint)
  def toPrimitive(value: QV4.Value, typeHint: QV4.TypeHint) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RuntimeHelpers::toPrimitive(const Value
    &value, TypeHint typeHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#toPrimitive

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    typeHint : QV4.TypeHint
      Passed on as its number.
    """
    #  ReturnedValue QV4::RuntimeHelpers::toPrimitive(const Value &value,
    #      TypeHint typeHint)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers11toPrimitiveERKNS_5ValueENS_8TypeHin'
        'tE',
        CuteMixin._valueOf(value), typeHint.value,
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Object'], WAIT['QV4.String'],
  )
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Object'], NoneType)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.String'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.Object'], WAIT['QV4.String'])
  @overload(NoneType, WAIT['QV4.Object'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.String'])
  @overload(NoneType, NoneType, NoneType)
  def ordinaryToPrimitive(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QV4.Object],
      typeHint: Optional[QV4.String],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::RuntimeHelpers::ordinaryToPrimitive(ExecutionEngine *engine, const
    Object *object, String *typeHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#ordinaryToPrimitive

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeHint : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::RuntimeHelpers::ordinaryToPrimitive(ExecutionEngine
    #      *engine, const Object *object, String *typeHint)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers19ordinaryToPrimitiveEPNS_15Execution'
        'EngineEPKNS_6ObjectEPNS_6StringE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object),
        CuteMixin._addressOf(typeHint),
    )

  @staticmethod
  @overload(str)
  def stringToNumber(s: str) -> float:
    """
    Calls Qt's 'double QV4::RuntimeHelpers::stringToNumber(const QString
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#stringToNumber

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  double QV4::RuntimeHelpers::stringToNumber(const QString &s)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers14stringToNumberERK7QString', s,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], float)
  @overload(NoneType, float)
  def stringFromNumber(
      engine: Optional[QV4.ExecutionEngine],
      number: float,
  ) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String
    *QV4::RuntimeHelpers::stringFromNumber(ExecutionEngine *engine, double
    number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#stringFromNumber

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    number : float
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::RuntimeHelpers::stringFromNumber(ExecutionEngine
    #      *engine, double number)
    address = Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers16stringFromNumberEPNS_15ExecutionEng'
        'ineEd',
        CuteMixin._addressOf(engine), number,
    )
    return QV4.Heap.String._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Value'])
  def toNumber(value: QV4.Value) -> float:
    """
    Calls Qt's 'double QV4::RuntimeHelpers::toNumber(const Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-runtimehelpers.html#toNumber

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  double QV4::RuntimeHelpers::toNumber(const Value &value)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers8toNumberERKNS_5ValueE',
        CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(QString, float)
  @overload(NoneType, float)
  @overload(QString, float, int)
  @overload(NoneType, float, int)
  def numberToString(
      result: Optional[QString],
      num: float,
      radix: int = 10,
  ) -> None:
    """
    Calls Qt's 'void QV4::RuntimeHelpers::numberToString(QString *result,
    double num, int radix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#numberToString

    Parameters
    ----------

    result : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    num : float
      Passed on as it is.

    radix : int
      Passed on as it is. May be left out, as in Qt: it is then 10.
    """
    #  void QV4::RuntimeHelpers::numberToString(QString *result, double num,
    #      int radix)
    Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers14numberToStringEP7QStringdi',
        CuteMixin._addressOf(result), num, radix,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], QV4.TypeHint)
  @overload(NoneType, WAIT['QV4.Value'], QV4.TypeHint)
  def convertToString(
      engine: Optional[QV4.ExecutionEngine],
      value: QV4.Value,
      a2: QV4.TypeHint = QV4.TypeHint.STRING_HINT,
  ) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String
    *QV4::RuntimeHelpers::convertToString(ExecutionEngine *engine, Value
    value, TypeHint a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#convertToString

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    a2 : QV4.TypeHint
      Passed on as its number. May be left out, as in Qt: it is then
      QV4.TypeHint.STRING_HINT.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::RuntimeHelpers::convertToString(ExecutionEngine
    #      *engine, Value value, TypeHint a2)
    address = Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers15convertToStringEPNS_15ExecutionEngi'
        'neENS_5ValueENS_8TypeHintE',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(value), a2.value,
    )
    return QV4.Heap.String._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def convertToObject(
      engine: Optional[QV4.ExecutionEngine],
      value: QV4.Value,
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::RuntimeHelpers::convertToObject(ExecutionEngine *engine, const
    Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#convertToObject

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::RuntimeHelpers::convertToObject(ExecutionEngine
    #      *engine, const Value &value)
    address = Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers15convertToObjectEPNS_15ExecutionEngi'
        'neERKNS_5ValueE',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(value),
    )
    return QV4.Heap.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
  def equalHelper(x: QV4.Value, y: QV4.Value) -> int:
    """
    Calls Qt's 'Bool QV4::RuntimeHelpers::equalHelper(const Value &x, const
    Value &y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#equalHelper

    Parameters
    ----------

    x : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    y : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  Bool QV4::RuntimeHelpers::equalHelper(const Value &x, const Value &y)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers11equalHelperERKNS_5ValueES3_',
        CuteMixin._valueOf(x), CuteMixin._valueOf(y),
    )

  @staticmethod
  @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
  def strictEqual(x: QV4.Value, y: QV4.Value) -> int:
    """
    Calls Qt's 'Bool QV4::RuntimeHelpers::strictEqual(const Value &x, const
    Value &y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimehelpers.html#strictEqual

    Parameters
    ----------

    x : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    y : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  Bool QV4::RuntimeHelpers::strictEqual(const Value &x, const Value &y)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers11strictEqualERKNS_5ValueES3_',
        CuteMixin._valueOf(x), CuteMixin._valueOf(y),
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
  )
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
  def addHelper(
      engine: Optional[QV4.ExecutionEngine],
      left: QV4.Value,
      right: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RuntimeHelpers::addHelper(ExecutionEngine
    *engine, const Value &left, const Value &right)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-runtimehelpers.html#addHelper

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    left : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    right : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::RuntimeHelpers::addHelper(ExecutionEngine *engine,
    #      const Value &left, const Value &right)
    return Rituals.call(
        'ritual_ZN3QV414RuntimeHelpers9addHelperEPNS_15ExecutionEngineERKNS'
        '_5ValueES5_',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(left),
        CuteMixin._valueOf(right),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::RuntimeHelpers'

  #  Qt's '~QV4::RuntimeHelpers()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::RuntimeHelpers behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV414RuntimeHelpersD1Ev'

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
