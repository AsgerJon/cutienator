"""
QOpcUaDataValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuadatavalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QVariant = WAIT['QVariant']


class QOpcUaDataValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaDataValue: a plain Python object standing in
  front of one C++ QOpcUaDataValue.

  C++ hands a QOpcUaDataValue around as a copy, so every C++ QOpcUaDataValue
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaDataValue that has a ritual and that Python
  can call so far, 14 names in all: 'serverTimestamp', 'setServerTimestamp',
  'serverPicoseconds', 'setServerPicoseconds', 'sourceTimestamp',
  'setSourceTimestamp', 'sourcePicoseconds', 'setSourcePicoseconds',
  'statusCode', 'setStatusCode', 'value', 'setValue', '__eq__', '__ne__'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaDataValue &QOpcUaDataValue::operator=(const QOpcUaDataValue
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaDataValue::~QOpcUaDataValue()': the destructor: Python
    removes its C++ QOpcUaDataValue by it, and has no other use for it.
  - Qt's 'void QOpcUaDataValue::swap(QOpcUaDataValue &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QVariant QOpcUaDataValue::operator QVariant() const': an operator
    Python has no name for.

  What to expect
  --------------

  - The C++ QOpcUaDataValue is created at the first use, not by
    'QOpcUaDataValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaDataValue back gives a copy the ritual made for
    Python, in a new cute QOpcUaDataValue.
  - Each name of Qt's QOpcUaDataValue that has no cute function yet, 'swap',
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
  __qt_class__ = 'QOpcUaDataValue'

  #  Qt's '~QOpcUaDataValue()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaDataValue behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QOpcUaDataValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def serverTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaDataValue::serverTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#serverTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaDataValue::serverTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaDataValue15serverTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def serverPicoseconds(self) -> int:
    """
    Calls Qt's 'quint16 QOpcUaDataValue::serverPicoseconds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#serverPicoseconds
    """
    #  quint16 QOpcUaDataValue::serverPicoseconds() const
    return self.uglySide.call(
        'ritual_ZNK15QOpcUaDataValue17serverPicosecondsEv',
    )

  def sourceTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaDataValue::sourceTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#sourceTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaDataValue::sourceTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaDataValue15sourceTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def sourcePicoseconds(self) -> int:
    """
    Calls Qt's 'quint16 QOpcUaDataValue::sourcePicoseconds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#sourcePicoseconds
    """
    #  quint16 QOpcUaDataValue::sourcePicoseconds() const
    return self.uglySide.call(
        'ritual_ZNK15QOpcUaDataValue17sourcePicosecondsEv',
    )

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaDataValue::statusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuadatavalue.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaDataValue::statusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK15QOpcUaDataValue10statusCodeEv',
    ))

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaDataValue::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuadatavalue.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaDataValue::value() const
    address = self.uglySide.call('ritual_ZNK15QOpcUaDataValue5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setServerTimestamp(self, serverTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaDataValue::setServerTimestamp(const QDateTime
    &serverTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#setServerTimestamp

    Parameters
    ----------

    serverTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaDataValue::setServerTimestamp(const QDateTime
    #      &serverTimestamp)
    self.uglySide.call(
        'ritual_ZN15QOpcUaDataValue18setServerTimestampERK9QDateTime',
        self._valueOf(serverTimestamp),
    )

  @overload(int)
  def setServerPicoseconds(self, serverPicoseconds: int) -> None:
    """
    Calls Qt's 'void QOpcUaDataValue::setServerPicoseconds(quint16
    serverPicoseconds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#setServerPicoseconds

    Parameters
    ----------

    serverPicoseconds : int
      Passed on as it is.
    """
    #  void QOpcUaDataValue::setServerPicoseconds(quint16 serverPicoseconds)
    self.uglySide.call(
        'ritual_ZN15QOpcUaDataValue20setServerPicosecondsEt',
        serverPicoseconds,
    )

  @overload(QDateTime)
  def setSourceTimestamp(self, sourceTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaDataValue::setSourceTimestamp(const QDateTime
    &sourceTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#setSourceTimestamp

    Parameters
    ----------

    sourceTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaDataValue::setSourceTimestamp(const QDateTime
    #      &sourceTimestamp)
    self.uglySide.call(
        'ritual_ZN15QOpcUaDataValue18setSourceTimestampERK9QDateTime',
        self._valueOf(sourceTimestamp),
    )

  @overload(int)
  def setSourcePicoseconds(self, sourcePicoseconds: int) -> None:
    """
    Calls Qt's 'void QOpcUaDataValue::setSourcePicoseconds(quint16
    sourcePicoseconds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#setSourcePicoseconds

    Parameters
    ----------

    sourcePicoseconds : int
      Passed on as it is.
    """
    #  void QOpcUaDataValue::setSourcePicoseconds(quint16 sourcePicoseconds)
    self.uglySide.call(
        'ritual_ZN15QOpcUaDataValue20setSourcePicosecondsEt',
        sourcePicoseconds,
    )

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void QOpcUaDataValue::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuadatavalue.html#setStatusCode

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaDataValue::setStatusCode(QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN15QOpcUaDataValue13setStatusCodeEN6QOpcUa12UaStatusCodeE',
        statusCode.value,
    )

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QOpcUaDataValue::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuadatavalue.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaDataValue::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN15QOpcUaDataValue8setValueERK8QVariant',
        self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaDataValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaDataValue &lhs, const
    QOpcUaDataValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuadatavalue.html#operator==

    Parameters
    ----------

    rhs : QOpcUaDataValue
      Passed on as a value: Qt reads the C++ QOpcUaDataValue, which stays
      Python's own.
    """
    #  bool operator==(const QOpcUaDataValue &lhs, const QOpcUaDataValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK15QOpcUaDataValueS1_',
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
  def __ne__(self, rhs: QOpcUaDataValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaDataValue &lhs, const
    QOpcUaDataValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuadatavalue.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaDataValue
      Passed on as a value: Qt reads the C++ QOpcUaDataValue, which stays
      Python's own.
    """
    #  bool operator!=(const QOpcUaDataValue &lhs, const QOpcUaDataValue
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK15QOpcUaDataValueS1_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaDataValue::QOpcUaDataValue()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#QOpcUaDataValue
    """
    #  QOpcUaDataValue::QOpcUaDataValue()
    self._noteCreation(QOpcUaDataValue, lambda: Rituals.call(
        'ritual_ZN15QOpcUaDataValueC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaDataValue) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaDataValue::QOpcUaDataValue(const
    QOpcUaDataValue &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadatavalue.html#QOpcUaDataValue

    Parameters
    ----------

    other : QOpcUaDataValue
      Passed on as a value: Qt reads the C++ QOpcUaDataValue, which stays
      Python's own.
    """
    #  QOpcUaDataValue::QOpcUaDataValue(const QOpcUaDataValue &other)
    self._noteCreation(QOpcUaDataValue, lambda: Rituals.call(
        'ritual_ZN15QOpcUaDataValueC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaDataValue::swap(QOpcUaDataValue &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaDataValue.swap' has no cute function yet. Qt's 'void "
        "QOpcUaDataValue::swap(QOpcUaDataValue &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QOpcUaDataValue>': the list of QOpcUaDataValue, which
#  'QList[QOpcUaDataValue]' gives. It is made here, so that there is one as
#  soon as there can be a QOpcUaDataValue.
QList.createKind(
    QOpcUaDataValue, 'value',
    make='ritual_list_make_QOpcUaDataValue',
    add='ritual_list_add_QOpcUaDataValue',
    size='ritual_list_size_QOpcUaDataValue',
    at='ritual_list_at_QOpcUaDataValue',
    drop='ritual_list_drop_QOpcUaDataValue',
)
