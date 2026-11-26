//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 4. Kept as it is when the
//  generator runs again.
#include <QtCore/qvariant.h>
#include <QtCore/qmetatype.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qvariant_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QVariant::Private::canUseInternalSpace(const
//      QtPrivate::QMetaTypeInterface *type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QVariant7Private19canUseInternalSpaceEPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *type) {
  return QVariant::Private::canUseInternalSpace(type);
}

//  QVariant::Private::Private()
extern "C" Q_DECL_EXPORT
QVariant::Private *ritual_ZN8QVariant7PrivateC1Ev() {
  return new QVariant::Private();
}

//  QVariant::Private::Private(const QtPrivate::QMetaTypeInterface *iface)
extern "C" Q_DECL_EXPORT
QVariant::Private *ritual_ZN8QVariant7PrivateC1EPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *iface) {
  return new QVariant::Private(iface);
}

//  const void *QVariant::Private::storage() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK8QVariant7Private7storageEv(
    const QVariant::Private *self) {
  return self->storage();
}

//  const QtPrivate::QMetaTypeInterface *QVariant::Private::typeInterface()
//      const
extern "C" Q_DECL_EXPORT
const QtPrivate::QMetaTypeInterface *ritual_ZNK8QVariant7Private13typeInterfaceEv(
    const QVariant::Private *self) {
  return self->typeInterface();
}

//  QMetaType QVariant::Private::type() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK8QVariant7Private4typeEv(
    const QVariant::Private *self) {
  return new QMetaType(self->type());
}

//  QVariant::Private::~Private()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QVariant7PrivateD1Ev(QVariant::Private *self) {
  delete self;
}

//  const int &QVariant::Private::get<int>() const
extern "C" Q_DECL_EXPORT
const int *ritual_ZNK8QVariant7Private3getIiEERKT_v(
    const QVariant::Private *self) {
  return &(self->get<int>());
}

//  const double &QVariant::Private::get<double>() const
extern "C" Q_DECL_EXPORT
const double *ritual_ZNK8QVariant7Private3getIdEERKT_v(
    const QVariant::Private *self) {
  return &(self->get<double>());
}

//  const bool &QVariant::Private::get<bool>() const
extern "C" Q_DECL_EXPORT
const bool *ritual_ZNK8QVariant7Private3getIbEERKT_v(
    const QVariant::Private *self) {
  return &(self->get<bool>());
}

//  const QString &QVariant::Private::get<QString>() const
extern "C" Q_DECL_EXPORT
const QString *ritual_ZNK8QVariant7Private3getI7QStringEERKT_v(
    const QVariant::Private *self) {
  return &(self->get<QString>());
}
