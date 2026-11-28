"""
QPlatformMediaIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaintegration_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformMediaIntegration to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String, QMetaObject
  from . import QCapturableWindow, QCapturableWindowPrivate
  from . import QGStreamerInterface, QPlatformAudioDevices
  from . import QPlatformCapturableWindows, QPlatformMediaFormatInfo
  from . import QPlatformSurfaceCapture, QPlatformVideoDevices
  from . import QScreenCapture, QWindowCapture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCapturableWindowPrivate = WAIT['QCapturableWindowPrivate']
  QLatin1String = WAIT['QLatin1String']
  QScreenCapture = WAIT['QScreenCapture']
  QWindowCapture = WAIT['QWindowCapture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformMediaIntegration(QObject):
  """
  The cute side of Qt's QPlatformMediaIntegration: a plain Python object
  standing in front of one C++ QPlatformMediaIntegration.

  It is built on the cute 'QObject', as Qt's QPlatformMediaIntegration is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformMediaIntegration that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'instance',
  'formatInfo', 'createScreenCapture', 'createWindowCapture',
  'capturableWindowsList', 'isCapturableWindowValid', 'videoDevices',
  'capturableWindows', 'audioDevices', 'availableBackends', 'defaultBackend',
  'setBackend', 'name', 'audioBackendName',
  'isCameraSwitchingDuringRecordingSupported', 'gstreamerInterface',
  'resetInstance', 'createFormatInfo', 'createVideoDevices',
  'createCapturableWindows'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformMediaIntegration::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformMediaIntegration::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformMediaIntegration::~QPlatformMediaIntegration()': the
    destructor: Python never removes a C++ QPlatformMediaIntegration.
  - Qt's 'q23::expected<QPlatformCamera *, QString>
    QPlatformMediaIntegration::createCamera(QCamera *a0)': gives a type
    Python has no way to take yet.
  - Qt's 'q23::expected<QPlatformAudioDecoder *, QString>
    QPlatformMediaIntegration::createAudioDecoder(QAudioDecoder *a0)': gives
    a type Python has no way to take yet.
  - Qt's 'q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString>
    QPlatformMediaIntegration::createAudioResampler(const QAudioFormat &a0,
    const QAudioFormat &a1)': gives a type Python has no way to take yet.
  - Qt's 'q23::expected<QPlatformMediaCaptureSession *, QString>
    QPlatformMediaIntegration::createCaptureSession()': gives a type Python
    has no way to take yet.
  - Qt's 'q23::expected<QPlatformMediaPlayer *, QString>
    QPlatformMediaIntegration::createPlayer(QMediaPlayer *a0)': gives a type
    Python has no way to take yet.
  - Qt's 'q23::expected<QPlatformMediaRecorder *, QString>
    QPlatformMediaIntegration::createRecorder(QMediaRecorder *a0)': gives a
    type Python has no way to take yet.
  - Qt's 'q23::expected<QPlatformImageCapture *, QString>
    QPlatformMediaIntegration::createImageCapture(QImageCapture *a0)': gives
    a type Python has no way to take yet.
  - Qt's 'q23::expected<QPlatformAudioInput *, QString>
    QPlatformMediaIntegration::createAudioInput(QAudioInput *a0)': gives a
    type Python has no way to take yet.
  - Qt's 'q23::expected<QPlatformAudioOutput *, QString>
    QPlatformMediaIntegration::createAudioOutput(QAudioOutput *a0)': gives a
    type Python has no way to take yet.
  - Qt's 'q23::expected<QPlatformVideoSink *, QString>
    QPlatformMediaIntegration::createVideoSink(QVideoSink *a0)': gives a type
    Python has no way to take yet.
  - Qt's 'q23::expected<QCapturableWindow, QString>
    QPlatformMediaIntegration::capturableWindowFromQWindow(QWindow *a0)':
    gives a type Python has no way to take yet.
  - Qt's 'QVideoFrame
    QPlatformMediaIntegration::convertVideoFrame(QVideoFrame &a0, const
    QVideoFrameFormat &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'q23::expected<QPlatformCamera *, QString>
    QPlatformMediaIntegration::createGStreamerVideoSource(
    QGStreamerVideoSource *a0, const GstElementOrDescription &a1)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 42 functions Qt declares: 2 not a gap; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QPlatformMediaIntegration is created at the first use, not by
    'QPlatformMediaIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMediaIntegration.
  - Qt tells when it has removed the C++ QPlatformMediaIntegration. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformMediaIntegration that has no cute function
    yet, 'capturableWindowFromQWindow', 'convertVideoFrame',
    'createAudioDecoder', 'createAudioDevices', 'createAudioInput',
    'createAudioOutput', 'createAudioResampler', 'createCamera',
    'createCaptureSession', 'createGStreamerVideoSource',
    'createImageCapture', 'createPlayer', 'createRecorder',
    'createVideoSink', holds a function that raises 'NotImplementedError',
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
    Calls Qt's 'QString QPlatformMediaIntegration::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaintegration.html#tr

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
    #  QString QPlatformMediaIntegration::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QPlatformMediaIntegration2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QPlatformMediaIntegration]:
    """
    Calls Qt's 'QPlatformMediaIntegration
    *QPlatformMediaIntegration::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#instance

    Returns
    -------

    Optional[QPlatformMediaIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMediaIntegration *QPlatformMediaIntegration::instance()
    address = Rituals.call('ritual_ZN25QPlatformMediaIntegration8instanceEv')
    return QPlatformMediaIntegration._cuteAt(address)

  @staticmethod
  def availableBackends() -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformMediaIntegration::availableBackends()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#availableBackends

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformMediaIntegration::availableBackends()
    address = Rituals.call(
        'ritual_ZN25QPlatformMediaIntegration17availableBackendsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def defaultBackend() -> str:
    """
    Calls Qt's 'QString QPlatformMediaIntegration::defaultBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#defaultBackend

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformMediaIntegration::defaultBackend()
    return Rituals.call(
        'ritual_ZN25QPlatformMediaIntegration14defaultBackendEv',
    )

  @staticmethod
  @overload(str)
  def setBackend(backend: str) -> None:
    """
    Calls Qt's 'void QPlatformMediaIntegration::setBackend(const QString
    &backend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#setBackend

    Parameters
    ----------

    backend : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformMediaIntegration::setBackend(const QString &backend)
    Rituals.call(
        'ritual_ZN25QPlatformMediaIntegration10setBackendERK7QString',
        backend,
    )

  @staticmethod
  def audioBackendName() -> QLatin1String:
    """
    Calls Qt's 'QLatin1String QPlatformMediaIntegration::audioBackendName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#audioBackendName

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String QPlatformMediaIntegration::audioBackendName()
    address = Rituals.call(
        'ritual_ZN25QPlatformMediaIntegration16audioBackendNameEv',
    )
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMediaIntegration'

  #  A C++ QPlatformMediaIntegration Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformMediaIntegration'

  #  The functions Qt calls itself that QPlatformMediaIntegration is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createCamera': (
          'q23::expected<QPlatformCamera *, QString> '
          'QPlatformMediaIntegration::createCamera(QCamera *)',
      ),
      'createAudioDecoder': (
          'q23::expected<QPlatformAudioDecoder *, QString> '
          'QPlatformMediaIntegration::createAudioDecoder(QAudioDecoder *)',
      ),
      'createAudioResampler': (
          'q23::expected<std::unique_ptr<QPlatformAudioResampler>, '
          'QString> QPlatformMediaIntegration::createAudioResampler(const '
          'QAudioFormat &, const QAudioFormat &)',
      ),
      'createCaptureSession': (
          'q23::expected<QPlatformMediaCaptureSession *, QString> '
          'QPlatformMediaIntegration::createCaptureSession()',
      ),
      'createPlayer': (
          'q23::expected<QPlatformMediaPlayer *, QString> '
          'QPlatformMediaIntegration::createPlayer(QMediaPlayer *)',
      ),
      'createRecorder': (
          'q23::expected<QPlatformMediaRecorder *, QString> '
          'QPlatformMediaIntegration::createRecorder(QMediaRecorder *)',
      ),
      'createImageCapture': (
          'q23::expected<QPlatformImageCapture *, QString> '
          'QPlatformMediaIntegration::createImageCapture(QImageCapture *)',
      ),
      'createAudioInput': (
          'q23::expected<QPlatformAudioInput *, QString> '
          'QPlatformMediaIntegration::createAudioInput(QAudioInput *)',
      ),
      'createAudioOutput': (
          'q23::expected<QPlatformAudioOutput *, QString> '
          'QPlatformMediaIntegration::createAudioOutput(QAudioOutput *)',
      ),
      'createVideoSink': (
          'q23::expected<QPlatformVideoSink *, QString> '
          'QPlatformMediaIntegration::createVideoSink(QVideoSink *)',
      ),
      'convertVideoFrame': (
          'QVideoFrame '
          'QPlatformMediaIntegration::convertVideoFrame(QVideoFrame &, '
          'const QVideoFrameFormat &)',
      ),
      'createGStreamerVideoSource': (
          'q23::expected<QPlatformCamera *, QString> '
          'QPlatformMediaIntegration::createGStreamerVideoSource(QGStreamer'
          'VideoSource *, const GstElementOrDescription &)',
      ),
      'createAudioDevices': (
          'std::unique_ptr<QPlatformAudioDevices> '
          'QPlatformMediaIntegration::createAudioDevices()',
      ),
  }

  #  The functions Qt calls itself that QPlatformMediaIntegration is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'createScreenCapture': (
          ('_ZN25QPlatformMediaIntegration19createScreenCaptureEP14QScreenC'
           'apture',
           ('address', 'address', 'QtMultimedia:QPlatformSurfaceCapture'),
           (
               ('address', 'address', 'QtMultimedia:QScreenCapture'),
           )),
      ),
      'createWindowCapture': (
          ('_ZN25QPlatformMediaIntegration19createWindowCaptureEP14QWindowC'
           'apture',
           ('address', 'address', 'QtMultimedia:QPlatformSurfaceCapture'),
           (
               ('address', 'address', 'QtMultimedia:QWindowCapture'),
           )),
      ),
      'isCameraSwitchingDuringRecordingSupported': (
          ('_ZNK25QPlatformMediaIntegration41isCameraSwitchingDuringRecordi'
           'ngSupportedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'gstreamerInterface': (
          ('_ZN25QPlatformMediaIntegration18gstreamerInterfaceEv',
           ('address', 'address', 'QtMultimedia:QGStreamerInterface'),
           ()),
      ),
      'createFormatInfo': (
          ('_ZN25QPlatformMediaIntegration16createFormatInfoEv',
           ('address', 'address', 'QtMultimedia:QPlatformMediaFormatInfo'),
           ()),
      ),
      'createVideoDevices': (
          ('_ZN25QPlatformMediaIntegration18createVideoDevicesEv',
           ('address', 'address', 'QtMultimedia:QPlatformVideoDevices'),
           ()),
      ),
      'createCapturableWindows': (
          ('_ZN25QPlatformMediaIntegration23createCapturableWindowsEv',
           ('address', 'address', 'QtMultimedia:QPlatformCapturableWindows'),
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
    Calls Qt's 'const QMetaObject *QPlatformMediaIntegration::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformMediaIntegration::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformMediaIntegration10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isCameraSwitchingDuringRecordingSupported(self) -> bool:
    """
    Calls Qt's 'bool
    QPlatformMediaIntegration::isCameraSwitchingDuringRecordingSupported()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html
    """
    #  bool QPlatformMediaIntegration::
    #      isCameraSwitchingDuringRecordingSupported() const
    ritual = (
        'ritual_ZNK25QPlatformMediaIntegration41isCameraSwitchingDuringReco'
        'rdingSupportedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QPlatformMediaIntegration41isCameraSwitchingDuri'
          'ngRecordingSupportedEv')
    return self.uglySide.call(ritual)

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

  @overload(QLatin1String)
  def __init__(self, a0: QLatin1String) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformMediaIntegration::QPlatformMediaIntegration(QLatin1String a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html

    Parameters
    ----------

    a0 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QPlatformMediaIntegration::QPlatformMediaIntegration(QLatin1String a0)
    self._noteCreation(QPlatformMediaIntegration, lambda: Rituals.call(
        'ritual_ZN25QPlatformMediaIntegrationC1E13QLatin1String',
        self._valueOf(a0),
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

  def formatInfo(self) -> Optional[QPlatformMediaFormatInfo]:
    """
    Calls Qt's 'const QPlatformMediaFormatInfo
    *QPlatformMediaIntegration::formatInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#formatInfo

    Returns
    -------

    Optional[QPlatformMediaFormatInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlatformMediaFormatInfo
    #      *QPlatformMediaIntegration::formatInfo()
    address = self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration10formatInfoEv',
    )
    from . import QPlatformMediaFormatInfo
    return QPlatformMediaFormatInfo._cuteAt(address)

  @overload(QScreenCapture)
  @overload(NoneType)
  def createScreenCapture(
      self,
      a0: Optional[QScreenCapture],
  ) -> Optional[QPlatformSurfaceCapture]:
    """
    Calls Qt's 'QPlatformSurfaceCapture
    *QPlatformMediaIntegration::createScreenCapture(QScreenCapture *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#createScreenCapture

    Parameters
    ----------

    a0 : Optional[QScreenCapture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformSurfaceCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurfaceCapture
    #      *QPlatformMediaIntegration::createScreenCapture(QScreenCapture
    #      *a0)
    ritual = (
        'ritual_ZN25QPlatformMediaIntegration19createScreenCaptureEP14QScre'
        'enCapture')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPlatformMediaIntegration19createScreenCaptureEP1'
          '4QScreenCapture')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from . import QPlatformSurfaceCapture
    return QPlatformSurfaceCapture._cuteAt(address)

  @overload(QWindowCapture)
  @overload(NoneType)
  def createWindowCapture(
      self,
      a0: Optional[QWindowCapture],
  ) -> Optional[QPlatformSurfaceCapture]:
    """
    Calls Qt's 'QPlatformSurfaceCapture
    *QPlatformMediaIntegration::createWindowCapture(QWindowCapture *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#createWindowCapture

    Parameters
    ----------

    a0 : Optional[QWindowCapture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformSurfaceCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurfaceCapture
    #      *QPlatformMediaIntegration::createWindowCapture(QWindowCapture
    #      *a0)
    ritual = (
        'ritual_ZN25QPlatformMediaIntegration19createWindowCaptureEP14QWind'
        'owCapture')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPlatformMediaIntegration19createWindowCaptureEP1'
          '4QWindowCapture')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from . import QPlatformSurfaceCapture
    return QPlatformSurfaceCapture._cuteAt(address)

  def capturableWindowsList(self) -> QList[QCapturableWindow]:
    """
    Calls Qt's 'QList<QCapturableWindow>
    QPlatformMediaIntegration::capturableWindowsList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html

    Returns
    -------

    QList[QCapturableWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCapturableWindow>
    #      QPlatformMediaIntegration::capturableWindowsList()
    address = self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration21capturableWindowsListEv',
    )
    from . import QCapturableWindow
    return QList[QCapturableWindow]._cuteOwning(address)

  @overload(QCapturableWindowPrivate)
  def isCapturableWindowValid(self, a0: QCapturableWindowPrivate) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaIntegration::isCapturableWindowValid(const
    QCapturableWindowPrivate &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html

    Parameters
    ----------

    a0 : QCapturableWindowPrivate
      Passed on as a value: Qt reads the C++ QCapturableWindowPrivate, which
      stays Python's own.
    """
    #  bool QPlatformMediaIntegration::isCapturableWindowValid(const
    #      QCapturableWindowPrivate &a0)
    return self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration23isCapturableWindowValidERK24'
        'QCapturableWindowPrivate',
        self._valueOf(a0),
    )

  def videoDevices(self) -> Optional[QPlatformVideoDevices]:
    """
    Calls Qt's 'QPlatformVideoDevices
    *QPlatformMediaIntegration::videoDevices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#videoDevices

    Returns
    -------

    Optional[QPlatformVideoDevices]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformVideoDevices *QPlatformMediaIntegration::videoDevices()
    address = self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration12videoDevicesEv',
    )
    from . import QPlatformVideoDevices
    return QPlatformVideoDevices._cuteAt(address)

  def capturableWindows(self) -> Optional[QPlatformCapturableWindows]:
    """
    Calls Qt's 'QPlatformCapturableWindows
    *QPlatformMediaIntegration::capturableWindows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#capturableWindows

    Returns
    -------

    Optional[QPlatformCapturableWindows]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformCapturableWindows
    #      *QPlatformMediaIntegration::capturableWindows()
    address = self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration17capturableWindowsEv',
    )
    from . import QPlatformCapturableWindows
    return QPlatformCapturableWindows._cuteAt(address)

  def audioDevices(self) -> Optional[QPlatformAudioDevices]:
    """
    Calls Qt's 'QPlatformAudioDevices
    *QPlatformMediaIntegration::audioDevices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#audioDevices

    Returns
    -------

    Optional[QPlatformAudioDevices]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioDevices *QPlatformMediaIntegration::audioDevices()
    address = self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration12audioDevicesEv',
    )
    from . import QPlatformAudioDevices
    return QPlatformAudioDevices._cuteAt(address)

  def name(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1String QPlatformMediaIntegration::name()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#name

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String QPlatformMediaIntegration::name()
    address = self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration4nameEv',
    )
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def gstreamerInterface(self) -> Optional[QGStreamerInterface]:
    """
    Calls Qt's 'QGStreamerInterface
    *QPlatformMediaIntegration::gstreamerInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#gstreamerInterface

    Returns
    -------

    Optional[QGStreamerInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGStreamerInterface *QPlatformMediaIntegration::gstreamerInterface()
    ritual = 'ritual_ZN25QPlatformMediaIntegration18gstreamerInterfaceEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPlatformMediaIntegration18gstreamerInterfaceEv')
    address = self.uglySide.call(ritual)
    from . import QGStreamerInterface
    return QGStreamerInterface._cuteAt(address)

  def resetInstance(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaIntegration::resetInstance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#resetInstance
    """
    #  void QPlatformMediaIntegration::resetInstance()
    self.uglySide.call(
        'ritual_ZN25QPlatformMediaIntegration13resetInstanceEv',
    )

  def createFormatInfo(self) -> Optional[QPlatformMediaFormatInfo]:
    """
    Calls Qt's 'QPlatformMediaFormatInfo
    *QPlatformMediaIntegration::createFormatInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#createFormatInfo

    Returns
    -------

    Optional[QPlatformMediaFormatInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMediaFormatInfo
    #      *QPlatformMediaIntegration::createFormatInfo()
    ritual = 'ritual_ZN25QPlatformMediaIntegration16createFormatInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QPlatformMediaIntegration16createFormatInfoEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMediaFormatInfo
    return QPlatformMediaFormatInfo._cuteAt(address)

  def createVideoDevices(self) -> Optional[QPlatformVideoDevices]:
    """
    Calls Qt's 'QPlatformVideoDevices
    *QPlatformMediaIntegration::createVideoDevices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html#createVideoDevices

    Returns
    -------

    Optional[QPlatformVideoDevices]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformVideoDevices *QPlatformMediaIntegration::createVideoDevices()
    ritual = 'ritual_ZN25QPlatformMediaIntegration18createVideoDevicesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPlatformMediaIntegration18createVideoDevicesEv')
    address = self.uglySide.call(ritual)
    from . import QPlatformVideoDevices
    return QPlatformVideoDevices._cuteAt(address)

  def createCapturableWindows(self) -> Optional[QPlatformCapturableWindows]:
    """
    Calls Qt's 'QPlatformCapturableWindows
    *QPlatformMediaIntegration::createCapturableWindows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaintegration.html

    Returns
    -------

    Optional[QPlatformCapturableWindows]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformCapturableWindows
    #      *QPlatformMediaIntegration::createCapturableWindows()
    ritual = (
        'ritual_ZN25QPlatformMediaIntegration23createCapturableWindowsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPlatformMediaIntegration23createCapturableWindow'
          'sEv')
    address = self.uglySide.call(ritual)
    from . import QPlatformCapturableWindows
    return QPlatformCapturableWindows._cuteAt(address)

  @staticmethod
  def capturableWindowFromQWindow(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QCapturableWindow, QString>
    QPlatformMediaIntegration::capturableWindowFromQWindow(QWindow *a0)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.capturableWindowFromQWindow' has no "
        "cute function yet. Qt's 'q23::expected<QCapturableWindow, QString> "
        "QPlatformMediaIntegration::capturableWindowFromQWindow(QWindow "
        "*a0)': gives a type Python has no way to take yet.")

  @staticmethod
  def convertVideoFrame(*__, **_) -> Never:
    """
    Qt's 'QVideoFrame
    QPlatformMediaIntegration::convertVideoFrame(QVideoFrame &a0, const
    QVideoFrameFormat &a1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.convertVideoFrame' has no cute function "
        "yet. Qt's 'QVideoFrame "
        "QPlatformMediaIntegration::convertVideoFrame(QVideoFrame &a0, "
        "const QVideoFrameFormat &a1)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def createAudioDecoder(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformAudioDecoder *, QString>
    QPlatformMediaIntegration::createAudioDecoder(QAudioDecoder *a0)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createAudioDecoder' has no cute "
        "function yet. Qt's 'q23::expected<QPlatformAudioDecoder *, "
        "QString> "
        "QPlatformMediaIntegration::createAudioDecoder(QAudioDecoder *a0)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def createAudioDevices(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QPlatformAudioDevices>
    QPlatformMediaIntegration::createAudioDevices()': the compiler refuses
    its ritual as it would be written here: invalid application of 'sizeof'
    to an incomplete type 'QPlatformAudioDevices'.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createAudioDevices' has no cute "
        "function yet. Qt's 'std::unique_ptr<QPlatformAudioDevices> "
        "QPlatformMediaIntegration::createAudioDevices()': the compiler "
        "refuses its ritual as it would be written here: invalid "
        "application of 'sizeof' to an incomplete type "
        "'QPlatformAudioDevices'.")

  @staticmethod
  def createAudioInput(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformAudioInput *, QString>
    QPlatformMediaIntegration::createAudioInput(QAudioInput *a0)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createAudioInput' has no cute function "
        "yet. Qt's 'q23::expected<QPlatformAudioInput *, QString> "
        "QPlatformMediaIntegration::createAudioInput(QAudioInput *a0)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def createAudioOutput(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformAudioOutput *, QString>
    QPlatformMediaIntegration::createAudioOutput(QAudioOutput *a0)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createAudioOutput' has no cute function "
        "yet. Qt's 'q23::expected<QPlatformAudioOutput *, QString> "
        "QPlatformMediaIntegration::createAudioOutput(QAudioOutput *a0)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def createAudioResampler(*__, **_) -> Never:
    """
    Qt's 'q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString>
    QPlatformMediaIntegration::createAudioResampler(const QAudioFormat &a0,
    const QAudioFormat &a1)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createAudioResampler' has no cute "
        "function yet. Qt's "
        "'q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString> "
        "QPlatformMediaIntegration::createAudioResampler(const QAudioFormat "
        "&a0, const QAudioFormat &a1)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def createCamera(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformCamera *, QString>
    QPlatformMediaIntegration::createCamera(QCamera *a0)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createCamera' has no cute function yet. "
        "Qt's 'q23::expected<QPlatformCamera *, QString> "
        "QPlatformMediaIntegration::createCamera(QCamera *a0)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def createCaptureSession(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformMediaCaptureSession *, QString>
    QPlatformMediaIntegration::createCaptureSession()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createCaptureSession' has no cute "
        "function yet. Qt's 'q23::expected<QPlatformMediaCaptureSession *, "
        "QString> QPlatformMediaIntegration::createCaptureSession()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def createGStreamerVideoSource(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformCamera *, QString>
    QPlatformMediaIntegration::createGStreamerVideoSource(
    QGStreamerVideoSource *a0, const GstElementOrDescription &a1)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createGStreamerVideoSource' has no cute "
        "function yet. Qt's 'q23::expected<QPlatformCamera *, QString> "
        "QPlatformMediaIntegration::createGStreamerVideoSource(QGStreamerVid"
        "eoSource *a0, const GstElementOrDescription &a1)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def createImageCapture(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformImageCapture *, QString>
    QPlatformMediaIntegration::createImageCapture(QImageCapture *a0)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createImageCapture' has no cute "
        "function yet. Qt's 'q23::expected<QPlatformImageCapture *, "
        "QString> "
        "QPlatformMediaIntegration::createImageCapture(QImageCapture *a0)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def createPlayer(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformMediaPlayer *, QString>
    QPlatformMediaIntegration::createPlayer(QMediaPlayer *a0)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createPlayer' has no cute function yet. "
        "Qt's 'q23::expected<QPlatformMediaPlayer *, QString> "
        "QPlatformMediaIntegration::createPlayer(QMediaPlayer *a0)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def createRecorder(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformMediaRecorder *, QString>
    QPlatformMediaIntegration::createRecorder(QMediaRecorder *a0)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createRecorder' has no cute function "
        "yet. Qt's 'q23::expected<QPlatformMediaRecorder *, QString> "
        "QPlatformMediaIntegration::createRecorder(QMediaRecorder *a0)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def createVideoSink(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QPlatformVideoSink *, QString>
    QPlatformMediaIntegration::createVideoSink(QVideoSink *a0)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaIntegration.createVideoSink' has no cute function "
        "yet. Qt's 'q23::expected<QPlatformVideoSink *, QString> "
        "QPlatformMediaIntegration::createVideoSink(QVideoSink *a0)': gives "
        "a type Python has no way to take yet.")
