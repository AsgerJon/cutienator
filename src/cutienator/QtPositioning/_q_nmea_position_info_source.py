"""
QNmeaPositionInfoSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qnmeapositioninfosource.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGeoPositionInfoSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject
  from . import QGeoPositionInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNmeaPositionInfoSource(QGeoPositionInfoSource):
  """
  The cute side of Qt's QNmeaPositionInfoSource: a plain Python object
  standing in front of one C++ QNmeaPositionInfoSource.

  It is built on the cute 'QGeoPositionInfoSource', as Qt's
  QNmeaPositionInfoSource is built on Qt's QGeoPositionInfoSource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNmeaPositionInfoSource that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr',
  'setUserEquivalentRangeError', 'userEquivalentRangeError', 'updateMode',
  'setDevice', 'device', 'setUpdateInterval', 'lastKnownPosition',
  'supportedPositioningMethods', 'minimumUpdateInterval', 'error',
  'startUpdates', 'stopUpdates', 'requestUpdate', 'setError'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNmeaPositionInfoSource::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNmeaPositionInfoSource::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNmeaPositionInfoSource::~QNmeaPositionInfoSource()': the
    destructor: Python never removes a C++ QNmeaPositionInfoSource.
  - Qt's 'bool QNmeaPositionInfoSource::parsePosInfoFromNmeaData(const char
    *data, int size, QGeoPositionInfo *posInfo, bool *hasFix)': takes a
    number to change where it is.
  - Qt's 'bool
    QNmeaPositionInfoSource::parsePosInfoFromNmeaData(QByteArrayView data,
    QGeoPositionInfo *posInfo, bool *hasFix)': takes a number to change where
    it is.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QNmeaPositionInfoSource is created at the first use, not by
    'QNmeaPositionInfoSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNmeaPositionInfoSource.
  - Qt tells when it has removed the C++ QNmeaPositionInfoSource. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNmeaPositionInfoSource that has no cute function yet,
    'parsePosInfoFromNmeaData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QNmeaPositionInfoSource, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class UpdateMode(CuteNum):
    """
    The enum 'QNmeaPositionInfoSource::UpdateMode' of Qt, with the 2 names Qt
    gives in it.
    """

    RealTimeMode = Kee[int](1)
    SimulationMode = Kee[int](2)

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
    Calls Qt's 'QString QNmeaPositionInfoSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnmeapositioninfosource.html#tr

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
    #  QString QNmeaPositionInfoSource::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QNmeaPositionInfoSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaPositionInfoSource'

  #  A C++ QNmeaPositionInfoSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNmeaPositionInfoSource'

  #  The functions Qt calls itself that QNmeaPositionInfoSource is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'parsePosInfoFromNmeaData': (
          'bool QNmeaPositionInfoSource::parsePosInfoFromNmeaData(const '
          'char *, int, QGeoPositionInfo *, bool *)',
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
    Calls Qt's 'const QMetaObject *QNmeaPositionInfoSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNmeaPositionInfoSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QNmeaPositionInfoSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def userEquivalentRangeError(self) -> float:
    """
    Calls Qt's 'double QNmeaPositionInfoSource::userEquivalentRangeError()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html
    """
    #  double QNmeaPositionInfoSource::userEquivalentRangeError() const
    return self.uglySide.call(
        'ritual_ZNK23QNmeaPositionInfoSource24userEquivalentRangeErrorEv',
    )

  def updateMode(self) -> UpdateMode:
    """
    Calls Qt's 'UpdateMode QNmeaPositionInfoSource::updateMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#updateMode

    Returns
    -------

    UpdateMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UpdateMode(number)'
      gives.
    """
    #  UpdateMode QNmeaPositionInfoSource::updateMode() const
    return QNmeaPositionInfoSource.UpdateMode(self.uglySide.call(
        'ritual_ZNK23QNmeaPositionInfoSource10updateModeEv',
    ))

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QNmeaPositionInfoSource::device() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QNmeaPositionInfoSource::device() const
    address = self.uglySide.call(
        'ritual_ZNK23QNmeaPositionInfoSource6deviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  @overload()
  @overload(bool)
  def lastKnownPosition(
      self,
      fromSatellitePositioningMethodsOnly: bool = False,
  ) -> QGeoPositionInfo:
    """
    Calls Qt's 'QGeoPositionInfo
    QNmeaPositionInfoSource::lastKnownPosition(bool
    fromSatellitePositioningMethodsOnly) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#lastKnownPosition

    Parameters
    ----------

    fromSatellitePositioningMethodsOnly : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QGeoPositionInfo
      A new cute QGeoPositionInfo around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoPositionInfo QNmeaPositionInfoSource::lastKnownPosition(bool
    #      fromSatellitePositioningMethodsOnly) const
    ritual = 'ritual_ZNK23QNmeaPositionInfoSource17lastKnownPositionEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QNmeaPositionInfoSource17lastKnownPositionEb'
    address = self.uglySide.call(ritual, fromSatellitePositioningMethodsOnly)
    from . import QGeoPositionInfo
    return QGeoPositionInfo._cuteOwning(address)

  def supportedPositioningMethods(
      self,
  ) -> QGeoPositionInfoSource.PositioningMethods:
    """
    Calls Qt's 'PositioningMethods
    QNmeaPositionInfoSource::supportedPositioningMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html

    Returns
    -------

    QGeoPositionInfoSource.PositioningMethods
      The value standing for the combination Qt gave back.
    """
    #  PositioningMethods
    #      QNmeaPositionInfoSource::supportedPositioningMethods() const
    ritual = (
        'ritual_ZNK23QNmeaPositionInfoSource27supportedPositioningMethodsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QNmeaPositionInfoSource27supportedPositioningMet'
          'hodsEv')
    return QGeoPositionInfoSource.PositioningMethods(self.uglySide.call(
        ritual,
    ))

  def minimumUpdateInterval(self) -> int:
    """
    Calls Qt's 'int QNmeaPositionInfoSource::minimumUpdateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#minimumUpdateInterval
    """
    #  int QNmeaPositionInfoSource::minimumUpdateInterval() const
    ritual = 'ritual_ZNK23QNmeaPositionInfoSource21minimumUpdateIntervalEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QNmeaPositionInfoSource21minimumUpdateIntervalEv')
    return self.uglySide.call(ritual)

  def error(self) -> QGeoPositionInfoSource.Error:
    """
    Calls Qt's 'Error QNmeaPositionInfoSource::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnmeapositioninfosource.html#error

    Returns
    -------

    QGeoPositionInfoSource.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoPositionInfoSource.Error(number)' gives.
    """
    #  Error QNmeaPositionInfoSource::error() const
    ritual = 'ritual_ZNK23QNmeaPositionInfoSource5errorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QNmeaPositionInfoSource5errorEv'
    return QGeoPositionInfoSource.Error(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setUserEquivalentRangeError(self, uere: float) -> None:
    """
    Calls Qt's 'void
    QNmeaPositionInfoSource::setUserEquivalentRangeError(double uere)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html

    Parameters
    ----------

    uere : float
      Passed on as it is.
    """
    #  void QNmeaPositionInfoSource::setUserEquivalentRangeError(double uere)
    self.uglySide.call(
        'ritual_ZN23QNmeaPositionInfoSource27setUserEquivalentRangeErrorEd',
        uere,
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, source: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSource::setDevice(QIODevice *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#setDevice

    Parameters
    ----------

    source : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNmeaPositionInfoSource::setDevice(QIODevice *source)
    self.uglySide.call(
        'ritual_ZN23QNmeaPositionInfoSource9setDeviceEP9QIODevice',
        self._addressOf(source),
    )

  @overload(int)
  def setUpdateInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSource::setUpdateInterval(int msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#setUpdateInterval

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QNmeaPositionInfoSource::setUpdateInterval(int msec)
    ritual = 'ritual_ZN23QNmeaPositionInfoSource17setUpdateIntervalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QNmeaPositionInfoSource17setUpdateIntervalEi'
    self.uglySide.call(ritual, msec)

  @overload(QGeoPositionInfoSource.Error)
  def setError(self, positionError: QGeoPositionInfoSource.Error) -> None:
    """
    Calls Qt's 'void
    QNmeaPositionInfoSource::setError(QGeoPositionInfoSource::Error
    positionError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#setError

    Parameters
    ----------

    positionError : QGeoPositionInfoSource.Error
      Passed on as its number.
    """
    #  void QNmeaPositionInfoSource::setError(QGeoPositionInfoSource::Error
    #      positionError)
    self.uglySide.call(
        'ritual_ZN23QNmeaPositionInfoSource8setErrorEN22QGeoPositionInfoSou'
        'rce5ErrorE',
        positionError.value,
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

  @overload(UpdateMode)
  @overload(UpdateMode, QObject)
  @overload(UpdateMode, NoneType)
  def __init__(
      self,
      updateMode: UpdateMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNmeaPositionInfoSource::QNmeaPositionInfoSource(UpdateMode updateMode,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html

    Parameters
    ----------

    updateMode : UpdateMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNmeaPositionInfoSource::QNmeaPositionInfoSource(UpdateMode
    #      updateMode, QObject *parent)
    self._noteCreation(QNmeaPositionInfoSource, lambda: Rituals.call(
        'ritual_ZN23QNmeaPositionInfoSourceC1ENS_10UpdateModeEP7QObject',
        updateMode.value, self._addressOf(parent, 'QObject'),
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

  def startUpdates(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSource::startUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#startUpdates
    """
    #  void QNmeaPositionInfoSource::startUpdates()
    ritual = 'ritual_ZN23QNmeaPositionInfoSource12startUpdatesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QNmeaPositionInfoSource12startUpdatesEv'
    self.uglySide.call(ritual)

  def stopUpdates(self) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSource::stopUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#stopUpdates
    """
    #  void QNmeaPositionInfoSource::stopUpdates()
    ritual = 'ritual_ZN23QNmeaPositionInfoSource11stopUpdatesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QNmeaPositionInfoSource11stopUpdatesEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def requestUpdate(self, timeout: int = 0) -> None:
    """
    Calls Qt's 'void QNmeaPositionInfoSource::requestUpdate(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html#requestUpdate

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QNmeaPositionInfoSource::requestUpdate(int timeout)
    ritual = 'ritual_ZN23QNmeaPositionInfoSource13requestUpdateEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QNmeaPositionInfoSource13requestUpdateEi'
    self.uglySide.call(ritual, timeout)

  @staticmethod
  def parsePosInfoFromNmeaData(*__, **_) -> Never:
    """
    - Qt's 'bool QNmeaPositionInfoSource::parsePosInfoFromNmeaData(const char
      *data, int size, QGeoPositionInfo *posInfo, bool *hasFix)': takes a
      number to change where it is.
    - Qt's 'bool
      QNmeaPositionInfoSource::parsePosInfoFromNmeaData(QByteArrayView data,
      QGeoPositionInfo *posInfo, bool *hasFix)': takes a number to change
      where it is.
    """
    raise NotImplementedError(
        "'QNmeaPositionInfoSource.parsePosInfoFromNmeaData' has no cute "
        "function yet. Qt's 'bool "
        "QNmeaPositionInfoSource::parsePosInfoFromNmeaData(const char "
        "*data, int size, QGeoPositionInfo *posInfo, bool *hasFix)': takes "
        "a number to change where it is. Qt's 'bool "
        "QNmeaPositionInfoSource::parsePosInfoFromNmeaData(QByteArrayView "
        "data, QGeoPositionInfo *posInfo, bool *hasFix)': takes a number to "
        "change where it is.")
