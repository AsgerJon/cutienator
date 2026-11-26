//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qextrudedtextgeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qextrudedtextgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qextrudedtextgeometry.h>
#include <Qt3DExtras/private/qextrudedtextgeometry_p.h>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <QtGui/private/qtriangulator_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QVector3D>
#include <QtGui/QTextLayout>
#include <QtCore/QTime>
#include <QtGui/QPainterPath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/3dtext/qextrudedtextgeometry.cpp, line 23, as local:qextrudedtextgeometry.cpp:IndexType
namespace Qt3DExtras {
namespace {
using IndexType = unsigned int;
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/3dtext/qextrudedtextgeometry.cpp, line 25, as local:qextrudedtextgeometry.cpp:TriangulationData
namespace Qt3DExtras {
namespace {
struct TriangulationData {
    struct Outline {
        int begin;
        int end;
    };

    std::vector<QVector3D> vertices;
    std::vector<IndexType> indices;
    std::vector<Outline> outlines;
    std::vector<IndexType> outlineIndices;
    bool inverted;
};
}  // namespace
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/3dtext/qextrudedtextgeometry.cpp, line 116, as _ZN10Qt3DExtras28QExtrudedTextGeometryPrivate4initEv
namespace Qt3DExtras {
inline void QExtrudedTextGeometryPrivate::init()
{
    Q_Q(QExtrudedTextGeometry);
    m_positionAttribute = new Qt3DCore::QAttribute(q);
    m_normalAttribute = new Qt3DCore::QAttribute(q);
    m_indexAttribute = new Qt3DCore::QAttribute(q);
    m_vertexBuffer = new Qt3DCore::QBuffer(q);
    m_indexBuffer = new Qt3DCore::QBuffer(q);

    const quint32 elementSize = 3 + 3;
    const quint32 stride = elementSize * sizeof(float);

    m_positionAttribute->setName(Qt3DCore::QAttribute::defaultPositionAttributeName());
    m_positionAttribute->setVertexBaseType(Qt3DCore::QAttribute::Float);
    m_positionAttribute->setVertexSize(3);
    m_positionAttribute->setAttributeType(Qt3DCore::QAttribute::VertexAttribute);
    m_positionAttribute->setBuffer(m_vertexBuffer);
    m_positionAttribute->setByteStride(stride);
    m_positionAttribute->setByteOffset(0);
    m_positionAttribute->setCount(0);

    m_normalAttribute->setName(Qt3DCore::QAttribute::defaultNormalAttributeName());
    m_normalAttribute->setVertexBaseType(Qt3DCore::QAttribute::Float);
    m_normalAttribute->setVertexSize(3);
    m_normalAttribute->setAttributeType(Qt3DCore::QAttribute::VertexAttribute);
    m_normalAttribute->setBuffer(m_vertexBuffer);
    m_normalAttribute->setByteStride(stride);
    m_normalAttribute->setByteOffset(3 * sizeof(float));
    m_normalAttribute->setCount(0);

    m_indexAttribute->setAttributeType(Qt3DCore::QAttribute::IndexAttribute);
    m_indexAttribute->setVertexBaseType(Qt3DCore::QAttribute::UnsignedInt);
    m_indexAttribute->setBuffer(m_indexBuffer);
    m_indexAttribute->setCount(0);

    q->addAttribute(m_positionAttribute);
    q->addAttribute(m_normalAttribute);
    q->addAttribute(m_indexAttribute);

    update();
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QExtrudedTextGeometryPrivate that Python can take functions over in. Every Qt3DExtras::QExtrudedTextGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QExtrudedTextGeometryPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DExtras_QExtrudedTextGeometryPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
class CuteQt3DExtras_QExtrudedTextGeometryPrivate : public Qt3DExtras::QExtrudedTextGeometryPrivate {
public:
  using Qt3DExtras::QExtrudedTextGeometryPrivate::QExtrudedTextGeometryPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DExtras::QExtrudedTextGeometryPrivate::update()
  void update() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QExtrudedTextGeometryPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DExtras::QExtrudedTextGeometryPrivate::update();
  }

  //  void Qt3DCore::QGeometryPrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QExtrudedTextGeometryPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::setScene(scene);
  }
};

//  void Qt3DExtras::QExtrudedTextGeometryPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras28QExtrudedTextGeometryPrivate4initEv(
    Qt3DExtras::QExtrudedTextGeometryPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QExtrudedTextGeometryPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras28QExtrudedTextGeometryPrivate6updateEv(
    Qt3DExtras::QExtrudedTextGeometryPrivate *self) {
  self->update();
}

//  QExtrudedTextGeometry *Qt3DExtras::QExtrudedTextGeometryPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QExtrudedTextGeometry *ritual_ZN10Qt3DExtras28QExtrudedTextGeometryPrivate6q_funcEv(
    Qt3DExtras::QExtrudedTextGeometryPrivate *self) {
  return self->q_func();
}

//  const QExtrudedTextGeometry
//      *Qt3DExtras::QExtrudedTextGeometryPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QExtrudedTextGeometry *ritual_ZNK10Qt3DExtras28QExtrudedTextGeometryPrivate6q_funcEv(
    const Qt3DExtras::QExtrudedTextGeometryPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QExtrudedTextGeometryPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QExtrudedTextGeometryPrivate(
    Qt3DExtras::QExtrudedTextGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QExtrudedTextGeometryPrivate *>(self)->take(key, call);
}
