"""
QOpcUaNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuanode_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpcUaNodePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate
from . import QOpcUa, QOpcUaMonitoringParameters

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QOpcUaClient, QOpcUaNode, QOpcUaNodeImpl, QOpcUaReadResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaClient = WAIT['QOpcUaClient']
  QOpcUaNodeImpl = WAIT['QOpcUaNodeImpl']
  QOpcUaReadResult = WAIT['QOpcUaReadResult']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaNodePrivate(QObjectPrivate):
  """
  The cute side of Qt's QOpcUaNodePrivate: a plain Python object standing in
  front of one C++ QOpcUaNodePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QOpcUaNodePrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaNodePrivate that has a ritual and that Python
  can call so far, 6 names in all: 'q_func', 'createConnections',
  'handleAttributesRead', 'handleAttributesWritten',
  'handleMonitoringEnableDisable', 'handleMonitoringStatusChange'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpcUaNode *QOpcUaNodePrivate::q_func() const': takes in
    Python what 'QOpcUaNode *QOpcUaNodePrivate::q_func()' takes.
  - Qt's 'QOpcUaNodePrivate::~QOpcUaNodePrivate()': the destructor: Python
    never removes a C++ QOpcUaNodePrivate.

  What to expect
  --------------

  - The C++ QOpcUaNodePrivate is created at the first use, not by
    'QOpcUaNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaNodePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaNodePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(
      self,
      impl: Optional[QOpcUaNodeImpl],
      client: Optional[QOpcUaClient],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaNodePrivate::QOpcUaNodePrivate(QOpcUaNodeImpl *impl, QOpcUaClient
    *client)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeprivate.html#QOpcUaNodePrivate

    Parameters
    ----------

    impl : Optional[QOpcUaNodeImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    client : Optional[QOpcUaClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpcUaNodePrivate::QOpcUaNodePrivate(QOpcUaNodeImpl *impl,
    #      QOpcUaClient *client)
    self._noteCreation(QOpcUaNodePrivate, lambda: Rituals.call(
        'ritual_ZN17QOpcUaNodePrivateC1EP14QOpcUaNodeImplP12QOpcUaClient',
        self._addressOf(impl), self._addressOf(client),
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

  def q_func(self) -> Optional[QOpcUaNode]:
    """
    Calls Qt's 'QOpcUaNode *QOpcUaNodePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuanodeprivate.html#q_func

    Returns
    -------

    Optional[QOpcUaNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaNode *QOpcUaNodePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QOpcUaNodePrivate6q_funcEv')
    from . import QOpcUaNode
    return QOpcUaNode._cuteAt(address)

  def createConnections(self) -> None:
    """
    Calls Qt's 'void QOpcUaNodePrivate::createConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeprivate.html#createConnections
    """
    #  void QOpcUaNodePrivate::createConnections()
    self.uglySide.call('ritual_ZN17QOpcUaNodePrivate17createConnectionsEv')

  @overload(QList[QOpcUaReadResult], QOpcUa.UaStatusCode)
  def handleAttributesRead(
      self,
      attr: QList[QOpcUaReadResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaNodePrivate::handleAttributesRead(const
    QList<QOpcUaReadResult> &attr, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeprivate.html#handleAttributesRead

    Parameters
    ----------

    attr : QList[QOpcUaReadResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaNodePrivate::handleAttributesRead(const
    #      QList<QOpcUaReadResult> &attr, QOpcUa::UaStatusCode serviceResult)
    self.uglySide.call(
        'ritual_ZN17QOpcUaNodePrivate20handleAttributesReadERK5QListI16QOpc'
        'UaReadResultEN6QOpcUa12UaStatusCodeE',
        self._valueOf(attr), serviceResult.value,
    )

  @overload(QOpcUa.NodeAttribute, QVariant, QOpcUa.UaStatusCode)
  def handleAttributesWritten(
      self,
      attr: QOpcUa.NodeAttribute,
      value: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodePrivate::handleAttributesWritten(QOpcUa::NodeAttribute attr,
    const QVariant &value, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeprivate.html#handleAttributesWritten

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
    #  void QOpcUaNodePrivate::handleAttributesWritten(QOpcUa::NodeAttribute
    #      attr, const QVariant &value, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN17QOpcUaNodePrivate23handleAttributesWrittenEN6QOpcUa13No'
        'deAttributeERK8QVariantNS0_12UaStatusCodeE',
        attr.value, self._valueOf(value), statusCode.value,
    )

  @overload(QOpcUa.NodeAttribute, bool, QOpcUaMonitoringParameters)
  def handleMonitoringEnableDisable(
      self,
      attr: QOpcUa.NodeAttribute,
      subscribe: bool,
      status: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodePrivate::handleMonitoringEnableDisable(QOpcUa::NodeAttribute
    attr, bool subscribe, const QOpcUaMonitoringParameters &status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeprivate.html

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
    #  void QOpcUaNodePrivate::handleMonitoringEnableDisable(QOpcUa::
    #      NodeAttribute attr, bool subscribe, const
    #      QOpcUaMonitoringParameters &status)
    self.uglySide.call(
        'ritual_ZN17QOpcUaNodePrivate29handleMonitoringEnableDisableEN6QOpc'
        'Ua13NodeAttributeEbRK26QOpcUaMonitoringParameters',
        attr.value, subscribe, self._valueOf(status),
    )

  @overload(
      QOpcUa.NodeAttribute, QOpcUaMonitoringParameters.Parameters,
      QOpcUaMonitoringParameters,
  )
  def handleMonitoringStatusChange(
      self,
      attr: QOpcUa.NodeAttribute,
      items: QOpcUaMonitoringParameters.Parameters,
      param: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaNodePrivate::handleMonitoringStatusChange(QOpcUa::NodeAttribute
    attr, QOpcUaMonitoringParameters::Parameters items, const
    QOpcUaMonitoringParameters &param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuanodeprivate.html

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
    #  void QOpcUaNodePrivate::handleMonitoringStatusChange(QOpcUa::
    #      NodeAttribute attr, QOpcUaMonitoringParameters::Parameters items,
    #      const QOpcUaMonitoringParameters &param)
    self.uglySide.call(
        'ritual_ZN17QOpcUaNodePrivate28handleMonitoringStatusChangeEN6QOpcU'
        'a13NodeAttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEE'
        'RKS3_',
        attr.value, items.value, self._valueOf(param),
    )
