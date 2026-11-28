"""
QJSValuePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qjsvalue_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QJSValuePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String, QString
  from . import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJSValuePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSValuePrivate: a plain Python object standing in
  front of one C++ QJSValuePrivate.

  C++ hands a QJSValuePrivate around as a copy, so every C++ QJSValuePrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJSValuePrivate that has a ritual and that Python
  can call so far, 21 names in all: 'tag', 'encodeUndefined', 'encodeNull',
  'intValue', 'encode', 'boolValue', 'qv4ValuePtr', 'qStringPtr',
  'fromReturnedValue', 'takeManagedValue', 'asPrimitiveType', 'asQString',
  'asReturnedValue', 'setString', 'adoptPersistentValue', 'setValue',
  'manageStringOnV4Heap', 'convertToReturnedValue', 'engine', 'checkEngine',
  'free'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QJSValuePrivate::pointer(quint64 raw)': gives 'void', which
    has no cute class yet.
  - Qt's 'quint64 QJSValuePrivate::encodePointer(void *pointer, Kind tag)':
    names 'void', which has no cute class yet.
  - Qt's 'quint64 QJSValuePrivate::encode(uint uintValue)': takes in Python
    what 'quint64 QJSValuePrivate::encode(int intValue)' takes.
  - Qt's 'QJSValuePrivate::~QJSValuePrivate()': the destructor: Python
    removes its C++ QJSValuePrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QJSValuePrivate is created at the first use, not by
    'QJSValuePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJSValuePrivate back gives a copy the ritual made for
    Python, in a new cute QJSValuePrivate.
  - Each name of Qt's QJSValuePrivate that has no cute function yet,
    'asManagedType', 'doublePtr', 'encodePointer', 'pointer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QJSValuePrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Kind(CuteNum, scoped=True):
    """
    The enum 'QJSValuePrivate::Kind' of Qt, with the 7 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Undefined = Kee[int](0)
    Null = Kee[int](2)
    IntValue = Kee[int](4)
    BoolValue = Kee[int](6)
    DoublePtr = Kee[int](1)
    QV4ValuePtr = Kee[int](3)
    QStringPtr = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def tag(raw: int) -> Kind:
    """
    Calls Qt's 'Kind QJSValuePrivate::tag(quint64 raw)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#tag

    Parameters
    ----------

    raw : int
      Passed on as it is.

    Returns
    -------

    Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Kind(number)' gives.
    """
    #  Kind QJSValuePrivate::tag(quint64 raw)
    return QJSValuePrivate.Kind(Rituals.call(
        'ritual_ZN15QJSValuePrivate3tagEy', raw,
    ))

  @staticmethod
  def encodeUndefined() -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encodeUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#encodeUndefined
    """
    #  quint64 QJSValuePrivate::encodeUndefined()
    return Rituals.call('ritual_ZN15QJSValuePrivate15encodeUndefinedEv')

  @staticmethod
  def encodeNull() -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encodeNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#encodeNull
    """
    #  quint64 QJSValuePrivate::encodeNull()
    return Rituals.call('ritual_ZN15QJSValuePrivate10encodeNullEv')

  @staticmethod
  @overload(int)
  def intValue(v: int) -> int:
    """
    Calls Qt's 'int QJSValuePrivate::intValue(quint64 v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#intValue

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  int QJSValuePrivate::intValue(quint64 v)
    return Rituals.call('ritual_ZN15QJSValuePrivate8intValueEy', v)

  @staticmethod
  @overload(int)
  def encode(intValue: int) -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encode(int intValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#encode

    Parameters
    ----------

    intValue : int
      Passed on as it is.
    """
    #  quint64 QJSValuePrivate::encode(int intValue)
    return Rituals.call('ritual_ZN15QJSValuePrivate6encodeEi', intValue)

  @staticmethod
  @overload(bool)
  def encode(boolValue: bool) -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encode(bool boolValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#encode

    Parameters
    ----------

    boolValue : bool
      Passed on as it is.
    """
    #  quint64 QJSValuePrivate::encode(bool boolValue)
    return Rituals.call('ritual_ZN15QJSValuePrivate6encodeEb', boolValue)

  @staticmethod
  @overload(float)
  def encode(doubleValue: float) -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encode(double doubleValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#encode

    Parameters
    ----------

    doubleValue : float
      Passed on as it is.
    """
    #  quint64 QJSValuePrivate::encode(double doubleValue)
    return Rituals.call('ritual_ZN15QJSValuePrivate6encodeEd', doubleValue)

  @staticmethod
  @overload(WAIT['QV4.Value'])
  def encode(qv4Value: QV4.Value) -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encode(const QV4::Value &qv4Value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#encode

    Parameters
    ----------

    qv4Value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  quint64 QJSValuePrivate::encode(const QV4::Value &qv4Value)
    return Rituals.call(
        'ritual_ZN15QJSValuePrivate6encodeERKN3QV45ValueE',
        CuteMixin._valueOf(qv4Value),
    )

  @staticmethod
  @overload(str)
  def encode(stringValue: str) -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encode(QString stringValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#encode

    Parameters
    ----------

    stringValue : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  quint64 QJSValuePrivate::encode(QString stringValue)
    return Rituals.call(
        'ritual_ZN15QJSValuePrivate6encodeE7QString', stringValue,
    )

  @staticmethod
  @overload(QLatin1String)
  def encode(stringValue: QLatin1String) -> int:
    """
    Calls Qt's 'quint64 QJSValuePrivate::encode(QLatin1String stringValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#encode

    Parameters
    ----------

    stringValue : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  quint64 QJSValuePrivate::encode(QLatin1String stringValue)
    return Rituals.call(
        'ritual_ZN15QJSValuePrivate6encodeE13QLatin1String',
        CuteMixin._valueOf(stringValue),
    )

  @staticmethod
  @overload(int)
  def boolValue(v: int) -> bool:
    """
    Calls Qt's 'bool QJSValuePrivate::boolValue(quint64 v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#boolValue

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  bool QJSValuePrivate::boolValue(quint64 v)
    return Rituals.call('ritual_ZN15QJSValuePrivate9boolValueEy', v)

  @staticmethod
  @overload(int)
  def qv4ValuePtr(v: int) -> Optional[QV4.Value]:
    """
    Calls Qt's 'QV4::Value *QJSValuePrivate::qv4ValuePtr(quint64 v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#qv4ValuePtr

    Parameters
    ----------

    v : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Value *QJSValuePrivate::qv4ValuePtr(quint64 v)
    address = Rituals.call('ritual_ZN15QJSValuePrivate11qv4ValuePtrEy', v)
    return QV4.Value._cuteAt(address)

  @staticmethod
  @overload(int)
  def qStringPtr(v: int) -> Optional[QString]:
    """
    Calls Qt's 'QString *QJSValuePrivate::qStringPtr(quint64 v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#qStringPtr

    Parameters
    ----------

    v : int
      Passed on as it is.

    Returns
    -------

    Optional[QString]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QString *QJSValuePrivate::qStringPtr(quint64 v)
    address = Rituals.call('ritual_ZN15QJSValuePrivate10qStringPtrEy', v)
    from ..QtCore import QString
    return QString._cuteAt(address)

  @staticmethod
  @overload(int)
  def fromReturnedValue(d: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue
    QJSValuePrivate::fromReturnedValue(QV4::ReturnedValue d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#fromReturnedValue

    Parameters
    ----------

    d : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValuePrivate::fromReturnedValue(QV4::ReturnedValue d)
    address = Rituals.call(
        'ritual_ZN15QJSValuePrivate17fromReturnedValueEy', d,
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @staticmethod
  @overload(QJSValue)
  @overload(NoneType)
  def takeManagedValue(jsval: Optional[QJSValue]) -> Optional[QV4.Value]:
    """
    Calls Qt's 'QV4::Value *QJSValuePrivate::takeManagedValue(QJSValue
    *jsval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#takeManagedValue

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Value *QJSValuePrivate::takeManagedValue(QJSValue *jsval)
    address = Rituals.call(
        'ritual_ZN15QJSValuePrivate16takeManagedValueEP8QJSValue',
        CuteMixin._addressOf(jsval),
    )
    return QV4.Value._cuteAt(address)

  @staticmethod
  @overload(QJSValue)
  @overload(NoneType)
  def asPrimitiveType(jsval: Optional[QJSValue]) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QJSValuePrivate::asPrimitiveType(const
    QJSValue *jsval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#asPrimitiveType

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::ReturnedValue QJSValuePrivate::asPrimitiveType(const QJSValue
    #      *jsval)
    return Rituals.call(
        'ritual_ZN15QJSValuePrivate15asPrimitiveTypeEPK8QJSValue',
        CuteMixin._addressOf(jsval),
    )

  @staticmethod
  @overload(QJSValue)
  @overload(NoneType)
  def asQString(jsval: Optional[QJSValue]) -> Optional[QString]:
    """
    Calls Qt's 'const QString *QJSValuePrivate::asQString(const QJSValue
    *jsval)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#asQString

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QString]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QString *QJSValuePrivate::asQString(const QJSValue *jsval)
    address = Rituals.call(
        'ritual_ZN15QJSValuePrivate9asQStringEPK8QJSValue',
        CuteMixin._addressOf(jsval),
    )
    from ..QtCore import QString
    return QString._cuteAt(address)

  @staticmethod
  @overload(QJSValue)
  @overload(NoneType)
  def asReturnedValue(jsval: Optional[QJSValue]) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QJSValuePrivate::asReturnedValue(const
    QJSValue *jsval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#asReturnedValue

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::ReturnedValue QJSValuePrivate::asReturnedValue(const QJSValue
    #      *jsval)
    return Rituals.call(
        'ritual_ZN15QJSValuePrivate15asReturnedValueEPK8QJSValue',
        CuteMixin._addressOf(jsval),
    )

  @staticmethod
  @overload(QJSValue, str)
  @overload(NoneType, str)
  def setString(jsval: Optional[QJSValue], s: str) -> None:
    """
    Calls Qt's 'void QJSValuePrivate::setString(QJSValue *jsval, QString s)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#setString

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QJSValuePrivate::setString(QJSValue *jsval, QString s)
    Rituals.call(
        'ritual_ZN15QJSValuePrivate9setStringEP8QJSValue7QString',
        CuteMixin._addressOf(jsval), s,
    )

  @staticmethod
  @overload(QJSValue, WAIT['QV4.Value'])
  @overload(QJSValue, NoneType)
  @overload(NoneType, WAIT['QV4.Value'])
  @overload(NoneType, NoneType)
  def adoptPersistentValue(
      jsval: Optional[QJSValue],
      v: Optional[QV4.Value],
  ) -> None:
    """
    Calls Qt's 'void QJSValuePrivate::adoptPersistentValue(QJSValue *jsval,
    QV4::Value *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#adoptPersistentValue

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QJSValuePrivate::adoptPersistentValue(QJSValue *jsval, QV4::Value
    #      *v)
    Rituals.call(
        'ritual_ZN15QJSValuePrivate20adoptPersistentValueEP8QJSValuePN3QV45'
        'ValueE',
        CuteMixin._addressOf(jsval), CuteMixin._addressOf(v),
    )

  @staticmethod
  @overload(QJSValue, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def setValue(jsval: Optional[QJSValue], v: QV4.Value) -> None:
    """
    Calls Qt's 'void QJSValuePrivate::setValue(QJSValue *jsval, const
    QV4::Value &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#setValue

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QJSValuePrivate::setValue(QJSValue *jsval, const QV4::Value &v)
    Rituals.call(
        'ritual_ZN15QJSValuePrivate8setValueEP8QJSValueRKN3QV45ValueE',
        CuteMixin._addressOf(jsval), CuteMixin._valueOf(v),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QJSValue)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QJSValue)
  @overload(NoneType, NoneType)
  def manageStringOnV4Heap(
      e: Optional[QV4.ExecutionEngine],
      jsval: Optional[QJSValue],
  ) -> None:
    """
    Calls Qt's 'void
    QJSValuePrivate::manageStringOnV4Heap(QV4::ExecutionEngine *e, QJSValue
    *jsval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#manageStringOnV4Heap

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QJSValuePrivate::manageStringOnV4Heap(QV4::ExecutionEngine *e,
    #      QJSValue *jsval)
    Rituals.call(
        'ritual_ZN15QJSValuePrivate20manageStringOnV4HeapEPN3QV415Execution'
        'EngineEP8QJSValue',
        CuteMixin._addressOf(e), CuteMixin._addressOf(jsval),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QJSValue)
  @overload(NoneType, QJSValue)
  def convertToReturnedValue(
      e: Optional[QV4.ExecutionEngine],
      jsval: QJSValue,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QJSValuePrivate::convertToReturnedValue(QV4::ExecutionEngine *e, const
    QJSValue &jsval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueprivate.html#convertToReturnedValue

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    jsval : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  QV4::ReturnedValue
    #      QJSValuePrivate::convertToReturnedValue(QV4::ExecutionEngine *e,
    #      const QJSValue &jsval)
    return Rituals.call(
        'ritual_ZN15QJSValuePrivate22convertToReturnedValueEPN3QV415Executi'
        'onEngineERK8QJSValue',
        CuteMixin._addressOf(e), CuteMixin._valueOf(jsval),
    )

  @staticmethod
  @overload(QJSValue)
  @overload(NoneType)
  def engine(jsval: Optional[QJSValue]) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QJSValuePrivate::engine(const QJSValue
    *jsval)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#engine

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QJSValuePrivate::engine(const QJSValue *jsval)
    address = Rituals.call(
        'ritual_ZN15QJSValuePrivate6engineEPK8QJSValue',
        CuteMixin._addressOf(jsval),
    )
    return QV4.ExecutionEngine._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QJSValue)
  @overload(NoneType, QJSValue)
  def checkEngine(e: Optional[QV4.ExecutionEngine], jsval: QJSValue) -> bool:
    """
    Calls Qt's 'bool QJSValuePrivate::checkEngine(QV4::ExecutionEngine *e,
    const QJSValue &jsval)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#checkEngine

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    jsval : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  bool QJSValuePrivate::checkEngine(QV4::ExecutionEngine *e, const
    #      QJSValue &jsval)
    return Rituals.call(
        'ritual_ZN15QJSValuePrivate11checkEngineEPN3QV415ExecutionEngineERK'
        '8QJSValue',
        CuteMixin._addressOf(e), CuteMixin._valueOf(jsval),
    )

  @staticmethod
  @overload(QJSValue)
  @overload(NoneType)
  def free(jsval: Optional[QJSValue]) -> None:
    """
    Calls Qt's 'void QJSValuePrivate::free(QJSValue *jsval)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueprivate.html#free

    Parameters
    ----------

    jsval : Optional[QJSValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QJSValuePrivate::free(QJSValue *jsval)
    Rituals.call(
        'ritual_ZN15QJSValuePrivate4freeEP8QJSValue',
        CuteMixin._addressOf(jsval),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSValuePrivate'

  #  Qt's '~QJSValuePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QJSValuePrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QJSValuePrivateD1Ev'

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
  def asManagedType(*__, **_) -> Never:
    """
    Qt's 'QJSValuePrivate::asManagedType': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QJSValuePrivate.asManagedType' has no cute function yet. Qt's "
        "'QJSValuePrivate::asManagedType': a template: a pattern and no "
        "single function.")

  @staticmethod
  def doublePtr(*__, **_) -> Never:
    """
    Qt's 'double *QJSValuePrivate::doublePtr(quint64 v)': takes or gives a
    type that cannot be passed yet: double *.
    """
    raise NotImplementedError(
        "'QJSValuePrivate.doublePtr' has no cute function yet. Qt's 'double "
        "*QJSValuePrivate::doublePtr(quint64 v)': takes or gives a type "
        "that cannot be passed yet: double *.")

  @staticmethod
  def encodePointer(*__, **_) -> Never:
    """
    Qt's 'quint64 QJSValuePrivate::encodePointer(void *pointer, Kind tag)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSValuePrivate.encodePointer' has no cute function yet. Qt's "
        "'quint64 QJSValuePrivate::encodePointer(void *pointer, Kind tag)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def pointer(*__, **_) -> Never:
    """
    Qt's 'void *QJSValuePrivate::pointer(quint64 raw)': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSValuePrivate.pointer' has no cute function yet. Qt's 'void "
        "*QJSValuePrivate::pointer(quint64 raw)': gives 'void', which has "
        "no cute class yet.")
