"""
QSGTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgtexture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtGui import QRhi, QRhiResourceUpdateBatch, QRhiTexture
  from . import QSGTexturePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGTexture(QObject):
  """
  The cute side of Qt's QSGTexture: a plain Python object standing in front
  of one C++ QSGTexture.

  It is built on the cute 'QObject', as Qt's QSGTexture is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGTexture that has a ritual and that Python can
  call so far, 23 names in all: 'metaObject', 'tr', 'd_func',
  'comparisonKey', 'rhiTexture', 'textureSize', 'hasAlphaChannel',
  'hasMipmaps', 'normalizedTextureSubRect', 'isAtlasTexture',
  'removedFromAtlas', 'commitTextureOperations', 'setMipmapFiltering',
  'mipmapFiltering', 'setFiltering', 'filtering', 'setAnisotropyLevel',
  'anisotropyLevel', 'setHorizontalWrapMode', 'horizontalWrapMode',
  'setVerticalWrapMode', 'verticalWrapMode', 'convertToNormalizedSourceRect'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGTexture::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSGTexture::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSGTexturePrivate *QSGTexture::d_func() const': takes in
    Python what 'QSGTexturePrivate *QSGTexture::d_func()' takes.
  - Qt's 'QSGTexture::~QSGTexture()': the destructor: Python never removes a
    C++ QSGTexture.
  - Qt's 'void *QSGTexture::resolveInterface(const char *name, int revision)
    const': gives 'void', which has no cute class yet.
  - Qt's 'QSGTexture::QSGTexture(QSGTexturePrivate &dd)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QSGTexture is created at the first use, not by 'QSGTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGTexture.
  - Qt tells when it has removed the C++ QSGTexture. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSGTexture that has no cute function yet,
    'nativeInterface', 'resolveInterface', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSGTexture, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AnisotropyLevel(CuteNum):
    """
    The enum 'QSGTexture::AnisotropyLevel' of Qt, with the 5 names Qt gives
    in it.
    """

    AnisotropyNone = Kee[int](0)
    Anisotropy2x = Kee[int](1)
    Anisotropy4x = Kee[int](2)
    Anisotropy8x = Kee[int](3)
    Anisotropy16x = Kee[int](4)

  class Filtering(CuteNum):
    """
    The enum 'QSGTexture::Filtering' of Qt, with the 3 names Qt gives in it.
    """

    NULL = Kee[int](0)
    Nearest = Kee[int](1)
    Linear = Kee[int](2)

  class WrapMode(CuteNum):
    """
    The enum 'QSGTexture::WrapMode' of Qt, with the 3 names Qt gives in it.
    """

    Repeat = Kee[int](0)
    ClampToEdge = Kee[int](1)
    MirroredRepeat = Kee[int](2)

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
    Calls Qt's 'QString QSGTexture::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#tr

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
    #  QString QSGTexture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QSGTexture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTexture'

  #  A C++ QSGTexture Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGTexture'

  #  The functions Qt calls itself that QSGTexture is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'comparisonKey': (
          ('_ZNK10QSGTexture13comparisonKeyEv',
           ('long long', 'number', ''),
           ()),
      ),
      'rhiTexture': (
          ('_ZNK10QSGTexture10rhiTextureEv',
           ('address', 'address', 'QtGui:QRhiTexture'),
           ()),
      ),
      'textureSize': (
          ('_ZNK10QSGTexture11textureSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'hasAlphaChannel': (
          ('_ZNK10QSGTexture15hasAlphaChannelEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hasMipmaps': (
          ('_ZNK10QSGTexture10hasMipmapsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'normalizedTextureSubRect': (
          ('_ZNK10QSGTexture24normalizedTextureSubRectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'isAtlasTexture': (
          ('_ZNK10QSGTexture14isAtlasTextureEv',
           ('bool', 'number', ''),
           ()),
      ),
      'removedFromAtlas': (
          ('_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch',
           ('address', 'address', 'QtQuick:QSGTexture'),
           (
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
           )),
      ),
      'commitTextureOperations': (
          ('_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceU'
           'pdateBatch',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhi'),
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
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
    Calls Qt's 'const QMetaObject *QSGTexture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGTexture::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QSGTexture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGTexture::comparisonKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#comparisonKey
    """
    #  qint64 QSGTexture::comparisonKey() const
    return self.uglySide.call('ritual_ZNK10QSGTexture13comparisonKeyEv')

  def rhiTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGTexture::rhiTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#rhiTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGTexture::rhiTexture() const
    ritual = 'ritual_ZNK10QSGTexture10rhiTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSGTexture10rhiTextureEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGTexture::textureSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGTexture::textureSize() const
    address = self.uglySide.call('ritual_ZNK10QSGTexture11textureSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGTexture::hasAlphaChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#hasAlphaChannel
    """
    #  bool QSGTexture::hasAlphaChannel() const
    return self.uglySide.call('ritual_ZNK10QSGTexture15hasAlphaChannelEv')

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGTexture::hasMipmaps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#hasMipmaps
    """
    #  bool QSGTexture::hasMipmaps() const
    return self.uglySide.call('ritual_ZNK10QSGTexture10hasMipmapsEv')

  def normalizedTextureSubRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGTexture::normalizedTextureSubRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexture.html#normalizedTextureSubRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGTexture::normalizedTextureSubRect() const
    ritual = 'ritual_ZNK10QSGTexture24normalizedTextureSubRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSGTexture24normalizedTextureSubRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isAtlasTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGTexture::isAtlasTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#isAtlasTexture
    """
    #  bool QSGTexture::isAtlasTexture() const
    ritual = 'ritual_ZNK10QSGTexture14isAtlasTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSGTexture14isAtlasTextureEv'
    return self.uglySide.call(ritual)

  @overload()
  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def removedFromAtlas(
      self,
      resourceUpdates: Optional[QRhiResourceUpdateBatch] = None,
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch *resourceUpdates)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#removedFromAtlas

    Parameters
    ----------

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
    #      *resourceUpdates) const
    ritual = (
        'ritual_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatc'
        'h')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpda'
          'teBatch')
    address = self.uglySide.call(ritual, self._addressOf(resourceUpdates))
    return QSGTexture._cuteAt(address)

  def mipmapFiltering(self) -> Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGTexture::mipmapFiltering() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#mipmapFiltering

    Returns
    -------

    Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGTexture::mipmapFiltering() const
    return QSGTexture.Filtering(self.uglySide.call(
        'ritual_ZNK10QSGTexture15mipmapFilteringEv',
    ))

  def filtering(self) -> Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGTexture::filtering() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#filtering

    Returns
    -------

    Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGTexture::filtering() const
    return QSGTexture.Filtering(self.uglySide.call(
        'ritual_ZNK10QSGTexture9filteringEv',
    ))

  def anisotropyLevel(self) -> AnisotropyLevel:
    """
    Calls Qt's 'QSGTexture::AnisotropyLevel QSGTexture::anisotropyLevel()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#anisotropyLevel

    Returns
    -------

    AnisotropyLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AnisotropyLevel(number)'
      gives.
    """
    #  QSGTexture::AnisotropyLevel QSGTexture::anisotropyLevel() const
    return QSGTexture.AnisotropyLevel(self.uglySide.call(
        'ritual_ZNK10QSGTexture15anisotropyLevelEv',
    ))

  def horizontalWrapMode(self) -> WrapMode:
    """
    Calls Qt's 'QSGTexture::WrapMode QSGTexture::horizontalWrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#horizontalWrapMode

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  QSGTexture::WrapMode QSGTexture::horizontalWrapMode() const
    return QSGTexture.WrapMode(self.uglySide.call(
        'ritual_ZNK10QSGTexture18horizontalWrapModeEv',
    ))

  def verticalWrapMode(self) -> WrapMode:
    """
    Calls Qt's 'QSGTexture::WrapMode QSGTexture::verticalWrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#verticalWrapMode

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  QSGTexture::WrapMode QSGTexture::verticalWrapMode() const
    return QSGTexture.WrapMode(self.uglySide.call(
        'ritual_ZNK10QSGTexture16verticalWrapModeEv',
    ))

  @overload(QRectF)
  def convertToNormalizedSourceRect(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QSGTexture::convertToNormalizedSourceRect(const QRectF
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexture.html#convertToNormalizedSourceRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGTexture::convertToNormalizedSourceRect(const QRectF &rect)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QSGTexture29convertToNormalizedSourceRectERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Filtering)
  def setMipmapFiltering(self, filter: Filtering) -> None:
    """
    Calls Qt's 'void QSGTexture::setMipmapFiltering(Filtering filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#setMipmapFiltering

    Parameters
    ----------

    filter : Filtering
      Passed on as its number.
    """
    #  void QSGTexture::setMipmapFiltering(Filtering filter)
    self.uglySide.call(
        'ritual_ZN10QSGTexture18setMipmapFilteringENS_9FilteringE',
        filter.value,
    )

  @overload(Filtering)
  def setFiltering(self, filter: Filtering) -> None:
    """
    Calls Qt's 'void QSGTexture::setFiltering(Filtering filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#setFiltering

    Parameters
    ----------

    filter : Filtering
      Passed on as its number.
    """
    #  void QSGTexture::setFiltering(Filtering filter)
    self.uglySide.call(
        'ritual_ZN10QSGTexture12setFilteringENS_9FilteringE', filter.value,
    )

  @overload(AnisotropyLevel)
  def setAnisotropyLevel(self, level: AnisotropyLevel) -> None:
    """
    Calls Qt's 'void QSGTexture::setAnisotropyLevel(AnisotropyLevel level)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#setAnisotropyLevel

    Parameters
    ----------

    level : AnisotropyLevel
      Passed on as its number.
    """
    #  void QSGTexture::setAnisotropyLevel(AnisotropyLevel level)
    self.uglySide.call(
        'ritual_ZN10QSGTexture18setAnisotropyLevelENS_15AnisotropyLevelE',
        level.value,
    )

  @overload(WrapMode)
  def setHorizontalWrapMode(self, hwrap: WrapMode) -> None:
    """
    Calls Qt's 'void QSGTexture::setHorizontalWrapMode(WrapMode hwrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexture.html#setHorizontalWrapMode

    Parameters
    ----------

    hwrap : WrapMode
      Passed on as its number.
    """
    #  void QSGTexture::setHorizontalWrapMode(WrapMode hwrap)
    self.uglySide.call(
        'ritual_ZN10QSGTexture21setHorizontalWrapModeENS_8WrapModeE',
        hwrap.value,
    )

  @overload(WrapMode)
  def setVerticalWrapMode(self, vwrap: WrapMode) -> None:
    """
    Calls Qt's 'void QSGTexture::setVerticalWrapMode(WrapMode vwrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexture.html#setVerticalWrapMode

    Parameters
    ----------

    vwrap : WrapMode
      Passed on as its number.
    """
    #  void QSGTexture::setVerticalWrapMode(WrapMode vwrap)
    self.uglySide.call(
        'ritual_ZN10QSGTexture19setVerticalWrapModeENS_8WrapModeE',
        vwrap.value,
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
    Notes what was given, for Qt's 'QSGTexture::QSGTexture()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#QSGTexture
    """
    #  QSGTexture::QSGTexture()
    self._noteCreation(QSGTexture, lambda: Rituals.call(
        'ritual_ZN10QSGTextureC1Ev',
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

  def d_func(self) -> Optional[QSGTexturePrivate]:
    """
    Calls Qt's 'QSGTexturePrivate *QSGTexture::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexture.html#d_func

    Returns
    -------

    Optional[QSGTexturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexturePrivate *QSGTexture::d_func()
    address = self.uglySide.call('ritual_ZN10QSGTexture6d_funcEv')
    from . import QSGTexturePrivate
    return QSGTexturePrivate._cuteAt(address)

  @overload(QRhi, QRhiResourceUpdateBatch)
  @overload(QRhi, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def commitTextureOperations(
      self,
      rhi: Optional[QRhi],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSGTexture::commitTextureOperations(QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexture.html#commitTextureOperations

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGTexture::commitTextureOperations(QRhi *rhi,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResour'
        'ceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhi'
          'ResourceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(rhi), self._addressOf(resourceUpdates),
    )

  @staticmethod
  def nativeInterface(*__, **_) -> Never:
    """
    Qt's 'QSGTexture::nativeInterface': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QSGTexture.nativeInterface' has no cute function yet. Qt's "
        "'QSGTexture::nativeInterface': a template: a pattern and no single "
        "function.")

  @staticmethod
  def resolveInterface(*__, **_) -> Never:
    """
    Qt's 'void *QSGTexture::resolveInterface(const char *name, int revision)
    const': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGTexture.resolveInterface' has no cute function yet. Qt's 'void "
        "*QSGTexture::resolveInterface(const char *name, int revision) "
        "const': gives 'void', which has no cute class yet.")
