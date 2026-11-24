//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhinull.cpp, line 811, as _ZN25QNullRenderPassDescriptorC1EP18QRhiImplementation
inline QNullRenderPassDescriptor::QNullRenderPassDescriptor(QRhiImplementation *rhi)
    : QRhiRenderPassDescriptor(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 885, as _ZN24QNullTextureRenderTargetD1Ev
inline QNullTextureRenderTarget::~QNullTextureRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 890, as _ZN24QNullTextureRenderTarget7destroyEv
inline void QNullTextureRenderTarget::destroy()
{
    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 924, as _ZNK24QNullTextureRenderTarget9pixelSizeEv
inline QSize QNullTextureRenderTarget::pixelSize() const
{
    if (!QRhiRenderTargetAttachmentTracker::isUpToDate<QNullTexture, QNullRenderBuffer>(m_desc, d.currentResIdList))
        const_cast<QNullTextureRenderTarget *>(this)->create();

    return d.pixelSize;
}

//  from src/gui/rhi/qrhinull.cpp, line 932, as _ZNK24QNullTextureRenderTarget16devicePixelRatioEv
inline float QNullTextureRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhinull.cpp, line 937, as _ZNK24QNullTextureRenderTarget11sampleCountEv
inline int QNullTextureRenderTarget::sampleCount() const
{
    return 1;
}

//  from src/gui/rhi/qrhinull.cpp, line 897, as _ZN24QNullTextureRenderTarget33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QNullTextureRenderTarget::newCompatibleRenderPassDescriptor()
{
    QNullRenderPassDescriptor *rpD = new QNullRenderPassDescriptor(m_rhi);
    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(rpD, false);
    return rpD;
}

//  from src/gui/rhi/qrhinull.cpp, line 905, as _ZN24QNullTextureRenderTarget6createEv
inline bool QNullTextureRenderTarget::create()
{
    QRHI_RES_RHI(QRhiNull);
    d.rp = QRHI_RES(QNullRenderPassDescriptor, m_renderPassDesc);
    if (m_desc.cbeginColorAttachments() != m_desc.cendColorAttachments()) {
        const QRhiColorAttachment *colorAtt = m_desc.cbeginColorAttachments();
        QRhiTexture *tex = colorAtt->texture();
        QRhiRenderBuffer *rb = colorAtt->renderBuffer();
        d.pixelSize = tex ? rhiD->q->sizeForMipLevel(colorAtt->level(), tex->pixelSize()) : rb->pixelSize();
    } else if (m_desc.depthStencilBuffer()) {
        d.pixelSize = m_desc.depthStencilBuffer()->pixelSize();
    } else if (m_desc.depthTexture()) {
        d.pixelSize = m_desc.depthTexture()->pixelSize();
    }
    QRhiRenderTargetAttachmentTracker::updateResIdList<QNullTexture, QNullRenderBuffer>(m_desc, &d.currentResIdList);
    rhiD->registerResource(this);
    return true;
}
//  -----------------------------------------------------------------------

//  A QNullTextureRenderTarget that Python can take functions over in. Every QNullTextureRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullTextureRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQNullTextureRenderTargetCall1)(const void *, int *);
typedef float (*CuteQNullTextureRenderTargetCall2)(const void *, int *);
typedef int (*CuteQNullTextureRenderTargetCall3)(const void *, int *);
typedef void * (*CuteQNullTextureRenderTargetCall4)(const void *, int *);
typedef bool (*CuteQNullTextureRenderTargetCall5)(const void *, int *);
typedef int (*CuteQNullTextureRenderTargetCall6)(const void *, int *);
class CuteQNullTextureRenderTarget : public QNullTextureRenderTarget {
public:
  using QNullTextureRenderTarget::QNullTextureRenderTarget;
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

  //  void QNullTextureRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullTextureRenderTargetCall0 call = reinterpret_cast<CuteQNullTextureRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullTextureRenderTarget::destroy();
  }

  //  QSize QNullTextureRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullTextureRenderTargetCall1 call = reinterpret_cast<CuteQNullTextureRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNullTextureRenderTarget::pixelSize();
  }

  //  float QNullTextureRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullTextureRenderTargetCall2 call = reinterpret_cast<CuteQNullTextureRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QNullTextureRenderTarget::devicePixelRatio();
  }

  //  int QNullTextureRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullTextureRenderTargetCall3 call = reinterpret_cast<CuteQNullTextureRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QNullTextureRenderTarget::sampleCount();
  }

  //  QRhiRenderPassDescriptor
  //      *QNullTextureRenderTarget::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[4]) {
      int handled = 0;
      CuteQNullTextureRenderTargetCall4 call = reinterpret_cast<CuteQNullTextureRenderTargetCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QNullTextureRenderTarget::newCompatibleRenderPassDescriptor();
  }

  //  bool QNullTextureRenderTarget::create()
  bool create() override {
    if (taken[5]) {
      int handled = 0;
      CuteQNullTextureRenderTargetCall5 call = reinterpret_cast<CuteQNullTextureRenderTargetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullTextureRenderTarget::create();
  }

  //  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQNullTextureRenderTargetCall6 call = reinterpret_cast<CuteQNullTextureRenderTargetCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTextureRenderTarget::resourceType();
  }
};

//  QNullTextureRenderTarget::~QNullTextureRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNullTextureRenderTargetD1Ev(
    QNullTextureRenderTarget *self) {
  delete self;
}

//  void QNullTextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNullTextureRenderTarget7destroyEv(
    QNullTextureRenderTarget *self) {
  self->destroy();
}

//  QSize QNullTextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK24QNullTextureRenderTarget9pixelSizeEv(
    const QNullTextureRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QNullTextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QNullTextureRenderTarget16devicePixelRatioEv(
    const QNullTextureRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QNullTextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QNullTextureRenderTarget11sampleCountEv(
    const QNullTextureRenderTarget *self) {
  return self->sampleCount();
}

//  QRhiRenderPassDescriptor
//      *QNullTextureRenderTarget::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN24QNullTextureRenderTarget33newCompatibleRenderPassDescriptorEv(
    QNullTextureRenderTarget *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QNullTextureRenderTarget::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QNullTextureRenderTarget6createEv(
    QNullTextureRenderTarget *self) {
  return self->create();
}

//  a Python function taken by a CuteQNullTextureRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullTextureRenderTarget(
    QNullTextureRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullTextureRenderTarget *>(self)->take(key, call);
}

//  void QNullTextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QNullTextureRenderTarget7destroyEv(
    QNullTextureRenderTarget *self) {
  self->QNullTextureRenderTarget::destroy();
}

//  QSize QNullTextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK24QNullTextureRenderTarget9pixelSizeEv(
    const QNullTextureRenderTarget *self) {
  return new QSize(self->QNullTextureRenderTarget::pixelSize());
}

//  float QNullTextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK24QNullTextureRenderTarget16devicePixelRatioEv(
    const QNullTextureRenderTarget *self) {
  return self->QNullTextureRenderTarget::devicePixelRatio();
}

//  int QNullTextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QNullTextureRenderTarget11sampleCountEv(
    const QNullTextureRenderTarget *self) {
  return self->QNullTextureRenderTarget::sampleCount();
}

//  bool QNullTextureRenderTarget::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QNullTextureRenderTarget6createEv(
    QNullTextureRenderTarget *self) {
  return self->QNullTextureRenderTarget::create();
}
