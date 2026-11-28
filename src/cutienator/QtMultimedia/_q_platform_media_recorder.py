"""
QPlatformMediaRecorder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediarecorder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformMediaRecorder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QMediaRecorder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QUrl
  from . import QMediaEncoderSettings, QMediaMetaData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QMediaEncoderSettings = WAIT['QMediaEncoderSettings']
  QMediaMetaData = WAIT['QMediaMetaData']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformMediaRecorder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformMediaRecorder: a plain Python object
  standing in front of one C++ QPlatformMediaRecorder.

  What exists
  -----------

  Every function of Qt's QPlatformMediaRecorder that has a ritual and that
  Python can call so far, 25 names in all: 'isLocationWritable', 'state',
  'pause', 'resume', 'stop', 'duration', 'setMetaData', 'metaData', 'error',
  'errorString', 'outputLocation', 'setOutputLocation', 'actualLocation',
  'clearActualLocation', 'clearError', 'outputDevice', 'setOutputDevice',
  'updateAutoStop', 'stateChanged', 'durationChanged',
  'actualLocationChanged', 'updateError', 'metaDataChanged', 'mediaRecorder',
  'findActualLocation'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformMediaRecorder::~QPlatformMediaRecorder()': the destructor:
    Python never removes a C++ QPlatformMediaRecorder.
  - Qt's 'void QPlatformMediaRecorder::record(QMediaEncoderSettings
    &settings)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 28 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QPlatformMediaRecorder is created at the first use, not by
    'QPlatformMediaRecorder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMediaRecorder.
  - Each name of Qt's QPlatformMediaRecorder that has no cute function yet,
    '__init__', 'record', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMediaRecorder'

  #  A C++ QPlatformMediaRecorder Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformMediaRecorder'

  #  The functions Qt calls itself that QPlatformMediaRecorder is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'record': (
          'void QPlatformMediaRecorder::record(QMediaEncoderSettings &)',
      ),
  }

  #  The functions Qt calls itself that QPlatformMediaRecorder is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isLocationWritable': (
          ('_ZNK22QPlatformMediaRecorder18isLocationWritableERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'state': (
          ('_ZNK22QPlatformMediaRecorder5stateEv',
           ('int', 'enum', 'QtMultimedia:QMediaRecorder.RecorderState'),
           ()),
      ),
      'pause': (
          ('_ZN22QPlatformMediaRecorder5pauseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resume': (
          ('_ZN22QPlatformMediaRecorder6resumeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN22QPlatformMediaRecorder4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'duration': (
          ('_ZNK22QPlatformMediaRecorder8durationEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setMetaData': (
          ('_ZN22QPlatformMediaRecorder11setMetaDataERK14QMediaMetaData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtMultimedia:QMediaMetaData'),
           )),
      ),
      'metaData': (
          ('_ZNK22QPlatformMediaRecorder8metaDataEv',
           ('address', 'value', 'QtMultimedia:QMediaMetaData'),
           ()),
      ),
      'setOutputLocation': (
          ('_ZN22QPlatformMediaRecorder17setOutputLocationERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'updateAutoStop': (
          ('_ZN22QPlatformMediaRecorder14updateAutoStopEv',
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

  @overload(QUrl)
  def isLocationWritable(self, location: QUrl) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaRecorder::isLocationWritable(const QUrl
    &location) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#isLocationWritable

    Parameters
    ----------

    location : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QPlatformMediaRecorder::isLocationWritable(const QUrl &location)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QPlatformMediaRecorder18isLocationWritableERK4QUrl',
        self._valueOf(location),
    )

  def state(self) -> QMediaRecorder.RecorderState:
    """
    Calls Qt's 'QMediaRecorder::RecorderState QPlatformMediaRecorder::state()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediarecorder.html#state

    Returns
    -------

    QMediaRecorder.RecorderState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaRecorder.RecorderState(number)' gives.
    """
    #  QMediaRecorder::RecorderState QPlatformMediaRecorder::state() const
    ritual = 'ritual_ZNK22QPlatformMediaRecorder5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QPlatformMediaRecorder5stateEv'
    return QMediaRecorder.RecorderState(self.uglySide.call(ritual))

  def duration(self) -> int:
    """
    Calls Qt's 'qint64 QPlatformMediaRecorder::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#duration
    """
    #  qint64 QPlatformMediaRecorder::duration() const
    ritual = 'ritual_ZNK22QPlatformMediaRecorder8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QPlatformMediaRecorder8durationEv'
    return self.uglySide.call(ritual)

  def metaData(self) -> QMediaMetaData:
    """
    Calls Qt's 'QMediaMetaData QPlatformMediaRecorder::metaData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#metaData

    Returns
    -------

    QMediaMetaData
      A new cute QMediaMetaData around the copy Qt gave back. Python owns it.
    """
    #  QMediaMetaData QPlatformMediaRecorder::metaData() const
    ritual = 'ritual_ZNK22QPlatformMediaRecorder8metaDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QPlatformMediaRecorder8metaDataEv'
    address = self.uglySide.call(ritual)
    from . import QMediaMetaData
    return QMediaMetaData._cuteOwning(address)

  def error(self) -> QMediaRecorder.Error:
    """
    Calls Qt's 'QMediaRecorder::Error QPlatformMediaRecorder::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediarecorder.html#error

    Returns
    -------

    QMediaRecorder.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaRecorder.Error(number)' gives.
    """
    #  QMediaRecorder::Error QPlatformMediaRecorder::error() const
    return QMediaRecorder.Error(self.uglySide.call(
        'ritual_ZNK22QPlatformMediaRecorder5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPlatformMediaRecorder::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformMediaRecorder::errorString() const
    return self.uglySide.call(
        'ritual_ZNK22QPlatformMediaRecorder11errorStringEv',
    )

  def outputLocation(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPlatformMediaRecorder::outputLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#outputLocation

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlatformMediaRecorder::outputLocation() const
    address = self.uglySide.call(
        'ritual_ZNK22QPlatformMediaRecorder14outputLocationEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def actualLocation(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPlatformMediaRecorder::actualLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#actualLocation

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlatformMediaRecorder::actualLocation() const
    address = self.uglySide.call(
        'ritual_ZNK22QPlatformMediaRecorder14actualLocationEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def outputDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QPlatformMediaRecorder::outputDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#outputDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QPlatformMediaRecorder::outputDevice() const
    address = self.uglySide.call(
        'ritual_ZNK22QPlatformMediaRecorder12outputDeviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  @overload(QMediaEncoderSettings)
  def findActualLocation(self, settings: QMediaEncoderSettings) -> str:
    """
    Calls Qt's 'QString QPlatformMediaRecorder::findActualLocation(const
    QMediaEncoderSettings &settings) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#findActualLocation

    Parameters
    ----------

    settings : QMediaEncoderSettings
      Passed on as a value: Qt reads the C++ QMediaEncoderSettings, which
      stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformMediaRecorder::findActualLocation(const
    #      QMediaEncoderSettings &settings) const
    return self.uglySide.call(
        'ritual_ZNK22QPlatformMediaRecorder18findActualLocationERK21QMediaE'
        'ncoderSettings',
        self._valueOf(settings),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaMetaData)
  def setMetaData(self, a0: QMediaMetaData) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::setMetaData(const QMediaMetaData
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#setMetaData

    Parameters
    ----------

    a0 : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  void QPlatformMediaRecorder::setMetaData(const QMediaMetaData &a0)
    ritual = (
        'ritual_ZN22QPlatformMediaRecorder11setMetaDataERK14QMediaMetaData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QPlatformMediaRecorder11setMetaDataERK14QMediaMet'
          'aData')
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QUrl)
  def setOutputLocation(self, location: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::setOutputLocation(const QUrl
    &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#setOutputLocation

    Parameters
    ----------

    location : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformMediaRecorder::setOutputLocation(const QUrl &location)
    ritual = 'ritual_ZN22QPlatformMediaRecorder17setOutputLocationERK4QUrl'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QPlatformMediaRecorder17setOutputLocationERK4QUrl')
    self.uglySide.call(ritual, self._valueOf(location))

  @overload(QIODevice)
  @overload(NoneType)
  def setOutputDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::setOutputDevice(QIODevice
    *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#setOutputDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaRecorder::setOutputDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder15setOutputDeviceEP9QIODevice',
        self._addressOf(device),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QPlatformMediaRecorder::QPlatformMediaRecorder(QMediaRecorder
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformMediaRecorder.__init__' has no cute function yet. Qt's "
        "'QPlatformMediaRecorder::QPlatformMediaRecorder(QMediaRecorder "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  def pause(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediarecorder.html#pause
    """
    #  void QPlatformMediaRecorder::pause()
    ritual = 'ritual_ZN22QPlatformMediaRecorder5pauseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformMediaRecorder5pauseEv'
    self.uglySide.call(ritual)

  def resume(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediarecorder.html#resume
    """
    #  void QPlatformMediaRecorder::resume()
    ritual = 'ritual_ZN22QPlatformMediaRecorder6resumeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformMediaRecorder6resumeEv'
    self.uglySide.call(ritual)

  def stop(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediarecorder.html#stop
    """
    #  void QPlatformMediaRecorder::stop()
    self.uglySide.call('ritual_ZN22QPlatformMediaRecorder4stopEv')

  def clearActualLocation(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::clearActualLocation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#clearActualLocation
    """
    #  void QPlatformMediaRecorder::clearActualLocation()
    self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder19clearActualLocationEv',
    )

  def clearError(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::clearError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#clearError
    """
    #  void QPlatformMediaRecorder::clearError()
    self.uglySide.call('ritual_ZN22QPlatformMediaRecorder10clearErrorEv')

  def updateAutoStop(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::updateAutoStop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#updateAutoStop
    """
    #  void QPlatformMediaRecorder::updateAutoStop()
    ritual = 'ritual_ZN22QPlatformMediaRecorder14updateAutoStopEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformMediaRecorder14updateAutoStopEv'
    self.uglySide.call(ritual)

  @overload(QMediaRecorder.RecorderState)
  def stateChanged(self, state: QMediaRecorder.RecorderState) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaRecorder::stateChanged(QMediaRecorder::RecorderState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#stateChanged

    Parameters
    ----------

    state : QMediaRecorder.RecorderState
      Passed on as its number.
    """
    #  void
    #      QPlatformMediaRecorder::stateChanged(QMediaRecorder::RecorderState
    #      state)
    self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder12stateChangedEN14QMediaRecorder1'
        '3RecorderStateE',
        state.value,
    )

  @overload(int)
  def durationChanged(self, position: int) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::durationChanged(qint64
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#durationChanged

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QPlatformMediaRecorder::durationChanged(qint64 position)
    self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder15durationChangedEx', position,
    )

  @overload(QUrl)
  def actualLocationChanged(self, location: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::actualLocationChanged(const QUrl
    &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#actualLocationChanged

    Parameters
    ----------

    location : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformMediaRecorder::actualLocationChanged(const QUrl
    #      &location)
    self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder21actualLocationChangedERK4QUrl',
        self._valueOf(location),
    )

  @overload(QMediaRecorder.Error, str)
  def updateError(
      self,
      error: QMediaRecorder.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaRecorder::updateError(QMediaRecorder::Error error, const
    QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#updateError

    Parameters
    ----------

    error : QMediaRecorder.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformMediaRecorder::updateError(QMediaRecorder::Error error,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder11updateErrorEN14QMediaRecorder5E'
        'rrorERK7QString',
        error.value, errorString,
    )

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaRecorder::metaDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#metaDataChanged
    """
    #  void QPlatformMediaRecorder::metaDataChanged()
    self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder15metaDataChangedEv',
    )

  def mediaRecorder(self) -> Optional[QMediaRecorder]:
    """
    Calls Qt's 'QMediaRecorder *QPlatformMediaRecorder::mediaRecorder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediarecorder.html#mediaRecorder

    Returns
    -------

    Optional[QMediaRecorder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaRecorder *QPlatformMediaRecorder::mediaRecorder()
    address = self.uglySide.call(
        'ritual_ZN22QPlatformMediaRecorder13mediaRecorderEv',
    )
    return QMediaRecorder._cuteAt(address)

  @staticmethod
  def record(*__, **_) -> Never:
    """
    Qt's 'void QPlatformMediaRecorder::record(QMediaEncoderSettings
    &settings)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaRecorder.record' has no cute function yet. Qt's "
        "'void QPlatformMediaRecorder::record(QMediaEncoderSettings "
        "&settings)': takes a type Python has no way to hand over yet.")
