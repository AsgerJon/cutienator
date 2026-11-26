//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qcylindergeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qcylindergeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qcylindergeometry.h>
#include <Qt3DExtras/private/qcylindergeometry_p.h>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <QtGui/QVector3D>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/geometries/qcylindergeometry.cpp, line 27, as local:qcylindergeometry.cpp:faceCount
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline int faceCount(int slices, int rings)
{
    return (slices * 2) * (rings - 1) // two tris per side, for each pair of adjacent rings
            + slices * 2; // two caps
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcylindergeometry.cpp, line 33, as local:qcylindergeometry.cpp:vertexCount
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline int vertexCount(int slices, int rings)
{
    return (slices + 1) * rings + 2 * (slices + 1) + 2;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcylindergeometry.cpp, line 38, as local:qcylindergeometry.cpp:createSidesVertices
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline void createSidesVertices(float *&verticesPtr,
                         int rings,
                         int slices,
                         double radius,
                         double length)
{
    const float dY = length / static_cast<float>(rings - 1);
    const float dTheta = (M_PI * 2) / static_cast<float>(slices);

    for (int ring = 0; ring < rings; ++ring) {
        const float y = -length / 2.0f + static_cast<float>(ring) * dY;

        for (int slice = 0; slice <= slices; ++slice) {
            const float theta = static_cast<float>(slice) * dTheta;
            const float ct = qCos(theta);
            const float st = qSin(theta);

            *verticesPtr++ = radius * ct;
            *verticesPtr++ = y;
            *verticesPtr++ = radius * st;

            *verticesPtr++ = (y + length / 2.0) / length;
            *verticesPtr++ = theta / (M_PI * 2);

            QVector3D n(ct, 0.0f, st);
            n.normalize();
            *verticesPtr++ = n.x();
            *verticesPtr++ = n.y();
            *verticesPtr++ = n.z();
        }
    }
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcylindergeometry.cpp, line 71, as local:qcylindergeometry.cpp:createSidesIndices
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline void createSidesIndices(quint16 *&indicesPtr, int rings, int slices)
{
    for (int ring = 0; ring < rings - 1; ++ring) {
        const int ringIndexStart = ring * (slices + 1);
        const int nextRingIndexStart = (ring + 1) * (slices + 1);

        for (int slice = 0; slice < slices; ++slice) {
            const int nextSlice = slice + 1;

            *indicesPtr++ = (ringIndexStart + slice);
            *indicesPtr++ = (nextRingIndexStart + slice);
            *indicesPtr++ = (ringIndexStart + nextSlice);
            *indicesPtr++ = (ringIndexStart + nextSlice);
            *indicesPtr++ = (nextRingIndexStart + slice);
            *indicesPtr++ = (nextRingIndexStart + nextSlice);
        }
    }
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcylindergeometry.cpp, line 90, as local:qcylindergeometry.cpp:createDiscVertices
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline void createDiscVertices(float *&verticesPtr,
                        int slices,
                        double radius,
                        double yPosition)
{
    const float dTheta = (M_PI * 2) / static_cast<float>(slices);
    const double yNormal = (yPosition < 0.0f) ? -1.0f : 1.0f;

    *verticesPtr++ = 0.0f;
    *verticesPtr++ = yPosition;
    *verticesPtr++ = 0.0f;

    *verticesPtr++ = 1.0f;
    *verticesPtr++ = 0.0f;

    *verticesPtr++ = 0.0f;
    *verticesPtr++ = yNormal;
    *verticesPtr++ = 0.0f;

    for (int slice = 0; slice <= slices; ++slice) {
        const float theta = static_cast<float>(slice) * dTheta;
        const float ct = qCos(theta);
        const float st = qSin(theta);

        *verticesPtr++ = radius * ct;
        *verticesPtr++ = yPosition;
        *verticesPtr++ = radius * st;

        *verticesPtr++ = 1.0f;
        *verticesPtr++ = theta / (M_PI * 2);

        *verticesPtr++ = 0.0f;
        *verticesPtr++ = yNormal;
        *verticesPtr++ = 0.0f;
    }
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcylindergeometry.cpp, line 127, as local:qcylindergeometry.cpp:createDiscIndices
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline void createDiscIndices(quint16 *&indicesPtr,
                       int discCenterIndex,
                       int slices,
                       double yPosition)
{
    const double yNormal = (yPosition < 0.0f) ? -1.0f : 1.0f;

    for (int slice = 0; slice < slices; ++slice) {
        const int nextSlice = slice + 1;

        *indicesPtr++ = discCenterIndex;
        *indicesPtr++ = (discCenterIndex + 1 + nextSlice);
        *indicesPtr++ = (discCenterIndex + 1 + slice);

        if (yNormal < 0.0f)
            qSwap(*(indicesPtr -1), *(indicesPtr - 2));
    }
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcylindergeometry.cpp, line 148, as _ZN10Qt3DExtras24QCylinderGeometryPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QCylinderGeometryPrivate::QCylinderGeometryPrivate()
    : QGeometryPrivate()
    , m_rings(16)
    , m_slices(16)
    , m_radius(1.0f)
    , m_length(1.0f)
    , m_positionAttribute(nullptr)
    , m_normalAttribute(nullptr)
    , m_texCoordAttribute(nullptr)
    , m_indexAttribute(nullptr)
    , m_vertexBuffer(nullptr)
    , m_indexBuffer(nullptr)
{
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QCylinderGeometryPrivate that Python can take functions over in. Every Qt3DExtras::QCylinderGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QCylinderGeometryPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QCylinderGeometryPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QCylinderGeometryPrivate : public Qt3DExtras::QCylinderGeometryPrivate {
public:
  using Qt3DExtras::QCylinderGeometryPrivate::QCylinderGeometryPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QGeometryPrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QCylinderGeometryPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::setScene(scene);
  }

  //  void Qt3DCore::QGeometryPrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QCylinderGeometryPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QCylinderGeometryPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::update();
  }
};

//  Qt3DExtras::QCylinderGeometryPrivate::QCylinderGeometryPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCylinderGeometryPrivate *ritual_ZN10Qt3DExtras24QCylinderGeometryPrivateC1Ev() {
  return new CuteQt3DExtras_QCylinderGeometryPrivate();
}

//  QCylinderGeometry *Qt3DExtras::QCylinderGeometryPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCylinderGeometry *ritual_ZN10Qt3DExtras24QCylinderGeometryPrivate6q_funcEv(
    Qt3DExtras::QCylinderGeometryPrivate *self) {
  return self->q_func();
}

//  const QCylinderGeometry *Qt3DExtras::QCylinderGeometryPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QCylinderGeometry *ritual_ZNK10Qt3DExtras24QCylinderGeometryPrivate6q_funcEv(
    const Qt3DExtras::QCylinderGeometryPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QCylinderGeometryPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QCylinderGeometryPrivate(
    Qt3DExtras::QCylinderGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QCylinderGeometryPrivate *>(self)->take(key, call);
}
