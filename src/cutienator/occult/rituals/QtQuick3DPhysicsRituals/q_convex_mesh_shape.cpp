//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qconvexmeshshape_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qconvexmeshshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QConvexMeshShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QConvexMeshShape10metaObjectEv(
    const QConvexMeshShape *self) {
  return self->metaObject();
}

//  void *QConvexMeshShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QConvexMeshShape11qt_metacastEPKc(
    QConvexMeshShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QConvexMeshShape::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QConvexMeshShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QConvexMeshShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QConvexMeshShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QConvexMeshShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QConvexMeshShape::tr(s, c, n));
}

//  QMeshShape::MeshType QConvexMeshShape::shapeType() const
extern "C" Q_DECL_EXPORT
QMeshShape::MeshType ritual_ZNK16QConvexMeshShape9shapeTypeEv(
    const QConvexMeshShape *self) {
  return self->shapeType();
}

//  bool QConvexMeshShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QConvexMeshShape13isStaticShapeEv(
    const QConvexMeshShape *self) {
  return self->isStaticShape();
}

//  QMeshShape::MeshType QConvexMeshShape::shapeType() const
extern "C" Q_DECL_EXPORT
QMeshShape::MeshType ritual_own_ZNK16QConvexMeshShape9shapeTypeEv(
    const QConvexMeshShape *self) {
  return self->QConvexMeshShape::shapeType();
}

//  bool QConvexMeshShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QConvexMeshShape13isStaticShapeEv(
    const QConvexMeshShape *self) {
  return self->QConvexMeshShape::isStaticShape();
}
