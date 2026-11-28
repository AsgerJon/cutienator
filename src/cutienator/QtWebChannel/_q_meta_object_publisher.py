"""
QMetaObjectPublisher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebChannel/6.12.0/QtWebChannel/private/qmetaobjectpublisher_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QMetaObjectPublisher to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonArray, QJsonObject, QJsonValue, QMetaMethod
  from ..QtCore import QMetaObject, QTimerEvent, QVariant
  from . import QWebChannel, QWebChannelAbstractTransport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']
  QJsonValue = WAIT['QJsonValue']
  QMetaMethod = WAIT['QMetaMethod']
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']
  QWebChannel = WAIT['QWebChannel']
  QWebChannelAbstractTransport = WAIT['QWebChannelAbstractTransport']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaObjectPublisher(QObject):
  """
  The cute side of Qt's QMetaObjectPublisher: a plain Python object standing
  in front of one C++ QMetaObjectPublisher.

  It is built on the cute 'QObject', as Qt's QMetaObjectPublisher is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMetaObjectPublisher that has a ritual and that
  Python can call so far, 39 names in all: 'metaObject', 'tr',
  'registerObject', 'broadcastMessage', 'enqueueBroadcastMessage',
  'enqueueMessage', 'sendEnqueuedPropertyUpdates', 'classInfoForObject',
  'setClientIsIdle', 'isClientIdle', 'initializeClient',
  'sendPendingPropertyUpdates', 'setProperty', 'signalEmitted',
  'propertyValueChanged', 'startPropertyUpdateTimer', 'objectDestroyed',
  'unwrapObject', 'unwrapMap', 'unwrapList', 'unwrapVariant', 'toVariant',
  'conversionScore', 'methodOverloadBadness', 'transportRemoved',
  'wrapResult', 'wrapList', 'wrapMap', 'deleteWrappedObject',
  'propertyUpdateInterval', 'setPropertyUpdateInterval', 'setBlockUpdates',
  'blockUpdates', 'blockUpdatesChanged', 'handleMessage', 'timerEvent',
  'onBlockUpdatesChanged', '_qt_property_blockUpdatesStatus_offset',
  '_qt_property_propertyUpdateIntervalTime_offset'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMetaObjectPublisher::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QMetaObjectPublisher::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QMetaObjectPublisher::~QMetaObjectPublisher()': the destructor:
    Python never removes a C++ QMetaObjectPublisher.
  - Qt's 'void QMetaObjectPublisher::initializePropertyUpdates(QObject *const
    object, const QJsonObject &objectInfo)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QVariant QMetaObjectPublisher::invokeMethod_helper(QObject *const
    object, const QMetaMethod &method, const QJsonArray &args)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QVariant QMetaObjectPublisher::invokeMethod(QObject *const object,
    const QMetaMethod &method, const QJsonArray &args)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVariant QMetaObjectPublisher::invokeMethod(QObject *const object,
    const int methodIndex, const QJsonArray &args)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QVariant QMetaObjectPublisher::invokeMethod(QObject *const object,
    const QByteArray &methodName, const QJsonArray &args)': takes a type
    Python has no way to hand over yet.
  - Qt's 'SignalHandler<QMetaObjectPublisher>
    *QMetaObjectPublisher::signalHandlerFor(const QObject *object)': gives
    'SignalHandler<QMetaObjectPublisher>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QMetaObjectPublisher is created at the first use, not by
    'QMetaObjectPublisher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetaObjectPublisher.
  - Qt tells when it has removed the C++ QMetaObjectPublisher. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QMetaObjectPublisher that has no cute function yet,
    'initializePropertyUpdates', 'invokeMethod', 'invokeMethod_helper',
    'signalHandlerFor', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QMetaObjectPublisher::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectpublisher.html#tr

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
    #  QString QMetaObjectPublisher::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QMetaObjectPublisher2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_blockUpdatesStatus_offset() -> int:
    """
    Calls Qt's 'size_t
    QMetaObjectPublisher::_qt_property_blockUpdatesStatus_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html
    """
    #  size_t QMetaObjectPublisher::_qt_property_blockUpdatesStatus_offset()
    return Rituals.call(
        'ritual_ZN20QMetaObjectPublisher38_qt_property_blockUpdatesStatus_o'
        'ffsetEv',
    )

  @staticmethod
  def _qt_property_propertyUpdateIntervalTime_offset() -> int:
    """
    Calls Qt's 'size_t
    QMetaObjectPublisher::_qt_property_propertyUpdateIntervalTime_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html
    """
    #  size_t QMetaObjectPublisher::
    #      _qt_property_propertyUpdateIntervalTime_offset()
    return Rituals.call(
        'ritual_ZN20QMetaObjectPublisher46_qt_property_propertyUpdateInterv'
        'alTime_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaObjectPublisher'

  #  A C++ QMetaObjectPublisher Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMetaObjectPublisher'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaObjectPublisher::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaObjectPublisher::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def unwrapObject(self, objectId: str) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMetaObjectPublisher::unwrapObject(const QString
    &objectId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#unwrapObject

    Parameters
    ----------

    objectId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QMetaObjectPublisher::unwrapObject(const QString &objectId)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher12unwrapObjectERK7QString',
        objectId,
    )
    return QObject._cuteAt(address)

  @overload(QMap[str, QVariant])
  def unwrapMap(self, map: QMap[str, QVariant]) -> QVariant:
    """
    Calls Qt's 'QVariant QMetaObjectPublisher::unwrapMap(QVariantMap map)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#unwrapMap

    Parameters
    ----------

    map : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMetaObjectPublisher::unwrapMap(QVariantMap map) const
    address = self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher9unwrapMapE4QMapI7QString8QVariant'
        'E',
        self._valueOf(map),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QList[QVariant])
  def unwrapList(self, list: QList[QVariant]) -> QVariant:
    """
    Calls Qt's 'QVariant QMetaObjectPublisher::unwrapList(QVariantList list)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#unwrapList

    Parameters
    ----------

    list : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMetaObjectPublisher::unwrapList(QVariantList list) const
    address = self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher10unwrapListE5QListI8QVariantE',
        self._valueOf(list),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def unwrapVariant(self, value: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QMetaObjectPublisher::unwrapVariant(const QVariant
    &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#unwrapVariant

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMetaObjectPublisher::unwrapVariant(const QVariant &value)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher13unwrapVariantERK8QVariant',
        self._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QJsonValue, int)
  def toVariant(self, value: QJsonValue, targetType: int) -> QVariant:
    """
    Calls Qt's 'QVariant QMetaObjectPublisher::toVariant(const QJsonValue
    &value, int targetType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#toVariant

    Parameters
    ----------

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.

    targetType : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMetaObjectPublisher::toVariant(const QJsonValue &value, int
    #      targetType) const
    address = self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher9toVariantERK10QJsonValuei',
        self._valueOf(value), targetType,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QJsonValue, int)
  def conversionScore(self, value: QJsonValue, targetType: int) -> int:
    """
    Calls Qt's 'int QMetaObjectPublisher::conversionScore(const QJsonValue
    &value, int targetType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#conversionScore

    Parameters
    ----------

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.

    targetType : int
      Passed on as it is.
    """
    #  int QMetaObjectPublisher::conversionScore(const QJsonValue &value, int
    #      targetType) const
    return self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher15conversionScoreERK10QJsonValuei',
        self._valueOf(value), targetType,
    )

  @overload(QMetaMethod, QJsonArray)
  def methodOverloadBadness(
      self,
      method: QMetaMethod,
      args: QJsonArray,
  ) -> int:
    """
    Calls Qt's 'int QMetaObjectPublisher::methodOverloadBadness(const
    QMetaMethod &method, const QJsonArray &args) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#methodOverloadBadness

    Parameters
    ----------

    method : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.

    args : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  int QMetaObjectPublisher::methodOverloadBadness(const QMetaMethod
    #      &method, const QJsonArray &args) const
    return self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher21methodOverloadBadnessERK11QMetaM'
        'ethodRK10QJsonArray',
        self._valueOf(method), self._valueOf(args),
    )

  def blockUpdates(self) -> bool:
    """
    Calls Qt's 'bool QMetaObjectPublisher::blockUpdates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#blockUpdates
    """
    #  bool QMetaObjectPublisher::blockUpdates() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher12blockUpdatesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool, QWebChannelAbstractTransport)
  @overload(bool, NoneType)
  def setClientIsIdle(
      self,
      isIdle: bool,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::setClientIsIdle(bool isIdle,
    QWebChannelAbstractTransport *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#setClientIsIdle

    Parameters
    ----------

    isIdle : bool
      Passed on as it is.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::setClientIsIdle(bool isIdle,
    #      QWebChannelAbstractTransport *transport)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher15setClientIsIdleEbP28QWebChannelAb'
        'stractTransport',
        isIdle, self._addressOf(transport),
    )

  @overload(QObject, int, QJsonValue)
  @overload(NoneType, int, QJsonValue)
  def setProperty(
      self,
      object: Optional[QObject],
      propertyIndex: int,
      value: QJsonValue,
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::setProperty(QObject *object, const
    int propertyIndex, const QJsonValue &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#setProperty

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QMetaObjectPublisher::setProperty(QObject *object, const int
    #      propertyIndex, const QJsonValue &value)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher11setPropertyEP7QObjectiRK10QJsonVa'
        'lue',
        self._addressOf(object, 'QObject'), propertyIndex,
        self._valueOf(value),
    )

  @overload(int)
  def setPropertyUpdateInterval(self, ms: int) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::setPropertyUpdateInterval(int
    ms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html

    Parameters
    ----------

    ms : int
      Passed on as it is.
    """
    #  void QMetaObjectPublisher::setPropertyUpdateInterval(int ms)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher25setPropertyUpdateIntervalEi', ms,
    )

  @overload(bool)
  def setBlockUpdates(self, block: bool) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::setBlockUpdates(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#setBlockUpdates

    Parameters
    ----------

    block : bool
      Passed on as it is.
    """
    #  void QMetaObjectPublisher::setBlockUpdates(bool block)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher15setBlockUpdatesEb', block,
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

  @overload(QWebChannel)
  @overload(NoneType)
  def __init__(self, webChannel: Optional[QWebChannel]) -> None:
    """
    Notes what was given, for Qt's
    'QMetaObjectPublisher::QMetaObjectPublisher(QWebChannel *webChannel)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#QMetaObjectPublisher

    Parameters
    ----------

    webChannel : Optional[QWebChannel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMetaObjectPublisher::QMetaObjectPublisher(QWebChannel *webChannel)
    self._noteCreation(QMetaObjectPublisher, lambda: Rituals.call(
        'ritual_ZN20QMetaObjectPublisherC1EP11QWebChannel',
        self._addressOf(webChannel),
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

  @overload(str, QObject)
  @overload(str, NoneType)
  def registerObject(self, id: str, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::registerObject(const QString &id,
    QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#registerObject

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::registerObject(const QString &id, QObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher14registerObjectERK7QStringP7QObjec'
        't',
        id, self._addressOf(object, 'QObject'),
    )

  @overload(QJsonObject)
  def broadcastMessage(self, message: QJsonObject) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::broadcastMessage(const QJsonObject
    &message) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#broadcastMessage

    Parameters
    ----------

    message : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QMetaObjectPublisher::broadcastMessage(const QJsonObject
    #      &message) const
    self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher16broadcastMessageERK11QJsonObject',
        self._valueOf(message),
    )

  @overload(QJsonObject)
  def enqueueBroadcastMessage(self, message: QJsonObject) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::enqueueBroadcastMessage(const
    QJsonObject &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#enqueueBroadcastMessage

    Parameters
    ----------

    message : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QMetaObjectPublisher::enqueueBroadcastMessage(const QJsonObject
    #      &message)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher23enqueueBroadcastMessageERK11QJson'
        'Object',
        self._valueOf(message),
    )

  @overload(QJsonObject, QWebChannelAbstractTransport)
  @overload(QJsonObject, NoneType)
  def enqueueMessage(
      self,
      message: QJsonObject,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::enqueueMessage(const QJsonObject
    &message, QWebChannelAbstractTransport *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#enqueueMessage

    Parameters
    ----------

    message : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::enqueueMessage(const QJsonObject &message,
    #      QWebChannelAbstractTransport *transport)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher14enqueueMessageERK11QJsonObjectP28'
        'QWebChannelAbstractTransport',
        self._valueOf(message), self._addressOf(transport),
    )

  @overload(QWebChannelAbstractTransport)
  @overload(NoneType)
  def sendEnqueuedPropertyUpdates(
      self,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::sendEnqueuedPropertyUpdates(
    QWebChannelAbstractTransport *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html

    Parameters
    ----------

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::sendEnqueuedPropertyUpdates(
    #      QWebChannelAbstractTransport *transport)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher27sendEnqueuedPropertyUpdatesEP28QW'
        'ebChannelAbstractTransport',
        self._addressOf(transport),
    )

  @overload(QObject, QWebChannelAbstractTransport)
  @overload(QObject, NoneType)
  @overload(NoneType, QWebChannelAbstractTransport)
  @overload(NoneType, NoneType)
  def classInfoForObject(
      self,
      object: Optional[QObject],
      transport: Optional[QWebChannelAbstractTransport],
  ) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QMetaObjectPublisher::classInfoForObject(const
    QObject *object, QWebChannelAbstractTransport *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#classInfoForObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QMetaObjectPublisher::classInfoForObject(const QObject
    #      *object, QWebChannelAbstractTransport *transport)
    address = self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher18classInfoForObjectEPK7QObjectP28Q'
        'WebChannelAbstractTransport',
        self._addressOf(object, 'QObject'), self._addressOf(transport),
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  @overload(QWebChannelAbstractTransport)
  @overload(NoneType)
  def isClientIdle(
      self,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> bool:
    """
    Calls Qt's 'bool
    QMetaObjectPublisher::isClientIdle(QWebChannelAbstractTransport
    *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#isClientIdle

    Parameters
    ----------

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetaObjectPublisher::isClientIdle(QWebChannelAbstractTransport
    #      *transport)
    return self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher12isClientIdleEP28QWebChannelAbstra'
        'ctTransport',
        self._addressOf(transport),
    )

  @overload(QWebChannelAbstractTransport)
  @overload(NoneType)
  def initializeClient(
      self,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject
    QMetaObjectPublisher::initializeClient(QWebChannelAbstractTransport
    *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#initializeClient

    Parameters
    ----------

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QMetaObjectPublisher::initializeClient(
    #      QWebChannelAbstractTransport *transport)
    address = self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher16initializeClientEP28QWebChannelAb'
        'stractTransport',
        self._addressOf(transport),
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  def sendPendingPropertyUpdates(self) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::sendPendingPropertyUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html
    """
    #  void QMetaObjectPublisher::sendPendingPropertyUpdates()
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher26sendPendingPropertyUpdatesEv',
    )

  @overload(QObject, int, QList[QVariant])
  @overload(NoneType, int, QList[QVariant])
  def signalEmitted(
      self,
      object: Optional[QObject],
      signalIndex: int,
      arguments: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::signalEmitted(const QObject
    *object, const int signalIndex, const QVariantList &arguments)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#signalEmitted

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signalIndex : int
      Passed on as it is.

    arguments : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QMetaObjectPublisher::signalEmitted(const QObject *object, const
    #      int signalIndex, const QVariantList &arguments)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher13signalEmittedEPK7QObjectiRK5QList'
        'I8QVariantE',
        self._addressOf(object, 'QObject'), signalIndex,
        self._valueOf(arguments),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def propertyValueChanged(
      self,
      object: Optional[QObject],
      propertyIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::propertyValueChanged(const QObject
    *object, const int propertyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#propertyValueChanged

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.
    """
    #  void QMetaObjectPublisher::propertyValueChanged(const QObject *object,
    #      const int propertyIndex)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher20propertyValueChangedEPK7QObjecti',
        self._addressOf(object, 'QObject'), propertyIndex,
    )

  @overload()
  @overload(bool)
  def startPropertyUpdateTimer(self, forceRestart: bool = False) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::startPropertyUpdateTimer(bool
    forceRestart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#startPropertyUpdateTimer

    Parameters
    ----------

    forceRestart : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QMetaObjectPublisher::startPropertyUpdateTimer(bool forceRestart)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher24startPropertyUpdateTimerEb',
        forceRestart,
    )

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::objectDestroyed(const QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#objectDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::objectDestroyed(const QObject *object)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher15objectDestroyedEPK7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QWebChannelAbstractTransport)
  @overload(NoneType)
  def transportRemoved(
      self,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void
    QMetaObjectPublisher::transportRemoved(QWebChannelAbstractTransport
    *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#transportRemoved

    Parameters
    ----------

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::transportRemoved(
    #      QWebChannelAbstractTransport *transport)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher16transportRemovedEP28QWebChannelAb'
        'stractTransport',
        self._addressOf(transport),
    )

  @overload(QVariant, QWebChannelAbstractTransport)
  @overload(QVariant, NoneType)
  @overload(QVariant, QWebChannelAbstractTransport, str)
  @overload(QVariant, NoneType, str)
  def wrapResult(
      self,
      result: QVariant,
      transport: Optional[QWebChannelAbstractTransport],
      parentObjectId: str = '',
  ) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QMetaObjectPublisher::wrapResult(const QVariant
    &result, QWebChannelAbstractTransport *transport, const QString
    &parentObjectId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#wrapResult

    Parameters
    ----------

    result : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentObjectId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QMetaObjectPublisher::wrapResult(const QVariant &result,
    #      QWebChannelAbstractTransport *transport, const QString
    #      &parentObjectId)
    address = self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher10wrapResultERK8QVariantP28QWebChan'
        'nelAbstractTransportRK7QString',
        self._valueOf(result), self._addressOf(transport), parentObjectId,
    )
    from ..QtCore import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(QList[QVariant], QWebChannelAbstractTransport)
  @overload(QList[QVariant], NoneType)
  @overload(QList[QVariant], QWebChannelAbstractTransport, str)
  @overload(QList[QVariant], NoneType, str)
  def wrapList(
      self,
      list: QList[QVariant],
      transport: Optional[QWebChannelAbstractTransport],
      parentObjectId: str = '',
  ) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QMetaObjectPublisher::wrapList(const QVariantList
    &list, QWebChannelAbstractTransport *transport, const QString
    &parentObjectId)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectpublisher.html#wrapList

    Parameters
    ----------

    list : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentObjectId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QMetaObjectPublisher::wrapList(const QVariantList &list,
    #      QWebChannelAbstractTransport *transport, const QString
    #      &parentObjectId)
    address = self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher8wrapListERK5QListI8QVariantEP28QWe'
        'bChannelAbstractTransportRK7QString',
        self._valueOf(list), self._addressOf(transport), parentObjectId,
    )
    from ..QtCore import QJsonArray
    return QJsonArray._cuteOwning(address)

  @overload(QMap[str, QVariant], QWebChannelAbstractTransport)
  @overload(QMap[str, QVariant], NoneType)
  @overload(QMap[str, QVariant], QWebChannelAbstractTransport, str)
  @overload(QMap[str, QVariant], NoneType, str)
  def wrapMap(
      self,
      map: QMap[str, QVariant],
      transport: Optional[QWebChannelAbstractTransport],
      parentObjectId: str = '',
  ) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QMetaObjectPublisher::wrapMap(const QVariantMap
    &map, QWebChannelAbstractTransport *transport, const QString
    &parentObjectId)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectpublisher.html#wrapMap

    Parameters
    ----------

    map : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentObjectId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QMetaObjectPublisher::wrapMap(const QVariantMap &map,
    #      QWebChannelAbstractTransport *transport, const QString
    #      &parentObjectId)
    address = self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher7wrapMapERK4QMapI7QString8QVariantE'
        'P28QWebChannelAbstractTransportRKS1_',
        self._valueOf(map), self._addressOf(transport), parentObjectId,
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  @overload(QObject)
  @overload(NoneType)
  def deleteWrappedObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::deleteWrappedObject(QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#deleteWrappedObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::deleteWrappedObject(QObject *object) const
    self.uglySide.call(
        'ritual_ZNK20QMetaObjectPublisher19deleteWrappedObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def propertyUpdateInterval(self) -> int:
    """
    Calls Qt's 'int QMetaObjectPublisher::propertyUpdateInterval()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#propertyUpdateInterval
    """
    #  int QMetaObjectPublisher::propertyUpdateInterval()
    return self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher22propertyUpdateIntervalEv',
    )

  @overload(bool)
  def blockUpdatesChanged(self, block: bool) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::blockUpdatesChanged(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#blockUpdatesChanged

    Parameters
    ----------

    block : bool
      Passed on as it is.
    """
    #  void QMetaObjectPublisher::blockUpdatesChanged(bool block)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher19blockUpdatesChangedEb', block,
    )

  @overload(QJsonObject, QWebChannelAbstractTransport)
  @overload(QJsonObject, NoneType)
  def handleMessage(
      self,
      message: QJsonObject,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::handleMessage(const QJsonObject
    &message, QWebChannelAbstractTransport *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#handleMessage

    Parameters
    ----------

    message : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::handleMessage(const QJsonObject &message,
    #      QWebChannelAbstractTransport *transport)
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher13handleMessageERK11QJsonObjectP28Q'
        'WebChannelAbstractTransport',
        self._valueOf(message), self._addressOf(transport),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::timerEvent(QTimerEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectPublisher::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN20QMetaObjectPublisher10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QMetaObjectPublisher10timerEventEP11QTimerEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  def onBlockUpdatesChanged(self) -> None:
    """
    Calls Qt's 'void QMetaObjectPublisher::onBlockUpdatesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectpublisher.html#onBlockUpdatesChanged
    """
    #  void QMetaObjectPublisher::onBlockUpdatesChanged()
    self.uglySide.call(
        'ritual_ZN20QMetaObjectPublisher21onBlockUpdatesChangedEv',
    )

  @staticmethod
  def initializePropertyUpdates(*__, **_) -> Never:
    """
    Qt's 'void QMetaObjectPublisher::initializePropertyUpdates(QObject *const
    object, const QJsonObject &objectInfo)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaObjectPublisher.initializePropertyUpdates' has no cute "
        "function yet. Qt's 'void "
        "QMetaObjectPublisher::initializePropertyUpdates(QObject *const "
        "object, const QJsonObject &objectInfo)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def invokeMethod(*__, **_) -> Never:
    """
    - Qt's 'QVariant QMetaObjectPublisher::invokeMethod(QObject *const
      object, const QMetaMethod &method, const QJsonArray &args)': takes a
      type Python has no way to hand over yet.
    - Qt's 'QVariant QMetaObjectPublisher::invokeMethod(QObject *const
      object, const int methodIndex, const QJsonArray &args)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QVariant QMetaObjectPublisher::invokeMethod(QObject *const
      object, const QByteArray &methodName, const QJsonArray &args)': takes a
      type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaObjectPublisher.invokeMethod' has no cute function yet. Qt's "
        "'QVariant QMetaObjectPublisher::invokeMethod(QObject *const "
        "object, const QMetaMethod &method, const QJsonArray &args)': takes "
        "a type Python has no way to hand over yet. Qt's 'QVariant "
        "QMetaObjectPublisher::invokeMethod(QObject *const object, const "
        "int methodIndex, const QJsonArray &args)': takes a type Python has "
        "no way to hand over yet. Qt's 'QVariant "
        "QMetaObjectPublisher::invokeMethod(QObject *const object, const "
        "QByteArray &methodName, const QJsonArray &args)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def invokeMethod_helper(*__, **_) -> Never:
    """
    Qt's 'QVariant QMetaObjectPublisher::invokeMethod_helper(QObject *const
    object, const QMetaMethod &method, const QJsonArray &args)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaObjectPublisher.invokeMethod_helper' has no cute function "
        "yet. Qt's 'QVariant "
        "QMetaObjectPublisher::invokeMethod_helper(QObject *const object, "
        "const QMetaMethod &method, const QJsonArray &args)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def signalHandlerFor(*__, **_) -> Never:
    """
    Qt's 'SignalHandler<QMetaObjectPublisher>
    *QMetaObjectPublisher::signalHandlerFor(const QObject *object)': gives
    'SignalHandler<QMetaObjectPublisher>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaObjectPublisher.signalHandlerFor' has no cute function yet. "
        "Qt's 'SignalHandler<QMetaObjectPublisher> "
        "*QMetaObjectPublisher::signalHandlerFor(const QObject *object)': "
        "gives 'SignalHandler<QMetaObjectPublisher>', which has no cute "
        "class yet.")
