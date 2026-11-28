"""
QBackingStoreDefaultCompositor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qbackingstoredefaultcompositor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBackingStoreDefaultCompositor to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QBackingStoreDefaultCompositor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBackingStoreDefaultCompositor: a plain Python object
  standing in front of one C++ QBackingStoreDefaultCompositor.

  What exists
  -----------

  Every function of Qt's QBackingStoreDefaultCompositor that has a ritual and
  that Python can call so far, 1 name in all: 'reset'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBackingStoreDefaultCompositor::~QBackingStoreDefaultCompositor()':
    the destructor: Python never removes a C++
    QBackingStoreDefaultCompositor.
  - Qt's 'QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const
    QPlatformBackingStore *backingStore, QRhi *rhi, QRhiResourceUpdateBatch
    *resourceUpdates, const QRegion &dirtyRegion,
    QPlatformBackingStore::TextureFlags *flags) const': names
    'QPlatformBackingStore::TextureFlags', which has no cute class yet.
  - Qt's 'QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const QImage
    &image, QRhi *rhi, QRhiResourceUpdateBatch *resourceUpdates, const
    QRegion &dirtyRegion, QPlatformBackingStore::TextureFlags *flags) const':
    names 'QPlatformBackingStore::TextureFlags', which has no cute class yet.
  - Qt's 'void QBackingStoreDefaultCompositor::updateUniforms(PerQuadData *d,
    QRhiResourceUpdateBatch *resourceUpdates, const QMatrix4x4 &target, const
    QMatrix3x3 &source, UpdateUniformOptions options)': names
    'QBackingStoreDefaultCompositor::PerQuadData', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QBackingStoreDefaultCompositor is created at the first use, not
    by 'QBackingStoreDefaultCompositor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBackingStoreDefaultCompositor.
  - Each name of Qt's QBackingStoreDefaultCompositor that has no cute
    function yet, 'createPerQuadData', 'ensureResources', 'flush',
    'toTexture', 'updatePerQuadData', 'updateUniforms', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBackingStoreDefaultCompositor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def reset(self) -> None:
    """
    Calls Qt's 'void QBackingStoreDefaultCompositor::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstoredefaultcompositor.html#reset
    """
    #  void QBackingStoreDefaultCompositor::reset()
    self.uglySide.call('ritual_ZN30QBackingStoreDefaultCompositor5resetEv')

  @staticmethod
  def createPerQuadData(*__, **_) -> Never:
    """
    Qt's 'PerQuadData
    QBackingStoreDefaultCompositor::createPerQuadData(QRhiTexture *texture,
    QRhiTexture *textureExtra)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'UBUF_SIZE'.
    """
    raise NotImplementedError(
        "'QBackingStoreDefaultCompositor.createPerQuadData' has no cute "
        "function yet. Qt's 'PerQuadData "
        "QBackingStoreDefaultCompositor::createPerQuadData(QRhiTexture "
        "*texture, QRhiTexture *textureExtra)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'UBUF_SIZE'.")

  @staticmethod
  def ensureResources(*__, **_) -> Never:
    """
    Qt's 'void
    QBackingStoreDefaultCompositor::ensureResources(QRhiResourceUpdateBatch
    *resourceUpdates, QRhiRenderPassDescriptor *rpDesc)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'PipelineBlend'.
    """
    raise NotImplementedError(
        "'QBackingStoreDefaultCompositor.ensureResources' has no cute "
        "function yet. Qt's 'void "
        "QBackingStoreDefaultCompositor::ensureResources(QRhiResourceUpdateB"
        "atch *resourceUpdates, QRhiRenderPassDescriptor *rpDesc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'PipelineBlend'.")

  @staticmethod
  def flush(*__, **_) -> Never:
    """
    Qt's 'QPlatformBackingStore::FlushResult
    QBackingStoreDefaultCompositor::flush(QPlatformBackingStore
    *backingStore, QRhi *rhi, QRhiSwapChain *swapchain, QWindow *window,
    qreal sourceDevicePixelRatio, const QRegion &region, const QPoint
    &offset, QPlatformTextureList *textures, bool translucentBackground,
    qreal sourceTransformFactor)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'origin'.
    """
    raise NotImplementedError(
        "'QBackingStoreDefaultCompositor.flush' has no cute function yet. "
        "Qt's 'QPlatformBackingStore::FlushResult "
        "QBackingStoreDefaultCompositor::flush(QPlatformBackingStore "
        "*backingStore, QRhi *rhi, QRhiSwapChain *swapchain, QWindow "
        "*window, qreal sourceDevicePixelRatio, const QRegion &region, "
        "const QPoint &offset, QPlatformTextureList *textures, bool "
        "translucentBackground, qreal sourceTransformFactor)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'origin'.")

  @staticmethod
  def toTexture(*__, **_) -> Never:
    """
    - Qt's 'QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const
      QPlatformBackingStore *backingStore, QRhi *rhi, QRhiResourceUpdateBatch
      *resourceUpdates, const QRegion &dirtyRegion,
      QPlatformBackingStore::TextureFlags *flags) const': names
      'QPlatformBackingStore::TextureFlags', which has no cute class yet.
    - Qt's 'QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const
      QImage &image, QRhi *rhi, QRhiResourceUpdateBatch *resourceUpdates,
      const QRegion &dirtyRegion, QPlatformBackingStore::TextureFlags *flags)
      const': names 'QPlatformBackingStore::TextureFlags', which has no cute
      class yet.
    """
    raise NotImplementedError(
        "'QBackingStoreDefaultCompositor.toTexture' has no cute function "
        "yet. Qt's 'QRhiTexture "
        "*QBackingStoreDefaultCompositor::toTexture(const "
        "QPlatformBackingStore *backingStore, QRhi *rhi, "
        "QRhiResourceUpdateBatch *resourceUpdates, const QRegion "
        "&dirtyRegion, QPlatformBackingStore::TextureFlags *flags) const': "
        "names 'QPlatformBackingStore::TextureFlags', which has no cute "
        "class yet. Qt's 'QRhiTexture "
        "*QBackingStoreDefaultCompositor::toTexture(const QImage &image, "
        "QRhi *rhi, QRhiResourceUpdateBatch *resourceUpdates, const QRegion "
        "&dirtyRegion, QPlatformBackingStore::TextureFlags *flags) const': "
        "names 'QPlatformBackingStore::TextureFlags', which has no cute "
        "class yet.")

  @staticmethod
  def updatePerQuadData(*__, **_) -> Never:
    """
    Qt's 'void QBackingStoreDefaultCompositor::updatePerQuadData(PerQuadData
    *d, QRhiTexture *texture, QRhiTexture *textureExtra,
    UpdateQuadDataOptions options)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'UBUF_SIZE'.
    """
    raise NotImplementedError(
        "'QBackingStoreDefaultCompositor.updatePerQuadData' has no cute "
        "function yet. Qt's 'void "
        "QBackingStoreDefaultCompositor::updatePerQuadData(PerQuadData *d, "
        "QRhiTexture *texture, QRhiTexture *textureExtra, "
        "UpdateQuadDataOptions options)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'UBUF_SIZE'.")

  @staticmethod
  def updateUniforms(*__, **_) -> Never:
    """
    Qt's 'void QBackingStoreDefaultCompositor::updateUniforms(PerQuadData *d,
    QRhiResourceUpdateBatch *resourceUpdates, const QMatrix4x4 &target, const
    QMatrix3x3 &source, UpdateUniformOptions options)': names
    'QBackingStoreDefaultCompositor::PerQuadData', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QBackingStoreDefaultCompositor.updateUniforms' has no cute "
        "function yet. Qt's 'void "
        "QBackingStoreDefaultCompositor::updateUniforms(PerQuadData *d, "
        "QRhiResourceUpdateBatch *resourceUpdates, const QMatrix4x4 "
        "&target, const QMatrix3x3 &source, UpdateUniformOptions options)': "
        "names 'QBackingStoreDefaultCompositor::PerQuadData', which has no "
        "cute class yet.")
