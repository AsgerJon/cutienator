//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgplane_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <optional>
#include <QtGui/QVector3D>
#include <QtCore/QVector>
#include <QtGui/QVector2D>
#include <QtGui/QMatrix4x4>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 20, as _ZN13QSSGRenderRay9intersectERK9QSSGPlaneRKS_
inline std::optional<QVector3D> QSSGRenderRay::intersect(const QSSGPlane &inPlane, const QSSGRenderRay &ray)
{
    float Vd = QVector3D::dotProduct(inPlane.n, ray.direction);
    if (std::abs(Vd) < .0001f)
        return std::nullopt;
    float V0 = -1.0f * (QVector3D::dotProduct(inPlane.n, ray.origin) + inPlane.d);
    float t = V0 / Vd;
    return ray.origin + (ray.direction * t);
}

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 117, as _ZN13QSSGRenderRay17triangleIntersectERKS_RK9QVector3DS4_S4_RfS5_RS2_16QSSGCullFaceMode
inline bool QSSGRenderRay::triangleIntersect(const QSSGRenderRay &ray,
                                      const QVector3D &v0,
                                      const QVector3D &v1,
                                      const QVector3D &v2,
                                      float &u,
                                      float &v,
                                      QVector3D &normal,
                                      QSSGCullFaceMode cullMode)
{
    const float epsilon = std::numeric_limits<float>::epsilon();

    // Compute the Triangle's Edges
    const QVector3D edge1 = v1 - v0;
    const QVector3D edge2 = v2 - v0;

    // Compute the vector P as the cross product of the ray direction and edge2
    const QVector3D P = QVector3D::crossProduct(ray.direction, edge2);

    // Compute the determinant
    const float determinant = QVector3D::dotProduct(edge1, P);

    // If the determinant is near zero the ray lies in the plane of the triangle.
    if (std::abs(determinant) < epsilon)
        return false;

    // A positive determinant means the ray hit the front face
    const bool frontFacing = determinant > 0.0f;
    switch (cullMode) {
    case QSSGCullFaceMode::Unknown:
    case QSSGCullFaceMode::Back:
        if (!frontFacing)
            return false;
        break;
    case QSSGCullFaceMode::Front:
        if (frontFacing)
            return false;
        break;
    case QSSGCullFaceMode::FrontAndBack:
        return false;
    case QSSGCullFaceMode::Disabled:
        break;
    }

    const float invDeterminant = 1.0f / determinant;

    // Compute the vector T from the ray origin to the first vertex of the triangle
    const QVector3D T = ray.origin - v0;

    // Calculate coordinate u and test bounds
    u = QVector3D::dotProduct(T, P) * invDeterminant;
    if (u < 0.0f || u > 1.0f)
        return false;

    // Compute the vector Q as the cross product of vector T and edge1
    const QVector3D Q = QVector3D::crossProduct(T, edge1);

    // Calculate coordinate v and test bounds
    v = QVector3D::dotProduct(ray.direction, Q) * invDeterminant;
    if (v < 0.0f || ((u + v) > 1.0f))
        return false;

    // Calculate the value of t, the parameter of the intersection point along the ray
    const float t = QVector3D::dotProduct(edge2, Q) * invDeterminant;

    if (t > epsilon) {
        normal = QVector3D::crossProduct(edge1, edge2).normalized();
        return true;
    }

    return false;
}

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

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 190, as _ZN13QSSGRenderRay16intersectWithBVHERKNS_7RayDataEPK15QSSGMeshBVHNodePK14QSSGRenderMeshR5QListINS_18IntersectionResultEE16QSSGCullFaceModei
inline void QSSGRenderRay::intersectWithBVH(const RayData &data,
                                     const QSSGMeshBVHNode *bvh,
                                     const QSSGRenderMesh *mesh,
                                     QVector<IntersectionResult> &intersections,
                                     QSSGCullFaceMode cullMode,
                                     int depth)
{
    if (!bvh || !mesh || !mesh->bvh)
        return;

    // If this is a leaf node, process it's triangles
    if (bvh->count != 0) {
        // If there is an intersection on a leaf node, then test against geometry
        auto results = intersectWithBVHTriangles(data, mesh->bvh->triangles(), bvh->offset, bvh->count, cullMode);
        if (!results.isEmpty())
            intersections.append(results);
        return;
    }

    auto hit = QSSGRenderRay::intersectWithAABBv2(data, bvh->left->boundingData);
    if (hit.intersects())
        intersectWithBVH(data, static_cast<const QSSGMeshBVHNode *>(bvh->left), mesh, intersections, cullMode, depth + 1);

    hit = QSSGRenderRay::intersectWithAABBv2(data, bvh->right->boundingData);
    if (hit.intersects())
        intersectWithBVH(data, static_cast<const QSSGMeshBVHNode *>(bvh->right), mesh, intersections, cullMode, depth + 1);
}

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 220, as _ZN13QSSGRenderRay25intersectWithBVHTrianglesERKNS_7RayDataERKSt6vectorI19QSSGMeshBVHTriangleSaIS4_EEii16QSSGCullFaceMode
inline QVector<QSSGRenderRay::IntersectionResult> QSSGRenderRay::intersectWithBVHTriangles(const RayData &data,
                                                                                    const QSSGMeshBVHTriangles &bvhTriangles,
                                                                                    int triangleOffset,
                                                                                    int triangleCount,
                                                                                    QSSGCullFaceMode cullMode)
{
    Q_ASSERT(bvhTriangles.size() >= size_t(triangleOffset + triangleCount));

    QVector<QSSGRenderRay::IntersectionResult> results;

    for (int i = triangleOffset; i < triangleCount + triangleOffset; ++i) {
        const auto &triangle = bvhTriangles[i];

        QSSGRenderRay relativeRay(data.origin, data.direction);

        // Use Barycentric Coordinates to get the intersection values
        float u = 0.f;
        float v = 0.f;
        QVector3D normal;
        const bool intersects = triangleIntersect(relativeRay,
                                                  triangle.vertex1,
                                                  triangle.vertex2,
                                                  triangle.vertex3,
                                                  u,
                                                  v,
                                                  normal,
                                                  cullMode);
        if (intersects) {
            const float w = 1.0f - u - v;
            const QVector3D localIntersectionPoint = w * triangle.vertex1 +
                                                     u * triangle.vertex2 +
                                                     v * triangle.vertex3;

            const QVector2D uvCoordinate = w * triangle.uvCoord1 +
                                           u * triangle.uvCoord2 +
                                           v * triangle.uvCoord3;
            // Get the intersection point in scene coordinates
            const QVector3D sceneIntersectionPos = QSSGUtils::mat44::transform(data.globalTransform,
                                                                    localIntersectionPoint);
            const QVector3D hitVector = data.ray.origin - sceneIntersectionPos;
            // Get the magnitude of the hit vector
            const float rayLengthSquared = QSSGUtils::vec3::magnitudeSquared(hitVector);

            // Get the normal vector in scene coordinates
            const QMatrix3x3 normalMatrix = data.globalTransform.normalMatrix();
            const QVector3D sceneNormal = QSSGUtils::mat33::transform(normalMatrix, normal);

            results.append(IntersectionResult(rayLengthSquared,
                                              uvCoordinate,
                                              sceneIntersectionPos,
                                              localIntersectionPoint,
                                              normal,
                                              sceneNormal));
        }
    }

    // Does not intersect with any of the triangles
    return results;
}

