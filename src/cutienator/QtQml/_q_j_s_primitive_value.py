"""
QJSPrimitiveValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qjsprimitivevalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QMetaType, QVariant
  from . import QJSPrimitiveNull, QJSPrimitiveUndefined
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSPrimitiveNull = WAIT['QJSPrimitiveNull']
  QJSPrimitiveUndefined = WAIT['QJSPrimitiveUndefined']
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']


class QJSPrimitiveValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSPrimitiveValue: a plain Python object standing in
  front of one C++ QJSPrimitiveValue.

  C++ hands a QJSPrimitiveValue around as a copy, so every C++
  QJSPrimitiveValue behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJSPrimitiveValue that has a ritual and that Python
  can call so far, 27 names in all: 'type', 'toBoolean', 'toInteger',
  'toDouble', 'toString', '__add__', '__sub__', '__mul__', '__truediv__',
  '__mod__', '__pos__', '__neg__', 'strictlyEquals', 'equals', '__eq__',
  '__ne__', '__lt__', '__gt__', '__le__', '__ge__', 'asBoolean', 'asInteger',
  'asDouble', 'asString', 'parsedEquals', 'numberFromString',
  'isNanOrUndefined'. It can be made from Python, in 9 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJSPrimitiveValue::QJSPrimitiveValue(const QMetaType type, const
    void *value)': names 'void', which has no cute class yet.
  - Qt's 'void *QJSPrimitiveValue::data()': gives 'void', which has no cute
    class yet.
  - Qt's 'const void *QJSPrimitiveValue::data() const': gives 'void', which
    has no cute class yet.
  - Qt's 'const void *QJSPrimitiveValue::constData() const': gives 'void',
    which has no cute class yet.
  - Qt's 'QJSPrimitiveValue &QJSPrimitiveValue::operator++()': an operator
    Python has no name for.
  - Qt's 'QJSPrimitiveValue QJSPrimitiveValue::operator++(int a0)': an
    operator Python has no name for.
  - Qt's 'QJSPrimitiveValue &QJSPrimitiveValue::operator--()': an operator
    Python has no name for.
  - Qt's 'QJSPrimitiveValue QJSPrimitiveValue::operator--(int a0)': an
    operator Python has no name for.
  - Qt's 'QJSPrimitiveValue::~QJSPrimitiveValue()': the destructor: Python
    removes its C++ QJSPrimitiveValue by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 52 functions Qt declares: 3 a template; 2 leans on 'QtPrivate; 1
  forbidden.

  What to expect
  --------------

  - The C++ QJSPrimitiveValue is created at the first use, not by
    'QJSPrimitiveValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJSPrimitiveValue back gives a copy the ritual made
    for Python, in a new cute QJSPrimitiveValue.
  - Each name of Qt's QJSPrimitiveValue that has no cute function yet,
    'constData', 'data', 'metaType', 'operate', 'operateOnIntegers', 'to',
    'toVariant', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QJSPrimitiveValue, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QJSPrimitiveValue::Type' of Qt, with the 6 names Qt gives in
    it.
    """

    Undefined = Kee[int](0)
    Null = Kee[int](1)
    Boolean = Kee[int](2)
    Integer = Kee[int](3)
    Double = Kee[int](4)
    String = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def numberFromString(string: str) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue QJSPrimitiveValue::numberFromString(const
    QString &string)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#numberFromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue QJSPrimitiveValue::numberFromString(const QString
    #      &string)
    address = Rituals.call(
        'ritual_ZN17QJSPrimitiveValue16numberFromStringERK7QString', string,
    )
    return QJSPrimitiveValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSPrimitiveValue'

  #  Qt's '~QJSPrimitiveValue()'. Naming it makes this a value class: Python
  #  owns every C++ QJSPrimitiveValue behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QJSPrimitiveValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QJSPrimitiveValue::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QJSPrimitiveValue::type() const
    return QJSPrimitiveValue.Type(self.uglySide.call(
        'ritual_ZNK17QJSPrimitiveValue4typeEv',
    ))

  def toBoolean(self) -> bool:
    """
    Calls Qt's 'bool QJSPrimitiveValue::toBoolean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#toBoolean
    """
    #  bool QJSPrimitiveValue::toBoolean() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue9toBooleanEv')

  def toInteger(self) -> int:
    """
    Calls Qt's 'int QJSPrimitiveValue::toInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#toInteger
    """
    #  int QJSPrimitiveValue::toInteger() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue9toIntegerEv')

  def toDouble(self) -> float:
    """
    Calls Qt's 'double QJSPrimitiveValue::toDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#toDouble
    """
    #  double QJSPrimitiveValue::toDouble() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue8toDoubleEv')

  @overload()
  def toString(self) -> str:
    """
    Calls Qt's 'QString QJSPrimitiveValue::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSPrimitiveValue::toString() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue8toStringEv')

  @staticmethod
  @overload(float)
  def toString(d: float) -> str:
    """
    Calls Qt's 'QString QJSPrimitiveValue::toString(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#toString

    Parameters
    ----------

    d : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSPrimitiveValue::toString(double d)
    return Rituals.call('ritual_ZN17QJSPrimitiveValue8toStringEd', d)

  @overload(THIS)
  def strictlyEquals(self, other: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool QJSPrimitiveValue::strictlyEquals(const
    QJSPrimitiveValue &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#strictlyEquals

    Parameters
    ----------

    other : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool QJSPrimitiveValue::strictlyEquals(const QJSPrimitiveValue &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QJSPrimitiveValue14strictlyEqualsERKS_',
        self._valueOf(other),
    )

  @overload(THIS)
  def equals(self, other: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool QJSPrimitiveValue::equals(const QJSPrimitiveValue
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#equals

    Parameters
    ----------

    other : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool QJSPrimitiveValue::equals(const QJSPrimitiveValue &other) const
    return self.uglySide.call(
        'ritual_ZNK17QJSPrimitiveValue6equalsERKS_', self._valueOf(other),
    )

  def asBoolean(self) -> bool:
    """
    Calls Qt's 'bool QJSPrimitiveValue::asBoolean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#asBoolean
    """
    #  bool QJSPrimitiveValue::asBoolean() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue9asBooleanEv')

  def asInteger(self) -> int:
    """
    Calls Qt's 'int QJSPrimitiveValue::asInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#asInteger
    """
    #  int QJSPrimitiveValue::asInteger() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue9asIntegerEv')

  def asDouble(self) -> float:
    """
    Calls Qt's 'double QJSPrimitiveValue::asDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#asDouble
    """
    #  double QJSPrimitiveValue::asDouble() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue8asDoubleEv')

  def asString(self) -> str:
    """
    Calls Qt's 'QString QJSPrimitiveValue::asString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#asString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSPrimitiveValue::asString() const
    return self.uglySide.call('ritual_ZNK17QJSPrimitiveValue8asStringEv')

  @overload(THIS)
  def parsedEquals(self, other: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool QJSPrimitiveValue::parsedEquals(const QJSPrimitiveValue
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#parsedEquals

    Parameters
    ----------

    other : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool QJSPrimitiveValue::parsedEquals(const QJSPrimitiveValue &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QJSPrimitiveValue12parsedEqualsERKS_',
        self._valueOf(other),
    )

  def isNanOrUndefined(self) -> bool:
    """
    Calls Qt's 'bool QJSPrimitiveValue::isNanOrUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#isNanOrUndefined
    """
    #  bool QJSPrimitiveValue::isNanOrUndefined() const
    return self.uglySide.call(
        'ritual_ZNK17QJSPrimitiveValue16isNanOrUndefinedEv',
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

  @overload(THIS)
  def __add__(self, rhs: QJSPrimitiveValue) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue operator+(const QJSPrimitiveValue &lhs,
    const QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator+

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue operator+(const QJSPrimitiveValue &lhs, const
    #      QJSPrimitiveValue &rhs)
    address = Rituals.call(
        'ritual_ZplRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )
    return QJSPrimitiveValue._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, rhs: QJSPrimitiveValue) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue operator-(const QJSPrimitiveValue &lhs,
    const QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator-

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue operator-(const QJSPrimitiveValue &lhs, const
    #      QJSPrimitiveValue &rhs)
    address = Rituals.call(
        'ritual_ZmiRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )
    return QJSPrimitiveValue._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __mul__(self, rhs: QJSPrimitiveValue) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue operator*(const QJSPrimitiveValue &lhs,
    const QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator*

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue operator*(const QJSPrimitiveValue &lhs, const
    #      QJSPrimitiveValue &rhs)
    address = Rituals.call(
        'ritual_ZmlRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )
    return QJSPrimitiveValue._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __truediv__(self, rhs: QJSPrimitiveValue) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue operator/(const QJSPrimitiveValue &lhs,
    const QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator/

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue operator/(const QJSPrimitiveValue &lhs, const
    #      QJSPrimitiveValue &rhs)
    address = Rituals.call(
        'ritual_ZdvRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )
    return QJSPrimitiveValue._cuteOwning(address)

  @overload.fallback
  def __truediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __mod__(self, rhs: QJSPrimitiveValue) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue operator%(const QJSPrimitiveValue &lhs,
    const QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator%

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue operator%(const QJSPrimitiveValue &lhs, const
    #      QJSPrimitiveValue &rhs)
    address = Rituals.call(
        'ritual_ZrmRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )
    return QJSPrimitiveValue._cuteOwning(address)

  @overload.fallback
  def __mod__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __pos__(self) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue QJSPrimitiveValue::operator+()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator+

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue QJSPrimitiveValue::operator+()
    address = self.uglySide.call('ritual_ZN17QJSPrimitiveValuepsEv')
    return QJSPrimitiveValue._cuteOwning(address)

  def __neg__(self) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue QJSPrimitiveValue::operator-()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator-

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue QJSPrimitiveValue::operator-()
    address = self.uglySide.call('ritual_ZN17QJSPrimitiveValuengEv')
    return QJSPrimitiveValue._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QJSPrimitiveValue &lhs, const
    QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator==

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool operator==(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJSPrimitiveValue &lhs, const
    QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator!=

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool operator!=(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool operator<(const QJSPrimitiveValue &lhs, const
    QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator<

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool operator<(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZltRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool operator>(const QJSPrimitiveValue &lhs, const
    QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator>

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool operator>(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZgtRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool operator<=(const QJSPrimitiveValue &lhs, const
    QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator<=

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool operator<=(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZleRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QJSPrimitiveValue) -> bool:
    """
    Calls Qt's 'bool operator>=(const QJSPrimitiveValue &lhs, const
    QJSPrimitiveValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsprimitivevalue.html#operator>=

    Parameters
    ----------

    rhs : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.
    """
    #  bool operator>=(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZgeRK17QJSPrimitiveValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QJSPrimitiveValue::QJSPrimitiveValue()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue()
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1Ev',
    ))

  @overload(QJSPrimitiveUndefined)
  def __init__(self, undefined: QJSPrimitiveUndefined) -> None:
    """
    Notes what was given, for Qt's
    'QJSPrimitiveValue::QJSPrimitiveValue(QJSPrimitiveUndefined undefined)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    undefined : QJSPrimitiveUndefined
      Passed on as a value: Qt reads the C++ QJSPrimitiveUndefined, which
      stays Python's own.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(QJSPrimitiveUndefined undefined)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1E21QJSPrimitiveUndefined',
        self._valueOf(undefined),
    ))

  @overload(QJSPrimitiveNull)
  def __init__(self, null: QJSPrimitiveNull) -> None:
    """
    Notes what was given, for Qt's
    'QJSPrimitiveValue::QJSPrimitiveValue(QJSPrimitiveNull null)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    null : QJSPrimitiveNull
      Passed on as a value: Qt reads the C++ QJSPrimitiveNull, which stays
      Python's own.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(QJSPrimitiveNull null)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1E16QJSPrimitiveNull',
        self._valueOf(null),
    ))

  @overload(bool)
  def __init__(self, value: bool) -> None:
    """
    Notes what was given, for Qt's 'QJSPrimitiveValue::QJSPrimitiveValue(bool
    value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(bool value)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1Eb', value,
    ))

  @overload(int)
  def __init__(self, value: int) -> None:
    """
    Notes what was given, for Qt's 'QJSPrimitiveValue::QJSPrimitiveValue(int
    value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(int value)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1Ei', value,
    ))

  @overload(float)
  def __init__(self, value: float) -> None:
    """
    Notes what was given, for Qt's
    'QJSPrimitiveValue::QJSPrimitiveValue(double value)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(double value)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1Ed', value,
    ))

  @overload(str)
  def __init__(self, string: str) -> None:
    """
    Notes what was given, for Qt's
    'QJSPrimitiveValue::QJSPrimitiveValue(QString string)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(QString string)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1E7QString', string,
    ))

  @overload(QMetaType)
  def __init__(self, type: QMetaType) -> None:
    """
    Notes what was given, for Qt's
    'QJSPrimitiveValue::QJSPrimitiveValue(QMetaType type)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(QMetaType type)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1E9QMetaType', self._valueOf(type),
    ))

  @overload(QVariant)
  def __init__(self, variant: QVariant) -> None:
    """
    Notes what was given, for Qt's
    'QJSPrimitiveValue::QJSPrimitiveValue(const QVariant &variant)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsprimitivevalue.html#QJSPrimitiveValue

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QJSPrimitiveValue::QJSPrimitiveValue(const QVariant &variant)
    self._noteCreation(QJSPrimitiveValue, lambda: Rituals.call(
        'ritual_ZN17QJSPrimitiveValueC1ERK8QVariant', self._valueOf(variant),
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

  @staticmethod
  def constData(*__, **_) -> Never:
    """
    Qt's 'const void *QJSPrimitiveValue::constData() const': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSPrimitiveValue.constData' has no cute function yet. Qt's "
        "'const void *QJSPrimitiveValue::constData() const': gives 'void', "
        "which has no cute class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    - Qt's 'void *QJSPrimitiveValue::data()': gives 'void', which has no cute
      class yet.
    - Qt's 'const void *QJSPrimitiveValue::data() const': gives 'void', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSPrimitiveValue.data' has no cute function yet. Qt's 'void "
        "*QJSPrimitiveValue::data()': gives 'void', which has no cute class "
        "yet. Qt's 'const void *QJSPrimitiveValue::data() const': gives "
        "'void', which has no cute class yet.")

  @staticmethod
  def metaType(*__, **_) -> Never:
    """
    Qt's 'QMetaType QJSPrimitiveValue::metaType() const': leans on
    'QtPrivate::QMetaTypeInterfaceWrapper<decltype(nullptr)>::metaType',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QJSPrimitiveValue.metaType' has no cute function yet. Qt's "
        "'QMetaType QJSPrimitiveValue::metaType() const': leans on "
        "'QtPrivate::QMetaTypeInterfaceWrapper<decltype(nullptr)>::metaType'"
        ", which Qt's source does not mark for use from outside Qt and has "
        "no code for that could be taken.")

  @staticmethod
  def operate(*__, **_) -> Never:
    """
    Qt's 'QJSPrimitiveValue::operate': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSPrimitiveValue.operate' has no cute function yet. Qt's "
        "'QJSPrimitiveValue::operate': a template: a pattern and no single "
        "function.")

  @staticmethod
  def operateOnIntegers(*__, **_) -> Never:
    """
    Qt's 'QJSPrimitiveValue::operateOnIntegers': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QJSPrimitiveValue.operateOnIntegers' has no cute function yet. "
        "Qt's 'QJSPrimitiveValue::operateOnIntegers': a template: a pattern "
        "and no single function.")

  @staticmethod
  def to(*__, **_) -> Never:
    """
    Qt's 'QJSPrimitiveValue::to': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSPrimitiveValue.to' has no cute function yet. Qt's "
        "'QJSPrimitiveValue::to': a template: a pattern and no single "
        "function.")

  @staticmethod
  def toVariant(*__, **_) -> Never:
    """
    Qt's 'QVariant QJSPrimitiveValue::toVariant() const': leans on
    'QtPrivate::QMetaTypeInterfaceWrapper<decltype(nullptr)>::metaType',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QJSPrimitiveValue.toVariant' has no cute function yet. Qt's "
        "'QVariant QJSPrimitiveValue::toVariant() const': leans on "
        "'QtPrivate::QMetaTypeInterfaceWrapper<decltype(nullptr)>::metaType'"
        ", which Qt's source does not mark for use from outside Qt and has "
        "no code for that could be taken.")
