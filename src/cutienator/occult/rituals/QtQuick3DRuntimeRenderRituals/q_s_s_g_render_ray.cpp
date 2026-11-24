//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#include <QtQuick3DUtils/private/qssgplane_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgmeshbvh_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendermesh_p.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 30, as _ZN13QSSGRenderRay13createRayDataERK10QMatrix4x4RKS_
inline QSSGRenderRay::RayData QSSGRenderRay::createRayData(const QMatrix4x4 &globalTransform,
                                                    const QSSGRenderRay &ray)
{
    using DirectionOp = RayData::DirectionOp;
    QMatrix4x4 originTransform = globalTransform.inverted();
    QVector3D transformedOrigin = QSSGUtils::mat44::transform(originTransform, ray.origin);
    float *outOriginTransformPtr(originTransform.data());
    outOriginTransformPtr[12] = outOriginTransformPtr[13] = outOriginTransformPtr[14] = 0.0f;
    const QVector3D &transformedDirection = QSSGUtils::mat44::rotate(originTransform, ray.direction).normalized();
    static auto getInverseAndDirOp = [](const QVector3D &dir, QVector3D &invDir, DirectionOp (&dirOp)[3]) {
        for (int i = 0; i != 3; ++i) {
            const float axisDir = dir[i];
            dirOp[i] = qFuzzyIsNull(axisDir) ? DirectionOp::Zero : ((axisDir < -std::numeric_limits<float>::epsilon())
                                                                    ? DirectionOp::Swap
                                                                    : DirectionOp::Normal);
            invDir[i] = qFuzzyIsNull(axisDir) ? 0.0f : (1.0f / axisDir);
        }
    };
    DirectionOp dirOp[3];
    QVector3D transformedDirectionInvers;
    getInverseAndDirOp(transformedDirection, transformedDirectionInvers, dirOp);
    return RayData{ globalTransform, ray, transformedOrigin, transformedDirectionInvers,
                    transformedDirection, { dirOp[0], dirOp[1], dirOp[2] } };
}

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 55, as _ZN13QSSGRenderRay24createIntersectionResultERKNS_7RayDataERKNS_9HitResultE
inline QSSGRenderRay::IntersectionResult QSSGRenderRay::createIntersectionResult(const QSSGRenderRay::RayData &data,
                                                                          const HitResult &hit)
{
    Q_ASSERT(hit.intersects());
    Q_ASSERT(hit.bounds != nullptr);
    const QSSGBounds3 &bounds = *hit.bounds;
    // Local postion
    const QVector3D &scaledDir = data.direction * hit.min;
    const QVector3D &localPosition = scaledDir + data.origin;
    // ray length squared
    const QVector3D &globalPosition = QSSGUtils::mat44::transform(data.globalTransform, localPosition);
    const QVector3D &cameraToLocal = data.ray.origin - globalPosition;
    const float rayLenSquared = QSSGUtils::vec3::magnitudeSquared(cameraToLocal);
    // UV coordinates
    const auto &boundsMin = bounds.minimum;
    const auto &boundsMax = bounds.maximum;
    const float xRange = boundsMax.x() - boundsMin.x();
    const float yRange = boundsMax.y() - boundsMin.y();
    const QVector2D uvCoords{((localPosition[0] - boundsMin.x()) / xRange), ((localPosition[1] - boundsMin.y()) / yRange)};

    // Since we just intersected with a bounding box, there is no face normal
    return IntersectionResult(rayLenSquared, uvCoords, globalPosition, localPosition, QVector3D(), QVector3D());
}

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 79, as _ZN13QSSGRenderRay19intersectWithAABBv2ERKNS_7RayDataERK11QSSGBounds3
inline QSSGRenderRay::HitResult QSSGRenderRay::intersectWithAABBv2(const QSSGRenderRay::RayData &data,
                                                            const QSSGBounds3 &bounds)
{
    // Intersect the origin with the AABB described by bounds.

    // Scan each axis separately.  This code basically finds the distance
    // from the origin to the near and far bbox planes for a given
    // axis.  It then divides this distance by the direction for that axis to
    // get a range of t [near,far] that the ray intersects assuming the ray is
    // described via origin + t*(direction).  Running through all three axis means
    // that you need to min/max those ranges together to find a global min/max
    // that the pick could possibly be in.
    float tmax = std::numeric_limits<float>::max();
    float tmin = std::numeric_limits<float>::min();
    float origin;
    const QVector3D *const barray[] { &bounds.minimum, &bounds.maximum };

    for (int axis = 0; axis != 3; ++axis) {
        origin = data.origin[axis];
        const bool zeroDir = (data.dirOp[axis] == RayData::DirectionOp::Zero);
        if (zeroDir && (origin < bounds.minimum[axis] || origin > bounds.maximum[axis])) {
            // Pickray is roughly parallel to the plane of the slab
            // so, if the origin is not in the range, we have no intersection
            return { -1.0f, -1.0f, nullptr };
        }
        if (!zeroDir) {
            // Shrink the intersections to find the closest hit
            tmax = std::min(((*barray[1-quint8(data.dirOp[axis])])[axis] - origin) * data.directionInvers[axis], tmax);
            tmin = std::max(((*barray[quint8(data.dirOp[axis])])[axis] - origin) * data.directionInvers[axis], tmin);
        }
    }

    return { tmin, tmax, &bounds };
}
//  -----------------------------------------------------------------------

