"""
QRemoteObjectSourceIo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsourceio_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectSourceIo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectSourceIo(QObject):
  """
  The cute side of Qt's QRemoteObjectSourceIo: a plain Python object standing
  in front of one C++ QRemoteObjectSourceIo.

  It is built on the cute 'QObject', as Qt's QRemoteObjectSourceIo is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectSourceIo that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'disableRemoting',
  'serverAddress', 'handleConnection', 'onServerDisconnect', 'onServerRead',
  'serverRemoved'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectSourceIo::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QRemoteObjectSourceIo::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectSourceIo::~QRemoteObjectSourceIo()': the destructor:
    Python never removes a C++ QRemoteObjectSourceIo.
  - Qt's 'void QRemoteObjectSourceIo::remoteObjectAdded(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QRemoteObjectSourceIo::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  12 of the 24 functions Qt declares: 6 leans on 'QRemoteObjectSourceIo; 3
  leans on 'QRemoteObjectPackets; 2 not a gap; 1 leans on 'LocalServerImpl.

  What to expect
  --------------

  - The C++ QRemoteObjectSourceIo is created at the first use, not by
    'QRemoteObjectSourceIo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectSourceIo.
  - Qt tells when it has removed the C++ QRemoteObjectSourceIo. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectSourceIo that has no cute function yet,
    '__init__', 'enableRemoting', 'newConnection', 'registerSource',
    'remoteObjectAdded', 'remoteObjectRemoved', 'setSocketOptions',
    'startListening', 'unregisterSource', holds a function that raises
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
  __qt_class__ = 'QRemoteObjectSourceIo'

  #  A C++ QRemoteObjectSourceIo Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectSourceIo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRemoteObjectSourceIo::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourceio.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectSourceIo::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QRemoteObjectSourceIo10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def serverAddress(self) -> QUrl:
    """
    Calls Qt's 'QUrl QRemoteObjectSourceIo::serverAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourceio.html#serverAddress

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QRemoteObjectSourceIo::serverAddress() const
    address = self.uglySide.call(
        'ritual_ZNK21QRemoteObjectSourceIo13serverAddressEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QRemoteObjectSourceIo::QRemoteObjectSourceIo(const QUrl &address,
      QObject *parent)': leans on
      'QRemoteObjectSourceIo::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'QRemoteObjectSourceIo::QRemoteObjectSourceIo(QObject *parent)':
      leans on 'QRemoteObjectSourceIo::qt_metacall(QMetaObject::Call, int,
      void**)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.__init__' has no cute function yet. Qt's "
        "'QRemoteObjectSourceIo::QRemoteObjectSourceIo(const QUrl &address, "
        "QObject *parent)': leans on "
        "'QRemoteObjectSourceIo::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's "
        "'QRemoteObjectSourceIo::QRemoteObjectSourceIo(QObject *parent)': "
        "leans on 'QRemoteObjectSourceIo::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QObject)
  @overload(NoneType)
  def disableRemoting(self, object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectSourceIo::disableRemoting(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourceio.html#disableRemoting

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRemoteObjectSourceIo::disableRemoting(QObject *object)
    return self.uglySide.call(
        'ritual_ZN21QRemoteObjectSourceIo15disableRemotingEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def handleConnection(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectSourceIo::handleConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourceio.html#handleConnection
    """
    #  void QRemoteObjectSourceIo::handleConnection()
    self.uglySide.call(
        'ritual_ZN21QRemoteObjectSourceIo16handleConnectionEv',
    )

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def onServerDisconnect(self, obj: Optional[QObject] = None) -> None:
    """
    Calls Qt's 'void QRemoteObjectSourceIo::onServerDisconnect(QObject
    *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourceio.html#onServerDisconnect

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QRemoteObjectSourceIo::onServerDisconnect(QObject *obj)
    self.uglySide.call(
        'ritual_ZN21QRemoteObjectSourceIo18onServerDisconnectEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def onServerRead(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QRemoteObjectSourceIo::onServerRead(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourceio.html#onServerRead

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectSourceIo::onServerRead(QObject *obj)
    self.uglySide.call(
        'ritual_ZN21QRemoteObjectSourceIo12onServerReadEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(QUrl)
  def serverRemoved(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QRemoteObjectSourceIo::serverRemoved(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourceio.html#serverRemoved

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QRemoteObjectSourceIo::serverRemoved(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN21QRemoteObjectSourceIo13serverRemovedERK4QUrl',
        self._valueOf(url),
    )

  @staticmethod
  def enableRemoting(*__, **_) -> Never:
    """
    - Qt's 'bool QRemoteObjectSourceIo::enableRemoting(QObject *object, const
      QMetaObject *meta, const QString &name, const QString &typeName)':
      leans on 'QRemoteObjectPackets::CodecBase::send(QSet<QtROIoDeviceBase*>
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    - Qt's 'bool QRemoteObjectSourceIo::enableRemoting(QObject *object, const
      SourceApiMap *api, QObject *adapter)': leans on
      'QRemoteObjectPackets::CodecBase::send(QSet<QtROIoDeviceBase*>
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.enableRemoting' has no cute function yet. "
        "Qt's 'bool QRemoteObjectSourceIo::enableRemoting(QObject *object, "
        "const QMetaObject *meta, const QString &name, const QString "
        "&typeName)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QSet<QtROIoDeviceBase*> "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's 'bool "
        "QRemoteObjectSourceIo::enableRemoting(QObject *object, const "
        "SourceApiMap *api, QObject *adapter)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QSet<QtROIoDeviceBase*> "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def newConnection(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectSourceIo::newConnection(QtROIoDeviceBase *conn)':
    leans on 'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.newConnection' has no cute function yet. "
        "Qt's 'void QRemoteObjectSourceIo::newConnection(QtROIoDeviceBase "
        "*conn)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def registerSource(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectSourceIo::registerSource(QRemoteObjectSourceBase
    *source)': leans on
    'QRemoteObjectSourceIo::remoteObjectAdded(std::pair<QString,
    QRemoteObjectSourceLocationInfo> const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.registerSource' has no cute function yet. "
        "Qt's 'void "
        "QRemoteObjectSourceIo::registerSource(QRemoteObjectSourceBase "
        "*source)': leans on "
        "'QRemoteObjectSourceIo::remoteObjectAdded(std::pair<QString, "
        "QRemoteObjectSourceLocationInfo> const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def remoteObjectAdded(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectSourceIo::remoteObjectAdded(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.remoteObjectAdded' has no cute function "
        "yet. Qt's 'void QRemoteObjectSourceIo::remoteObjectAdded(const "
        "QRemoteObjectSourceLocation &a0)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def remoteObjectRemoved(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectSourceIo::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.remoteObjectRemoved' has no cute function "
        "yet. Qt's 'void QRemoteObjectSourceIo::remoteObjectRemoved(const "
        "QRemoteObjectSourceLocation &a0)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setSocketOptions(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectSourceIo::setSocketOptions(QLocalServer::SocketOptions
    options)': leans on 'LocalServerImpl::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.setSocketOptions' has no cute function yet. "
        "Qt's 'void "
        "QRemoteObjectSourceIo::setSocketOptions(QLocalServer::SocketOptions"
        " options)': leans on 'LocalServerImpl::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def startListening(*__, **_) -> Never:
    """
    Qt's 'bool QRemoteObjectSourceIo::startListening()': leans on
    'QRemoteObjectSourceIo::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.startListening' has no cute function yet. "
        "Qt's 'bool QRemoteObjectSourceIo::startListening()': leans on "
        "'QRemoteObjectSourceIo::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def unregisterSource(*__, **_) -> Never:
    """
    Qt's 'void
    QRemoteObjectSourceIo::unregisterSource(QRemoteObjectSourceBase
    *source)': leans on
    'QRemoteObjectSourceIo::remoteObjectRemoved(std::pair<QString,
    QRemoteObjectSourceLocationInfo> const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceIo.unregisterSource' has no cute function yet. "
        "Qt's 'void "
        "QRemoteObjectSourceIo::unregisterSource(QRemoteObjectSourceBase "
        "*source)': leans on "
        "'QRemoteObjectSourceIo::remoteObjectRemoved(std::pair<QString, "
        "QRemoteObjectSourceLocationInfo> const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