//  from ../qtquick3d/src/runtimerender/qssgrenderray.cpp, line 280, as _ZNK13QSSGRenderRay8relativeERK10QMatrix4x4RK11QSSGBounds321QSSGRenderBasisPlanes
inline std::optional<QVector2D> QSSGRenderRay::relative(const QMatrix4x4 &inGlobalTransform,
                                                     const QSSGBounds3 &inBounds,
                                                     QSSGRenderBasisPlanes inPlane) const
{
    QMatrix4x4 theOriginTransform = inGlobalTransform.inverted();

    QVector3D theTransformedOrigin = QSSGUtils::mat44::transform(theOriginTransform, origin);
    float *outOriginTransformPtr(theOriginTransform.data());
    outOriginTransformPtr[12] = outOriginTransformPtr[13] = outOriginTransformPtr[14] = 0.0f;
    QVector3D theTransformedDirection = QSSGUtils::mat44::rotate(theOriginTransform, direction);

    // The XY plane is going to be a plane with either positive or negative Z direction that runs
    // through
    QVector3D theDirection(0, 0, 1);
    QVector3D theRight(1, 0, 0);
    QVector3D theUp(0, 1, 0);
    switch (inPlane) {
    case QSSGRenderBasisPlanes::XY:
        break;
    case QSSGRenderBasisPlanes::XZ:
        theDirection = QVector3D(0, 1, 0);
        theUp = QVector3D(0, 0, 1);
        break;
    case QSSGRenderBasisPlanes::YZ:
        theDirection = QVector3D(1, 0, 0);
        theRight = QVector3D(0, 0, 1);
        break;
    }
    QSSGPlane thePlane(theDirection,
                         QVector3D::dotProduct(theDirection, theTransformedDirection) > 0.0f
                                 ? QVector3D::dotProduct(theDirection, inBounds.maximum)
                                 : QVector3D::dotProduct(theDirection, inBounds.minimum));

    const QSSGRenderRay relativeRay(theTransformedOrigin, theTransformedDirection);
    std::optional<QVector3D> localIsect = QSSGRenderRay::intersect(thePlane, relativeRay);
    if (localIsect.has_value()) {
        float xRange = QVector3D::dotProduct(theRight, inBounds.maximum) - QVector3D::dotProduct(theRight, inBounds.minimum);
        float yRange = QVector3D::dotProduct(theUp, inBounds.maximum) - QVector3D::dotProduct(theUp, inBounds.minimum);
        float xOrigin = xRange / 2.0f + QVector3D::dotProduct(theRight, inBounds.minimum);
        float yOrigin = yRange / 2.0f + QVector3D::dotProduct(theUp, inBounds.minimum);
        return QVector2D((QVector3D::dotProduct(theRight, *localIsect) - xOrigin) / xRange,
                         (QVector3D::dotProduct(theUp, *localIsect) - yOrigin) / yRange);
    }
    return std::nullopt;
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

//  std::optional<QVector3D> QSSGRenderRay::intersect(const QSSGPlane
//      &inPlane, const QSSGRenderRay &ray)
extern "C" Q_DECL_EXPORT
std::optional<QVector3D> *ritual_ZN13QSSGRenderRay9intersectERK9QSSGPlaneRKS_(
    const QSSGPlane *inPlane,
    const QSSGRenderRay *ray) {
  return new std::optional<QVector3D>(
      QSSGRenderRay::intersect(
          *inPlane,
          *ray));
}

//  bool QSSGRenderRay::triangleIntersect(const QSSGRenderRay &ray, const
//      QVector3D &v0, const QVector3D &v1, const QVector3D &v2, float &u,
//      float &v, QVector3D &normal, QSSGCullFaceMode cullMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSSGRenderRay17triangleIntersectERKS_RK9QVector3DS4_S4_RfS5_RS2_16QSSGCullFaceMode(
    const QSSGRenderRay *ray,
    const QVector3D *v0,
    const QVector3D *v1,
    const QVector3D *v2,
    float *u,
    float *v,
    QVector3D *normal,
    QSSGCullFaceMode cullMode) {
  return QSSGRenderRay::triangleIntersect(
      *ray,
      *v0,
      *v1,
      *v2,
      *u,
      *v,
      *normal,
      cullMode);
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

//  void QSSGRenderRay::intersectWithBVH(const RayData &data, const
//      QSSGMeshBVHNode *bvh, const QSSGRenderMesh *mesh,
//      QVector<IntersectionResult> &intersections, QSSGCullFaceMode
//      cullMode, int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGRenderRay16intersectWithBVHERKNS_7RayDataEPK15QSSGMeshBVHNodePK14QSSGRenderMeshR5QListINS_18IntersectionResultEE16QSSGCullFaceModei(
    const QSSGRenderRay::RayData *data,
    const QSSGMeshBVHNode *bvh,
    const QSSGRenderMesh *mesh,
    QVector<QSSGRenderRay::IntersectionResult> *intersections,
    QSSGCullFaceMode cullMode,
    int depth) {
  QSSGRenderRay::intersectWithBVH(
      *data,
      bvh,
      mesh,
      *intersections,
      cullMode,
      depth);
}

