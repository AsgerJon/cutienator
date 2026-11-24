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

//  A QMetalShaderResourceBindings that Python can take functions over in. Every QMetalShaderResourceBindings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalShaderResourceBindingsCall0)(const void *, int *);
typedef bool (*CuteQMetalShaderResourceBindingsCall1)(const void *, int *);
typedef void (*CuteQMetalShaderResourceBindingsCall2)(const void *, int, int *);
typedef int (*CuteQMetalShaderResourceBindingsCall3)(const void *, int *);
class CuteQMetalShaderResourceBindings : public QMetalShaderResourceBindings {
public:
  using QMetalShaderResourceBindings::QMetalShaderResourceBindings;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QRhiShaderResourceBindings6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QRhiShaderResourceBindings15updateResourcesE6QFlagsINS_10UpdateFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QMetalShaderResourceBindings::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalShaderResourceBindingsCall0 call = reinterpret_cast<CuteQMetalShaderResourceBindingsCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalShaderResourceBindings::destroy();
  }

  //  bool QMetalShaderResourceBindings::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalShaderResourceBindingsCall1 call = reinterpret_cast<CuteQMetalShaderResourceBindingsCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalShaderResourceBindings::create();
  }

  //  void QMetalShaderResourceBindings::updateResources(UpdateFlags flags)
  void updateResources(
      QRhiShaderResourceBindings::UpdateFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalShaderResourceBindingsCall2 call = reinterpret_cast<CuteQMetalShaderResourceBindingsCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QMetalShaderResourceBindings::updateResources(flags);
  }

  //  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalShaderResourceBindingsCall3 call = reinterpret_cast<CuteQMetalShaderResourceBindingsCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShaderResourceBindings::resourceType();
  }
};

//  a Python function taken by a CuteQMetalShaderResourceBindings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalShaderResourceBindings(
    QMetalShaderResourceBindings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalShaderResourceBindings *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
