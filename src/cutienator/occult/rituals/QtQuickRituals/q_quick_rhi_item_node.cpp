//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrhiitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrhiitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickrhiitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickrhiitem.cpp, line 175, as _ZNK17QQuickRhiItemNode7textureEv
inline QSGTexture *QQuickRhiItemNode::texture() const
{
    return m_sgTexture.get();
}

//  from ../qtdeclarative/src/quick/items/qquickrhiitem.cpp, line 198, as _ZN17QQuickRhiItemNode4syncEv
inline void QQuickRhiItemNode::sync()
{
    if (!m_rhi) {
        m_rhi = m_window->rhi();
        if (!m_rhi) {
            qWarning("No QRhi found for window %p, QQuickRhiItem will not be functional", m_window);
            return;
        }
    }

    m_dpr = m_window->effectiveDevicePixelRatio();
    const int minTexSize = m_rhi->resourceLimit(QRhi::TextureSizeMin);
    const int maxTexSize = m_rhi->resourceLimit(QRhi::TextureSizeMax);

    QQuickRhiItemPrivate *itemD = m_item->d_func();
    QSize newSize = QSize(itemD->fixedTextureWidth, itemD->fixedTextureHeight);
    if (newSize.isEmpty())
        newSize = (QSizeF(m_item->width(), m_item->height()) * m_dpr).toSize();

    newSize.setWidth(qMin(maxTexSize, qMax(minTexSize, newSize.width())));
    newSize.setHeight(qMin(maxTexSize, qMax(minTexSize, newSize.height())));

    if (m_colorTexture) {
        if (m_colorTexture->format() != itemD->rhiTextureFormat
            || m_colorTexture->sampleCount() != itemD->samples)
        {
            resetColorBufferObjects();
            resetRenderTargetObjects();
        }
    }

    if (m_msaaColorBuffer) {
        if (m_msaaColorBuffer->backingFormat() != itemD->rhiTextureFormat
            || m_msaaColorBuffer->sampleCount() != itemD->samples)
        {
            resetColorBufferObjects();
            resetRenderTargetObjects();
        }
    }

    if (m_sgTexture && m_sgTexture->hasAlphaChannel() != itemD->blend) {
        resetColorBufferObjects();
        resetRenderTargetObjects();
    }

    if (!m_colorTexture && itemD->samples <= 1) {
        if (!m_rhi->isTextureFormatSupported(itemD->rhiTextureFormat)) {
            qWarning("QQuickRhiItem: The requested texture format (%d) is not supported by the "
                     "underlying 3D graphics API implementation", int(itemD->rhiTextureFormat));
        }
        m_colorTexture = m_rhi->newTexture(itemD->rhiTextureFormat, newSize, itemD->samples,
                                           QRhiTexture::RenderTarget | QRhiTexture::UsedAsTransferSource);
        if (!m_colorTexture->create()) {
            qWarning("Failed to create backing texture for QQuickRhiItem");
            delete m_colorTexture;
            m_colorTexture = nullptr;
            return;
        }
    }

    if (itemD->samples > 1) {
        if (!m_msaaColorBuffer) {
            if (!m_rhi->isFeatureSupported(QRhi::MultisampleRenderBuffer)) {
                qWarning("QQuickRhiItem: Multisample renderbuffers are reported as unsupported; "
                         "sample count %d will not work as expected", itemD->samples);
            }
            if (!m_rhi->isTextureFormatSupported(itemD->rhiTextureFormat)) {
                qWarning("QQuickRhiItem: The requested texture format (%d) is not supported by the "
                         "underlying 3D graphics API implementation", int(itemD->rhiTextureFormat));
            }
            m_msaaColorBuffer.reset(m_rhi->newRenderBuffer(QRhiRenderBuffer::Color, newSize, itemD->samples,
                                                           {}, itemD->rhiTextureFormat));
            if (!m_msaaColorBuffer->create()) {
                qWarning("Failed to create multisample color buffer for QQuickRhiItem");
                m_msaaColorBuffer.reset();
                return;
            }
        }
        if (!m_resolveTexture) {
            m_resolveTexture = m_rhi->newTexture(itemD->rhiTextureFormat, newSize, 1,
                                                 QRhiTexture::RenderTarget | QRhiTexture::UsedAsTransferSource);
            if (!m_resolveTexture->create()) {
                qWarning("Failed to create resolve texture for QQuickRhiItem");
                delete m_resolveTexture;
                m_resolveTexture = nullptr;
                return;
            }
        }
    } else if (m_resolveTexture) {
        m_resolveTexture->deleteLater();
        m_resolveTexture = nullptr;
    }

    if (m_colorTexture && m_colorTexture->pixelSize() != newSize) {
        m_colorTexture->setPixelSize(newSize);
        if (!m_colorTexture->create())
            qWarning("Failed to rebuild texture for QQuickRhiItem after resizing");
    }

    if (m_msaaColorBuffer && m_msaaColorBuffer->pixelSize() != newSize) {
        m_msaaColorBuffer->setPixelSize(newSize);
        if (!m_msaaColorBuffer->create())
            qWarning("Failed to rebuild multisample color buffer for QQuickRhiitem after resizing");
    }

    if (m_resolveTexture && m_resolveTexture->pixelSize() != newSize) {
        m_resolveTexture->setPixelSize(newSize);
        if (!m_resolveTexture->create())
            qWarning("Failed to rebuild resolve texture for QQuickRhiItem after resizing");
    }

    if (!m_sgTexture) {
        QQuickWindow::CreateTextureOptions options;
        if (itemD->blend)
            options |= QQuickWindow::TextureHasAlphaChannel;
        // the QSGTexture takes ownership of the QRhiTexture
        m_sgTexture.reset(m_window->createTextureFromRhiTexture(m_colorTexture ? m_colorTexture : m_resolveTexture,
                                                                options));
        setTexture(m_sgTexture.get());
    }

    if (itemD->autoRenderTarget) {
        const QSize pixelSize = m_colorTexture ? m_colorTexture->pixelSize()
                                               : m_msaaColorBuffer->pixelSize();
        if (!m_depthStencilBuffer) {
            m_depthStencilBuffer.reset(m_rhi->newRenderBuffer(QRhiRenderBuffer::DepthStencil, pixelSize, itemD->samples));
            if (!m_depthStencilBuffer->create()) {
                qWarning("Failed to create depth-stencil buffer for QQuickRhiItem");
                resetRenderTargetObjects();
                return;
            }
        } else if (m_depthStencilBuffer->pixelSize() != pixelSize) {
            m_depthStencilBuffer->setPixelSize(pixelSize);
            if (!m_depthStencilBuffer->create()) {
                qWarning("Failed to rebuild depth-stencil buffer for QQuickRhiItem with new size");
                return;
            }
        }
        if (!m_renderTarget) {
            QRhiColorAttachment color0;
            if (m_colorTexture)
                color0.setTexture(m_colorTexture);
            else
                color0.setRenderBuffer(m_msaaColorBuffer.get());
            if (itemD->samples > 1)
                color0.setResolveTexture(m_resolveTexture);
            QRhiTextureRenderTargetDescription rtDesc(color0, m_depthStencilBuffer.get());
            m_renderTarget.reset(m_rhi->newTextureRenderTarget(rtDesc));
            m_renderPassDescriptor.reset(m_renderTarget->newCompatibleRenderPassDescriptor());
            m_renderTarget->setRenderPassDescriptor(m_renderPassDescriptor.get());
            if (!m_renderTarget->create()) {
                qWarning("Failed to create render target for QQuickRhiitem");
                resetRenderTargetObjects();
                return;
            }
        }
    } else {
        resetRenderTargetObjects();
    }

    if (newSize != itemD->effectiveTextureSize) {
        itemD->effectiveTextureSize = newSize;
        emit m_item->effectiveColorBufferSizeChanged();
    }

    QRhiCommandBuffer *cb = queryCommandBuffer();
    if (cb)
        m_renderer->initialize(cb);

    m_renderer->synchronize(m_item);
}

