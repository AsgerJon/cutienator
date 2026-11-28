"""
QOpcUaClientPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuaclient_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpcUaClientPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate, QStringList
from . import QOpcUa, QOpcUaClient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOpcUaApplicationIdentity, QOpcUaClientImpl
  from . import QOpcUaEndpointDescription, QOpcUaPkiConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaApplicationIdentity = WAIT['QOpcUaApplicationIdentity']
  QOpcUaClientImpl = WAIT['QOpcUaClientImpl']
  QOpcUaEndpointDescription = WAIT['QOpcUaEndpointDescription']
  QOpcUaPkiConfiguration = WAIT['QOpcUaPkiConfiguration']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaClientPrivate(QObjectPrivate):
  """
  The cute side of Qt's QOpcUaClientPrivate: a plain Python object standing
  in front of one C++ QOpcUaClientPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QOpcUaClientPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaClientPrivate that has a ritual and that
  Python can call so far, 12 names in all: 'q_func', 'connectToEndpoint',
  'disconnectFromEndpoint', 'setStateAndError', 'updateNamespaceArray',
  'namespaceArray', 'namespaceArrayUpdated', 'setupNamespaceArrayMonitoring',
  'setApplicationIdentity', 'applicationIdentity', 'setPkiConfiguration',
  'pkiConfiguration'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpcUaClient *QOpcUaClientPrivate::q_func() const': takes in
    Python what 'QOpcUaClient *QOpcUaClientPrivate::q_func()' takes.
  - Qt's 'QOpcUaClientPrivate::~QOpcUaClientPrivate()': the destructor:
    Python never removes a C++ QOpcUaClientPrivate.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QOpcUaClientPrivate is created at the first use, not by
    'QOpcUaClientPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaClientPrivate.
  - Each name of Qt's QOpcUaClientPrivate that has no cute function yet,
    'checkAndSetUrl', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaClientPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def namespaceArray(self) -> QStringList:
    """
    Calls Qt's 'QStringList QOpcUaClientPrivate::namespaceArray() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#namespaceArray

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QOpcUaClientPrivate::namespaceArray() const
    address = self.uglySide.call(
        'ritual_ZNK19QOpcUaClientPrivate14namespaceArrayEv',
    )
    return QStringList._cuteOwning(address)

  def applicationIdentity(self) -> QOpcUaApplicationIdentity:
    """
    Calls Qt's 'QOpcUaApplicationIdentity
    QOpcUaClientPrivate::applicationIdentity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#applicationIdentity

    Returns
    -------

    QOpcUaApplicationIdentity
      A new cute QOpcUaApplicationIdentity around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaApplicationIdentity QOpcUaClientPrivate::applicationIdentity()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QOpcUaClientPrivate19applicationIdentityEv',
    )
    from . import QOpcUaApplicationIdentity
    return QOpcUaApplicationIdentity._cuteOwning(address)

  def pkiConfiguration(self) -> QOpcUaPkiConfiguration:
    """
    Calls Qt's 'QOpcUaPkiConfiguration
    QOpcUaClientPrivate::pkiConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#pkiConfiguration

    Returns
    -------

    QOpcUaPkiConfiguration
      A new cute QOpcUaPkiConfiguration around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaPkiConfiguration QOpcUaClientPrivate::pkiConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK19QOpcUaClientPrivate16pkiConfigurationEv',
    )
    from . import QOpcUaPkiConfiguration
    return QOpcUaPkiConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUaClient.ClientState)
  @overload(QOpcUaClient.ClientState, QOpcUaClient.ClientError)
  def setStateAndError(
      self,
      state: QOpcUaClient.ClientState,
      error: QOpcUaClient.ClientError = QOpcUaClient.ClientError.NoError,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClientPrivate::setStateAndError(QOpcUaClient::ClientState state,
    QOpcUaClient::ClientError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#setStateAndError

    Parameters
    ----------

    state : QOpcUaClient.ClientState
      Passed on as its number.

    error : QOpcUaClient.ClientError
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUaClient.ClientError.NoError.
    """
    #  void QOpcUaClientPrivate::setStateAndError(QOpcUaClient::ClientState
    #      state, QOpcUaClient::ClientError error)
    self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate16setStateAndErrorEN12QOpcUaClient11'
        'ClientStateENS0_11ClientErrorE',
        state.value, error.value,
    )

  @overload(QOpcUaApplicationIdentity)
  def setApplicationIdentity(
      self,
      identity: QOpcUaApplicationIdentity,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientPrivate::setApplicationIdentity(const
    QOpcUaApplicationIdentity &identity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#setApplicationIdentity

    Parameters
    ----------

    identity : QOpcUaApplicationIdentity
      Passed on as a value: Qt reads the C++ QOpcUaApplicationIdentity, which
      stays Python's own.
    """
    #  void QOpcUaClientPrivate::setApplicationIdentity(const
    #      QOpcUaApplicationIdentity &identity)
    self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate22setApplicationIdentityERK25QOpcUaA'
        'pplicationIdentity',
        self._valueOf(identity),
    )

  @overload(QOpcUaPkiConfiguration)
  def setPkiConfiguration(self, config: QOpcUaPkiConfiguration) -> None:
    """
    Calls Qt's 'void QOpcUaClientPrivate::setPkiConfiguration(const
    QOpcUaPkiConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#setPkiConfiguration

    Parameters
    ----------

    config : QOpcUaPkiConfiguration
      Passed on as a value: Qt reads the C++ QOpcUaPkiConfiguration, which
      stays Python's own.
    """
    #  void QOpcUaClientPrivate::setPkiConfiguration(const
    #      QOpcUaPkiConfiguration &config)
    self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate19setPkiConfigurationERK22QOpcUaPkiC'
        'onfiguration',
        self._valueOf(config),
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

  @overload(QOpcUaClientImpl)
  @overload(NoneType)
  def __init__(self, impl: Optional[QOpcUaClientImpl]) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaClientPrivate::QOpcUaClientPrivate(QOpcUaClientImpl *impl)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#QOpcUaClientPrivate

    Parameters
    ----------

    impl : Optional[QOpcUaClientImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpcUaClientPrivate::QOpcUaClientPrivate(QOpcUaClientImpl *impl)
    self._noteCreation(QOpcUaClientPrivate, lambda: Rituals.call(
        'ritual_ZN19QOpcUaClientPrivateC1EP16QOpcUaClientImpl',
        self._addressOf(impl),
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

  def q_func(self) -> Optional[QOpcUaClient]:
    """
    Calls Qt's 'QOpcUaClient *QOpcUaClientPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientprivate.html#q_func

    Returns
    -------

    Optional[QOpcUaClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaClient *QOpcUaClientPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QOpcUaClientPrivate6q_funcEv')
    return QOpcUaClient._cuteAt(address)

  @overload(QOpcUaEndpointDescription)
  def connectToEndpoint(self, endpoint: QOpcUaEndpointDescription) -> None:
    """
    Calls Qt's 'void QOpcUaClientPrivate::connectToEndpoint(const
    QOpcUaEndpointDescription &endpoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#connectToEndpoint

    Parameters
    ----------

    endpoint : QOpcUaEndpointDescription
      Passed on as a value: Qt reads the C++ QOpcUaEndpointDescription, which
      stays Python's own.
    """
    #  void QOpcUaClientPrivate::connectToEndpoint(const
    #      QOpcUaEndpointDescription &endpoint)
    self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate17connectToEndpointERK25QOpcUaEndpoi'
        'ntDescription',
        self._valueOf(endpoint),
    )

  def disconnectFromEndpoint(self) -> None:
    """
    Calls Qt's 'void QOpcUaClientPrivate::disconnectFromEndpoint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#disconnectFromEndpoint
    """
    #  void QOpcUaClientPrivate::disconnectFromEndpoint()
    self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate22disconnectFromEndpointEv',
    )

  def updateNamespaceArray(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientPrivate::updateNamespaceArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#updateNamespaceArray
    """
    #  bool QOpcUaClientPrivate::updateNamespaceArray()
    return self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate20updateNamespaceArrayEv',
    )

  @overload(QOpcUa.NodeAttributes)
  def namespaceArrayUpdated(self, attr: QOpcUa.NodeAttributes) -> None:
    """
    Calls Qt's 'void
    QOpcUaClientPrivate::namespaceArrayUpdated(QOpcUa::NodeAttributes attr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html#namespaceArrayUpdated

    Parameters
    ----------

    attr : QOpcUa.NodeAttributes
      Passed on as its number.
    """
    #  void QOpcUaClientPrivate::namespaceArrayUpdated(QOpcUa::NodeAttributes
    #      attr)
    self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate21namespaceArrayUpdatedE6QFlagsIN6QO'
        'pcUa13NodeAttributeEE',
        attr.value,
    )

  def setupNamespaceArrayMonitoring(self) -> None:
    """
    Calls Qt's 'void QOpcUaClientPrivate::setupNamespaceArrayMonitoring()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientprivate.html
    """
    #  void QOpcUaClientPrivate::setupNamespaceArrayMonitoring()
    self.uglySide.call(
        'ritual_ZN19QOpcUaClientPrivate29setupNamespaceArrayMonitoringEv',
    )

  @staticmethod
  def checkAndSetUrl(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaClientPrivate::checkAndSetUrl(const QUrl &url)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QOpcUaClientPrivate.checkAndSetUrl' has no cute function yet. "
        "Qt's 'bool QOpcUaClientPrivate::checkAndSetUrl(const QUrl &url)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
