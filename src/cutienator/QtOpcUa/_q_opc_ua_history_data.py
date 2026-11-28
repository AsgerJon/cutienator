"""
QOpcUaHistoryData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuahistorydata.h, Qt 6.12.0. Changes made here are lost.
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

  from . import QOpcUaDataValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaDataValue = WAIT['QOpcUaDataValue']


class QOpcUaHistoryData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaHistoryData: a plain Python object standing in
  front of one C++ QOpcUaHistoryData.

  C++ hands a QOpcUaHistoryData around as a copy, so every C++
  QOpcUaHistoryData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaHistoryData that has a ritual and that Python
  can call so far, 7 names in all: 'statusCode', 'setStatusCode', 'result',
  'count', 'addValue', 'nodeId', 'setNodeId'. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaHistoryData::~QOpcUaHistoryData()': the destructor: Python
    removes its C++ QOpcUaHistoryData by it, and has no other use for it.
  - Qt's 'void QOpcUaHistoryData::swap(QOpcUaHistoryData &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QOpcUaHistoryData &QOpcUaHistoryData::operator=(const
    QOpcUaHistoryData &other)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QOpcUaHistoryData is created at the first use, not by
    'QOpcUaHistoryData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaHistoryData back gives a copy the ritual made
    for Python, in a new cute QOpcUaHistoryData.
  - Each name of Qt's QOpcUaHistoryData that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaHistoryData'

  #  Qt's '~QOpcUaHistoryData()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaHistoryData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QOpcUaHistoryDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaHistoryData::statusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistorydata.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaHistoryData::statusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK17QOpcUaHistoryData10statusCodeEv',
    ))

  def result(self) -> QList[QOpcUaDataValue]:
    """
    Calls Qt's 'QList<QOpcUaDataValue> QOpcUaHistoryData::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistorydata.html#result

    Returns
    -------

    QList[QOpcUaDataValue]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaDataValue> QOpcUaHistoryData::result() const
    address = self.uglySide.call('ritual_ZNK17QOpcUaHistoryData6resultEv')
    from . import QOpcUaDataValue
    return QList[QOpcUaDataValue]._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QOpcUaHistoryData::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistorydata.html#count
    """
    #  int QOpcUaHistoryData::count() const
    return self.uglySide.call('ritual_ZNK17QOpcUaHistoryData5countEv')

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaHistoryData::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistorydata.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaHistoryData::nodeId() const
    return self.uglySide.call('ritual_ZNK17QOpcUaHistoryData6nodeIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryData::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistorydata.html#setStatusCode

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaHistoryData::setStatusCode(QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN17QOpcUaHistoryData13setStatusCodeEN6QOpcUa12UaStatusCode'
        'E',
        statusCode.value,
    )

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryData::setNodeId(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistorydata.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaHistoryData::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN17QOpcUaHistoryData9setNodeIdERK7QString', nodeId,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaHistoryData::QOpcUaHistoryData()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistorydata.html#QOpcUaHistoryData
    """
    #  QOpcUaHistoryData::QOpcUaHistoryData()
    self._noteCreation(QOpcUaHistoryData, lambda: Rituals.call(
        'ritual_ZN17QOpcUaHistoryDataC1Ev',
    ))

  @overload(str)
  def __init__(self, nodeId: str) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryData::QOpcUaHistoryData(const QString &nodeId)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistorydata.html#QOpcUaHistoryData

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QOpcUaHistoryData::QOpcUaHistoryData(const QString &nodeId)
    self._noteCreation(QOpcUaHistoryData, lambda: Rituals.call(
        'ritual_ZN17QOpcUaHistoryDataC1ERK7QString', nodeId,
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaHistoryData) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryData::QOpcUaHistoryData(const QOpcUaHistoryData &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistorydata.html#QOpcUaHistoryData

    Parameters
    ----------

    other : QOpcUaHistoryData
      Passed on as a value: Qt reads the C++ QOpcUaHistoryData, which stays
      Python's own.
    """
    #  QOpcUaHistoryData::QOpcUaHistoryData(const QOpcUaHistoryData &other)
    self._noteCreation(QOpcUaHistoryData, lambda: Rituals.call(
        'ritual_ZN17QOpcUaHistoryDataC1ERKS_', self._valueOf(other),
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

  @overload(QOpcUaDataValue)
  def addValue(self, value: QOpcUaDataValue) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryData::addValue(const QOpcUaDataValue
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistorydata.html#addValue

    Parameters
    ----------

    value : QOpcUaDataValue
      Passed on as a value: Qt reads the C++ QOpcUaDataValue, which stays
      Python's own.
    """
    #  void QOpcUaHistoryData::addValue(const QOpcUaDataValue &value)
    self.uglySide.call(
        'ritual_ZN17QOpcUaHistoryData8addValueERK15QOpcUaDataValue',
        self._valueOf(value),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaHistoryData::swap(QOpcUaHistoryData &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaHistoryData.swap' has no cute function yet. Qt's 'void "
        "QOpcUaHistoryData::swap(QOpcUaHistoryData &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QOpcUaHistoryData>': the list of QOpcUaHistoryData, which
#  'QList[QOpcUaHistoryData]' gives. It is made here, so that there is one as
#  soon as there can be a QOpcUaHistoryData.
QList.createKind(
    QOpcUaHistoryData, 'value',
    make='ritual_list_make_QOpcUaHistoryData',
    add='ritual_list_add_QOpcUaHistoryData',
    size='ritual_list_size_QOpcUaHistoryData',
    at='ritual_list_at_QOpcUaHistoryData',
    drop='ritual_list_drop_QOpcUaHistoryData',
)
