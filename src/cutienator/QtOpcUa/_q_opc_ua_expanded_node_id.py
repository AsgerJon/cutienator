"""
QOpcUaExpandedNodeId binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaexpandednodeid.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QOpcUaExpandedNodeId(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaExpandedNodeId: a plain Python object standing
  in front of one C++ QOpcUaExpandedNodeId.

  C++ hands a QOpcUaExpandedNodeId around as a copy, so every C++
  QOpcUaExpandedNodeId behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaExpandedNodeId that has a ritual and that
  Python can call so far, 7 names in all: '__eq__', 'serverIndex',
  'setServerIndex', 'namespaceUri', 'setNamespaceUri', 'nodeId', 'setNodeId'.
  It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaExpandedNodeId &QOpcUaExpandedNodeId::operator=(const
    QOpcUaExpandedNodeId &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaExpandedNodeId::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaExpandedNodeId::~QOpcUaExpandedNodeId()': the destructor:
    Python removes its C++ QOpcUaExpandedNodeId by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaExpandedNodeId is created at the first use, not by
    'QOpcUaExpandedNodeId(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaExpandedNodeId back gives a copy the ritual
    made for Python, in a new cute QOpcUaExpandedNodeId.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaExpandedNodeId'

  #  Qt's '~QOpcUaExpandedNodeId()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaExpandedNodeId behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpcUaExpandedNodeIdD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def serverIndex(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaExpandedNodeId::serverIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#serverIndex
    """
    #  quint32 QOpcUaExpandedNodeId::serverIndex() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaExpandedNodeId11serverIndexEv',
    )

  def namespaceUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaExpandedNodeId::namespaceUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#namespaceUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaExpandedNodeId::namespaceUri() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaExpandedNodeId12namespaceUriEv',
    )

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaExpandedNodeId::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaExpandedNodeId::nodeId() const
    return self.uglySide.call('ritual_ZNK20QOpcUaExpandedNodeId6nodeIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setServerIndex(self, serverIndex: int) -> None:
    """
    Calls Qt's 'void QOpcUaExpandedNodeId::setServerIndex(quint32
    serverIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#setServerIndex

    Parameters
    ----------

    serverIndex : int
      Passed on as it is.
    """
    #  void QOpcUaExpandedNodeId::setServerIndex(quint32 serverIndex)
    self.uglySide.call(
        'ritual_ZN20QOpcUaExpandedNodeId14setServerIndexEj', serverIndex,
    )

  @overload(str)
  def setNamespaceUri(self, namespaceUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaExpandedNodeId::setNamespaceUri(const QString
    &namespaceUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#setNamespaceUri

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaExpandedNodeId::setNamespaceUri(const QString
    #      &namespaceUri)
    self.uglySide.call(
        'ritual_ZN20QOpcUaExpandedNodeId15setNamespaceUriERK7QString',
        namespaceUri,
    )

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaExpandedNodeId::setNodeId(const QString &nodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaExpandedNodeId::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN20QOpcUaExpandedNodeId9setNodeIdERK7QString', nodeId,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QOpcUaExpandedNodeId) -> bool:
    """
    Calls Qt's 'bool QOpcUaExpandedNodeId::operator==(const
    QOpcUaExpandedNodeId &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#operator==

    Parameters
    ----------

    a0 : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  bool QOpcUaExpandedNodeId::operator==(const QOpcUaExpandedNodeId &a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaExpandedNodeIdeqERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    Notes what was given, for Qt's
    'QOpcUaExpandedNodeId::QOpcUaExpandedNodeId()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#QOpcUaExpandedNodeId
    """
    #  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId()
    self._noteCreation(QOpcUaExpandedNodeId, lambda: Rituals.call(
        'ritual_ZN20QOpcUaExpandedNodeIdC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaExpandedNodeId) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QOpcUaExpandedNodeId
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#QOpcUaExpandedNodeId

    Parameters
    ----------

    a0 : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QOpcUaExpandedNodeId
    #      &a0)
    self._noteCreation(QOpcUaExpandedNodeId, lambda: Rituals.call(
        'ritual_ZN20QOpcUaExpandedNodeIdC1ERKS_', self._valueOf(a0),
    ))

  @overload(str)
  def __init__(self, nodeId: str) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QString &nodeId)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#QOpcUaExpandedNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QString &nodeId)
    self._noteCreation(QOpcUaExpandedNodeId, lambda: Rituals.call(
        'ritual_ZN20QOpcUaExpandedNodeIdC1ERK7QString', nodeId,
    ))

  @overload(str, str)
  @overload(str, str, int)
  def __init__(
      self,
      namespaceUri: str,
      nodeId: str,
      serverIndex: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QString &namespaceUri,
    const QString &nodeId, quint32 serverIndex)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaexpandednodeid.html#QOpcUaExpandedNodeId

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    serverIndex : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QString
    #      &namespaceUri, const QString &nodeId, quint32 serverIndex)
    self._noteCreation(QOpcUaExpandedNodeId, lambda: Rituals.call(
        'ritual_ZN20QOpcUaExpandedNodeIdC1ERK7QStringS2_j',
        namespaceUri, nodeId, serverIndex,
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
