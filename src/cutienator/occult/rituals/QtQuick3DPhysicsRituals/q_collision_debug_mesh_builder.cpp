//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DPhysi
//  cs/6.12.0/QtQuick3DPhysics/private/qcollisiondebugmeshbuilder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qcollisiondebugmeshbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/private/qcollisiondebugmeshbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3dphysics/src/quick3dphysics/qcollisiondebugmeshbuilder.cpp, line 9, as _ZN26QCollisionDebugMeshBuilderC1Ev
inline QCollisionDebugMeshBuilder::QCollisionDebugMeshBuilder() { }

//  from ../qtquick3dphysics/src/quick3dphysics/qcollisiondebugmeshbuilder.cpp, line 11, as _ZN26QCollisionDebugMeshBuilder5resetEv
inline void QCollisionDebugMeshBuilder::reset()
{
    m_vertices.clear();
    m_normals.clear();
}

//  from ../qtquick3dphysics/src/quick3dphysics/qcollisiondebugmeshbuilder.cpp, line 17, as _ZN26QCollisionDebugMeshBuilder7addLineERK9QVector3DS2_S2_
inline void QCollisionDebugMeshBuilder::addLine(const QVector3D &start, const QVector3D &end,
                                         const QVector3D &normal)
{
    m_vertices.append(start);
    m_vertices.append(end);
    m_normals.append(normal);
}

//  from ../qtquick3dphysics/src/quick3dphysics/qcollisiondebugmeshbuilder.cpp, line 25, as _ZN26QCollisionDebugMeshBuilder19generateVertexArrayEv
inline QByteArray QCollisionDebugMeshBuilder::generateVertexArray()
{
    QByteArray output;
    const int size = m_normals.count();
    output.resize(4 * 4 * sizeof(float) * size);

    float *data = reinterpret_cast<float *>(output.data());

    for (int i = 0; i < size; ++i) {
        const QVector3D &start = m_vertices[i * 2];
        const QVector3D &end = m_vertices[i * 2 + 1];
        const QVector3D &normal = m_normals[i];

        data[0] = start.x();
        data[1] = start.y();
        data[2] = start.z();
        data[3] = 1.0f;

        data[4] = normal.x();
        data[5] = normal.y();
        data[6] = normal.z();
        data[7] = 0.0f;

        data += 8;
        data[0] = end.x();
        data[1] = end.y();
        data[2] = end.z();
        data[3] = 1.0f;

        data[4] = normal.x();
        data[5] = normal.y();
        data[6] = normal.z();
        data[7] = 0.0f;

        data += 8;
    }

    return output;
}
//  -----------------------------------------------------------------------

//  QCollisionDebugMeshBuilder::QCollisionDebugMeshBuilder()
extern "C" Q_DECL_EXPORT
QCollisionDebugMeshBuilder *ritual_ZN26QCollisionDebugMeshBuilderC1Ev() {
  return new QCollisionDebugMeshBuilder();
}

//  void QCollisionDebugMeshBuilder::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCollisionDebugMeshBuilder5resetEv(
    QCollisionDebugMeshBuilder *self) {
  self->reset();
}

//  void QCollisionDebugMeshBuilder::addLine(const QVector3D &start, const
//      QVector3D &end, const QVector3D &normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCollisionDebugMeshBuilder7addLineERK9QVector3DS2_S2_(
    QCollisionDebugMeshBuilder *self,
    const QVector3D *start,
    const QVector3D *end,
    const QVector3D *normal) {
  self->addLine(*start, *end, *normal);
}

//  QByteArray QCollisionDebugMeshBuilder::generateVertexArray()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN26QCollisionDebugMeshBuilder19generateVertexArrayEv(
    QCollisionDebugMeshBuilder *self) {
  return new QByteArray(self->generateVertexArray());
}

//  QCollisionDebugMeshBuilder::~QCollisionDebugMeshBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCollisionDebugMeshBuilderD1Ev(
    QCollisionDebugMeshBuilder *self) {
  delete self;
}
