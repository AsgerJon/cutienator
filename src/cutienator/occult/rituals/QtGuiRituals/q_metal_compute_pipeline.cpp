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

//  A QMetalComputePipeline that Python can take functions over in. Every QMetalComputePipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalComputePipelineCall0)(const void *, int *);
typedef bool (*CuteQMetalComputePipelineCall1)(const void *, int *);
typedef int (*CuteQMetalComputePipelineCall2)(const void *, int *);
class CuteQMetalComputePipeline : public QMetalComputePipeline {
public:
  using QMetalComputePipeline::QMetalComputePipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QRhiComputePipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QMetalComputePipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalComputePipelineCall0 call = reinterpret_cast<CuteQMetalComputePipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalComputePipeline::destroy();
  }

  //  bool QMetalComputePipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalComputePipelineCall1 call = reinterpret_cast<CuteQMetalComputePipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalComputePipeline::create();
  }

  //  QRhiResource::Type QRhiComputePipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalComputePipelineCall2 call = reinterpret_cast<CuteQMetalComputePipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiComputePipeline::resourceType();
  }
};

//  a Python function taken by a CuteQMetalComputePipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalComputePipeline(
    QMetalComputePipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalComputePipeline *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
