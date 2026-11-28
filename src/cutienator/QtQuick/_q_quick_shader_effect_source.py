"""
QQuickShaderEffectSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickshadereffectsource_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShaderEffectSource to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from . import QQuickGeometryChange, QSGNode, QSGTextureProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShaderEffectSource(QQuickItem):
  """
  The cute side of Qt's QQuickShaderEffectSource: a plain Python object
  standing in front of one C++ QQuickShaderEffectSource.

  It is built on the cute 'QQuickItem', as Qt's QQuickShaderEffectSource is
  built on Qt's QQuickItem, and has everything that class has. Qt's
  QQuickShaderEffectSource is built on Qt's
  QSafeQuickItemChangeListener<QQuickShaderEffectSource> as well, which is
  not reflected.

  What exists
  -----------

  Every function of Qt's QQuickShaderEffectSource that has a ritual and that
  Python can call so far, 46 names in all: 'metaObject', 'tr', 'wrapMode',
  'setWrapMode', 'sourceItem', 'setSourceItem', 'sourceRect',
  'setSourceRect', 'textureSize', 'setTextureSize', 'format', 'setFormat',
  'live', 'setLive', 'hideSource', 'setHideSource', 'mipmap', 'setMipmap',
  'recursive', 'setRecursive', 'textureMirroring', 'setTextureMirroring',
  'isTextureProvider', 'textureProvider', 'scheduleUpdate', 'samples',
  'setSamples', 'wrapModeChanged', 'sourceItemChanged', 'sourceRectChanged',
  'textureSizeChanged', 'formatChanged', 'liveChanged', 'hideSourceChanged',
  'mipmapChanged', 'recursiveChanged', 'textureMirroringChanged',
  'samplesChanged', 'scheduledUpdateCompleted', 'sourceItemDestroyed',
  'invalidateSceneGraph', 'releaseResources', 'updatePaintNode',
  'itemGeometryChanged', 'itemChange', 'ensureTexture'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShaderEffectSource::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickShaderEffectSource::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickShaderEffectSource::~QQuickShaderEffectSource()': the
    destructor: Python never removes a C++ QQuickShaderEffectSource.

  What has no ritual
  ------------------

  2 of the 52 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickShaderEffectSource is created at the first use, not by
    'QQuickShaderEffectSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShaderEffectSource.
  - Qt tells when it has removed the C++ QQuickShaderEffectSource. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickShaderEffectSource, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Format(CuteNum):
    """
    The enum 'QQuickShaderEffectSource::Format' of Qt, with the 6 names Qt
    gives in it.
    """

    RGBA8 = Kee[int](1)
    RGBA16F = Kee[int](2)
    RGBA32F = Kee[int](3)
    Alpha = Kee[int](1)
    RGB = Kee[int](1)
    RGBA = Kee[int](1)

  class TextureMirroring(CuteNum):
    """
    The enum 'QQuickShaderEffectSource::TextureMirroring' of Qt, with the 3
    names Qt gives in it.
    """

    NoMirroring = Kee[int](0)
    MirrorHorizontally = Kee[int](1)
    MirrorVertically = Kee[int](2)

  class WrapMode(CuteNum):
    """
    The enum 'QQuickShaderEffectSource::WrapMode' of Qt, with the 4 names Qt
    gives in it.
    """

    ClampToEdge = Kee[int](0)
    RepeatHorizontally = Kee[int](1)
    RepeatVertically = Kee[int](2)
    Repeat = Kee[int](3)

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
    Calls Qt's 'QString QQuickShaderEffectSource::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffectsource.html#tr

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
    #  QString QQuickShaderEffectSource::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickShaderEffectSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShaderEffectSource'

  #  A C++ QQuickShaderEffectSource Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShaderEffectSource'

  #  The functions Qt calls itself that QQuickShaderEffectSource is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN24QQuickShaderEffectSource19itemGeometryChangedEP10QQuickIte'
           'm20QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
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
    Calls Qt's 'const QMetaObject *QQuickShaderEffectSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShaderEffectSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def wrapMode(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode QQuickShaderEffectSource::wrapMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#wrapMode

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode QQuickShaderEffectSource::wrapMode() const
    return QQuickShaderEffectSource.WrapMode(self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource8wrapModeEv',
    ))

  def sourceItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickShaderEffectSource::sourceItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#sourceItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickShaderEffectSource::sourceItem() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource10sourceItemEv',
    )
    return QQuickItem._cuteAt(address)

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickShaderEffectSource::sourceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickShaderEffectSource::sourceRect() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource10sourceRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickShaderEffectSource::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickShaderEffectSource::textureSize() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource11textureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def format(self) -> Format:
    """
    Calls Qt's 'Format QQuickShaderEffectSource::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QQuickShaderEffectSource::format() const
    return QQuickShaderEffectSource.Format(self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource6formatEv',
    ))

  def live(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectSource::live() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffectsource.html#live
    """
    #  bool QQuickShaderEffectSource::live() const
    return self.uglySide.call('ritual_ZNK24QQuickShaderEffectSource4liveEv')

  def hideSource(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectSource::hideSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#hideSource
    """
    #  bool QQuickShaderEffectSource::hideSource() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource10hideSourceEv',
    )

  def mipmap(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectSource::mipmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#mipmap
    """
    #  bool QQuickShaderEffectSource::mipmap() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource6mipmapEv',
    )

  def recursive(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectSource::recursive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#recursive
    """
    #  bool QQuickShaderEffectSource::recursive() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource9recursiveEv',
    )

  def textureMirroring(self) -> TextureMirroring:
    """
    Calls Qt's 'TextureMirroring QQuickShaderEffectSource::textureMirroring()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#textureMirroring

    Returns
    -------

    TextureMirroring
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureMirroring(number)'
      gives.
    """
    #  TextureMirroring QQuickShaderEffectSource::textureMirroring() const
    return QQuickShaderEffectSource.TextureMirroring(self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource16textureMirroringEv',
    ))

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectSource::isTextureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#isTextureProvider
    """
    #  bool QQuickShaderEffectSource::isTextureProvider() const
    ritual = 'ritual_ZNK24QQuickShaderEffectSource17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQuickShaderEffectSource17isTextureProviderEv')
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider
    *QQuickShaderEffectSource::textureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuickShaderEffectSource::textureProvider() const
    ritual = 'ritual_ZNK24QQuickShaderEffectSource15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QQuickShaderEffectSource15textureProviderEv'
    address = self.uglySide.call(ritual)
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  def samples(self) -> int:
    """
    Calls Qt's 'int QQuickShaderEffectSource::samples() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#samples
    """
    #  int QQuickShaderEffectSource::samples() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickShaderEffectSource7samplesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WrapMode)
  def setWrapMode(self, mode: WrapMode) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setWrapMode(WrapMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setWrapMode

    Parameters
    ----------

    mode : WrapMode
      Passed on as its number.
    """
    #  void QQuickShaderEffectSource::setWrapMode(WrapMode mode)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource11setWrapModeENS_8WrapModeE',
        mode.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setSourceItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setSourceItem(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setSourceItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShaderEffectSource::setSourceItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource13setSourceItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QRectF)
  def setSourceRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setSourceRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setSourceRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickShaderEffectSource::setSourceRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource13setSourceRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QSize)
  def setTextureSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setTextureSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setTextureSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickShaderEffectSource::setTextureSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource14setTextureSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(Format)
  def setFormat(self, format: Format) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setFormat(Format format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setFormat

    Parameters
    ----------

    format : Format
      Passed on as its number.
    """
    #  void QQuickShaderEffectSource::setFormat(Format format)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource9setFormatENS_6FormatE',
        format.value,
    )

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setLive(bool live)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffectSource::setLive(bool live)
    self.uglySide.call('ritual_ZN24QQuickShaderEffectSource7setLiveEb', live)

  @overload(bool)
  def setHideSource(self, hide: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setHideSource(bool hide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setHideSource

    Parameters
    ----------

    hide : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffectSource::setHideSource(bool hide)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource13setHideSourceEb', hide,
    )

  @overload(bool)
  def setMipmap(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setMipmap(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setMipmap

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffectSource::setMipmap(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource9setMipmapEb', enabled,
    )

  @overload(bool)
  def setRecursive(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setRecursive(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setRecursive

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffectSource::setRecursive(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource12setRecursiveEb', enabled,
    )

  @overload(TextureMirroring)
  def setTextureMirroring(self, mirroring: TextureMirroring) -> None:
    """
    Calls Qt's 'void
    QQuickShaderEffectSource::setTextureMirroring(TextureMirroring
    mirroring)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setTextureMirroring

    Parameters
    ----------

    mirroring : TextureMirroring
      Passed on as its number.
    """
    #  void QQuickShaderEffectSource::setTextureMirroring(TextureMirroring
    #      mirroring)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource19setTextureMirroringENS_16Text'
        'ureMirroringE',
        mirroring.value,
    )

  @overload(int)
  def setSamples(self, count: int) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::setSamples(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#setSamples

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickShaderEffectSource::setSamples(int count)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource10setSamplesEi', count,
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
    'QQuickShaderEffectSource::QQuickShaderEffectSource(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShaderEffectSource::QQuickShaderEffectSource(QQuickItem *parent)
    self._noteCreation(QQuickShaderEffectSource, lambda: Rituals.call(
        'ritual_ZN24QQuickShaderEffectSourceC1EP10QQuickItem',
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

  def scheduleUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::scheduleUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#scheduleUpdate
    """
    #  void QQuickShaderEffectSource::scheduleUpdate()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource14scheduleUpdateEv',
    )

  def wrapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::wrapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#wrapModeChanged
    """
    #  void QQuickShaderEffectSource::wrapModeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource15wrapModeChangedEv',
    )

  def sourceItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::sourceItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#sourceItemChanged
    """
    #  void QQuickShaderEffectSource::sourceItemChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource17sourceItemChangedEv',
    )

  def sourceRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::sourceRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#sourceRectChanged
    """
    #  void QQuickShaderEffectSource::sourceRectChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource17sourceRectChangedEv',
    )

  def textureSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::textureSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#textureSizeChanged
    """
    #  void QQuickShaderEffectSource::textureSizeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource18textureSizeChangedEv',
    )

  def formatChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::formatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#formatChanged
    """
    #  void QQuickShaderEffectSource::formatChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource13formatChangedEv',
    )

  def liveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::liveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#liveChanged
    """
    #  void QQuickShaderEffectSource::liveChanged()
    self.uglySide.call('ritual_ZN24QQuickShaderEffectSource11liveChangedEv')

  def hideSourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::hideSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#hideSourceChanged
    """
    #  void QQuickShaderEffectSource::hideSourceChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource17hideSourceChangedEv',
    )

  def mipmapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::mipmapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#mipmapChanged
    """
    #  void QQuickShaderEffectSource::mipmapChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource13mipmapChangedEv',
    )

  def recursiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::recursiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#recursiveChanged
    """
    #  void QQuickShaderEffectSource::recursiveChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource16recursiveChangedEv',
    )

  def textureMirroringChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::textureMirroringChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html
    """
    #  void QQuickShaderEffectSource::textureMirroringChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource23textureMirroringChangedEv',
    )

  def samplesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::samplesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#samplesChanged
    """
    #  void QQuickShaderEffectSource::samplesChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource14samplesChangedEv',
    )

  def scheduledUpdateCompleted(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::scheduledUpdateCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html
    """
    #  void QQuickShaderEffectSource::scheduledUpdateCompleted()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource24scheduledUpdateCompletedEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def sourceItemDestroyed(self, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::sourceItemDestroyed(QObject
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#sourceItemDestroyed

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShaderEffectSource::sourceItemDestroyed(QObject *item)
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource19sourceItemDestroyedEP7QObject',
        self._addressOf(item, 'QObject'),
    )

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#invalidateSceneGraph
    """
    #  void QQuickShaderEffectSource::invalidateSceneGraph()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource20invalidateSceneGraphEv',
    )

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#releaseResources
    """
    #  void QQuickShaderEffectSource::releaseResources()
    ritual = 'ritual_ZN24QQuickShaderEffectSource16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickShaderEffectSource16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickShaderEffectSource::updatePaintNode(QSGNode
    *a0, UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickShaderEffectSource::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN24QQuickShaderEffectSource15updatePaintNodeEP7QSGNodePN10'
        'QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShaderEffectSource15updatePaintNodeEP7QSGNo'
          'dePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickShaderEffectSource::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &a2)
    ritual = (
        'ritual_ZN24QQuickShaderEffectSource19itemGeometryChangedEP10QQuick'
        'Item20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShaderEffectSource19itemGeometryChangedEP10'
          'QQuickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(a2),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::itemChange(ItemChange change,
    const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickShaderEffectSource::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN24QQuickShaderEffectSource10itemChangeEN10QQuickItem10Ite'
        'mChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickShaderEffectSource10itemChangeEN10QQuickIte'
          'm10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def ensureTexture(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectSource::ensureTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectsource.html#ensureTexture
    """
    #  void QQuickShaderEffectSource::ensureTexture()
    self.uglySide.call(
        'ritual_ZN24QQuickShaderEffectSource13ensureTextureEv',
    )
