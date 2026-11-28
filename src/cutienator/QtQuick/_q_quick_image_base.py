"""
QQuickImageBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickimagebase_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickImageBase to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickImplicitSizeItem, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize, QUrl
  from ..QtGui import QColorSpace, QImage
  from . import QQuickImageBasePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorSpace = WAIT['QColorSpace']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImageBase(QQuickImplicitSizeItem):
  """
  The cute side of Qt's QQuickImageBase: a plain Python object standing in
  front of one C++ QQuickImageBase.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's QQuickImageBase
  is built on Qt's QQuickImplicitSizeItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImageBase that has a ritual and that Python
  can call so far, 53 names in all: 'metaObject', 'tr', 'status', 'progress',
  'source', 'setSource', 'asynchronous', 'setAsynchronous', 'cache',
  'setCache', 'image', 'setSourceSize', 'sourceSize', 'resetSourceSize',
  'sourceClipRect', 'setSourceClipRect', 'resetSourceClipRect', 'setMirror',
  'mirror', 'setMirrorVertically', 'mirrorVertically', 'setCurrentFrame',
  'currentFrame', 'frameCount', 'setAutoTransform', 'autoTransform',
  'colorSpace', 'setColorSpace', 'retainWhileLoading',
  'setRetainWhileLoading', 'emitAutoTransformBaseChanged', 'sourceChanged',
  'sourceSizeChanged', 'statusChanged', 'progressChanged',
  'asynchronousChanged', 'cacheChanged', 'mirrorChanged',
  'currentFrameChanged', 'frameCountChanged', 'sourceClipRectChanged',
  'colorSpaceChanged', 'mirrorVerticallyChanged',
  'retainWhileLoadingChanged', 'loadEmptyUrl', 'loadPixmap', 'load',
  'componentComplete', 'pixmapChange', 'itemChange', 'requestFinished',
  'requestProgress', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImageBase::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickImageBase::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickImageBase::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuickImageBase::~QQuickImageBase()': the destructor: Python never
    removes a C++ QQuickImageBase.
  - Qt's 'void QQuickImageBase::resolve2xLocalFile(const QUrl &url, qreal
    targetDevicePixelRatio, QUrl *sourceUrl, qreal *sourceDevicePixelRatio)':
    takes a number to change where it is.
  - Qt's 'QQuickImageBase::QQuickImageBase(QQuickImageBasePrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickImageBasePrivate *QQuickImageBase::d_func() const':
    takes in Python what 'QQuickImageBasePrivate *QQuickImageBase::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 65 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickImageBase is created at the first use, not by
    'QQuickImageBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageBase.
  - Qt tells when it has removed the C++ QQuickImageBase. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickImageBase that has no cute function yet,
    'resolve2xLocalFile', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQuickImageBase, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LoadPixmapOption(CuteFlags):
    """
    The flags enum 'QQuickImageBase::LoadPixmapOption' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QQuickImageBase::LoadPixmapOptions'.
    """

    NoOption = 0x0
    HandleDPR = 0x1
    UseProviderOptions = 0x2

  LoadPixmapOptions = LoadPixmapOption

  class Status(CuteNum):
    """
    The enum 'QQuickImageBase::Status' of Qt, with the 4 names Qt gives in
    it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QQuickImageBase::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#tr

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
    #  QString QQuickImageBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickImageBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImageBase'

  #  A C++ QQuickImageBase Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImageBase'

  #  The functions Qt calls itself that QQuickImageBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setSource': (
          ('_ZN15QQuickImageBase9setSourceERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'setSourceSize': (
          ('_ZN15QQuickImageBase13setSourceSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'setMirror': (
          ('_ZN15QQuickImageBase9setMirrorEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setMirrorVertically': (
          ('_ZN15QQuickImageBase19setMirrorVerticallyEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setCurrentFrame': (
          ('_ZN15QQuickImageBase15setCurrentFrameEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'currentFrame': (
          ('_ZNK15QQuickImageBase12currentFrameEv',
           ('int', 'number', ''),
           ()),
      ),
      'frameCount': (
          ('_ZNK15QQuickImageBase10frameCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'setAutoTransform': (
          ('_ZN15QQuickImageBase16setAutoTransformEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setColorSpace': (
          ('_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColorSpace'),
           )),
      ),
      'emitAutoTransformBaseChanged': (
          ('_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'load': (
          ('_ZN15QQuickImageBase4loadEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'pixmapChange': (
          ('_ZN15QQuickImageBase12pixmapChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'requestFinished': (
          ('_ZN15QQuickImageBase15requestFinishedEv',
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
    Calls Qt's 'const QMetaObject *QQuickImageBase::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImageBase::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickImageBase10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickImageBase::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickImageBase::status() const
    return QQuickImageBase.Status(self.uglySide.call(
        'ritual_ZNK15QQuickImageBase6statusEv',
    ))

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageBase::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#progress
    """
    #  qreal QQuickImageBase::progress() const
    return self.uglySide.call('ritual_ZNK15QQuickImageBase8progressEv')

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickImageBase::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickImageBase::source() const
    address = self.uglySide.call('ritual_ZNK15QQuickImageBase6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageBase::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#asynchronous
    """
    #  bool QQuickImageBase::asynchronous() const
    return self.uglySide.call('ritual_ZNK15QQuickImageBase12asynchronousEv')

  def cache(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageBase::cache() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#cache
    """
    #  bool QQuickImageBase::cache() const
    return self.uglySide.call('ritual_ZNK15QQuickImageBase5cacheEv')

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickImageBase::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickImageBase::image() const
    address = self.uglySide.call('ritual_ZNK15QQuickImageBase5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def sourceSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickImageBase::sourceSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#sourceSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickImageBase::sourceSize() const
    address = self.uglySide.call('ritual_ZNK15QQuickImageBase10sourceSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sourceClipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickImageBase::sourceClipRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#sourceClipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickImageBase::sourceClipRect() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickImageBase14sourceClipRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def mirror(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageBase::mirror() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#mirror
    """
    #  bool QQuickImageBase::mirror() const
    return self.uglySide.call('ritual_ZNK15QQuickImageBase6mirrorEv')

  def mirrorVertically(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageBase::mirrorVertically() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#mirrorVertically
    """
    #  bool QQuickImageBase::mirrorVertically() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickImageBase16mirrorVerticallyEv',
    )

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QQuickImageBase::currentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#currentFrame
    """
    #  int QQuickImageBase::currentFrame() const
    ritual = 'ritual_ZNK15QQuickImageBase12currentFrameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickImageBase12currentFrameEv'
    return self.uglySide.call(ritual)

  def frameCount(self) -> int:
    """
    Calls Qt's 'int QQuickImageBase::frameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#frameCount
    """
    #  int QQuickImageBase::frameCount() const
    ritual = 'ritual_ZNK15QQuickImageBase10frameCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickImageBase10frameCountEv'
    return self.uglySide.call(ritual)

  def autoTransform(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageBase::autoTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#autoTransform
    """
    #  bool QQuickImageBase::autoTransform() const
    return self.uglySide.call('ritual_ZNK15QQuickImageBase13autoTransformEv')

  def colorSpace(self) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QQuickImageBase::colorSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#colorSpace

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QQuickImageBase::colorSpace() const
    address = self.uglySide.call('ritual_ZNK15QQuickImageBase10colorSpaceEv')
    from ..QtGui import QColorSpace
    return QColorSpace._cuteOwning(address)

  def retainWhileLoading(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageBase::retainWhileLoading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#retainWhileLoading
    """
    #  bool QQuickImageBase::retainWhileLoading() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickImageBase18retainWhileLoadingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickImageBase::setSource(const QUrl &url)
    ritual = 'ritual_ZN15QQuickImageBase9setSourceERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase9setSourceERK4QUrl'
    self.uglySide.call(ritual, self._valueOf(url))

  @overload(bool)
  def setAsynchronous(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setAsynchronous(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#setAsynchronous

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickImageBase::setAsynchronous(bool a0)
    self.uglySide.call('ritual_ZN15QQuickImageBase15setAsynchronousEb', a0)

  @overload(bool)
  def setCache(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setCache(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#setCache

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickImageBase::setCache(bool a0)
    self.uglySide.call('ritual_ZN15QQuickImageBase8setCacheEb', a0)

  @overload(QSize)
  def setSourceSize(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setSourceSize(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#setSourceSize

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickImageBase::setSourceSize(const QSize &a0)
    ritual = 'ritual_ZN15QQuickImageBase13setSourceSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase13setSourceSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QRectF)
  def setSourceClipRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setSourceClipRect(const QRectF &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#setSourceClipRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickImageBase::setSourceClipRect(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase17setSourceClipRectERK6QRectF',
        self._valueOf(r),
    )

  @overload(bool)
  def setMirror(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setMirror(bool mirror)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#setMirror

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QQuickImageBase::setMirror(bool mirror)
    ritual = 'ritual_ZN15QQuickImageBase9setMirrorEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase9setMirrorEb'
    self.uglySide.call(ritual, mirror)

  @overload(bool)
  def setMirrorVertically(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setMirrorVertically(bool mirror)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#setMirrorVertically

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QQuickImageBase::setMirrorVertically(bool mirror)
    ritual = 'ritual_ZN15QQuickImageBase19setMirrorVerticallyEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase19setMirrorVerticallyEb'
    self.uglySide.call(ritual, mirror)

  @overload(int)
  def setCurrentFrame(self, frame: int) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setCurrentFrame(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#setCurrentFrame

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QQuickImageBase::setCurrentFrame(int frame)
    ritual = 'ritual_ZN15QQuickImageBase15setCurrentFrameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase15setCurrentFrameEi'
    self.uglySide.call(ritual, frame)

  @overload(bool)
  def setAutoTransform(self, transform: bool) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setAutoTransform(bool transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#setAutoTransform

    Parameters
    ----------

    transform : bool
      Passed on as it is.
    """
    #  void QQuickImageBase::setAutoTransform(bool transform)
    ritual = 'ritual_ZN15QQuickImageBase16setAutoTransformEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase16setAutoTransformEb'
    self.uglySide.call(ritual, transform)

  @overload(QColorSpace)
  def setColorSpace(self, colorSpace: QColorSpace) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setColorSpace(const QColorSpace
    &colorSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#setColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  void QQuickImageBase::setColorSpace(const QColorSpace &colorSpace)
    ritual = 'ritual_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace')
    self.uglySide.call(ritual, self._valueOf(colorSpace))

  @overload(bool)
  def setRetainWhileLoading(self, retain: bool) -> None:
    """
    Calls Qt's 'void QQuickImageBase::setRetainWhileLoading(bool retain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#setRetainWhileLoading

    Parameters
    ----------

    retain : bool
      Passed on as it is.
    """
    #  void QQuickImageBase::setRetainWhileLoading(bool retain)
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase21setRetainWhileLoadingEb', retain,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickImageBase::QQuickImageBase(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#QQuickImageBase

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickImageBase::QQuickImageBase(QQuickItem *parent)
    self._noteCreation(QQuickImageBase, lambda: Rituals.call(
        'ritual_ZN15QQuickImageBaseC1EP10QQuickItem',
        self._addressOf(parent),
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

  def resetSourceSize(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::resetSourceSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#resetSourceSize
    """
    #  void QQuickImageBase::resetSourceSize()
    self.uglySide.call('ritual_ZN15QQuickImageBase15resetSourceSizeEv')

  def resetSourceClipRect(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::resetSourceClipRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#resetSourceClipRect
    """
    #  void QQuickImageBase::resetSourceClipRect()
    self.uglySide.call('ritual_ZN15QQuickImageBase19resetSourceClipRectEv')

  def emitAutoTransformBaseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::emitAutoTransformBaseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#emitAutoTransformBaseChanged
    """
    #  void QQuickImageBase::emitAutoTransformBaseChanged()
    ritual = 'ritual_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv')
    self.uglySide.call(ritual)

  @overload(QUrl)
  def sourceChanged(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQuickImageBase::sourceChanged(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#sourceChanged

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickImageBase::sourceChanged(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase13sourceChangedERK4QUrl',
        self._valueOf(a0),
    )

  def sourceSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::sourceSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#sourceSizeChanged
    """
    #  void QQuickImageBase::sourceSizeChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase17sourceSizeChangedEv')

  @overload(Status)
  def statusChanged(self, a0: Status) -> None:
    """
    Calls Qt's 'void QQuickImageBase::statusChanged(QQuickImageBase::Status
    a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#statusChanged

    Parameters
    ----------

    a0 : Status
      Passed on as its number.
    """
    #  void QQuickImageBase::statusChanged(QQuickImageBase::Status a0)
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase13statusChangedENS_6StatusE', a0.value,
    )

  @overload(float)
  def progressChanged(self, progress: float) -> None:
    """
    Calls Qt's 'void QQuickImageBase::progressChanged(qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#progressChanged

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQuickImageBase::progressChanged(qreal progress)
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase15progressChangedEd', progress,
    )

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#asynchronousChanged
    """
    #  void QQuickImageBase::asynchronousChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase19asynchronousChangedEv')

  def cacheChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::cacheChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#cacheChanged
    """
    #  void QQuickImageBase::cacheChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase12cacheChangedEv')

  def mirrorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::mirrorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#mirrorChanged
    """
    #  void QQuickImageBase::mirrorChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase13mirrorChangedEv')

  def currentFrameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::currentFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#currentFrameChanged
    """
    #  void QQuickImageBase::currentFrameChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase19currentFrameChangedEv')

  def frameCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::frameCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#frameCountChanged
    """
    #  void QQuickImageBase::frameCountChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase17frameCountChangedEv')

  def sourceClipRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::sourceClipRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#sourceClipRectChanged
    """
    #  void QQuickImageBase::sourceClipRectChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase21sourceClipRectChangedEv')

  def colorSpaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::colorSpaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#colorSpaceChanged
    """
    #  void QQuickImageBase::colorSpaceChanged()
    self.uglySide.call('ritual_ZN15QQuickImageBase17colorSpaceChangedEv')

  def mirrorVerticallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::mirrorVerticallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#mirrorVerticallyChanged
    """
    #  void QQuickImageBase::mirrorVerticallyChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase23mirrorVerticallyChangedEv',
    )

  def retainWhileLoadingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::retainWhileLoadingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#retainWhileLoadingChanged
    """
    #  void QQuickImageBase::retainWhileLoadingChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase25retainWhileLoadingChangedEv',
    )

  def loadEmptyUrl(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::loadEmptyUrl()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#loadEmptyUrl
    """
    #  void QQuickImageBase::loadEmptyUrl()
    self.uglySide.call('ritual_ZN15QQuickImageBase12loadEmptyUrlEv')

  @overload(QUrl)
  @overload(QUrl, LoadPixmapOptions)
  def loadPixmap(
      self,
      url: QUrl,
      loadOptions: LoadPixmapOptions = LoadPixmapOptions.NoOption,
  ) -> None:
    """
    Calls Qt's 'void QQuickImageBase::loadPixmap(const QUrl &url,
    LoadPixmapOptions loadOptions)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#loadPixmap

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    loadOptions : LoadPixmapOptions
      Passed on as its number. May be left out, as in Qt: it is then
      LoadPixmapOptions.NoOption.
    """
    #  void QQuickImageBase::loadPixmap(const QUrl &url, LoadPixmapOptions
    #      loadOptions)
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase10loadPixmapERK4QUrl6QFlagsINS_16LoadPix'
        'mapOptionEE',
        self._valueOf(url), loadOptions.value,
    )

  def load(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#load
    """
    #  void QQuickImageBase::load()
    ritual = 'ritual_ZN15QQuickImageBase4loadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase4loadEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#componentComplete
    """
    #  void QQuickImageBase::componentComplete()
    ritual = 'ritual_ZN15QQuickImageBase17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase17componentCompleteEv'
    self.uglySide.call(ritual)

  def pixmapChange(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::pixmapChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#pixmapChange
    """
    #  void QQuickImageBase::pixmapChange()
    ritual = 'ritual_ZN15QQuickImageBase12pixmapChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase12pixmapChangeEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickImageBase::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickImageBase::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN15QQuickImageBase10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickImageBase10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void QQuickImageBase::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#requestFinished
    """
    #  void QQuickImageBase::requestFinished()
    ritual = 'ritual_ZN15QQuickImageBase15requestFinishedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickImageBase15requestFinishedEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def requestProgress(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQuickImageBase::requestProgress(qint64 a0, qint64 a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagebase.html#requestProgress

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQuickImageBase::requestProgress(qint64 a0, qint64 a1)
    self.uglySide.call(
        'ritual_ZN15QQuickImageBase15requestProgressExx', a0, a1,
    )

  def d_func(self) -> Optional[QQuickImageBasePrivate]:
    """
    Calls Qt's 'QQuickImageBasePrivate *QQuickImageBase::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagebase.html#d_func

    Returns
    -------

    Optional[QQuickImageBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageBasePrivate *QQuickImageBase::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickImageBase6d_funcEv')
    from . import QQuickImageBasePrivate
    return QQuickImageBasePrivate._cuteAt(address)

  @staticmethod
  def resolve2xLocalFile(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageBase::resolve2xLocalFile(const QUrl &url, qreal
    targetDevicePixelRatio, QUrl *sourceUrl, qreal *sourceDevicePixelRatio)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickImageBase.resolve2xLocalFile' has no cute function yet. "
        "Qt's 'void QQuickImageBase::resolve2xLocalFile(const QUrl &url, "
        "qreal targetDevicePixelRatio, QUrl *sourceUrl, qreal "
        "*sourceDevicePixelRatio)': takes a number to change where it is.")
