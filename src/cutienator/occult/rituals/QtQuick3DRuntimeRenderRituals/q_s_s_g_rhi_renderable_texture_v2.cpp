//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#include <QtCore/qvariant.h>
#include <QtGui/private/qrhi_p.h>
#include <QtQuick3DUtils/private/qquick3dprofiler_p.h>
#include <QtQuick3DUtils/private/qssgmesh_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderableimage_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendermesh_p.h>
#include <QtQuick3DRuntimeRender/private/qssguserrenderpassmanager_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtGui/qquaternion.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/qssgrhicontext.cpp, line 1841, as _ZN26QSSGRhiRenderableTextureV2D1Ev
inline QSSGRhiRenderableTextureV2::~QSSGRhiRenderableTextureV2()
{
    for (auto &tex : textures)
        tex->invalidate();
}

//  from ../qtquick3d/src/runtimerender/qssgrhicontext.cpp, line 1856, as _ZN26QSSGRhiRenderableTextureV214setDescriptionEP4QRhi34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE
inline void QSSGRhiRenderableTextureV2::setDescription(QRhi *rhi, QRhiTextureRenderTargetDescription rtDesc, QRhiTextureRenderTarget::Flags flags)
{
    Q_ASSERT(rhi);

    textures.clear();
    const size_t colorAttachmentCount = rtDesc.colorAttachmentCount();
    for (size_t i = 0; i < colorAttachmentCount; ++i)
        textures.push_back(std::make_unique<QSSGManagedRhiTexture>(m_manager, rtDesc.colorAttachmentAt(i)->texture(), QSSGManagedRhiTexture::Private::Initialize));

    if (rtDesc.depthTexture()) {
        depthTexture = std::make_unique<QSSGManagedRhiTexture>(m_manager, rtDesc.depthTexture(), QSSGManagedRhiTexture::Private::Initialize);
        depthStencil.reset();
    } else if (rtDesc.depthStencilBuffer()) {
        depthStencil.reset(rtDesc.depthStencilBuffer());
        depthTexture.reset();
    } else {
        depthTexture.reset();
        depthStencil = nullptr;
    }

    dirty = ColorTextureDirty | DepthTextureDirty | DepthStencilDirty;

    rt.reset(rhi->newTextureRenderTarget(rtDesc));
    rt->setName(rtName);
    rt->setFlags(flags);
    rpDesc.reset(rt->newCompatibleRenderPassDescriptor());
    rt->setRenderPassDescriptor(rpDesc.get());
    if (!rt->create()) {
        qWarning("Failed to create renderable texture render target");
        rt.reset();
        return;
    }
}

//  from ../qtquick3d/src/runtimerender/qssgrhicontext.cpp, line 1890, as _ZN26QSSGRhiRenderableTextureV217resetRenderTargetEv
inline void QSSGRhiRenderableTextureV2::resetRenderTarget()
{
    rt.reset();
    rpDesc.reset();
}

//  from ../qtquick3d/src/runtimerender/qssgrhicontext.cpp, line 1896, as _ZN26QSSGRhiRenderableTextureV25resetEv
inline void QSSGRhiRenderableTextureV2::reset()
{
    if (rt)
        rt->setDescription({/* empty */});

    resetRenderTarget();

    textures.clear();

    depthStencil = nullptr;
    depthTexture.reset();
}

//  from ../qtquick3d/src/runtimerender/qssgrhicontext.cpp, line 1911, as _ZN26QSSGRhiRenderableTextureV210invalidateEv
inline void QSSGRhiRenderableTextureV2::invalidate()
{
    // NOTE: This does not delete the texture wrappers, just releases the underlying QRhiTexture.
    for (auto &tex : textures)
        tex->invalidate();

    if (depthTexture)
        depthTexture->invalidate();

    reset();
}
//  -----------------------------------------------------------------------

//  QSSGRhiRenderableTextureV2::~QSSGRhiRenderableTextureV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRhiRenderableTextureV2D1Ev(
    QSSGRhiRenderableTextureV2 *self) {
  delete self;
}

//  void QSSGRhiRenderableTextureV2::setDescription(QRhi *rhi,
//      QRhiTextureRenderTargetDescription rtDesc,
//      QRhiTextureRenderTarget::Flags a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRhiRenderableTextureV214setDescriptionEP4QRhi34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QSSGRhiRenderableTextureV2 *self,
    QRhi *rhi,
    const QRhiTextureRenderTargetDescription *rtDesc,
    int a2) {
  self->setDescription(
      rhi,
      *rtDesc,
      QFlags<QRhiTextureRenderTarget::Flag>::fromInt(a2));
}

//  void QSSGRhiRenderableTextureV2::setName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRhiRenderableTextureV27setNameERK10QByteArray(
    QSSGRhiRenderableTextureV2 *self,
    const QByteArray *name) {
  self->setName(*name);
}

//  const QByteArray &QSSGRhiRenderableTextureV2::getName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK26QSSGRhiRenderableTextureV27getNameEv(
    const QSSGRhiRenderableTextureV2 *self) {
  return new QByteArray(self->getName());
}

//  bool QSSGRhiRenderableTextureV2::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSSGRhiRenderableTextureV27isValidEv(
    const QSSGRhiRenderableTextureV2 *self) {
  return self->isValid();
}

//  void QSSGRhiRenderableTextureV2::resetRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRhiRenderableTextureV217resetRenderTargetEv(
    QSSGRhiRenderableTextureV2 *self) {
  self->resetRenderTarget();
}

//  void QSSGRhiRenderableTextureV2::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRhiRenderableTextureV25resetEv(
    QSSGRhiRenderableTextureV2 *self) {
  self->reset();
}

//  void QSSGRhiRenderableTextureV2::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRhiRenderableTextureV210invalidateEv(
    QSSGRhiRenderableTextureV2 *self) {
  self->invalidate();
}
