"""
QOpcUaAddReferenceItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaaddreferenceitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QOpcUaExpandedNodeId
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']


class QOpcUaAddReferenceItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaAddReferenceItem: a plain Python object
  standing in front of one C++ QOpcUaAddReferenceItem.

  C++ hands a QOpcUaAddReferenceItem around as a copy, so every C++
  QOpcUaAddReferenceItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaAddReferenceItem that has a ritual and that
  Python can call so far, 12 names in all: 'sourceNodeId', 'setSourceNodeId',
  'referenceTypeId', 'setReferenceTypeId', 'isForwardReference',
  'setIsForwardReference', 'targetNodeId', 'setTargetNodeId',
  'targetNodeClass', 'setTargetNodeClass', 'targetServerUri',
  'setTargetServerUri'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaAddReferenceItem &QOpcUaAddReferenceItem::operator=(const
    QOpcUaAddReferenceItem &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaAddReferenceItem::~QOpcUaAddReferenceItem()': the destructor:
    Python removes its C++ QOpcUaAddReferenceItem by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaAddReferenceItem is created at the first use, not by
    'QOpcUaAddReferenceItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaAddReferenceItem back gives a copy the ritual
    made for Python, in a new cute QOpcUaAddReferenceItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaAddReferenceItem'

  #  Qt's '~QOpcUaAddReferenceItem()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaAddReferenceItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QOpcUaAddReferenceItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sourceNodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaAddReferenceItem::sourceNodeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#sourceNodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaAddReferenceItem::sourceNodeId() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaAddReferenceItem12sourceNodeIdEv',
    )

  def referenceTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaAddReferenceItem::referenceTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#referenceTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaAddReferenceItem::referenceTypeId() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaAddReferenceItem15referenceTypeIdEv',
    )

  def isForwardReference(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaAddReferenceItem::isForwardReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#isForwardReference
    """
    #  bool QOpcUaAddReferenceItem::isForwardReference() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaAddReferenceItem18isForwardReferenceEv',
    )

  def targetNodeId(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId QOpcUaAddReferenceItem::targetNodeId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#targetNodeId

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaAddReferenceItem::targetNodeId() const
    address = self.uglySide.call(
        'ritual_ZNK22QOpcUaAddReferenceItem12targetNodeIdEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  def targetNodeClass(self) -> QOpcUa.NodeClass:
    """
    Calls Qt's 'QOpcUa::NodeClass QOpcUaAddReferenceItem::targetNodeClass()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#targetNodeClass

    Returns
    -------

    QOpcUa.NodeClass
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.NodeClass(number)'
      gives.
    """
    #  QOpcUa::NodeClass QOpcUaAddReferenceItem::targetNodeClass() const
    return QOpcUa.NodeClass(self.uglySide.call(
        'ritual_ZNK22QOpcUaAddReferenceItem15targetNodeClassEv',
    ))

  def targetServerUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaAddReferenceItem::targetServerUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#targetServerUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaAddReferenceItem::targetServerUri() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaAddReferenceItem15targetServerUriEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSourceNodeId(self, sourceNodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaAddReferenceItem::setSourceNodeId(const QString
    &sourceNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#setSourceNodeId

    Parameters
    ----------

    sourceNodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAddReferenceItem::setSourceNodeId(const QString
    #      &sourceNodeId)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAddReferenceItem15setSourceNodeIdERK7QString',
        sourceNodeId,
    )

  @overload(str)
  def setReferenceTypeId(self, referenceTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaAddReferenceItem::setReferenceTypeId(const QString
    &referenceTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#setReferenceTypeId

    Parameters
    ----------

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAddReferenceItem::setReferenceTypeId(const QString
    #      &referenceTypeId)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAddReferenceItem18setReferenceTypeIdERK7QString',
        referenceTypeId,
    )

  @overload(bool)
  def setIsForwardReference(self, isForwardReference: bool) -> None:
    """
    Calls Qt's 'void QOpcUaAddReferenceItem::setIsForwardReference(bool
    isForwardReference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#setIsForwardReference

    Parameters
    ----------

    isForwardReference : bool
      Passed on as it is.
    """
    #  void QOpcUaAddReferenceItem::setIsForwardReference(bool
    #      isForwardReference)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAddReferenceItem21setIsForwardReferenceEb',
        isForwardReference,
    )

  @overload(QOpcUaExpandedNodeId)
  def setTargetNodeId(self, targetNodeId: QOpcUaExpandedNodeId) -> None:
    """
    Calls Qt's 'void QOpcUaAddReferenceItem::setTargetNodeId(const
    QOpcUaExpandedNodeId &targetNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#setTargetNodeId

    Parameters
    ----------

    targetNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaAddReferenceItem::setTargetNodeId(const
    #      QOpcUaExpandedNodeId &targetNodeId)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAddReferenceItem15setTargetNodeIdERK20QOpcUaExpan'
        'dedNodeId',
        self._valueOf(targetNodeId),
    )

  @overload(QOpcUa.NodeClass)
  def setTargetNodeClass(self, targetNodeClass: QOpcUa.NodeClass) -> None:
    """
    Calls Qt's 'void
    QOpcUaAddReferenceItem::setTargetNodeClass(QOpcUa::NodeClass
    targetNodeClass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#setTargetNodeClass

    Parameters
    ----------

    targetNodeClass : QOpcUa.NodeClass
      Passed on as its number.
    """
    #  void QOpcUaAddReferenceItem::setTargetNodeClass(QOpcUa::NodeClass
    #      targetNodeClass)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAddReferenceItem18setTargetNodeClassEN6QOpcUa9Nod'
        'eClassE',
        targetNodeClass.value,
    )

  @overload(str)
  def setTargetServerUri(self, targetServerUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaAddReferenceItem::setTargetServerUri(const QString
    &targetServerUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#setTargetServerUri

    Parameters
    ----------

    targetServerUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAddReferenceItem::setTargetServerUri(const QString
    #      &targetServerUri)
    self.uglySide.call(
        'ritual_ZN22QOpcUaAddReferenceItem18setTargetServerUriERK7QString',
        targetServerUri,
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
    Notes what was given, for Qt's
    'QOpcUaAddReferenceItem::QOpcUaAddReferenceItem()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#QOpcUaAddReferenceItem
    """
    #  QOpcUaAddReferenceItem::QOpcUaAddReferenceItem()
    self._noteCreation(QOpcUaAddReferenceItem, lambda: Rituals.call(
        'ritual_ZN22QOpcUaAddReferenceItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaAddReferenceItem) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaAddReferenceItem::QOpcUaAddReferenceItem(const
    QOpcUaAddReferenceItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddreferenceitem.html#QOpcUaAddReferenceItem

    Parameters
    ----------

    other : QOpcUaAddReferenceItem
      Passed on as a value: Qt reads the C++ QOpcUaAddReferenceItem, which
      stays Python's own.
    """
    #  QOpcUaAddReferenceItem::QOpcUaAddReferenceItem(const
    #      QOpcUaAddReferenceItem &other)
    self._noteCreation(QOpcUaAddReferenceItem, lambda: Rituals.call(
        'ritual_ZN22QOpcUaAddReferenceItemC1ERKS_', self._valueOf(other),
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
