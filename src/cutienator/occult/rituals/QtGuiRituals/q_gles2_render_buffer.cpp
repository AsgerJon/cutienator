//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of 'qrhivulkan_p.h' also
//  stands under '__has_include(<vulkan/vulkan.h>)', as in Qt's
//  'qvulkaninstance.h', since that header uses the types of Vulkan's own
//  header, which a machine with Qt but without Vulkan's headers lacks;
//  the include of 'qrhid3d12_p.h' also stands under
//  '__has_include(<D3D12MemAlloc.h>)', since that header includes
//  'D3D12MemAlloc.h', which Qt's kit for Windows does not ship; no ritual
//  here needs either. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhi_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtGui/private/qrhinull_p.h>
#ifndef QT_NO_OPENGL
#include <QtGui/private/qrhigles2_p.h>
#endif
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#endif
#if defined(Q_OS_WIN) && __has_include(<D3D12MemAlloc.h>)
#include <QtGui/private/qrhid3d12_p.h>
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
#endif
#include <limits>
#include <memory>
#include <QtGui/private/qrhigles2_p.h>
#include <QtGui/QOffscreenSurface>
#include <QtGui/QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformopenglcontext.h>
#include <QtCore/qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 9043, as _ZNK18QRhiImplementation20effectiveSampleCountEi
inline int QRhiImplementation::effectiveSampleCount(int sampleCount) const
{
    // Stay compatible with QSurfaceFormat and friends where samples == 0 means the same as 1.
    const int s = qBound(1, sampleCount, 64);
    const QList<int> supported = supportedSampleCounts();
    int result = 1;

    // Stay compatible with Qt 5 in that requesting an unsupported sample count
    // is not an error (although we still do a categorized debug print about
    // this), and rather a supported value, preferably a close one, not just 1,
    // is used instead. This is actually deviating from Qt 5 as that performs a
    // clamping only and does not handle cases such as when sample count 2 is
    // not supported but 4 is. (OpenGL handles things like that gracefully,
    // other APIs may not, so improve this by picking the next largest, or in
    // absence of that, the largest value; this with the goal to not reduce
    // quality by rather picking a larger-than-requested value than a smaller one)

    for (int i = 0, ie = supported.count(); i != ie; ++i) {
        // assumes the 'supported' list is sorted
        if (supported[i] >= s) {
            result = supported[i];
            break;
        }
    }

    if (result != s) {
        if (result == 1 && !supported.isEmpty())
            result = supported.last();
        qCDebug(QRHI_LOG_INFO, "Attempted to set unsupported sample count %d, using %d instead",
                sampleCount, result);
    }

    return result;
}