//  from ../qtdeclarative/src/quick/items/qquickrhiitem.cpp, line 370, as _ZN17QQuickRhiItemNode18queryCommandBufferEv
inline QRhiCommandBuffer *QQuickRhiItemNode::queryCommandBuffer()
{
    QRhiSwapChain *swapchain = m_window->swapChain();
    QSGRendererInterface *rif = m_window->rendererInterface();

    // Handle both cases: on-screen QQuickWindow vs. off-screen QQuickWindow
    // e.g. by using QQuickRenderControl to redirect into a texture.
    QRhiCommandBuffer *cb = swapchain ? swapchain->currentFrameCommandBuffer()
                                      : static_cast<QRhiCommandBuffer *>(
                                          rif->getResource(m_window, QSGRendererInterface::RhiRedirectCommandBuffer));

    if (!cb) {
        qWarning("QQuickRhiItem: Neither swapchain nor redirected command buffer are available.");
        return nullptr;
    }

    return cb;
}

//  from ../qtdeclarative/src/quick/items/qquickrhiitem.cpp, line 180, as _ZN17QQuickRhiItemNode23resetColorBufferObjectsEv
inline void QQuickRhiItemNode::resetColorBufferObjects()
{
    // owns either m_colorTexture or m_resolveTexture
    m_sgTexture.reset();

    m_colorTexture = nullptr;
    m_resolveTexture = nullptr;

    m_msaaColorBuffer.reset();
}

//  from ../qtdeclarative/src/quick/items/qquickrhiitem.cpp, line 191, as _ZN17QQuickRhiItemNode24resetRenderTargetObjectsEv
inline void QQuickRhiItemNode::resetRenderTargetObjects()
{
    m_renderTarget.reset();
    m_renderPassDescriptor.reset();
    m_depthStencilBuffer.reset();
}

