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

//  A QMetalShadingRateMap that Python can take functions over in. Every QMetalShadingRateMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalShadingRateMapCall0)(const void *, int *);
typedef bool (*CuteQMetalShadingRateMapCall1)(const void *, const QRhiShadingRateMap::NativeShadingRateMap *, int *);
typedef int (*CuteQMetalShadingRateMapCall2)(const void *, int *);
typedef bool (*CuteQMetalShadingRateMapCall3)(const void *, QRhiTexture *, int *);
class CuteQMetalShadingRateMap : public QMetalShadingRateMap {
public:
  using QMetalShadingRateMap::QMetalShadingRateMap;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiShadingRateMap10createFromENS_20NativeShadingRateMapE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QMetalShadingRateMap::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalShadingRateMapCall0 call = reinterpret_cast<CuteQMetalShadingRateMapCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalShadingRateMap::destroy();
  }

  //  bool QMetalShadingRateMap::createFrom(NativeShadingRateMap src)
  bool createFrom(QRhiShadingRateMap::NativeShadingRateMap src) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalShadingRateMapCall1 call = reinterpret_cast<CuteQMetalShadingRateMapCall1>(taken[1]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QMetalShadingRateMap::createFrom(src);
  }

  //  QRhiResource::Type QRhiShadingRateMap::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalShadingRateMapCall2 call = reinterpret_cast<CuteQMetalShadingRateMapCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShadingRateMap::resourceType();
  }

  //  bool QRhiShadingRateMap::createFrom(QRhiTexture *src)
  bool createFrom(QRhiTexture *src) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalShadingRateMapCall3 call = reinterpret_cast<CuteQMetalShadingRateMapCall3>(taken[3]);
      bool given = call(this, src, &handled);
      if (handled) return given;
    }
    return QRhiShadingRateMap::createFrom(src);
  }
};

//  void QMetalShadingRateMap::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetalShadingRateMap7destroyEv(QMetalShadingRateMap *self) {
  self->destroy();
}

//  bool QMetalShadingRateMap::createFrom(NativeShadingRateMap src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QMetalShadingRateMap10createFromEN18QRhiShadingRateMap20NativeShadingRateMapE(
    QMetalShadingRateMap *self,
    const QRhiShadingRateMap::NativeShadingRateMap *src) {
  return self->createFrom(*src);
}

//  a Python function taken by a CuteQMetalShadingRateMap, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalShadingRateMap(
    QMetalShadingRateMap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalShadingRateMap *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
