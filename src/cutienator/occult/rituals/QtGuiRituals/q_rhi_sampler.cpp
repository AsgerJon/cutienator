//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QRhiSampler that Python can take functions over in. Every QRhiSampler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiSamplerCall0)(const void *, int *);
typedef bool (*CuteQRhiSamplerCall1)(const void *, int *);
typedef void (*CuteQRhiSamplerCall2)(const void *, int *);
class CuteQRhiSampler : public QRhiSampler {
public:
  using QRhiSampler::QRhiSampler;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiSampler6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiSampler::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiSamplerCall0 call = reinterpret_cast<CuteQRhiSamplerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSampler::resourceType();
  }

  //  bool QRhiSampler::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiSamplerCall1 call = reinterpret_cast<CuteQRhiSamplerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiSamplerCall2 call = reinterpret_cast<CuteQRhiSamplerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiSampler::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK11QRhiSampler12resourceTypeEv(
    const QRhiSampler *self) {
  return self->resourceType();
}

//  Filter QRhiSampler::magFilter() const
extern "C" Q_DECL_EXPORT
QRhiSampler::Filter ritual_ZNK11QRhiSampler9magFilterEv(
    const QRhiSampler *self) {
  return self->magFilter();
}

//  void QRhiSampler::setMagFilter(Filter f)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiSampler12setMagFilterENS_6FilterE(
    QRhiSampler *self,
    QRhiSampler::Filter f) {
  self->setMagFilter(f);
}

//  Filter QRhiSampler::minFilter() const
extern "C" Q_DECL_EXPORT
QRhiSampler::Filter ritual_ZNK11QRhiSampler9minFilterEv(
    const QRhiSampler *self) {
  return self->minFilter();
}

//  void QRhiSampler::setMinFilter(Filter f)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiSampler12setMinFilterENS_6FilterE(
    QRhiSampler *self,
    QRhiSampler::Filter f) {
  self->setMinFilter(f);
}

//  Filter QRhiSampler::mipmapMode() const
extern "C" Q_DECL_EXPORT
QRhiSampler::Filter ritual_ZNK11QRhiSampler10mipmapModeEv(
    const QRhiSampler *self) {
  return self->mipmapMode();
}

//  void QRhiSampler::setMipmapMode(Filter f)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiSampler13setMipmapModeENS_6FilterE(
    QRhiSampler *self,
    QRhiSampler::Filter f) {
  self->setMipmapMode(f);
}

//  AddressMode QRhiSampler::addressU() const
extern "C" Q_DECL_EXPORT
QRhiSampler::AddressMode ritual_ZNK11QRhiSampler8addressUEv(
    const QRhiSampler *self) {
  return self->addressU();
}

//  void QRhiSampler::setAddressU(AddressMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiSampler11setAddressUENS_11AddressModeE(
    QRhiSampler *self,
    QRhiSampler::AddressMode mode) {
  self->setAddressU(mode);
}

//  AddressMode QRhiSampler::addressV() const
extern "C" Q_DECL_EXPORT
QRhiSampler::AddressMode ritual_ZNK11QRhiSampler8addressVEv(
    const QRhiSampler *self) {
  return self->addressV();
}

//  void QRhiSampler::setAddressV(AddressMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiSampler11setAddressVENS_11AddressModeE(
    QRhiSampler *self,
    QRhiSampler::AddressMode mode) {
  self->setAddressV(mode);
}

//  AddressMode QRhiSampler::addressW() const
extern "C" Q_DECL_EXPORT
QRhiSampler::AddressMode ritual_ZNK11QRhiSampler8addressWEv(
    const QRhiSampler *self) {
  return self->addressW();
}

//  void QRhiSampler::setAddressW(AddressMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiSampler11setAddressWENS_11AddressModeE(
    QRhiSampler *self,
    QRhiSampler::AddressMode mode) {
  self->setAddressW(mode);
}

//  CompareOp QRhiSampler::textureCompareOp() const
extern "C" Q_DECL_EXPORT
QRhiSampler::CompareOp ritual_ZNK11QRhiSampler16textureCompareOpEv(
    const QRhiSampler *self) {
  return self->textureCompareOp();
}

//  void QRhiSampler::setTextureCompareOp(CompareOp op)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiSampler19setTextureCompareOpENS_9CompareOpE(
    QRhiSampler *self,
    QRhiSampler::CompareOp op) {
  self->setTextureCompareOp(op);
}

//  bool QRhiSampler::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRhiSampler6createEv(QRhiSampler *self) {
  return self->create();
}

//  a Python function taken by a CuteQRhiSampler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiSampler(
    QRhiSampler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiSampler *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiSampler::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK11QRhiSampler12resourceTypeEv(
    const QRhiSampler *self) {
  return self->QRhiSampler::resourceType();
}
