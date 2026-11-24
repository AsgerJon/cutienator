//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDesignerIntrospectionInterface::~QDesignerIntrospectionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerIntrospectionInterfaceD1Ev(
    QDesignerIntrospectionInterface *self) {
  delete self;
}

//  const QDesignerMetaObjectInterface
//      *QDesignerIntrospectionInterface::metaObject(const QObject *object)
//      const
extern "C" Q_DECL_EXPORT
const QDesignerMetaObjectInterface *ritual_ZNK31QDesignerIntrospectionInterface10metaObjectEPK7QObject(
    const QDesignerIntrospectionInterface *self,
    const QObject *object) {
  return self->metaObject(object);
}
