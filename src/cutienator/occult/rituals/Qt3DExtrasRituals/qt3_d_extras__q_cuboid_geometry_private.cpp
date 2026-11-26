//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qcuboidgeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qcuboidgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qcuboidgeometry.h>
#include <Qt3DExtras/private/qcuboidgeometry_p.h>
#include <Qt3DCore/qattribute.h>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/private/corelogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/geometries/qcuboidgeometry.cpp, line 20, as local:qcuboidgeometry.cpp:PositiveX
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
enum PlaneNormal {
    PositiveX,
    NegativeX,
    PositiveY,
    NegativeY,
    PositiveZ,
    NegativeZ
};
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcuboidgeometry.cpp, line 29, as local:qcuboidgeometry.cpp:createPlaneVertexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline void createPlaneVertexData(float w, float h, const QSize &resolution,
                           PlaneNormal normal, float planeDistance,
                           float *vertices)
{
    const float a0 = -w / 2.0f;
    const float b0 = -h / 2.0f;
    const float da = w / (resolution.width() - 1);
    const float db = h / (resolution.height() - 1);
    const float du = 1.0f / (resolution.width() - 1);
    const float dv = 1.0f / (resolution.height() - 1);

    switch (normal) {
    case NegativeX:
        // Iterate over z
        for (int j = resolution.height() - 1; j >= 0; --j) {
            const float b = b0 + static_cast<float>(j) * db;
            const float v = static_cast<float>(j) * dv;

            // Iterate over y
            for (int i = 0; i < resolution.width(); ++i) {
                const float a = a0 + static_cast<float>(i) * da;
                const float u = static_cast<float>(i) * du;

                // position
                *vertices++ = planeDistance;
                *vertices++ = a;
                *vertices++ = b;

                // texture coordinates
                *vertices++ = v;
                *vertices++ = u;

                // normal
                *vertices++ = -1.0f;
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;

                // tangent
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = 1.0f;
                *vertices++ = 1.0f;
            }
        }
        break;

    case PositiveX: {
        // Iterate over z
        for (int j = 0; j < resolution.height(); ++j) {
            const float b = b0 + static_cast<float>(j) * db;
            const float v = static_cast<float>(j) * dv;

            // Iterate over y
            for (int i = 0; i < resolution.width(); ++i) {
                const float a = a0 + static_cast<float>(i) * da;
                const float u = static_cast<float>(i) * du;

                // position
                *vertices++ = planeDistance;
                *vertices++ = a;
                *vertices++ = b;

                // texture coordinates
                *vertices++ = 1.0f - v;
                *vertices++ = u;

                // normal
                *vertices++ = 1.0f;
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;

                // tangent
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = -1.0f;
                *vertices++ = 1.0f;
            }
        }
        break;
    }

    case NegativeY:
        // Iterate over z
        for (int j = 0; j < resolution.height(); ++j) {
            const float b = b0 + static_cast<float>(j) * db;
            const float v = static_cast<float>(j) * dv;

            // Iterate over x
            // This iterates in the opposite sense to the other directions
            // so that the winding order is correct
            for (int i = 0; i < resolution.width(); ++i) {
                const float a = a0 + static_cast<float>(i) * da;
                const float u = static_cast<float>(i) * du;

                // position
                *vertices++ = a;
                *vertices++ = planeDistance;
                *vertices++ = b;

                // texture coordinates
                *vertices++ = u;
                *vertices++ = v;

                // normal
                *vertices++ = 0.0f;
                *vertices++ = -1.0f;
                *vertices++ = 0.0f;

                // tangent
                *vertices++ = 1.0f;
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = 1.0f;
            }
        }
        break;

    case PositiveY: {
        // Iterate over z
        for (int j = resolution.height() - 1; j >= 0; --j) {
            const float b = b0 + static_cast<float>(j) * db;
            const float v = static_cast<float>(j) * dv;

            // Iterate over x
            // This iterates in the opposite sense to the other directions
            // so that the winding order is correct
            for (int i = 0; i < resolution.width(); ++i) {
                const float a = a0 + static_cast<float>(i) * da;
                const float u = static_cast<float>(i) * du;

                // position
                *vertices++ = a;
                *vertices++ = planeDistance;
                *vertices++ = b;

                // texture coordinates
                *vertices++ = u;
                *vertices++ = 1.0f - v;

                // normal
                *vertices++ = 0.0f;
                *vertices++ = 1.0f;
                *vertices++ = 0.0f;

                // tangent
                *vertices++ = 1.0f;
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = 1.0f;
            }
        }
        break;
    }

    case NegativeZ:
        // Iterate over y
        for (int j = 0; j < resolution.height(); ++j) {
            const float b = b0 + static_cast<float>(j) * db;
            const float v = static_cast<float>(j) * dv;

            // Iterate over x
            for (int i = resolution.width() - 1; i >= 0; --i) {
                const float a = a0 + static_cast<float>(i) * da;
                const float u = static_cast<float>(i) * du;

                // position
                *vertices++ = a;
                *vertices++ = b;
                *vertices++ = planeDistance;

                // texture coordinates
                *vertices++ = 1.0f - u;
                *vertices++ = v;

                // normal
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = -1.0f;

                // tangent
                *vertices++ = -1.0f;
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = 1.0f;
            }
        }
        break;

    case PositiveZ: {
        // Iterate over y
        for (int j = 0; j < resolution.height(); ++j) {
            const float b = b0 + static_cast<float>(j) * db;
            const float v = static_cast<float>(j) * dv;

            // Iterate over x
            for (int i = 0; i < resolution.width(); ++i) {
                const float a = a0 + static_cast<float>(i) * da;
                const float u = static_cast<float>(i) * du;

                // position
                *vertices++ = a;
                *vertices++ = b;
                *vertices++ = planeDistance;

                // texture coordinates
                *vertices++ = u;
                *vertices++ = v;

                // normal
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = 1.0f;

                // tangent
                *vertices++ = 1.0f;
                *vertices++ = 0.0f;
                *vertices++ = 0.0f;
                *vertices++ = 1.0f;
            }
        }
        break;
    }
    } // switch (normal)
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcuboidgeometry.cpp, line 254, as local:qcuboidgeometry.cpp:createPlaneIndexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline void createPlaneIndexData(const QSize &resolution, quint16 *indices, quint16 &baseVertex)
{
    // Populate indices taking care to get correct CCW winding on all faces
    // Iterate over v direction (rows)
    for (int j = 0; j < resolution.height() - 1; ++j) {
        const int rowStartIndex = j * resolution.width() + baseVertex;
        const int nextRowStartIndex = (j + 1) * resolution.width() + baseVertex;

        // Iterate over u direction (columns)
        for (int i = 0; i < resolution.width() - 1; ++i) {
            // Split quad into two triangles
            *indices++ = rowStartIndex + i;
            *indices++ = rowStartIndex + i + 1;
            *indices++ = nextRowStartIndex + i;

            *indices++ = nextRowStartIndex + i;
            *indices++ = rowStartIndex + i + 1;
            *indices++ = nextRowStartIndex + i + 1;
        }
    }
    baseVertex += resolution.width() * resolution.height();
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qcuboidgeometry.cpp, line 350, as _ZN10Qt3DExtras22QCuboidGeometryPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QCuboidGeometryPrivate::QCuboidGeometryPrivate()
    : QGeometryPrivate()
    , m_xExtent(1.0f)
    , m_yExtent(1.0f)
    , m_zExtent(1.0f)
    , m_yzFaceResolution(2, 2)
    , m_xzFaceResolution(2, 2)
    , m_xyFaceResolution(2, 2)
    , m_positionAttribute(nullptr)
    , m_normalAttribute(nullptr)
    , m_texCoordAttribute(nullptr)
    , m_tangentAttribute(nullptr)
    , m_indexAttribute(nullptr)
    , m_vertexBuffer(nullptr)
    , m_indexBuffer(nullptr)
{
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QCuboidGeometryPrivate that Python can take functions over in. Every Qt3DExtras::QCuboidGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QCuboidGeometryPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QCuboidGeometryPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QCuboidGeometryPrivate : public Qt3DExtras::QCuboidGeometryPrivate {
public:
  using Qt3DExtras::QCuboidGeometryPrivate::QCuboidGeometryPrivate;
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
      CuteQt3DExtras_QCuboidGeometryPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::setScene(scene);
  }

  //  void Qt3DCore::QGeometryPrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QCuboidGeometryPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QCuboidGeometryPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::update();
  }
};

//  Qt3DExtras::QCuboidGeometryPrivate::QCuboidGeometryPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCuboidGeometryPrivate *ritual_ZN10Qt3DExtras22QCuboidGeometryPrivateC1Ev() {
  return new CuteQt3DExtras_QCuboidGeometryPrivate();
}

//  QCuboidGeometry *Qt3DExtras::QCuboidGeometryPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QCuboidGeometry *ritual_ZN10Qt3DExtras22QCuboidGeometryPrivate6q_funcEv(
    Qt3DExtras::QCuboidGeometryPrivate *self) {
  return self->q_func();
}

//  const QCuboidGeometry *Qt3DExtras::QCuboidGeometryPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QCuboidGeometry *ritual_ZNK10Qt3DExtras22QCuboidGeometryPrivate6q_funcEv(
    const Qt3DExtras::QCuboidGeometryPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QCuboidGeometryPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QCuboidGeometryPrivate(
    Qt3DExtras::QCuboidGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QCuboidGeometryPrivate *>(self)->take(key, call);
}
