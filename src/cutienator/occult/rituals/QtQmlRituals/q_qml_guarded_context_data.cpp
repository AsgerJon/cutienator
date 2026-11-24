//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlguardedcontextdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlguardedcontextdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlGuardedContextData::QQmlGuardedContextData()
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZN22QQmlGuardedContextDataC1Ev() {
  return new QQmlGuardedContextData();
}

//  QQmlGuardedContextData::~QQmlGuardedContextData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGuardedContextDataD1Ev(QQmlGuardedContextData *self) {
  delete self;
}

//  bool QQmlGuardedContextData::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQmlGuardedContextData6isNullEv(
    const QQmlGuardedContextData *self) {
  return self->isNull();
}

//  QQmlContextData *QQmlGuardedContextData::operator->() const
extern "C" Q_DECL_EXPORT
QQmlContextData *ritual_ZNK22QQmlGuardedContextDataptEv(
    const QQmlGuardedContextData *self) {
  return self->operator->();
}

//  QQmlGuardedContextData *QQmlGuardedContextData::next() const
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZNK22QQmlGuardedContextData4nextEv(
    const QQmlGuardedContextData *self) {
  return self->next();
}

//  void QQmlGuardedContextData::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGuardedContextData5resetEv(
    QQmlGuardedContextData *self) {
  self->reset();
}

//  void QQmlGuardedContextData::unlink()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGuardedContextData6unlinkEv(
    QQmlGuardedContextData *self) {
  self->unlink();
}
