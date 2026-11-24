//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QObjectPrivate::TaggedSignalVector::TaggedSignalVector()
extern "C" Q_DECL_EXPORT
QObjectPrivate::TaggedSignalVector *ritual_ZN14QObjectPrivate18TaggedSignalVectorC1Ev() {
  return new QObjectPrivate::TaggedSignalVector();
}

//  QObjectPrivate::TaggedSignalVector::TaggedSignalVector(Connection *v)
extern "C" Q_DECL_EXPORT
QObjectPrivate::TaggedSignalVector *ritual_ZN14QObjectPrivate18TaggedSignalVectorC1EPNS_10ConnectionE(
    QObjectPrivate::Connection *v) {
  return new QObjectPrivate::TaggedSignalVector(v);
}

//  QObjectPrivate::TaggedSignalVector::TaggedSignalVector(SignalVector *v)
extern "C" Q_DECL_EXPORT
QObjectPrivate::TaggedSignalVector *ritual_ZN14QObjectPrivate18TaggedSignalVectorC1EPNS_12SignalVectorE(
    QObjectPrivate::SignalVector *v) {
  return new QObjectPrivate::TaggedSignalVector(v);
}

//  SignalVector *QObjectPrivate::TaggedSignalVector::operator
//      QObjectPrivate::SignalVector *() const
extern "C" Q_DECL_EXPORT
QObjectPrivate::SignalVector *ritual_ZNK14QObjectPrivate18TaggedSignalVectorcvPNS_12SignalVectorEEv(
    const QObjectPrivate::TaggedSignalVector *self) {
  return self->operator QObjectPrivate::SignalVector *();
}

//  Connection *QObjectPrivate::TaggedSignalVector::operator
//      QObjectPrivate::Connection *() const
extern "C" Q_DECL_EXPORT
QObjectPrivate::Connection *ritual_ZNK14QObjectPrivate18TaggedSignalVectorcvPNS_10ConnectionEEv(
    const QObjectPrivate::TaggedSignalVector *self) {
  return self->operator QObjectPrivate::Connection *();
}

//  QObjectPrivate::TaggedSignalVector::~TaggedSignalVector()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate18TaggedSignalVectorD1Ev(
    QObjectPrivate::TaggedSignalVector *self) {
  delete self;
}
