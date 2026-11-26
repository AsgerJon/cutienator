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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMetalSampler that Python can take functions over in. Every QMetalSampler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalSamplerCall0)(const void *, int *);
typedef bool (*CuteQMetalSamplerCall1)(const void *, int *);
typedef int (*CuteQMetalSamplerCall2)(const void *, int *);
class CuteQMetalSampler : public QMetalSampler {
public:
  using QMetalSampler::QMetalSampler;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiSampler6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QMetalSampler::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalSamplerCall0 call = reinterpret_cast<CuteQMetalSamplerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalSampler::destroy();
  }

  //  bool QMetalSampler::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalSamplerCall1 call = reinterpret_cast<CuteQMetalSamplerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalSampler::create();
  }

  //  QRhiResource::Type QRhiSampler::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalSamplerCall2 call = reinterpret_cast<CuteQMetalSamplerCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSampler::resourceType();
  }
};

//  void QMetalSampler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMetalSampler7destroyEv(QMetalSampler *self) {
  self->destroy();
}

//  bool QMetalSampler::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QMetalSampler6createEv(QMetalSampler *self) {
  return self->create();
}

//  a Python function taken by a CuteQMetalSampler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalSampler(
    QMetalSampler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalSampler *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
