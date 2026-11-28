"""
QNmeaSatelliteInfoSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qnmeasatelliteinfosource.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGeoSatelliteInfoSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNmeaSatelliteInfoSource(QGeoSatelliteInfoSource):
  """
  The cute side of Qt's QNmeaSatelliteInfoSource: a plain Python object
  standing in front of one C++ QNmeaSatelliteInfoSource.

  It is built on the cute 'QGeoSatelliteInfoSource', as Qt's
  QNmeaSatelliteInfoSource is built on Qt's QGeoSatelliteInfoSource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNmeaSatelliteInfoSource that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'updateMode',
  'setDevice', 'device', 'setUpdateInterval', 'minimumUpdateInterval',
  'error', 'setBackendProperty', 'backendProperty', 'startUpdates',
  'stopUpdates', 'requestUpdate', 'setError'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNmeaSatelliteInfoSource::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QNmeaSatelliteInfoSource::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNmeaSatelliteInfoSource::~QNmeaSatelliteInfoSource()': the
    destructor: Python never removes a C++ QNmeaSatelliteInfoSource.
  - Qt's 'QGeoSatelliteInfo::SatelliteSystem
    QNmeaSatelliteInfoSource::parseSatellitesInUseFromNmea(const char *data,
    int size, QList<int> &pnrsInUse)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QGeoSatelliteInfo::SatelliteSystem
    QNmeaSatelliteInfoSource::parseSatellitesInUseFromNmea(QByteArrayView
    data, QList<int> &pnrsInUse)': takes a type Python has no way to hand
    over yet.
  - Qt's 'SatelliteInfoParseStatus
    QNmeaSatelliteInfoSource::parseSatelliteInfoFromNmea(const char *data,
    int size, QList<QGeoSatelliteInfo> &infos,
    QGeoSatelliteInfo::SatelliteSystem &system)': takes a type Python has no
    way to hand over yet.
  - Qt's 'SatelliteInfoParseStatus
    QNmeaSatelliteInfoSource::parseSatelliteInfoFromNmea(QByteArrayView data,
    QList<QGeoSatelliteInfo> &infos, QGeoSatelliteInfo::SatelliteSystem
    &system)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QNmeaSatelliteInfoSource is created at the first use, not by
    'QNmeaSatelliteInfoSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNmeaSatelliteInfoSource.
  - Qt tells when it has removed the C++ QNmeaSatelliteInfoSource. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNmeaSatelliteInfoSource that has no cute function yet,
    'parseSatelliteInfoFromNmea', 'parseSatellitesInUseFromNmea', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QNmeaSatelliteInfoSource, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class UpdateMode(CuteNum, scoped=True):
    """
    The enum 'QNmeaSatelliteInfoSource::UpdateMode' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
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
    Calls Qt's 'QString QNmeaSatelliteInfoSource::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#tr

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
    #  QString QNmeaSatelliteInfoSource::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QNmeaSatelliteInfoSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaSatelliteInfoSource'

  #  A C++ QNmeaSatelliteInfoSource Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNmeaSatelliteInfoSource'

  #  The functions Qt calls itself that QNmeaSatelliteInfoSource is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'parseSatellitesInUseFromNmea': (
          'QGeoSatelliteInfo::SatelliteSystem '
          'QNmeaSatelliteInfoSource::parseSatellitesInUseFromNmea(const '
          'char *, int, QList<int> &)',
      ),
      'parseSatelliteInfoFromNmea': (
          'SatelliteInfoParseStatus '
          'QNmeaSatelliteInfoSource::parseSatelliteInfoFromNmea(const char '
          '*, int, QList<QGeoSatelliteInfo> &, '
          'QGeoSatelliteInfo::SatelliteSystem &)',
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
    Calls Qt's 'const QMetaObject *QNmeaSatelliteInfoSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNmeaSatelliteInfoSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def updateMode(self) -> UpdateMode:
    """
    Calls Qt's 'UpdateMode QNmeaSatelliteInfoSource::updateMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#updateMode

    Returns
    -------

    UpdateMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UpdateMode(number)'
      gives.
    """
    #  UpdateMode QNmeaSatelliteInfoSource::updateMode() const
    return QNmeaSatelliteInfoSource.UpdateMode(self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoSource10updateModeEv',
    ))

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QNmeaSatelliteInfoSource::device() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QNmeaSatelliteInfoSource::device() const
    address = self.uglySide.call(
        'ritual_ZNK24QNmeaSatelliteInfoSource6deviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def minimumUpdateInterval(self) -> int:
    """
    Calls Qt's 'int QNmeaSatelliteInfoSource::minimumUpdateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html
    """
    #  int QNmeaSatelliteInfoSource::minimumUpdateInterval() const
    ritual = 'ritual_ZNK24QNmeaSatelliteInfoSource21minimumUpdateIntervalEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QNmeaSatelliteInfoSource21minimumUpdateIntervalE'
          'v')
    return self.uglySide.call(ritual)

  def error(self) -> QGeoSatelliteInfoSource.Error:
    """
    Calls Qt's 'Error QNmeaSatelliteInfoSource::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#error

    Returns
    -------

    QGeoSatelliteInfoSource.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoSatelliteInfoSource.Error(number)' gives.
    """
    #  Error QNmeaSatelliteInfoSource::error() const
    ritual = 'ritual_ZNK24QNmeaSatelliteInfoSource5errorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QNmeaSatelliteInfoSource5errorEv'
    return QGeoSatelliteInfoSource.Error(self.uglySide.call(ritual))

  @overload(str)
  def backendProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QNmeaSatelliteInfoSource::backendProperty(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#backendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNmeaSatelliteInfoSource::backendProperty(const QString
    #      &name) const
    ritual = (
        'ritual_ZNK24QNmeaSatelliteInfoSource15backendPropertyERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QNmeaSatelliteInfoSource15backendPropertyERK7QSt'
          'ring')
    address = self.uglySide.call(ritual, name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, source: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSource::setDevice(QIODevice *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#setDevice

    Parameters
    ----------

    source : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNmeaSatelliteInfoSource::setDevice(QIODevice *source)
    self.uglySide.call(
        'ritual_ZN24QNmeaSatelliteInfoSource9setDeviceEP9QIODevice',
        self._addressOf(source),
    )

  @overload(int)
  def setUpdateInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSource::setUpdateInterval(int msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#setUpdateInterval

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QNmeaSatelliteInfoSource::setUpdateInterval(int msec)
    ritual = 'ritual_ZN24QNmeaSatelliteInfoSource17setUpdateIntervalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QNmeaSatelliteInfoSource17setUpdateIntervalEi'
    self.uglySide.call(ritual, msec)

  @overload(str, QVariant)
  def setBackendProperty(self, name: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QNmeaSatelliteInfoSource::setBackendProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#setBackendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QNmeaSatelliteInfoSource::setBackendProperty(const QString &name,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN24QNmeaSatelliteInfoSource18setBackendPropertyERK7QString'
        'RK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QNmeaSatelliteInfoSource18setBackendPropertyERK7Q'
          'StringRK8QVariant')
    return self.uglySide.call(ritual, name, self._valueOf(value))

  @overload(QGeoSatelliteInfoSource.Error)
  def setError(self, satelliteError: QGeoSatelliteInfoSource.Error) -> None:
    """
    Calls Qt's 'void
    QNmeaSatelliteInfoSource::setError(QGeoSatelliteInfoSource::Error
    satelliteError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#setError

    Parameters
    ----------

    satelliteError : QGeoSatelliteInfoSource.Error
      Passed on as its number.
    """
    #  void QNmeaSatelliteInfoSource::setError(QGeoSatelliteInfoSource::Error
    #      satelliteError)
    self.uglySide.call(
        'ritual_ZN24QNmeaSatelliteInfoSource8setErrorEN23QGeoSatelliteInfoS'
        'ource5ErrorE',
        satelliteError.value,
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
      mode: UpdateMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNmeaSatelliteInfoSource::QNmeaSatelliteInfoSource(UpdateMode mode,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html

    Parameters
    ----------

    mode : UpdateMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNmeaSatelliteInfoSource::QNmeaSatelliteInfoSource(UpdateMode mode,
    #      QObject *parent)
    self._noteCreation(QNmeaSatelliteInfoSource, lambda: Rituals.call(
        'ritual_ZN24QNmeaSatelliteInfoSourceC1ENS_10UpdateModeEP7QObject',
        mode.value, self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QNmeaSatelliteInfoSource::startUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#startUpdates
    """
    #  void QNmeaSatelliteInfoSource::startUpdates()
    ritual = 'ritual_ZN24QNmeaSatelliteInfoSource12startUpdatesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QNmeaSatelliteInfoSource12startUpdatesEv'
    self.uglySide.call(ritual)

  def stopUpdates(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSource::stopUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#stopUpdates
    """
    #  void QNmeaSatelliteInfoSource::stopUpdates()
    ritual = 'ritual_ZN24QNmeaSatelliteInfoSource11stopUpdatesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QNmeaSatelliteInfoSource11stopUpdatesEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def requestUpdate(self, timeout: int = 0) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteInfoSource::requestUpdate(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliteinfosource.html#requestUpdate

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QNmeaSatelliteInfoSource::requestUpdate(int timeout)
    ritual = 'ritual_ZN24QNmeaSatelliteInfoSource13requestUpdateEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QNmeaSatelliteInfoSource13requestUpdateEi'
    self.uglySide.call(ritual, timeout)

  @staticmethod
  def parseSatelliteInfoFromNmea(*__, **_) -> Never:
    """
    - Qt's 'SatelliteInfoParseStatus
      QNmeaSatelliteInfoSource::parseSatelliteInfoFromNmea(const char *data,
      int size, QList<QGeoSatelliteInfo> &infos,
      QGeoSatelliteInfo::SatelliteSystem &system)': takes a type Python has
      no way to hand over yet.
    - Qt's 'SatelliteInfoParseStatus
      QNmeaSatelliteInfoSource::parseSatelliteInfoFromNmea(QByteArrayView
      data, QList<QGeoSatelliteInfo> &infos,
      QGeoSatelliteInfo::SatelliteSystem &system)': takes a type Python has
      no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteInfoSource.parseSatelliteInfoFromNmea' has no cute "
        "function yet. Qt's 'SatelliteInfoParseStatus "
        "QNmeaSatelliteInfoSource::parseSatelliteInfoFromNmea(const char "
        "*data, int size, QList<QGeoSatelliteInfo> &infos, "
        "QGeoSatelliteInfo::SatelliteSystem &system)': takes a type Python "
        "has no way to hand over yet. Qt's 'SatelliteInfoParseStatus "
        "QNmeaSatelliteInfoSource::parseSatelliteInfoFromNmea(QByteArrayView"
        " data, QList<QGeoSatelliteInfo> &infos, "
        "QGeoSatelliteInfo::SatelliteSystem &system)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def parseSatellitesInUseFromNmea(*__, **_) -> Never:
    """
    - Qt's 'QGeoSatelliteInfo::SatelliteSystem
      QNmeaSatelliteInfoSource::parseSatellitesInUseFromNmea(const char
      *data, int size, QList<int> &pnrsInUse)': takes a type Python has no
      way to hand over yet.
    - Qt's 'QGeoSatelliteInfo::SatelliteSystem
      QNmeaSatelliteInfoSource::parseSatellitesInUseFromNmea(QByteArrayView
      data, QList<int> &pnrsInUse)': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteInfoSource.parseSatellitesInUseFromNmea' has no "
        "cute function yet. Qt's 'QGeoSatelliteInfo::SatelliteSystem "
        "QNmeaSatelliteInfoSource::parseSatellitesInUseFromNmea(const char "
        "*data, int size, QList<int> &pnrsInUse)': takes a type Python has "
        "no way to hand over yet. Qt's 'QGeoSatelliteInfo::SatelliteSystem "
        "QNmeaSatelliteInfoSource::parseSatellitesInUseFromNmea(QByteArrayVi"
        "ew data, QList<int> &pnrsInUse)': takes a type Python has no way "
        "to hand over yet.")
