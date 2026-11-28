"""
QBinaryJsonValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonvalue_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QBinaryJsonValue to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QJsonValue
from . import QBinaryJsonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBinaryJsonValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonValue: a plain Python object standing in
  front of one C++ QBinaryJsonValue.

  What exists
  -----------

  Every function of Qt's QBinaryJsonValue that has a ritual and that Python
  can call so far, 4 names in all: 'type', 'toBool', 'toDouble', 'toString'.
  It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBinaryJsonValue::QBinaryJsonValue(const QBinaryJsonArray &a)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QBinaryJsonValue::QBinaryJsonValue(const QBinaryJsonObject &o)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QBinaryJsonValue::~QBinaryJsonValue()': the destructor: Python
    never removes a C++ QBinaryJsonValue.
  - Qt's 'QBinaryJsonValue::QBinaryJsonValue(QBinaryJsonValue &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QBinaryJsonValue &QBinaryJsonValue::operator=(QBinaryJsonValue
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QBinaryJsonValue QBinaryJsonValue::fromJsonValue(const QJsonValue
    &json)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QBinaryJsonValue is created at the first use, not by
    'QBinaryJsonValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBinaryJsonValue.
  - Each name of Qt's QBinaryJsonValue that has no cute function yet,
    'fromJsonValue', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QBinaryJsonValue'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QJsonValue.Type:
    """
    Calls Qt's 'QJsonValue::Type QBinaryJsonValue::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonvalue.html#type

    Returns
    -------

    QJsonValue.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QJsonValue.Type(number)'
      gives.
    """
    #  QJsonValue::Type QBinaryJsonValue::type() const
    return QJsonValue.Type(self.uglySide.call(
        'ritual_ZNK16QBinaryJsonValue4typeEv',
    ))

  def toBool(self) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonValue::toBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonvalue.html#toBool
    """
    #  bool QBinaryJsonValue::toBool() const
    return self.uglySide.call('ritual_ZNK16QBinaryJsonValue6toBoolEv')

  def toDouble(self) -> float:
    """
    Calls Qt's 'double QBinaryJsonValue::toDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonvalue.html#toDouble
    """
    #  double QBinaryJsonValue::toDouble() const
    return self.uglySide.call('ritual_ZNK16QBinaryJsonValue8toDoubleEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QBinaryJsonValue::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonvalue.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBinaryJsonValue::toString() const
    return self.uglySide.call('ritual_ZNK16QBinaryJsonValue8toStringEv')

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

  @overload(QJsonValue.Type)
  def __init__(self, type: QJsonValue.Type) -> None:
    """
    Notes what was given, for Qt's
    'QBinaryJsonValue::QBinaryJsonValue(QJsonValue::Type type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonvalue.html#QBinaryJsonValue

    Parameters
    ----------

    type : QJsonValue.Type
      Passed on as its number.
    """
    #  QBinaryJsonValue::QBinaryJsonValue(QJsonValue::Type type)
    self._noteCreation(QBinaryJsonValue, lambda: Rituals.call(
        'ritual_ZN16QBinaryJsonValueC1EN10QJsonValue4TypeE', type.value,
    ))

  @overload(bool)
  def __init__(self, b: bool) -> None:
    """
    Notes what was given, for Qt's 'QBinaryJsonValue::QBinaryJsonValue(bool
    b)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonvalue.html#QBinaryJsonValue

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  QBinaryJsonValue::QBinaryJsonValue(bool b)
    self._noteCreation(QBinaryJsonValue, lambda: Rituals.call(
        'ritual_ZN16QBinaryJsonValueC1Eb', b,
    ))

  @overload(float)
  def __init__(self, n: float) -> None:
    """
    Notes what was given, for Qt's 'QBinaryJsonValue::QBinaryJsonValue(double
    n)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonvalue.html#QBinaryJsonValue

    Parameters
    ----------

    n : float
      Passed on as it is.
    """
    #  QBinaryJsonValue::QBinaryJsonValue(double n)
    self._noteCreation(QBinaryJsonValue, lambda: Rituals.call(
        'ritual_ZN16QBinaryJsonValueC1Ed', n,
    ))

  @overload(str)
  def __init__(self, s: str) -> None:
    """
    Notes what was given, for Qt's
    'QBinaryJsonValue::QBinaryJsonValue(QString s)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonvalue.html#QBinaryJsonValue

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QBinaryJsonValue::QBinaryJsonValue(QString s)
    self._noteCreation(QBinaryJsonValue, lambda: Rituals.call(
        'ritual_ZN16QBinaryJsonValueC1E7QString', s,
    ))

  @overload(
      WAIT['QBinaryJsonPrivate.MutableData'],
      WAIT['QBinaryJsonPrivate.Base'], WAIT['QBinaryJsonPrivate.Value'],
  )
  @overload(
      WAIT['QBinaryJsonPrivate.MutableData'], NoneType,
      WAIT['QBinaryJsonPrivate.Value'],
  )
  @overload(
      NoneType, WAIT['QBinaryJsonPrivate.Base'],
      WAIT['QBinaryJsonPrivate.Value'],
  )
  @overload(NoneType, NoneType, WAIT['QBinaryJsonPrivate.Value'])
  def __init__(
      self,
      d: Optional[QBinaryJsonPrivate.MutableData],
      parent: Optional[QBinaryJsonPrivate.Base],
      v: QBinaryJsonPrivate.Value,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBinaryJsonValue::QBinaryJsonValue(QBinaryJsonPrivate::MutableData *d,
    QBinaryJsonPrivate::Base *parent, const QBinaryJsonPrivate::Value &v)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonvalue.html#QBinaryJsonValue

    Parameters
    ----------

    d : Optional[QBinaryJsonPrivate.MutableData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : QBinaryJsonPrivate.Value
      Passed on as a value: Qt reads the C++ QBinaryJsonPrivate::Value, which
      stays Python's own.
    """
    #  QBinaryJsonValue::QBinaryJsonValue(QBinaryJsonPrivate::MutableData *d,
    #      QBinaryJsonPrivate::Base *parent, const QBinaryJsonPrivate::Value
    #      &v)
    self._noteCreation(QBinaryJsonValue, lambda: Rituals.call(
        'ritual_ZN16QBinaryJsonValueC1EPN18QBinaryJsonPrivate11MutableDataE'
        'PNS0_4BaseERKNS0_5ValueE',
        self._addressOf(d), self._addressOf(parent), self._valueOf(v),
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
  def fromJsonValue(*__, **_) -> Never:
    """
    Qt's 'QBinaryJsonValue QBinaryJsonValue::fromJsonValue(const QJsonValue
    &json)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBinaryJsonValue.fromJsonValue' has no cute function yet. Qt's "
        "'QBinaryJsonValue QBinaryJsonValue::fromJsonValue(const QJsonValue "
        "&json)': gives a type Python has no way to take yet.")
