//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qmorphtarget.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qmorphtarget.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  const QMetaObject *Qt3DAnimation::QMorphTarget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation12QMorphTarget10metaObjectEv(
    const Qt3DAnimation::QMorphTarget *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QMorphTarget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation12QMorphTarget11qt_metacastEPKc(
    Qt3DAnimation::QMorphTarget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QMorphTarget::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation12QMorphTarget11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QMorphTarget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QMorphTarget::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation12QMorphTarget2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QMorphTarget::tr(s, c, n));
}

//  Qt3DAnimation::QMorphTarget::QMorphTarget(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphTarget *ritual_ZN13Qt3DAnimation12QMorphTargetC1EP7QObject(
    QObject *parent) {
  return new Qt3DAnimation::QMorphTarget(parent);
}

//  QList<Qt3DCore::QAttribute *>
//      Qt3DAnimation::QMorphTarget::attributeList() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QAttribute *> *ritual_ZNK13Qt3DAnimation12QMorphTarget13attributeListEv(
    const Qt3DAnimation::QMorphTarget *self) {
  return new QList<Qt3DCore::QAttribute *>(self->attributeList());
}

//  QStringList Qt3DAnimation::QMorphTarget::attributeNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13Qt3DAnimation12QMorphTarget14attributeNamesEv(
    const Qt3DAnimation::QMorphTarget *self) {
  return new QList<QString>(self->attributeNames());
}

//  void Qt3DAnimation::QMorphTarget::setAttributes(const
//      QList<Qt3DCore::QAttribute *> &attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation12QMorphTarget13setAttributesERK5QListIPN8Qt3DCore10QAttributeEE(
    Qt3DAnimation::QMorphTarget *self,
    const QList<Qt3DCore::QAttribute *> *attributes) {
  self->setAttributes(*attributes);
}

//  void Qt3DAnimation::QMorphTarget::addAttribute(Qt3DCore::QAttribute
//      *attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation12QMorphTarget12addAttributeEPN8Qt3DCore10QAttributeE(
    Qt3DAnimation::QMorphTarget *self,
    Qt3DCore::QAttribute *attribute) {
  self->addAttribute(attribute);
}

//  void Qt3DAnimation::QMorphTarget::removeAttribute(Qt3DCore::QAttribute
//      *attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation12QMorphTarget15removeAttributeEPN8Qt3DCore10QAttributeE(
    Qt3DAnimation::QMorphTarget *self,
    Qt3DCore::QAttribute *attribute) {
  self->removeAttribute(attribute);
}

//  QMorphTarget
//      *Qt3DAnimation::QMorphTarget::fromGeometry(Qt3DCore::QGeometry
//      *geometry, const QStringList &attributes)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphTarget *ritual_ZN13Qt3DAnimation12QMorphTarget12fromGeometryEPN8Qt3DCore9QGeometryERK5QListI7QStringE(
    Qt3DCore::QGeometry *geometry,
    const QList<QString> *attributes) {
  return Qt3DAnimation::QMorphTarget::fromGeometry(geometry, *attributes);
}

//  void Qt3DAnimation::QMorphTarget::attributeNamesChanged(const QStringList
//      &attributeNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation12QMorphTarget21attributeNamesChangedERK5QListI7QStringE(
    Qt3DAnimation::QMorphTarget *self,
    const QList<QString> *attributeNames) {
  self->attributeNamesChanged(*attributeNames);
}

//  QMorphTargetPrivate *Qt3DAnimation::QMorphTarget::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphTargetPrivate *ritual_ZN13Qt3DAnimation12QMorphTarget6d_funcEv(
    Qt3DAnimation::QMorphTarget *self) {
  return self->d_func();
}

//  const QMorphTargetPrivate *Qt3DAnimation::QMorphTarget::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QMorphTargetPrivate *ritual_ZNK13Qt3DAnimation12QMorphTarget6d_funcEv(
    const Qt3DAnimation::QMorphTarget *self) {
  return self->d_func();
}

//  a QList<Qt3DCore::QAttribute *> a ritual of Qt3DAnimation::QMorphTarget
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QMorphTarget__QList_Qt3DCore_QAttribute(
    QList<Qt3DCore::QAttribute *> *self) {
  delete self;
}
