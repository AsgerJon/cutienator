//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qraycastingservice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qraycastingservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/qraycastingservice_p.h>
#include <Qt3DRender/private/qray3d_p.h>
#include <Qt3DRender/private/sphere_p.h>
#include <Qt3DRender/private/qboundingvolumeprovider_p.h>
#include <QtConcurrent/QtConcurrent>
#include "math.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/raycasting/qraycastingservice.cpp, line 23, as local:qraycastingservice.cpp:Hit
namespace Qt3DRender::RayCasting {
using namespace Qt3DCore;
namespace {
struct Hit
{
    Hit()
        : intersects(false)
        , distance(-1.0f)
    {}

    bool intersects;
    float distance;
    Qt3DCore::QNodeId id;
    Vector3D intersection;
    Vector3D uvw;
};
}  // namespace
}  // namespace Qt3DRender::RayCasting

//  from ../qt3d/src/render/raycasting/qraycastingservice.cpp, line 42, as local:qraycastingservice.cpp:volumeRayIntersection
namespace Qt3DRender::RayCasting {
using namespace Qt3DCore;
namespace {
inline Hit volumeRayIntersection(const QBoundingVolume *volume, const QRay3D &ray)
{
    Hit hit;
    if ((hit.intersects = volume->intersects(ray, &hit.intersection, &hit.uvw))) {
        hit.distance = ray.projectedDistance(hit.intersection);
        hit.id = volume->id();
    }
    return hit;
}
}  // namespace
}  // namespace Qt3DRender::RayCasting

//  from ../qt3d/src/render/raycasting/qraycastingservice.cpp, line 71, as local:qraycastingservice.cpp:CollisionGathererFunctor
namespace Qt3DRender::RayCasting {
using namespace Qt3DCore;
namespace {
struct CollisionGathererFunctor
{
    QRay3D ray;

    typedef Hit result_type;

    Hit operator ()(const QBoundingVolume *volume) const
    {
        return volumeRayIntersection(volume, ray);
    }
};
}  // namespace
}  // namespace Qt3DRender::RayCasting

//  from ../qt3d/src/render/raycasting/qraycastingservice.cpp, line 138, as _ZN10Qt3DRender10RayCasting25QRayCastingServicePrivateC1ERK7QString
namespace Qt3DRender::RayCasting {
using namespace Qt3DCore;
inline QRayCastingServicePrivate::QRayCastingServicePrivate(const QString &description)
    : QAbstractCollisionQueryServicePrivate(description)
    , m_handlesCount(0)
{
}
}  // namespace Qt3DRender::RayCasting
//  -----------------------------------------------------------------------

//  Qt3DRender::RayCasting::QRayCastingServicePrivate::QRayCastingServicePriv
//      ate(const QString &description)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QRayCastingServicePrivate *ritual_ZN10Qt3DRender10RayCasting25QRayCastingServicePrivateC1ERK7QString(
    const QString *description) {
  return new Qt3DRender::RayCasting::QRayCastingServicePrivate(*description);
}

//  QRayCastingService
//      *Qt3DRender::RayCasting::QRayCastingServicePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QRayCastingService *ritual_ZN10Qt3DRender10RayCasting25QRayCastingServicePrivate6q_funcEv(
    Qt3DRender::RayCasting::QRayCastingServicePrivate *self) {
  return self->q_func();
}

//  const QRayCastingService
//      *Qt3DRender::RayCasting::QRayCastingServicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::RayCasting::QRayCastingService *ritual_ZNK10Qt3DRender10RayCasting25QRayCastingServicePrivate6q_funcEv(
    const Qt3DRender::RayCasting::QRayCastingServicePrivate *self) {
  return self->q_func();
}
