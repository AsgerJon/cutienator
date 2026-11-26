//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtorusgeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtorusgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qtorusgeometry.h>
#include <Qt3DExtras/private/qtorusgeometry_p.h>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <QtGui/QVector3D>
#include <QtGui/QVector4D>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 23, as local:qtorusgeometry.cpp:vertexCount
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline int vertexCount(int requestedRings, int requestedSlices)
{
    return (requestedRings + 1) * (requestedSlices + 1);
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 28, as local:qtorusgeometry.cpp:triangleCount
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline int triangleCount(int requestedRings, int requestedSlices)
{
    return 2 * requestedRings * requestedSlices;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 33, as local:qtorusgeometry.cpp:createTorusVertexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline QByteArray createTorusVertexData(double radius, double minorRadius,
                                 int rings, int slices)
{
    // The additional side and ring compared to what the user asked
    // for is because we also need to ensure proper texture coordinate
    // wrapping at the seams. Without this the last ring and side would
    // interpolate the texture coordinates from ~0.9x back down to 0
    // (the starting value at the first ring). So we insert an extra
    // ring and side with the same positions as the first ring and side
    // but with texture coordinates of 1 (compared to 0).
    const int nVerts  = vertexCount(rings, slices);
    QByteArray bufferBytes;
    // vec3 pos, vec2 texCoord, vec3 normal, vec4 tangent
    const quint32 elementSize = 3 + 2 + 3 + 4;
    const quint32 stride = elementSize * sizeof(float);
    bufferBytes.resize(stride * nVerts);

    float* fptr = reinterpret_cast<float*>(bufferBytes.data());

    const float ringFactor = (M_PI * 2) / static_cast<float>(rings);
    const float sliceFactor = (M_PI * 2) / static_cast<float>(slices);

    for (int ring = 0; ring <= rings; ++ring) {
        const float u = ring * ringFactor;
        const float cu = qCos(u);
        const float su = qSin(u);

        for (int slice = 0; slice <= slices; ++slice) {
            const float v = slice * sliceFactor;
            const float cv = qCos(v + M_PI);
            const float sv = qSin(v);
            const float r = (radius + minorRadius * cv);

            *fptr++ = r * cu;
            *fptr++ = r * su;
            *fptr++ = minorRadius * sv;

            *fptr++ = u / (M_PI * 2);
            *fptr++ = v / (M_PI * 2);

            QVector3D n(cv * cu, cv * su, sv);
            n.normalize();
            *fptr++ = n.x();
            *fptr++ = n.y();
            *fptr++ = n.z();

            QVector4D t(-su, cu, 0.0f, 1.0f);
            t.normalize();
            *fptr++ = t.x();
            *fptr++ = t.y();
            *fptr++ = t.z();
            *fptr++ = t.w();
        }
    }

    return bufferBytes;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 91, as local:qtorusgeometry.cpp:createTorusIndexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline QByteArray createTorusIndexData(int requestedRings, int requestedSlices)
{
    const int slices = requestedSlices + 1;
    int triangles = triangleCount(requestedRings, requestedSlices);
    qsizetype indices = triangles * 3;
    Q_ASSERT(indices < 65536);
    QByteArray indexBytes;
    indexBytes.resize(indices * sizeof(quint16));
    quint16* indexPtr = reinterpret_cast<quint16*>(indexBytes.data());

    for (int ring = 0; ring < requestedRings; ++ring) {
        const int ringStart = ring * slices;
        const int nextRingStart = (ring + 1) * slices;
        for (int slice = 0; slice < requestedSlices; ++slice) {
            const int nextSlice = (slice + 1) % slices;
            *indexPtr++ = ringStart + slice;
            *indexPtr++ = ringStart + nextSlice;
            *indexPtr++ = nextRingStart + slice;
            *indexPtr++ = ringStart + nextSlice;
            *indexPtr++ = nextRingStart + nextSlice;
            *indexPtr++ = nextRingStart + slice;
        }
    }

    return indexBytes;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 120, as _ZN10Qt3DExtras21QTorusGeometryPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTorusGeometryPrivate::QTorusGeometryPrivate()
    : QGeometryPrivate()
    , m_rings(16)
    , m_slices(16)
    , m_radius(1.0f)
    , m_minorRadius(1.0f)
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

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 136, as _ZN10Qt3DExtras21QTorusGeometryPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QTorusGeometryPrivate::init()
{
    Q_Q(QTorusGeometry);
    m_positionAttribute = new QAttribute(q);
    m_normalAttribute = new QAttribute(q);
    m_texCoordAttribute = new QAttribute(q);
    m_tangentAttribute = new QAttribute(q);
    m_indexAttribute = new QAttribute(q);
    m_vertexBuffer = new Qt3DCore::QBuffer(q);
    m_indexBuffer = new Qt3DCore::QBuffer(q);
    // vec3 pos, vec2 tex, vec3 normal, vec4 tangent
    const quint32 elementSize = 3 + 2 + 3 + 4;
    const quint32 stride = elementSize * sizeof(float);
    const int nVerts = vertexCount(m_rings, m_slices);
    const int triangles = triangleCount(m_rings, m_slices);

    m_positionAttribute->setName(QAttribute::defaultPositionAttributeName());
    m_positionAttribute->setVertexBaseType(QAttribute::Float);
    m_positionAttribute->setVertexSize(3);
    m_positionAttribute->setAttributeType(QAttribute::VertexAttribute);
    m_positionAttribute->setBuffer(m_vertexBuffer);
    m_positionAttribute->setByteStride(stride);
    m_positionAttribute->setCount(nVerts);

    m_texCoordAttribute->setName(QAttribute::defaultTextureCoordinateAttributeName());
    m_texCoordAttribute->setVertexBaseType(QAttribute::Float);
    m_texCoordAttribute->setVertexSize(2);
    m_texCoordAttribute->setAttributeType(QAttribute::VertexAttribute);
    m_texCoordAttribute->setBuffer(m_vertexBuffer);
    m_texCoordAttribute->setByteStride(stride);
    m_texCoordAttribute->setByteOffset(3 * sizeof(float));
    m_texCoordAttribute->setCount(nVerts);

    m_normalAttribute->setName(QAttribute::defaultNormalAttributeName());
    m_normalAttribute->setVertexBaseType(QAttribute::Float);
    m_normalAttribute->setVertexSize(3);
    m_normalAttribute->setAttributeType(QAttribute::VertexAttribute);
    m_normalAttribute->setBuffer(m_vertexBuffer);
    m_normalAttribute->setByteStride(stride);
    m_normalAttribute->setByteOffset(5 * sizeof(float));
    m_normalAttribute->setCount(nVerts);

    m_tangentAttribute->setName(QAttribute::defaultTangentAttributeName());
    m_tangentAttribute->setVertexBaseType(QAttribute::Float);
    m_tangentAttribute->setVertexSize(4);
    m_tangentAttribute->setAttributeType(QAttribute::VertexAttribute);
    m_tangentAttribute->setBuffer(m_vertexBuffer);
    m_tangentAttribute->setByteStride(stride);
    m_tangentAttribute->setByteOffset(8 * sizeof(float));
    m_tangentAttribute->setCount(nVerts);

    m_indexAttribute->setAttributeType(QAttribute::IndexAttribute);
    m_indexAttribute->setVertexBaseType(QAttribute::UnsignedShort);
    m_indexAttribute->setBuffer(m_indexBuffer);

    m_indexAttribute->setCount(triangles * 3);

    m_vertexBuffer->setData(generateVertexData());
    m_indexBuffer->setData(generateIndexData());

    q->addAttribute(m_positionAttribute);
    q->addAttribute(m_texCoordAttribute);
    q->addAttribute(m_normalAttribute);
    q->addAttribute(m_tangentAttribute);
    q->addAttribute(m_indexAttribute);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 203, as _ZNK10Qt3DExtras21QTorusGeometryPrivate18generateVertexDataEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QByteArray QTorusGeometryPrivate::generateVertexData() const
{
    return createTorusVertexData(m_radius, m_minorRadius, m_rings, m_slices);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qtorusgeometry.cpp, line 208, as _ZNK10Qt3DExtras21QTorusGeometryPrivate17generateIndexDataEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QByteArray QTorusGeometryPrivate::generateIndexData() const
{
    return createTorusIndexData(m_rings, m_slices);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QTorusGeometryPrivate that Python can take functions over in. Every Qt3DExtras::QTorusGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QTorusGeometryPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QTorusGeometryPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QTorusGeometryPrivate : public Qt3DExtras::QTorusGeometryPrivate {
public:
  using Qt3DExtras::QTorusGeometryPrivate::QTorusGeometryPrivate;
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
      CuteQt3DExtras_QTorusGeometryPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::setScene(scene);
  }

  //  void Qt3DCore::QGeometryPrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QTorusGeometryPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QTorusGeometryPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::update();
  }
};

//  Qt3DExtras::QTorusGeometryPrivate::QTorusGeometryPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTorusGeometryPrivate *ritual_ZN10Qt3DExtras21QTorusGeometryPrivateC1Ev() {
  return new CuteQt3DExtras_QTorusGeometryPrivate();
}

//  void Qt3DExtras::QTorusGeometryPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QTorusGeometryPrivate4initEv(
    Qt3DExtras::QTorusGeometryPrivate *self) {
  self->init();
}

//  QTorusGeometry *Qt3DExtras::QTorusGeometryPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTorusGeometry *ritual_ZN10Qt3DExtras21QTorusGeometryPrivate6q_funcEv(
    Qt3DExtras::QTorusGeometryPrivate *self) {
  return self->q_func();
}

//  const QTorusGeometry *Qt3DExtras::QTorusGeometryPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QTorusGeometry *ritual_ZNK10Qt3DExtras21QTorusGeometryPrivate6q_funcEv(
    const Qt3DExtras::QTorusGeometryPrivate *self) {
  return self->q_func();
}

//  QByteArray Qt3DExtras::QTorusGeometryPrivate::generateVertexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DExtras21QTorusGeometryPrivate18generateVertexDataEv(
    const Qt3DExtras::QTorusGeometryPrivate *self) {
  return new QByteArray(self->generateVertexData());
}

//  QByteArray Qt3DExtras::QTorusGeometryPrivate::generateIndexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DExtras21QTorusGeometryPrivate17generateIndexDataEv(
    const Qt3DExtras::QTorusGeometryPrivate *self) {
  return new QByteArray(self->generateIndexData());
}

//  a Python function taken by a CuteQt3DExtras_QTorusGeometryPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTorusGeometryPrivate(
    Qt3DExtras::QTorusGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTorusGeometryPrivate *>(self)->take(key, call);
}
