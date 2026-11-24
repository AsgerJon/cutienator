//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlrefcount_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlrefcount_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlRefCount::QQmlRefCount()
extern "C" Q_DECL_EXPORT
QQmlRefCount *ritual_ZN12QQmlRefCountC1Ev() {
  return new QQmlRefCount();
}

//  void QQmlRefCount::addref() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QQmlRefCount6addrefEv(const QQmlRefCount *self) {
  self->addref();
}

//  int QQmlRefCount::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQmlRefCount5countEv(const QQmlRefCount *self) {
  return self->count();
}

//  QQmlRefCount::~QQmlRefCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlRefCountD1Ev(QQmlRefCount *self) {
  delete self;
}