//  from src/gui/rhi/qrhigles2.cpp, line 5998, as _ZN18QGles2RenderBufferD1Ev
inline QGles2RenderBuffer::~QGles2RenderBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6003, as _ZN18QGles2RenderBuffer7destroyEv
inline void QGles2RenderBuffer::destroy()
{
    if (!renderbuffer)
        return;

    QRhiGles2::DeferredReleaseEntry e;
    e.type = QRhiGles2::DeferredReleaseEntry::RenderBuffer;

    e.renderbuffer.renderbuffer = renderbuffer;
    e.renderbuffer.renderbuffer2 = stencilRenderbuffer;

    renderbuffer = 0;
    stencilRenderbuffer = 0;

    QRHI_RES_RHI(QRhiGles2);
    if (rhiD) {
        if (owns)
            rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 6118, as _ZN18QGles2RenderBuffer10createFromEN16QRhiRenderBuffer18NativeRenderBufferE
inline bool QGles2RenderBuffer::createFrom(NativeRenderBuffer src)
{
    if (!src.object)
        return false;

    if (renderbuffer)
        destroy();

    QRHI_RES_RHI(QRhiGles2);
    samples = rhiD->effectiveSampleCount(m_sampleCount);

    if (m_flags.testFlag(UsedWithSwapChainOnly))
        qWarning("RenderBuffer: UsedWithSwapChainOnly is meaningless when importing an existing native object");

    if (!rhiD->ensureContext())
        return false;

    renderbuffer = src.object;

    owns = false;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6143, as _ZNK18QGles2RenderBuffer13backingFormatEv
inline QRhiTexture::Format QGles2RenderBuffer::backingFormat() const
{
    if (m_backingFormatHint != QRhiTexture::UnknownFormat)
        return m_backingFormatHint;
    else
        return m_type == Color ? QRhiTexture::RGBA8 : QRhiTexture::UnknownFormat;
}
//  -----------------------------------------------------------------------

//  A QGles2RenderBuffer that Python can take functions over in. Every QGles2RenderBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2RenderBufferCall0)(const void *, int *);
typedef bool (*CuteQGles2RenderBufferCall1)(const void *, int *);
typedef bool (*CuteQGles2RenderBufferCall2)(const void *, const QRhiRenderBuffer::NativeRenderBuffer *, int *);
typedef int (*CuteQGles2RenderBufferCall3)(const void *, int *);
typedef int (*CuteQGles2RenderBufferCall4)(const void *, int *);
class CuteQGles2RenderBuffer : public QGles2RenderBuffer {
public:
  using QGles2RenderBuffer::QGles2RenderBuffer;
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
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderBuffer13backingFormatEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QGles2RenderBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2RenderBufferCall0 call = reinterpret_cast<CuteQGles2RenderBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2RenderBuffer::destroy();
  }

  //  bool QGles2RenderBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2RenderBufferCall1 call = reinterpret_cast<CuteQGles2RenderBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2RenderBuffer::create();
  }

  //  bool QGles2RenderBuffer::createFrom(NativeRenderBuffer src)
  bool createFrom(QRhiRenderBuffer::NativeRenderBuffer src) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2RenderBufferCall2 call = reinterpret_cast<CuteQGles2RenderBufferCall2>(taken[2]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QGles2RenderBuffer::createFrom(src);
  }

  //  QRhiTexture::Format QGles2RenderBuffer::backingFormat() const
  QRhiTexture::Format backingFormat() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2RenderBufferCall3 call = reinterpret_cast<CuteQGles2RenderBufferCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture::Format>(given);
    }
    return QGles2RenderBuffer::backingFormat();
  }

  //  QRhiResource::Type QRhiRenderBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGles2RenderBufferCall4 call = reinterpret_cast<CuteQGles2RenderBufferCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderBuffer::resourceType();
  }
};

//  QGles2RenderBuffer::~QGles2RenderBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGles2RenderBufferD1Ev(QGles2RenderBuffer *self) {
  delete self;
}

//  void QGles2RenderBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGles2RenderBuffer7destroyEv(QGles2RenderBuffer *self) {
  self->destroy();
}

//  bool QGles2RenderBuffer::createFrom(NativeRenderBuffer src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QGles2RenderBuffer10createFromEN16QRhiRenderBuffer18NativeRenderBufferE(
    QGles2RenderBuffer *self,
    const QRhiRenderBuffer::NativeRenderBuffer *src) {
  return self->createFrom(*src);
}

//  QRhiTexture::Format QGles2RenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK18QGles2RenderBuffer13backingFormatEv(
    const QGles2RenderBuffer *self) {
  return self->backingFormat();
}

//  a Python function taken by a CuteQGles2RenderBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2RenderBuffer(
    QGles2RenderBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2RenderBuffer *>(self)->take(key, call);
}

//  void QGles2RenderBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QGles2RenderBuffer7destroyEv(QGles2RenderBuffer *self) {
  self->QGles2RenderBuffer::destroy();
}

//  QRhiTexture::Format QGles2RenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_own_ZNK18QGles2RenderBuffer13backingFormatEv(
    const QGles2RenderBuffer *self) {
  return self->QGles2RenderBuffer::backingFormat();
}

#endif  // QT_CONFIG(opengl)
