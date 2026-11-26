//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_introspection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_introspection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::QDesignerIntrospection::QDesignerIntrospection()
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerIntrospection *ritual_ZN18qdesigner_internal22QDesignerIntrospectionC1Ev() {
  return new qdesigner_internal::QDesignerIntrospection();
}

//  qdesigner_internal::QDesignerIntrospection::~QDesignerIntrospection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22QDesignerIntrospectionD1Ev(
    qdesigner_internal::QDesignerIntrospection *self) {
  delete self;
}

//  const QDesignerMetaObjectInterface
//      *qdesigner_internal::QDesignerIntrospection::metaObject(const QObject
//      *object) const
extern "C" Q_DECL_EXPORT
const QDesignerMetaObjectInterface *ritual_ZNK18qdesigner_internal22QDesignerIntrospection10metaObjectEPK7QObject(
    const qdesigner_internal::QDesignerIntrospection *self,
    const QObject *object) {
  return self->metaObject(object);
}

//  const QDesignerMetaObjectInterface *qdesigner_internal::QDesignerIntrospe
//      ction::metaObjectForQMetaObject(const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
const QDesignerMetaObjectInterface *ritual_ZNK18qdesigner_internal22QDesignerIntrospection24metaObjectForQMetaObjectEPK11QMetaObject(
    const qdesigner_internal::QDesignerIntrospection *self,
    const QMetaObject *metaObject) {
  return self->metaObjectForQMetaObject(metaObject);
}
