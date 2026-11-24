//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhigles2_p.h"
#include <QOffscreenSurface>
#include <QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <qpa/qplatformopenglcontext.h>
#include <qmath.h>
#include <limits>
#include "qrhi_p.h"
#include <qmath.h>
#include <QLoggingCategory>
#include "private/qloggingregistry_p.h"
#include "qrhinull_p.h"
#ifndef QT_NO_OPENGL
#include "qrhigles2_p.h"
#endif
#if QT_CONFIG(vulkan)
#endif
#ifdef Q_OS_WIN
#include "qrhid3d11_p.h"
#include "qrhid3d12_p.h"
#endif
#if QT_CONFIG(metal)
#include "qrhimetal_p.h"
#endif
#include <limits>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhigles2.cpp, line 6462, as _ZN26QGles2RenderPassDescriptorC1EP18QRhiImplementation
inline QGles2RenderPassDescriptor::QGles2RenderPassDescriptor(QRhiImplementation *rhi)
    : QRhiRenderPassDescriptor(rhi)
{
}

//  from src/gui/rhi/qrhi.cpp, line 8894, as _ZNK18QRhiImplementation25isStencilSupportingFormatEN11QRhiTexture6FormatE
inline bool QRhiImplementation::isStencilSupportingFormat(QRhiTexture::Format format) const
{
    switch (format) {
    case QRhiTexture::D24S8:
    case QRhiTexture::D32FS8:
        return true;
    default:
        break;
    }
    return false;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6537, as _ZN25QGles2TextureRenderTargetD1Ev
inline QGles2TextureRenderTarget::~QGles2TextureRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6542, as _ZN25QGles2TextureRenderTarget7destroyEv
inline void QGles2TextureRenderTarget::destroy()
{
    if (!framebuffer)
        return;

    QRhiGles2::DeferredReleaseEntry e;
    e.type = QRhiGles2::DeferredReleaseEntry::TextureRenderTarget;

    e.textureRenderTarget.framebuffer = framebuffer;
    e.textureRenderTarget.nonMsaaThrowawayDepthTexture = nonMsaaThrowawayDepthTexture;

    framebuffer = 0;
    nonMsaaThrowawayDepthTexture = 0;

    QRHI_RES_RHI(QRhiGles2);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 6839, as _ZNK25QGles2TextureRenderTarget9pixelSizeEv
inline QSize QGles2TextureRenderTarget::pixelSize() const
{
    if (!QRhiRenderTargetAttachmentTracker::isUpToDate<QGles2Texture, QGles2RenderBuffer>(m_desc, d.currentResIdList))
        const_cast<QGles2TextureRenderTarget *>(this)->create();

    return d.pixelSize;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6847, as _ZNK25QGles2TextureRenderTarget16devicePixelRatioEv
inline float QGles2TextureRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6852, as _ZNK25QGles2TextureRenderTarget11sampleCountEv
inline int QGles2TextureRenderTarget::sampleCount() const
{
    return d.sampleCount;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6563, as _ZN25QGles2TextureRenderTarget33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QGles2TextureRenderTarget::newCompatibleRenderPassDescriptor()
{
    QGles2RenderPassDescriptor *rpD = new QGles2RenderPassDescriptor(m_rhi);
    QRHI_RES_RHI(QRhiGles2);
    rhiD->registerResource(rpD, false);
    return rpD;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6571, as _ZN25QGles2TextureRenderTarget6createEv
inline bool QGles2TextureRenderTarget::create()
{
    QRHI_RES_RHI(QRhiGles2);

    if (framebuffer)
        destroy();

    const bool hasColorAttachments = m_desc.colorAttachmentCount() > 0;
    Q_ASSERT(hasColorAttachments || m_desc.depthTexture());
    Q_ASSERT(!m_desc.depthStencilBuffer() || !m_desc.depthTexture());
    const bool hasDepthStencil = m_desc.depthStencilBuffer() || m_desc.depthTexture();

    if (hasColorAttachments) {
        const int count = int(m_desc.colorAttachmentCount());
        if (count > rhiD->caps.maxDrawBuffers) {
            qWarning("QGles2TextureRenderTarget: Too many color attachments (%d, max is %d)",
                     count, rhiD->caps.maxDrawBuffers);
        }
    }
    if (m_desc.depthTexture() && !rhiD->caps.depthTexture)
        qWarning("QGles2TextureRenderTarget: Depth texture is not supported and will be ignored");

    if (!rhiD->ensureContext())
        return false;

    rhiD->f->glGenFramebuffers(1, &framebuffer);
    rhiD->f->glBindFramebuffer(GL_FRAMEBUFFER, framebuffer);

    d.colorAttCount = 0;
    int attIndex = 0;
    int multiViewCount = 0;
    for (auto it = m_desc.cbeginColorAttachments(), itEnd = m_desc.cendColorAttachments(); it != itEnd; ++it, ++attIndex) {
        d.colorAttCount += 1;
        const QRhiColorAttachment &colorAtt(*it);
        QRhiTexture *texture = colorAtt.texture();
        QRhiRenderBuffer *renderBuffer = colorAtt.renderBuffer();
        Q_ASSERT(texture || renderBuffer);
        if (texture) {
            QGles2Texture *texD = QRHI_RES(QGles2Texture, texture);
            Q_ASSERT(texD->texture && texD->specified);
            if (texD->flags().testFlag(QRhiTexture::ThreeDimensional) || texD->flags().testFlag(QRhiTexture::TextureArray)) {
                if (colorAtt.multiViewCount() < 2) {
                    rhiD->f->glFramebufferTextureLayer(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + uint(attIndex), texD->texture,
                                                       colorAtt.level(), colorAtt.layer());
                } else {
                    multiViewCount = colorAtt.multiViewCount();
                    if (texD->samples > 1 && rhiD->caps.glesMultiviewMultisampleRenderToTexture && colorAtt.resolveTexture()) {
                        // Special path for GLES and GL_OVR_multiview_multisampled_render_to_texture:
                        // ignore the color attachment's (multisample) texture
                        // array and give the resolve texture array to GL. (no
                        // explicit resolving is needed by us later on)
                        QGles2Texture *resolveTexD = QRHI_RES(QGles2Texture, colorAtt.resolveTexture());
                        rhiD->glFramebufferTextureMultisampleMultiviewOVR(GL_FRAMEBUFFER,
                                                                          GL_COLOR_ATTACHMENT0 + uint(attIndex),
                                                                          resolveTexD->texture,
                                                                          colorAtt.resolveLevel(),
                                                                          texD->samples,
                                                                          colorAtt.resolveLayer(),
                                                                          multiViewCount);
                    } else {
                        rhiD->glFramebufferTextureMultiviewOVR(GL_FRAMEBUFFER,
                                                               GL_COLOR_ATTACHMENT0 + uint(attIndex),
                                                               texD->texture,
                                                               colorAtt.level(),
                                                               colorAtt.layer(),
                                                               multiViewCount);
                    }
                }
            } else if (texD->flags().testFlag(QRhiTexture::OneDimensional)) {
                rhiD->glFramebufferTexture1D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + uint(attIndex),
                                             texD->target + uint(colorAtt.layer()), texD->texture,
                                             colorAtt.level());
            } else {
                if (texD->samples > 1 && rhiD->caps.glesMultisampleRenderToTexture && colorAtt.resolveTexture()) {
                    // Special path for GLES and GL_EXT_multisampled_render_to_texture:
                    // ignore the color attachment's (multisample) texture and
                    // give the resolve texture to GL. (no explicit resolving is
                    // needed by us later on)
                    QGles2Texture *resolveTexD = QRHI_RES(QGles2Texture, colorAtt.resolveTexture());
                    const GLenum faceTargetBase = resolveTexD->flags().testFlag(QRhiTexture::CubeMap) ? GL_TEXTURE_CUBE_MAP_POSITIVE_X : resolveTexD->target;
                    rhiD->glFramebufferTexture2DMultisampleEXT(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + uint(attIndex), faceTargetBase + uint(colorAtt.resolveLayer()),
                                                               resolveTexD->texture, colorAtt.level(), texD->samples);
                } else {
                    const GLenum faceTargetBase = texD->flags().testFlag(QRhiTexture::CubeMap) ? GL_TEXTURE_CUBE_MAP_POSITIVE_X : texD->target;
                    rhiD->f->glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + uint(attIndex), faceTargetBase + uint(colorAtt.layer()),
                                                    texD->texture, colorAtt.level());
                }
            }
            if (attIndex == 0) {
                d.pixelSize = rhiD->q->sizeForMipLevel(colorAtt.level(), texD->pixelSize());
                d.sampleCount = texD->samples;
            }
        } else if (renderBuffer) {
            QGles2RenderBuffer *rbD = QRHI_RES(QGles2RenderBuffer, renderBuffer);
            if (rbD->samples > 1 && rhiD->caps.glesMultisampleRenderToTexture && colorAtt.resolveTexture()) {
                // Special path for GLES and GL_EXT_multisampled_render_to_texture: ignore
                // the (multisample) renderbuffer and give the resolve texture to GL. (so
                // no explicit resolve; depending on GL implementation internals, this may
                // play nicer with tiled architectures)
                QGles2Texture *resolveTexD = QRHI_RES(QGles2Texture, colorAtt.resolveTexture());
                const GLenum faceTargetBase = resolveTexD->flags().testFlag(QRhiTexture::CubeMap) ? GL_TEXTURE_CUBE_MAP_POSITIVE_X : resolveTexD->target;
                rhiD->glFramebufferTexture2DMultisampleEXT(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + uint(attIndex), faceTargetBase + uint(colorAtt.resolveLayer()),
                                                           resolveTexD->texture, colorAtt.level(), rbD->samples);
            } else {
                rhiD->f->glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + uint(attIndex), GL_RENDERBUFFER, rbD->renderbuffer);
            }
            if (attIndex == 0) {
                d.pixelSize = rbD->pixelSize();
                d.sampleCount = rbD->samples;
            }
        }
    }

    if (hasDepthStencil) {
        if (m_desc.depthStencilBuffer()) {
            QGles2RenderBuffer *depthRbD = QRHI_RES(QGles2RenderBuffer, m_desc.depthStencilBuffer());
            if (rhiD->caps.needsDepthStencilCombinedAttach) {
                rhiD->f->glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, GL_RENDERBUFFER,
                                                   depthRbD->renderbuffer);
            } else {
                rhiD->f->glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER,
                                                   depthRbD->renderbuffer);
                if (depthRbD->stencilRenderbuffer) {
                    rhiD->f->glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_STENCIL_ATTACHMENT, GL_RENDERBUFFER,
                                                       depthRbD->stencilRenderbuffer);
                } else {
                    // packed depth-stencil
                    rhiD->f->glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_STENCIL_ATTACHMENT, GL_RENDERBUFFER,
                                                       depthRbD->renderbuffer);
                }
            }
            if (d.colorAttCount == 0) {
                d.pixelSize = depthRbD->pixelSize();
                d.sampleCount = depthRbD->samples;
            }
        } else {
            QGles2Texture *depthTexD = QRHI_RES(QGles2Texture, m_desc.depthTexture());
            if (multiViewCount < 2) {
                if (depthTexD->samples > 1 && rhiD->caps.glesMultisampleRenderToTexture && m_desc.depthResolveTexture()) {
                    // Special path for GLES and
                    // GL_EXT_multisampled_render_to_texture, for depth-stencil.
                    // Relevant only when depthResolveTexture is set.
                    QGles2Texture *depthResolveTexD = QRHI_RES(QGles2Texture, m_desc.depthResolveTexture());
                    rhiD->glFramebufferTexture2DMultisampleEXT(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, depthResolveTexD->target,
                                                               depthResolveTexD->texture, 0, depthTexD->samples);
                    if (rhiD->isStencilSupportingFormat(depthResolveTexD->format())) {
                        rhiD->glFramebufferTexture2DMultisampleEXT(GL_FRAMEBUFFER, GL_STENCIL_ATTACHMENT, depthResolveTexD->target,
                                                                   depthResolveTexD->texture, 0, depthTexD->samples);
                    }
                } else if (rhiD->caps.ctxMajor >= 3 && depthTexD->flags().testFlag(QRhiTexture::TextureArray) && m_desc.depthLayer() >= 0) {
                    rhiD->f->glFramebufferTextureLayer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, depthTexD->texture,
                                                       /*level*/0, m_desc.depthLayer());
                    if (rhiD->isStencilSupportingFormat(depthTexD->format())) {
                        rhiD->f->glFramebufferTextureLayer(GL_FRAMEBUFFER, GL_STENCIL_ATTACHMENT, depthTexD->texture,
                                                           /*level*/0, m_desc.depthLayer());
                    }
                } else {
                    rhiD->f->glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, depthTexD->target,
                                                    depthTexD->texture, 0);
                    if (rhiD->isStencilSupportingFormat(depthTexD->format())) {
                        rhiD->f->glFramebufferTexture2D(GL_FRAMEBUFFER, GL_STENCIL_ATTACHMENT, depthTexD->target,
                                                        depthTexD->texture, 0);
                    }
                }
            } else {
                if (depthTexD->samples > 1 && rhiD->caps.glesMultiviewMultisampleRenderToTexture) {
                    // And so it turns out
                    // https://registry.khronos.org/OpenGL/extensions/OVR/OVR_multiview.txt
                    // does not work with multisample 2D texture arrays. (at least
                    // that's what Issue 30 in the extension spec seems to imply)
                    //
                    // There is https://registry.khronos.org/OpenGL/extensions/EXT/EXT_multiview_texture_multisample.txt
                    // that seems to resolve that, but that does not seem to
                    // work (or not available) on GLES devices such as the Quest 3.
                    //
                    // So instead, on GLES we can use the
                    // multisample-multiview-auto-resolving version (which in
                    // turn is not supported on desktop GL e.g. by NVIDIA), too
                    // bad we have a multisample depth texture array here as
                    // every other API out there requires that. So, in absence
                    // of a depthResolveTexture, create a temporary one ignoring
                    // what the user has already created.
                    //
                    if (!m_flags.testFlag(DoNotStoreDepthStencilContents) && !m_desc.depthResolveTexture()) {
                        qWarning("Attempted to create a multiview+multisample QRhiTextureRenderTarget, but DoNotStoreDepthStencilContents was not set."
                                 " This path has no choice but to behave as if DoNotStoreDepthStencilContents was set, because QRhi is forced to create"
                                 " a throwaway non-multisample depth texture here. Set the flag to silence this warning, or set a depthResolveTexture.");
                    }
                    if (m_desc.depthResolveTexture()) {
                        QGles2Texture *depthResolveTexD = QRHI_RES(QGles2Texture, m_desc.depthResolveTexture());
                        rhiD->glFramebufferTextureMultisampleMultiviewOVR(GL_FRAMEBUFFER,
                                                                          GL_DEPTH_ATTACHMENT,
                                                                          depthResolveTexD->texture,
                                                                          0,
                                                                          depthTexD->samples,
                                                                          0,
                                                                          multiViewCount);
                        if (rhiD->isStencilSupportingFormat(depthResolveTexD->format())) {
                            rhiD->glFramebufferTextureMultisampleMultiviewOVR(GL_FRAMEBUFFER,
                                                                              GL_STENCIL_ATTACHMENT,
                                                                              depthResolveTexD->texture,
                                                                              0,
                                                                              depthTexD->samples,
                                                                              0,
                                                                              multiViewCount);
                        }
                    } else {
                        if (!nonMsaaThrowawayDepthTexture) {
                            rhiD->f->glGenTextures(1, &nonMsaaThrowawayDepthTexture);
                            rhiD->f->glBindTexture(GL_TEXTURE_2D_ARRAY, nonMsaaThrowawayDepthTexture);
                            rhiD->f->glTexStorage3D(GL_TEXTURE_2D_ARRAY, 1, GL_DEPTH24_STENCIL8,
                                                    depthTexD->pixelSize().width(), depthTexD->pixelSize().height(), multiViewCount);
                        }
                        rhiD->glFramebufferTextureMultisampleMultiviewOVR(GL_FRAMEBUFFER,
                                                                          GL_DEPTH_ATTACHMENT,
                                                                          nonMsaaThrowawayDepthTexture,
                                                                          0,
                                                                          depthTexD->samples,
                                                                          0,
                                                                          multiViewCount);
                        rhiD->glFramebufferTextureMultisampleMultiviewOVR(GL_FRAMEBUFFER,
                                                                          GL_STENCIL_ATTACHMENT,
                                                                          nonMsaaThrowawayDepthTexture,
                                                                          0,
                                                                          depthTexD->samples,
                                                                          0,
                                                                          multiViewCount);
                    }
                } else {
                    // The depth texture here must be an array with at least
                    // multiViewCount elements, and the format should be D24 or D32F
                    // for depth only, or D24S8 for depth and stencil.
                    rhiD->glFramebufferTextureMultiviewOVR(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, depthTexD->texture,
                                                           0, 0, multiViewCount);
                    if (rhiD->isStencilSupportingFormat(depthTexD->format())) {
                        rhiD->glFramebufferTextureMultiviewOVR(GL_FRAMEBUFFER, GL_STENCIL_ATTACHMENT, depthTexD->texture,
                                                               0, 0, multiViewCount);
                    }
                }
            }
            if (d.colorAttCount == 0) {
                d.pixelSize = depthTexD->pixelSize();
                d.sampleCount = depthTexD->samples;
            }
        }
        d.dsAttCount = 1;
    } else {
        d.dsAttCount = 0;
    }

    d.dpr = 1;
    d.rp = QRHI_RES(QGles2RenderPassDescriptor, m_renderPassDesc);

    GLenum status = rhiD->f->glCheckFramebufferStatus(GL_FRAMEBUFFER);
    if (status != GL_NO_ERROR && status != GL_FRAMEBUFFER_COMPLETE) {
        qWarning("Framebuffer incomplete: 0x%x", status);
        return false;
    }

    if (rhiD->glObjectLabel)
        rhiD->glObjectLabel(GL_FRAMEBUFFER, framebuffer, -1, m_objectName.constData());

    QRhiRenderTargetAttachmentTracker::updateResIdList<QGles2Texture, QGles2RenderBuffer>(m_desc, &d.currentResIdList);

    rhiD->registerResource(this);
    return true;
}
//  -----------------------------------------------------------------------

