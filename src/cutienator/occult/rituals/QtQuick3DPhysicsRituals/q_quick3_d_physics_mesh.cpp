//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsmeshutils_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsmeshutils_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQuick3DPhysicsMesh::QQuick3DPhysicsMesh(const QString &qmlSource)
extern "C" Q_DECL_EXPORT
QQuick3DPhysicsMesh *ritual_ZN19QQuick3DPhysicsMeshC1ERK7QString(
    const QString *qmlSource) {
  return new QQuick3DPhysicsMesh(*qmlSource);
}

//  QQuick3DPhysicsMesh::QQuick3DPhysicsMesh(const QQuick3DGeometry
//      *geometrySource)
extern "C" Q_DECL_EXPORT
QQuick3DPhysicsMesh *ritual_ZN19QQuick3DPhysicsMeshC1EPK16QQuick3DGeometry(
    const QQuick3DGeometry *geometrySource) {
  return new QQuick3DPhysicsMesh(geometrySource);
}

//  QQuick3DPhysicsMesh::~QQuick3DPhysicsMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DPhysicsMeshD1Ev(QQuick3DPhysicsMesh *self) {
  delete self;
}

//  void QQuick3DPhysicsMesh::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DPhysicsMesh3refEv(QQuick3DPhysicsMesh *self) {
  self->ref();
}

//  int QQuick3DPhysicsMesh::deref()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DPhysicsMesh5derefEv(QQuick3DPhysicsMesh *self) {
  return self->deref();
}