//  QVector<IntersectionResult>
//      QSSGRenderRay::intersectWithBVHTriangles(const RayData &data, const
//      std::vector<QSSGMeshBVHTriangle> &bvhTriangles, int triangleOffset,
//      int triangleCount, QSSGCullFaceMode cullMode)
extern "C" Q_DECL_EXPORT
QVector<QSSGRenderRay::IntersectionResult> *ritual_ZN13QSSGRenderRay25intersectWithBVHTrianglesERKNS_7RayDataERKSt6vectorI19QSSGMeshBVHTriangleSaIS4_EEii16QSSGCullFaceMode(
    const QSSGRenderRay::RayData *data,
    const std::vector<QSSGMeshBVHTriangle> *bvhTriangles,
    int triangleOffset,
    int triangleCount,
    QSSGCullFaceMode cullMode) {
  return new QVector<QSSGRenderRay::IntersectionResult>(
      QSSGRenderRay::intersectWithBVHTriangles(
          *data,
          *bvhTriangles,
          triangleOffset,
          triangleCount,
          cullMode));
}

//  std::optional<QVector2D> QSSGRenderRay::relative(const QMatrix4x4
//      &inGlobalTransform, const QSSGBounds3 &inBounds,
//      QSSGRenderBasisPlanes inPlane) const
extern "C" Q_DECL_EXPORT
std::optional<QVector2D> *ritual_ZNK13QSSGRenderRay8relativeERK10QMatrix4x4RK11QSSGBounds321QSSGRenderBasisPlanes(
    const QSSGRenderRay *self,
    const QMatrix4x4 *inGlobalTransform,
    const QSSGBounds3 *inBounds,
    QSSGRenderBasisPlanes inPlane) {
  return new std::optional<QVector2D>(
      self->relative(
          *inGlobalTransform,
          *inBounds,
          inPlane));
}

