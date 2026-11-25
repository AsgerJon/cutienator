//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the OpenGL headers of macOS lack
//  'GL_SHADER_STORAGE_BUFFER' and 'GL_BUFFER', which the code taken
//  from Qt for 'create' uses, so the file defines every constant of
//  that code that Qt's 'qrhigles2.cpp' defines for itself, with Qt's
//  own '#ifndef' lines and values. Kept as it is when the generator
//  runs again.
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  The constants Qt defines for itself where the OpenGL headers
//  lack them.
//  from src/gui/rhi/qrhigles2.cpp, line 337
#ifndef GL_SHADER_STORAGE_BUFFER
#define GL_SHADER_STORAGE_BUFFER          0x90D2
#endif
//  from src/gui/rhi/qrhigles2.cpp, line 417
#ifndef GL_MAP_WRITE_BIT
#define GL_MAP_WRITE_BIT                  0x0002
#endif
//  from src/gui/rhi/qrhigles2.cpp, line 421
#ifndef GL_MAP_INVALIDATE_BUFFER_BIT
#define GL_MAP_INVALIDATE_BUFFER_BIT      0x0008
#endif
//  from src/gui/rhi/qrhigles2.cpp, line 589
#ifndef GL_BUFFER
#define GL_BUFFER                         0x82E0
#endif
//  from src/gui/rhi/qrhigles2.cpp, line 601
#ifndef GL_DRAW_INDIRECT_BUFFER
#define GL_DRAW_INDIRECT_BUFFER           0x8F3F
#endif

//  from src/gui/rhi/qrhigles2.cpp, line 5979, as _ZN12QGles2Buffer38fullDynamicBufferUpdateForCurrentFrameEPKvj
inline void QGles2Buffer::fullDynamicBufferUpdateForCurrentFrame(const void *bufferData, quint32 size)
{
    const quint32 copySize = size > 0 ? size : m_size;
    if (!m_usage.testFlag(UniformBuffer)) {
        QRHI_RES_RHI(QRhiGles2);
        rhiD->f->glBindBuffer(targetForDataOps, buffer);
        rhiD->f->glBufferSubData(targetForDataOps, 0, copySize, bufferData);
    } else {
        memcpy(data.data(), bufferData, copySize);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 5949, as _ZN12QGles2Buffer43beginFullDynamicBufferUpdateForCurrentFrameEv
inline char *QGles2Buffer::beginFullDynamicBufferUpdateForCurrentFrame()
{
    Q_ASSERT(m_type == Dynamic);
    if (!m_usage.testFlag(UniformBuffer)) {
        QRHI_RES_RHI(QRhiGles2);
        rhiD->f->glBindBuffer(targetForDataOps, buffer);
        if (rhiD->caps.properMapBuffer) {
            return static_cast<char *>(rhiD->f->glMapBufferRange(targetForDataOps, 0, nonZeroSize,
                                                                 GL_MAP_WRITE_BIT | GL_MAP_INVALIDATE_BUFFER_BIT));
        } else {
            // Need some storage for the data, use the otherwise unused 'data' member.
            if (data.isEmpty())
                data.resize(nonZeroSize);
        }
    }
    return data.data();
}

//  from src/gui/rhi/qrhigles2.cpp, line 5875, as _ZN12QGles2BufferD1Ev
inline QGles2Buffer::~QGles2Buffer()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 5880, as _ZN12QGles2Buffer7destroyEv
inline void QGles2Buffer::destroy()
{
    data.clear();
    if (!buffer)
        return;

    QRhiGles2::DeferredReleaseEntry e;
    e.type = QRhiGles2::DeferredReleaseEntry::Buffer;

    e.buffer.buffer = buffer;
    buffer = 0;

    QRHI_RES_RHI(QRhiGles2);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 5899, as _ZN12QGles2Buffer6createEv
inline bool QGles2Buffer::create()
{
    if (buffer)
        destroy();

    QRHI_RES_RHI(QRhiGles2);

    nonZeroSize = m_size <= 0 ? 256 : m_size;

    if (m_usage.testFlag(QRhiBuffer::UniformBuffer)) {
        if (int(m_usage) != QRhiBuffer::UniformBuffer) {
            qWarning("Uniform buffer: multiple usages specified, this is not supported by the OpenGL backend");
            return false;
        }
        data.resize(nonZeroSize);
        return true;
    }

    if (!rhiD->ensureContext())
        return false;

    targetForDataOps = GL_ARRAY_BUFFER;
    if (m_usage.testFlag(QRhiBuffer::IndexBuffer))
        targetForDataOps = GL_ELEMENT_ARRAY_BUFFER;
    else if (m_usage.testFlag(QRhiBuffer::StorageBuffer))
        targetForDataOps = GL_SHADER_STORAGE_BUFFER;
    else if (m_usage.testFlag(QRhiBuffer::IndirectBuffer))
        targetForDataOps = GL_DRAW_INDIRECT_BUFFER;

    rhiD->f->glGenBuffers(1, &buffer);
    rhiD->f->glBindBuffer(targetForDataOps, buffer);
    rhiD->f->glBufferData(targetForDataOps, nonZeroSize, nullptr, m_type == Dynamic ? GL_DYNAMIC_DRAW : GL_STATIC_DRAW);

    if (rhiD->glObjectLabel)
        rhiD->glObjectLabel(GL_BUFFER, buffer, -1, m_objectName.constData());

    usageState.access = AccessNone;

    rhiD->registerResource(this);
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 5941, as _ZN12QGles2Buffer12nativeBufferEv
inline QRhiBuffer::NativeBuffer QGles2Buffer::nativeBuffer()
{
    if (m_usage.testFlag(QRhiBuffer::UniformBuffer))
        return { {}, 0 };

    return { { &buffer }, 1 };
}

//  from src/gui/rhi/qrhigles2.cpp, line 5967, as _ZN12QGles2Buffer41endFullDynamicBufferUpdateForCurrentFrameEv
inline void QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame()
{
    if (!m_usage.testFlag(UniformBuffer)) {
        QRHI_RES_RHI(QRhiGles2);
        rhiD->f->glBindBuffer(targetForDataOps, buffer);
        if (rhiD->caps.properMapBuffer)
            rhiD->f->glUnmapBuffer(targetForDataOps);
        else
            rhiD->f->glBufferSubData(targetForDataOps, 0, nonZeroSize, data.data());
    }
}
//  -----------------------------------------------------------------------

//  A QGles2Buffer that Python can take functions over in. Every QGles2Buffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2BufferCall0)(const void *, int *);
typedef bool (*CuteQGles2BufferCall1)(const void *, int *);
typedef const QRhiBuffer::NativeBuffer * (*CuteQGles2BufferCall2)(const void *, int *);
typedef void (*CuteQGles2BufferCall3)(const void *, int *);
typedef int (*CuteQGles2BufferCall4)(const void *, int *);
class CuteQGles2Buffer : public QGles2Buffer {
public:
  using QGles2Buffer::QGles2Buffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer12nativeBufferEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QGles2Buffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2BufferCall0 call = reinterpret_cast<CuteQGles2BufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2Buffer::destroy();
  }

  //  bool QGles2Buffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2BufferCall1 call = reinterpret_cast<CuteQGles2BufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2Buffer::create();
  }

  //  QRhiBuffer::NativeBuffer QGles2Buffer::nativeBuffer()
  QRhiBuffer::NativeBuffer nativeBuffer() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2BufferCall2 call = reinterpret_cast<CuteQGles2BufferCall2>(taken[2]);
      const QRhiBuffer::NativeBuffer * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGles2Buffer::nativeBuffer();
  }

  //  void QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame()
  void endFullDynamicBufferUpdateForCurrentFrame() override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2BufferCall3 call = reinterpret_cast<CuteQGles2BufferCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame();
  }

  //  QRhiResource::Type QRhiBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGles2BufferCall4 call = reinterpret_cast<CuteQGles2BufferCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiBuffer::resourceType();
  }
};

