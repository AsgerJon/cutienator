//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtrianglemeshshape_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtrianglemeshshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QTriangleMeshShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QTriangleMeshShape10metaObjectEv(
    const QTriangleMeshShape *self) {
  return self->metaObject();
}

//  void *QTriangleMeshShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QTriangleMeshShape11qt_metacastEPKc(
    QTriangleMeshShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTriangleMeshShape::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QTriangleMeshShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QTriangleMeshShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTriangleMeshShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QTriangleMeshShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTriangleMeshShape::tr(s, c, n));
}

//  QMeshShape::MeshType QTriangleMeshShape::shapeType() const
extern "C" Q_DECL_EXPORT
QMeshShape::MeshType ritual_ZNK18QTriangleMeshShape9shapeTypeEv(
    const QTriangleMeshShape *self) {
  return self->shapeType();
}

//  bool QTriangleMeshShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTriangleMeshShape13isStaticShapeEv(
    const QTriangleMeshShape *self) {
  return self->isStaticShape();
}

//  QMeshShape::MeshType QTriangleMeshShape::shapeType() const
extern "C" Q_DECL_EXPORT
QMeshShape::MeshType ritual_own_ZNK18QTriangleMeshShape9shapeTypeEv(
    const QTriangleMeshShape *self) {
  return self->QTriangleMeshShape::shapeType();
}

//  bool QTriangleMeshShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QTriangleMeshShape13isStaticShapeEv(
    const QTriangleMeshShape *self) {
  return self->QTriangleMeshShape::isStaticShape();
}
