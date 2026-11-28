"""
QOpcUaReadResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuareadresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDateTime, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QVariant = WAIT['QVariant']


class QOpcUaReadResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaReadResult: a plain Python object standing in
  front of one C++ QOpcUaReadResult.

  C++ hands a QOpcUaReadResult around as a copy, so every C++
  QOpcUaReadResult behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaReadResult that has a ritual and that Python
  can call so far, 14 names in all: 'serverTimestamp', 'setServerTimestamp',
  'sourceTimestamp', 'setSourceTimestamp', 'statusCode', 'setStatusCode',
  'nodeId', 'setNodeId', 'attribute', 'setAttribute', 'indexRange',
  'setIndexRange', 'value', 'setValue'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaReadResult &QOpcUaReadResult::operator=(const
    QOpcUaReadResult &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaReadResult::~QOpcUaReadResult()': the destructor: Python
    removes its C++ QOpcUaReadResult by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaReadResult is created at the first use, not by
    'QOpcUaReadResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaReadResult back gives a copy the ritual made
    for Python, in a new cute QOpcUaReadResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaReadResult'

  #  Qt's '~QOpcUaReadResult()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaReadResult behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QOpcUaReadResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def serverTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaReadResult::serverTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#serverTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaReadResult::serverTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK16QOpcUaReadResult15serverTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def sourceTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaReadResult::sourceTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#sourceTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaReadResult::sourceTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK16QOpcUaReadResult15sourceTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaReadResult::statusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaReadResult::statusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK16QOpcUaReadResult10statusCodeEv',
    ))

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaReadResult::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaReadResult::nodeId() const
    return self.uglySide.call('ritual_ZNK16QOpcUaReadResult6nodeIdEv')

  def attribute(self) -> QOpcUa.NodeAttribute:
    """
    Calls Qt's 'QOpcUa::NodeAttribute QOpcUaReadResult::attribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#attribute

    Returns
    -------

    QOpcUa.NodeAttribute
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.NodeAttribute(number)' gives.
    """
    #  QOpcUa::NodeAttribute QOpcUaReadResult::attribute() const
    return QOpcUa.NodeAttribute(self.uglySide.call(
        'ritual_ZNK16QOpcUaReadResult9attributeEv',
    ))

  def indexRange(self) -> str:
    """
    Calls Qt's 'QString QOpcUaReadResult::indexRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#indexRange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaReadResult::indexRange() const
    return self.uglySide.call('ritual_ZNK16QOpcUaReadResult10indexRangeEv')

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaReadResult::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaReadResult::value() const
    address = self.uglySide.call('ritual_ZNK16QOpcUaReadResult5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setServerTimestamp(self, serverTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaReadResult::setServerTimestamp(const QDateTime
    &serverTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#setServerTimestamp

    Parameters
    ----------

    serverTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaReadResult::setServerTimestamp(const QDateTime
    #      &serverTimestamp)
    self.uglySide.call(
        'ritual_ZN16QOpcUaReadResult18setServerTimestampERK9QDateTime',
        self._valueOf(serverTimestamp),
    )

  @overload(QDateTime)
  def setSourceTimestamp(self, sourceTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaReadResult::setSourceTimestamp(const QDateTime
    &sourceTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#setSourceTimestamp

    Parameters
    ----------

    sourceTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaReadResult::setSourceTimestamp(const QDateTime
    #      &sourceTimestamp)
    self.uglySide.call(
        'ritual_ZN16QOpcUaReadResult18setSourceTimestampERK9QDateTime',
        self._valueOf(sourceTimestamp),
    )

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void QOpcUaReadResult::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#setStatusCode

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaReadResult::setStatusCode(QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaReadResult13setStatusCodeEN6QOpcUa12UaStatusCodeE',
        statusCode.value,
    )

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaReadResult::setNodeId(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaReadResult::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN16QOpcUaReadResult9setNodeIdERK7QString', nodeId,
    )

  @overload(QOpcUa.NodeAttribute)
  def setAttribute(self, attribute: QOpcUa.NodeAttribute) -> None:
    """
    Calls Qt's 'void QOpcUaReadResult::setAttribute(QOpcUa::NodeAttribute
    attribute)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#setAttribute

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.
    """
    #  void QOpcUaReadResult::setAttribute(QOpcUa::NodeAttribute attribute)
    self.uglySide.call(
        'ritual_ZN16QOpcUaReadResult12setAttributeEN6QOpcUa13NodeAttributeE',
        attribute.value,
    )

  @overload(str)
  def setIndexRange(self, indexRange: str) -> None:
    """
    Calls Qt's 'void QOpcUaReadResult::setIndexRange(const QString
    &indexRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#setIndexRange

    Parameters
    ----------

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaReadResult::setIndexRange(const QString &indexRange)
    self.uglySide.call(
        'ritual_ZN16QOpcUaReadResult13setIndexRangeERK7QString', indexRange,
    )

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QOpcUaReadResult::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareadresult.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaReadResult::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN16QOpcUaReadResult8setValueERK8QVariant',
        self._valueOf(value),
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
    Notes what was given, for Qt's 'QOpcUaReadResult::QOpcUaReadResult()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#QOpcUaReadResult
    """
    #  QOpcUaReadResult::QOpcUaReadResult()
    self._noteCreation(QOpcUaReadResult, lambda: Rituals.call(
        'ritual_ZN16QOpcUaReadResultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaReadResult) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaReadResult::QOpcUaReadResult(const
    QOpcUaReadResult &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuareadresult.html#QOpcUaReadResult

    Parameters
    ----------

    other : QOpcUaReadResult
      Passed on as a value: Qt reads the C++ QOpcUaReadResult, which stays
      Python's own.
    """
    #  QOpcUaReadResult::QOpcUaReadResult(const QOpcUaReadResult &other)
    self._noteCreation(QOpcUaReadResult, lambda: Rituals.call(
        'ritual_ZN16QOpcUaReadResultC1ERKS_', self._valueOf(other),
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


#  Qt's 'QList<QOpcUaReadResult>': the list of QOpcUaReadResult, which
#  'QList[QOpcUaReadResult]' gives. It is made here, so that there is one as
#  soon as there can be a QOpcUaReadResult.
QList.createKind(
    QOpcUaReadResult, 'value',
    make='ritual_list_make_QOpcUaReadResult',
    add='ritual_list_add_QOpcUaReadResult',
    size='ritual_list_size_QOpcUaReadResult',
    at='ritual_list_at_QOpcUaReadResult',
    drop='ritual_list_drop_QOpcUaReadResult',
)
