"""
QOpcUaAddNodeItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaaddnodeitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaExpandedNodeId, QOpcUaNodeCreationAttributes
  from . import QOpcUaQualifiedName
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']
  QOpcUaNodeCreationAttributes = WAIT['QOpcUaNodeCreationAttributes']
  QOpcUaQualifiedName = WAIT['QOpcUaQualifiedName']


class QOpcUaAddNodeItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaAddNodeItem: a plain Python object standing in
  front of one C++ QOpcUaAddNodeItem.

  C++ hands a QOpcUaAddNodeItem around as a copy, so every C++
  QOpcUaAddNodeItem behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaAddNodeItem that has a ritual and that Python
  can call so far, 13 names in all: 'parentNodeId', 'setParentNodeId',
  'referenceTypeId', 'setReferenceTypeId', 'requestedNewNodeId',
  'setRequestedNewNodeId', 'browseName', 'setBrowseName', 'nodeClass',
  'nodeAttributes', 'setNodeAttributes', 'typeDefinition',
  'setTypeDefinition'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaAddNodeItem &QOpcUaAddNodeItem::operator=(const
    QOpcUaAddNodeItem &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaAddNodeItem::~QOpcUaAddNodeItem()': the destructor: Python
    removes its C++ QOpcUaAddNodeItem by it, and has no other use for it.
  - Qt's 'void QOpcUaAddNodeItem::setNodeClass(const QOpcUa::NodeClass
    &nodeClass)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaNodeCreationAttributes
    &QOpcUaAddNodeItem::nodeAttributesRef()': gives a type Python has no way
    to take yet.

  What to expect
  --------------

  - The C++ QOpcUaAddNodeItem is created at the first use, not by
    'QOpcUaAddNodeItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaAddNodeItem back gives a copy the ritual made
    for Python, in a new cute QOpcUaAddNodeItem.
  - Each name of Qt's QOpcUaAddNodeItem that has no cute function yet,
    'nodeAttributesRef', 'setNodeClass', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaAddNodeItem'

  #  Qt's '~QOpcUaAddNodeItem()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaAddNodeItem behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QOpcUaAddNodeItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parentNodeId(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId QOpcUaAddNodeItem::parentNodeId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#parentNodeId

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaAddNodeItem::parentNodeId() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpcUaAddNodeItem12parentNodeIdEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  def referenceTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaAddNodeItem::referenceTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#referenceTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaAddNodeItem::referenceTypeId() const
    return self.uglySide.call(
        'ritual_ZNK17QOpcUaAddNodeItem15referenceTypeIdEv',
    )

  def requestedNewNodeId(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId QOpcUaAddNodeItem::requestedNewNodeId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#requestedNewNodeId

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaAddNodeItem::requestedNewNodeId() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpcUaAddNodeItem18requestedNewNodeIdEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  def browseName(self) -> QOpcUaQualifiedName:
    """
    Calls Qt's 'QOpcUaQualifiedName QOpcUaAddNodeItem::browseName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#browseName

    Returns
    -------

    QOpcUaQualifiedName
      A new cute QOpcUaQualifiedName around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaQualifiedName QOpcUaAddNodeItem::browseName() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpcUaAddNodeItem10browseNameEv',
    )
    from . import QOpcUaQualifiedName
    return QOpcUaQualifiedName._cuteOwning(address)

  def nodeClass(self) -> QOpcUa.NodeClass:
    """
    Calls Qt's 'QOpcUa::NodeClass QOpcUaAddNodeItem::nodeClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#nodeClass

    Returns
    -------

    QOpcUa.NodeClass
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.NodeClass(number)'
      gives.
    """
    #  QOpcUa::NodeClass QOpcUaAddNodeItem::nodeClass() const
    return QOpcUa.NodeClass(self.uglySide.call(
        'ritual_ZNK17QOpcUaAddNodeItem9nodeClassEv',
    ))

  def nodeAttributes(self) -> QOpcUaNodeCreationAttributes:
    """
    Calls Qt's 'QOpcUaNodeCreationAttributes
    QOpcUaAddNodeItem::nodeAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#nodeAttributes

    Returns
    -------

    QOpcUaNodeCreationAttributes
      A new cute QOpcUaNodeCreationAttributes around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaNodeCreationAttributes QOpcUaAddNodeItem::nodeAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpcUaAddNodeItem14nodeAttributesEv',
    )
    from . import QOpcUaNodeCreationAttributes
    return QOpcUaNodeCreationAttributes._cuteOwning(address)

  def typeDefinition(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId QOpcUaAddNodeItem::typeDefinition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#typeDefinition

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaAddNodeItem::typeDefinition() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpcUaAddNodeItem14typeDefinitionEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUaExpandedNodeId)
  def setParentNodeId(self, parentNodeId: QOpcUaExpandedNodeId) -> None:
    """
    Calls Qt's 'void QOpcUaAddNodeItem::setParentNodeId(const
    QOpcUaExpandedNodeId &parentNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#setParentNodeId

    Parameters
    ----------

    parentNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaAddNodeItem::setParentNodeId(const QOpcUaExpandedNodeId
    #      &parentNodeId)
    self.uglySide.call(
        'ritual_ZN17QOpcUaAddNodeItem15setParentNodeIdERK20QOpcUaExpandedNo'
        'deId',
        self._valueOf(parentNodeId),
    )

  @overload(str)
  def setReferenceTypeId(self, referenceTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaAddNodeItem::setReferenceTypeId(const QString
    &referenceTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#setReferenceTypeId

    Parameters
    ----------

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAddNodeItem::setReferenceTypeId(const QString
    #      &referenceTypeId)
    self.uglySide.call(
        'ritual_ZN17QOpcUaAddNodeItem18setReferenceTypeIdERK7QString',
        referenceTypeId,
    )

  @overload(QOpcUaExpandedNodeId)
  def setRequestedNewNodeId(
      self,
      requestedNewNodeId: QOpcUaExpandedNodeId,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaAddNodeItem::setRequestedNewNodeId(const
    QOpcUaExpandedNodeId &requestedNewNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#setRequestedNewNodeId

    Parameters
    ----------

    requestedNewNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaAddNodeItem::setRequestedNewNodeId(const
    #      QOpcUaExpandedNodeId &requestedNewNodeId)
    self.uglySide.call(
        'ritual_ZN17QOpcUaAddNodeItem21setRequestedNewNodeIdERK20QOpcUaExpa'
        'ndedNodeId',
        self._valueOf(requestedNewNodeId),
    )

  @overload(QOpcUaQualifiedName)
  def setBrowseName(self, browseName: QOpcUaQualifiedName) -> None:
    """
    Calls Qt's 'void QOpcUaAddNodeItem::setBrowseName(const
    QOpcUaQualifiedName &browseName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#setBrowseName

    Parameters
    ----------

    browseName : QOpcUaQualifiedName
      Passed on as a value: Qt reads the C++ QOpcUaQualifiedName, which stays
      Python's own.
    """
    #  void QOpcUaAddNodeItem::setBrowseName(const QOpcUaQualifiedName
    #      &browseName)
    self.uglySide.call(
        'ritual_ZN17QOpcUaAddNodeItem13setBrowseNameERK19QOpcUaQualifiedNam'
        'e',
        self._valueOf(browseName),
    )

  @overload(QOpcUaNodeCreationAttributes)
  def setNodeAttributes(
      self,
      nodeAttributes: QOpcUaNodeCreationAttributes,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaAddNodeItem::setNodeAttributes(const
    QOpcUaNodeCreationAttributes &nodeAttributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#setNodeAttributes

    Parameters
    ----------

    nodeAttributes : QOpcUaNodeCreationAttributes
      Passed on as a value: Qt reads the C++ QOpcUaNodeCreationAttributes,
      which stays Python's own.
    """
    #  void QOpcUaAddNodeItem::setNodeAttributes(const
    #      QOpcUaNodeCreationAttributes &nodeAttributes)
    self.uglySide.call(
        'ritual_ZN17QOpcUaAddNodeItem17setNodeAttributesERK28QOpcUaNodeCrea'
        'tionAttributes',
        self._valueOf(nodeAttributes),
    )

  @overload(QOpcUaExpandedNodeId)
  def setTypeDefinition(self, typeDefinition: QOpcUaExpandedNodeId) -> None:
    """
    Calls Qt's 'void QOpcUaAddNodeItem::setTypeDefinition(const
    QOpcUaExpandedNodeId &typeDefinition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#setTypeDefinition

    Parameters
    ----------

    typeDefinition : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaAddNodeItem::setTypeDefinition(const QOpcUaExpandedNodeId
    #      &typeDefinition)
    self.uglySide.call(
        'ritual_ZN17QOpcUaAddNodeItem17setTypeDefinitionERK20QOpcUaExpanded'
        'NodeId',
        self._valueOf(typeDefinition),
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
    Notes what was given, for Qt's 'QOpcUaAddNodeItem::QOpcUaAddNodeItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#QOpcUaAddNodeItem
    """
    #  QOpcUaAddNodeItem::QOpcUaAddNodeItem()
    self._noteCreation(QOpcUaAddNodeItem, lambda: Rituals.call(
        'ritual_ZN17QOpcUaAddNodeItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaAddNodeItem) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaAddNodeItem::QOpcUaAddNodeItem(const QOpcUaAddNodeItem &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaddnodeitem.html#QOpcUaAddNodeItem

    Parameters
    ----------

    a0 : QOpcUaAddNodeItem
      Passed on as a value: Qt reads the C++ QOpcUaAddNodeItem, which stays
      Python's own.
    """
    #  QOpcUaAddNodeItem::QOpcUaAddNodeItem(const QOpcUaAddNodeItem &a0)
    self._noteCreation(QOpcUaAddNodeItem, lambda: Rituals.call(
        'ritual_ZN17QOpcUaAddNodeItemC1ERKS_', self._valueOf(a0),
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
  def nodeAttributesRef(*__, **_) -> Never:
    """
    Qt's 'QOpcUaNodeCreationAttributes
    &QOpcUaAddNodeItem::nodeAttributesRef()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaAddNodeItem.nodeAttributesRef' has no cute function yet. "
        "Qt's 'QOpcUaNodeCreationAttributes "
        "&QOpcUaAddNodeItem::nodeAttributesRef()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def setNodeClass(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaAddNodeItem::setNodeClass(const QOpcUa::NodeClass
    &nodeClass)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaAddNodeItem.setNodeClass' has no cute function yet. Qt's "
        "'void QOpcUaAddNodeItem::setNodeClass(const QOpcUa::NodeClass "
        "&nodeClass)': takes a type Python has no way to hand over yet.")
