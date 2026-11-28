"""
QMovie binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qmovie.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QImageReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject, QRect, QSize
  from . import QColor, QImage, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QIODevice = WAIT['QIODevice']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMovie(QObject):
  """
  The cute side of Qt's QMovie: a plain Python object standing in front of
  one C++ QMovie.

  It is built on the cute 'QObject', as Qt's QMovie is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMovie that has a ritual and that Python can call so
  far, 40 names in all: 'metaObject', 'tr', 'supportedFormats', 'setDevice',
  'device', 'setFileName', 'fileName', 'setFormat', 'format',
  'setBackgroundColor', 'backgroundColor', 'state', 'frameRect',
  'currentImage', 'currentPixmap', 'isValid', 'lastError', 'lastErrorString',
  'jumpToFrame', 'loopCount', 'frameCount', 'nextFrameDelay',
  'currentFrameNumber', 'speed', 'scaledSize', 'setScaledSize', 'cacheMode',
  'setCacheMode', 'started', 'resized', 'updated', 'stateChanged', 'error',
  'finished', 'frameChanged', 'start', 'jumpToNextFrame', 'setPaused',
  'stop', 'setSpeed'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMovie::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QMovie::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QMoviePrivate *QMovie::d_func()': gives 'QMoviePrivate', which has
    no cute class yet.
  - Qt's 'const QMoviePrivate *QMovie::d_func() const': gives
    'QMoviePrivate', which has no cute class yet.
  - Qt's 'QMovie::~QMovie()': the destructor: Python never removes a C++
    QMovie.
  - Qt's 'QBindable<int> QMovie::bindableSpeed()': gives a type Python has no
    way to take yet.
  - Qt's 'QBindable<CacheMode> QMovie::bindableCacheMode()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 54 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMovie is created at the first use, not by 'QMovie(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMovie.
  - Qt tells when it has removed the C++ QMovie. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QMovie that has no cute function yet,
    'bindableCacheMode', 'bindableSpeed', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMovie, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class CacheMode(CuteNum):
    """
    The enum 'QMovie::CacheMode' of Qt, with the 2 names Qt gives in it.
    """

    CacheNone = Kee[int](0)
    CacheAll = Kee[int](1)

  class MovieState(CuteNum):
    """
    The enum 'QMovie::MovieState' of Qt, with the 3 names Qt gives in it.
    """

    NotRunning = Kee[int](0)
    Paused = Kee[int](1)
    Running = Kee[int](2)

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
    Calls Qt's 'QString QMovie::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#tr

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
    #  QString QMovie::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QMovie2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def supportedFormats() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QMovie::supportedFormats()'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#supportedFormats

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QMovie::supportedFormats()
    address = Rituals.call('ritual_ZN6QMovie16supportedFormatsEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMovie'

  #  A C++ QMovie Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMovie'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMovie::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMovie::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QMovie10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QMovie::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QMovie::device() const
    address = self.uglySide.call('ritual_ZNK6QMovie6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QMovie::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMovie::fileName() const
    return self.uglySide.call('ritual_ZNK6QMovie8fileNameEv')

  def format(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMovie::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#format

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMovie::format() const
    address = self.uglySide.call('ritual_ZNK6QMovie6formatEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QMovie::backgroundColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QMovie::backgroundColor() const
    address = self.uglySide.call('ritual_ZNK6QMovie15backgroundColorEv')
    from . import QColor
    return QColor._cuteOwning(address)

  def state(self) -> MovieState:
    """
    Calls Qt's 'MovieState QMovie::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#state

    Returns
    -------

    MovieState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MovieState(number)'
      gives.
    """
    #  MovieState QMovie::state() const
    return QMovie.MovieState(self.uglySide.call('ritual_ZNK6QMovie5stateEv'))

  def frameRect(self) -> QRect:
    """
    Calls Qt's 'QRect QMovie::frameRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#frameRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMovie::frameRect() const
    address = self.uglySide.call('ritual_ZNK6QMovie9frameRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def currentImage(self) -> QImage:
    """
    Calls Qt's 'QImage QMovie::currentImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#currentImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QMovie::currentImage() const
    address = self.uglySide.call('ritual_ZNK6QMovie12currentImageEv')
    from . import QImage
    return QImage._cuteOwning(address)

  def currentPixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QMovie::currentPixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#currentPixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QMovie::currentPixmap() const
    address = self.uglySide.call('ritual_ZNK6QMovie13currentPixmapEv')
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMovie::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#isValid
    """
    #  bool QMovie::isValid() const
    return self.uglySide.call('ritual_ZNK6QMovie7isValidEv')

  def lastError(self) -> QImageReader.ImageReaderError:
    """
    Calls Qt's 'QImageReader::ImageReaderError QMovie::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#lastError

    Returns
    -------

    QImageReader.ImageReaderError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QImageReader.ImageReaderError(number)' gives.
    """
    #  QImageReader::ImageReaderError QMovie::lastError() const
    return QImageReader.ImageReaderError(self.uglySide.call(
        'ritual_ZNK6QMovie9lastErrorEv',
    ))

  def lastErrorString(self) -> str:
    """
    Calls Qt's 'QString QMovie::lastErrorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#lastErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMovie::lastErrorString() const
    return self.uglySide.call('ritual_ZNK6QMovie15lastErrorStringEv')

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QMovie::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#loopCount
    """
    #  int QMovie::loopCount() const
    return self.uglySide.call('ritual_ZNK6QMovie9loopCountEv')

  def frameCount(self) -> int:
    """
    Calls Qt's 'int QMovie::frameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#frameCount
    """
    #  int QMovie::frameCount() const
    return self.uglySide.call('ritual_ZNK6QMovie10frameCountEv')

  def nextFrameDelay(self) -> int:
    """
    Calls Qt's 'int QMovie::nextFrameDelay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#nextFrameDelay
    """
    #  int QMovie::nextFrameDelay() const
    return self.uglySide.call('ritual_ZNK6QMovie14nextFrameDelayEv')

  def currentFrameNumber(self) -> int:
    """
    Calls Qt's 'int QMovie::currentFrameNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#currentFrameNumber
    """
    #  int QMovie::currentFrameNumber() const
    return self.uglySide.call('ritual_ZNK6QMovie18currentFrameNumberEv')

  def speed(self) -> int:
    """
    Calls Qt's 'int QMovie::speed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#speed
    """
    #  int QMovie::speed() const
    return self.uglySide.call('ritual_ZNK6QMovie5speedEv')

  def cacheMode(self) -> CacheMode:
    """
    Calls Qt's 'CacheMode QMovie::cacheMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#cacheMode

    Returns
    -------

    CacheMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CacheMode(number)' gives.
    """
    #  CacheMode QMovie::cacheMode() const
    return QMovie.CacheMode(self.uglySide.call(
        'ritual_ZNK6QMovie9cacheModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QMovie::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMovie::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN6QMovie9setDeviceEP9QIODevice', self._addressOf(device),
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QMovie::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMovie::setFileName(const QString &fileName)
    self.uglySide.call('ritual_ZN6QMovie11setFileNameERK7QString', fileName)

  @overload(QByteArray)
  def setFormat(self, format: QByteArray) -> None:
    """
    Calls Qt's 'void QMovie::setFormat(const QByteArray &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setFormat

    Parameters
    ----------

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMovie::setFormat(const QByteArray &format)
    self.uglySide.call(
        'ritual_ZN6QMovie9setFormatERK10QByteArray', self._valueOf(format),
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QMovie::setBackgroundColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QMovie::setBackgroundColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN6QMovie18setBackgroundColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QSize)
  def setScaledSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QMovie::setScaledSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setScaledSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QMovie::setScaledSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN6QMovie13setScaledSizeERK5QSize', self._valueOf(size),
    )

  @overload(CacheMode)
  def setCacheMode(self, mode: CacheMode) -> None:
    """
    Calls Qt's 'void QMovie::setCacheMode(CacheMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setCacheMode

    Parameters
    ----------

    mode : CacheMode
      Passed on as its number.
    """
    #  void QMovie::setCacheMode(CacheMode mode)
    self.uglySide.call(
        'ritual_ZN6QMovie12setCacheModeENS_9CacheModeE', mode.value,
    )

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QMovie::setPaused(bool paused)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QMovie::setPaused(bool paused)
    self.uglySide.call('ritual_ZN6QMovie9setPausedEb', paused)

  @overload(int)
  def setSpeed(self, percentSpeed: int) -> None:
    """
    Calls Qt's 'void QMovie::setSpeed(int percentSpeed)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#setSpeed

    Parameters
    ----------

    percentSpeed : int
      Passed on as it is.
    """
    #  void QMovie::setSpeed(int percentSpeed)
    self.uglySide.call('ritual_ZN6QMovie8setSpeedEi', percentSpeed)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  @overload(QIODevice, QByteArray, QObject)
  @overload(QIODevice, QByteArray, NoneType)
  @overload(NoneType, QByteArray, QObject)
  @overload(NoneType, QByteArray, NoneType)
  def __init__(
      self,
      device: Optional[QIODevice],
      format: Optional[QByteArray] = None,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QMovie::QMovie(QIODevice *device, const
    QByteArray &format, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#QMovie

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMovie::QMovie(QIODevice *device, const QByteArray &format, QObject
    #      *parent)
    if format is None:
      from ..QtCore import QByteArray
      format = QByteArray()
    self._noteCreation(QMovie, lambda: Rituals.call(
        'ritual_ZN6QMovieC1EP9QIODeviceRK10QByteArrayP7QObject',
        self._addressOf(device), self._valueOf(format),
        self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QMovie::QMovie(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#QMovie

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMovie::QMovie(QObject *parent)
    self._noteCreation(QMovie, lambda: Rituals.call(
        'ritual_ZN6QMovieC1EP7QObject', self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QByteArray)
  @overload(str, QByteArray, QObject)
  @overload(str, QByteArray, NoneType)
  def __init__(
      self,
      fileName: str,
      format: Optional[QByteArray] = None,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QMovie::QMovie(const QString &fileName,
    const QByteArray &format, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#QMovie

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMovie::QMovie(const QString &fileName, const QByteArray &format,
    #      QObject *parent)
    if format is None:
      from ..QtCore import QByteArray
      format = QByteArray()
    self._noteCreation(QMovie, lambda: Rituals.call(
        'ritual_ZN6QMovieC1ERK7QStringRK10QByteArrayP7QObject',
        fileName, self._valueOf(format), self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def jumpToFrame(self, frameNumber: int) -> bool:
    """
    Calls Qt's 'bool QMovie::jumpToFrame(int frameNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#jumpToFrame

    Parameters
    ----------

    frameNumber : int
      Passed on as it is.
    """
    #  bool QMovie::jumpToFrame(int frameNumber)
    return self.uglySide.call('ritual_ZN6QMovie11jumpToFrameEi', frameNumber)

  def scaledSize(self) -> QSize:
    """
    Calls Qt's 'QSize QMovie::scaledSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#scaledSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMovie::scaledSize()
    address = self.uglySide.call('ritual_ZN6QMovie10scaledSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def started(self) -> None:
    """
    Calls Qt's 'void QMovie::started()'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#started
    """
    #  void QMovie::started()
    self.uglySide.call('ritual_ZN6QMovie7startedEv')

  @overload(QSize)
  def resized(self, size: QSize) -> None:
    """
    Calls Qt's 'void QMovie::resized(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#resized

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QMovie::resized(const QSize &size)
    self.uglySide.call(
        'ritual_ZN6QMovie7resizedERK5QSize', self._valueOf(size),
    )

  @overload(QRect)
  def updated(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QMovie::updated(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#updated

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QMovie::updated(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN6QMovie7updatedERK5QRect', self._valueOf(rect),
    )

  @overload(MovieState)
  def stateChanged(self, state: MovieState) -> None:
    """
    Calls Qt's 'void QMovie::stateChanged(QMovie::MovieState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#stateChanged

    Parameters
    ----------

    state : MovieState
      Passed on as its number.
    """
    #  void QMovie::stateChanged(QMovie::MovieState state)
    self.uglySide.call(
        'ritual_ZN6QMovie12stateChangedENS_10MovieStateE', state.value,
    )

  @overload(QImageReader.ImageReaderError)
  def error(self, error: QImageReader.ImageReaderError) -> None:
    """
    Calls Qt's 'void QMovie::error(QImageReader::ImageReaderError error)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#error

    Parameters
    ----------

    error : QImageReader.ImageReaderError
      Passed on as its number.
    """
    #  void QMovie::error(QImageReader::ImageReaderError error)
    self.uglySide.call(
        'ritual_ZN6QMovie5errorEN12QImageReader16ImageReaderErrorE',
        error.value,
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QMovie::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#finished
    """
    #  void QMovie::finished()
    self.uglySide.call('ritual_ZN6QMovie8finishedEv')

  @overload(int)
  def frameChanged(self, frameNumber: int) -> None:
    """
    Calls Qt's 'void QMovie::frameChanged(int frameNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#frameChanged

    Parameters
    ----------

    frameNumber : int
      Passed on as it is.
    """
    #  void QMovie::frameChanged(int frameNumber)
    self.uglySide.call('ritual_ZN6QMovie12frameChangedEi', frameNumber)

  def start(self) -> None:
    """
    Calls Qt's 'void QMovie::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#start
    """
    #  void QMovie::start()
    self.uglySide.call('ritual_ZN6QMovie5startEv')

  def jumpToNextFrame(self) -> bool:
    """
    Calls Qt's 'bool QMovie::jumpToNextFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#jumpToNextFrame
    """
    #  bool QMovie::jumpToNextFrame()
    return self.uglySide.call('ritual_ZN6QMovie15jumpToNextFrameEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QMovie::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qmovie.html#stop
    """
    #  void QMovie::stop()
    self.uglySide.call('ritual_ZN6QMovie4stopEv')

  @staticmethod
  def bindableCacheMode(*__, **_) -> Never:
    """
    Qt's 'QBindable<CacheMode> QMovie::bindableCacheMode()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMovie.bindableCacheMode' has no cute function yet. Qt's "
        "'QBindable<CacheMode> QMovie::bindableCacheMode()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableSpeed(*__, **_) -> Never:
    """
    Qt's 'QBindable<int> QMovie::bindableSpeed()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QMovie.bindableSpeed' has no cute function yet. Qt's "
        "'QBindable<int> QMovie::bindableSpeed()': gives a type Python has "
        "no way to take yet.")