//  QSSGRenderRay::QSSGRenderRay()
extern "C" Q_DECL_EXPORT
QSSGRenderRay *ritual_ZN13QSSGRenderRayC1Ev() {
  return new QSSGRenderRay();
}

//  QSSGRenderRay::QSSGRenderRay(const QVector3D &inOrigin, const QVector3D
//      &inDirection)
extern "C" Q_DECL_EXPORT
QSSGRenderRay *ritual_ZN13QSSGRenderRayC1ERK9QVector3DS2_(
    const QVector3D *inOrigin,
    const QVector3D *inDirection) {
  return new QSSGRenderRay(*inOrigin, *inDirection);
}

//  RayData QSSGRenderRay::createRayData(const QMatrix4x4 &globalTransform,
//      const QSSGRenderRay &ray)
extern "C" Q_DECL_EXPORT
QSSGRenderRay::RayData *ritual_ZN13QSSGRenderRay13createRayDataERK10QMatrix4x4RKS_(
    const QMatrix4x4 *globalTransform,
    const QSSGRenderRay *ray) {
  return new QSSGRenderRay::RayData(
      QSSGRenderRay::createRayData(
          *globalTransform,
          *ray));
}

//  IntersectionResult QSSGRenderRay::createIntersectionResult(const RayData
//      &data, const HitResult &hit)
extern "C" Q_DECL_EXPORT
QSSGRenderRay::IntersectionResult *ritual_ZN13QSSGRenderRay24createIntersectionResultERKNS_7RayDataERKNS_9HitResultE(
    const QSSGRenderRay::RayData *data,
    const QSSGRenderRay::HitResult *hit) {
  return new QSSGRenderRay::IntersectionResult(
      QSSGRenderRay::createIntersectionResult(
          *data,
          *hit));
}

//  HitResult QSSGRenderRay::intersectWithAABBv2(const RayData &data, const
//      QSSGBounds3 &bounds)
extern "C" Q_DECL_EXPORT
QSSGRenderRay::HitResult *ritual_ZN13QSSGRenderRay19intersectWithAABBv2ERKNS_7RayDataERK11QSSGBounds3(
    const QSSGRenderRay::RayData *data,
    const QSSGBounds3 *bounds) {
  return new QSSGRenderRay::HitResult(
      QSSGRenderRay::intersectWithAABBv2(
          *data,
          *bounds));
}

//  QSSGRenderRay::~QSSGRenderRay()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGRenderRayD1Ev(QSSGRenderRay *self) {
  delete self;
}
