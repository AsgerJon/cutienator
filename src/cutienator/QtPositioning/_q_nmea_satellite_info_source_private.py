"""
QNmeaSatelliteInfoSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QNmeaSatelliteInfoSourcePrivate to be private: it declares the
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNmeaSatelliteInfoSourcePrivate(QObject):
  """
  The cute side of Qt's QNmeaSatelliteInfoSourcePrivate: a plain Python
  object standing in front of one C++ QNmeaSatelliteInfoSourcePrivate.

  It is built on the cute 'QObject', as Qt's QNmeaSatelliteInfoSourcePrivate
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNmeaSatelliteInfoSourcePrivate that has a ritual
  and that Python can call so far, 13 names in all: 'metaObject',
  'startUpdates', 'stopUpdates', 'requestUpdate', 'notifyNewUpdate',
  'readyRead', 'emitPendingUpdate', 'sourceDataClosed',
  'updateRequestTimeout', 'openSourceDevice', 'initialize',
  'prepareSourceDevice', 'timerEvent'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNmeaSatelliteInfoSourcePrivate::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QNmeaSatelliteInfoSourcePrivate::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QNmeaSatelliteInfoSourcePrivate::~QNmeaSatelliteInfoSourcePrivate()':
    the destructor: Python never removes a C++
    QNmeaSatelliteInfoSourcePrivate.
  - Qt's 'bool
    QNmeaSatelliteInfoSourcePrivate::emitUpdated(QNmeaSatelliteInfoUpdate
    &update, bool fromRequestUpdate)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  5 of the 22 functions Qt declares: 2 not a gap; 2 leans on
  'QNmeaSatelliteInfoSourcePrivate; 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QNmeaSatelliteInfoSourcePrivate is created at the first use, not
    by 'QNmeaSatelliteInfoSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNmeaSatelliteInfoSourcePrivate.
  - Qt tells when it has removed the C++ QNmeaSatelliteInfoSourcePrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNmeaSatelliteInfoSourcePrivate that has no cute
    function yet, '__init__', 'emitUpdated', 'processNmeaData', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaSatelliteInfoSourcePrivate'

  #  A C++ QNmeaSatelliteInfoSourcePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNmeaSatelliteInfoSourcePrivate'

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
    *QNmeaSatelliteInfoSourcePrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNmeaSatelliteInfoSourcePrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QNmeaSatelliteInfoSourcePrivate10metaObjectEv',
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
    Qt's 'QNmeaSatelliteInfoSourcePrivate::QNmeaSatelliteInfoSourcePrivate(
    QNmeaSatelliteInfoSource *parent, QNmeaSatelliteInfoSource::UpdateMode
    updateMode)': leans on
    'QNmeaSatelliteInfoSourcePrivate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteInfoSourcePrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QNmeaSatelliteInfoSourcePrivate::QNmeaSatelliteInfoSourcePrivate(Q"
        "NmeaSatelliteInfoSource *parent, "
        "QNmeaSatelliteInfoSource::UpdateMode updateMode)': leans on "
        "'QNmeaSatelliteInfoSourcePrivate::qt_metacall(QMetaObject::Call, "
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

  def startUpdates(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::startUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html#startUpdates
    """
    #  void QNmeaSatelliteInfoSourcePrivate::startUpdates()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate12startUpdatesEv',
    )

  def stopUpdates(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::stopUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html#stopUpdates
    """
    #  void QNmeaSatelliteInfoSourcePrivate::stopUpdates()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate11stopUpdatesEv',
    )

  @overload(int)
  def requestUpdate(self, msec: int) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::requestUpdate(int
    msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html#requestUpdate

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QNmeaSatelliteInfoSourcePrivate::requestUpdate(int msec)
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate13requestUpdateEi', msec,
    )

  def notifyNewUpdate(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::notifyNewUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html
    """
    #  void QNmeaSatelliteInfoSourcePrivate::notifyNewUpdate()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate15notifyNewUpdateEv',
    )

  def readyRead(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::readyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html#readyRead
    """
    #  void QNmeaSatelliteInfoSourcePrivate::readyRead()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate9readyReadEv',
    )

  def emitPendingUpdate(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::emitPendingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html
    """
    #  void QNmeaSatelliteInfoSourcePrivate::emitPendingUpdate()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate17emitPendingUpdateEv',
    )

  def sourceDataClosed(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::sourceDataClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html
    """
    #  void QNmeaSatelliteInfoSourcePrivate::sourceDataClosed()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate16sourceDataClosedEv',
    )

  def updateRequestTimeout(self) -> None:
    """
    Calls Qt's 'void
    QNmeaSatelliteInfoSourcePrivate::updateRequestTimeout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html
    """
    #  void QNmeaSatelliteInfoSourcePrivate::updateRequestTimeout()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate20updateRequestTimeoutEv',
    )

  def openSourceDevice(self) -> bool:
    """
    Calls Qt's 'bool QNmeaSatelliteInfoSourcePrivate::openSourceDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html
    """
    #  bool QNmeaSatelliteInfoSourcePrivate::openSourceDevice()
    return self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate16openSourceDeviceEv',
    )

  def initialize(self) -> bool:
    """
    Calls Qt's 'bool QNmeaSatelliteInfoSourcePrivate::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html#initialize
    """
    #  bool QNmeaSatelliteInfoSourcePrivate::initialize()
    return self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate10initializeEv',
    )

  def prepareSourceDevice(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::prepareSourceDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html
    """
    #  void QNmeaSatelliteInfoSourcePrivate::prepareSourceDevice()
    self.uglySide.call(
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate19prepareSourceDeviceEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSourcePrivate::timerEvent(QTimerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosourceprivate.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNmeaSatelliteInfoSourcePrivate::timerEvent(QTimerEvent *event)
    ritual = (
        'ritual_ZN31QNmeaSatelliteInfoSourcePrivate10timerEventEP11QTimerEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QNmeaSatelliteInfoSourcePrivate10timerEventEP11QT'
          'imerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def emitUpdated(*__, **_) -> Never:
    """
    Qt's 'bool
    QNmeaSatelliteInfoSourcePrivate::emitUpdated(QNmeaSatelliteInfoUpdate
    &update, bool fromRequestUpdate)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteInfoSourcePrivate.emitUpdated' has no cute function "
        "yet. Qt's 'bool "
        "QNmeaSatelliteInfoSourcePrivate::emitUpdated(QNmeaSatelliteInfoUpda"
        "te &update, bool fromRequestUpdate)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def processNmeaData(*__, **_) -> Never:
    """
    Qt's 'void
    QNmeaSatelliteInfoSourcePrivate::processNmeaData(QNmeaSatelliteInfoUpdate
    &updateInfo)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: no member named
    'nmeaSentences' in 'QGeoSatelliteInfoPrivate'.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteInfoSourcePrivate.processNmeaData' has no cute "
        "function yet. Qt's 'void "
        "QNmeaSatelliteInfoSourcePrivate::processNmeaData(QNmeaSatelliteInfo"
        "Update &updateInfo)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: no "
        "member named 'nmeaSentences' in 'QGeoSatelliteInfoPrivate'.")