//  QGles2Buffer::~QGles2Buffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGles2BufferD1Ev(QGles2Buffer *self) {
  delete self;
}

//  void QGles2Buffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGles2Buffer7destroyEv(QGles2Buffer *self) {
  self->destroy();
}

//  bool QGles2Buffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QGles2Buffer6createEv(QGles2Buffer *self) {
  return self->create();
}

//  QRhiBuffer::NativeBuffer QGles2Buffer::nativeBuffer()
extern "C" Q_DECL_EXPORT
QRhiBuffer::NativeBuffer *ritual_ZN12QGles2Buffer12nativeBufferEv(
    QGles2Buffer *self) {
  return new QRhiBuffer::NativeBuffer(self->nativeBuffer());
}

//  void QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGles2Buffer41endFullDynamicBufferUpdateForCurrentFrameEv(
    QGles2Buffer *self) {
  self->endFullDynamicBufferUpdateForCurrentFrame();
}

//  a Python function taken by a CuteQGles2Buffer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2Buffer(
    QGles2Buffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2Buffer *>(self)->take(key, call);
}

//  void QGles2Buffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGles2Buffer7destroyEv(QGles2Buffer *self) {
  self->QGles2Buffer::destroy();
}

//  QRhiBuffer::NativeBuffer QGles2Buffer::nativeBuffer()
extern "C" Q_DECL_EXPORT
QRhiBuffer::NativeBuffer *ritual_own_ZN12QGles2Buffer12nativeBufferEv(
    QGles2Buffer *self) {
  return new QRhiBuffer::NativeBuffer(self->QGles2Buffer::nativeBuffer());
}

//  void QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGles2Buffer41endFullDynamicBufferUpdateForCurrentFrameEv(
    QGles2Buffer *self) {
  self->QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame();
}

#endif  // QT_CONFIG(opengl)
