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
typedef void (*CuteQMetalBufferCall3)(const void *, int *);
typedef int (*CuteQMetalBufferCall4)(const void *, int *);
class CuteQMetalBuffer : public QMetalBuffer {
public:
  using QMetalBuffer::QMetalBuffer;
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

  //  void QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame()
  void endFullDynamicBufferUpdateForCurrentFrame() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalBufferCall3 call = reinterpret_cast<CuteQMetalBufferCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame();
  }

  //  QRhiResource::Type QRhiBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalBufferCall4 call = reinterpret_cast<CuteQMetalBufferCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiBuffer::resourceType();
  }
};

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
