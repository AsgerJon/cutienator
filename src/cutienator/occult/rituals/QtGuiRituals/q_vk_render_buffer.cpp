//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhivulkan_p.h>
#include <QtGui/qpa/qplatformvulkaninstance.h>
#include <QtCore/qmath.h>
#include <QtGui/qwindow.h>
#include <QtGui/private/qvulkandefaultinstance_p.h>
#include <QtCore/q20memory.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 6776, as _ZN10QRhiVulkan13setObjectNameEm12VkObjectTypeRK10QByteArrayi
inline void QRhiVulkan::setObjectName(uint64_t object, VkObjectType type, const QByteArray &name, int slot)
{
#ifdef VK_EXT_debug_utils
    if (!debugMarkers || !caps.debugUtils || name.isEmpty())
        return;

    VkDebugUtilsObjectNameInfoEXT nameInfo = {};
    nameInfo.sType = VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT;
    nameInfo.objectType = type;
    nameInfo.objectHandle = object;
    QByteArray decoratedName = name;
    if (slot >= 0) {
        decoratedName += '/';
        decoratedName += QByteArray::number(slot);
    }
    nameInfo.pObjectName = decoratedName.constData();
    vkSetDebugUtilsObjectNameEXT(dev, &nameInfo);
#else
    Q_UNUSED(object);
    Q_UNUSED(type);
    Q_UNUSED(name);
    Q_UNUSED(slot);
#endif
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7368, as _ZN15QVkRenderBufferD1Ev
inline QVkRenderBuffer::~QVkRenderBuffer()
{
    destroy();
    delete backingTexture;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7374, as _ZN15QVkRenderBuffer7destroyEv
inline void QVkRenderBuffer::destroy()
{
    if (!memory && !backingTexture)
        return;

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::RenderBuffer;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.renderBuffer.memory = memory;
    e.renderBuffer.image = image;
    e.renderBuffer.imageView = imageView;

    memory = VK_NULL_HANDLE;
    image = VK_NULL_HANDLE;
    imageView = VK_NULL_HANDLE;

    if (backingTexture) {
        Q_ASSERT(backingTexture->lastActiveFrameSlot == -1);
        backingTexture->lastActiveFrameSlot = e.lastActiveFrameSlot;
        backingTexture->destroy();
    }

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7404, as _ZN15QVkRenderBuffer6createEv
inline bool QVkRenderBuffer::create()
{
    if (memory || backingTexture)
        destroy();

    if (m_pixelSize.isEmpty())
        return false;

    QRHI_RES_RHI(QRhiVulkan);
    samples = rhiD->effectiveSampleCountBits(m_sampleCount);

    switch (m_type) {
    case QRhiRenderBuffer::Color:
    {
        if (!backingTexture) {
            backingTexture = QRHI_RES(QVkTexture, rhiD->createTexture(backingFormat(),
                                                                      m_pixelSize,
                                                                      1,
                                                                      0,
                                                                      m_sampleCount,
                                                                      QRhiTexture::RenderTarget | QRhiTexture::UsedAsTransferSource));
        } else {
            backingTexture->setPixelSize(m_pixelSize);
            backingTexture->setSampleCount(m_sampleCount);
        }
        backingTexture->setName(m_objectName);
        if (!backingTexture->create())
            return false;
        vkformat = backingTexture->vkformat;
    }
        break;
    case QRhiRenderBuffer::DepthStencil:
        vkformat = rhiD->optimalDepthStencilFormat();
        if (!rhiD->createTransientImage(vkformat,
                                        m_pixelSize,
                                        VK_IMAGE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT,
                                        VK_IMAGE_ASPECT_DEPTH_BIT | VK_IMAGE_ASPECT_STENCIL_BIT,
                                        samples,
                                        &memory,
                                        &image,
                                        &imageView,
                                        1))
        {
            return false;
        }
        rhiD->setObjectName(uint64_t(image), VK_OBJECT_TYPE_IMAGE, m_objectName);
        break;
    default:
        Q_UNREACHABLE();
        break;
    }

    lastActiveFrameSlot = -1;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7462, as _ZNK15QVkRenderBuffer13backingFormatEv
inline QRhiTexture::Format QVkRenderBuffer::backingFormat() const
{
    if (m_backingFormatHint != QRhiTexture::UnknownFormat)
        return m_backingFormatHint;
    else
        return m_type == Color ? QRhiTexture::RGBA8 : QRhiTexture::UnknownFormat;
}
//  -----------------------------------------------------------------------

//  A QVkRenderBuffer that Python can take functions over in. Every QVkRenderBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkRenderBufferCall0)(const void *, int *);
typedef bool (*CuteQVkRenderBufferCall1)(const void *, int *);
typedef int (*CuteQVkRenderBufferCall2)(const void *, int *);
typedef int (*CuteQVkRenderBufferCall3)(const void *, int *);
typedef bool (*CuteQVkRenderBufferCall4)(const void *, const QRhiRenderBuffer::NativeRenderBuffer *, int *);
class CuteQVkRenderBuffer : public QVkRenderBuffer {
public:
  using QVkRenderBuffer::QVkRenderBuffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderBuffer13backingFormatEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QVkRenderBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkRenderBufferCall0 call = reinterpret_cast<CuteQVkRenderBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkRenderBuffer::destroy();
  }

  //  bool QVkRenderBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkRenderBufferCall1 call = reinterpret_cast<CuteQVkRenderBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkRenderBuffer::create();
  }

  //  QRhiTexture::Format QVkRenderBuffer::backingFormat() const
  QRhiTexture::Format backingFormat() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkRenderBufferCall2 call = reinterpret_cast<CuteQVkRenderBufferCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture::Format>(given);
    }
    return QVkRenderBuffer::backingFormat();
  }

  //  QRhiResource::Type QRhiRenderBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkRenderBufferCall3 call = reinterpret_cast<CuteQVkRenderBufferCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderBuffer::resourceType();
  }

  //  bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)
  bool createFrom(QRhiRenderBuffer::NativeRenderBuffer src) override {
    if (taken[4]) {
      int handled = 0;
      CuteQVkRenderBufferCall4 call = reinterpret_cast<CuteQVkRenderBufferCall4>(taken[4]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QRhiRenderBuffer::createFrom(src);
  }
};

//  QVkRenderBuffer::~QVkRenderBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVkRenderBufferD1Ev(QVkRenderBuffer *self) {
  delete self;
}

//  void QVkRenderBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVkRenderBuffer7destroyEv(QVkRenderBuffer *self) {
  self->destroy();
}

//  bool QVkRenderBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QVkRenderBuffer6createEv(QVkRenderBuffer *self) {
  return self->create();
}

//  QRhiTexture::Format QVkRenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK15QVkRenderBuffer13backingFormatEv(
    const QVkRenderBuffer *self) {
  return self->backingFormat();
}

//  a Python function taken by a CuteQVkRenderBuffer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkRenderBuffer(
    QVkRenderBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkRenderBuffer *>(self)->take(key, call);
}

//  void QVkRenderBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QVkRenderBuffer7destroyEv(QVkRenderBuffer *self) {
  self->QVkRenderBuffer::destroy();
}

//  QRhiTexture::Format QVkRenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_own_ZNK15QVkRenderBuffer13backingFormatEv(
    const QVkRenderBuffer *self) {
  return self->QVkRenderBuffer::backingFormat();
}

#endif  // QT_CONFIG(vulkan)
