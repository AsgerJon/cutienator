"""
QMediaCaptureSession binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qmediacapturesession.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAudioBufferInput, QAudioInput, QAudioOutput, QCamera
  from . import QImageCapture, QMediaCaptureSessionPrivate, QMediaRecorder
  from . import QPlatformMediaCaptureSession, QScreenCapture
  from . import QVideoFrameInput, QVideoSink, QWindowCapture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioBufferInput = WAIT['QAudioBufferInput']
  QAudioInput = WAIT['QAudioInput']
  QAudioOutput = WAIT['QAudioOutput']
  QCamera = WAIT['QCamera']
  QImageCapture = WAIT['QImageCapture']
  QMediaRecorder = WAIT['QMediaRecorder']
  QScreenCapture = WAIT['QScreenCapture']
  QVideoFrameInput = WAIT['QVideoFrameInput']
  QVideoSink = WAIT['QVideoSink']
  QWindowCapture = WAIT['QWindowCapture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMediaCaptureSession(QObject):
  """
  The cute side of Qt's QMediaCaptureSession: a plain Python object standing
  in front of one C++ QMediaCaptureSession.

  It is built on the cute 'QObject', as Qt's QMediaCaptureSession is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMediaCaptureSession that has a ritual and that
  Python can call so far, 39 names in all: 'metaObject', 'tr', 'audioInput',
  'setAudioInput', 'audioBufferInput', 'setAudioBufferInput', 'camera',
  'setCamera', 'nativeVideoSource', 'setNativeVideoSource', 'imageCapture',
  'setImageCapture', 'screenCapture', 'setScreenCapture', 'windowCapture',
  'setWindowCapture', 'videoFrameInput', 'setVideoFrameInput', 'recorder',
  'setRecorder', 'setVideoOutput', 'videoOutput', 'setVideoSink',
  'videoSink', 'setAudioOutput', 'audioOutput', 'platformSession',
  'audioInputChanged', 'audioBufferInputChanged', 'cameraChanged',
  'nativeVideoSourceChanged', 'screenCaptureChanged', 'windowCaptureChanged',
  'videoFrameInputChanged', 'imageCaptureChanged', 'recorderChanged',
  'videoOutputChanged', 'audioOutputChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMediaCaptureSession::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QMediaCaptureSession::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QMediaCaptureSession::~QMediaCaptureSession()': the destructor:
    Python never removes a C++ QMediaCaptureSession.
  - Qt's 'const QMediaCaptureSessionPrivate *QMediaCaptureSession::d_func()
    const': takes in Python what 'QMediaCaptureSessionPrivate
    *QMediaCaptureSession::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 49 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QMediaCaptureSession is created at the first use, not by
    'QMediaCaptureSession(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMediaCaptureSession.
  - Qt tells when it has removed the C++ QMediaCaptureSession. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QMediaCaptureSession that has no cute function yet,
    'setObject', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QMediaCaptureSession::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediacapturesession.html#tr

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
    #  QString QMediaCaptureSession::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QMediaCaptureSession2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaCaptureSession'

  #  A C++ QMediaCaptureSession Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMediaCaptureSession'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMediaCaptureSession::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMediaCaptureSession::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def audioInput(self) -> Optional[QAudioInput]:
    """
    Calls Qt's 'QAudioInput *QMediaCaptureSession::audioInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#audioInput

    Returns
    -------

    Optional[QAudioInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioInput *QMediaCaptureSession::audioInput() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession10audioInputEv',
    )
    from . import QAudioInput
    return QAudioInput._cuteAt(address)

  def audioBufferInput(self) -> Optional[QAudioBufferInput]:
    """
    Calls Qt's 'QAudioBufferInput *QMediaCaptureSession::audioBufferInput()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#audioBufferInput

    Returns
    -------

    Optional[QAudioBufferInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioBufferInput *QMediaCaptureSession::audioBufferInput() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession16audioBufferInputEv',
    )
    from . import QAudioBufferInput
    return QAudioBufferInput._cuteAt(address)

  def camera(self) -> Optional[QCamera]:
    """
    Calls Qt's 'QCamera *QMediaCaptureSession::camera() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediacapturesession.html#camera

    Returns
    -------

    Optional[QCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCamera *QMediaCaptureSession::camera() const
    address = self.uglySide.call('ritual_ZNK20QMediaCaptureSession6cameraEv')
    from . import QCamera
    return QCamera._cuteAt(address)

  def nativeVideoSource(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMediaCaptureSession::nativeVideoSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#nativeVideoSource

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QMediaCaptureSession::nativeVideoSource() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession17nativeVideoSourceEv',
    )
    return QObject._cuteAt(address)

  def videoFrameInput(self) -> Optional[QVideoFrameInput]:
    """
    Calls Qt's 'QVideoFrameInput *QMediaCaptureSession::videoFrameInput()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#videoFrameInput

    Returns
    -------

    Optional[QVideoFrameInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoFrameInput *QMediaCaptureSession::videoFrameInput() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession15videoFrameInputEv',
    )
    from . import QVideoFrameInput
    return QVideoFrameInput._cuteAt(address)

  def videoOutput(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMediaCaptureSession::videoOutput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#videoOutput

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QMediaCaptureSession::videoOutput() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession11videoOutputEv',
    )
    return QObject._cuteAt(address)

  def videoSink(self) -> Optional[QVideoSink]:
    """
    Calls Qt's 'QVideoSink *QMediaCaptureSession::videoSink() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#videoSink

    Returns
    -------

    Optional[QVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoSink *QMediaCaptureSession::videoSink() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession9videoSinkEv',
    )
    from . import QVideoSink
    return QVideoSink._cuteAt(address)

  def audioOutput(self) -> Optional[QAudioOutput]:
    """
    Calls Qt's 'QAudioOutput *QMediaCaptureSession::audioOutput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#audioOutput

    Returns
    -------

    Optional[QAudioOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioOutput *QMediaCaptureSession::audioOutput() const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession11audioOutputEv',
    )
    from . import QAudioOutput
    return QAudioOutput._cuteAt(address)

  def platformSession(self) -> Optional[QPlatformMediaCaptureSession]:
    """
    Calls Qt's 'QPlatformMediaCaptureSession
    *QMediaCaptureSession::platformSession() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#platformSession

    Returns
    -------

    Optional[QPlatformMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMediaCaptureSession *QMediaCaptureSession::platformSession()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QMediaCaptureSession15platformSessionEv',
    )
    from . import QPlatformMediaCaptureSession
    return QPlatformMediaCaptureSession._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioInput)
  @overload(NoneType)
  def setAudioInput(self, input: Optional[QAudioInput]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setAudioInput(QAudioInput
    *input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setAudioInput

    Parameters
    ----------

    input : Optional[QAudioInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setAudioInput(QAudioInput *input)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession13setAudioInputEP11QAudioInput',
        self._addressOf(input),
    )

  @overload(QAudioBufferInput)
  @overload(NoneType)
  def setAudioBufferInput(self, input: Optional[QAudioBufferInput]) -> None:
    """
    Calls Qt's 'void
    QMediaCaptureSession::setAudioBufferInput(QAudioBufferInput *input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setAudioBufferInput

    Parameters
    ----------

    input : Optional[QAudioBufferInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setAudioBufferInput(QAudioBufferInput
    #      *input)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession19setAudioBufferInputEP17QAudioBuff'
        'erInput',
        self._addressOf(input),
    )

  @overload(QCamera)
  @overload(NoneType)
  def setCamera(self, camera: Optional[QCamera]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setCamera(QCamera *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setCamera

    Parameters
    ----------

    camera : Optional[QCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setCamera(QCamera *camera)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession9setCameraEP7QCamera',
        self._addressOf(camera),
    )

  @overload(QObject)
  @overload(NoneType)
  def setNativeVideoSource(self, videoSource: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setNativeVideoSource(QObject
    *videoSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setNativeVideoSource

    Parameters
    ----------

    videoSource : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setNativeVideoSource(QObject *videoSource)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession20setNativeVideoSourceEP7QObject',
        self._addressOf(videoSource, 'QObject'),
    )

  @overload(QImageCapture)
  @overload(NoneType)
  def setImageCapture(self, imageCapture: Optional[QImageCapture]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setImageCapture(QImageCapture
    *imageCapture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setImageCapture

    Parameters
    ----------

    imageCapture : Optional[QImageCapture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setImageCapture(QImageCapture
    #      *imageCapture)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession15setImageCaptureEP13QImageCapture',
        self._addressOf(imageCapture),
    )

  @overload(QScreenCapture)
  @overload(NoneType)
  def setScreenCapture(
      self,
      screenCapture: Optional[QScreenCapture],
  ) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setScreenCapture(QScreenCapture
    *screenCapture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setScreenCapture

    Parameters
    ----------

    screenCapture : Optional[QScreenCapture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setScreenCapture(QScreenCapture
    #      *screenCapture)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession16setScreenCaptureEP14QScreenCaptur'
        'e',
        self._addressOf(screenCapture),
    )

  @overload(QWindowCapture)
  @overload(NoneType)
  def setWindowCapture(
      self,
      windowCapture: Optional[QWindowCapture],
  ) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setWindowCapture(QWindowCapture
    *windowCapture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setWindowCapture

    Parameters
    ----------

    windowCapture : Optional[QWindowCapture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setWindowCapture(QWindowCapture
    #      *windowCapture)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession16setWindowCaptureEP14QWindowCaptur'
        'e',
        self._addressOf(windowCapture),
    )

  @overload(QVideoFrameInput)
  @overload(NoneType)
  def setVideoFrameInput(self, input: Optional[QVideoFrameInput]) -> None:
    """
    Calls Qt's 'void
    QMediaCaptureSession::setVideoFrameInput(QVideoFrameInput *input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setVideoFrameInput

    Parameters
    ----------

    input : Optional[QVideoFrameInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setVideoFrameInput(QVideoFrameInput *input)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession18setVideoFrameInputEP16QVideoFrame'
        'Input',
        self._addressOf(input),
    )

  @overload(QMediaRecorder)
  @overload(NoneType)
  def setRecorder(self, recorder: Optional[QMediaRecorder]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setRecorder(QMediaRecorder
    *recorder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setRecorder

    Parameters
    ----------

    recorder : Optional[QMediaRecorder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setRecorder(QMediaRecorder *recorder)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession11setRecorderEP14QMediaRecorder',
        self._addressOf(recorder),
    )

  @overload(QObject)
  @overload(NoneType)
  def setVideoOutput(self, output: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setVideoOutput(QObject *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setVideoOutput

    Parameters
    ----------

    output : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setVideoOutput(QObject *output)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession14setVideoOutputEP7QObject',
        self._addressOf(output, 'QObject'),
    )

  @overload(QVideoSink)
  @overload(NoneType)
  def setVideoSink(self, sink: Optional[QVideoSink]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setVideoSink(QVideoSink *sink)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setVideoSink

    Parameters
    ----------

    sink : Optional[QVideoSink]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setVideoSink(QVideoSink *sink)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession12setVideoSinkEP10QVideoSink',
        self._addressOf(sink),
    )

  @overload(QAudioOutput)
  @overload(NoneType)
  def setAudioOutput(self, output: Optional[QAudioOutput]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::setAudioOutput(QAudioOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#setAudioOutput

    Parameters
    ----------

    output : Optional[QAudioOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSession::setAudioOutput(QAudioOutput *output)
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession14setAudioOutputEP12QAudioOutput',
        self._addressOf(output),
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
    'QMediaCaptureSession::QMediaCaptureSession(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#QMediaCaptureSession

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMediaCaptureSession::QMediaCaptureSession(QObject *parent)
    self._noteCreation(QMediaCaptureSession, lambda: Rituals.call(
        'ritual_ZN20QMediaCaptureSessionC1EP7QObject',
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

  def imageCapture(self) -> Optional[QImageCapture]:
    """
    Calls Qt's 'QImageCapture *QMediaCaptureSession::imageCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#imageCapture

    Returns
    -------

    Optional[QImageCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImageCapture *QMediaCaptureSession::imageCapture()
    address = self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession12imageCaptureEv',
    )
    from . import QImageCapture
    return QImageCapture._cuteAt(address)

  def screenCapture(self) -> Optional[QScreenCapture]:
    """
    Calls Qt's 'QScreenCapture *QMediaCaptureSession::screenCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#screenCapture

    Returns
    -------

    Optional[QScreenCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreenCapture *QMediaCaptureSession::screenCapture()
    address = self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession13screenCaptureEv',
    )
    from . import QScreenCapture
    return QScreenCapture._cuteAt(address)

  def windowCapture(self) -> Optional[QWindowCapture]:
    """
    Calls Qt's 'QWindowCapture *QMediaCaptureSession::windowCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#windowCapture

    Returns
    -------

    Optional[QWindowCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowCapture *QMediaCaptureSession::windowCapture()
    address = self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession13windowCaptureEv',
    )
    from . import QWindowCapture
    return QWindowCapture._cuteAt(address)

  def recorder(self) -> Optional[QMediaRecorder]:
    """
    Calls Qt's 'QMediaRecorder *QMediaCaptureSession::recorder()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediacapturesession.html#recorder

    Returns
    -------

    Optional[QMediaRecorder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaRecorder *QMediaCaptureSession::recorder()
    address = self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession8recorderEv',
    )
    from . import QMediaRecorder
    return QMediaRecorder._cuteAt(address)

  def audioInputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::audioInputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#audioInputChanged
    """
    #  void QMediaCaptureSession::audioInputChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession17audioInputChangedEv',
    )

  def audioBufferInputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::audioBufferInputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#audioBufferInputChanged
    """
    #  void QMediaCaptureSession::audioBufferInputChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession23audioBufferInputChangedEv',
    )

  def cameraChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::cameraChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#cameraChanged
    """
    #  void QMediaCaptureSession::cameraChanged()
    self.uglySide.call('ritual_ZN20QMediaCaptureSession13cameraChangedEv')

  def nativeVideoSourceChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::nativeVideoSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#nativeVideoSourceChanged
    """
    #  void QMediaCaptureSession::nativeVideoSourceChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession24nativeVideoSourceChangedEv',
    )

  def screenCaptureChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::screenCaptureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#screenCaptureChanged
    """
    #  void QMediaCaptureSession::screenCaptureChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession20screenCaptureChangedEv',
    )

  def windowCaptureChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::windowCaptureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#windowCaptureChanged
    """
    #  void QMediaCaptureSession::windowCaptureChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession20windowCaptureChangedEv',
    )

  def videoFrameInputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::videoFrameInputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#videoFrameInputChanged
    """
    #  void QMediaCaptureSession::videoFrameInputChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession22videoFrameInputChangedEv',
    )

  def imageCaptureChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::imageCaptureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#imageCaptureChanged
    """
    #  void QMediaCaptureSession::imageCaptureChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession19imageCaptureChangedEv',
    )

  def recorderChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::recorderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#recorderChanged
    """
    #  void QMediaCaptureSession::recorderChanged()
    self.uglySide.call('ritual_ZN20QMediaCaptureSession15recorderChangedEv')

  def videoOutputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::videoOutputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#videoOutputChanged
    """
    #  void QMediaCaptureSession::videoOutputChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession18videoOutputChangedEv',
    )

  def audioOutputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaCaptureSession::audioOutputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesession.html#audioOutputChanged
    """
    #  void QMediaCaptureSession::audioOutputChanged()
    self.uglySide.call(
        'ritual_ZN20QMediaCaptureSession18audioOutputChangedEv',
    )

  def d_func(self) -> Optional[QMediaCaptureSessionPrivate]:
    """
    Calls Qt's 'QMediaCaptureSessionPrivate *QMediaCaptureSession::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediacapturesession.html#d_func

    Returns
    -------

    Optional[QMediaCaptureSessionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSessionPrivate *QMediaCaptureSession::d_func()
    address = self.uglySide.call('ritual_ZN20QMediaCaptureSession6d_funcEv')
    from . import QMediaCaptureSessionPrivate
    return QMediaCaptureSessionPrivate._cuteAt(address)

  @staticmethod
  def setObject(*__, **_) -> Never:
    """
    Qt's 'QMediaCaptureSession::setObject': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QMediaCaptureSession.setObject' has no cute function yet. Qt's "
        "'QMediaCaptureSession::setObject': a template: a pattern and no "
        "single function.")
