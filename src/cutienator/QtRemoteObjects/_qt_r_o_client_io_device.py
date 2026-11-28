"""
QtROClientIoDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QRemoteObjectNode, QtROIoDeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QtROClientIoDevicePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtROClientIoDevice(QtROIoDeviceBase):
  """
  The cute side of Qt's QtROClientIoDevice: a plain Python object standing in
  front of one C++ QtROClientIoDevice.

  It is built on the cute 'QtROIoDeviceBase', as Qt's QtROClientIoDevice is
  built on Qt's QtROIoDeviceBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtROClientIoDevice that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr',
  'disconnectFromServer', 'connectToServer', 'url', 'shouldReconnect',
  'setError', 'doDisconnectFromServer', 'deviceType', 'setUrl', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtROClientIoDevice::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QtROClientIoDevice::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QtROClientIoDevice::~QtROClientIoDevice()': the destructor: Python
    never removes a C++ QtROClientIoDevice.
  - Qt's 'const QtROClientIoDevicePrivate *QtROClientIoDevice::d_func()
    const': takes in Python what 'QtROClientIoDevicePrivate
    *QtROClientIoDevice::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QtROClientIoDevice is created at the first use, not by
    'QtROClientIoDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtROClientIoDevice.
  - Qt tells when it has removed the C++ QtROClientIoDevice. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QtROClientIoDevice::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientiodevice.html#tr

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
    #  QString QtROClientIoDevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QtROClientIoDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROClientIoDevice'

  #  A C++ QtROClientIoDevice Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtROClientIoDevice'

  #  The functions Qt calls itself that QtROClientIoDevice is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'connectToServer': (
          ('_ZN18QtROClientIoDevice15connectToServerEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'doDisconnectFromServer': (
          ('_ZN18QtROClientIoDevice22doDisconnectFromServerEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QtROClientIoDevice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientiodevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtROClientIoDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtROClientIoDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QtROClientIoDevice::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientiodevice.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QtROClientIoDevice::url() const
    address = self.uglySide.call('ritual_ZNK18QtROClientIoDevice3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def deviceType(self) -> str:
    """
    Calls Qt's 'QString QtROClientIoDevice::deviceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientiodevice.html#deviceType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtROClientIoDevice::deviceType() const
    ritual = 'ritual_ZNK18QtROClientIoDevice10deviceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QtROClientIoDevice10deviceTypeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRemoteObjectNode.ErrorCode)
  def setError(self, a0: QRemoteObjectNode.ErrorCode) -> None:
    """
    Calls Qt's 'void
    QtROClientIoDevice::setError(QRemoteObjectNode::ErrorCode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientiodevice.html#setError

    Parameters
    ----------

    a0 : QRemoteObjectNode.ErrorCode
      Passed on as its number.
    """
    #  void QtROClientIoDevice::setError(QRemoteObjectNode::ErrorCode a0)
    self.uglySide.call(
        'ritual_ZN18QtROClientIoDevice8setErrorEN17QRemoteObjectNode9ErrorC'
        'odeE',
        a0.value,
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QtROClientIoDevice::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientiodevice.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QtROClientIoDevice::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN18QtROClientIoDevice6setUrlERK4QUrl', self._valueOf(url),
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
    'QtROClientIoDevice::QtROClientIoDevice(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroclientiodevice.html#QtROClientIoDevice

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtROClientIoDevice::QtROClientIoDevice(QObject *parent)
    self._noteCreation(QtROClientIoDevice, lambda: Rituals.call(
        'ritual_ZN18QtROClientIoDeviceC1EP7QObject',
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

  def disconnectFromServer(self) -> None:
    """
    Calls Qt's 'void QtROClientIoDevice::disconnectFromServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroclientiodevice.html#disconnectFromServer
    """
    #  void QtROClientIoDevice::disconnectFromServer()
    self.uglySide.call(
        'ritual_ZN18QtROClientIoDevice20disconnectFromServerEv',
    )

  def connectToServer(self) -> None:
    """
    Calls Qt's 'void QtROClientIoDevice::connectToServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroclientiodevice.html#connectToServer
    """
    #  void QtROClientIoDevice::connectToServer()
    self.uglySide.call('ritual_ZN18QtROClientIoDevice15connectToServerEv')

  @overload(THIS)
  @overload(NoneType)
  def shouldReconnect(self, a0: Optional[QtROClientIoDevice]) -> None:
    """
    Calls Qt's 'void QtROClientIoDevice::shouldReconnect(QtROClientIoDevice
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroclientiodevice.html#shouldReconnect

    Parameters
    ----------

    a0 : Optional[QtROClientIoDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtROClientIoDevice::shouldReconnect(QtROClientIoDevice *a0)
    self.uglySide.call(
        'ritual_ZN18QtROClientIoDevice15shouldReconnectEPS_',
        self._addressOf(a0),
    )

  def doDisconnectFromServer(self) -> None:
    """
    Calls Qt's 'void QtROClientIoDevice::doDisconnectFromServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroclientiodevice.html#doDisconnectFromServer
    """
    #  void QtROClientIoDevice::doDisconnectFromServer()
    self.uglySide.call(
        'ritual_ZN18QtROClientIoDevice22doDisconnectFromServerEv',
    )

  def d_func(self) -> Optional[QtROClientIoDevicePrivate]:
    """
    Calls Qt's 'QtROClientIoDevicePrivate *QtROClientIoDevice::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientiodevice.html#d_func

    Returns
    -------

    Optional[QtROClientIoDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROClientIoDevicePrivate *QtROClientIoDevice::d_func()
    address = self.uglySide.call('ritual_ZN18QtROClientIoDevice6d_funcEv')
    from . import QtROClientIoDevicePrivate
    return QtROClientIoDevicePrivate._cuteAt(address)
