//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qvideoframeformat.h>
#include <QtGui/qmatrix4x4.h>
#include <QtMultimedia/qabstractvideobuffer.h>
#include <cstring>

//  A QHwVideoBuffer that Python can take functions over in. Every QHwVideoBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQHwVideoBufferCall0)(const void *, int *);
typedef const QVideoFrameFormat * (*CuteQHwVideoBufferCall1)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQHwVideoBufferCall2)(const void *, int *);
typedef bool (*CuteQHwVideoBufferCall3)(const void *, int *);
typedef const QAbstractVideoBuffer::MapData * (*CuteQHwVideoBufferCall4)(const void *, int, int *);
typedef void (*CuteQHwVideoBufferCall5)(const void *, int *);
class CuteQHwVideoBuffer : public QHwVideoBuffer {
public:
  using QHwVideoBuffer::QHwVideoBuffer;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QHwVideoBuffer26associatedCurrentThreadRhiEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAbstractVideoBuffer6formatEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QHwVideoBuffer21externalTextureMatrixEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QHwVideoBuffer8isDmaBufEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractVideoBuffer3mapEN11QVideoFrame7MapModeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractVideoBuffer5unmapEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  QRhi *QHwVideoBuffer::associatedCurrentThreadRhi() const
  QRhi *associatedCurrentThreadRhi() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHwVideoBufferCall0 call = reinterpret_cast<CuteQHwVideoBufferCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhi *>(given);
    }
    return QHwVideoBuffer::associatedCurrentThreadRhi();
  }

  //  QVideoFrameFormat QHwVideoBuffer::format() const
  QVideoFrameFormat format() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHwVideoBufferCall1 call = reinterpret_cast<CuteQHwVideoBufferCall1>(taken[1]);
      const QVideoFrameFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHwVideoBuffer::format();
  }

  //  QMatrix4x4 QHwVideoBuffer::externalTextureMatrix() const
  QMatrix4x4 externalTextureMatrix() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHwVideoBufferCall2 call = reinterpret_cast<CuteQHwVideoBufferCall2>(taken[2]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHwVideoBuffer::externalTextureMatrix();
  }

  //  bool QHwVideoBuffer::isDmaBuf() const
  bool isDmaBuf() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHwVideoBufferCall3 call = reinterpret_cast<CuteQHwVideoBufferCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHwVideoBuffer::isDmaBuf();
  }

  //  MapData QAbstractVideoBuffer::map(QVideoFrame::MapMode mode)
  QAbstractVideoBuffer::MapData map(QVideoFrame::MapMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHwVideoBufferCall4 call = reinterpret_cast<CuteQHwVideoBufferCall4>(taken[4]);
      const QAbstractVideoBuffer::MapData * given = call(this, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QAbstractVideoBuffer::unmap()
  void unmap() override {
    if (taken[5]) {
      int handled = 0;
      CuteQHwVideoBufferCall5 call = reinterpret_cast<CuteQHwVideoBufferCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractVideoBuffer::unmap();
  }
};

//  QHwVideoBuffer::~QHwVideoBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHwVideoBufferD1Ev(QHwVideoBuffer *self) {
  delete self;
}

//  QVideoFrame::HandleType QHwVideoBuffer::handleType() const
extern "C" Q_DECL_EXPORT
QVideoFrame::HandleType ritual_ZNK14QHwVideoBuffer10handleTypeEv(
    const QHwVideoBuffer *self) {
  return self->handleType();
}

//  QRhi *QHwVideoBuffer::associatedCurrentThreadRhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK14QHwVideoBuffer26associatedCurrentThreadRhiEv(
    const QHwVideoBuffer *self) {
  return self->associatedCurrentThreadRhi();
}

//  QVideoFrameFormat QHwVideoBuffer::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK14QHwVideoBuffer6formatEv(
    const QHwVideoBuffer *self) {
  return new QVideoFrameFormat(self->format());
}

//  QMatrix4x4 QHwVideoBuffer::externalTextureMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK14QHwVideoBuffer21externalTextureMatrixEv(
    const QHwVideoBuffer *self) {
  return new QMatrix4x4(self->externalTextureMatrix());
}

//  bool QHwVideoBuffer::isDmaBuf() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QHwVideoBuffer8isDmaBufEv(const QHwVideoBuffer *self) {
  return self->isDmaBuf();
}

//  QHwVideoBuffer as the QVideoFrameTexturesHandles it is built on
extern "C" Q_DECL_EXPORT
QVideoFrameTexturesHandles *ritual_cast_QHwVideoBuffer_QVideoFrameTexturesHandles(
    QHwVideoBuffer *self) {
  return static_cast<QVideoFrameTexturesHandles *>(self);
}

//  a Python function taken by a CuteQHwVideoBuffer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHwVideoBuffer(
    QHwVideoBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHwVideoBuffer *>(self)->take(key, call);
}

//  QRhi *QHwVideoBuffer::associatedCurrentThreadRhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_own_ZNK14QHwVideoBuffer26associatedCurrentThreadRhiEv(
    const QHwVideoBuffer *self) {
  return self->QHwVideoBuffer::associatedCurrentThreadRhi();
}

//  QVideoFrameFormat QHwVideoBuffer::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_own_ZNK14QHwVideoBuffer6formatEv(
    const QHwVideoBuffer *self) {
  return new QVideoFrameFormat(self->QHwVideoBuffer::format());
}

//  QMatrix4x4 QHwVideoBuffer::externalTextureMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_own_ZNK14QHwVideoBuffer21externalTextureMatrixEv(
    const QHwVideoBuffer *self) {
  return new QMatrix4x4(self->QHwVideoBuffer::externalTextureMatrix());
}

//  bool QHwVideoBuffer::isDmaBuf() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QHwVideoBuffer8isDmaBufEv(const QHwVideoBuffer *self) {
  return self->QHwVideoBuffer::isDmaBuf();
}
