"""
QScreenCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qscreencapture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QScreen
  from . import QMediaCaptureSession, QPlatformSurfaceCapture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMediaCaptureSession = WAIT['QMediaCaptureSession']
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScreenCapture(QObject):
  """
  The cute side of Qt's QScreenCapture: a plain Python object standing in
  front of one C++ QScreenCapture.

  It is built on the cute 'QObject', as Qt's QScreenCapture is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScreenCapture that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'captureSession',
  'setScreen', 'screen', 'isActive', 'error', 'errorString', 'setActive',
  'start', 'stop', 'activeChanged', 'errorChanged', 'screenChanged',
  'errorOccurred', 'maximumFrameRateChanged', 'setCaptureSession',
  'platformScreenCapture'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScreenCapture::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QScreenCapture::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QScreenCapture::~QScreenCapture()': the destructor: Python never
    removes a C++ QScreenCapture.
  - Qt's 'void QScreenCapture::setMaximumFrameRate(std::optional<qreal>
    frameRate)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<qreal> QScreenCapture::maximumFrameRate() const':
    gives a type Python has no way to take yet.
  - Qt's 'QScreenCapturePrivate *QScreenCapture::d_func()': gives
    'QScreenCapturePrivate', which has no cute class yet.
  - Qt's 'const QScreenCapturePrivate *QScreenCapture::d_func() const': gives
    'QScreenCapturePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QScreenCapture is created at the first use, not by
    'QScreenCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScreenCapture.
  - Qt tells when it has removed the C++ QScreenCapture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScreenCapture that has no cute function yet,
    'maximumFrameRate', 'setMaximumFrameRate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QScreenCapture, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QScreenCapture::Error' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    InternalError = Kee[int](1)
    CapturingNotSupported = Kee[int](2)
    CaptureFailed = Kee[int](4)
    NotFound = Kee[int](5)

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
    Calls Qt's 'QString QScreenCapture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#tr

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
    #  QString QScreenCapture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QScreenCapture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScreenCapture'

  #  A C++ QScreenCapture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScreenCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScreenCapture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScreenCapture::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QScreenCapture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QScreenCapture::captureSession()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QScreenCapture::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK14QScreenCapture14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QScreenCapture::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QScreenCapture::screen() const
    address = self.uglySide.call('ritual_ZNK14QScreenCapture6screenEv')
    from ..QtGui import QScreen
    return QScreen._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QScreenCapture::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#isActive
    """
    #  bool QScreenCapture::isActive() const
    return self.uglySide.call('ritual_ZNK14QScreenCapture8isActiveEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QScreenCapture::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QScreenCapture::error() const
    return QScreenCapture.Error(self.uglySide.call(
        'ritual_ZNK14QScreenCapture5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QScreenCapture::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScreenCapture::errorString() const
    return self.uglySide.call('ritual_ZNK14QScreenCapture11errorStringEv')

  def platformScreenCapture(self) -> Optional[QPlatformSurfaceCapture]:
    """
    Calls Qt's 'QPlatformSurfaceCapture
    *QScreenCapture::platformScreenCapture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreencapture.html#platformScreenCapture

    Returns
    -------

    Optional[QPlatformSurfaceCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurfaceCapture *QScreenCapture::platformScreenCapture() const
    address = self.uglySide.call(
        'ritual_ZNK14QScreenCapture21platformScreenCaptureEv',
    )
    from . import QPlatformSurfaceCapture
    return QPlatformSurfaceCapture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QScreenCapture::setScreen(QScreen *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#setScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScreenCapture::setScreen(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN14QScreenCapture9setScreenEP7QScreen',
        self._addressOf(screen),
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QScreenCapture::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QScreenCapture::setActive(bool active)
    self.uglySide.call('ritual_ZN14QScreenCapture9setActiveEb', active)

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      captureSession: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void QScreenCapture::setCaptureSession(QMediaCaptureSession
    *captureSession)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreencapture.html#setCaptureSession

    Parameters
    ----------

    captureSession : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScreenCapture::setCaptureSession(QMediaCaptureSession
    #      *captureSession)
    self.uglySide.call(
        'ritual_ZN14QScreenCapture17setCaptureSessionEP20QMediaCaptureSessi'
        'on',
        self._addressOf(captureSession),
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
    Notes what was given, for Qt's 'QScreenCapture::QScreenCapture(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#QScreenCapture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScreenCapture::QScreenCapture(QObject *parent)
    self._noteCreation(QScreenCapture, lambda: Rituals.call(
        'ritual_ZN14QScreenCaptureC1EP7QObject',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QScreenCapture::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#start
    """
    #  void QScreenCapture::start()
    self.uglySide.call('ritual_ZN14QScreenCapture5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QScreenCapture::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#stop
    """
    #  void QScreenCapture::stop()
    self.uglySide.call('ritual_ZN14QScreenCapture4stopEv')

  @overload(bool)
  def activeChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QScreenCapture::activeChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#activeChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QScreenCapture::activeChanged(bool a0)
    self.uglySide.call('ritual_ZN14QScreenCapture13activeChangedEb', a0)

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QScreenCapture::errorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#errorChanged
    """
    #  void QScreenCapture::errorChanged()
    self.uglySide.call('ritual_ZN14QScreenCapture12errorChangedEv')

  @overload(QScreen)
  @overload(NoneType)
  def screenChanged(self, a0: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QScreenCapture::screenChanged(QScreen *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#screenChanged

    Parameters
    ----------

    a0 : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScreenCapture::screenChanged(QScreen *a0)
    self.uglySide.call(
        'ritual_ZN14QScreenCapture13screenChangedEP7QScreen',
        self._addressOf(a0),
    )

  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QScreenCapture::errorOccurred(QScreenCapture::Error
    error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreencapture.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScreenCapture::errorOccurred(QScreenCapture::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN14QScreenCapture13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )

  def maximumFrameRateChanged(self) -> None:
    """
    Calls Qt's 'void QScreenCapture::maximumFrameRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreencapture.html#maximumFrameRateChanged
    """
    #  void QScreenCapture::maximumFrameRateChanged()
    self.uglySide.call(
        'ritual_ZN14QScreenCapture23maximumFrameRateChangedEv',
    )

  @staticmethod
  def maximumFrameRate(*__, **_) -> Never:
    """
    Qt's 'std::optional<qreal> QScreenCapture::maximumFrameRate() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScreenCapture.maximumFrameRate' has no cute function yet. Qt's "
        "'std::optional<qreal> QScreenCapture::maximumFrameRate() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setMaximumFrameRate(*__, **_) -> Never:
    """
    Qt's 'void QScreenCapture::setMaximumFrameRate(std::optional<qreal>
    frameRate)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScreenCapture.setMaximumFrameRate' has no cute function yet. "
        "Qt's 'void "
        "QScreenCapture::setMaximumFrameRate(std::optional<qreal> "
        "frameRate)': takes a type Python has no way to hand over yet.")
