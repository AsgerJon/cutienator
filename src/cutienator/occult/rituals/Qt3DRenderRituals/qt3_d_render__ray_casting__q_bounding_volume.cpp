//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qboundingvolume_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qboundingvolume_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DRender::RayCasting::QBoundingVolume that Python can take functions over in. Every Qt3DRender::RayCasting::QBoundingVolume
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const Qt3DCore::QNodeId * (*CuteQt3DRender_RayCasting_QBoundingVolumeCall0)(const void *, int *);
typedef int (*CuteQt3DRender_RayCasting_QBoundingVolumeCall1)(const void *, int *);
class CuteQt3DRender_RayCasting_QBoundingVolume : public Qt3DRender::RayCasting::QBoundingVolume {
public:
  using Qt3DRender::RayCasting::QBoundingVolume::QBoundingVolume;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10Qt3DRender10RayCasting15QBoundingVolume2idEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender10RayCasting15QBoundingVolume4typeEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  Qt3DCore::QNodeId Qt3DRender::RayCasting::QBoundingVolume::id() const
  Qt3DCore::QNodeId id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_RayCasting_QBoundingVolumeCall0 call = reinterpret_cast<CuteQt3DRender_RayCasting_QBoundingVolumeCall0>(taken[0]);
      const Qt3DCore::QNodeId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  Type Qt3DRender::RayCasting::QBoundingVolume::type() const
  Qt3DRender::RayCasting::QBoundingVolume::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_RayCasting_QBoundingVolumeCall1 call = reinterpret_cast<CuteQt3DRender_RayCasting_QBoundingVolumeCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::RayCasting::QBoundingVolume::Type>(given);
    }
    return {};
  }
};

//  Qt3DRender::RayCasting::QBoundingVolume::~QBoundingVolume()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10RayCasting15QBoundingVolumeD1Ev(
    Qt3DRender::RayCasting::QBoundingVolume *self) {
  delete self;
}

//  Qt3DCore::QNodeId Qt3DRender::RayCasting::QBoundingVolume::id() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender10RayCasting15QBoundingVolume2idEv(
    const Qt3DRender::RayCasting::QBoundingVolume *self) {
  return new Qt3DCore::QNodeId(self->id());
}

//  Type Qt3DRender::RayCasting::QBoundingVolume::type() const
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QBoundingVolume::Type ritual_ZNK10Qt3DRender10RayCasting15QBoundingVolume4typeEv(
    const Qt3DRender::RayCasting::QBoundingVolume *self) {
  return self->type();
}

//  a Python function taken by a CuteQt3DRender_RayCasting_QBoundingVolume,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_RayCasting_QBoundingVolume(
    Qt3DRender::RayCasting::QBoundingVolume *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_RayCasting_QBoundingVolume *>(self)->take(key, call);
}