//  A QGles2TextureRenderTarget that Python can take functions over in. Every QGles2TextureRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2TextureRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQGles2TextureRenderTargetCall1)(const void *, int *);
typedef float (*CuteQGles2TextureRenderTargetCall2)(const void *, int *);
typedef int (*CuteQGles2TextureRenderTargetCall3)(const void *, int *);
typedef void * (*CuteQGles2TextureRenderTargetCall4)(const void *, int *);
typedef bool (*CuteQGles2TextureRenderTargetCall5)(const void *, int *);
typedef int (*CuteQGles2TextureRenderTargetCall6)(const void *, int *);
class CuteQGles2TextureRenderTarget : public QGles2TextureRenderTarget {
public:
  using QGles2TextureRenderTarget::QGles2TextureRenderTarget;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget9pixelSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget16devicePixelRatioEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget11sampleCountEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget33newCompatibleRenderPassDescriptorEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget6createEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QGles2TextureRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2TextureRenderTargetCall0 call = reinterpret_cast<CuteQGles2TextureRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2TextureRenderTarget::destroy();
  }

  //  QSize QGles2TextureRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2TextureRenderTargetCall1 call = reinterpret_cast<CuteQGles2TextureRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGles2TextureRenderTarget::pixelSize();
  }

  //  float QGles2TextureRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2TextureRenderTargetCall2 call = reinterpret_cast<CuteQGles2TextureRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2TextureRenderTarget::devicePixelRatio();
  }

  //  int QGles2TextureRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2TextureRenderTargetCall3 call = reinterpret_cast<CuteQGles2TextureRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2TextureRenderTarget::sampleCount();
  }

  //  QRhiRenderPassDescriptor
  //      *QGles2TextureRenderTarget::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGles2TextureRenderTargetCall4 call = reinterpret_cast<CuteQGles2TextureRenderTargetCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QGles2TextureRenderTarget::newCompatibleRenderPassDescriptor();
  }

  //  bool QGles2TextureRenderTarget::create()
  bool create() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGles2TextureRenderTargetCall5 call = reinterpret_cast<CuteQGles2TextureRenderTargetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2TextureRenderTarget::create();
  }

  //  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGles2TextureRenderTargetCall6 call = reinterpret_cast<CuteQGles2TextureRenderTargetCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTextureRenderTarget::resourceType();
  }
};

