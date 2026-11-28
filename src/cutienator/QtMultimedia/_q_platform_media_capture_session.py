"""
QPlatformMediaCaptureSession binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediacapture_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformMediaCaptureSession to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QMediaCaptureSession, QPlatformAudioBufferInput
  from . import QPlatformAudioInput, QPlatformAudioOutput
  from . import QPlatformMediaRecorder, QPlatformSurfaceCapture
  from . import QPlatformVideoFrameInput, QVideoSink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMediaCaptureSession = WAIT['QMediaCaptureSession']
  QPlatformAudioBufferInput = WAIT['QPlatformAudioBufferInput']
  QPlatformAudioInput = WAIT['QPlatformAudioInput']
  QPlatformAudioOutput = WAIT['QPlatformAudioOutput']
  QPlatformMediaRecorder = WAIT['QPlatformMediaRecorder']
  QPlatformSurfaceCapture = WAIT['QPlatformSurfaceCapture']
  QPlatformVideoFrameInput = WAIT['QPlatformVideoFrameInput']
  QVideoSink = WAIT['QVideoSink']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformMediaCaptureSession(QObject):
  """
  The cute side of Qt's QPlatformMediaCaptureSession: a plain Python object
  standing in front of one C++ QPlatformMediaCaptureSession.

  It is built on the cute 'QObject', as Qt's QPlatformMediaCaptureSession is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformMediaCaptureSession that has a ritual and
  that Python can call so far, 22 names in all: 'metaObject', 'tr',
  'setCaptureSession', 'captureSession', 'screenCapture', 'setScreenCapture',
  'windowCapture', 'setWindowCapture', 'videoFrameInput',
  'setVideoFrameInput', 'mediaRecorder', 'setMediaRecorder', 'setAudioInput',
  'setAudioBufferInput', 'setVideoPreview', 'setAudioOutput',
  'cameraChanged', 'screenCaptureChanged', 'windowCaptureChanged',
  'videoFrameInputChanged', 'imageCaptureChanged', 'encoderChanged'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformMediaCaptureSession::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QPlatformMediaCaptureSession::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformMediaCaptureSession::~QPlatformMediaCaptureSession()': the
    destructor: Python never removes a C++ QPlatformMediaCaptureSession.
  - Qt's 'QPlatformCamera *QPlatformMediaCaptureSession::camera()': gives
    'QPlatformCamera', which has no cute class yet.
  - Qt's 'void QPlatformMediaCaptureSession::setCamera(QPlatformCamera *a0)':
    names 'QPlatformCamera', which has no cute class yet.
  - Qt's 'QPlatformImageCapture
    *QPlatformMediaCaptureSession::imageCapture()': gives
    'QPlatformImageCapture', which has no cute class yet.
  - Qt's 'void
    QPlatformMediaCaptureSession::setImageCapture(QPlatformImageCapture
    *a0)': names 'QPlatformImageCapture', which has no cute class yet.
  - Qt's 'std::vector<QPlatformVideoSource *>
    QPlatformMediaCaptureSession::activeVideoSources()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformMediaCaptureSession is created at the first use, not by
    'QPlatformMediaCaptureSession(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMediaCaptureSession.
  - Qt tells when it has removed the C++ QPlatformMediaCaptureSession. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformMediaCaptureSession that has no cute function
    yet, 'activeVideoSources', 'camera', 'imageCapture', 'setCamera',
    'setImageCapture', holds a function that raises 'NotImplementedError',
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
    Calls Qt's 'QString QPlatformMediaCaptureSession::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#tr

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
    #  QString QPlatformMediaCaptureSession::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QPlatformMediaCaptureSession2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMediaCaptureSession'

  #  A C++ QPlatformMediaCaptureSession Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformMediaCaptureSession'

  #  The functions Qt calls itself that QPlatformMediaCaptureSession is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'camera': (
          'QPlatformCamera *QPlatformMediaCaptureSession::camera()',
      ),
      'setCamera': (
          'void QPlatformMediaCaptureSession::setCamera(QPlatformCamera *)',
      ),
      'imageCapture': (
          'QPlatformImageCapture '
          '*QPlatformMediaCaptureSession::imageCapture()',
      ),
      'setImageCapture': (
          'void '
          'QPlatformMediaCaptureSession::setImageCapture(QPlatformImageCapt'
          'ure *)',
      ),
  }

  #  The functions Qt calls itself that QPlatformMediaCaptureSession is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'screenCapture': (
          ('_ZN28QPlatformMediaCaptureSession13screenCaptureEv',
           ('address', 'address', 'QtMultimedia:QPlatformSurfaceCapture'),
           ()),
      ),
      'setScreenCapture': (
          ('_ZN28QPlatformMediaCaptureSession16setScreenCaptureEP23QPlatfor'
           'mSurfaceCapture',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtMultimedia:QPlatformSurfaceCapture'),
           )),
      ),
      'windowCapture': (
          ('_ZN28QPlatformMediaCaptureSession13windowCaptureEv',
           ('address', 'address', 'QtMultimedia:QPlatformSurfaceCapture'),
           ()),
      ),
      'setWindowCapture': (
          ('_ZN28QPlatformMediaCaptureSession16setWindowCaptureEP23QPlatfor'
           'mSurfaceCapture',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtMultimedia:QPlatformSurfaceCapture'),
           )),
      ),
      'videoFrameInput': (
          ('_ZN28QPlatformMediaCaptureSession15videoFrameInputEv',
           ('address', 'address', 'QtMultimedia:QPlatformVideoFrameInput'),
           ()),
      ),
      'setVideoFrameInput': (
          ('_ZN28QPlatformMediaCaptureSession18setVideoFrameInputEP24QPlatf'
           'ormVideoFrameInput',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtMultimedia:QPlatformVideoFrameInput'),
           )),
      ),
      'mediaRecorder': (
          ('_ZN28QPlatformMediaCaptureSession13mediaRecorderEv',
           ('address', 'address', 'QtMultimedia:QPlatformMediaRecorder'),
           ()),
      ),
      'setMediaRecorder': (
          ('_ZN28QPlatformMediaCaptureSession16setMediaRecorderEP22QPlatfor'
           'mMediaRecorder',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QPlatformMediaRecorder'),
           )),
      ),
      'setAudioInput': (
          ('_ZN28QPlatformMediaCaptureSession13setAudioInputEP19QPlatformAu'
           'dioInput',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QPlatformAudioInput'),
           )),
      ),
      'setAudioBufferInput': (
          ('_ZN28QPlatformMediaCaptureSession19setAudioBufferInputEP25QPlat'
           'formAudioBufferInput',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtMultimedia:QPlatformAudioBufferInput'),
           )),
      ),
      'setVideoPreview': (
          ('_ZN28QPlatformMediaCaptureSession15setVideoPreviewEP10QVideoSin'
           'k',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QVideoSink'),
           )),
      ),
      'setAudioOutput': (
          ('_ZN28QPlatformMediaCaptureSession14setAudioOutputEP20QPlatformA'
           'udioOutput',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QPlatformAudioOutput'),
           )),
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
    Calls Qt's 'const QMetaObject *QPlatformMediaCaptureSession::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformMediaCaptureSession::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QPlatformMediaCaptureSession10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession
    *QPlatformMediaCaptureSession::captureSession() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QPlatformMediaCaptureSession::captureSession()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QPlatformMediaCaptureSession14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      session: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaCaptureSession::setCaptureSession(QMediaCaptureSession
    *session)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html

    Parameters
    ----------

    session : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setCaptureSession(
    #      QMediaCaptureSession *session)
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession17setCaptureSessionEP20QMed'
        'iaCaptureSession',
        self._addressOf(session),
    )

  @overload(QPlatformSurfaceCapture)
  @overload(NoneType)
  def setScreenCapture(self, a0: Optional[QPlatformSurfaceCapture]) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaCaptureSession::setScreenCapture(QPlatformSurfaceCapture
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#setScreenCapture

    Parameters
    ----------

    a0 : Optional[QPlatformSurfaceCapture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setScreenCapture(
    #      QPlatformSurfaceCapture *a0)
    ritual = (
        'ritual_ZN28QPlatformMediaCaptureSession16setScreenCaptureEP23QPlat'
        'formSurfaceCapture')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession16setScreenCaptureEP2'
          '3QPlatformSurfaceCapture')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformSurfaceCapture)
  @overload(NoneType)
  def setWindowCapture(self, a0: Optional[QPlatformSurfaceCapture]) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaCaptureSession::setWindowCapture(QPlatformSurfaceCapture
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#setWindowCapture

    Parameters
    ----------

    a0 : Optional[QPlatformSurfaceCapture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setWindowCapture(
    #      QPlatformSurfaceCapture *a0)
    ritual = (
        'ritual_ZN28QPlatformMediaCaptureSession16setWindowCaptureEP23QPlat'
        'formSurfaceCapture')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession16setWindowCaptureEP2'
          '3QPlatformSurfaceCapture')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformVideoFrameInput)
  @overload(NoneType)
  def setVideoFrameInput(
      self,
      a0: Optional[QPlatformVideoFrameInput],
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaCaptureSession::setVideoFrameInput(QPlatformVideoFrameInput
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html

    Parameters
    ----------

    a0 : Optional[QPlatformVideoFrameInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setVideoFrameInput(
    #      QPlatformVideoFrameInput *a0)
    ritual = (
        'ritual_ZN28QPlatformMediaCaptureSession18setVideoFrameInputEP24QPl'
        'atformVideoFrameInput')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession18setVideoFrameInputE'
          'P24QPlatformVideoFrameInput')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformMediaRecorder)
  @overload(NoneType)
  def setMediaRecorder(self, a0: Optional[QPlatformMediaRecorder]) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaCaptureSession::setMediaRecorder(QPlatformMediaRecorder
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#setMediaRecorder

    Parameters
    ----------

    a0 : Optional[QPlatformMediaRecorder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setMediaRecorder(
    #      QPlatformMediaRecorder *a0)
    ritual = (
        'ritual_ZN28QPlatformMediaCaptureSession16setMediaRecorderEP22QPlat'
        'formMediaRecorder')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession16setMediaRecorderEP2'
          '2QPlatformMediaRecorder')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformAudioInput)
  @overload(NoneType)
  def setAudioInput(self, input: Optional[QPlatformAudioInput]) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaCaptureSession::setAudioInput(QPlatformAudioInput *input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#setAudioInput

    Parameters
    ----------

    input : Optional[QPlatformAudioInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setAudioInput(QPlatformAudioInput
    #      *input)
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession13setAudioInputEP19QPlatfor'
        'mAudioInput',
        self._addressOf(input),
    )

  @overload(QPlatformAudioBufferInput)
  @overload(NoneType)
  def setAudioBufferInput(
      self,
      a0: Optional[QPlatformAudioBufferInput],
  ) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::setAudioBufferInput(
    QPlatformAudioBufferInput *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html

    Parameters
    ----------

    a0 : Optional[QPlatformAudioBufferInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setAudioBufferInput(
    #      QPlatformAudioBufferInput *a0)
    ritual = (
        'ritual_ZN28QPlatformMediaCaptureSession19setAudioBufferInputEP25QP'
        'latformAudioBufferInput')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession19setAudioBufferInput'
          'EP25QPlatformAudioBufferInput')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QVideoSink)
  @overload(NoneType)
  def setVideoPreview(self, a0: Optional[QVideoSink]) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::setVideoPreview(QVideoSink
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#setVideoPreview

    Parameters
    ----------

    a0 : Optional[QVideoSink]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setVideoPreview(QVideoSink *a0)
    ritual = (
        'ritual_ZN28QPlatformMediaCaptureSession15setVideoPreviewEP10QVideo'
        'Sink')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession15setVideoPreviewEP10'
          'QVideoSink')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformAudioOutput)
  @overload(NoneType)
  def setAudioOutput(self, a0: Optional[QPlatformAudioOutput]) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaCaptureSession::setAudioOutput(QPlatformAudioOutput *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#setAudioOutput

    Parameters
    ----------

    a0 : Optional[QPlatformAudioOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaCaptureSession::setAudioOutput(QPlatformAudioOutput
    #      *a0)
    ritual = (
        'ritual_ZN28QPlatformMediaCaptureSession14setAudioOutputEP20QPlatfo'
        'rmAudioOutput')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession14setAudioOutputEP20Q'
          'PlatformAudioOutput')
    self.uglySide.call(ritual, self._addressOf(a0))

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformMediaCaptureSession::QPlatformMediaCaptureSession()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html
    """
    #  QPlatformMediaCaptureSession::QPlatformMediaCaptureSession()
    self._noteCreation(QPlatformMediaCaptureSession, lambda: Rituals.call(
        'ritual_ZN28QPlatformMediaCaptureSessionC1Ev',
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

  def screenCapture(self) -> Optional[QPlatformSurfaceCapture]:
    """
    Calls Qt's 'QPlatformSurfaceCapture
    *QPlatformMediaCaptureSession::screenCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#screenCapture

    Returns
    -------

    Optional[QPlatformSurfaceCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurfaceCapture *QPlatformMediaCaptureSession::screenCapture()
    ritual = 'ritual_ZN28QPlatformMediaCaptureSession13screenCaptureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QPlatformMediaCaptureSession13screenCaptureEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformSurfaceCapture
    return QPlatformSurfaceCapture._cuteAt(address)

  def windowCapture(self) -> Optional[QPlatformSurfaceCapture]:
    """
    Calls Qt's 'QPlatformSurfaceCapture
    *QPlatformMediaCaptureSession::windowCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#windowCapture

    Returns
    -------

    Optional[QPlatformSurfaceCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurfaceCapture *QPlatformMediaCaptureSession::windowCapture()
    ritual = 'ritual_ZN28QPlatformMediaCaptureSession13windowCaptureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QPlatformMediaCaptureSession13windowCaptureEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformSurfaceCapture
    return QPlatformSurfaceCapture._cuteAt(address)

  def videoFrameInput(self) -> Optional[QPlatformVideoFrameInput]:
    """
    Calls Qt's 'QPlatformVideoFrameInput
    *QPlatformMediaCaptureSession::videoFrameInput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#videoFrameInput

    Returns
    -------

    Optional[QPlatformVideoFrameInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformVideoFrameInput
    #      *QPlatformMediaCaptureSession::videoFrameInput()
    ritual = 'ritual_ZN28QPlatformMediaCaptureSession15videoFrameInputEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QPlatformMediaCaptureSession15videoFrameInputEv')
    address = self.uglySide.call(ritual)
    from . import QPlatformVideoFrameInput
    return QPlatformVideoFrameInput._cuteAt(address)

  def mediaRecorder(self) -> Optional[QPlatformMediaRecorder]:
    """
    Calls Qt's 'QPlatformMediaRecorder
    *QPlatformMediaCaptureSession::mediaRecorder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#mediaRecorder

    Returns
    -------

    Optional[QPlatformMediaRecorder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMediaRecorder *QPlatformMediaCaptureSession::mediaRecorder()
    address = self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession13mediaRecorderEv',
    )
    from . import QPlatformMediaRecorder
    return QPlatformMediaRecorder._cuteAt(address)

  def cameraChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::cameraChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#cameraChanged
    """
    #  void QPlatformMediaCaptureSession::cameraChanged()
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession13cameraChangedEv',
    )

  def screenCaptureChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::screenCaptureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html
    """
    #  void QPlatformMediaCaptureSession::screenCaptureChanged()
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession20screenCaptureChangedEv',
    )

  def windowCaptureChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::windowCaptureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html
    """
    #  void QPlatformMediaCaptureSession::windowCaptureChanged()
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession20windowCaptureChangedEv',
    )

  def videoFrameInputChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::videoFrameInputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html
    """
    #  void QPlatformMediaCaptureSession::videoFrameInputChanged()
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession22videoFrameInputChangedEv',
    )

  def imageCaptureChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::imageCaptureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html
    """
    #  void QPlatformMediaCaptureSession::imageCaptureChanged()
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession19imageCaptureChangedEv',
    )

  def encoderChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaCaptureSession::encoderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediacapturesession.html#encoderChanged
    """
    #  void QPlatformMediaCaptureSession::encoderChanged()
    self.uglySide.call(
        'ritual_ZN28QPlatformMediaCaptureSession14encoderChangedEv',
    )

  @staticmethod
  def activeVideoSources(*__, **_) -> Never:
    """
    Qt's 'std::vector<QPlatformVideoSource *>
    QPlatformMediaCaptureSession::activeVideoSources()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaCaptureSession.activeVideoSources' has no cute "
        "function yet. Qt's 'std::vector<QPlatformVideoSource *> "
        "QPlatformMediaCaptureSession::activeVideoSources()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def camera(*__, **_) -> Never:
    """
    Qt's 'QPlatformCamera *QPlatformMediaCaptureSession::camera()': gives
    'QPlatformCamera', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaCaptureSession.camera' has no cute function yet. "
        "Qt's 'QPlatformCamera *QPlatformMediaCaptureSession::camera()': "
        "gives 'QPlatformCamera', which has no cute class yet.")

  @staticmethod
  def imageCapture(*__, **_) -> Never:
    """
    Qt's 'QPlatformImageCapture
    *QPlatformMediaCaptureSession::imageCapture()': gives
    'QPlatformImageCapture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaCaptureSession.imageCapture' has no cute function "
        "yet. Qt's 'QPlatformImageCapture "
        "*QPlatformMediaCaptureSession::imageCapture()': gives "
        "'QPlatformImageCapture', which has no cute class yet.")

  @staticmethod
  def setCamera(*__, **_) -> Never:
    """
    Qt's 'void QPlatformMediaCaptureSession::setCamera(QPlatformCamera *a0)':
    names 'QPlatformCamera', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaCaptureSession.setCamera' has no cute function yet. "
        "Qt's 'void QPlatformMediaCaptureSession::setCamera(QPlatformCamera "
        "*a0)': names 'QPlatformCamera', which has no cute class yet.")

  @staticmethod
  def setImageCapture(*__, **_) -> Never:
    """
    Qt's 'void
    QPlatformMediaCaptureSession::setImageCapture(QPlatformImageCapture
    *a0)': names 'QPlatformImageCapture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaCaptureSession.setImageCapture' has no cute "
        "function yet. Qt's 'void "
        "QPlatformMediaCaptureSession::setImageCapture(QPlatformImageCapture"
        " *a0)': names 'QPlatformImageCapture', which has no cute class yet."
    )
