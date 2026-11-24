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

//  A QMetalGraphicsPipeline that Python can take functions over in. Every QMetalGraphicsPipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalGraphicsPipelineCall0)(const void *, int *);
typedef bool (*CuteQMetalGraphicsPipelineCall1)(const void *, int *);
typedef int (*CuteQMetalGraphicsPipelineCall2)(const void *, int *);
class CuteQMetalGraphicsPipeline : public QMetalGraphicsPipeline {
public:
  using QMetalGraphicsPipeline::QMetalGraphicsPipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRhiGraphicsPipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QMetalGraphicsPipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalGraphicsPipelineCall0 call = reinterpret_cast<CuteQMetalGraphicsPipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalGraphicsPipeline::destroy();
  }

  //  bool QMetalGraphicsPipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalGraphicsPipelineCall1 call = reinterpret_cast<CuteQMetalGraphicsPipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalGraphicsPipeline::create();
  }

  //  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalGraphicsPipelineCall2 call = reinterpret_cast<CuteQMetalGraphicsPipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiGraphicsPipeline::resourceType();
  }
};

//  a Python function taken by a CuteQMetalGraphicsPipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalGraphicsPipeline(
    QMetalGraphicsPipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalGraphicsPipeline *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
