//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const ConnectionList &QObjectPrivate::SignalVector::at(int i) const
extern "C" Q_DECL_EXPORT
QObjectPrivate::ConnectionList *ritual_ZNK14QObjectPrivate12SignalVector2atEi(
    const QObjectPrivate::SignalVector *self,
    int i) {
  return new QObjectPrivate::ConnectionList(self->at(i));
}

//  int QObjectPrivate::SignalVector::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QObjectPrivate12SignalVector5countEv(
    const QObjectPrivate::SignalVector *self) {
  return self->count();
}

//  QObjectPrivate::SignalVector::~SignalVector()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate12SignalVectorD1Ev(
    QObjectPrivate::SignalVector *self) {
  delete self;
}
