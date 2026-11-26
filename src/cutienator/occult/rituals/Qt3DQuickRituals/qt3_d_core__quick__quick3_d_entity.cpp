//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentity_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <Qt3DCore/Qt3DCore>

//  const QMetaObject *Qt3DCore::Quick::Quick3DEntity::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick13Quick3DEntity10metaObjectEv(
    const Qt3DCore::Quick::Quick3DEntity *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Quick::Quick3DEntity::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Quick13Quick3DEntity11qt_metacastEPKc(
    Qt3DCore::Quick::Quick3DEntity *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::Quick::Quick3DEntity::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Quick13Quick3DEntity11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Quick::Quick3DEntity *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Quick::Quick3DEntity::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick13Quick3DEntity2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DEntity::tr(s, c, n));
}

//  Qt3DCore::Quick::Quick3DEntity::Quick3DEntity(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DEntity *ritual_ZN8Qt3DCore5Quick13Quick3DEntityC1EP7QObject(
    QObject *parent) {
  return new Qt3DCore::Quick::Quick3DEntity(parent);
}

//  QQmlListProperty<Qt3DCore::QComponent>
//      Qt3DCore::Quick::Quick3DEntity::componentList()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DCore::QComponent> *ritual_ZN8Qt3DCore5Quick13Quick3DEntity13componentListEv(
    Qt3DCore::Quick::Quick3DEntity *self) {
  return new QQmlListProperty<Qt3DCore::QComponent>(self->componentList());
}

//  QEntity *Qt3DCore::Quick::Quick3DEntity::parentEntity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK8Qt3DCore5Quick13Quick3DEntity12parentEntityEv(
    const Qt3DCore::Quick::Quick3DEntity *self) {
  return self->parentEntity();
}

//  a QQmlListProperty<Qt3DCore::QComponent> a ritual of
//      Qt3DCore::Quick::Quick3DEntity gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_Quick_Quick3DEntity__QQmlListProperty_Qt3DCore_QComponent(
    QQmlListProperty<Qt3DCore::QComponent> *self) {
  delete self;
}
