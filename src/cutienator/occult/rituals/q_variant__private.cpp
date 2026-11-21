//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvariant.h>
#include <QtCore/qmetatype.h>

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
