//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qplanegeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qplanegeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qplanegeometry.h>
#include <Qt3DExtras/private/qplanegeometry_p.h>
#include <Qt3DCore/qattribute.h>
#include <Qt3DCore/qbuffer.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/geometries/qplanegeometry.cpp, line 21, as local:qplanegeometry.cpp:createPlaneVertexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline QByteArray createPlaneVertexData(float w, float h, const QSize &resolution, bool mirrored)
{
    Q_ASSERT(w > 0.0f);
    Q_ASSERT(h > 0.0f);
    Q_ASSERT(resolution.width() >= 2);
    Q_ASSERT(resolution.height() >= 2);

    const int nVerts = resolution.width() * resolution.height();

    // Populate a buffer with the interleaved per-vertex data with
    // vec3 pos, vec2 texCoord, vec3 normal, vec4 tangent
    const quint32 elementSize = 3 + 2 + 3 + 4;
    const quint32 stride = elementSize * sizeof(float);
    QByteArray bufferBytes;
    bufferBytes.resize(stride * nVerts);
    float* fptr = reinterpret_cast<float*>(bufferBytes.data());

    const float x0 = -w / 2.0f;
    const float z0 = -h / 2.0f;
    const float dx = w / (resolution.width() - 1);
    const float dz = h / (resolution.height() - 1);
    const float du = 1.0 / (resolution.width() - 1);
    const float dv = 1.0 / (resolution.height() - 1);

    // Iterate over z
    for (int j = 0; j < resolution.height(); ++j) {
        const float z = z0 + static_cast<float>(j) * dz;
        const float v = static_cast<float>(j) * dv;

        // Iterate over x
        for (int i = 0; i < resolution.width(); ++i) {
            const float x = x0 + static_cast<float>(i) * dx;
            const float u = static_cast<float>(i) * du;

            // position
            *fptr++ = x;
            *fptr++ = 0.0;
            *fptr++ = z;

            // texture coordinates
            *fptr++ = u;
            *fptr++ = mirrored ? 1.0f - v : v;

            // normal
            *fptr++ = 0.0f;
            *fptr++ = 1.0f;
            *fptr++ = 0.0f;

            // tangent
            *fptr++ = 1.0f;
            *fptr++ = 0.0f;
            *fptr++ = 0.0f;
            *fptr++ = 1.0f;
        }
    }

    return bufferBytes;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qplanegeometry.cpp, line 80, as local:qplanegeometry.cpp:createPlaneIndexData
namespace Qt3DExtras {
using namespace Qt3DCore;
namespace {
inline QByteArray createPlaneIndexData(const QSize &resolution)
{
    // Create the index data. 2 triangles per rectangular face
    const int faces = 2 * (resolution.width() - 1) * (resolution.height() - 1);
    const qsizetype indices = 3 * faces;
    Q_ASSERT(indices < std::numeric_limits<quint16>::max());
    QByteArray indexBytes;
    indexBytes.resize(indices * sizeof(quint16));
    quint16* indexPtr = reinterpret_cast<quint16*>(indexBytes.data());

    // Iterate over z
    for (int j = 0; j < resolution.height() - 1; ++j) {
        const int rowStartIndex = j * resolution.width();
        const int nextRowStartIndex = (j + 1) * resolution.width();

        // Iterate over x
        for (int i = 0; i < resolution.width() - 1; ++i) {
            // Split quad into two triangles
            *indexPtr++ = rowStartIndex + i;
            *indexPtr++ = nextRowStartIndex + i;
            *indexPtr++ = rowStartIndex + i + 1;

            *indexPtr++ = nextRowStartIndex + i;
            *indexPtr++ = nextRowStartIndex + i + 1;
            *indexPtr++ = rowStartIndex + i + 1;
        }
    }

    return indexBytes;
}
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qplanegeometry.cpp, line 389, as _ZN10Qt3DExtras21QPlaneGeometryPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QPlaneGeometryPrivate::QPlaneGeometryPrivate()
    : QGeometryPrivate()
    , m_width(1.0f)
    , m_height(1.0f)
    , m_meshResolution(QSize(2, 2))
    , m_mirrored(false)
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

//  from ../qt3d/src/extras/geometries/qplanegeometry.cpp, line 405, as _ZN10Qt3DExtras21QPlaneGeometryPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QPlaneGeometryPrivate::init()
{
    Q_Q(QPlaneGeometry);
    m_positionAttribute = new QAttribute(q);
    m_normalAttribute = new QAttribute(q);
    m_texCoordAttribute = new QAttribute(q);
    m_tangentAttribute = new QAttribute(q);
    m_indexAttribute = new QAttribute(q);
    m_vertexBuffer = new Qt3DCore::QBuffer(q);
    m_indexBuffer = new Qt3DCore::QBuffer(q);

    const int nVerts = m_meshResolution.width() * m_meshResolution.height();
    const int stride = (3 + 2 + 3 + 4) * sizeof(float);
    const int faces = 2 * (m_meshResolution.width() - 1) * (m_meshResolution.height() - 1);

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

    // Each primitive has 3 vertives
    m_indexAttribute->setCount(faces * 3);

    m_vertexBuffer->setData(generateVertexData());
    m_indexBuffer->setData(generateIndexData());

    q->addAttribute(m_positionAttribute);
    q->addAttribute(m_texCoordAttribute);
    q->addAttribute(m_normalAttribute);
    q->addAttribute(m_tangentAttribute);
    q->addAttribute(m_indexAttribute);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qplanegeometry.cpp, line 472, as _ZNK10Qt3DExtras21QPlaneGeometryPrivate18generateVertexDataEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QByteArray QPlaneGeometryPrivate::generateVertexData() const
{
    return createPlaneVertexData(m_width, m_height, m_meshResolution, m_mirrored);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/geometries/qplanegeometry.cpp, line 477, as _ZNK10Qt3DExtras21QPlaneGeometryPrivate17generateIndexDataEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QByteArray QPlaneGeometryPrivate::generateIndexData() const
{
    return createPlaneIndexData(m_meshResolution);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QPlaneGeometryPrivate that Python can take functions over in. Every Qt3DExtras::QPlaneGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QPlaneGeometryPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QPlaneGeometryPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QPlaneGeometryPrivate : public Qt3DExtras::QPlaneGeometryPrivate {
public:
  using Qt3DExtras::QPlaneGeometryPrivate::QPlaneGeometryPrivate;
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
      CuteQt3DExtras_QPlaneGeometryPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::setScene(scene);
  }

  //  void Qt3DCore::QGeometryPrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QPlaneGeometryPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::update();
  }
};

//  Qt3DExtras::QPlaneGeometryPrivate::QPlaneGeometryPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPlaneGeometryPrivate *ritual_ZN10Qt3DExtras21QPlaneGeometryPrivateC1Ev() {
  return new CuteQt3DExtras_QPlaneGeometryPrivate();
}

//  void Qt3DExtras::QPlaneGeometryPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QPlaneGeometryPrivate4initEv(
    Qt3DExtras::QPlaneGeometryPrivate *self) {
  self->init();
}

//  QPlaneGeometry *Qt3DExtras::QPlaneGeometryPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPlaneGeometry *ritual_ZN10Qt3DExtras21QPlaneGeometryPrivate6q_funcEv(
    Qt3DExtras::QPlaneGeometryPrivate *self) {
  return self->q_func();
}

//  const QPlaneGeometry *Qt3DExtras::QPlaneGeometryPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPlaneGeometry *ritual_ZNK10Qt3DExtras21QPlaneGeometryPrivate6q_funcEv(
    const Qt3DExtras::QPlaneGeometryPrivate *self) {
  return self->q_func();
}

//  QByteArray Qt3DExtras::QPlaneGeometryPrivate::generateVertexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DExtras21QPlaneGeometryPrivate18generateVertexDataEv(
    const Qt3DExtras::QPlaneGeometryPrivate *self) {
  return new QByteArray(self->generateVertexData());
}

//  QByteArray Qt3DExtras::QPlaneGeometryPrivate::generateIndexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DExtras21QPlaneGeometryPrivate17generateIndexDataEv(
    const Qt3DExtras::QPlaneGeometryPrivate *self) {
  return new QByteArray(self->generateIndexData());
}

//  a Python function taken by a CuteQt3DExtras_QPlaneGeometryPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPlaneGeometryPrivate(
    Qt3DExtras::QPlaneGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPlaneGeometryPrivate *>(self)->take(key, call);
}
