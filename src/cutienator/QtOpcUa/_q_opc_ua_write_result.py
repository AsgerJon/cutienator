"""
QOpcUaWriteResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuawriteresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa


class QOpcUaWriteResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaWriteResult: a plain Python object standing in
  front of one C++ QOpcUaWriteResult.

  C++ hands a QOpcUaWriteResult around as a copy, so every C++
  QOpcUaWriteResult behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaWriteResult that has a ritual and that Python
  can call so far, 8 names in all: 'nodeId', 'setNodeId', 'attribute',
  'setAttribute', 'indexRange', 'setIndexRange', 'statusCode',
  'setStatusCode'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaWriteResult &QOpcUaWriteResult::operator=(const
    QOpcUaWriteResult &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaWriteResult::~QOpcUaWriteResult()': the destructor: Python
    removes its C++ QOpcUaWriteResult by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaWriteResult is created at the first use, not by
    'QOpcUaWriteResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaWriteResult back gives a copy the ritual made
    for Python, in a new cute QOpcUaWriteResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaWriteResult'

  #  Qt's '~QOpcUaWriteResult()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaWriteResult behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QOpcUaWriteResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaWriteResult::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteresult.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaWriteResult::nodeId() const
    return self.uglySide.call('ritual_ZNK17QOpcUaWriteResult6nodeIdEv')

  def attribute(self) -> QOpcUa.NodeAttribute:
    """
    Calls Qt's 'QOpcUa::NodeAttribute QOpcUaWriteResult::attribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteresult.html#attribute

    Returns
    -------

    QOpcUa.NodeAttribute
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.NodeAttribute(number)' gives.
    """
    #  QOpcUa::NodeAttribute QOpcUaWriteResult::attribute() const
    return QOpcUa.NodeAttribute(self.uglySide.call(
        'ritual_ZNK17QOpcUaWriteResult9attributeEv',
    ))

  def indexRange(self) -> str:
    """
    Calls Qt's 'QString QOpcUaWriteResult::indexRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteresult.html#indexRange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaWriteResult::indexRange() const
    return self.uglySide.call('ritual_ZNK17QOpcUaWriteResult10indexRangeEv')

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaWriteResult::statusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteresult.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaWriteResult::statusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK17QOpcUaWriteResult10statusCodeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaWriteResult::setNodeId(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteresult.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaWriteResult::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN17QOpcUaWriteResult9setNodeIdERK7QString', nodeId,
    )

  @overload(QOpcUa.NodeAttribute)
  def setAttribute(self, attribute: QOpcUa.NodeAttribute) -> None:
    """
    Calls Qt's 'void QOpcUaWriteResult::setAttribute(QOpcUa::NodeAttribute
    attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteresult.html#setAttribute

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.
    """
    #  void QOpcUaWriteResult::setAttribute(QOpcUa::NodeAttribute attribute)
    self.uglySide.call(
        'ritual_ZN17QOpcUaWriteResult12setAttributeEN6QOpcUa13NodeAttribute'
        'E',
        attribute.value,
    )

  @overload(str)
  def setIndexRange(self, indexRange: str) -> None:
    """
    Calls Qt's 'void QOpcUaWriteResult::setIndexRange(const QString
    &indexRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteresult.html#setIndexRange

    Parameters
    ----------

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaWriteResult::setIndexRange(const QString &indexRange)
    self.uglySide.call(
        'ritual_ZN17QOpcUaWriteResult13setIndexRangeERK7QString', indexRange,
    )

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void QOpcUaWriteResult::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteresult.html#setStatusCode

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaWriteResult::setStatusCode(QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN17QOpcUaWriteResult13setStatusCodeEN6QOpcUa12UaStatusCode'
        'E',
        statusCode.value,
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
    Notes what was given, for Qt's 'QOpcUaWriteResult::QOpcUaWriteResult()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteresult.html#QOpcUaWriteResult
    """
    #  QOpcUaWriteResult::QOpcUaWriteResult()
    self._noteCreation(QOpcUaWriteResult, lambda: Rituals.call(
        'ritual_ZN17QOpcUaWriteResultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaWriteResult) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaWriteResult::QOpcUaWriteResult(const QOpcUaWriteResult &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteresult.html#QOpcUaWriteResult

    Parameters
    ----------

    other : QOpcUaWriteResult
      Passed on as a value: Qt reads the C++ QOpcUaWriteResult, which stays
      Python's own.
    """
    #  QOpcUaWriteResult::QOpcUaWriteResult(const QOpcUaWriteResult &other)
    self._noteCreation(QOpcUaWriteResult, lambda: Rituals.call(
        'ritual_ZN17QOpcUaWriteResultC1ERKS_', self._valueOf(other),
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


#  Qt's 'QList<QOpcUaWriteResult>': the list of QOpcUaWriteResult, which
#  'QList[QOpcUaWriteResult]' gives. It is made here, so that there is one as
#  soon as there can be a QOpcUaWriteResult.
QList.createKind(
    QOpcUaWriteResult, 'value',
    make='ritual_list_make_QOpcUaWriteResult',
    add='ritual_list_add_QOpcUaWriteResult',
    size='ritual_list_size_QOpcUaWriteResult',
    at='ritual_list_at_QOpcUaWriteResult',
    drop='ritual_list_drop_QOpcUaWriteResult',
)
