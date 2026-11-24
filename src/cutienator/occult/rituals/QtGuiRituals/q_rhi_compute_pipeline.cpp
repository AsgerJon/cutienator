//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QRhiComputePipeline that Python can take functions over in. Every QRhiComputePipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiComputePipelineCall0)(const void *, int *);
typedef bool (*CuteQRhiComputePipelineCall1)(const void *, int *);
typedef void (*CuteQRhiComputePipelineCall2)(const void *, int *);
class CuteQRhiComputePipeline : public QRhiComputePipeline {
public:
  using QRhiComputePipeline::QRhiComputePipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QRhiComputePipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiComputePipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiComputePipelineCall0 call = reinterpret_cast<CuteQRhiComputePipelineCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiComputePipeline::resourceType();
  }

  //  bool QRhiComputePipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiComputePipelineCall1 call = reinterpret_cast<CuteQRhiComputePipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiComputePipelineCall2 call = reinterpret_cast<CuteQRhiComputePipelineCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiComputePipeline::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK19QRhiComputePipeline12resourceTypeEv(
    const QRhiComputePipeline *self) {
  return self->resourceType();
}

//  bool QRhiComputePipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRhiComputePipeline6createEv(QRhiComputePipeline *self) {
  return self->create();
}

//  Flags QRhiComputePipeline::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QRhiComputePipeline5flagsEv(
    const QRhiComputePipeline *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QRhiComputePipeline::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiComputePipeline8setFlagsE6QFlagsINS_4FlagEE(
    QRhiComputePipeline *self,
    int f) {
  self->setFlags(QFlags<QRhiComputePipeline::Flag>::fromInt(f));
}

//  QRhiShaderStage QRhiComputePipeline::shaderStage() const
extern "C" Q_DECL_EXPORT
QRhiShaderStage *ritual_ZNK19QRhiComputePipeline11shaderStageEv(
    const QRhiComputePipeline *self) {
  return new QRhiShaderStage(self->shaderStage());
}

//  void QRhiComputePipeline::setShaderStage(const QRhiShaderStage &stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiComputePipeline14setShaderStageERK15QRhiShaderStage(
    QRhiComputePipeline *self,
    const QRhiShaderStage *stage) {
  self->setShaderStage(*stage);
}

//  QRhiShaderResourceBindings *QRhiComputePipeline::shaderResourceBindings()
//      const
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZNK19QRhiComputePipeline22shaderResourceBindingsEv(
    const QRhiComputePipeline *self) {
  return self->shaderResourceBindings();
}

//  void
//      QRhiComputePipeline::setShaderResourceBindings(QRhiShaderResourceBind
//      ings *srb)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiComputePipeline25setShaderResourceBindingsEP26QRhiShaderResourceBindings(
    QRhiComputePipeline *self,
    QRhiShaderResourceBindings *srb) {
  self->setShaderResourceBindings(srb);
}

//  a Python function taken by a CuteQRhiComputePipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiComputePipeline(
    QRhiComputePipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiComputePipeline *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiComputePipeline::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK19QRhiComputePipeline12resourceTypeEv(
    const QRhiComputePipeline *self) {
  return self->QRhiComputePipeline::resourceType();
}
