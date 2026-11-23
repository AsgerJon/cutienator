//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  bool QMetaObject::Connection::isConnected_helper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaObject10Connection18isConnected_helperEv(
    const QMetaObject::Connection *self) {
  return self->isConnected_helper();
}

//  QMetaObject::Connection::~Connection()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMetaObject10ConnectionD1Ev(QMetaObject::Connection *self) {
  delete self;
}

//  QMetaObject::Connection::Connection()
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN11QMetaObject10ConnectionC1Ev() {
  return new QMetaObject::Connection();
}

//  QMetaObject::Connection::Connection(const Connection &other)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN11QMetaObject10ConnectionC1ERKS0_(
    const QMetaObject::Connection *other) {
  return new QMetaObject::Connection(*other);
}
