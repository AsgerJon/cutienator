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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  QSSGRhiRenderableTextureV2::QSSGRhiRenderableTextureV2(const
//      std::shared_ptr<QSSGUserRenderPassManager> &manager, Private a1)
extern "C" Q_DECL_EXPORT
QSSGRhiRenderableTextureV2 *ritual_ZN26QSSGRhiRenderableTextureV2C1ERKSt10shared_ptrI25QSSGUserRenderPassManagerENS_7PrivateE(
    const std::shared_ptr<QSSGUserRenderPassManager> *manager,
    QSSGRhiRenderableTextureV2::Private a1) {
  return new QSSGRhiRenderableTextureV2(*manager, a1);
}

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

//  const QSSGManagedRhiTexturePtr
//      &QSSGRhiRenderableTextureV2::getDepthTexture() const
extern "C" Q_DECL_EXPORT
const QSSGManagedRhiTexturePtr *ritual_ZNK26QSSGRhiRenderableTextureV215getDepthTextureEv(
    const QSSGRhiRenderableTextureV2 *self) {
  return &(self->getDepthTexture());
}

//  const std::unique_ptr<QRhiRenderBuffer>
//      &QSSGRhiRenderableTextureV2::getDepthStencil() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QRhiRenderBuffer> *ritual_ZNK26QSSGRhiRenderableTextureV215getDepthStencilEv(
    const QSSGRhiRenderableTextureV2 *self) {
  return &(self->getDepthStencil());
}

//  const std::unique_ptr<QRhiRenderPassDescriptor>
//      &QSSGRhiRenderableTextureV2::getRenderPassDescriptor() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QRhiRenderPassDescriptor> *ritual_ZNK26QSSGRhiRenderableTextureV223getRenderPassDescriptorEv(
    const QSSGRhiRenderableTextureV2 *self) {
  return &(self->getRenderPassDescriptor());
}

//  const std::unique_ptr<QRhiTextureRenderTarget>
//      &QSSGRhiRenderableTextureV2::getRenderTarget() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QRhiTextureRenderTarget> *ritual_ZNK26QSSGRhiRenderableTextureV215getRenderTargetEv(
    const QSSGRhiRenderableTextureV2 *self) {
  return &(self->getRenderTarget());
}

//  size_t QSSGRhiRenderableTextureV2::colorAttachmentCount() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK26QSSGRhiRenderableTextureV220colorAttachmentCountEv(
    const QSSGRhiRenderableTextureV2 *self) {
  return self->colorAttachmentCount();
}

//  const QSSGManagedRhiTexturePtr
//      &QSSGRhiRenderableTextureV2::getColorTexture(int index) const
extern "C" Q_DECL_EXPORT
const QSSGManagedRhiTexturePtr *ritual_ZNK26QSSGRhiRenderableTextureV215getColorTextureEi(
    const QSSGRhiRenderableTextureV2 *self,
    int index) {
  return &(self->getColorTexture(index));
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