//  from ../qtdeclarative/src/quick/items/qquickrhiitem.cpp, line 389, as _ZN17QQuickRhiItemNode6renderEv
inline void QQuickRhiItemNode::render()
{
    // called before Qt Quick starts recording its main render pass

    if (!isValid() || !m_renderPending)
        return;

    QRhiCommandBuffer *cb = queryCommandBuffer();
    if (!cb)
        return;

    m_renderPending = false;
    m_renderer->render(cb);

    markDirty(QSGNode::DirtyMaterial);
    emit textureChanged();
}
//  -----------------------------------------------------------------------

//  A QQuickRhiItemNode that Python can take functions over in. Every QQuickRhiItemNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickRhiItemNodeCall0)(const void *, int *);
typedef bool (*CuteQQuickRhiItemNodeCall1)(const void *, int *);
typedef void (*CuteQQuickRhiItemNodeCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRhiItemNodeCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRhiItemNodeCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemNodeCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemNodeCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemNodeCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemNodeCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemNodeCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRhiItemNode : public QQuickRhiItemNode {
public:
  using QQuickRhiItemNode::QQuickRhiItemNode;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QSGTextureProvider7textureEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSGTexture *QQuickRhiItemNode::texture() const
  QSGTexture *texture() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall0 call = reinterpret_cast<CuteQQuickRhiItemNodeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QQuickRhiItemNode::texture();
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall1 call = reinterpret_cast<CuteQQuickRhiItemNodeCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall2 call = reinterpret_cast<CuteQQuickRhiItemNodeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall3 call = reinterpret_cast<CuteQQuickRhiItemNodeCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall4 call = reinterpret_cast<CuteQQuickRhiItemNodeCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall5 call = reinterpret_cast<CuteQQuickRhiItemNodeCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall6 call = reinterpret_cast<CuteQQuickRhiItemNodeCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall7 call = reinterpret_cast<CuteQQuickRhiItemNodeCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall8 call = reinterpret_cast<CuteQQuickRhiItemNodeCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRhiItemNodeCall9 call = reinterpret_cast<CuteQQuickRhiItemNodeCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRhiItemNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickRhiItemNode10metaObjectEv(
    const QQuickRhiItemNode *self) {
  return self->metaObject();
}

//  QSGTexture *QQuickRhiItemNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK17QQuickRhiItemNode7textureEv(
    const QQuickRhiItemNode *self) {
  return self->texture();
}

//  void QQuickRhiItemNode::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRhiItemNode4syncEv(QQuickRhiItemNode *self) {
  self->sync();
}

//  QRhiCommandBuffer *QQuickRhiItemNode::queryCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZN17QQuickRhiItemNode18queryCommandBufferEv(
    QQuickRhiItemNode *self) {
  return self->queryCommandBuffer();
}

//  void QQuickRhiItemNode::resetColorBufferObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRhiItemNode23resetColorBufferObjectsEv(
    QQuickRhiItemNode *self) {
  self->resetColorBufferObjects();
}

//  void QQuickRhiItemNode::resetRenderTargetObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRhiItemNode24resetRenderTargetObjectsEv(
    QQuickRhiItemNode *self) {
  self->resetRenderTargetObjects();
}

//  bool QQuickRhiItemNode::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickRhiItemNode7isValidEv(const QQuickRhiItemNode *self) {
  return self->isValid();
}

//  void QQuickRhiItemNode::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRhiItemNode14scheduleUpdateEv(
    QQuickRhiItemNode *self) {
  self->scheduleUpdate();
}

//  bool QQuickRhiItemNode::hasRenderer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickRhiItemNode11hasRendererEv(
    const QQuickRhiItemNode *self) {
  return self->hasRenderer();
}

//  void QQuickRhiItemNode::setRenderer(QQuickRhiItemRenderer *r)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRhiItemNode11setRendererEP21QQuickRhiItemRenderer(
    QQuickRhiItemNode *self,
    QQuickRhiItemRenderer *r) {
  self->setRenderer(r);
}

//  void QQuickRhiItemNode::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRhiItemNode6renderEv(QQuickRhiItemNode *self) {
  self->render();
}

//  QQuickRhiItemNode as the QSGSimpleTextureNode it is built on
extern "C" Q_DECL_EXPORT
QSGSimpleTextureNode *ritual_cast_QQuickRhiItemNode_QSGSimpleTextureNode(
    QQuickRhiItemNode *self) {
  return static_cast<QSGSimpleTextureNode *>(self);
}

//  a Python function taken by a CuteQQuickRhiItemNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRhiItemNode(
    QQuickRhiItemNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRhiItemNode *>(self)->take(key, call);
}

//  QSGTexture *QQuickRhiItemNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK17QQuickRhiItemNode7textureEv(
    const QQuickRhiItemNode *self) {
  return self->QQuickRhiItemNode::texture();
}