//  std::optional<QVector2D> QSSGRenderRay::relativeXY(const QMatrix4x4
//      &inGlobalTransform, const QSSGBounds3 &inBounds) const
extern "C" Q_DECL_EXPORT
std::optional<QVector2D> *ritual_ZNK13QSSGRenderRay10relativeXYERK10QMatrix4x4RK11QSSGBounds3(
    const QSSGRenderRay *self,
    const QMatrix4x4 *inGlobalTransform,
    const QSSGBounds3 *inBounds) {
  return new std::optional<QVector2D>(
      self->relativeXY(
          *inGlobalTransform,
          *inBounds));
}

//  QSSGRenderRay::~QSSGRenderRay()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGRenderRayD1Ev(QSSGRenderRay *self) {
  delete self;
}

//  a std::optional<QVector3D> a ritual of QSSGRenderRay gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderRay__std_optional_QVector3D(
    std::optional<QVector3D> *self) {
  delete self;
}

//  a QVector<QSSGRenderRay::IntersectionResult> a ritual of QSSGRenderRay
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderRay__QVector_QSSGRenderRay_IntersectionResult(
    QVector<QSSGRenderRay::IntersectionResult> *self) {
  delete self;
}

//  a std::optional<QVector2D> a ritual of QSSGRenderRay gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderRay__std_optional_QVector2D(
    std::optional<QVector2D> *self) {
  delete self;
}