//  QGles2TextureRenderTarget::~QGles2TextureRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGles2TextureRenderTargetD1Ev(
    QGles2TextureRenderTarget *self) {
  delete self;
}

//  void QGles2TextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGles2TextureRenderTarget7destroyEv(
    QGles2TextureRenderTarget *self) {
  self->destroy();
}

//  QSize QGles2TextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK25QGles2TextureRenderTarget9pixelSizeEv(
    const QGles2TextureRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QGles2TextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QGles2TextureRenderTarget16devicePixelRatioEv(
    const QGles2TextureRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QGles2TextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QGles2TextureRenderTarget11sampleCountEv(
    const QGles2TextureRenderTarget *self) {
  return self->sampleCount();
}

//  QRhiRenderPassDescriptor
//      *QGles2TextureRenderTarget::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN25QGles2TextureRenderTarget33newCompatibleRenderPassDescriptorEv(
    QGles2TextureRenderTarget *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QGles2TextureRenderTarget::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QGles2TextureRenderTarget6createEv(
    QGles2TextureRenderTarget *self) {
  return self->create();
}

//  a Python function taken by a CuteQGles2TextureRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2TextureRenderTarget(
    QGles2TextureRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2TextureRenderTarget *>(self)->take(key, call);
}

//  void QGles2TextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGles2TextureRenderTarget7destroyEv(
    QGles2TextureRenderTarget *self) {
  self->QGles2TextureRenderTarget::destroy();
}

//  QSize QGles2TextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK25QGles2TextureRenderTarget9pixelSizeEv(
    const QGles2TextureRenderTarget *self) {
  return new QSize(self->QGles2TextureRenderTarget::pixelSize());
}

//  float QGles2TextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK25QGles2TextureRenderTarget16devicePixelRatioEv(
    const QGles2TextureRenderTarget *self) {
  return self->QGles2TextureRenderTarget::devicePixelRatio();
}

//  int QGles2TextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QGles2TextureRenderTarget11sampleCountEv(
    const QGles2TextureRenderTarget *self) {
  return self->QGles2TextureRenderTarget::sampleCount();
}
