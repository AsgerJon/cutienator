"""
QQuickPixmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPixmap to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickImageProviderOptions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QObject, QRect, QSize, QUrl
  from ..QtGui import QColorSpace, QImage
  from ..QtQml import QQmlEngine
  from . import QQuickTextureFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QImage = WAIT['QImage']
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPixmap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickPixmap: a plain Python object standing in front
  of one C++ QQuickPixmap.

  What exists
  -----------

  Every function of Qt's QQuickPixmap that has a ritual and that Python can
  call so far, 28 names in all: 'tr', 'isNull', 'isReady', 'isError',
  'isLoading', 'status', 'error', 'url', 'implicitSize', 'requestRegion',
  'requestSize', 'autoTransform', 'frameCount', 'image', 'setImage',
  'colorSpace', 'textureFactory', 'rect', 'width', 'height', 'load',
  'loadImageFromDevice', 'clear', 'connectFinished',
  'connectDownloadProgress', 'purgeCache', 'isCached',
  'isScalableImageFormat'. It can be made from Python, in 5 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickPixmap::~QQuickPixmap()': the destructor: Python never
    removes a C++ QQuickPixmap.
  - Qt's 'void QQuickPixmap::setPixmap(const QQuickPixmap &other)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 44 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPixmap is created at the first use, not by
    'QQuickPixmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPixmap.
  - Each name of Qt's QQuickPixmap that has no cute function yet,
    'setPixmap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuickPixmap, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Option(CuteFlags):
    """
    The flags enum 'QQuickPixmap::Option' of Qt, with the 2 names Qt gives in
    it. Qt names the type of its combinations 'QQuickPixmap::Options'.
    """

    Asynchronous = 0x1
    Cache = 0x2

  Options = Option

  class Status(CuteNum):
    """
    The enum 'QQuickPixmap::Status' of Qt, with the 4 names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Error = Kee[int](2)
    Loading = Kee[int](3)

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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QQuickPixmap::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPixmap::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN12QQuickPixmap2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  def purgeCache() -> None:
    """
    Calls Qt's 'void QQuickPixmap::purgeCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#purgeCache
    """
    #  void QQuickPixmap::purgeCache()
    Rituals.call('ritual_ZN12QQuickPixmap10purgeCacheEv')

  @staticmethod
  @overload(QUrl, QRect, QSize, int, QQuickImageProviderOptions)
  def isCached(
      url: QUrl,
      requestRegion: QRect,
      requestSize: QSize,
      frame: int,
      options: QQuickImageProviderOptions,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::isCached(const QUrl &url, const QRect
    &requestRegion, const QSize &requestSize, const int frame, const
    QQuickImageProviderOptions &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#isCached

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    requestRegion : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    requestSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    frame : int
      Passed on as it is.

    options : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.
    """
    #  bool QQuickPixmap::isCached(const QUrl &url, const QRect
    #      &requestRegion, const QSize &requestSize, const int frame, const
    #      QQuickImageProviderOptions &options)
    return Rituals.call(
        'ritual_ZN12QQuickPixmap8isCachedERK4QUrlRK5QRectRK5QSizeiRK26QQuic'
        'kImageProviderOptions',
        CuteMixin._valueOf(url), CuteMixin._valueOf(requestRegion),
        CuteMixin._valueOf(requestSize), frame, CuteMixin._valueOf(options),
    )

  @staticmethod
  @overload(QUrl)
  def isScalableImageFormat(url: QUrl) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::isScalableImageFormat(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpixmap.html#isScalableImageFormat

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQuickPixmap::isScalableImageFormat(const QUrl &url)
    return Rituals.call(
        'ritual_ZN12QQuickPixmap21isScalableImageFormatERK4QUrl',
        CuteMixin._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPixmap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#isNull
    """
    #  bool QQuickPixmap::isNull() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap6isNullEv')

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#isReady
    """
    #  bool QQuickPixmap::isReady() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap7isReadyEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#isError
    """
    #  bool QQuickPixmap::isError() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap7isErrorEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#isLoading
    """
    #  bool QQuickPixmap::isLoading() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap9isLoadingEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickPixmap::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickPixmap::status() const
    return QQuickPixmap.Status(self.uglySide.call(
        'ritual_ZNK12QQuickPixmap6statusEv',
    ))

  def error(self) -> str:
    """
    Calls Qt's 'QString QQuickPixmap::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#error

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPixmap::error() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap5errorEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'const QUrl &QQuickPixmap::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  const QUrl &QQuickPixmap::url() const
    address = self.uglySide.call('ritual_ZNK12QQuickPixmap3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def implicitSize(self) -> QSize:
    """
    Calls Qt's 'const QSize &QQuickPixmap::implicitSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#implicitSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  const QSize &QQuickPixmap::implicitSize() const
    address = self.uglySide.call('ritual_ZNK12QQuickPixmap12implicitSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def requestRegion(self) -> QRect:
    """
    Calls Qt's 'const QRect &QQuickPixmap::requestRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#requestRegion

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  const QRect &QQuickPixmap::requestRegion() const
    address = self.uglySide.call('ritual_ZNK12QQuickPixmap13requestRegionEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def requestSize(self) -> QSize:
    """
    Calls Qt's 'const QSize &QQuickPixmap::requestSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#requestSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  const QSize &QQuickPixmap::requestSize() const
    address = self.uglySide.call('ritual_ZNK12QQuickPixmap11requestSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def autoTransform(self) -> QQuickImageProviderOptions.AutoTransform:
    """
    Calls Qt's 'QQuickImageProviderOptions::AutoTransform
    QQuickPixmap::autoTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#autoTransform

    Returns
    -------

    QQuickImageProviderOptions.AutoTransform
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickImageProviderOptions.AutoTransform(number)' gives.
    """
    #  QQuickImageProviderOptions::AutoTransform
    #      QQuickPixmap::autoTransform() const
    return QQuickImageProviderOptions.AutoTransform(self.uglySide.call(
        'ritual_ZNK12QQuickPixmap13autoTransformEv',
    ))

  def frameCount(self) -> int:
    """
    Calls Qt's 'int QQuickPixmap::frameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#frameCount
    """
    #  int QQuickPixmap::frameCount() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap10frameCountEv')

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickPixmap::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickPixmap::image() const
    address = self.uglySide.call('ritual_ZNK12QQuickPixmap5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def colorSpace(self) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QQuickPixmap::colorSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#colorSpace

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QQuickPixmap::colorSpace() const
    address = self.uglySide.call('ritual_ZNK12QQuickPixmap10colorSpaceEv')
    from ..QtGui import QColorSpace
    return QColorSpace._cuteOwning(address)

  def textureFactory(self) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory *QQuickPixmap::textureFactory() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#textureFactory

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory *QQuickPixmap::textureFactory() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickPixmap14textureFactoryEv',
    )
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QQuickPixmap::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickPixmap::rect() const
    address = self.uglySide.call('ritual_ZNK12QQuickPixmap4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QQuickPixmap::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#width
    """
    #  int QQuickPixmap::width() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QQuickPixmap::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#height
    """
    #  int QQuickPixmap::height() const
    return self.uglySide.call('ritual_ZNK12QQuickPixmap6heightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QImage)
  def setImage(self, a0: QImage) -> None:
    """
    Calls Qt's 'void QQuickPixmap::setImage(const QImage &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#setImage

    Parameters
    ----------

    a0 : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QQuickPixmap::setImage(const QImage &a0)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap8setImageERK6QImage', self._valueOf(a0),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQuickPixmap::QQuickPixmap()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#QQuickPixmap
    """
    #  QQuickPixmap::QQuickPixmap()
    self._noteCreation(QQuickPixmap, lambda: Rituals.call(
        'ritual_ZN12QQuickPixmapC1Ev',
    ))

  @overload(QQmlEngine, QUrl)
  @overload(NoneType, QUrl)
  def __init__(self, a0: Optional[QQmlEngine], a1: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QQuickPixmap::QQuickPixmap(QQmlEngine
    *a0, const QUrl &a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#QQuickPixmap

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QQuickPixmap::QQuickPixmap(QQmlEngine *a0, const QUrl &a1)
    self._noteCreation(QQuickPixmap, lambda: Rituals.call(
        'ritual_ZN12QQuickPixmapC1EP10QQmlEngineRK4QUrl',
        self._addressOf(a0), self._valueOf(a1),
    ))

  @overload(QQmlEngine, QUrl, Options)
  @overload(NoneType, QUrl, Options)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      a1: QUrl,
      options: Options,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickPixmap::QQuickPixmap(QQmlEngine
    *a0, const QUrl &a1, Options options)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#QQuickPixmap

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    options : Options
      Passed on as its number.
    """
    #  QQuickPixmap::QQuickPixmap(QQmlEngine *a0, const QUrl &a1, Options
    #      options)
    self._noteCreation(QQuickPixmap, lambda: Rituals.call(
        'ritual_ZN12QQuickPixmapC1EP10QQmlEngineRK4QUrl6QFlagsINS_6OptionEE',
        self._addressOf(a0), self._valueOf(a1), options.value,
    ))

  @overload(QQmlEngine, QUrl, QRect, QSize)
  @overload(NoneType, QUrl, QRect, QSize)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      a1: QUrl,
      region: QRect,
      a3: QSize,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickPixmap::QQuickPixmap(QQmlEngine
    *a0, const QUrl &a1, const QRect &region, const QSize &a3)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#QQuickPixmap

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    region : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    a3 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QQuickPixmap::QQuickPixmap(QQmlEngine *a0, const QUrl &a1, const QRect
    #      &region, const QSize &a3)
    self._noteCreation(QQuickPixmap, lambda: Rituals.call(
        'ritual_ZN12QQuickPixmapC1EP10QQmlEngineRK4QUrlRK5QRectRK5QSize',
        self._addressOf(a0), self._valueOf(a1), self._valueOf(region),
        self._valueOf(a3),
    ))

  @overload(QUrl, QImage)
  def __init__(self, a0: QUrl, image: QImage) -> None:
    """
    Notes what was given, for Qt's 'QQuickPixmap::QQuickPixmap(const QUrl
    &a0, const QImage &image)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#QQuickPixmap

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  QQuickPixmap::QQuickPixmap(const QUrl &a0, const QImage &image)
    self._noteCreation(QQuickPixmap, lambda: Rituals.call(
        'ritual_ZN12QQuickPixmapC1ERK4QUrlRK6QImage',
        self._valueOf(a0), self._valueOf(image),
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

  @overload(QQmlEngine, QUrl)
  @overload(NoneType, QUrl)
  def load(self, a0: Optional[QQmlEngine], a1: QUrl) -> None:
    """
    Calls Qt's 'void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#load

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrl',
        self._addressOf(a0), self._valueOf(a1),
    )

  @overload(QQmlEngine, QUrl, Options)
  @overload(NoneType, QUrl, Options)
  def load(
      self,
      a0: Optional[QQmlEngine],
      a1: QUrl,
      options: Options,
  ) -> None:
    """
    Calls Qt's 'void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1,
    QQuickPixmap::Options options)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#load

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    options : Options
      Passed on as its number.
    """
    #  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1,
    #      QQuickPixmap::Options options)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrl6QFlagsINS_6Optio'
        'nEE',
        self._addressOf(a0), self._valueOf(a1), options.value,
    )

  @overload(QQmlEngine, QUrl, QRect, QSize)
  @overload(NoneType, QUrl, QRect, QSize)
  def load(
      self,
      a0: Optional[QQmlEngine],
      a1: QUrl,
      requestRegion: QRect,
      requestSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const
    QRect &requestRegion, const QSize &requestSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#load

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    requestRegion : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    requestSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const QRect
    #      &requestRegion, const QSize &requestSize)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrlRK5QRectRK5QSize',
        self._addressOf(a0), self._valueOf(a1), self._valueOf(requestRegion),
        self._valueOf(requestSize),
    )

  @overload(QQmlEngine, QUrl, QRect, QSize, Options)
  @overload(NoneType, QUrl, QRect, QSize, Options)
  def load(
      self,
      a0: Optional[QQmlEngine],
      a1: QUrl,
      requestRegion: QRect,
      requestSize: QSize,
      options: Options,
  ) -> None:
    """
    Calls Qt's 'void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const
    QRect &requestRegion, const QSize &requestSize, QQuickPixmap::Options
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#load

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    requestRegion : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    requestSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : Options
      Passed on as its number.
    """
    #  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const QRect
    #      &requestRegion, const QSize &requestSize, QQuickPixmap::Options
    #      options)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrlRK5QRectRK5QSize6'
        'QFlagsINS_6OptionEE',
        self._addressOf(a0), self._valueOf(a1), self._valueOf(requestRegion),
        self._valueOf(requestSize), options.value,
    )

  @overload(
      QQmlEngine, QUrl, QRect, QSize, Options, QQuickImageProviderOptions,
  )
  @overload(
      NoneType, QUrl, QRect, QSize, Options, QQuickImageProviderOptions,
  )
  @overload(
      QQmlEngine, QUrl, QRect, QSize, Options, QQuickImageProviderOptions,
      int,
  )
  @overload(
      NoneType, QUrl, QRect, QSize, Options, QQuickImageProviderOptions, int,
  )
  @overload(
      QQmlEngine, QUrl, QRect, QSize, Options, QQuickImageProviderOptions,
      int, int,
  )
  @overload(
      NoneType, QUrl, QRect, QSize, Options, QQuickImageProviderOptions, int,
      int,
  )
  @overload(
      QQmlEngine, QUrl, QRect, QSize, Options, QQuickImageProviderOptions,
      int, int, float,
  )
  @overload(
      NoneType, QUrl, QRect, QSize, Options, QQuickImageProviderOptions, int,
      int, float,
  )
  def load(
      self,
      a0: Optional[QQmlEngine],
      a1: QUrl,
      requestRegion: QRect,
      requestSize: QSize,
      options: Options,
      providerOptions: QQuickImageProviderOptions,
      frame: int = 0,
      frameCount: int = 1,
      devicePixelRatio: float = 1.0,
  ) -> None:
    """
    Calls Qt's 'void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const
    QRect &requestRegion, const QSize &requestSize, QQuickPixmap::Options
    options, const QQuickImageProviderOptions &providerOptions, int frame,
    int frameCount, qreal devicePixelRatio)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#load

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    requestRegion : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    requestSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : Options
      Passed on as its number.

    providerOptions : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    frame : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    frameCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    devicePixelRatio : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const QRect
    #      &requestRegion, const QSize &requestSize, QQuickPixmap::Options
    #      options, const QQuickImageProviderOptions &providerOptions, int
    #      frame, int frameCount, qreal devicePixelRatio)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrlRK5QRectRK5QSize6'
        'QFlagsINS_6OptionEERK26QQuickImageProviderOptionsiid',
        self._addressOf(a0), self._valueOf(a1), self._valueOf(requestRegion),
        self._valueOf(requestSize), options.value,
        self._valueOf(providerOptions), frame, frameCount, devicePixelRatio,
    )

  @overload(
      QQmlEngine, QIODevice, QUrl, QRect, QSize, QQuickImageProviderOptions,
  )
  @overload(
      QQmlEngine, NoneType, QUrl, QRect, QSize, QQuickImageProviderOptions,
  )
  @overload(
      NoneType, QIODevice, QUrl, QRect, QSize, QQuickImageProviderOptions,
  )
  @overload(
      NoneType, NoneType, QUrl, QRect, QSize, QQuickImageProviderOptions,
  )
  @overload(
      QQmlEngine, QIODevice, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int,
  )
  @overload(
      QQmlEngine, NoneType, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int,
  )
  @overload(
      NoneType, QIODevice, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int,
  )
  @overload(
      NoneType, NoneType, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int,
  )
  @overload(
      QQmlEngine, QIODevice, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int, int,
  )
  @overload(
      QQmlEngine, NoneType, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int, int,
  )
  @overload(
      NoneType, QIODevice, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int, int,
  )
  @overload(
      NoneType, NoneType, QUrl, QRect, QSize, QQuickImageProviderOptions,
      int, int,
  )
  def loadImageFromDevice(
      self,
      engine: Optional[QQmlEngine],
      device: Optional[QIODevice],
      url: QUrl,
      requestRegion: QRect,
      requestSize: QSize,
      providerOptions: QQuickImageProviderOptions,
      frame: int = 0,
      frameCount: int = 1,
  ) -> None:
    """
    Calls Qt's 'void QQuickPixmap::loadImageFromDevice(QQmlEngine *engine,
    QIODevice *device, const QUrl &url, const QRect &requestRegion, const
    QSize &requestSize, const QQuickImageProviderOptions &providerOptions,
    int frame, int frameCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpixmap.html#loadImageFromDevice

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    requestRegion : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    requestSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    providerOptions : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    frame : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    frameCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QQuickPixmap::loadImageFromDevice(QQmlEngine *engine, QIODevice
    #      *device, const QUrl &url, const QRect &requestRegion, const QSize
    #      &requestSize, const QQuickImageProviderOptions &providerOptions,
    #      int frame, int frameCount)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap19loadImageFromDeviceEP10QQmlEngineP9QIODev'
        'iceRK4QUrlRK5QRectRK5QSizeRK26QQuickImageProviderOptionsii',
        self._addressOf(engine), self._addressOf(device), self._valueOf(url),
        self._valueOf(requestRegion), self._valueOf(requestSize),
        self._valueOf(providerOptions), frame, frameCount,
    )

  @overload()
  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickPixmap::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#clear
    """
    #  void QQuickPixmap::clear()
    self.uglySide.call('ritual_ZN12QQuickPixmap5clearEv')

  @overload(QObject)
  @overload(NoneType)
  def clear(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickPixmap::clear(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#clear

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPixmap::clear(QObject *a0)
    self.uglySide.call(
        'ritual_ZN12QQuickPixmap5clearEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def connectFinished(
      self,
      a0: Optional[QObject],
      a1: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::connectFinished(QObject *a0, const char
    *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#connectFinished

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QQuickPixmap::connectFinished(QObject *a0, const char *a1)
    return self.uglySide.call(
        'ritual_ZN12QQuickPixmap15connectFinishedEP7QObjectPKc',
        self._addressOf(a0, 'QObject'), self._bytesOf(a1),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def connectFinished(self, a0: Optional[QObject], a1: int) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::connectFinished(QObject *a0, int a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmap.html#connectFinished

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  bool QQuickPixmap::connectFinished(QObject *a0, int a1)
    return self.uglySide.call(
        'ritual_ZN12QQuickPixmap15connectFinishedEP7QObjecti',
        self._addressOf(a0, 'QObject'), a1,
    )

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def connectDownloadProgress(
      self,
      a0: Optional[QObject],
      a1: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::connectDownloadProgress(QObject *a0, const
    char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpixmap.html#connectDownloadProgress

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QQuickPixmap::connectDownloadProgress(QObject *a0, const char
    #      *a1)
    return self.uglySide.call(
        'ritual_ZN12QQuickPixmap23connectDownloadProgressEP7QObjectPKc',
        self._addressOf(a0, 'QObject'), self._bytesOf(a1),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def connectDownloadProgress(self, a0: Optional[QObject], a1: int) -> bool:
    """
    Calls Qt's 'bool QQuickPixmap::connectDownloadProgress(QObject *a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpixmap.html#connectDownloadProgress

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  bool QQuickPixmap::connectDownloadProgress(QObject *a0, int a1)
    return self.uglySide.call(
        'ritual_ZN12QQuickPixmap23connectDownloadProgressEP7QObjecti',
        self._addressOf(a0, 'QObject'), a1,
    )

  @staticmethod
  def setPixmap(*__, **_) -> Never:
    """
    Qt's 'void QQuickPixmap::setPixmap(const QQuickPixmap &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPixmap.setPixmap' has no cute function yet. Qt's 'void "
        "QQuickPixmap::setPixmap(const QQuickPixmap &other)': takes a type "
        "Python has no way to hand over yet.")
