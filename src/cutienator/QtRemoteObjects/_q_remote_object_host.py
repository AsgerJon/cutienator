"""
QRemoteObjectHost binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtNetwork import QLocalServer
from . import QRemoteObjectHostBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QRemoteObjectHostPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectHost(QRemoteObjectHostBase):
  """
  The cute side of Qt's QRemoteObjectHost: a plain Python object standing in
  front of one C++ QRemoteObjectHost.

  It is built on the cute 'QRemoteObjectHostBase', as Qt's QRemoteObjectHost
  is built on Qt's QRemoteObjectHostBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectHost that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'hostUrl',
  'setHostUrl', 'setLocalServerOptions', 'hostUrlChanged', 'd_func'. It can
  be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectHost::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QRemoteObjectHost::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectHost::~QRemoteObjectHost()': the destructor: Python
    never removes a C++ QRemoteObjectHost.
  - Qt's 'QRemoteObjectHost::QRemoteObjectHost(QRemoteObjectHostPrivate &a0,
    QObject *a1)': takes a type Python has no way to hand over yet.
  - Qt's 'const QRemoteObjectHostPrivate *QRemoteObjectHost::d_func() const':
    takes in Python what 'QRemoteObjectHostPrivate
    *QRemoteObjectHost::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QRemoteObjectHost is created at the first use, not by
    'QRemoteObjectHost(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectHost.
  - Qt tells when it has removed the C++ QRemoteObjectHost. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QRemoteObjectHost::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthost.html#tr

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
    #  QString QRemoteObjectHost::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QRemoteObjectHost2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QLocalServer.SocketOptions)
  def setLocalServerOptions(options: QLocalServer.SocketOptions) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectHost::setLocalServerOptions(QLocalServer::SocketOptions
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthost.html#setLocalServerOptions

    Parameters
    ----------

    options : QLocalServer.SocketOptions
      Passed on as its number.
    """
    #  void QRemoteObjectHost::setLocalServerOptions(QLocalServer::
    #      SocketOptions options)
    Rituals.call(
        'ritual_ZN17QRemoteObjectHost21setLocalServerOptionsE6QFlagsIN12QLo'
        'calServer12SocketOptionEE',
        options.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectHost'

  #  A C++ QRemoteObjectHost Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectHost'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRemoteObjectHost::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthost.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectHost::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QRemoteObjectHost10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hostUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QRemoteObjectHost::hostUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthost.html#hostUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QRemoteObjectHost::hostUrl() const
    ritual = 'ritual_ZNK17QRemoteObjectHost7hostUrlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QRemoteObjectHost7hostUrlEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  @overload(QUrl, QRemoteObjectHostBase.AllowedSchemas)
  def setHostUrl(
      self,
      hostAddress: QUrl,
      allowedSchemas: QRemoteObjectHostBase.AllowedSchemas = (
          QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly),
  ) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectHost::setHostUrl(const QUrl &hostAddress,
    AllowedSchemas allowedSchemas)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthost.html#setHostUrl

    Parameters
    ----------

    hostAddress : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    allowedSchemas : QRemoteObjectHostBase.AllowedSchemas
      Passed on as its number. May be left out, as in Qt: it is then
      QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly.
    """
    #  bool QRemoteObjectHost::setHostUrl(const QUrl &hostAddress,
    #      AllowedSchemas allowedSchemas)
    ritual = (
        'ritual_ZN17QRemoteObjectHost10setHostUrlERK4QUrlN21QRemoteObjectHo'
        'stBase14AllowedSchemasE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QRemoteObjectHost10setHostUrlERK4QUrlN21QRemoteOb'
          'jectHostBase14AllowedSchemasE')
    return self.uglySide.call(
        ritual, self._valueOf(hostAddress), allowedSchemas.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectHost::QRemoteObjectHost(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthost.html#QRemoteObjectHost

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectHost::QRemoteObjectHost(QObject *parent)
    self._noteCreation(QRemoteObjectHost, lambda: Rituals.call(
        'ritual_ZN17QRemoteObjectHostC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QUrl)
  @overload(QUrl, QUrl)
  @overload(QUrl, QUrl, QRemoteObjectHostBase.AllowedSchemas)
  @overload(QUrl, QUrl, QRemoteObjectHostBase.AllowedSchemas, QObject)
  @overload(QUrl, QUrl, QRemoteObjectHostBase.AllowedSchemas, NoneType)
  def __init__(
      self,
      address: QUrl,
      registryAddress: Optional[QUrl] = None,
      allowedSchemas: QRemoteObjectHostBase.AllowedSchemas = (
          QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly),
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectHost::QRemoteObjectHost(const QUrl &address, const QUrl
    &registryAddress, AllowedSchemas allowedSchemas, QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthost.html#QRemoteObjectHost

    Parameters
    ----------

    address : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    registryAddress : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.

    allowedSchemas : QRemoteObjectHostBase.AllowedSchemas
      Passed on as its number. May be left out, as in Qt: it is then
      QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectHost::QRemoteObjectHost(const QUrl &address, const QUrl
    #      &registryAddress, AllowedSchemas allowedSchemas, QObject *parent)
    if registryAddress is None:
      from ..QtCore import QUrl
      registryAddress = QUrl()
    self._noteCreation(QRemoteObjectHost, lambda: Rituals.call(
        'ritual_ZN17QRemoteObjectHostC1ERK4QUrlS2_N21QRemoteObjectHostBase1'
        '4AllowedSchemasEP7QObject',
        self._valueOf(address), self._valueOf(registryAddress),
        allowedSchemas.value, self._addressOf(parent, 'QObject'),
    ))

  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def __init__(self, address: QUrl, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectHost::QRemoteObjectHost(const QUrl &address, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthost.html#QRemoteObjectHost

    Parameters
    ----------

    address : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRemoteObjectHost::QRemoteObjectHost(const QUrl &address, QObject
    #      *parent)
    self._noteCreation(QRemoteObjectHost, lambda: Rituals.call(
        'ritual_ZN17QRemoteObjectHostC1ERK4QUrlP7QObject',
        self._valueOf(address), self._addressOf(parent, 'QObject'),
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

  def hostUrlChanged(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectHost::hostUrlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthost.html#hostUrlChanged
    """
    #  void QRemoteObjectHost::hostUrlChanged()
    self.uglySide.call('ritual_ZN17QRemoteObjectHost14hostUrlChangedEv')

  def d_func(self) -> Optional[QRemoteObjectHostPrivate]:
    """
    Calls Qt's 'QRemoteObjectHostPrivate *QRemoteObjectHost::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthost.html#d_func

    Returns
    -------

    Optional[QRemoteObjectHostPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectHostPrivate *QRemoteObjectHost::d_func()
    address = self.uglySide.call('ritual_ZN17QRemoteObjectHost6d_funcEv')
    from . import QRemoteObjectHostPrivate
    return QRemoteObjectHostPrivate._cuteAt(address)
