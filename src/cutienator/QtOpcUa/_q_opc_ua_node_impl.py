"""
QOpcUaNodeImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuanodeimpl_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpcUaNodeImpl to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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
  from . import QOpcUaBrowsePathTarget, QOpcUaBrowseRequest
  from . import QOpcUaHistoryData, QOpcUaHistoryReadResponse
  from . import QOpcUaReadResult, QOpcUaReferenceDescription
  from . import QOpcUaRelativePathElement
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QOpcUaBrowsePathTarget = WAIT['QOpcUaBrowsePathTarget']
  QOpcUaBrowseRequest = WAIT['QOpcUaBrowseRequest']
  QOpcUaHistoryData = WAIT['QOpcUaHistoryData']
  QOpcUaReadResult = WAIT['QOpcUaReadResult']
  QOpcUaReferenceDescription = WAIT['QOpcUaReferenceDescription']
  QOpcUaRelativePathElement = WAIT['QOpcUaRelativePathElement']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaNodeImpl(QObject):
  """
  The cute side of Qt's QOpcUaNodeImpl: a plain Python object standing in
  front of one C++ QOpcUaNodeImpl.

  It is built on the cute 'QObject', as Qt's QOpcUaNodeImpl is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaNodeImpl that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'readAttributes',
  'enableMonitoring', 'disableMonitoring', 'browse', 'nodeId',
  'writeAttribute', 'modifyMonitoring', 'readHistoryRaw',
  'readHistoryEvents', 'resolveBrowsePath', 'handle', 'setHandle',
  'registered', 'setRegistered', 'attributesRead', 'attributeWritten',
  'browseFinished', 'dataChangeOccurred', 'eventOccurred',
  'monitoringEnableDisable', 'monitoringStatusChanged', 'methodCallFinished',
  'resolveBrowsePathFinished', 'readHistoryRawFinished'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaNodeImpl::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpcUaNodeImpl::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QOpcUaNodeImpl::~QOpcUaNodeImpl()': the destructor: Python never
    removes a C++ QOpcUaNodeImpl.
  - Qt's 'bool QOpcUaNodeImpl::writeAttributes(const QOpcUaNode::AttributeMap
    &toWrite, QOpcUa::Types valueAttributeType)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QOpcUaNodeImpl::callMethod(const QString &methodNodeId, const
    QList<QOpcUa::TypedVariant> &args)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  3 of the 34 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QOpcUaNodeImpl is created at the first use, not by
    'QOpcUaNodeImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaNodeImpl.
  - Qt tells when it has removed the C++ QOpcUaNodeImpl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpcUaNodeImpl that has no cute function yet,
    '__init__', 'callMethod', 'writeAttributes', holds a function that raises
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
    Calls Qt's 'QString QOpcUaNodeImpl::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#tr

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
    #  QString QOpcUaNodeImpl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QOpcUaNodeImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaNodeImpl'

  #  A C++ QOpcUaNodeImpl Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaNodeImpl'

  #  The functions Qt calls itself that QOpcUaNodeImpl is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'writeAttributes': (
          'bool QOpcUaNodeImpl::writeAttributes(const '
          'QOpcUaNode::AttributeMap &, QOpcUa::Types)',
      ),
      'callMethod': (
          'bool QOpcUaNodeImpl::callMethod(const QString &, const '
          'QList<QOpcUa::TypedVariant> &)',
      ),
      'resolveBrowsePath': (
          'bool QOpcUaNodeImpl::resolveBrowsePath(const '
          'QList<QOpcUaRelativePathElement> &)',
      ),
  }

  #  The functions Qt calls itself that QOpcUaNodeImpl is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'readAttributes': (
          ('_ZN14QOpcUaNodeImpl14readAttributesE6QFlagsIN6QOpcUa13NodeAttri'
           'buteEERK7QString',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtOpcUa:QOpcUa.NodeAttribute'),
               ('address', 'text', ''),
           )),
      ),
      'enableMonitoring': (
          ('_ZN14QOpcUaNodeImpl16enableMonitoringE6QFlagsIN6QOpcUa13NodeAtt'
           'ributeEERK26QOpcUaMonitoringParameters',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtOpcUa:QOpcUa.NodeAttribute'),
               ('address', 'value', 'QtOpcUa:QOpcUaMonitoringParameters'),
           )),
      ),
      'disableMonitoring': (
          ('_ZN14QOpcUaNodeImpl17disableMonitoringE6QFlagsIN6QOpcUa13NodeAt'
           'tributeEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtOpcUa:QOpcUa.NodeAttribute'),
           )),
      ),
      'browse': (
          ('_ZN14QOpcUaNodeImpl6browseERK19QOpcUaBrowseRequest',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtOpcUa:QOpcUaBrowseRequest'),
           )),
      ),
      'nodeId': (
          ('_ZNK14QOpcUaNodeImpl6nodeIdEv',
           ('address', 'text', ''),
           ()),
      ),
      'writeAttribute': (
          ('_ZN14QOpcUaNodeImpl14writeAttributeEN6QOpcUa13NodeAttributeERK8'
           'QVariantNS0_5TypesERK7QString',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtOpcUa:QOpcUa.NodeAttribute'),
               ('address', 'value', 'QtCore:QVariant'),
               ('int', 'enum', 'QtOpcUa:QOpcUa.Types'),
               ('address', 'text', ''),
           )),
      ),
      'modifyMonitoring': (
          ('_ZN14QOpcUaNodeImpl16modifyMonitoringEN6QOpcUa13NodeAttributeEN'
           '26QOpcUaMonitoringParameters9ParameterERK8QVariant',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtOpcUa:QOpcUa.NodeAttribute'),
               ('int', 'enum',
                'QtOpcUa:QOpcUaMonitoringParameters.Parameter'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'readHistoryRaw': (
          ('_ZN14QOpcUaNodeImpl14readHistoryRawERK9QDateTimeS2_jbN6QOpcUa18'
           'TimestampsToReturnE',
           ('address', 'address', 'QtOpcUa:QOpcUaHistoryReadResponse'),
           (
               ('address', 'value', 'QtCore:QDateTime'),
               ('address', 'value', 'QtCore:QDateTime'),
               ('unsigned int', 'number', ''),
               ('bool', 'number', ''),
               ('int', 'enum', 'QtOpcUa:QOpcUa.TimestampsToReturn'),
           )),
      ),
      'readHistoryEvents': (
          ('_ZN14QOpcUaNodeImpl17readHistoryEventsERK9QDateTimeS2_RKN26QOpc'
           'UaMonitoringParameters11EventFilterEj',
           ('address', 'address', 'QtOpcUa:QOpcUaHistoryReadResponse'),
           (
               ('address', 'value', 'QtCore:QDateTime'),
               ('address', 'value', 'QtCore:QDateTime'),
               ('address', 'value',
                'QtOpcUa:QOpcUaMonitoringParameters.EventFilter'),
               ('unsigned int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaNodeImpl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaNodeImpl::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QOpcUaNodeImpl10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaNodeImpl::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaNodeImpl::nodeId() const
    return self.uglySide.call('ritual_ZNK14QOpcUaNodeImpl6nodeIdEv')

  def handle(self) -> int:
    """
    Calls Qt's 'quint64 QOpcUaNodeImpl::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#handle
    """
    #  quint64 QOpcUaNodeImpl::handle() const
    return self.uglySide.call('ritual_ZNK14QOpcUaNodeImpl6handleEv')

  def registered(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeImpl::registered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#registered
    """
    #  bool QOpcUaNodeImpl::registered() const
    return self.uglySide.call('ritual_ZNK14QOpcUaNodeImpl10registeredEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setHandle(self, handle: int) -> None:
    """
    Calls Qt's 'void QOpcUaNodeImpl::setHandle(quint64 handle)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#setHandle

    Parameters
    ----------

    handle : int
      Passed on as it is.
    """
    #  void QOpcUaNodeImpl::setHandle(quint64 handle)
    self.uglySide.call('ritual_ZN14QOpcUaNodeImpl9setHandleEy', handle)

  @overload(bool)
  def setRegistered(self, registered: bool) -> None:
    """
    Calls Qt's 'void QOpcUaNodeImpl::setRegistered(bool registered)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#setRegistered

    Parameters
    ----------

    registered : bool
      Passed on as it is.
    """
    #  void QOpcUaNodeImpl::setRegistered(bool registered)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl13setRegisteredEb', registered,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QOpcUaNodeImpl::QOpcUaNodeImpl()': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QOpcUaNodeImpl.__init__' has no cute function yet. Qt's "
        "'QOpcUaNodeImpl::QOpcUaNodeImpl()': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  @overload(QOpcUa.NodeAttributes, str)
  def readAttributes(
      self,
      attr: QOpcUa.NodeAttributes,
      indexRange: str,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeImpl::readAttributes(QOpcUa::NodeAttributes
    attr, const QString &indexRange)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#readAttributes

    Parameters
    ----------

    attr : QOpcUa.NodeAttributes
      Passed on as its number.

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpcUaNodeImpl::readAttributes(QOpcUa::NodeAttributes attr, const
    #      QString &indexRange)
    return self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl14readAttributesE6QFlagsIN6QOpcUa13NodeAt'
        'tributeEERK7QString',
        attr.value, indexRange,
    )

  @overload(QOpcUa.NodeAttributes, QOpcUaMonitoringParameters)
  def enableMonitoring(
      self,
      attr: QOpcUa.NodeAttributes,
      settings: QOpcUaMonitoringParameters,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeImpl::enableMonitoring(QOpcUa::NodeAttributes
    attr, const QOpcUaMonitoringParameters &settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#enableMonitoring

    Parameters
    ----------

    attr : QOpcUa.NodeAttributes
      Passed on as its number.

    settings : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  bool QOpcUaNodeImpl::enableMonitoring(QOpcUa::NodeAttributes attr,
    #      const QOpcUaMonitoringParameters &settings)
    return self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl16enableMonitoringE6QFlagsIN6QOpcUa13Node'
        'AttributeEERK26QOpcUaMonitoringParameters',
        attr.value, self._valueOf(settings),
    )

  @overload(QOpcUa.NodeAttributes)
  def disableMonitoring(self, attr: QOpcUa.NodeAttributes) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeImpl::disableMonitoring(QOpcUa::NodeAttributes
    attr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#disableMonitoring

    Parameters
    ----------

    attr : QOpcUa.NodeAttributes
      Passed on as its number.
    """
    #  bool QOpcUaNodeImpl::disableMonitoring(QOpcUa::NodeAttributes attr)
    return self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl17disableMonitoringE6QFlagsIN6QOpcUa13Nod'
        'eAttributeEE',
        attr.value,
    )

  @overload(QOpcUaBrowseRequest)
  def browse(self, request: QOpcUaBrowseRequest) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeImpl::browse(const QOpcUaBrowseRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#browse

    Parameters
    ----------

    request : QOpcUaBrowseRequest
      Passed on as a value: Qt reads the C++ QOpcUaBrowseRequest, which stays
      Python's own.
    """
    #  bool QOpcUaNodeImpl::browse(const QOpcUaBrowseRequest &request)
    return self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl6browseERK19QOpcUaBrowseRequest',
        self._valueOf(request),
    )

  @overload(QOpcUa.NodeAttribute, QVariant, QOpcUa.Types, str)
  def writeAttribute(
      self,
      attribute: QOpcUa.NodeAttribute,
      value: QVariant,
      type: QOpcUa.Types,
      indexRange: str,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeImpl::writeAttribute(QOpcUa::NodeAttribute
    attribute, const QVariant &value, QOpcUa::Types type, const QString
    &indexRange)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#writeAttribute

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QOpcUa.Types
      Passed on as its number.

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpcUaNodeImpl::writeAttribute(QOpcUa::NodeAttribute attribute,
    #      const QVariant &value, QOpcUa::Types type, const QString
    #      &indexRange)
    return self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl14writeAttributeEN6QOpcUa13NodeAttributeE'
        'RK8QVariantNS0_5TypesERK7QString',
        attribute.value, self._valueOf(value), type.value, indexRange,
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
    Calls Qt's 'bool QOpcUaNodeImpl::modifyMonitoring(QOpcUa::NodeAttribute
    attr, QOpcUaMonitoringParameters::Parameter item, const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#modifyMonitoring

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
    #  bool QOpcUaNodeImpl::modifyMonitoring(QOpcUa::NodeAttribute attr,
    #      QOpcUaMonitoringParameters::Parameter item, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl16modifyMonitoringEN6QOpcUa13NodeAttribut'
        'eEN26QOpcUaMonitoringParameters9ParameterERK8QVariant',
        attr.value, item.value, self._valueOf(value),
    )

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
    Calls Qt's 'QOpcUaHistoryReadResponse
    *QOpcUaNodeImpl::readHistoryRaw(const QDateTime &startTime, const
    QDateTime &endTime, quint32 numValues, bool returnBounds,
    QOpcUa::TimestampsToReturn timestampsToReturn)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#readHistoryRaw

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
    #  QOpcUaHistoryReadResponse *QOpcUaNodeImpl::readHistoryRaw(const
    #      QDateTime &startTime, const QDateTime &endTime, quint32 numValues,
    #      bool returnBounds, QOpcUa::TimestampsToReturn timestampsToReturn)
    address = self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl14readHistoryRawERK9QDateTimeS2_jbN6QOpcU'
        'a18TimestampsToReturnE',
        self._valueOf(startTime), self._valueOf(endTime), numValues,
        returnBounds, timestampsToReturn.value,
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)

  @overload(
      QDateTime, QDateTime, QOpcUaMonitoringParameters.EventFilter, int,
  )
  def readHistoryEvents(
      self,
      startTime: QDateTime,
      endTime: QDateTime,
      filter: QOpcUaMonitoringParameters.EventFilter,
      numValues: int,
  ) -> Optional[QOpcUaHistoryReadResponse]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse
    *QOpcUaNodeImpl::readHistoryEvents(const QDateTime &startTime, const
    QDateTime &endTime, const QOpcUaMonitoringParameters::EventFilter
    &filter, quint32 numValues)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#readHistoryEvents

    Parameters
    ----------

    startTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    endTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    filter : QOpcUaMonitoringParameters.EventFilter
      Passed on as a value: Qt reads the C++
      QOpcUaMonitoringParameters::EventFilter, which stays Python's own.

    numValues : int
      Passed on as it is.

    Returns
    -------

    Optional[QOpcUaHistoryReadResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaHistoryReadResponse *QOpcUaNodeImpl::readHistoryEvents(const
    #      QDateTime &startTime, const QDateTime &endTime, const
    #      QOpcUaMonitoringParameters::EventFilter &filter, quint32
    #      numValues)
    address = self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl17readHistoryEventsERK9QDateTimeS2_RKN26Q'
        'OpcUaMonitoringParameters11EventFilterEj',
        self._valueOf(startTime), self._valueOf(endTime),
        self._valueOf(filter), numValues,
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)

  @overload(QList[QOpcUaRelativePathElement])
  def resolveBrowsePath(
      self,
      path: QList[QOpcUaRelativePathElement],
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaNodeImpl::resolveBrowsePath(const
    QList<QOpcUaRelativePathElement> &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#resolveBrowsePath

    Parameters
    ----------

    path : QList[QOpcUaRelativePathElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaNodeImpl::resolveBrowsePath(const
    #      QList<QOpcUaRelativePathElement> &path)
    return self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl17resolveBrowsePathERK5QListI25QOpcUaRela'
        'tivePathElementE',
        self._valueOf(path),
    )

  @overload(QList[QOpcUaReadResult], QOpcUa.UaStatusCode)
  def attributesRead(
      self,
      attr: QList[QOpcUaReadResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNodeImpl::attributesRead(QList<QOpcUaReadResult>
    attr, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#attributesRead

    Parameters
    ----------

    attr : QList[QOpcUaReadResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNodeImpl::attributesRead(QList<QOpcUaReadResult> attr,
    #      QOpcUa::UaStatusCode serviceResult)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl14attributesReadE5QListI16QOpcUaReadResul'
        'tEN6QOpcUa12UaStatusCodeE',
        self._valueOf(attr), serviceResult.value,
    )

  @overload(QOpcUa.NodeAttribute, QVariant, QOpcUa.UaStatusCode)
  def attributeWritten(
      self,
      attr: QOpcUa.NodeAttribute,
      value: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNodeImpl::attributeWritten(QOpcUa::NodeAttribute
    attr, QVariant value, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#attributeWritten

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNodeImpl::attributeWritten(QOpcUa::NodeAttribute attr,
    #      QVariant value, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl16attributeWrittenEN6QOpcUa13NodeAttribut'
        'eE8QVariantNS0_12UaStatusCodeE',
        attr.value, self._valueOf(value), statusCode.value,
    )

  @overload(QList[QOpcUaReferenceDescription], QOpcUa.UaStatusCode)
  def browseFinished(
      self,
      children: QList[QOpcUaReferenceDescription],
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeImpl::browseFinished(QList<QOpcUaReferenceDescription>
    children, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#browseFinished

    Parameters
    ----------

    children : QList[QOpcUaReferenceDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNodeImpl::browseFinished(QList<QOpcUaReferenceDescription>
    #      children, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl14browseFinishedE5QListI26QOpcUaReference'
        'DescriptionEN6QOpcUa12UaStatusCodeE',
        self._valueOf(children), statusCode.value,
    )

  @overload(QOpcUa.NodeAttribute, QOpcUaReadResult)
  def dataChangeOccurred(
      self,
      attr: QOpcUa.NodeAttribute,
      value: QOpcUaReadResult,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNodeImpl::dataChangeOccurred(QOpcUa::NodeAttribute
    attr, QOpcUaReadResult value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#dataChangeOccurred

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QOpcUaReadResult
      Passed on as a value: Qt reads the C++ QOpcUaReadResult, which stays
      Python's own.
    """
    #  void QOpcUaNodeImpl::dataChangeOccurred(QOpcUa::NodeAttribute attr,
    #      QOpcUaReadResult value)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl18dataChangeOccurredEN6QOpcUa13NodeAttrib'
        'uteE16QOpcUaReadResult',
        attr.value, self._valueOf(value),
    )

  @overload(QList[QVariant])
  def eventOccurred(self, eventFields: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QOpcUaNodeImpl::eventOccurred(QVariantList
    eventFields)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeimpl.html#eventOccurred

    Parameters
    ----------

    eventFields : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaNodeImpl::eventOccurred(QVariantList eventFields)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl13eventOccurredE5QListI8QVariantE',
        self._valueOf(eventFields),
    )

  @overload(QOpcUa.NodeAttribute, bool, QOpcUaMonitoringParameters)
  def monitoringEnableDisable(
      self,
      attr: QOpcUa.NodeAttribute,
      subscribe: bool,
      status: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeImpl::monitoringEnableDisable(QOpcUa::NodeAttribute attr, bool
    subscribe, QOpcUaMonitoringParameters status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#monitoringEnableDisable

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    subscribe : bool
      Passed on as it is.

    status : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  void QOpcUaNodeImpl::monitoringEnableDisable(QOpcUa::NodeAttribute
    #      attr, bool subscribe, QOpcUaMonitoringParameters status)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl23monitoringEnableDisableEN6QOpcUa13NodeA'
        'ttributeEb26QOpcUaMonitoringParameters',
        attr.value, subscribe, self._valueOf(status),
    )

  @overload(
      QOpcUa.NodeAttribute, QOpcUaMonitoringParameters.Parameters,
      QOpcUaMonitoringParameters,
  )
  def monitoringStatusChanged(
      self,
      attr: QOpcUa.NodeAttribute,
      items: QOpcUaMonitoringParameters.Parameters,
      param: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeImpl::monitoringStatusChanged(QOpcUa::NodeAttribute attr,
    QOpcUaMonitoringParameters::Parameters items, QOpcUaMonitoringParameters
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#monitoringStatusChanged

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    items : QOpcUaMonitoringParameters.Parameters
      Passed on as its number.

    param : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  void QOpcUaNodeImpl::monitoringStatusChanged(QOpcUa::NodeAttribute
    #      attr, QOpcUaMonitoringParameters::Parameters items,
    #      QOpcUaMonitoringParameters param)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl23monitoringStatusChangedEN6QOpcUa13NodeA'
        'ttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEES3_',
        attr.value, items.value, self._valueOf(param),
    )

  @overload(str, QVariant, QOpcUa.UaStatusCode)
  def methodCallFinished(
      self,
      methodNodeId: str,
      result: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNodeImpl::methodCallFinished(QString methodNodeId,
    QVariant result, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#methodCallFinished

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
    #  void QOpcUaNodeImpl::methodCallFinished(QString methodNodeId, QVariant
    #      result, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl18methodCallFinishedE7QString8QVariantN6Q'
        'OpcUa12UaStatusCodeE',
        methodNodeId, self._valueOf(result), statusCode.value,
    )

  @overload(
      QList[QOpcUaBrowsePathTarget], QList[QOpcUaRelativePathElement],
      QOpcUa.UaStatusCode,
  )
  def resolveBrowsePathFinished(
      self,
      targets: QList[QOpcUaBrowsePathTarget],
      path: QList[QOpcUaRelativePathElement],
      status: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeImpl::resolveBrowsePathFinished(QList<QOpcUaBrowsePathTarget>
    targets, QList<QOpcUaRelativePathElement> path, QOpcUa::UaStatusCode
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#resolveBrowsePathFinished

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

    status : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNodeImpl::resolveBrowsePathFinished(
    #      QList<QOpcUaBrowsePathTarget> targets,
    #      QList<QOpcUaRelativePathElement> path, QOpcUa::UaStatusCode
    #      status)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl25resolveBrowsePathFinishedE5QListI22QOpc'
        'UaBrowsePathTargetES0_I25QOpcUaRelativePathElementEN6QOpcUa12UaSta'
        'tusCodeE',
        self._valueOf(targets), self._valueOf(path), status.value,
    )

  @overload(QList[QOpcUaHistoryData], QOpcUa.UaStatusCode)
  def readHistoryRawFinished(
      self,
      results: QList[QOpcUaHistoryData],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodeImpl::readHistoryRawFinished(QList<QOpcUaHistoryData> results,
    QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeimpl.html#readHistoryRawFinished

    Parameters
    ----------

    results : QList[QOpcUaHistoryData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNodeImpl::readHistoryRawFinished(QList<QOpcUaHistoryData>
    #      results, QOpcUa::UaStatusCode serviceResult)
    self.uglySide.call(
        'ritual_ZN14QOpcUaNodeImpl22readHistoryRawFinishedE5QListI17QOpcUaH'
        'istoryDataEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @staticmethod
  def callMethod(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaNodeImpl::callMethod(const QString &methodNodeId, const
    QList<QOpcUa::TypedVariant> &args)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaNodeImpl.callMethod' has no cute function yet. Qt's 'bool "
        "QOpcUaNodeImpl::callMethod(const QString &methodNodeId, const "
        "QList<QOpcUa::TypedVariant> &args)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def writeAttributes(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaNodeImpl::writeAttributes(const QOpcUaNode::AttributeMap
    &toWrite, QOpcUa::Types valueAttributeType)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaNodeImpl.writeAttributes' has no cute function yet. Qt's "
        "'bool QOpcUaNodeImpl::writeAttributes(const "
        "QOpcUaNode::AttributeMap &toWrite, QOpcUa::Types "
        "valueAttributeType)': takes a type Python has no way to hand over "
        "yet.")
