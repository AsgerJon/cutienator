//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dgeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <Qt3DCore/Qt3DCore>

//  const QMetaObject *Qt3DCore::Quick::Quick3DGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick15Quick3DGeometry10metaObjectEv(
    const Qt3DCore::Quick::Quick3DGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Quick::Quick3DGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Quick15Quick3DGeometry11qt_metacastEPKc(
    Qt3DCore::Quick::Quick3DGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::Quick::Quick3DGeometry::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Quick15Quick3DGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Quick::Quick3DGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Quick::Quick3DGeometry::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick15Quick3DGeometry2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DGeometry::tr(s, c, n));
}

//  Qt3DCore::Quick::Quick3DGeometry::Quick3DGeometry(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DGeometry *ritual_ZN8Qt3DCore5Quick15Quick3DGeometryC1EP7QObject(
    QObject *parent) {
  return new Qt3DCore::Quick::Quick3DGeometry(parent);
}

//  QGeometry *Qt3DCore::Quick::Quick3DGeometry::parentGeometry() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZNK8Qt3DCore5Quick15Quick3DGeometry14parentGeometryEv(
    const Qt3DCore::Quick::Quick3DGeometry *self) {
  return self->parentGeometry();
}

//  QQmlListProperty<Qt3DCore::QAttribute>
//      Qt3DCore::Quick::Quick3DGeometry::attributeList()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DCore::QAttribute> *ritual_ZN8Qt3DCore5Quick15Quick3DGeometry13attributeListEv(
    Qt3DCore::Quick::Quick3DGeometry *self) {
  return new QQmlListProperty<Qt3DCore::QAttribute>(self->attributeList());
}

//  a QQmlListProperty<Qt3DCore::QAttribute> a ritual of
//      Qt3DCore::Quick::Quick3DGeometry gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_Quick_Quick3DGeometry__QQmlListProperty_Qt3DCore_QAttribute(
    QQmlListProperty<Qt3DCore::QAttribute> *self) {
  delete self;
}
