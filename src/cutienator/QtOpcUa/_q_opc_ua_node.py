"""
QOpcUaNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuanode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QOpcUa, QOpcUaMonitoringParameters

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QMetaObject, QVariant
  from . import QOpcUaBrowsePathTarget, QOpcUaBrowseRequest, QOpcUaClient
  from . import QOpcUaHistoryReadResponse, QOpcUaNodeImpl, QOpcUaNodePrivate
  from . import QOpcUaReferenceDescription, QOpcUaRelativePathElement
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QOpcUaBrowsePathTarget = WAIT['QOpcUaBrowsePathTarget']
  QOpcUaBrowseRequest = WAIT['QOpcUaBrowseRequest']
  QOpcUaClient = WAIT['QOpcUaClient']
  QOpcUaNodeImpl = WAIT['QOpcUaNodeImpl']
  QOpcUaReferenceDescription = WAIT['QOpcUaReferenceDescription']
  QOpcUaRelativePathElement = WAIT['QOpcUaRelativePathElement']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaNode(QObject):
  """
  The cute side of Qt's QOpcUaNode: a plain Python object standing in front
  of one C++ QOpcUaNode.

  It is built on the cute 'QObject', as Qt's QOpcUaNode is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaNode that has a ritual and that Python can
  call so far, 41 names in all: 'metaObject', 'tr', 'd_func',
  'mandatoryBaseAttributes', 'allBaseAttributes', 'readAttributes',
  'readAttributeRange', 'readValueAttribute', 'attribute', 'valueAttribute',
  'attributeError', 'valueAttributeError', 'sourceTimestamp',
  'serverTimestamp', 'writeAttribute', 'writeAttributeRange',
  'writeValueAttribute', 'enableMonitoring', 'disableMonitoring',
  'modifyMonitoring', 'monitoringStatus', 'modifyEventFilter',
  'modifyDataChangeFilter', 'browseChildren', 'nodeId', 'client',
  'resolveBrowsePath', 'browse', 'readHistoryRaw', 'attributeRead',
  'attributeWritten', 'dataChangeOccurred', 'attributeUpdated',
  'valueAttributeUpdated', 'eventOccurred', 'monitoringStatusChanged',
  'enableMonitoringFinished', 'disableMonitoringFinished',
  'methodCallFinished', 'browseFinished', 'resolveBrowsePathFinished'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaNode::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpcUaNode::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QOpcUaNodePrivate *QOpcUaNode::d_func() const': takes in
    Python what 'QOpcUaNodePrivate *QOpcUaNode::d_func()' takes.
  - Qt's 'QOpcUaNode::~QOpcUaNode()': the destructor: Python never removes a
    C++ QOpcUaNode.
  - Qt's 'bool QOpcUaNode::writeAttributes(const AttributeMap &toWrite,
    QOpcUa::Types valueAttributeType)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QOpcUaNode::callMethod(const QString &methodNodeId, const
    QList<QOpcUa::TypedVariant> &args)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryEvents(const
    QDateTime &startTime, const QDateTime &endTime,
    QOpcUaMonitoringParameters::EventFilter &filter, quint32 numValues)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 54 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpcUaNode is created at the first use, not by 'QOpcUaNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaNode.
  - Qt tells when it has removed the C++ QOpcUaNode. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QOpcUaNode that has no cute function yet, 'callMethod',
    'readHistoryEvents', 'writeAttributes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QOpcUaNode::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QOpcUaNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def mandatoryBaseAttributes() -> QOpcUa.NodeAttributes:
    """
    Calls Qt's 'QOpcUa::NodeAttributes
    QOpcUaNode::mandatoryBaseAttributes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#mandatoryBaseAttributes

    Returns
    -------

    QOpcUa.NodeAttributes
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::NodeAttributes QOpcUaNode::mandatoryBaseAttributes()
    return QOpcUa.NodeAttributes(Rituals.call(
        'ritual_ZN10QOpcUaNode23mandatoryBaseAttributesEv',
    ))

  @staticmethod
  def allBaseAttributes() -> QOpcUa.NodeAttributes:
    """
    Calls Qt's 'QOpcUa::NodeAttributes QOpcUaNode::allBaseAttributes()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#allBaseAttributes

    Returns
    -------

    QOpcUa.NodeAttributes
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::NodeAttributes QOpcUaNode::allBaseAttributes()
    return QOpcUa.NodeAttributes(Rituals.call(
        'ritual_ZN10QOpcUaNode17allBaseAttributesEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaNode'

  #  A C++ QOpcUaNode Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaNode::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QOpcUaNode10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QOpcUa.NodeAttribute)
  def attribute(self, attribute: QOpcUa.NodeAttribute) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaNode::attribute(QOpcUa::NodeAttribute
    attribute) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#attribute

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaNode::attribute(QOpcUa::NodeAttribute attribute) const
    address = self.uglySide.call(
        'ritual_ZNK10QOpcUaNode9attributeEN6QOpcUa13NodeAttributeE',
        attribute.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def valueAttribute(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaNode::valueAttribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#valueAttribute

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaNode::valueAttribute() const
    address = self.uglySide.call('ritual_ZNK10QOpcUaNode14valueAttributeEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QOpcUa.NodeAttribute)
  def attributeError(
      self,
      attribute: QOpcUa.NodeAttribute,
  ) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode
    QOpcUaNode::attributeError(QOpcUa::NodeAttribute attribute) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#attributeError

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaNode::attributeError(QOpcUa::NodeAttribute
    #      attribute) const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK10QOpcUaNode14attributeErrorEN6QOpcUa13NodeAttributeE',
        attribute.value,
    ))

  def valueAttributeError(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaNode::valueAttributeError()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#valueAttributeError

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaNode::valueAttributeError() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK10QOpcUaNode19valueAttributeErrorEv',
    ))

  @overload(QOpcUa.NodeAttribute)
  def sourceTimestamp(self, attribute: QOpcUa.NodeAttribute) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaNode::sourceTimestamp(QOpcUa::NodeAttribute
    attribute) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#sourceTimestamp

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaNode::sourceTimestamp(QOpcUa::NodeAttribute attribute)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QOpcUaNode15sourceTimestampEN6QOpcUa13NodeAttributeE',
        attribute.value,
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QOpcUa.NodeAttribute)
  def serverTimestamp(self, attribute: QOpcUa.NodeAttribute) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaNode::serverTimestamp(QOpcUa::NodeAttribute
    attribute) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#serverTimestamp

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaNode::serverTimestamp(QOpcUa::NodeAttribute attribute)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QOpcUaNode15serverTimestampEN6QOpcUa13NodeAttributeE',
        attribute.value,
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaNode::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaNode::nodeId() const
    return self.uglySide.call('ritual_ZNK10QOpcUaNode6nodeIdEv')

  def client(self) -> Optional[QOpcUaClient]:
    """
    Calls Qt's 'QOpcUaClient *QOpcUaNode::client() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#client

    Returns
    -------

    Optional[QOpcUaClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaClient *QOpcUaNode::client() const
    address = self.uglySide.call('ritual_ZNK10QOpcUaNode6clientEv')
    from . import QOpcUaClient
    return QOpcUaClient._cuteAt(address)

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

  @overload(QOpcUaNodeImpl, QOpcUaClient)
  @overload(QOpcUaNodeImpl, NoneType)
  @overload(NoneType, QOpcUaClient)
  @overload(NoneType, NoneType)
  @overload(QOpcUaNodeImpl, QOpcUaClient, QObject)
  @overload(QOpcUaNodeImpl, QOpcUaClient, NoneType)
  @overload(QOpcUaNodeImpl, NoneType, QObject)
  @overload(QOpcUaNodeImpl, NoneType, NoneType)
  @overload(NoneType, QOpcUaClient, QObject)
  @overload(NoneType, QOpcUaClient, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      impl: Optional[QOpcUaNodeImpl],
      client: Optional[QOpcUaClient],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaNode::QOpcUaNode(QOpcUaNodeImpl
    *impl, QOpcUaClient *client, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#QOpcUaNode

    Parameters
    ----------

    impl : Optional[QOpcUaNodeImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    client : Optional[QOpcUaClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpcUaNode::QOpcUaNode(QOpcUaNodeImpl *impl, QOpcUaClient *client,
    #      QObject *parent)
    self._noteCreation(QOpcUaNode, lambda: Rituals.call(
        'ritual_ZN10QOpcUaNodeC1EP14QOpcUaNodeImplP12QOpcUaClientP7QObject',
        self._addressOf(impl), self._addressOf(client),
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QOpcUaNodePrivate]:
    """
    Calls Qt's 'QOpcUaNodePrivate *QOpcUaNode::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#d_func

    Returns
    -------

    Optional[QOpcUaNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaNodePrivate *QOpcUaNode::d_func()
    address = self.uglySide.call('ritual_ZN10QOpcUaNode6d_funcEv')
    from . import QOpcUaNodePrivate
    return QOpcUaNodePrivate._cuteAt(address)

  @overload(QOpcUa.NodeAttributes)
  def readAttributes(self, attributes: QOpcUa.NodeAttributes) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::readAttributes(QOpcUa::NodeAttributes
    attributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#readAttributes

    Parameters
    ----------

    attributes : QOpcUa.NodeAttributes
      Passed on as its number.
    """
    #  bool QOpcUaNode::readAttributes(QOpcUa::NodeAttributes attributes)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode14readAttributesE6QFlagsIN6QOpcUa13NodeAttrib'
        'uteEE',
        attributes.value,
    )

  @overload(QOpcUa.NodeAttribute, str)
  def readAttributeRange(
      self,
      attribute: QOpcUa.NodeAttribute,
      indexRange: str,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::readAttributeRange(QOpcUa::NodeAttribute
    attribute, const QString &indexRange)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#readAttributeRange

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpcUaNode::readAttributeRange(QOpcUa::NodeAttribute attribute,
    #      const QString &indexRange)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode18readAttributeRangeEN6QOpcUa13NodeAttributeE'
        'RK7QString',
        attribute.value, indexRange,
    )

  def readValueAttribute(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::readValueAttribute()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#readValueAttribute
    """
    #  bool QOpcUaNode::readValueAttribute()
    return self.uglySide.call('ritual_ZN10QOpcUaNode18readValueAttributeEv')

  @overload(QOpcUa.NodeAttribute, QVariant)
  @overload(QOpcUa.NodeAttribute, QVariant, QOpcUa.Types)
  def writeAttribute(
      self,
      attribute: QOpcUa.NodeAttribute,
      value: QVariant,
      type: QOpcUa.Types = QOpcUa.Types.Undefined,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::writeAttribute(QOpcUa::NodeAttribute
    attribute, const QVariant &value, QOpcUa::Types type)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#writeAttribute

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QOpcUa.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.Types.Undefined.
    """
    #  bool QOpcUaNode::writeAttribute(QOpcUa::NodeAttribute attribute, const
    #      QVariant &value, QOpcUa::Types type)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode14writeAttributeEN6QOpcUa13NodeAttributeERK8Q'
        'VariantNS0_5TypesE',
        attribute.value, self._valueOf(value), type.value,
    )

  @overload(QOpcUa.NodeAttribute, QVariant, str)
  @overload(QOpcUa.NodeAttribute, QVariant, str, QOpcUa.Types)
  def writeAttributeRange(
      self,
      attribute: QOpcUa.NodeAttribute,
      value: QVariant,
      indexRange: str,
      type: QOpcUa.Types = QOpcUa.Types.Undefined,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::writeAttributeRange(QOpcUa::NodeAttribute
    attribute, const QVariant &value, const QString &indexRange,
    QOpcUa::Types type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#writeAttributeRange

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    indexRange : str
      Passed on as it is: a QString is made of it for the call.

    type : QOpcUa.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.Types.Undefined.
    """
    #  bool QOpcUaNode::writeAttributeRange(QOpcUa::NodeAttribute attribute,
    #      const QVariant &value, const QString &indexRange, QOpcUa::Types
    #      type)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode19writeAttributeRangeEN6QOpcUa13NodeAttribute'
        'ERK8QVariantRK7QStringNS0_5TypesE',
        attribute.value, self._valueOf(value), indexRange, type.value,
    )

  @overload(QVariant)
  @overload(QVariant, QOpcUa.Types)
  def writeValueAttribute(
      self,
      value: QVariant,
      type: QOpcUa.Types = QOpcUa.Types.Undefined,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::writeValueAttribute(const QVariant &value,
    QOpcUa::Types type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#writeValueAttribute

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QOpcUa.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.Types.Undefined.
    """
    #  bool QOpcUaNode::writeValueAttribute(const QVariant &value,
    #      QOpcUa::Types type)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode19writeValueAttributeERK8QVariantN6QOpcUa5Typ'
        'esE',
        self._valueOf(value), type.value,
    )

  @overload(QOpcUa.NodeAttributes, QOpcUaMonitoringParameters)
  def enableMonitoring(
      self,
      attr: QOpcUa.NodeAttributes,
      settings: QOpcUaMonitoringParameters,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::enableMonitoring(QOpcUa::NodeAttributes
    attr, const QOpcUaMonitoringParameters &settings)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#enableMonitoring

    Parameters
    ----------

    attr : QOpcUa.NodeAttributes
      Passed on as its number.

    settings : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  bool QOpcUaNode::enableMonitoring(QOpcUa::NodeAttributes attr, const
    #      QOpcUaMonitoringParameters &settings)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode16enableMonitoringE6QFlagsIN6QOpcUa13NodeAttr'
        'ibuteEERK26QOpcUaMonitoringParameters',
        attr.value, self._valueOf(settings),
    )

  @overload(QOpcUa.NodeAttributes)
  def disableMonitoring(self, attr: QOpcUa.NodeAttributes) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::disableMonitoring(QOpcUa::NodeAttributes
    attr)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#disableMonitoring

    Parameters
    ----------

    attr : QOpcUa.NodeAttributes
      Passed on as its number.
    """
    #  bool QOpcUaNode::disableMonitoring(QOpcUa::NodeAttributes attr)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode17disableMonitoringE6QFlagsIN6QOpcUa13NodeAtt'
        'ributeEE',
        attr.value,
    )

  @overload(
      QOpcUa.NodeAttribute, QOpcUaMonitoringParameters.Parameter, QVariant,
  )
  def modifyMonitoring(
      self,
      attr: QOpcUa.NodeAttribute,
      item: QOpcUaMonitoringParameters.Parameter,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::modifyMonitoring(QOpcUa::NodeAttribute attr,
    QOpcUaMonitoringParameters::Parameter item, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#modifyMonitoring

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    item : QOpcUaMonitoringParameters.Parameter
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QOpcUaNode::modifyMonitoring(QOpcUa::NodeAttribute attr,
    #      QOpcUaMonitoringParameters::Parameter item, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode16modifyMonitoringEN6QOpcUa13NodeAttributeEN2'
        '6QOpcUaMonitoringParameters9ParameterERK8QVariant',
        attr.value, item.value, self._valueOf(value),
    )

  @overload(QOpcUa.NodeAttribute)
  def monitoringStatus(
      self,
      attr: QOpcUa.NodeAttribute,
  ) -> QOpcUaMonitoringParameters:
    """
    Calls Qt's 'QOpcUaMonitoringParameters
    QOpcUaNode::monitoringStatus(QOpcUa::NodeAttribute attr)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#monitoringStatus

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    Returns
    -------

    QOpcUaMonitoringParameters
      A new cute QOpcUaMonitoringParameters around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaMonitoringParameters
    #      QOpcUaNode::monitoringStatus(QOpcUa::NodeAttribute attr)
    address = self.uglySide.call(
        'ritual_ZN10QOpcUaNode16monitoringStatusEN6QOpcUa13NodeAttributeE',
        attr.value,
    )
    return QOpcUaMonitoringParameters._cuteOwning(address)

  @overload(QOpcUaMonitoringParameters.EventFilter)
  def modifyEventFilter(
      self,
      eventFilter: QOpcUaMonitoringParameters.EventFilter,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::modifyEventFilter(const
    QOpcUaMonitoringParameters::EventFilter &eventFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#modifyEventFilter

    Parameters
    ----------

    eventFilter : QOpcUaMonitoringParameters.EventFilter
      Passed on as a value: Qt reads the C++
      QOpcUaMonitoringParameters::EventFilter, which stays Python's own.
    """
    #  bool QOpcUaNode::modifyEventFilter(const
    #      QOpcUaMonitoringParameters::EventFilter &eventFilter)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode17modifyEventFilterERKN26QOpcUaMonitoringPara'
        'meters11EventFilterE',
        self._valueOf(eventFilter),
    )

  @overload(
      QOpcUa.NodeAttribute, QOpcUaMonitoringParameters.DataChangeFilter,
  )
  def modifyDataChangeFilter(
      self,
      attr: QOpcUa.NodeAttribute,
      filter: QOpcUaMonitoringParameters.DataChangeFilter,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::modifyDataChangeFilter(QOpcUa::NodeAttribute
    attr, const QOpcUaMonitoringParameters::DataChangeFilter &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#modifyDataChangeFilter

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    filter : QOpcUaMonitoringParameters.DataChangeFilter
      Passed on as a value: Qt reads the C++
      QOpcUaMonitoringParameters::DataChangeFilter, which stays Python's own.
    """
    #  bool QOpcUaNode::modifyDataChangeFilter(QOpcUa::NodeAttribute attr,
    #      const QOpcUaMonitoringParameters::DataChangeFilter &filter)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode22modifyDataChangeFilterEN6QOpcUa13NodeAttrib'
        'uteERKN26QOpcUaMonitoringParameters16DataChangeFilterE',
        attr.value, self._valueOf(filter),
    )

  @overload()
  @overload(QOpcUa.ReferenceTypeId)
  @overload(QOpcUa.ReferenceTypeId, QOpcUa.NodeClasses)
  def browseChildren(
      self,
      referenceType: QOpcUa.ReferenceTypeId = (
          QOpcUa.ReferenceTypeId.HierarchicalReferences),
      nodeClassMask: QOpcUa.NodeClasses = QOpcUa.NodeClasses.Undefined,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::browseChildren(QOpcUa::ReferenceTypeId
    referenceType, QOpcUa::NodeClasses nodeClassMask)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#browseChildren

    Parameters
    ----------

    referenceType : QOpcUa.ReferenceTypeId
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.ReferenceTypeId.HierarchicalReferences.

    nodeClassMask : QOpcUa.NodeClasses
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.NodeClasses.Undefined.
    """
    #  bool QOpcUaNode::browseChildren(QOpcUa::ReferenceTypeId referenceType,
    #      QOpcUa::NodeClasses nodeClassMask)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode14browseChildrenEN6QOpcUa15ReferenceTypeIdE6Q'
        'FlagsINS0_9NodeClassEE',
        referenceType.value, nodeClassMask.value,
    )

  @overload(QList[QOpcUaRelativePathElement])
  def resolveBrowsePath(
      self,
      path: QList[QOpcUaRelativePathElement],
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::resolveBrowsePath(const
    QList<QOpcUaRelativePathElement> &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#resolveBrowsePath

    Parameters
    ----------

    path : QList[QOpcUaRelativePathElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaNode::resolveBrowsePath(const
    #      QList<QOpcUaRelativePathElement> &path)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode17resolveBrowsePathERK5QListI25QOpcUaRelative'
        'PathElementE',
        self._valueOf(path),
    )

  @overload(QOpcUaBrowseRequest)
  def browse(self, request: QOpcUaBrowseRequest) -> bool:
    """
    Calls Qt's 'bool QOpcUaNode::browse(const QOpcUaBrowseRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#browse

    Parameters
    ----------

    request : QOpcUaBrowseRequest
      Passed on as a value: Qt reads the C++ QOpcUaBrowseRequest, which stays
      Python's own.
    """
    #  bool QOpcUaNode::browse(const QOpcUaBrowseRequest &request)
    return self.uglySide.call(
        'ritual_ZN10QOpcUaNode6browseERK19QOpcUaBrowseRequest',
        self._valueOf(request),
    )

  @overload(QDateTime, QDateTime, int, bool)
  def readHistoryRaw(
      self,
      startTime: QDateTime,
      endTime: QDateTime,
      numValues: int,
      returnBounds: bool,
  ) -> Optional[QOpcUaHistoryReadResponse]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryRaw(const
    QDateTime &startTime, const QDateTime &endTime, quint32 numValues, bool
    returnBounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#readHistoryRaw

    Parameters
    ----------

    startTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    endTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    numValues : int
      Passed on as it is.

    returnBounds : bool
      Passed on as it is.

    Returns
    -------

    Optional[QOpcUaHistoryReadResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryRaw(const QDateTime
    #      &startTime, const QDateTime &endTime, quint32 numValues, bool
    #      returnBounds)
    address = self.uglySide.call(
        'ritual_ZN10QOpcUaNode14readHistoryRawERK9QDateTimeS2_jb',
        self._valueOf(startTime), self._valueOf(endTime), numValues,
        returnBounds,
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)

  @overload(QDateTime, QDateTime, int, bool, QOpcUa.TimestampsToReturn)
  def readHistoryRaw(
      self,
      startTime: QDateTime,
      endTime: QDateTime,
      numValues: int,
      returnBounds: bool,
      timestampsToReturn: QOpcUa.TimestampsToReturn,
  ) -> Optional[QOpcUaHistoryReadResponse]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryRaw(const
    QDateTime &startTime, const QDateTime &endTime, quint32 numValues, bool
    returnBounds, QOpcUa::TimestampsToReturn timestampsToReturn)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#readHistoryRaw

    Parameters
    ----------

    startTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    endTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    numValues : int
      Passed on as it is.

    returnBounds : bool
      Passed on as it is.

    timestampsToReturn : QOpcUa.TimestampsToReturn
      Passed on as its number.

    Returns
    -------

    Optional[QOpcUaHistoryReadResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryRaw(const QDateTime
    #      &startTime, const QDateTime &endTime, quint32 numValues, bool
    #      returnBounds, QOpcUa::TimestampsToReturn timestampsToReturn)
    address = self.uglySide.call(
        'ritual_ZN10QOpcUaNode14readHistoryRawERK9QDateTimeS2_jbN6QOpcUa18T'
        'imestampsToReturnE',
        self._valueOf(startTime), self._valueOf(endTime), numValues,
        returnBounds, timestampsToReturn.value,
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)

  @overload(QOpcUa.NodeAttributes)
  def attributeRead(self, attributes: QOpcUa.NodeAttributes) -> None:
    """
    Calls Qt's 'void QOpcUaNode::attributeRead(QOpcUa::NodeAttributes
    attributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#attributeRead

    Parameters
    ----------

    attributes : QOpcUa.NodeAttributes
      Passed on as its number.
    """
    #  void QOpcUaNode::attributeRead(QOpcUa::NodeAttributes attributes)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode13attributeReadE6QFlagsIN6QOpcUa13NodeAttribu'
        'teEE',
        attributes.value,
    )

  @overload(QOpcUa.NodeAttribute, QOpcUa.UaStatusCode)
  def attributeWritten(
      self,
      attribute: QOpcUa.NodeAttribute,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNode::attributeWritten(QOpcUa::NodeAttribute
    attribute, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#attributeWritten

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNode::attributeWritten(QOpcUa::NodeAttribute attribute,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode16attributeWrittenEN6QOpcUa13NodeAttributeENS'
        '0_12UaStatusCodeE',
        attribute.value, statusCode.value,
    )

  @overload(QOpcUa.NodeAttribute, QVariant)
  def dataChangeOccurred(
      self,
      attr: QOpcUa.NodeAttribute,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNode::dataChangeOccurred(QOpcUa::NodeAttribute
    attr, QVariant value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#dataChangeOccurred

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaNode::dataChangeOccurred(QOpcUa::NodeAttribute attr,
    #      QVariant value)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode18dataChangeOccurredEN6QOpcUa13NodeAttributeE'
        '8QVariant',
        attr.value, self._valueOf(value),
    )

  @overload(QOpcUa.NodeAttribute, QVariant)
  def attributeUpdated(
      self,
      attr: QOpcUa.NodeAttribute,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNode::attributeUpdated(QOpcUa::NodeAttribute attr,
    QVariant value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#attributeUpdated

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaNode::attributeUpdated(QOpcUa::NodeAttribute attr, QVariant
    #      value)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode16attributeUpdatedEN6QOpcUa13NodeAttributeE8Q'
        'Variant',
        attr.value, self._valueOf(value),
    )

  @overload(QVariant)
  def valueAttributeUpdated(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QOpcUaNode::valueAttributeUpdated(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#valueAttributeUpdated

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaNode::valueAttributeUpdated(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode21valueAttributeUpdatedERK8QVariant',
        self._valueOf(value),
    )

  @overload(QList[QVariant])
  def eventOccurred(self, eventFields: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QOpcUaNode::eventOccurred(QVariantList eventFields)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#eventOccurred

    Parameters
    ----------

    eventFields : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaNode::eventOccurred(QVariantList eventFields)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode13eventOccurredE5QListI8QVariantE',
        self._valueOf(eventFields),
    )

  @overload(
      QOpcUa.NodeAttribute, QOpcUaMonitoringParameters.Parameters,
      QOpcUa.UaStatusCode,
  )
  def monitoringStatusChanged(
      self,
      attr: QOpcUa.NodeAttribute,
      items: QOpcUaMonitoringParameters.Parameters,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNode::monitoringStatusChanged(QOpcUa::NodeAttribute attr,
    QOpcUaMonitoringParameters::Parameters items, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#monitoringStatusChanged

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    items : QOpcUaMonitoringParameters.Parameters
      Passed on as its number.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNode::monitoringStatusChanged(QOpcUa::NodeAttribute attr,
    #      QOpcUaMonitoringParameters::Parameters items, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode23monitoringStatusChangedEN6QOpcUa13NodeAttri'
        'buteE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEENS0_12UaStat'
        'usCodeE',
        attr.value, items.value, statusCode.value,
    )

  @overload(QOpcUa.NodeAttribute, QOpcUa.UaStatusCode)
  def enableMonitoringFinished(
      self,
      attr: QOpcUa.NodeAttribute,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNode::enableMonitoringFinished(QOpcUa::NodeAttribute attr,
    QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#enableMonitoringFinished

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNode::enableMonitoringFinished(QOpcUa::NodeAttribute attr,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode24enableMonitoringFinishedEN6QOpcUa13NodeAttr'
        'ibuteENS0_12UaStatusCodeE',
        attr.value, statusCode.value,
    )

  @overload(QOpcUa.NodeAttribute, QOpcUa.UaStatusCode)
  def disableMonitoringFinished(
      self,
      attr: QOpcUa.NodeAttribute,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNode::disableMonitoringFinished(QOpcUa::NodeAttribute attr,
    QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#disableMonitoringFinished

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNode::disableMonitoringFinished(QOpcUa::NodeAttribute attr,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode25disableMonitoringFinishedEN6QOpcUa13NodeAtt'
        'ributeENS0_12UaStatusCodeE',
        attr.value, statusCode.value,
    )

  @overload(str, QVariant, QOpcUa.UaStatusCode)
  def methodCallFinished(
      self,
      methodNodeId: str,
      result: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNode::methodCallFinished(QString methodNodeId,
    QVariant result, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#methodCallFinished

    Parameters
    ----------

    methodNodeId : str
      Passed on as it is: a QString is made of it for the call.

    result : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNode::methodCallFinished(QString methodNodeId, QVariant
    #      result, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode18methodCallFinishedE7QString8QVariantN6QOpcU'
        'a12UaStatusCodeE',
        methodNodeId, self._valueOf(result), statusCode.value,
    )

  @overload(QList[QOpcUaReferenceDescription], QOpcUa.UaStatusCode)
  def browseFinished(
      self,
      children: QList[QOpcUaReferenceDescription],
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNode::browseFinished(QList<QOpcUaReferenceDescription> children,
    QOpcUa::UaStatusCode statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanode.html#browseFinished

    Parameters
    ----------

    children : QList[QOpcUaReferenceDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNode::browseFinished(QList<QOpcUaReferenceDescription>
    #      children, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode14browseFinishedE5QListI26QOpcUaReferenceDesc'
        'riptionEN6QOpcUa12UaStatusCodeE',
        self._valueOf(children), statusCode.value,
    )

  @overload(
      QList[QOpcUaBrowsePathTarget], QList[QOpcUaRelativePathElement],
      QOpcUa.UaStatusCode,
  )
  def resolveBrowsePathFinished(
      self,
      targets: QList[QOpcUaBrowsePathTarget],
      path: QList[QOpcUaRelativePathElement],
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNode::resolveBrowsePathFinished(QList<QOpcUaBrowsePathTarget>
    targets, QList<QOpcUaRelativePathElement> path, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanode.html#resolveBrowsePathFinished

    Parameters
    ----------

    targets : QList[QOpcUaBrowsePathTarget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    path : QList[QOpcUaRelativePathElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNode::resolveBrowsePathFinished(
    #      QList<QOpcUaBrowsePathTarget> targets,
    #      QList<QOpcUaRelativePathElement> path, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN10QOpcUaNode25resolveBrowsePathFinishedE5QListI22QOpcUaBr'
        'owsePathTargetES0_I25QOpcUaRelativePathElementEN6QOpcUa12UaStatusC'
        'odeE',
        self._valueOf(targets), self._valueOf(path), statusCode.value,
    )

  @staticmethod
  def callMethod(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaNode::callMethod(const QString &methodNodeId, const
    QList<QOpcUa::TypedVariant> &args)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaNode.callMethod' has no cute function yet. Qt's 'bool "
        "QOpcUaNode::callMethod(const QString &methodNodeId, const "
        "QList<QOpcUa::TypedVariant> &args)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def readHistoryEvents(*__, **_) -> Never:
    """
    Qt's 'QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryEvents(const
    QDateTime &startTime, const QDateTime &endTime,
    QOpcUaMonitoringParameters::EventFilter &filter, quint32 numValues)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaNode.readHistoryEvents' has no cute function yet. Qt's "
        "'QOpcUaHistoryReadResponse *QOpcUaNode::readHistoryEvents(const "
        "QDateTime &startTime, const QDateTime &endTime, "
        "QOpcUaMonitoringParameters::EventFilter &filter, quint32 "
        "numValues)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def writeAttributes(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaNode::writeAttributes(const AttributeMap &toWrite,
    QOpcUa::Types valueAttributeType)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaNode.writeAttributes' has no cute function yet. Qt's 'bool "
        "QOpcUaNode::writeAttributes(const AttributeMap &toWrite, "
        "QOpcUa::Types valueAttributeType)': takes a type Python has no way "
        "to hand over yet.")
