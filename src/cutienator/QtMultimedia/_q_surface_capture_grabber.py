"""
QSurfaceCaptureGrabber binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qsurfacecapturegrabber_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSurfaceCaptureGrabber to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QPlatformSurfaceCapture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVideoFrame = WAIT['QVideoFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSurfaceCaptureGrabber(QObject):
  """
  The cute side of Qt's QSurfaceCaptureGrabber: a plain Python object
  standing in front of one C++ QSurfaceCaptureGrabber.

  It is built on the cute 'QObject', as Qt's QSurfaceCaptureGrabber is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSurfaceCaptureGrabber that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'start',
  'stop', 'frameRate', 'frameGrabbed', 'errorUpdated', 'updateError',
  'grabFrame', 'updateTimerInterval', 'initializeGrabbingContext',
  'finalizeGrabbingContext', 'isGrabbingContextInitialized',
  'injectContextToGrabbingThread'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSurfaceCaptureGrabber::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSurfaceCaptureGrabber::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSurfaceCaptureGrabber::~QSurfaceCaptureGrabber()': the destructor:
    Python never removes a C++ QSurfaceCaptureGrabber.
  - Qt's 'void QSurfaceCaptureGrabber::setFrameRate(std::optional<qreal>
    a0)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QSurfaceCaptureGrabber is created at the first use, not by
    'QSurfaceCaptureGrabber(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSurfaceCaptureGrabber.
  - Qt tells when it has removed the C++ QSurfaceCaptureGrabber. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSurfaceCaptureGrabber that has no cute function yet,
    'addFrameCallback', 'setFrameRate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSurfaceCaptureGrabber, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ThreadPolicy(CuteNum):
    """
    The enum 'QSurfaceCaptureGrabber::ThreadPolicy' of Qt, with the 2 names
    Qt gives in it.
    """

    UseCurrentThread = Kee[int](0)
    CreateGrabbingThread = Kee[int](1)

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
    Calls Qt's 'QString QSurfaceCaptureGrabber::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#tr

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
    #  QString QSurfaceCaptureGrabber::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QSurfaceCaptureGrabber2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSurfaceCaptureGrabber'

  #  A C++ QSurfaceCaptureGrabber Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSurfaceCaptureGrabber'

  #  The functions Qt calls itself that QSurfaceCaptureGrabber is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'grabFrame': (
          ('_ZN22QSurfaceCaptureGrabber9grabFrameEv',
           ('address', 'value', 'QtMultimedia:QVideoFrame'),
           ()),
      ),
      'initializeGrabbingContext': (
          ('_ZN22QSurfaceCaptureGrabber25initializeGrabbingContextEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'finalizeGrabbingContext': (
          ('_ZN22QSurfaceCaptureGrabber23finalizeGrabbingContextEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSurfaceCaptureGrabber::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSurfaceCaptureGrabber::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QSurfaceCaptureGrabber10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def frameRate(self) -> float:
    """
    Calls Qt's 'qreal QSurfaceCaptureGrabber::frameRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#frameRate
    """
    #  qreal QSurfaceCaptureGrabber::frameRate() const
    return self.uglySide.call(
        'ritual_ZNK22QSurfaceCaptureGrabber9frameRateEv',
    )

  def isGrabbingContextInitialized(self) -> bool:
    """
    Calls Qt's 'bool QSurfaceCaptureGrabber::isGrabbingContextInitialized()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html
    """
    #  bool QSurfaceCaptureGrabber::isGrabbingContextInitialized() const
    return self.uglySide.call(
        'ritual_ZNK22QSurfaceCaptureGrabber28isGrabbingContextInitializedEv',
    )

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

  @overload()
  @overload(ThreadPolicy)
  def __init__(
      self,
      threadPolicy: ThreadPolicy = ThreadPolicy.CreateGrabbingThread,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSurfaceCaptureGrabber::QSurfaceCaptureGrabber(ThreadPolicy
    threadPolicy)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#QSurfaceCaptureGrabber

    Parameters
    ----------

    threadPolicy : ThreadPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      ThreadPolicy.CreateGrabbingThread.
    """
    #  QSurfaceCaptureGrabber::QSurfaceCaptureGrabber(ThreadPolicy
    #      threadPolicy)
    self._noteCreation(QSurfaceCaptureGrabber, lambda: Rituals.call(
        'ritual_ZN22QSurfaceCaptureGrabberC1ENS_12ThreadPolicyE',
        threadPolicy.value,
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
    Calls Qt's 'void QSurfaceCaptureGrabber::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#start
    """
    #  void QSurfaceCaptureGrabber::start()
    self.uglySide.call('ritual_ZN22QSurfaceCaptureGrabber5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QSurfaceCaptureGrabber::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#stop
    """
    #  void QSurfaceCaptureGrabber::stop()
    self.uglySide.call('ritual_ZN22QSurfaceCaptureGrabber4stopEv')

  @overload(QVideoFrame)
  def frameGrabbed(self, a0: QVideoFrame) -> None:
    """
    Calls Qt's 'void QSurfaceCaptureGrabber::frameGrabbed(const QVideoFrame
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#frameGrabbed

    Parameters
    ----------

    a0 : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QSurfaceCaptureGrabber::frameGrabbed(const QVideoFrame &a0)
    self.uglySide.call(
        'ritual_ZN22QSurfaceCaptureGrabber12frameGrabbedERK11QVideoFrame',
        self._valueOf(a0),
    )

  @overload(QPlatformSurfaceCapture.Error, str)
  def errorUpdated(
      self,
      error: QPlatformSurfaceCapture.Error,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void
    QSurfaceCaptureGrabber::errorUpdated(QPlatformSurfaceCapture::Error
    error, const QString &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#errorUpdated

    Parameters
    ----------

    error : QPlatformSurfaceCapture.Error
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSurfaceCaptureGrabber::errorUpdated(QPlatformSurfaceCapture::
    #      Error error, const QString &description)
    self.uglySide.call(
        'ritual_ZN22QSurfaceCaptureGrabber12errorUpdatedEN23QPlatformSurfac'
        'eCapture5ErrorERK7QString',
        error.value, description,
    )

  @overload(QPlatformSurfaceCapture.Error)
  @overload(QPlatformSurfaceCapture.Error, str)
  def updateError(
      self,
      error: QPlatformSurfaceCapture.Error,
      description: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QSurfaceCaptureGrabber::updateError(QPlatformSurfaceCapture::Error error,
    const QString &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#updateError

    Parameters
    ----------

    error : QPlatformSurfaceCapture.Error
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void
    #      QSurfaceCaptureGrabber::updateError(QPlatformSurfaceCapture::Error
    #      error, const QString &description)
    self.uglySide.call(
        'ritual_ZN22QSurfaceCaptureGrabber11updateErrorEN23QPlatformSurface'
        'Capture5ErrorERK7QString',
        error.value, description,
    )

  def grabFrame(self) -> QVideoFrame:
    """
    Calls Qt's 'QVideoFrame QSurfaceCaptureGrabber::grabFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#grabFrame

    Returns
    -------

    QVideoFrame
      A new cute QVideoFrame around the copy Qt gave back. Python owns it.
    """
    #  QVideoFrame QSurfaceCaptureGrabber::grabFrame()
    address = self.uglySide.call(
        'ritual_ZN22QSurfaceCaptureGrabber9grabFrameEv',
    )
    from . import QVideoFrame
    return QVideoFrame._cuteOwning(address)

  def updateTimerInterval(self) -> None:
    """
    Calls Qt's 'void QSurfaceCaptureGrabber::updateTimerInterval()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html#updateTimerInterval
    """
    #  void QSurfaceCaptureGrabber::updateTimerInterval()
    self.uglySide.call(
        'ritual_ZN22QSurfaceCaptureGrabber19updateTimerIntervalEv',
    )

  def initializeGrabbingContext(self) -> None:
    """
    Calls Qt's 'void QSurfaceCaptureGrabber::initializeGrabbingContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html
    """
    #  void QSurfaceCaptureGrabber::initializeGrabbingContext()
    ritual = 'ritual_ZN22QSurfaceCaptureGrabber25initializeGrabbingContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSurfaceCaptureGrabber25initializeGrabbingContext'
          'Ev')
    self.uglySide.call(ritual)

  def finalizeGrabbingContext(self) -> None:
    """
    Calls Qt's 'void QSurfaceCaptureGrabber::finalizeGrabbingContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html
    """
    #  void QSurfaceCaptureGrabber::finalizeGrabbingContext()
    ritual = 'ritual_ZN22QSurfaceCaptureGrabber23finalizeGrabbingContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSurfaceCaptureGrabber23finalizeGrabbingContextEv')
    self.uglySide.call(ritual)

  @overload(QObject)
  @overload(NoneType)
  def injectContextToGrabbingThread(
      self,
      context: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QSurfaceCaptureGrabber::injectContextToGrabbingThread(QObject *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacecapturegrabber.html

    Parameters
    ----------

    context : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurfaceCaptureGrabber::injectContextToGrabbingThread(QObject
    #      *context)
    self.uglySide.call(
        'ritual_ZN22QSurfaceCaptureGrabber29injectContextToGrabbingThreadEP'
        '7QObject',
        self._addressOf(context, 'QObject'),
    )

  @staticmethod
  def addFrameCallback(*__, **_) -> Never:
    """
    Qt's 'QSurfaceCaptureGrabber::addFrameCallback': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QSurfaceCaptureGrabber.addFrameCallback' has no cute function "
        "yet. Qt's 'QSurfaceCaptureGrabber::addFrameCallback': a template: "
        "a pattern and no single function.")

  @staticmethod
  def setFrameRate(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceCaptureGrabber::setFrameRate(std::optional<qreal>
    a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceCaptureGrabber.setFrameRate' has no cute function yet. "
        "Qt's 'void "
        "QSurfaceCaptureGrabber::setFrameRate(std::optional<qreal> a0)': "
        "takes a type Python has no way to hand over yet.")
