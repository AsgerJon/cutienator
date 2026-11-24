//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4urlobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  void QV4::UrlObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49UrlObject10__dataTestEv(QV4::UrlObject *self) {
  self->__dataTest();
}

//  QV4::Heap::UrlObject *QV4::UrlObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObject *ritual_ZNK3QV49UrlObject11d_uncheckedEv(
    const QV4::UrlObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::UrlObject *QV4::UrlObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObject *ritual_ZNK3QV49UrlObject1dEv(
    const QV4::UrlObject *self) {
  return self->d();
}

//  void QV4::UrlObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49UrlObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::UrlObject::virtualDestroy(b);
}

//  QV4::Object *QV4::UrlObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV49UrlObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::UrlObject::defaultPrototype(e);
}

//  QString QV4::UrlObject::hash() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4hashEv(const QV4::UrlObject *self) {
  return new QString(self->hash());
}

//  QString QV4::UrlObject::host() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4hostEv(const QV4::UrlObject *self) {
  return new QString(self->host());
}

//  QString QV4::UrlObject::hostname() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8hostnameEv(const QV4::UrlObject *self) {
  return new QString(self->hostname());
}

//  QString QV4::UrlObject::href() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4hrefEv(const QV4::UrlObject *self) {
  return new QString(self->href());
}

//  QString QV4::UrlObject::origin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject6originEv(const QV4::UrlObject *self) {
  return new QString(self->origin());
}

//  QString QV4::UrlObject::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8passwordEv(const QV4::UrlObject *self) {
  return new QString(self->password());
}

//  QString QV4::UrlObject::pathname() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8pathnameEv(const QV4::UrlObject *self) {
  return new QString(self->pathname());
}

//  QString QV4::UrlObject::port() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4portEv(const QV4::UrlObject *self) {
  return new QString(self->port());
}

//  QString QV4::UrlObject::protocol() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8protocolEv(const QV4::UrlObject *self) {
  return new QString(self->protocol());
}

//  QString QV4::UrlObject::username() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8usernameEv(const QV4::UrlObject *self) {
  return new QString(self->username());
}

//  QUrl QV4::UrlObject::toQUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV49UrlObject6toQUrlEv(const QV4::UrlObject *self) {
  return new QUrl(self->toQUrl());
}

//  const Heap::UrlObject *QV4::UrlObject::constD() const
extern "C" Q_DECL_EXPORT
const QV4::Heap::UrlObject *ritual_ZNK3QV49UrlObject6constDEv(
    const QV4::UrlObject *self) {
  return self->constD();
}
