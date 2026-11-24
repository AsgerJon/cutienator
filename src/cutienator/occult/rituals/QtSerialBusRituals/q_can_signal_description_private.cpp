//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcansignaldescription_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcansignaldescription_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qcansignaldescription.h>

//  bool QCanSignalDescriptionPrivate::isShared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QCanSignalDescriptionPrivate8isSharedEv(
    const QCanSignalDescriptionPrivate *self) {
  return self->isShared();
}

//  QCanSignalDescriptionPrivate *QCanSignalDescriptionPrivate::get(const
//      QCanSignalDescription &desc)
extern "C" Q_DECL_EXPORT
QCanSignalDescriptionPrivate *ritual_ZN28QCanSignalDescriptionPrivate3getERK21QCanSignalDescription(
    const QCanSignalDescription *desc) {
  return QCanSignalDescriptionPrivate::get(*desc);
}

//  QCanSignalDescriptionPrivate::~QCanSignalDescriptionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCanSignalDescriptionPrivateD1Ev(
    QCanSignalDescriptionPrivate *self) {
  delete self;
}
