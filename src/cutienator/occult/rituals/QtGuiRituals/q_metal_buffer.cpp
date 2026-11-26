//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMetalBuffer that Python can take functions over in. Every QMetalBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalBufferCall0)(const void *, int *);
typedef bool (*CuteQMetalBufferCall1)(const void *, int *);
typedef const QRhiBuffer::NativeBuffer * (*CuteQMetalBufferCall2)(const void *, int *);
typedef void * (*CuteQMetalBufferCall3)(const void *, int *);
typedef void (*CuteQMetalBufferCall4)(const void *, int *);
typedef int (*CuteQMetalBufferCall5)(const void *, int *);
typedef void (*CuteQMetalBufferCall6)(const void *, const void *, quint32, int *);
class CuteQMetalBuffer : public QMetalBuffer {
public:
  using QMetalBuffer::QMetalBuffer;
  void *taken[7] = {};

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
    if (!std::strcmp(key, "_ZN10QRhiBuffer43beginFullDynamicBufferUpdateForCurrentFrameEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer38fullDynamicBufferUpdateForCurrentFrameEPKvj")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QMetalBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalBufferCall0 call = reinterpret_cast<CuteQMetalBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalBuffer::destroy();
  }

  //  bool QMetalBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalBufferCall1 call = reinterpret_cast<CuteQMetalBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalBuffer::create();
  }

  //  QRhiBuffer::NativeBuffer QMetalBuffer::nativeBuffer()
  QRhiBuffer::NativeBuffer nativeBuffer() override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalBufferCall2 call = reinterpret_cast<CuteQMetalBufferCall2>(taken[2]);
      const QRhiBuffer::NativeBuffer * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMetalBuffer::nativeBuffer();
  }

  //  char *QMetalBuffer::beginFullDynamicBufferUpdateForCurrentFrame()
  char *beginFullDynamicBufferUpdateForCurrentFrame() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalBufferCall3 call = reinterpret_cast<CuteQMetalBufferCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<char *>(given);
    }
    return QMetalBuffer::beginFullDynamicBufferUpdateForCurrentFrame();
  }

  //  void QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame()
  void endFullDynamicBufferUpdateForCurrentFrame() override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalBufferCall4 call = reinterpret_cast<CuteQMetalBufferCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame();
  }

  //  QRhiResource::Type QRhiBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQMetalBufferCall5 call = reinterpret_cast<CuteQMetalBufferCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiBuffer::resourceType();
  }

  //  void QRhiBuffer::fullDynamicBufferUpdateForCurrentFrame(const void
  //      *data, quint32 size)
  void fullDynamicBufferUpdateForCurrentFrame(
      const void *data,
      quint32 size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMetalBufferCall6 call = reinterpret_cast<CuteQMetalBufferCall6>(taken[6]);
      call(this, data, size, &handled);
      if (handled) return;
    }
    QRhiBuffer::fullDynamicBufferUpdateForCurrentFrame(data, size);
  }
};

//  void QMetalBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMetalBuffer7destroyEv(QMetalBuffer *self) {
  self->destroy();
}

//  bool QMetalBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QMetalBuffer6createEv(QMetalBuffer *self) {
  return self->create();
}

//  QRhiBuffer::NativeBuffer QMetalBuffer::nativeBuffer()
extern "C" Q_DECL_EXPORT
QRhiBuffer::NativeBuffer *ritual_ZN12QMetalBuffer12nativeBufferEv(
    QMetalBuffer *self) {
  return new QRhiBuffer::NativeBuffer(self->nativeBuffer());
}

//  char *QMetalBuffer::beginFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
char *ritual_ZN12QMetalBuffer43beginFullDynamicBufferUpdateForCurrentFrameEv(
    QMetalBuffer *self) {
  return self->beginFullDynamicBufferUpdateForCurrentFrame();
}

//  void QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMetalBuffer41endFullDynamicBufferUpdateForCurrentFrameEv(
    QMetalBuffer *self) {
  self->endFullDynamicBufferUpdateForCurrentFrame();
}

//  a Python function taken by a CuteQMetalBuffer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalBuffer(
    QMetalBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalBuffer *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
