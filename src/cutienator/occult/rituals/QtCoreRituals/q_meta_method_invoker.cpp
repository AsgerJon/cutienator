//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>

//  InvokeFailReason QMetaMethodInvoker::invokeImpl(QMetaMethod self_, void
//      *target, Qt::ConnectionType a2, qsizetype paramCount, const void
//      *const *parameters, const char *const *typeNames, const
//      QtPrivate::QMetaTypeInterface *const *metaTypes)
extern "C" Q_DECL_EXPORT
QMetaMethodInvoker::InvokeFailReason ritual_ZN18QMetaMethodInvoker10invokeImplE11QMetaMethodPvN2Qt14ConnectionTypeExPKPKvPKPKcPKPKN9QtPrivate18QMetaTypeInterfaceE(
    const QMetaMethod *self_,
    void *target,
    Qt::ConnectionType a2,
    qsizetype paramCount,
    const void *const *parameters,
    const char *const *typeNames,
    const QtPrivate::QMetaTypeInterface *const *metaTypes) {
  return QMetaMethodInvoker::invokeImpl(
      *self_,
      target,
      a2,
      paramCount,
      parameters,
      typeNames,
      metaTypes);
}

//  QMetaMethodInvoker::~QMetaMethodInvoker()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodInvokerD1Ev(QMetaMethodInvoker *self) {
  delete self;
}
