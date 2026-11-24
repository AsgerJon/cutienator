//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::BoundingVolumeJobProcessor that Python can take functions over in. Every Qt3DCore::BoundingVolumeJobProcessor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_BoundingVolumeJobProcessorCall0)(const void *, const Qt3DCore::BoundingVolumeComputeResult *, bool, int *);
class CuteQt3DCore_BoundingVolumeJobProcessor : public Qt3DCore::BoundingVolumeJobProcessor {
public:
  using Qt3DCore::BoundingVolumeJobProcessor::BoundingVolumeJobProcessor;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore26BoundingVolumeJobProcessor7processERKNS_27BoundingVolumeComputeResultEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::BoundingVolumeJobProcessor::process(const
  //      BoundingVolumeComputeResult &result, bool computedResult)
  void process(
      const Qt3DCore::BoundingVolumeComputeResult &result,
      bool computedResult) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_BoundingVolumeJobProcessorCall0 call = reinterpret_cast<CuteQt3DCore_BoundingVolumeJobProcessorCall0>(taken[0]);
      call(this, &result, computedResult, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DCore::BoundingVolumeJobProcessor::~BoundingVolumeJobProcessor()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore26BoundingVolumeJobProcessorD1Ev(
    Qt3DCore::BoundingVolumeJobProcessor *self) {
  delete self;
}

//  void Qt3DCore::BoundingVolumeJobProcessor::process(const
//      BoundingVolumeComputeResult &result, bool computedResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore26BoundingVolumeJobProcessor7processERKNS_27BoundingVolumeComputeResultEb(
    Qt3DCore::BoundingVolumeJobProcessor *self,
    const Qt3DCore::BoundingVolumeComputeResult *result,
    bool computedResult) {
  self->process(*result, computedResult);
}

//  a Python function taken by a CuteQt3DCore_BoundingVolumeJobProcessor, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_BoundingVolumeJobProcessor(
    Qt3DCore::BoundingVolumeJobProcessor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_BoundingVolumeJobProcessor *>(self)->take(key, call);
}
