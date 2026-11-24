//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QRhiBuffer that Python can take functions over in. Every QRhiBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiBufferCall0)(const void *, int *);
typedef bool (*CuteQRhiBufferCall1)(const void *, int *);
typedef const QRhiBuffer::NativeBuffer * (*CuteQRhiBufferCall2)(const void *, int *);
typedef void (*CuteQRhiBufferCall3)(const void *, int *);
typedef void (*CuteQRhiBufferCall4)(const void *, int *);
class CuteQRhiBuffer : public QRhiBuffer {
public:
  using QRhiBuffer::QRhiBuffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
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
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiBufferCall0 call = reinterpret_cast<CuteQRhiBufferCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiBuffer::resourceType();
  }

  //  bool QRhiBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiBufferCall1 call = reinterpret_cast<CuteQRhiBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  NativeBuffer QRhiBuffer::nativeBuffer()
  QRhiBuffer::NativeBuffer nativeBuffer() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiBufferCall2 call = reinterpret_cast<CuteQRhiBufferCall2>(taken[2]);
      const QRhiBuffer::NativeBuffer * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiBuffer::nativeBuffer();
  }

  //  void QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame()
  void endFullDynamicBufferUpdateForCurrentFrame() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiBufferCall3 call = reinterpret_cast<CuteQRhiBufferCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame();
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiBufferCall4 call = reinterpret_cast<CuteQRhiBufferCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiBuffer::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK10QRhiBuffer12resourceTypeEv(
    const QRhiBuffer *self) {
  return self->resourceType();
}

//  Type QRhiBuffer::type() const
extern "C" Q_DECL_EXPORT
QRhiBuffer::Type ritual_ZNK10QRhiBuffer4typeEv(const QRhiBuffer *self) {
  return self->type();
}

//  void QRhiBuffer::setType(Type t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiBuffer7setTypeENS_4TypeE(
    QRhiBuffer *self,
    QRhiBuffer::Type t) {
  self->setType(t);
}

//  UsageFlags QRhiBuffer::usage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QRhiBuffer5usageEv(const QRhiBuffer *self) {
  return static_cast<int>(self->usage().toInt());
}

//  void QRhiBuffer::setUsage(UsageFlags u)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiBuffer8setUsageE6QFlagsINS_9UsageFlagEE(
    QRhiBuffer *self,
    int u) {
  self->setUsage(QFlags<QRhiBuffer::UsageFlag>::fromInt(u));
}

//  quint32 QRhiBuffer::size() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK10QRhiBuffer4sizeEv(const QRhiBuffer *self) {
  return self->size();
}

//  void QRhiBuffer::setSize(quint32 sz)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiBuffer7setSizeEj(QRhiBuffer *self, quint32 sz) {
  self->setSize(sz);
}

//  bool QRhiBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QRhiBuffer6createEv(QRhiBuffer *self) {
  return self->create();
}

//  NativeBuffer QRhiBuffer::nativeBuffer()
extern "C" Q_DECL_EXPORT
QRhiBuffer::NativeBuffer *ritual_ZN10QRhiBuffer12nativeBufferEv(
    QRhiBuffer *self) {
  return new QRhiBuffer::NativeBuffer(self->nativeBuffer());
}

//  void QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv(
    QRhiBuffer *self) {
  self->endFullDynamicBufferUpdateForCurrentFrame();
}

//  a Python function taken by a CuteQRhiBuffer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiBuffer(QRhiBuffer *self, const char *key, void *call) {
  return static_cast<CuteQRhiBuffer *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiBuffer::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK10QRhiBuffer12resourceTypeEv(
    const QRhiBuffer *self) {
  return self->QRhiBuffer::resourceType();
}

//  NativeBuffer QRhiBuffer::nativeBuffer()
extern "C" Q_DECL_EXPORT
QRhiBuffer::NativeBuffer *ritual_own_ZN10QRhiBuffer12nativeBufferEv(
    QRhiBuffer *self) {
  return new QRhiBuffer::NativeBuffer(self->QRhiBuffer::nativeBuffer());
}

//  void QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv(
    QRhiBuffer *self) {
  self->QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame();
}
