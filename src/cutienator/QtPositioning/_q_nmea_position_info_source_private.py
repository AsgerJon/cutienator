"""
QNmeaPositionInfoSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QNmeaPositionInfoSourcePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent
  from . import QGeoPositionInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoPositionInfo = WAIT['QGeoPositionInfo']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNmeaPositionInfoSourcePrivate(QObject):
  """
  The cute side of Qt's QNmeaPositionInfoSourcePrivate: a plain Python object
  standing in front of one C++ QNmeaPositionInfoSourcePrivate.

  It is built on the cute 'QObject', as Qt's QNmeaPositionInfoSourcePrivate
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNmeaPositionInfoSourcePrivate that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'stopUpdates',
  'notifyNewUpdate', 'readyRead', 'timerEvent', 'emitPendingUpdate',
  'sourceDataClosed', 'updateRequestTimeout', 'openSourceDevice',
  'prepareSourceDevice', 'emitUpdated'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNmeaPositionInfoSourcePrivate::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QNmeaPositionInfoSourcePrivate::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNmeaPositionInfoSourcePrivate::~QNmeaPositionInfoSourcePrivate()':
    the destructor: Python never removes a C++
    QNmeaPositionInfoSourcePrivate.
  - Qt's 'bool
    QNmeaPositionInfoSourcePrivate::parsePosInfoFromNmeaData(QByteArrayView
    data, QGeoPositionInfo *posInfo, bool *hasFix)': takes a number to change
    where it is.

  What has no ritual
  ------------------

  7 of the 22 functions Qt declares: 3 leans on 'QNmeaRealTimeReader; 2 not a
  gap; 2 leans on 'QNmeaPositionInfoSourcePrivate.

  What to expect
  --------------

  - The C++ QNmeaPositionInfoSourcePrivate is created at the first use, not
    by 'QNmeaPositionInfoSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNmeaPositionInfoSourcePrivate.
  - Qt tells when it has removed the C++ QNmeaPositionInfoSourcePrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNmeaPositionInfoSourcePrivate that has no cute
    function yet, '__init__', 'initialize', 'parsePosInfoFromNmeaData',
    'requestUpdate', 'startUpdates', holds a function that raises
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
  __qt_class__ = 'QNmeaPositionInfoSourcePrivate'

  #  A C++ QNmeaPositionInfoSourcePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNmeaPositionInfoSourcePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QNmeaPositionInfoSourcePrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNmeaPositionInfoSourcePrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QNmeaPositionInfoSourcePrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QNmeaPositionInfoSourcePrivate::QNmeaPositionInfoSourcePrivate(
    QNmeaPositionInfoSource *parent, QNmeaPositionInfoSource::UpdateMode
    updateMode)': leans on
    'QNmeaPositionInfoSourcePrivate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaPositionInfoSourcePrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QNmeaPositionInfoSourcePrivate::QNmeaPositionInfoSourcePrivate(QNm"
        "eaPositionInfoSource *parent, QNmeaPositionInfoSource::UpdateMode "
        "updateMode)': leans on "
        "'QNmeaPositionInfoSourcePrivate::qt_metacall(QMetaObject::Call, "
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

  def stopUpdates(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::stopUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html#stopUpdates
    """
    #  void QNmeaPositionInfoSourcePrivate::stopUpdates()
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate11stopUpdatesEv',
    )

  @overload(QGeoPositionInfo, bool)
  @overload(NoneType, bool)
  def notifyNewUpdate(
      self,
      update: Optional[QGeoPositionInfo],
      fixStatus: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QNmeaPositionInfoSourcePrivate::notifyNewUpdate(QGeoPositionInfo *update,
    bool fixStatus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html

    Parameters
    ----------

    update : Optional[QGeoPositionInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fixStatus : bool
      Passed on as it is.
    """
    #  void QNmeaPositionInfoSourcePrivate::notifyNewUpdate(QGeoPositionInfo
    #      *update, bool fixStatus)
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate15notifyNewUpdateEP16QGeo'
        'PositionInfob',
        self._addressOf(update), fixStatus,
    )

  def readyRead(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::readyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html#readyRead
    """
    #  void QNmeaPositionInfoSourcePrivate::readyRead()
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate9readyReadEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::timerEvent(QTimerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNmeaPositionInfoSourcePrivate::timerEvent(QTimerEvent *event)
    ritual = (
        'ritual_ZN30QNmeaPositionInfoSourcePrivate10timerEventEP11QTimerEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QNmeaPositionInfoSourcePrivate10timerEventEP11QTi'
          'merEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def emitPendingUpdate(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::emitPendingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html
    """
    #  void QNmeaPositionInfoSourcePrivate::emitPendingUpdate()
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate17emitPendingUpdateEv',
    )

  def sourceDataClosed(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::sourceDataClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html
    """
    #  void QNmeaPositionInfoSourcePrivate::sourceDataClosed()
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate16sourceDataClosedEv',
    )

  def updateRequestTimeout(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::updateRequestTimeout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html
    """
    #  void QNmeaPositionInfoSourcePrivate::updateRequestTimeout()
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate20updateRequestTimeoutEv',
    )

  def openSourceDevice(self) -> bool:
    """
    Calls Qt's 'bool QNmeaPositionInfoSourcePrivate::openSourceDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html
    """
    #  bool QNmeaPositionInfoSourcePrivate::openSourceDevice()
    return self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate16openSourceDeviceEv',
    )

  def prepareSourceDevice(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::prepareSourceDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html
    """
    #  void QNmeaPositionInfoSourcePrivate::prepareSourceDevice()
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate19prepareSourceDeviceEv',
    )

  @overload(QGeoPositionInfo)
  def emitUpdated(self, update: QGeoPositionInfo) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSourcePrivate::emitUpdated(const
    QGeoPositionInfo &update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosourceprivate.html#emitUpdated

    Parameters
    ----------

    update : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  void QNmeaPositionInfoSourcePrivate::emitUpdated(const
    #      QGeoPositionInfo &update)
    self.uglySide.call(
        'ritual_ZN30QNmeaPositionInfoSourcePrivate11emitUpdatedERK16QGeoPos'
        'itionInfo',
        self._valueOf(update),
    )

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'bool QNmeaPositionInfoSourcePrivate::initialize()': leans on
    'QNmeaRealTimeReader::QNmeaRealTimeReader(
    QNmeaPositionInfoSourcePrivate*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaPositionInfoSourcePrivate.initialize' has no cute function "
        "yet. Qt's 'bool QNmeaPositionInfoSourcePrivate::initialize()': "
        "leans on "
        "'QNmeaRealTimeReader::QNmeaRealTimeReader(QNmeaPositionInfoSourcePr"
        "ivate*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def parsePosInfoFromNmeaData(*__, **_) -> Never:
    """
    Qt's 'bool
    QNmeaPositionInfoSourcePrivate::parsePosInfoFromNmeaData(QByteArrayView
    data, QGeoPositionInfo *posInfo, bool *hasFix)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QNmeaPositionInfoSourcePrivate.parsePosInfoFromNmeaData' has no "
        "cute function yet. Qt's 'bool "
        "QNmeaPositionInfoSourcePrivate::parsePosInfoFromNmeaData(QByteArray"
        "View data, QGeoPositionInfo *posInfo, bool *hasFix)': takes a "
        "number to change where it is.")

  @staticmethod
  def requestUpdate(*__, **_) -> Never:
    """
    Qt's 'void QNmeaPositionInfoSourcePrivate::requestUpdate(int msec)':
    leans on 'QNmeaRealTimeReader::QNmeaRealTimeReader(
    QNmeaPositionInfoSourcePrivate*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaPositionInfoSourcePrivate.requestUpdate' has no cute "
        "function yet. Qt's 'void "
        "QNmeaPositionInfoSourcePrivate::requestUpdate(int msec)': leans on "
        "'QNmeaRealTimeReader::QNmeaRealTimeReader(QNmeaPositionInfoSourcePr"
        "ivate*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def startUpdates(*__, **_) -> Never:
    """
    Qt's 'void QNmeaPositionInfoSourcePrivate::startUpdates()': leans on
    'QNmeaRealTimeReader::QNmeaRealTimeReader(
    QNmeaPositionInfoSourcePrivate*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaPositionInfoSourcePrivate.startUpdates' has no cute function "
        "yet. Qt's 'void QNmeaPositionInfoSourcePrivate::startUpdates()': "
        "leans on "
        "'QNmeaRealTimeReader::QNmeaRealTimeReader(QNmeaPositionInfoSourcePr"
        "ivate*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
