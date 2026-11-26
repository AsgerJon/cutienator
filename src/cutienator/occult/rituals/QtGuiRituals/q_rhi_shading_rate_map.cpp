//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QRhiShadingRateMap that Python can take functions over in. Every QRhiShadingRateMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiShadingRateMapCall0)(const void *, int *);
typedef bool (*CuteQRhiShadingRateMapCall1)(const void *, const QRhiShadingRateMap::NativeShadingRateMap *, int *);
typedef bool (*CuteQRhiShadingRateMapCall2)(const void *, QRhiTexture *, int *);
typedef void (*CuteQRhiShadingRateMapCall3)(const void *, int *);
class CuteQRhiShadingRateMap : public QRhiShadingRateMap {
public:
  using QRhiShadingRateMap::QRhiShadingRateMap;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiShadingRateMap10createFromENS_20NativeShadingRateMapE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiShadingRateMap::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiShadingRateMapCall0 call = reinterpret_cast<CuteQRhiShadingRateMapCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShadingRateMap::resourceType();
  }

  //  bool QRhiShadingRateMap::createFrom(NativeShadingRateMap src)
  bool createFrom(QRhiShadingRateMap::NativeShadingRateMap src) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiShadingRateMapCall1 call = reinterpret_cast<CuteQRhiShadingRateMapCall1>(taken[1]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QRhiShadingRateMap::createFrom(src);
  }

  //  bool QRhiShadingRateMap::createFrom(QRhiTexture *src)
  bool createFrom(QRhiTexture *src) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiShadingRateMapCall2 call = reinterpret_cast<CuteQRhiShadingRateMapCall2>(taken[2]);
      bool given = call(this, src, &handled);
      if (handled) return given;
    }
    return QRhiShadingRateMap::createFrom(src);
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiShadingRateMapCall3 call = reinterpret_cast<CuteQRhiShadingRateMapCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiShadingRateMap::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK18QRhiShadingRateMap12resourceTypeEv(
    const QRhiShadingRateMap *self) {
  return self->resourceType();
}

//  bool QRhiShadingRateMap::createFrom(NativeShadingRateMap src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRhiShadingRateMap10createFromENS_20NativeShadingRateMapE(
    QRhiShadingRateMap *self,
    const QRhiShadingRateMap::NativeShadingRateMap *src) {
  return self->createFrom(*src);
}

//  bool QRhiShadingRateMap::createFrom(QRhiTexture *src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture(
    QRhiShadingRateMap *self,
    QRhiTexture *src) {
  return self->createFrom(src);
}

//  QRhiShadingRateMap::QRhiShadingRateMap(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN18QRhiShadingRateMapC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQRhiShadingRateMap(rhi);
}

//  a Python function taken by a CuteQRhiShadingRateMap, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiShadingRateMap(
    QRhiShadingRateMap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiShadingRateMap *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiShadingRateMap::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK18QRhiShadingRateMap12resourceTypeEv(
    const QRhiShadingRateMap *self) {
  return self->QRhiShadingRateMap::resourceType();
}

//  bool QRhiShadingRateMap::createFrom(NativeShadingRateMap src)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QRhiShadingRateMap10createFromENS_20NativeShadingRateMapE(
    QRhiShadingRateMap *self,
    const QRhiShadingRateMap::NativeShadingRateMap *src) {
  return self->QRhiShadingRateMap::createFrom(*src);
}

//  bool QRhiShadingRateMap::createFrom(QRhiTexture *src)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture(
    QRhiShadingRateMap *self,
    QRhiTexture *src) {
  return self->QRhiShadingRateMap::createFrom(src);
}
