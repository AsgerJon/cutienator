//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmemoryvideobuffer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmemoryvideobuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtMultimedia/qabstractvideobuffer.h>
#include <QtMultimedia/qvideoframeformat.h>
#include <cstring>

//  A QMemoryVideoBuffer that Python can take functions over in. Every QMemoryVideoBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QAbstractVideoBuffer::MapData * (*CuteQMemoryVideoBufferCall0)(const void *, int, int *);
typedef const QVideoFrameFormat * (*CuteQMemoryVideoBufferCall1)(const void *, int *);
typedef void (*CuteQMemoryVideoBufferCall2)(const void *, int *);
class CuteQMemoryVideoBuffer : public QMemoryVideoBuffer {
public:
  using QMemoryVideoBuffer::QMemoryVideoBuffer;
  CuteQMemoryVideoBuffer(const QMemoryVideoBuffer &other) : QMemoryVideoBuffer(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractVideoBuffer3mapEN11QVideoFrame7MapModeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAbstractVideoBuffer6formatEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractVideoBuffer5unmapEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  MapData QMemoryVideoBuffer::map(QVideoFrame::MapMode mode)
  QAbstractVideoBuffer::MapData map(QVideoFrame::MapMode mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMemoryVideoBufferCall0 call = reinterpret_cast<CuteQMemoryVideoBufferCall0>(taken[0]);
      const QAbstractVideoBuffer::MapData * given = call(this, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return QMemoryVideoBuffer::map(mode);
  }

  //  QVideoFrameFormat QMemoryVideoBuffer::format() const
  QVideoFrameFormat format() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMemoryVideoBufferCall1 call = reinterpret_cast<CuteQMemoryVideoBufferCall1>(taken[1]);
      const QVideoFrameFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMemoryVideoBuffer::format();
  }

  //  void QAbstractVideoBuffer::unmap()
  void unmap() override {
    if (taken[2]) {
      int handled = 0;
      CuteQMemoryVideoBufferCall2 call = reinterpret_cast<CuteQMemoryVideoBufferCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractVideoBuffer::unmap();
  }
};

//  QMemoryVideoBuffer::QMemoryVideoBuffer(QByteArray data, int bytesPerLine)
extern "C" Q_DECL_EXPORT
QMemoryVideoBuffer *ritual_ZN18QMemoryVideoBufferC1E10QByteArrayi(
    const QByteArray *data,
    int bytesPerLine) {
  return new CuteQMemoryVideoBuffer(*data, bytesPerLine);
}

//  QMemoryVideoBuffer::~QMemoryVideoBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMemoryVideoBufferD1Ev(QMemoryVideoBuffer *self) {
  delete self;
}

//  MapData QMemoryVideoBuffer::map(QVideoFrame::MapMode mode)
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer::MapData *ritual_ZN18QMemoryVideoBuffer3mapEN11QVideoFrame7MapModeE(
    QMemoryVideoBuffer *self,
    QVideoFrame::MapMode mode) {
  return new QAbstractVideoBuffer::MapData(self->map(mode));
}

//  QVideoFrameFormat QMemoryVideoBuffer::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK18QMemoryVideoBuffer6formatEv(
    const QMemoryVideoBuffer *self) {
  return new QVideoFrameFormat(self->format());
}

//  a Python function taken by a CuteQMemoryVideoBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMemoryVideoBuffer(
    QMemoryVideoBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMemoryVideoBuffer *>(self)->take(key, call);
}

//  MapData QMemoryVideoBuffer::map(QVideoFrame::MapMode mode)
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer::MapData *ritual_own_ZN18QMemoryVideoBuffer3mapEN11QVideoFrame7MapModeE(
    QMemoryVideoBuffer *self,
    QVideoFrame::MapMode mode) {
  return new QAbstractVideoBuffer::MapData(
      self->QMemoryVideoBuffer::map(
          mode));
}

//  QVideoFrameFormat QMemoryVideoBuffer::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_own_ZNK18QMemoryVideoBuffer6formatEv(
    const QMemoryVideoBuffer *self) {
  return new QVideoFrameFormat(self->QMemoryVideoBuffer::format());
}
