//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from src/gui/rhi/qrhinull.cpp, line 660, as _ZN11QNullBuffer43beginFullDynamicBufferUpdateForCurrentFrameEv
inline char *QNullBuffer::beginFullDynamicBufferUpdateForCurrentFrame()
{
    Q_ASSERT(m_type == Dynamic);
    return data;
}

//  from src/gui/rhi/qrhinull.cpp, line 626, as _ZN11QNullBufferC1EP18QRhiImplementationN10QRhiBuffer4TypeE6QFlagsINS2_9UsageFlagEEj
inline QNullBuffer::QNullBuffer(QRhiImplementation *rhi, Type type, UsageFlags usage, quint32 size)
    : QRhiBuffer(rhi, type, usage, size)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 631, as _ZN11QNullBufferD1Ev
inline QNullBuffer::~QNullBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 636, as _ZN11QNullBuffer7destroyEv
inline void QNullBuffer::destroy()
{
    delete[] data;
    data = nullptr;

    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 646, as _ZN11QNullBuffer6createEv
inline bool QNullBuffer::create()
{
    if (data)
        destroy();

    data = new char[m_size];
    memset(data, 0, m_size);

    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(this);

    return true;
}
//  -----------------------------------------------------------------------

//  A QNullBuffer that Python can take functions over in. Every QNullBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullBufferCall0)(const void *, int *);
typedef bool (*CuteQNullBufferCall1)(const void *, int *);
typedef int (*CuteQNullBufferCall2)(const void *, int *);
typedef const QRhiBuffer::NativeBuffer * (*CuteQNullBufferCall3)(const void *, int *);
typedef void (*CuteQNullBufferCall4)(const void *, int *);
class CuteQNullBuffer : public QNullBuffer {
public:
  using QNullBuffer::QNullBuffer;
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
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer12nativeBufferEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QNullBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullBufferCall0 call = reinterpret_cast<CuteQNullBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullBuffer::destroy();
  }

  //  bool QNullBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullBufferCall1 call = reinterpret_cast<CuteQNullBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullBuffer::create();
  }

  //  QRhiResource::Type QRhiBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullBufferCall2 call = reinterpret_cast<CuteQNullBufferCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiBuffer::resourceType();
  }

  //  NativeBuffer QRhiBuffer::nativeBuffer()
  QRhiBuffer::NativeBuffer nativeBuffer() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullBufferCall3 call = reinterpret_cast<CuteQNullBufferCall3>(taken[3]);
      const QRhiBuffer::NativeBuffer * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiBuffer::nativeBuffer();
  }

  //  void QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame()
  void endFullDynamicBufferUpdateForCurrentFrame() override {
    if (taken[4]) {
      int handled = 0;
      CuteQNullBufferCall4 call = reinterpret_cast<CuteQNullBufferCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame();
  }
};

//  QNullBuffer::QNullBuffer(QRhiImplementation *rhi, Type type, UsageFlags
//      usage, quint32 size)
extern "C" Q_DECL_EXPORT
QNullBuffer *ritual_ZN11QNullBufferC1EP18QRhiImplementationN10QRhiBuffer4TypeE6QFlagsINS2_9UsageFlagEEj(
    QRhiImplementation *rhi,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return new CuteQNullBuffer(
      rhi,
      type,
      QFlags<QRhiBuffer::UsageFlag>::fromInt(usage),
      size);
}

//  QNullBuffer::~QNullBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNullBufferD1Ev(QNullBuffer *self) {
  delete self;
}

//  void QNullBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNullBuffer7destroyEv(QNullBuffer *self) {
  self->destroy();
}

//  bool QNullBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QNullBuffer6createEv(QNullBuffer *self) {
  return self->create();
}

//  a Python function taken by a CuteQNullBuffer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullBuffer(
    QNullBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullBuffer *>(self)->take(key, call);
}

//  void QNullBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QNullBuffer7destroyEv(QNullBuffer *self) {
  self->QNullBuffer::destroy();
}

//  bool QNullBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QNullBuffer6createEv(QNullBuffer *self) {
  return self->QNullBuffer::create();
}
