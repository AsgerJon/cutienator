//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qabstractvideobuffer.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMultimedia/qabstractvideobuffer.h>
#include <QtMultimedia/qvideoframeformat.h>
#include <cstring>

//  A QAbstractVideoBuffer that Python can take functions over in. Every QAbstractVideoBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QAbstractVideoBuffer::MapData * (*CuteQAbstractVideoBufferCall0)(const void *, int, int *);
typedef void (*CuteQAbstractVideoBufferCall1)(const void *, int *);
typedef const QVideoFrameFormat * (*CuteQAbstractVideoBufferCall2)(const void *, int *);
class CuteQAbstractVideoBuffer : public QAbstractVideoBuffer {
public:
  using QAbstractVideoBuffer::QAbstractVideoBuffer;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractVideoBuffer3mapEN11QVideoFrame7MapModeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractVideoBuffer5unmapEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAbstractVideoBuffer6formatEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  MapData QAbstractVideoBuffer::map(QVideoFrame::MapMode mode)
  QAbstractVideoBuffer::MapData map(QVideoFrame::MapMode mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractVideoBufferCall0 call = reinterpret_cast<CuteQAbstractVideoBufferCall0>(taken[0]);
      const QAbstractVideoBuffer::MapData * given = call(this, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QAbstractVideoBuffer::unmap()
  void unmap() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractVideoBufferCall1 call = reinterpret_cast<CuteQAbstractVideoBufferCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractVideoBuffer::unmap();
  }

  //  QVideoFrameFormat QAbstractVideoBuffer::format() const
  QVideoFrameFormat format() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractVideoBufferCall2 call = reinterpret_cast<CuteQAbstractVideoBufferCall2>(taken[2]);
      const QVideoFrameFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QAbstractVideoBuffer::~QAbstractVideoBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractVideoBufferD1Ev(QAbstractVideoBuffer *self) {
  delete self;
}

//  MapData QAbstractVideoBuffer::map(QVideoFrame::MapMode mode)
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer::MapData *ritual_ZN20QAbstractVideoBuffer3mapEN11QVideoFrame7MapModeE(
    QAbstractVideoBuffer *self,
    QVideoFrame::MapMode mode) {
  return new QAbstractVideoBuffer::MapData(self->map(mode));
}

//  void QAbstractVideoBuffer::unmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractVideoBuffer5unmapEv(QAbstractVideoBuffer *self) {
  self->unmap();
}

//  QVideoFrameFormat QAbstractVideoBuffer::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK20QAbstractVideoBuffer6formatEv(
    const QAbstractVideoBuffer *self) {
  return new QVideoFrameFormat(self->format());
}

//  a Python function taken by a CuteQAbstractVideoBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractVideoBuffer(
    QAbstractVideoBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractVideoBuffer *>(self)->take(key, call);
}

//  void QAbstractVideoBuffer::unmap()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractVideoBuffer5unmapEv(
    QAbstractVideoBuffer *self) {
  self->QAbstractVideoBuffer::unmap();
}
