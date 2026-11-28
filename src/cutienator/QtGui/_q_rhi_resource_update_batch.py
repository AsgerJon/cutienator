"""
QRhiResourceUpdateBatch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QImage, QRhiBuffer, QRhiImplementation
  from . import QRhiReadbackDescription, QRhiReadbackResult, QRhiTexture
  from . import QRhiTextureCopyDescription, QRhiTextureUploadDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QImage = WAIT['QImage']
  QRhiBuffer = WAIT['QRhiBuffer']
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiReadbackDescription = WAIT['QRhiReadbackDescription']
  QRhiReadbackResult = WAIT['QRhiReadbackResult']
  QRhiTexture = WAIT['QRhiTexture']
  QRhiTextureCopyDescription = WAIT['QRhiTextureCopyDescription']
  QRhiTextureUploadDescription = WAIT['QRhiTextureUploadDescription']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiResourceUpdateBatch(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiResourceUpdateBatch: a plain Python object
  standing in front of one C++ QRhiResourceUpdateBatch.

  What exists
  -----------

  Every function of Qt's QRhiResourceUpdateBatch that has a ritual and that
  Python can call so far, 10 names in all: 'release', 'merge',
  'hasOptimalCapacity', 'updateDynamicBuffer', 'uploadStaticBuffer',
  'readBackBuffer', 'uploadTexture', 'copyTexture', 'readBackTexture',
  'generateMips'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiResourceUpdateBatch::~QRhiResourceUpdateBatch()': the
    destructor: Python never removes a C++ QRhiResourceUpdateBatch.
  - Qt's 'void QRhiResourceUpdateBatch::updateDynamicBuffer(QRhiBuffer *buf,
    quint32 offset, quint32 size, const void *data)': names 'void', which has
    no cute class yet.
  - Qt's 'void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer *buf,
    quint32 offset, quint32 size, const void *data)': names 'void', which has
    no cute class yet.
  - Qt's 'void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer *buf,
    const void *data)': names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QRhiResourceUpdateBatch is created at the first use, not by
    'QRhiResourceUpdateBatch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiResourceUpdateBatch.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiResourceUpdateBatch'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasOptimalCapacity(self) -> bool:
    """
    Calls Qt's 'bool QRhiResourceUpdateBatch::hasOptimalCapacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#hasOptimalCapacity
    """
    #  bool QRhiResourceUpdateBatch::hasOptimalCapacity() const
    return self.uglySide.call(
        'ritual_ZNK23QRhiResourceUpdateBatch18hasOptimalCapacityEv',
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

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiResourceUpdateBatch::QRhiResourceUpdateBatch(QRhiImplementation
    *rhi)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiResourceUpdateBatch::QRhiResourceUpdateBatch(QRhiImplementation
    #      *rhi)
    self._noteCreation(QRhiResourceUpdateBatch, lambda: Rituals.call(
        'ritual_ZN23QRhiResourceUpdateBatchC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  def release(self) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#release
    """
    #  void QRhiResourceUpdateBatch::release()
    self.uglySide.call('ritual_ZN23QRhiResourceUpdateBatch7releaseEv')

  @overload(THIS)
  @overload(NoneType)
  def merge(self, other: Optional[QRhiResourceUpdateBatch]) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::merge(QRhiResourceUpdateBatch
    *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#merge

    Parameters
    ----------

    other : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiResourceUpdateBatch::merge(QRhiResourceUpdateBatch *other)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch5mergeEPS_',
        self._addressOf(other),
    )

  @overload(QRhiBuffer, int, QByteArray)
  @overload(NoneType, int, QByteArray)
  def updateDynamicBuffer(
      self,
      buf: Optional[QRhiBuffer],
      offset: int,
      data: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::updateDynamicBuffer(QRhiBuffer
    *buf, quint32 offset, QByteArray data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#updateDynamicBuffer

    Parameters
    ----------

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiResourceUpdateBatch::updateDynamicBuffer(QRhiBuffer *buf,
    #      quint32 offset, QByteArray data)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch19updateDynamicBufferEP10QRhiBuf'
        'ferj10QByteArray',
        self._addressOf(buf), offset, self._valueOf(data),
    )

  @overload(QRhiBuffer, int, QByteArray)
  @overload(NoneType, int, QByteArray)
  def uploadStaticBuffer(
      self,
      buf: Optional[QRhiBuffer],
      offset: int,
      data: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer
    *buf, quint32 offset, QByteArray data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#uploadStaticBuffer

    Parameters
    ----------

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer *buf,
    #      quint32 offset, QByteArray data)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch18uploadStaticBufferEP10QRhiBuff'
        'erj10QByteArray',
        self._addressOf(buf), offset, self._valueOf(data),
    )

  @overload(QRhiBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def uploadStaticBuffer(
      self,
      buf: Optional[QRhiBuffer],
      data: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer
    *buf, QByteArray data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#uploadStaticBuffer

    Parameters
    ----------

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer *buf,
    #      QByteArray data)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch18uploadStaticBufferEP10QRhiBuff'
        'er10QByteArray',
        self._addressOf(buf), self._valueOf(data),
    )

  @overload(QRhiBuffer, int, int, QRhiReadbackResult)
  @overload(QRhiBuffer, int, int, NoneType)
  @overload(NoneType, int, int, QRhiReadbackResult)
  @overload(NoneType, int, int, NoneType)
  def readBackBuffer(
      self,
      buf: Optional[QRhiBuffer],
      offset: int,
      size: int,
      result: Optional[QRhiReadbackResult],
  ) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::readBackBuffer(QRhiBuffer *buf,
    quint32 offset, quint32 size, QRhiReadbackResult *result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#readBackBuffer

    Parameters
    ----------

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.

    result : Optional[QRhiReadbackResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiResourceUpdateBatch::readBackBuffer(QRhiBuffer *buf, quint32
    #      offset, quint32 size, QRhiReadbackResult *result)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch14readBackBufferEP10QRhiBufferjj'
        'P18QRhiReadbackResult',
        self._addressOf(buf), offset, size, self._addressOf(result),
    )

  @overload(QRhiTexture, QRhiTextureUploadDescription)
  @overload(NoneType, QRhiTextureUploadDescription)
  def uploadTexture(
      self,
      tex: Optional[QRhiTexture],
      desc: QRhiTextureUploadDescription,
  ) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::uploadTexture(QRhiTexture *tex,
    const QRhiTextureUploadDescription &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#uploadTexture

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    desc : QRhiTextureUploadDescription
      Passed on as a value: Qt reads the C++ QRhiTextureUploadDescription,
      which stays Python's own.
    """
    #  void QRhiResourceUpdateBatch::uploadTexture(QRhiTexture *tex, const
    #      QRhiTextureUploadDescription &desc)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch13uploadTextureEP11QRhiTextureRK'
        '28QRhiTextureUploadDescription',
        self._addressOf(tex), self._valueOf(desc),
    )

  @overload(QRhiTexture, QImage)
  @overload(NoneType, QImage)
  def uploadTexture(self, tex: Optional[QRhiTexture], image: QImage) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::uploadTexture(QRhiTexture *tex,
    const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#uploadTexture

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QRhiResourceUpdateBatch::uploadTexture(QRhiTexture *tex, const
    #      QImage &image)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch13uploadTextureEP11QRhiTextureRK'
        '6QImage',
        self._addressOf(tex), self._valueOf(image),
    )

  @overload(QRhiTexture, QRhiTexture)
  @overload(QRhiTexture, NoneType)
  @overload(NoneType, QRhiTexture)
  @overload(NoneType, NoneType)
  @overload(QRhiTexture, QRhiTexture, QRhiTextureCopyDescription)
  @overload(QRhiTexture, NoneType, QRhiTextureCopyDescription)
  @overload(NoneType, QRhiTexture, QRhiTextureCopyDescription)
  @overload(NoneType, NoneType, QRhiTextureCopyDescription)
  def copyTexture(
      self,
      dst: Optional[QRhiTexture],
      src: Optional[QRhiTexture],
      desc: Optional[QRhiTextureCopyDescription] = None,
  ) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::copyTexture(QRhiTexture *dst,
    QRhiTexture *src, const QRhiTextureCopyDescription &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#copyTexture

    Parameters
    ----------

    dst : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    src : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    desc : Optional[QRhiTextureCopyDescription]
      Passed on as a value: Qt reads the C++ QRhiTextureCopyDescription,
      which stays Python's own. May be left out, as in Qt: a new
      'QRhiTextureCopyDescription()' is then passed on.
    """
    #  void QRhiResourceUpdateBatch::copyTexture(QRhiTexture *dst,
    #      QRhiTexture *src, const QRhiTextureCopyDescription &desc)
    if desc is None:
      from . import QRhiTextureCopyDescription
      desc = QRhiTextureCopyDescription()
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch11copyTextureEP11QRhiTextureS1_R'
        'K26QRhiTextureCopyDescription',
        self._addressOf(dst), self._addressOf(src), self._valueOf(desc),
    )

  @overload(QRhiReadbackDescription, QRhiReadbackResult)
  @overload(QRhiReadbackDescription, NoneType)
  def readBackTexture(
      self,
      rb: QRhiReadbackDescription,
      result: Optional[QRhiReadbackResult],
  ) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::readBackTexture(const
    QRhiReadbackDescription &rb, QRhiReadbackResult *result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#readBackTexture

    Parameters
    ----------

    rb : QRhiReadbackDescription
      Passed on as a value: Qt reads the C++ QRhiReadbackDescription, which
      stays Python's own.

    result : Optional[QRhiReadbackResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiResourceUpdateBatch::readBackTexture(const
    #      QRhiReadbackDescription &rb, QRhiReadbackResult *result)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch15readBackTextureERK23QRhiReadba'
        'ckDescriptionP18QRhiReadbackResult',
        self._valueOf(rb), self._addressOf(result),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def generateMips(self, tex: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatch::generateMips(QRhiTexture
    *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatch.html#generateMips

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiResourceUpdateBatch::generateMips(QRhiTexture *tex)
    self.uglySide.call(
        'ritual_ZN23QRhiResourceUpdateBatch12generateMipsEP11QRhiTexture',
        self._addressOf(tex),
    )
