//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QRhiTexture that Python can take functions over in. Every QRhiTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiTextureCall0)(const void *, int *);
typedef bool (*CuteQRhiTextureCall1)(const void *, int *);
typedef const QRhiTexture::NativeTexture * (*CuteQRhiTextureCall2)(const void *, int *);
typedef bool (*CuteQRhiTextureCall3)(const void *, const QRhiTexture::NativeTexture *, int *);
typedef void (*CuteQRhiTextureCall4)(const void *, int, int *);
typedef void (*CuteQRhiTextureCall5)(const void *, int *);
class CuteQRhiTexture : public QRhiTexture {
public:
  using QRhiTexture::QRhiTexture;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture13nativeTextureEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture10createFromENS_13NativeTextureE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture15setNativeLayoutEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiTexture::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiTextureCall0 call = reinterpret_cast<CuteQRhiTextureCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTexture::resourceType();
  }

  //  bool QRhiTexture::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiTextureCall1 call = reinterpret_cast<CuteQRhiTextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  NativeTexture QRhiTexture::nativeTexture()
  QRhiTexture::NativeTexture nativeTexture() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiTextureCall2 call = reinterpret_cast<CuteQRhiTextureCall2>(taken[2]);
      const QRhiTexture::NativeTexture * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiTexture::nativeTexture();
  }

  //  bool QRhiTexture::createFrom(NativeTexture src)
  bool createFrom(QRhiTexture::NativeTexture src) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiTextureCall3 call = reinterpret_cast<CuteQRhiTextureCall3>(taken[3]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QRhiTexture::createFrom(src);
  }

  //  void QRhiTexture::setNativeLayout(int layout)
  void setNativeLayout(int layout) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiTextureCall4 call = reinterpret_cast<CuteQRhiTextureCall4>(taken[4]);
      call(this, layout, &handled);
      if (handled) return;
    }
    QRhiTexture::setNativeLayout(layout);
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiTextureCall5 call = reinterpret_cast<CuteQRhiTextureCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiTexture::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK11QRhiTexture12resourceTypeEv(
    const QRhiTexture *self) {
  return self->resourceType();
}

//  Format QRhiTexture::format() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK11QRhiTexture6formatEv(
    const QRhiTexture *self) {
  return self->format();
}

//  void QRhiTexture::setFormat(Format fmt)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture9setFormatENS_6FormatE(
    QRhiTexture *self,
    QRhiTexture::Format fmt) {
  self->setFormat(fmt);
}

//  QSize QRhiTexture::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QRhiTexture9pixelSizeEv(const QRhiTexture *self) {
  return new QSize(self->pixelSize());
}

//  void QRhiTexture::setPixelSize(const QSize &sz)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture12setPixelSizeERK5QSize(
    QRhiTexture *self,
    const QSize *sz) {
  self->setPixelSize(*sz);
}

//  int QRhiTexture::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRhiTexture5depthEv(const QRhiTexture *self) {
  return self->depth();
}

//  void QRhiTexture::setDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture8setDepthEi(QRhiTexture *self, int depth) {
  self->setDepth(depth);
}

//  int QRhiTexture::arraySize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRhiTexture9arraySizeEv(const QRhiTexture *self) {
  return self->arraySize();
}

//  void QRhiTexture::setArraySize(int arraySize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture12setArraySizeEi(
    QRhiTexture *self,
    int arraySize) {
  self->setArraySize(arraySize);
}

//  int QRhiTexture::arrayRangeStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRhiTexture15arrayRangeStartEv(const QRhiTexture *self) {
  return self->arrayRangeStart();
}

//  int QRhiTexture::arrayRangeLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRhiTexture16arrayRangeLengthEv(const QRhiTexture *self) {
  return self->arrayRangeLength();
}

//  void QRhiTexture::setArrayRange(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture13setArrayRangeEii(
    QRhiTexture *self,
    int startIndex,
    int count) {
  self->setArrayRange(startIndex, count);
}

//  Flags QRhiTexture::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRhiTexture5flagsEv(const QRhiTexture *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QRhiTexture::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture8setFlagsE6QFlagsINS_4FlagEE(
    QRhiTexture *self,
    int f) {
  self->setFlags(QFlags<QRhiTexture::Flag>::fromInt(f));
}

//  int QRhiTexture::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRhiTexture11sampleCountEv(const QRhiTexture *self) {
  return self->sampleCount();
}

//  void QRhiTexture::setSampleCount(int s)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture14setSampleCountEi(QRhiTexture *self, int s) {
  self->setSampleCount(s);
}

//  ViewFormat QRhiTexture::readViewFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::ViewFormat *ritual_ZNK11QRhiTexture14readViewFormatEv(
    const QRhiTexture *self) {
  return new QRhiTexture::ViewFormat(self->readViewFormat());
}

//  void QRhiTexture::setReadViewFormat(const ViewFormat &fmt)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture17setReadViewFormatERKNS_10ViewFormatE(
    QRhiTexture *self,
    const QRhiTexture::ViewFormat *fmt) {
  self->setReadViewFormat(*fmt);
}

//  ViewFormat QRhiTexture::writeViewFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::ViewFormat *ritual_ZNK11QRhiTexture15writeViewFormatEv(
    const QRhiTexture *self) {
  return new QRhiTexture::ViewFormat(self->writeViewFormat());
}

//  void QRhiTexture::setWriteViewFormat(const ViewFormat &fmt)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture18setWriteViewFormatERKNS_10ViewFormatE(
    QRhiTexture *self,
    const QRhiTexture::ViewFormat *fmt) {
  self->setWriteViewFormat(*fmt);
}

//  bool QRhiTexture::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRhiTexture6createEv(QRhiTexture *self) {
  return self->create();
}

//  NativeTexture QRhiTexture::nativeTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture::NativeTexture *ritual_ZN11QRhiTexture13nativeTextureEv(
    QRhiTexture *self) {
  return new QRhiTexture::NativeTexture(self->nativeTexture());
}

//  bool QRhiTexture::createFrom(NativeTexture src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRhiTexture10createFromENS_13NativeTextureE(
    QRhiTexture *self,
    const QRhiTexture::NativeTexture *src) {
  return self->createFrom(*src);
}

//  void QRhiTexture::setNativeLayout(int layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiTexture15setNativeLayoutEi(
    QRhiTexture *self,
    int layout) {
  self->setNativeLayout(layout);
}

//  a Python function taken by a CuteQRhiTexture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiTexture(
    QRhiTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiTexture *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiTexture::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK11QRhiTexture12resourceTypeEv(
    const QRhiTexture *self) {
  return self->QRhiTexture::resourceType();
}

//  NativeTexture QRhiTexture::nativeTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture::NativeTexture *ritual_own_ZN11QRhiTexture13nativeTextureEv(
    QRhiTexture *self) {
  return new QRhiTexture::NativeTexture(self->QRhiTexture::nativeTexture());
}

//  bool QRhiTexture::createFrom(NativeTexture src)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRhiTexture10createFromENS_13NativeTextureE(
    QRhiTexture *self,
    const QRhiTexture::NativeTexture *src) {
  return self->QRhiTexture::createFrom(*src);
}

//  void QRhiTexture::setNativeLayout(int layout)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRhiTexture15setNativeLayoutEi(
    QRhiTexture *self,
    int layout) {
  self->QRhiTexture::setNativeLayout(layout);
}
