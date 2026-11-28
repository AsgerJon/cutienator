"""
QWebChannel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebChannel/qwebchannel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QWebChannelAbstractTransport, QWebChannelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebChannelAbstractTransport = WAIT['QWebChannelAbstractTransport']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebChannel(QObject):
  """
  The cute side of Qt's QWebChannel: a plain Python object standing in front
  of one C++ QWebChannel.

  It is built on the cute 'QObject', as Qt's QWebChannel is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebChannel that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'registerObjects',
  'registeredObjects', 'registerObject', 'deregisterObject', 'blockUpdates',
  'setBlockUpdates', 'propertyUpdateInterval', 'setPropertyUpdateInterval',
  'blockUpdatesChanged', 'connectTo', 'disconnectFrom', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebChannel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWebChannel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWebChannel::~QWebChannel()': the destructor: Python never removes
    a C++ QWebChannel.
  - Qt's 'QBindable<bool> QWebChannel::bindableBlockUpdates()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<int> QWebChannel::bindablePropertyUpdateInterval()':
    gives a type Python has no way to take yet.
  - Qt's 'const QWebChannelPrivate *QWebChannel::d_func() const': takes in
    Python what 'QWebChannelPrivate *QWebChannel::d_func()' takes.
  - Qt's 'QWebChannel::QWebChannel(QWebChannelPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebChannel is created at the first use, not by
    'QWebChannel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebChannel.
  - Qt tells when it has removed the C++ QWebChannel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QWebChannel that has no cute function yet,
    'bindableBlockUpdates', 'bindablePropertyUpdateInterval', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QWebChannel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#tr

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
    #  QString QWebChannel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QWebChannel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebChannel'

  #  A C++ QWebChannel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebChannel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebChannel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebChannel::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QWebChannel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def registeredObjects(self) -> QHash[str, QObject]:
    """
    Calls Qt's 'QHash<QString, QObject *> QWebChannel::registeredObjects()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#registeredObjects

    Returns
    -------

    QHash[str, QObject]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QObject *> QWebChannel::registeredObjects() const
    address = self.uglySide.call(
        'ritual_ZNK11QWebChannel17registeredObjectsEv',
    )
    return QHash[str, QObject]._cuteOwning(address)

  def blockUpdates(self) -> bool:
    """
    Calls Qt's 'bool QWebChannel::blockUpdates() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#blockUpdates
    """
    #  bool QWebChannel::blockUpdates() const
    return self.uglySide.call('ritual_ZNK11QWebChannel12blockUpdatesEv')

  def propertyUpdateInterval(self) -> int:
    """
    Calls Qt's 'int QWebChannel::propertyUpdateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannel.html#propertyUpdateInterval
    """
    #  int QWebChannel::propertyUpdateInterval() const
    return self.uglySide.call(
        'ritual_ZNK11QWebChannel22propertyUpdateIntervalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setBlockUpdates(self, block: bool) -> None:
    """
    Calls Qt's 'void QWebChannel::setBlockUpdates(bool block)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#setBlockUpdates

    Parameters
    ----------

    block : bool
      Passed on as it is.
    """
    #  void QWebChannel::setBlockUpdates(bool block)
    self.uglySide.call('ritual_ZN11QWebChannel15setBlockUpdatesEb', block)

  @overload(int)
  def setPropertyUpdateInterval(self, ms: int) -> None:
    """
    Calls Qt's 'void QWebChannel::setPropertyUpdateInterval(int ms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannel.html#setPropertyUpdateInterval

    Parameters
    ----------

    ms : int
      Passed on as it is.
    """
    #  void QWebChannel::setPropertyUpdateInterval(int ms)
    self.uglySide.call(
        'ritual_ZN11QWebChannel25setPropertyUpdateIntervalEi', ms,
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
    Notes what was given, for Qt's 'QWebChannel::QWebChannel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#QWebChannel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebChannel::QWebChannel(QObject *parent)
    self._noteCreation(QWebChannel, lambda: Rituals.call(
        'ritual_ZN11QWebChannelC1EP7QObject',
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

  @overload(QHash[str, QObject])
  def registerObjects(self, objects: QHash[str, QObject]) -> None:
    """
    Calls Qt's 'void QWebChannel::registerObjects(const QHash<QString,
    QObject *> &objects)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#registerObjects

    Parameters
    ----------

    objects : QHash[str, QObject]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QWebChannel::registerObjects(const QHash<QString, QObject *>
    #      &objects)
    self.uglySide.call(
        'ritual_ZN11QWebChannel15registerObjectsERK5QHashI7QStringP7QObject'
        'E',
        self._valueOf(objects),
    )

  @overload(str, QObject)
  @overload(str, NoneType)
  def registerObject(self, id: str, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QWebChannel::registerObject(const QString &id, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#registerObject

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebChannel::registerObject(const QString &id, QObject *object)
    self.uglySide.call(
        'ritual_ZN11QWebChannel14registerObjectERK7QStringP7QObject',
        id, self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def deregisterObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QWebChannel::deregisterObject(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#deregisterObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebChannel::deregisterObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN11QWebChannel16deregisterObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(bool)
  def blockUpdatesChanged(self, block: bool) -> None:
    """
    Calls Qt's 'void QWebChannel::blockUpdatesChanged(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannel.html#blockUpdatesChanged

    Parameters
    ----------

    block : bool
      Passed on as it is.
    """
    #  void QWebChannel::blockUpdatesChanged(bool block)
    self.uglySide.call(
        'ritual_ZN11QWebChannel19blockUpdatesChangedEb', block,
    )

  @overload(QWebChannelAbstractTransport)
  @overload(NoneType)
  def connectTo(
      self,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void QWebChannel::connectTo(QWebChannelAbstractTransport
    *transport)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#connectTo

    Parameters
    ----------

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebChannel::connectTo(QWebChannelAbstractTransport *transport)
    self.uglySide.call(
        'ritual_ZN11QWebChannel9connectToEP28QWebChannelAbstractTransport',
        self._addressOf(transport),
    )

  @overload(QWebChannelAbstractTransport)
  @overload(NoneType)
  def disconnectFrom(
      self,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void QWebChannel::disconnectFrom(QWebChannelAbstractTransport
    *transport)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#disconnectFrom

    Parameters
    ----------

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebChannel::disconnectFrom(QWebChannelAbstractTransport
    #      *transport)
    self.uglySide.call(
        'ritual_ZN11QWebChannel14disconnectFromEP28QWebChannelAbstractTrans'
        'port',
        self._addressOf(transport),
    )

  def d_func(self) -> Optional[QWebChannelPrivate]:
    """
    Calls Qt's 'QWebChannelPrivate *QWebChannel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebchannel.html#d_func

    Returns
    -------

    Optional[QWebChannelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebChannelPrivate *QWebChannel::d_func()
    address = self.uglySide.call('ritual_ZN11QWebChannel6d_funcEv')
    from . import QWebChannelPrivate
    return QWebChannelPrivate._cuteAt(address)

  @staticmethod
  def bindableBlockUpdates(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QWebChannel::bindableBlockUpdates()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebChannel.bindableBlockUpdates' has no cute function yet. Qt's "
        "'QBindable<bool> QWebChannel::bindableBlockUpdates()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindablePropertyUpdateInterval(*__, **_) -> Never:
    """
    Qt's 'QBindable<int> QWebChannel::bindablePropertyUpdateInterval()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebChannel.bindablePropertyUpdateInterval' has no cute function "
        "yet. Qt's 'QBindable<int> "
        "QWebChannel::bindablePropertyUpdateInterval()': gives a type "
        "Python has no way to take yet.")
