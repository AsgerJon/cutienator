"""
QWindowCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qwindowcapture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QCapturableWindow, QMediaCaptureSession
  from . import QPlatformSurfaceCapture, QWindowCapturePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCapturableWindow = WAIT['QCapturableWindow']
  QMediaCaptureSession = WAIT['QMediaCaptureSession']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowCapture(QObject):
  """
  The cute side of Qt's QWindowCapture: a plain Python object standing in
  front of one C++ QWindowCapture.

  It is built on the cute 'QObject', as Qt's QWindowCapture is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowCapture that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'capturableWindows',
  'captureSession', 'setWindow', 'window', 'isActive', 'error',
  'errorString', 'setActive', 'start', 'stop', 'activeChanged',
  'windowChanged', 'errorChanged', 'errorOccurred',
  'maximumFrameRateChanged', 'setCaptureSession', 'platformWindowCapture',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWindowCapture::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWindowCapture::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWindowCapture::~QWindowCapture()': the destructor: Python never
    removes a C++ QWindowCapture.
  - Qt's 'void QWindowCapture::setMaximumFrameRate(std::optional<qreal>
    frameRate)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<qreal> QWindowCapture::maximumFrameRate() const':
    gives a type Python has no way to take yet.
  - Qt's 'const QWindowCapturePrivate *QWindowCapture::d_func() const': takes
    in Python what 'QWindowCapturePrivate *QWindowCapture::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 31 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWindowCapture is created at the first use, not by
    'QWindowCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowCapture.
  - Qt tells when it has removed the C++ QWindowCapture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWindowCapture that has no cute function yet,
    'maximumFrameRate', 'setMaximumFrameRate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWindowCapture, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QWindowCapture::Error' of Qt, with the 5 names Qt gives in it.
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
    Calls Qt's 'QString QWindowCapture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#tr

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
    #  QString QWindowCapture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QWindowCapture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def capturableWindows() -> QList[QCapturableWindow]:
    """
    Calls Qt's 'QList<QCapturableWindow>
    QWindowCapture::capturableWindows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcapture.html#capturableWindows

    Returns
    -------

    QList[QCapturableWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCapturableWindow> QWindowCapture::capturableWindows()
    address = Rituals.call('ritual_ZN14QWindowCapture17capturableWindowsEv')
    from . import QCapturableWindow
    return QList[QCapturableWindow]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowCapture'

  #  A C++ QWindowCapture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWindowCapture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWindowCapture::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QWindowCapture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QWindowCapture::captureSession()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QWindowCapture::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK14QWindowCapture14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def window(self) -> QCapturableWindow:
    """
    Calls Qt's 'QCapturableWindow QWindowCapture::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#window

    Returns
    -------

    QCapturableWindow
      A new cute QCapturableWindow around the copy Qt gave back. Python owns
      it.
    """
    #  QCapturableWindow QWindowCapture::window() const
    address = self.uglySide.call('ritual_ZNK14QWindowCapture6windowEv')
    from . import QCapturableWindow
    return QCapturableWindow._cuteOwning(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QWindowCapture::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#isActive
    """
    #  bool QWindowCapture::isActive() const
    return self.uglySide.call('ritual_ZNK14QWindowCapture8isActiveEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QWindowCapture::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QWindowCapture::error() const
    return QWindowCapture.Error(self.uglySide.call(
        'ritual_ZNK14QWindowCapture5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWindowCapture::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWindowCapture::errorString() const
    return self.uglySide.call('ritual_ZNK14QWindowCapture11errorStringEv')

  def platformWindowCapture(self) -> Optional[QPlatformSurfaceCapture]:
    """
    Calls Qt's 'QPlatformSurfaceCapture
    *QWindowCapture::platformWindowCapture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcapture.html#platformWindowCapture

    Returns
    -------

    Optional[QPlatformSurfaceCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurfaceCapture *QWindowCapture::platformWindowCapture() const
    address = self.uglySide.call(
        'ritual_ZNK14QWindowCapture21platformWindowCaptureEv',
    )
    from . import QPlatformSurfaceCapture
    return QPlatformSurfaceCapture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCapturableWindow)
  def setWindow(self, window: QCapturableWindow) -> None:
    """
    Calls Qt's 'void QWindowCapture::setWindow(QCapturableWindow window)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#setWindow

    Parameters
    ----------

    window : QCapturableWindow
      Passed on as a value: Qt reads the C++ QCapturableWindow, which stays
      Python's own.
    """
    #  void QWindowCapture::setWindow(QCapturableWindow window)
    self.uglySide.call(
        'ritual_ZN14QWindowCapture9setWindowE17QCapturableWindow',
        self._valueOf(window),
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QWindowCapture::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QWindowCapture::setActive(bool active)
    self.uglySide.call('ritual_ZN14QWindowCapture9setActiveEb', active)

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      captureSession: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void QWindowCapture::setCaptureSession(QMediaCaptureSession
    *captureSession)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcapture.html#setCaptureSession

    Parameters
    ----------

    captureSession : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowCapture::setCaptureSession(QMediaCaptureSession
    #      *captureSession)
    self.uglySide.call(
        'ritual_ZN14QWindowCapture17setCaptureSessionEP20QMediaCaptureSessi'
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
    Notes what was given, for Qt's 'QWindowCapture::QWindowCapture(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#QWindowCapture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWindowCapture::QWindowCapture(QObject *parent)
    self._noteCreation(QWindowCapture, lambda: Rituals.call(
        'ritual_ZN14QWindowCaptureC1EP7QObject',
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
    Calls Qt's 'void QWindowCapture::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#start
    """
    #  void QWindowCapture::start()
    self.uglySide.call('ritual_ZN14QWindowCapture5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QWindowCapture::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#stop
    """
    #  void QWindowCapture::stop()
    self.uglySide.call('ritual_ZN14QWindowCapture4stopEv')

  @overload(bool)
  def activeChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWindowCapture::activeChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#activeChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWindowCapture::activeChanged(bool a0)
    self.uglySide.call('ritual_ZN14QWindowCapture13activeChangedEb', a0)

  @overload(QCapturableWindow)
  def windowChanged(self, window: QCapturableWindow) -> None:
    """
    Calls Qt's 'void QWindowCapture::windowChanged(QCapturableWindow
    window)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#windowChanged

    Parameters
    ----------

    window : QCapturableWindow
      Passed on as a value: Qt reads the C++ QCapturableWindow, which stays
      Python's own.
    """
    #  void QWindowCapture::windowChanged(QCapturableWindow window)
    self.uglySide.call(
        'ritual_ZN14QWindowCapture13windowChangedE17QCapturableWindow',
        self._valueOf(window),
    )

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QWindowCapture::errorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#errorChanged
    """
    #  void QWindowCapture::errorChanged()
    self.uglySide.call('ritual_ZN14QWindowCapture12errorChangedEv')

  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QWindowCapture::errorOccurred(QWindowCapture::Error
    error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWindowCapture::errorOccurred(QWindowCapture::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN14QWindowCapture13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )

  def maximumFrameRateChanged(self) -> None:
    """
    Calls Qt's 'void QWindowCapture::maximumFrameRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcapture.html#maximumFrameRateChanged
    """
    #  void QWindowCapture::maximumFrameRateChanged()
    self.uglySide.call(
        'ritual_ZN14QWindowCapture23maximumFrameRateChangedEv',
    )

  def d_func(self) -> Optional[QWindowCapturePrivate]:
    """
    Calls Qt's 'QWindowCapturePrivate *QWindowCapture::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcapture.html#d_func

    Returns
    -------

    Optional[QWindowCapturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowCapturePrivate *QWindowCapture::d_func()
    address = self.uglySide.call('ritual_ZN14QWindowCapture6d_funcEv')
    from . import QWindowCapturePrivate
    return QWindowCapturePrivate._cuteAt(address)

  @staticmethod
  def maximumFrameRate(*__, **_) -> Never:
    """
    Qt's 'std::optional<qreal> QWindowCapture::maximumFrameRate() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWindowCapture.maximumFrameRate' has no cute function yet. Qt's "
        "'std::optional<qreal> QWindowCapture::maximumFrameRate() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setMaximumFrameRate(*__, **_) -> Never:
    """
    Qt's 'void QWindowCapture::setMaximumFrameRate(std::optional<qreal>
    frameRate)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWindowCapture.setMaximumFrameRate' has no cute function yet. "
        "Qt's 'void "
        "QWindowCapture::setMaximumFrameRate(std::optional<qreal> "
        "frameRate)': takes a type Python has no way to hand over yet.")
