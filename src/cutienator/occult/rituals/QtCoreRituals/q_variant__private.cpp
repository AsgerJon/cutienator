//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvariant.h>
#include <QtCore/qmetatype.h>

//  QVariant::Private::Private()
extern "C" Q_DECL_EXPORT
QVariant::Private *ritual_ZN8QVariant7PrivateC1Ev() {
  return new QVariant::Private();
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
