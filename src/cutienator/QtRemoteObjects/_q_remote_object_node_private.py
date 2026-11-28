"""
QRemoteObjectNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectNodePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QHash, QObjectPrivate
from . import QRemoteObjectNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QObject
  from . import QRemoteObjectReplica, QRemoteObjectSourceLocationInfo
  from . import QReplicaImplementationInterface, QtROClientIoDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObject = WAIT['QMetaObject']
  QObject = WAIT['QObject']
  QRemoteObjectReplica = WAIT['QRemoteObjectReplica']
  QtROClientIoDevice = WAIT['QtROClientIoDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectNodePrivate(QObjectPrivate):
  """
  The cute side of Qt's QRemoteObjectNodePrivate: a plain Python object
  standing in front of one C++ QRemoteObjectNodePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QRemoteObjectNodePrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectNodePrivate that has a ritual and that
  Python can call so far, 8 names in all: 'remoteObjectAddresses',
  'setLastError', 'connectReplica', 'hasInstance', 'onShouldReconnect',
  'handleNewAcquire', 'checkSignatures', 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectNodePrivate::~QRemoteObjectNodePrivate()': the
    destructor: Python never removes a C++ QRemoteObjectNodePrivate.
  - Qt's 'void QRemoteObjectNodePrivate::onRemoteObjectSourceRemoved(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
  - Qt's 'const QRemoteObjectNode *QRemoteObjectNodePrivate::q_func() const':
    takes in Python what 'QRemoteObjectNode
    *QRemoteObjectNodePrivate::q_func()' takes.

  What has no ritual
  ------------------

  14 of the 25 functions Qt declares: 7 leans on 'QRemoteObjectNodePrivate; 3
  leans on 'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray
  const&)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken; 2 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file; 2 leans on
  'QRemoteObjectPackets.

  What to expect
  --------------

  - The C++ QRemoteObjectNodePrivate is created at the first use, not by
    'QRemoteObjectNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectNodePrivate.
  - Each name of Qt's QRemoteObjectNodePrivate that has no cute function yet,
    '__init__', 'handlePointerToQObjectProperties',
    'handlePointerToQObjectProperty', 'handleReplicaConnection',
    'initConnection', 'initialize', 'onClientRead', 'onRegistryInitialized',
    'onRemoteObjectSourceAdded', 'onRemoteObjectSourceRemoved',
    'openConnectionIfNeeded', 'setRegistry', 'setRegistryUrlNodeImpl',
    'setReplicaImplementation', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QRemoteObjectNodePrivate, each a class in
  #  here as in C++.

  class SourceInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRemoteObjectNodePrivate::SourceInfo: a plain
    Python object standing in front of one C++
    QRemoteObjectNodePrivate::SourceInfo.

    C++ hands a QRemoteObjectNodePrivate::SourceInfo around as a copy, so
    every C++ QRemoteObjectNodePrivate::SourceInfo behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QRemoteObjectNodePrivate::SourceInfo yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRemoteObjectNodePrivate::SourceInfo::~SourceInfo()': the
      destructor: Python removes its C++ QRemoteObjectNodePrivate::SourceInfo
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRemoteObjectNodePrivate::SourceInfo is created at the first
      use, not by 'QRemoteObjectNodePrivate::SourceInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRemoteObjectNodePrivate::SourceInfo back gives a
      copy the ritual made for Python, in a new cute
      QRemoteObjectNodePrivate::SourceInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRemoteObjectNodePrivate::SourceInfo'

    #  Qt's '~QRemoteObjectNodePrivate::SourceInfo()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QRemoteObjectNodePrivate::SourceInfo behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN24QRemoteObjectNodePrivate10SourceInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectNodePrivate'

  #  A C++ QRemoteObjectNodePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectNodePrivate'

  #  The functions Qt calls itself that QRemoteObjectNodePrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'remoteObjectAddresses': (
          'QRemoteObjectSourceLocations '
          'QRemoteObjectNodePrivate::remoteObjectAddresses() const',
      ),
  }

  #  The functions Qt calls itself that QRemoteObjectNodePrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'handleNewAcquire': (
          ('_ZN24QRemoteObjectNodePrivate16handleNewAcquireEPK11QMetaObject'
           'P20QRemoteObjectReplicaRK7QString',
           ('address', 'address',
            'QtRemoteObjects:QReplicaImplementationInterface'),
           (
               ('address', 'address', 'QtCore:QMetaObject'),
               ('address', 'address',
                'QtRemoteObjects:QRemoteObjectReplica'),
               ('address', 'text', ''),
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

  def remoteObjectAddresses(
      self,
  ) -> QHash[str, QRemoteObjectSourceLocationInfo]:
    """
    Calls Qt's 'QRemoteObjectSourceLocations
    QRemoteObjectNodePrivate::remoteObjectAddresses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html

    Returns
    -------

    QHash[str, QRemoteObjectSourceLocationInfo]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QRemoteObjectSourceLocations
    #      QRemoteObjectNodePrivate::remoteObjectAddresses() const
    address = self.uglySide.call(
        'ritual_ZNK24QRemoteObjectNodePrivate21remoteObjectAddressesEv',
    )
    from . import QRemoteObjectSourceLocationInfo
    return QHash[str, QRemoteObjectSourceLocationInfo]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRemoteObjectNode.ErrorCode)
  def setLastError(self, errorCode: QRemoteObjectNode.ErrorCode) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectNodePrivate::setLastError(QRemoteObjectNode::ErrorCode
    errorCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html#setLastError

    Parameters
    ----------

    errorCode : QRemoteObjectNode.ErrorCode
      Passed on as its number.
    """
    #  void QRemoteObjectNodePrivate::setLastError(QRemoteObjectNode::
    #      ErrorCode errorCode)
    self.uglySide.call(
        'ritual_ZN24QRemoteObjectNodePrivate12setLastErrorEN17QRemoteObject'
        'Node9ErrorCodeE',
        errorCode.value,
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
    Qt's 'QRemoteObjectNodePrivate::QRemoteObjectNodePrivate()': leans on
    'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.__init__' has no cute function yet. Qt's "
        "'QRemoteObjectNodePrivate::QRemoteObjectNodePrivate()': leans on "
        "'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QObject, QRemoteObjectReplica)
  @overload(QObject, NoneType)
  @overload(NoneType, QRemoteObjectReplica)
  @overload(NoneType, NoneType)
  def connectReplica(
      self,
      object: Optional[QObject],
      instance: Optional[QRemoteObjectReplica],
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectNodePrivate::connectReplica(QObject
    *object, QRemoteObjectReplica *instance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html#connectReplica

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QRemoteObjectReplica]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectNodePrivate::connectReplica(QObject *object,
    #      QRemoteObjectReplica *instance)
    self.uglySide.call(
        'ritual_ZN24QRemoteObjectNodePrivate14connectReplicaEP7QObjectP20QR'
        'emoteObjectReplica',
        self._addressOf(object, 'QObject'), self._addressOf(instance),
    )

  @overload(str)
  def hasInstance(self, name: str) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectNodePrivate::hasInstance(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html#hasInstance

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QRemoteObjectNodePrivate::hasInstance(const QString &name)
    return self.uglySide.call(
        'ritual_ZN24QRemoteObjectNodePrivate11hasInstanceERK7QString', name,
    )

  @overload(QtROClientIoDevice)
  @overload(NoneType)
  def onShouldReconnect(
      self,
      ioDevice: Optional[QtROClientIoDevice],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectNodePrivate::onShouldReconnect(QtROClientIoDevice
    *ioDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html#onShouldReconnect

    Parameters
    ----------

    ioDevice : Optional[QtROClientIoDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectNodePrivate::onShouldReconnect(QtROClientIoDevice
    #      *ioDevice)
    self.uglySide.call(
        'ritual_ZN24QRemoteObjectNodePrivate17onShouldReconnectEP18QtROClie'
        'ntIoDevice',
        self._addressOf(ioDevice),
    )

  @overload(QMetaObject, QRemoteObjectReplica, str)
  @overload(QMetaObject, NoneType, str)
  @overload(NoneType, QRemoteObjectReplica, str)
  @overload(NoneType, NoneType, str)
  def handleNewAcquire(
      self,
      meta: Optional[QMetaObject],
      instance: Optional[QRemoteObjectReplica],
      name: str,
  ) -> Optional[QReplicaImplementationInterface]:
    """
    Calls Qt's 'QReplicaImplementationInterface
    *QRemoteObjectNodePrivate::handleNewAcquire(const QMetaObject *meta,
    QRemoteObjectReplica *instance, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html#handleNewAcquire

    Parameters
    ----------

    meta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QRemoteObjectReplica]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QReplicaImplementationInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QReplicaImplementationInterface
    #      *QRemoteObjectNodePrivate::handleNewAcquire(const QMetaObject
    #      *meta, QRemoteObjectReplica *instance, const QString &name)
    address = self.uglySide.call(
        'ritual_ZN24QRemoteObjectNodePrivate16handleNewAcquireEPK11QMetaObj'
        'ectP20QRemoteObjectReplicaRK7QString',
        self._addressOf(meta, 'QMetaObject'), self._addressOf(instance),
        name,
    )
    from . import QReplicaImplementationInterface
    return QReplicaImplementationInterface._cuteAt(address)

  @overload(QByteArray, QByteArray)
  def checkSignatures(self, a: QByteArray, b: QByteArray) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectNodePrivate::checkSignatures(const
    QByteArray &a, const QByteArray &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html#checkSignatures

    Parameters
    ----------

    a : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    b : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QRemoteObjectNodePrivate::checkSignatures(const QByteArray &a,
    #      const QByteArray &b)
    return self.uglySide.call(
        'ritual_ZN24QRemoteObjectNodePrivate15checkSignaturesERK10QByteArra'
        'yS2_',
        self._valueOf(a), self._valueOf(b),
    )

  def q_func(self) -> Optional[QRemoteObjectNode]:
    """
    Calls Qt's 'QRemoteObjectNode *QRemoteObjectNodePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnodeprivate.html#q_func

    Returns
    -------

    Optional[QRemoteObjectNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectNode *QRemoteObjectNodePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QRemoteObjectNodePrivate6q_funcEv',
    )
    return QRemoteObjectNode._cuteAt(address)

  @staticmethod
  def handlePointerToQObjectProperties(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::handlePointerToQObjectProperties(
    QConnectedReplicaImplementation *rep, QVariantList &properties)': leans
    on 'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.handlePointerToQObjectProperties' has no "
        "cute function yet. Qt's 'void "
        "QRemoteObjectNodePrivate::handlePointerToQObjectProperties(QConnect"
        "edReplicaImplementation *rep, QVariantList &properties)': leans on "
        "'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def handlePointerToQObjectProperty(*__, **_) -> Never:
    """
    Qt's 'QVariant QRemoteObjectNodePrivate::handlePointerToQObjectProperty(
    QConnectedReplicaImplementation *rep, int index, const QVariant
    &property)': leans on
    'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.handlePointerToQObjectProperty' has no "
        "cute function yet. Qt's 'QVariant "
        "QRemoteObjectNodePrivate::handlePointerToQObjectProperty(QConnected"
        "ReplicaImplementation *rep, int index, const QVariant &property)': "
        "leans on "
        "'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def handleReplicaConnection(*__, **_) -> Never:
    """
    - Qt's 'void QRemoteObjectNodePrivate::handleReplicaConnection(const
      QString &name)': leans on
      'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'void QRemoteObjectNodePrivate::handleReplicaConnection(const
      QByteArray &sourceSignature, QConnectedReplicaImplementation *rep,
      QtROIoDeviceBase *connection)': leans on
      'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.handleReplicaConnection' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectNodePrivate::handleReplicaConnection(const QString "
        "&name)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'void "
        "QRemoteObjectNodePrivate::handleReplicaConnection(const QByteArray "
        "&sourceSignature, QConnectedReplicaImplementation *rep, "
        "QtROIoDeviceBase *connection)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def initConnection(*__, **_) -> Never:
    """
    Qt's 'bool QRemoteObjectNodePrivate::initConnection(const QUrl
    &address)': leans on 'QRemoteObjectNodePrivate::onClientRead(QObject*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.initConnection' has no cute function "
        "yet. Qt's 'bool QRemoteObjectNodePrivate::initConnection(const "
        "QUrl &address)': leans on "
        "'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::initialize()': leans on
    'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.initialize' has no cute function yet. "
        "Qt's 'void QRemoteObjectNodePrivate::initialize()': leans on "
        "'qRegisterNormalizedMetaType_QRemoteObjectPackets__QRO_(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def onClientRead(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::onClientRead(QObject *obj)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'QRemoteObjectPacketTypeEnum'; did
    you mean 'QtRemoteObjects::QRemoteObjectPacketTypeEnum'?.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.onClientRead' has no cute function yet. "
        "Qt's 'void QRemoteObjectNodePrivate::onClientRead(QObject *obj)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name "
        "'QRemoteObjectPacketTypeEnum'; did you mean "
        "'QtRemoteObjects::QRemoteObjectPacketTypeEnum'?.")

  @staticmethod
  def onRegistryInitialized(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::onRegistryInitialized()': leans on
    'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.onRegistryInitialized' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectNodePrivate::onRegistryInitialized()': leans on "
        "'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def onRemoteObjectSourceAdded(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::onRemoteObjectSourceAdded(const
    QRemoteObjectSourceLocation &entry)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: invalid
    operands to binary expression ('QDebugIfHasDebugStream<QString,
    QRemoteObjectSourceLocationInfo>' (aka 'QDebug') and 'QHash<QString,
    QWeakPointer<QReplicaImplementationInterface>>').
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.onRemoteObjectSourceAdded' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectNodePrivate::onRemoteObjectSourceAdded(const "
        "QRemoteObjectSourceLocation &entry)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: invalid operands to binary expression "
        "('QDebugIfHasDebugStream<QString, "
        "QRemoteObjectSourceLocationInfo>' (aka 'QDebug') and "
        "'QHash<QString, QWeakPointer<QReplicaImplementationInterface>>').")

  @staticmethod
  def onRemoteObjectSourceRemoved(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::onRemoteObjectSourceRemoved(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.onRemoteObjectSourceRemoved' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectNodePrivate::onRemoteObjectSourceRemoved(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def openConnectionIfNeeded(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::openConnectionIfNeeded(const QString
    &name)': leans on 'QRemoteObjectNodePrivate::onClientRead(QObject*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.openConnectionIfNeeded' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectNodePrivate::openConnectionIfNeeded(const QString "
        "&name)': leans on "
        "'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setRegistry(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::setRegistry(QRemoteObjectRegistry
    *a0)': leans on 'QRemoteObjectNodePrivate::onClientRead(QObject*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.setRegistry' has no cute function yet. "
        "Qt's 'void "
        "QRemoteObjectNodePrivate::setRegistry(QRemoteObjectRegistry *a0)': "
        "leans on 'QRemoteObjectNodePrivate::onClientRead(QObject*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setRegistryUrlNodeImpl(*__, **_) -> Never:
    """
    Qt's 'bool QRemoteObjectNodePrivate::setRegistryUrlNodeImpl(const QUrl
    &registryAddr)': leans on
    'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.setRegistryUrlNodeImpl' has no cute "
        "function yet. Qt's 'bool "
        "QRemoteObjectNodePrivate::setRegistryUrlNodeImpl(const QUrl "
        "&registryAddr)': leans on "
        "'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setReplicaImplementation(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNodePrivate::setReplicaImplementation(const
    QMetaObject *a0, QRemoteObjectReplica *a1, const QString &a2)': leans on
    'QRemoteObjectNodePrivate::onClientRead(QObject*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectNodePrivate.setReplicaImplementation' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectNodePrivate::setReplicaImplementation(const "
        "QMetaObject *a0, QRemoteObjectReplica *a1, const QString &a2)': "
        "leans on 'QRemoteObjectNodePrivate::onClientRead(QObject*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
