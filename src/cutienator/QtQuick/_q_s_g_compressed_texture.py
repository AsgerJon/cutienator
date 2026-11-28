"""
QSGCompressedTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcompressedtexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGCompressedTexture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QRhi, QRhiResourceUpdateBatch, QRhiTexture
  from ..QtGui import QTextureFileData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QTextureFileData = WAIT['QTextureFileData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGCompressedTexture(QSGTexture):
  """
  The cute side of Qt's QSGCompressedTexture: a plain Python object standing
  in front of one C++ QSGCompressedTexture.

  It is built on the cute 'QSGTexture', as Qt's QSGCompressedTexture is built
  on Qt's QSGTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCompressedTexture that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'textureSize',
  'hasAlphaChannel', 'hasMipmaps', 'comparisonKey', 'rhiTexture',
  'commitTextureOperations', 'textureData', 'formatInfo', 'formatIsOpaque'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGCompressedTexture::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSGCompressedTexture::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGCompressedTexture::~QSGCompressedTexture()': the destructor:
    Python never removes a C++ QSGCompressedTexture.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGCompressedTexture is created at the first use, not by
    'QSGCompressedTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCompressedTexture.
  - Qt tells when it has removed the C++ QSGCompressedTexture. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside QSGCompressedTexture, each a class in here
  #  as in C++.

  class FormatInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGCompressedTexture::FormatInfo: a plain Python
    object standing in front of one C++ QSGCompressedTexture::FormatInfo.

    C++ hands a QSGCompressedTexture::FormatInfo around as a copy, so every
    C++ QSGCompressedTexture::FormatInfo behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSGCompressedTexture::FormatInfo yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGCompressedTexture::FormatInfo::~FormatInfo()': the destructor:
      Python removes its C++ QSGCompressedTexture::FormatInfo by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QSGCompressedTexture::FormatInfo is created at the first use,
      not by 'QSGCompressedTexture::FormatInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGCompressedTexture::FormatInfo back gives a copy
      the ritual made for Python, in a new cute
      QSGCompressedTexture::FormatInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGCompressedTexture::FormatInfo'

    #  Qt's '~QSGCompressedTexture::FormatInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QSGCompressedTexture::FormatInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN20QSGCompressedTexture10FormatInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QSGCompressedTexture::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcompressedtexture.html#tr

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
    #  QString QSGCompressedTexture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QSGCompressedTexture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int)
  def formatInfo(glTextureFormat: int) -> FormatInfo:
    """
    Calls Qt's 'FormatInfo QSGCompressedTexture::formatInfo(quint32
    glTextureFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#formatInfo

    Parameters
    ----------

    glTextureFormat : int
      Passed on as it is.

    Returns
    -------

    FormatInfo
      A new cute QSGCompressedTexture::FormatInfo around the copy Qt gave
      back. Python owns it.
    """
    #  FormatInfo QSGCompressedTexture::formatInfo(quint32 glTextureFormat)
    address = Rituals.call(
        'ritual_ZN20QSGCompressedTexture10formatInfoEj', glTextureFormat,
    )
    return QSGCompressedTexture.FormatInfo._cuteOwning(address)

  @staticmethod
  @overload(int)
  def formatIsOpaque(glTextureFormat: int) -> bool:
    """
    Calls Qt's 'bool QSGCompressedTexture::formatIsOpaque(quint32
    glTextureFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#formatIsOpaque

    Parameters
    ----------

    glTextureFormat : int
      Passed on as it is.
    """
    #  bool QSGCompressedTexture::formatIsOpaque(quint32 glTextureFormat)
    return Rituals.call(
        'ritual_ZN20QSGCompressedTexture14formatIsOpaqueEj', glTextureFormat,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGCompressedTexture'

  #  A C++ QSGCompressedTexture Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGCompressedTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGCompressedTexture::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGCompressedTexture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QSGCompressedTexture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGCompressedTexture::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGCompressedTexture::textureSize() const
    ritual = 'ritual_ZNK20QSGCompressedTexture11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGCompressedTexture11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGCompressedTexture::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#hasAlphaChannel
    """
    #  bool QSGCompressedTexture::hasAlphaChannel() const
    ritual = 'ritual_ZNK20QSGCompressedTexture15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGCompressedTexture15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGCompressedTexture::hasMipmaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#hasMipmaps
    """
    #  bool QSGCompressedTexture::hasMipmaps() const
    ritual = 'ritual_ZNK20QSGCompressedTexture10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGCompressedTexture10hasMipmapsEv'
    return self.uglySide.call(ritual)

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGCompressedTexture::comparisonKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#comparisonKey
    """
    #  qint64 QSGCompressedTexture::comparisonKey() const
    ritual = 'ritual_ZNK20QSGCompressedTexture13comparisonKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGCompressedTexture13comparisonKeyEv'
    return self.uglySide.call(ritual)

  def rhiTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGCompressedTexture::rhiTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#rhiTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGCompressedTexture::rhiTexture() const
    ritual = 'ritual_ZNK20QSGCompressedTexture10rhiTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGCompressedTexture10rhiTextureEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def textureData(self) -> QTextureFileData:
    """
    Calls Qt's 'QTextureFileData QSGCompressedTexture::textureData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#textureData

    Returns
    -------

    QTextureFileData
      A new cute QTextureFileData around the copy Qt gave back. Python owns
      it.
    """
    #  QTextureFileData QSGCompressedTexture::textureData() const
    address = self.uglySide.call(
        'ritual_ZNK20QSGCompressedTexture11textureDataEv',
    )
    from ..QtGui import QTextureFileData
    return QTextureFileData._cuteOwning(address)

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

  @overload(QTextureFileData)
  def __init__(self, texData: QTextureFileData) -> None:
    """
    Notes what was given, for Qt's
    'QSGCompressedTexture::QSGCompressedTexture(const QTextureFileData
    &texData)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#QSGCompressedTexture

    Parameters
    ----------

    texData : QTextureFileData
      Passed on as a value: Qt reads the C++ QTextureFileData, which stays
      Python's own.
    """
    #  QSGCompressedTexture::QSGCompressedTexture(const QTextureFileData
    #      &texData)
    self._noteCreation(QSGCompressedTexture, lambda: Rituals.call(
        'ritual_ZN20QSGCompressedTextureC1ERK16QTextureFileData',
        self._valueOf(texData),
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
    Calls Qt's 'void QSGCompressedTexture::commitTextureOperations(QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexture.html#commitTextureOperations

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGCompressedTexture::commitTextureOperations(QRhi *rhi,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN20QSGCompressedTexture23commitTextureOperationsEP4QRhiP23'
        'QRhiResourceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGCompressedTexture23commitTextureOperationsEP4Q'
          'RhiP23QRhiResourceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(rhi), self._addressOf(resourceUpdates),
    )
