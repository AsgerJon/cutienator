//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/boundingsphere_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: Vector3D is QVector3D or an SSE class by
//  system, and Matrix4x4 the same, so each value taken is made as
//  Vector3D(*x) or Matrix4x4(*x), and each value given is built from its
//  coordinates. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/boundingsphere_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qray3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::RayCasting::BoundingSphere that Python can take functions over in. Every Qt3DRender::RayCasting::BoundingSphere
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVector3D * (*CuteQt3DRender_RayCasting_BoundingSphereCall0)(const void *, int *);
typedef float (*CuteQt3DRender_RayCasting_BoundingSphereCall1)(const void *, int *);
typedef const Qt3DCore::QNodeId * (*CuteQt3DRender_RayCasting_BoundingSphereCall2)(const void *, int *);
typedef bool (*CuteQt3DRender_RayCasting_BoundingSphereCall3)(const void *, const Qt3DRender::RayCasting::QRay3D *, Vector3D *, Vector3D *, int *);
typedef int (*CuteQt3DRender_RayCasting_BoundingSphereCall4)(const void *, int *);
class CuteQt3DRender_RayCasting_BoundingSphere : public Qt3DRender::RayCasting::BoundingSphere {
public:
  using Qt3DRender::RayCasting::BoundingSphere::BoundingSphere;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10Qt3DRender10RayCasting14BoundingSphere6centerEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender10RayCasting14BoundingSphere6radiusEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender10RayCasting15QBoundingVolume2idEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender10RayCasting15QBoundingVolume10intersectsERKNS0_6QRay3DEP9QVector3DS6_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender10RayCasting15QBoundingVolume4typeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  Vector3D Qt3DRender::RayCasting::BoundingSphere::center() const
  Vector3D center() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_RayCasting_BoundingSphereCall0 call = reinterpret_cast<CuteQt3DRender_RayCasting_BoundingSphereCall0>(taken[0]);
      const QVector3D * given = call(this, &handled);
      if (handled && given) return Vector3D(*given);
    }
    return {};
  }

  //  float Qt3DRender::RayCasting::BoundingSphere::radius() const
  float radius() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_RayCasting_BoundingSphereCall1 call = reinterpret_cast<CuteQt3DRender_RayCasting_BoundingSphereCall1>(taken[1]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  Qt3DCore::QNodeId Qt3DRender::RayCasting::QBoundingVolume::id() const
  Qt3DCore::QNodeId id() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_RayCasting_BoundingSphereCall2 call = reinterpret_cast<CuteQt3DRender_RayCasting_BoundingSphereCall2>(taken[2]);
      const Qt3DCore::QNodeId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool Qt3DRender::RayCasting::QBoundingVolume::intersects(const QRay3D
  //      &ray, Vector3D *q, Vector3D *uvw) const
  bool intersects(
      const Qt3DRender::RayCasting::QRay3D &ray,
      Vector3D *q,
      Vector3D *uvw) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_RayCasting_BoundingSphereCall3 call = reinterpret_cast<CuteQt3DRender_RayCasting_BoundingSphereCall3>(taken[3]);
      bool given = call(this, &ray, q, uvw, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  Type Qt3DRender::RayCasting::QBoundingVolume::type() const
  Qt3DRender::RayCasting::QBoundingVolume::Type type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_RayCasting_BoundingSphereCall4 call = reinterpret_cast<CuteQt3DRender_RayCasting_BoundingSphereCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::RayCasting::QBoundingVolume::Type>(given);
    }
    return {};
  }
};

//  Vector3D Qt3DRender::RayCasting::BoundingSphere::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10RayCasting14BoundingSphere6centerEv(
    const Qt3DRender::RayCasting::BoundingSphere *self) {
  Vector3D v = self->center();
  return new QVector3D(v.x(), v.y(), v.z());
}

//  float Qt3DRender::RayCasting::BoundingSphere::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10RayCasting14BoundingSphere6radiusEv(
    const Qt3DRender::RayCasting::BoundingSphere *self) {
  return self->radius();
}

//  a Python function taken by a CuteQt3DRender_RayCasting_BoundingSphere,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_RayCasting_BoundingSphere(
    Qt3DRender::RayCasting::BoundingSphere *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_RayCasting_BoundingSphere *>(self)->take(key, call);
}
