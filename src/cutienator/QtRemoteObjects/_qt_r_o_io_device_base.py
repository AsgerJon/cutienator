"""
QtROIoDeviceBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject
  from . import QtROIoDeviceBasePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtROIoDeviceBase(QObject):
  """
  The cute side of Qt's QtROIoDeviceBase: a plain Python object standing in
  front of one C++ QtROIoDeviceBase.

  It is built on the cute 'QObject', as Qt's QtROIoDeviceBase is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtROIoDeviceBase that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'write', 'isOpen',
  'close', 'bytesAvailable', 'connection', 'initializeDataStream',
  'isClosing', 'addSource', 'removeSource', 'readyRead', 'disconnected',
  'deviceType', 'doClose', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtROIoDeviceBase::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QtROIoDeviceBase::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QtROIoDeviceBase::~QtROIoDeviceBase()': the destructor: Python
    never removes a C++ QtROIoDeviceBase.
  - Qt's 'bool
    QtROIoDeviceBase::read(QtRemoteObjects::QRemoteObjectPacketTypeEnum &a0,
    QString &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QSet<QString> QtROIoDeviceBase::remoteObjects() const': gives a
    type Python has no way to take yet.
  - Qt's 'QtROIoDeviceBase::QtROIoDeviceBase(QtROIoDeviceBasePrivate &a0,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QtROIoDeviceBasePrivate *QtROIoDeviceBase::d_func() const':
    takes in Python what 'QtROIoDeviceBasePrivate
    *QtROIoDeviceBase::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QtROIoDeviceBase is created at the first use, not by
    'QtROIoDeviceBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtROIoDeviceBase.
  - Qt tells when it has removed the C++ QtROIoDeviceBase. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtROIoDeviceBase that has no cute function yet, 'read',
    'remoteObjects', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QtROIoDeviceBase::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#tr

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
    #  QString QtROIoDeviceBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QtROIoDeviceBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROIoDeviceBase'

  #  A C++ QtROIoDeviceBase Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtROIoDeviceBase'

  #  The functions Qt calls itself that QtROIoDeviceBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'write': (
          ('_ZN16QtROIoDeviceBase5writeERK10QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
          ('_ZN16QtROIoDeviceBase5writeERK10QByteArrayx',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('long long', 'number', ''),
           )),
      ),
      'isOpen': (
          ('_ZNK16QtROIoDeviceBase6isOpenEv',
           ('bool', 'number', ''),
           ()),
      ),
      'close': (
          ('_ZN16QtROIoDeviceBase5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'bytesAvailable': (
          ('_ZNK16QtROIoDeviceBase14bytesAvailableEv',
           ('long long', 'number', ''),
           ()),
      ),
      'connection': (
          ('_ZNK16QtROIoDeviceBase10connectionEv',
           ('address', 'address', 'QtCore:QIODevice'),
           ()),
      ),
      'deviceType': (
          ('_ZNK16QtROIoDeviceBase10deviceTypeEv',
           ('address', 'text', ''),
           ()),
      ),
      'doClose': (
          ('_ZN16QtROIoDeviceBase7doCloseEv',
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
    Calls Qt's 'const QMetaObject *QtROIoDeviceBase::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtROIoDeviceBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QtROIoDeviceBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QtROIoDeviceBase::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#isOpen
    """
    #  bool QtROIoDeviceBase::isOpen() const
    ritual = 'ritual_ZNK16QtROIoDeviceBase6isOpenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QtROIoDeviceBase6isOpenEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QtROIoDeviceBase::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroiodevicebase.html#bytesAvailable
    """
    #  qint64 QtROIoDeviceBase::bytesAvailable() const
    ritual = 'ritual_ZNK16QtROIoDeviceBase14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QtROIoDeviceBase14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def connection(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QtROIoDeviceBase::connection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#connection

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QtROIoDeviceBase::connection() const
    address = self.uglySide.call(
        'ritual_ZNK16QtROIoDeviceBase10connectionEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def isClosing(self) -> bool:
    """
    Calls Qt's 'bool QtROIoDeviceBase::isClosing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#isClosing
    """
    #  bool QtROIoDeviceBase::isClosing() const
    return self.uglySide.call('ritual_ZNK16QtROIoDeviceBase9isClosingEv')

  def deviceType(self) -> str:
    """
    Calls Qt's 'QString QtROIoDeviceBase::deviceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#deviceType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtROIoDeviceBase::deviceType() const
    return self.uglySide.call('ritual_ZNK16QtROIoDeviceBase10deviceTypeEv')

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QtROIoDeviceBase::QtROIoDeviceBase(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroiodevicebase.html#QtROIoDeviceBase

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtROIoDeviceBase::QtROIoDeviceBase(QObject *parent)
    self._noteCreation(QtROIoDeviceBase, lambda: Rituals.call(
        'ritual_ZN16QtROIoDeviceBaseC1EP7QObject',
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

  @overload(QByteArray)
  def write(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::write(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#write

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtROIoDeviceBase::write(const QByteArray &data)
    ritual = 'ritual_ZN16QtROIoDeviceBase5writeERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QtROIoDeviceBase5writeERK10QByteArray'
    self.uglySide.call(ritual, self._valueOf(data))

  @overload(QByteArray, int)
  def write(self, data: QByteArray, a1: int) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::write(const QByteArray &data, qint64
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#write

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a1 : int
      Passed on as it is.
    """
    #  void QtROIoDeviceBase::write(const QByteArray &data, qint64 a1)
    ritual = 'ritual_ZN16QtROIoDeviceBase5writeERK10QByteArrayx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QtROIoDeviceBase5writeERK10QByteArrayx'
    self.uglySide.call(ritual, self._valueOf(data), a1)

  def close(self) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#close
    """
    #  void QtROIoDeviceBase::close()
    ritual = 'ritual_ZN16QtROIoDeviceBase5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QtROIoDeviceBase5closeEv'
    self.uglySide.call(ritual)

  def initializeDataStream(self) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::initializeDataStream()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroiodevicebase.html#initializeDataStream
    """
    #  void QtROIoDeviceBase::initializeDataStream()
    self.uglySide.call('ritual_ZN16QtROIoDeviceBase20initializeDataStreamEv')

  @overload(str)
  def addSource(self, a0: str) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::addSource(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#addSource

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtROIoDeviceBase::addSource(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QtROIoDeviceBase9addSourceERK7QString', a0,
    )

  @overload(str)
  def removeSource(self, a0: str) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::removeSource(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#removeSource

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtROIoDeviceBase::removeSource(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QtROIoDeviceBase12removeSourceERK7QString', a0,
    )

  def readyRead(self) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::readyRead()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#readyRead
    """
    #  void QtROIoDeviceBase::readyRead()
    self.uglySide.call('ritual_ZN16QtROIoDeviceBase9readyReadEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#disconnected
    """
    #  void QtROIoDeviceBase::disconnected()
    self.uglySide.call('ritual_ZN16QtROIoDeviceBase12disconnectedEv')

  def doClose(self) -> None:
    """
    Calls Qt's 'void QtROIoDeviceBase::doClose()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#doClose
    """
    #  void QtROIoDeviceBase::doClose()
    self.uglySide.call('ritual_ZN16QtROIoDeviceBase7doCloseEv')

  def d_func(self) -> Optional[QtROIoDeviceBasePrivate]:
    """
    Calls Qt's 'QtROIoDeviceBasePrivate *QtROIoDeviceBase::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroiodevicebase.html#d_func

    Returns
    -------

    Optional[QtROIoDeviceBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROIoDeviceBasePrivate *QtROIoDeviceBase::d_func()
    address = self.uglySide.call('ritual_ZN16QtROIoDeviceBase6d_funcEv')
    from . import QtROIoDeviceBasePrivate
    return QtROIoDeviceBasePrivate._cuteAt(address)

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'bool
    QtROIoDeviceBase::read(QtRemoteObjects::QRemoteObjectPacketTypeEnum &a0,
    QString &a1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtROIoDeviceBase.read' has no cute function yet. Qt's 'bool "
        "QtROIoDeviceBase::read(QtRemoteObjects::QRemoteObjectPacketTypeEnum"
        " &a0, QString &a1)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def remoteObjects(*__, **_) -> Never:
    """
    Qt's 'QSet<QString> QtROIoDeviceBase::remoteObjects() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtROIoDeviceBase.remoteObjects' has no cute function yet. Qt's "
        "'QSet<QString> QtROIoDeviceBase::remoteObjects() const': gives a "
        "type Python has no way to take yet.")
