//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  QMetaObject::Connection::Connection(void *data)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN11QMetaObject10ConnectionC1EPv(
    void *data) {
  return new QMetaObject::Connection(data);
}

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

//  Connection &QMetaObject::Connection::operator=(const Connection &other)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN11QMetaObject10ConnectionaSERKS0_(
    QMetaObject::Connection *self,
    const QMetaObject::Connection *other) {
  return &(self->operator=(*other));
}

#if !(defined(Q_QDOC))
//  RestrictedBool QMetaObject::Connection::operator void
//      *QMetaObject::Connection::*() const
extern "C" Q_DECL_EXPORT
QMetaObject::Connection::RestrictedBool ritual_ZNK11QMetaObject10ConnectioncvMS0_PvEv(
    const QMetaObject::Connection *self) {
  return self->operator QMetaObject::Connection::RestrictedBool();
}
#endif  // !(defined(Q_QDOC))

//  QMetaObject::Connection::Connection(Connection &&other)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN11QMetaObject10ConnectionC1EOS0_(
    QMetaObject::Connection *other) {
  return new QMetaObject::Connection(std::move(*other));
}

//  Connection &QMetaObject::Connection::operator=(Connection &&other)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN11QMetaObject10ConnectionaSEOS0_(
    QMetaObject::Connection *self,
    QMetaObject::Connection *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QMetaObject::Connection::swap(Connection &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMetaObject10Connection4swapERS0_(
    QMetaObject::Connection *self,
    QMetaObject::Connection *other) {
  self->swap(*other);
}
