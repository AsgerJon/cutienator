//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qspheregeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qspheregeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qspheregeometry.h>
#include <Qt3DExtras/private/qspheregeometry_p.h>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/geometries/qspheregeometry.cpp, line 26, as local:qspheregeometry.cpp:createSphereMeshVertexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline QByteArray createSphereMeshVertexData(float radius, int rings, int slices)
{
    QByteArray bufferBytes;
    // vec3 pos, vec2 texCoord, vec3 normal, vec4 tangent
    const quint32 elementSize = 3 + 2 + 3 + 4;
    const quint32 stride = elementSize * sizeof(float);
    const int nVerts  = (slices + 1) * (rings + 1);
    bufferBytes.resize(stride * nVerts);

    float* fptr = reinterpret_cast<float*>(bufferBytes.data());

    const float dTheta = (M_PI * 2) / static_cast<float>( slices );
    const float dPhi = M_PI / static_cast<float>( rings );
    const float du = 1.0f / static_cast<float>( slices );
    const float dv = 1.0f / static_cast<float>( rings );

    // Iterate over latitudes (rings)
    for ( int lat = 0; lat < rings + 1; ++lat )
    {
        const float phi = M_PI_2 - static_cast<float>( lat ) * dPhi;
        const float cosPhi = qCos( phi );
        const float sinPhi = qSin( phi );
        const float v = 1.0f - static_cast<float>( lat ) * dv;

        // Iterate over longitudes (slices)
        for ( int lon = 0; lon < slices + 1; ++lon )
        {
            const float theta = static_cast<float>( lon ) * dTheta;
            const float cosTheta = qCos( theta );
            const float sinTheta = qSin( theta );
            const float u = static_cast<float>( lon ) * du;

            *fptr++ = radius * cosTheta * cosPhi;
            *fptr++ = radius * sinPhi;
            *fptr++ = radius * sinTheta * cosPhi;

            *fptr++ = u;
            *fptr++ = v;

            *fptr++   = cosTheta * cosPhi;
            *fptr++ = sinPhi;
            *fptr++ = sinTheta * cosPhi;

            *fptr++ = sinTheta;
            *fptr++ = 0.0;
            *fptr++ = -cosTheta;
            *fptr++ = 1.0;
        }
    }
    return bufferBytes;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qspheregeometry.cpp, line 78, as local:qspheregeometry.cpp:createSphereMeshIndexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline QByteArray createSphereMeshIndexData(int rings, int slices)
{
    int faces = (slices * 2) * (rings - 2); // two tris per slice, for all middle rings
    faces += 2 * slices; // tri per slice for both top and bottom

    QByteArray indexBytes;
    const qsizetype indices = faces * 3;
    Q_ASSERT(indices < 65536);
    indexBytes.resize(indices * sizeof(quint16));
    quint16 *indexPtr = reinterpret_cast<quint16*>(indexBytes.data());

    // top cap
    {
        const int nextRingStartIndex = slices + 1;
        for ( int j = 0; j < slices; ++j )
        {
            *indexPtr++ = nextRingStartIndex + j;
            *indexPtr++ = 0;
            *indexPtr++ = nextRingStartIndex + j + 1;
        }
    }

    for ( int i = 1; i < (rings - 1); ++i )
    {
        const int ringStartIndex = i * ( slices + 1 );
        const int nextRingStartIndex = ( i + 1 ) * ( slices + 1 );

        for ( int j = 0; j < slices; ++j )
        {
            // Split the quad into two triangles
            *indexPtr++ = ringStartIndex + j;
            *indexPtr++ = ringStartIndex + j + 1;
            *indexPtr++ = nextRingStartIndex + j;
            *indexPtr++ = nextRingStartIndex + j;
            *indexPtr++ = ringStartIndex + j + 1;
            *indexPtr++ = nextRingStartIndex + j + 1;
        }
    }

    // bottom cap
    {
        const int ringStartIndex = (rings - 1) * ( slices + 1);
        const int nextRingStartIndex = (rings) * ( slices + 1);
        for ( int j = 0; j < slices; ++j )
        {
            *indexPtr++ = ringStartIndex + j + 1;
            *indexPtr++ = nextRingStartIndex;
            *indexPtr++ = ringStartIndex + j;
        }
    }

    return indexBytes;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qspheregeometry.cpp, line 134, as _ZN10Qt3DExtras22QSphereGeometryPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QSphereGeometryPrivate::QSphereGeometryPrivate()
    : QGeometryPrivate()
    , m_generateTangents(false)
    , m_rings(16)
    , m_slices(16)
    , m_radius(1.0f)
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

//  from ../qt3d/src/extras/geometries/qspheregeometry.cpp, line 150, as _ZN10Qt3DExtras22QSphereGeometryPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QSphereGeometryPrivate::init()
{
    Q_Q(QSphereGeometry);
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
    const int nVerts = (m_slices + 1) * (m_rings + 1);
    const int faces = (m_slices * 2) * (m_rings - 2) + (2 * m_slices);

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

    m_indexAttribute->setCount(faces * 3);

    m_vertexBuffer->setData(generateVertexData());
    m_indexBuffer->setData(generateIndexData());

    q->addAttribute(m_positionAttribute);
    q->addAttribute(m_texCoordAttribute);
    q->addAttribute(m_normalAttribute);
    if (m_generateTangents)
        q->addAttribute(m_tangentAttribute);
    q->addAttribute(m_indexAttribute);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qspheregeometry.cpp, line 219, as _ZNK10Qt3DExtras22QSphereGeometryPrivate18generateVertexDataEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QByteArray QSphereGeometryPrivate::generateVertexData() const
{
    return createSphereMeshVertexData(m_radius, m_rings, m_slices);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qspheregeometry.cpp, line 224, as _ZNK10Qt3DExtras22QSphereGeometryPrivate17generateIndexDataEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QByteArray QSphereGeometryPrivate::generateIndexData() const
{
    return createSphereMeshIndexData(m_rings, m_slices);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QSphereGeometryPrivate that Python can take functions over in. Every Qt3DExtras::QSphereGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QSphereGeometryPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QSphereGeometryPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QSphereGeometryPrivate : public Qt3DExtras::QSphereGeometryPrivate {
public:
  using Qt3DExtras::QSphereGeometryPrivate::QSphereGeometryPrivate;
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
      CuteQt3DExtras_QSphereGeometryPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::setScene(scene);
  }

  //  void Qt3DCore::QGeometryPrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QSphereGeometryPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QSphereGeometryPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::update();
  }
};

//  Qt3DExtras::QSphereGeometryPrivate::QSphereGeometryPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSphereGeometryPrivate *ritual_ZN10Qt3DExtras22QSphereGeometryPrivateC1Ev() {
  return new CuteQt3DExtras_QSphereGeometryPrivate();
}

//  void Qt3DExtras::QSphereGeometryPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QSphereGeometryPrivate4initEv(
    Qt3DExtras::QSphereGeometryPrivate *self) {
  self->init();
}

//  QSphereGeometry *Qt3DExtras::QSphereGeometryPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSphereGeometry *ritual_ZN10Qt3DExtras22QSphereGeometryPrivate6q_funcEv(
    Qt3DExtras::QSphereGeometryPrivate *self) {
  return self->q_func();
}

//  const QSphereGeometry *Qt3DExtras::QSphereGeometryPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSphereGeometry *ritual_ZNK10Qt3DExtras22QSphereGeometryPrivate6q_funcEv(
    const Qt3DExtras::QSphereGeometryPrivate *self) {
  return self->q_func();
}

//  QByteArray Qt3DExtras::QSphereGeometryPrivate::generateVertexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DExtras22QSphereGeometryPrivate18generateVertexDataEv(
    const Qt3DExtras::QSphereGeometryPrivate *self) {
  return new QByteArray(self->generateVertexData());
}

//  QByteArray Qt3DExtras::QSphereGeometryPrivate::generateIndexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DExtras22QSphereGeometryPrivate17generateIndexDataEv(
    const Qt3DExtras::QSphereGeometryPrivate *self) {
  return new QByteArray(self->generateIndexData());
}

//  a Python function taken by a CuteQt3DExtras_QSphereGeometryPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QSphereGeometryPrivate(
    Qt3DExtras::QSphereGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QSphereGeometryPrivate *>(self)->take(key, call);
}
