//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlguard_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlguard_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlGuardImpl::QQmlGuardImpl()
extern "C" Q_DECL_EXPORT
QQmlGuardImpl *ritual_ZN13QQmlGuardImplC1Ev() {
  return new QQmlGuardImpl();
}

//  QQmlGuardImpl::QQmlGuardImpl(QObject *a0)
extern "C" Q_DECL_EXPORT
QQmlGuardImpl *ritual_ZN13QQmlGuardImplC1EP7QObject(QObject *a0) {
  return new QQmlGuardImpl(a0);
}

//  QQmlGuardImpl::~QQmlGuardImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlGuardImplD1Ev(QQmlGuardImpl *self) {
  delete self;
}

//  void QQmlGuardImpl::addGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlGuardImpl8addGuardEv(QQmlGuardImpl *self) {
  self->addGuard();
}

//  void QQmlGuardImpl::remGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlGuardImpl8remGuardEv(QQmlGuardImpl *self) {
  self->remGuard();
}

//  void QQmlGuardImpl::setObject(QObject *g)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlGuardImpl9setObjectEP7QObject(
    QQmlGuardImpl *self,
    QObject *g) {
  self->setObject(g);
}

//  bool QQmlGuardImpl::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlGuardImpl6isNullEv(const QQmlGuardImpl *self) {
  return self->isNull();
}
