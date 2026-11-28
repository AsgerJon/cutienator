"""
QSGPlainTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgplaintexture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGPlainTexture to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickWindow, QQuickWindowPrivate, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QImage, QRhi, QRhiResourceUpdateBatch, QRhiTexture
  from . import QSGPlainTexturePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiTexture = WAIT['QRhiTexture']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGPlainTexture(QSGTexture):
  """
  The cute side of Qt's QSGPlainTexture: a plain Python object standing in
  front of one C++ QSGPlainTexture.

  It is built on the cute 'QSGTexture', as Qt's QSGPlainTexture is built on
  Qt's QSGTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGPlainTexture that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'd_func',
  'setOwnsTexture', 'ownsTexture', 'setTextureSize', 'textureSize',
  'setHasAlphaChannel', 'hasAlphaChannel', 'hasMipmaps', 'setImage', 'image',
  'comparisonKey', 'rhiTexture', 'commitTextureOperations', 'setTexture',
  'setTextureFromNativeTexture', 'fromImage'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGPlainTexture::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSGPlainTexture::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSGPlainTexturePrivate *QSGPlainTexture::d_func() const':
    takes in Python what 'QSGPlainTexturePrivate *QSGPlainTexture::d_func()'
    takes.
  - Qt's 'QSGPlainTexture::~QSGPlainTexture()': the destructor: Python never
    removes a C++ QSGPlainTexture.
  - Qt's 'QSGPlainTexture::QSGPlainTexture(QSGPlainTexturePrivate &dd)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGPlainTexture is created at the first use, not by
    'QSGPlainTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGPlainTexture.
  - Qt tells when it has removed the C++ QSGPlainTexture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QSGPlainTexture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#tr

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
    #  QString QSGPlainTexture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QSGPlainTexture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QImage)
  def fromImage(image: QImage) -> Optional[QSGPlainTexture]:
    """
    Calls Qt's 'QSGPlainTexture *QSGPlainTexture::fromImage(const QImage
    &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#fromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    Optional[QSGPlainTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGPlainTexture *QSGPlainTexture::fromImage(const QImage &image)
    address = Rituals.call(
        'ritual_ZN15QSGPlainTexture9fromImageERK6QImage',
        CuteMixin._valueOf(image),
    )
    return QSGPlainTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGPlainTexture'

  #  A C++ QSGPlainTexture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGPlainTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGPlainTexture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGPlainTexture::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QSGPlainTexture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ownsTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGPlainTexture::ownsTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#ownsTexture
    """
    #  bool QSGPlainTexture::ownsTexture() const
    return self.uglySide.call('ritual_ZNK15QSGPlainTexture11ownsTextureEv')

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGPlainTexture::textureSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGPlainTexture::textureSize() const
    ritual = 'ritual_ZNK15QSGPlainTexture11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGPlainTexture11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGPlainTexture::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgplaintexture.html#hasAlphaChannel
    """
    #  bool QSGPlainTexture::hasAlphaChannel() const
    ritual = 'ritual_ZNK15QSGPlainTexture15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGPlainTexture15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGPlainTexture::hasMipmaps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#hasMipmaps
    """
    #  bool QSGPlainTexture::hasMipmaps() const
    ritual = 'ritual_ZNK15QSGPlainTexture10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGPlainTexture10hasMipmapsEv'
    return self.uglySide.call(ritual)

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGPlainTexture::comparisonKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#comparisonKey
    """
    #  qint64 QSGPlainTexture::comparisonKey() const
    ritual = 'ritual_ZNK15QSGPlainTexture13comparisonKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGPlainTexture13comparisonKeyEv'
    return self.uglySide.call(ritual)

  def rhiTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGPlainTexture::rhiTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#rhiTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGPlainTexture::rhiTexture() const
    ritual = 'ritual_ZNK15QSGPlainTexture10rhiTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGPlainTexture10rhiTextureEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setOwnsTexture(self, owns: bool) -> None:
    """
    Calls Qt's 'void QSGPlainTexture::setOwnsTexture(bool owns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgplaintexture.html#setOwnsTexture

    Parameters
    ----------

    owns : bool
      Passed on as it is.
    """
    #  void QSGPlainTexture::setOwnsTexture(bool owns)
    self.uglySide.call('ritual_ZN15QSGPlainTexture14setOwnsTextureEb', owns)

  @overload(QSize)
  def setTextureSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGPlainTexture::setTextureSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgplaintexture.html#setTextureSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGPlainTexture::setTextureSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN15QSGPlainTexture14setTextureSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(bool)
  def setHasAlphaChannel(self, alpha: bool) -> None:
    """
    Calls Qt's 'void QSGPlainTexture::setHasAlphaChannel(bool alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgplaintexture.html#setHasAlphaChannel

    Parameters
    ----------

    alpha : bool
      Passed on as it is.
    """
    #  void QSGPlainTexture::setHasAlphaChannel(bool alpha)
    self.uglySide.call(
        'ritual_ZN15QSGPlainTexture18setHasAlphaChannelEb', alpha,
    )

  @overload(QImage)
  def setImage(self, image: QImage) -> None:
    """
    Calls Qt's 'void QSGPlainTexture::setImage(const QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#setImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QSGPlainTexture::setImage(const QImage &image)
    self.uglySide.call(
        'ritual_ZN15QSGPlainTexture8setImageERK6QImage',
        self._valueOf(image),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSGPlainTexture::setTexture(QRhiTexture *texture)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#setTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGPlainTexture::setTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN15QSGPlainTexture10setTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(
      QRhi, int, int, int, QSize, QQuickWindow.CreateTextureOptions,
      QQuickWindowPrivate.TextureFromNativeTextureFlags,
  )
  @overload(
      NoneType, int, int, int, QSize, QQuickWindow.CreateTextureOptions,
      QQuickWindowPrivate.TextureFromNativeTextureFlags,
  )
  def setTextureFromNativeTexture(
      self,
      rhi: Optional[QRhi],
      nativeObjectHandle: int,
      nativeLayoutOrState: int,
      nativeFormat: int,
      size: QSize,
      options: QQuickWindow.CreateTextureOptions,
      flags: QQuickWindowPrivate.TextureFromNativeTextureFlags,
  ) -> None:
    """
    Calls Qt's 'void QSGPlainTexture::setTextureFromNativeTexture(QRhi *rhi,
    quint64 nativeObjectHandle, int nativeLayoutOrState, uint nativeFormat,
    const QSize &size, QQuickWindow::CreateTextureOptions options,
    QQuickWindowPrivate::TextureFromNativeTextureFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgplaintexture.html#setTextureFromNativeTexture

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    nativeObjectHandle : int
      Passed on as it is.

    nativeLayoutOrState : int
      Passed on as it is.

    nativeFormat : int
      Passed on as it is.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickWindow.CreateTextureOptions
      Passed on as its number.

    flags : QQuickWindowPrivate.TextureFromNativeTextureFlags
      Passed on as its number.
    """
    #  void QSGPlainTexture::setTextureFromNativeTexture(QRhi *rhi, quint64
    #      nativeObjectHandle, int nativeLayoutOrState, uint nativeFormat,
    #      const QSize &size, QQuickWindow::CreateTextureOptions options,
    #      QQuickWindowPrivate::TextureFromNativeTextureFlags flags)
    self.uglySide.call(
        'ritual_ZN15QSGPlainTexture27setTextureFromNativeTextureEP4QRhiyijR'
        'K5QSize6QFlagsIN12QQuickWindow19CreateTextureOptionEES5_IN19QQuick'
        'WindowPrivate28TextureFromNativeTextureFlagEE',
        self._addressOf(rhi), nativeObjectHandle, nativeLayoutOrState,
        nativeFormat, self._valueOf(size), options.value, flags.value,
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
    Notes what was given, for Qt's 'QSGPlainTexture::QSGPlainTexture()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgplaintexture.html#QSGPlainTexture
    """
    #  QSGPlainTexture::QSGPlainTexture()
    self._noteCreation(QSGPlainTexture, lambda: Rituals.call(
        'ritual_ZN15QSGPlainTextureC1Ev',
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

  def d_func(self) -> Optional[QSGPlainTexturePrivate]:
    """
    Calls Qt's 'QSGPlainTexturePrivate *QSGPlainTexture::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#d_func

    Returns
    -------

    Optional[QSGPlainTexturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGPlainTexturePrivate *QSGPlainTexture::d_func()
    address = self.uglySide.call('ritual_ZN15QSGPlainTexture6d_funcEv')
    from . import QSGPlainTexturePrivate
    return QSGPlainTexturePrivate._cuteAt(address)

  def image(self) -> QImage:
    """
    Calls Qt's 'const QImage &QSGPlainTexture::image()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgplaintexture.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &QSGPlainTexture::image()
    address = self.uglySide.call('ritual_ZN15QSGPlainTexture5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

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
    Calls Qt's 'void QSGPlainTexture::commitTextureOperations(QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgplaintexture.html#commitTextureOperations

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGPlainTexture::commitTextureOperations(QRhi *rhi,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN15QSGPlainTexture23commitTextureOperationsEP4QRhiP23QRhiR'
        'esourceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QSGPlainTexture23commitTextureOperationsEP4QRhiP2'
          '3QRhiResourceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(rhi), self._addressOf(resourceUpdates),
    )
