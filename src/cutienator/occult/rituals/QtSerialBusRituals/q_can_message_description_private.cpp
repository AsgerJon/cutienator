//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcanmessagedescription_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcanmessagedescription_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qcanmessagedescription.h>

//  bool QCanMessageDescriptionPrivate::isShared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QCanMessageDescriptionPrivate8isSharedEv(
    const QCanMessageDescriptionPrivate *self) {
  return self->isShared();
}

//  QCanMessageDescriptionPrivate *QCanMessageDescriptionPrivate::get(const
//      QCanMessageDescription &desc)
extern "C" Q_DECL_EXPORT
QCanMessageDescriptionPrivate *ritual_ZN29QCanMessageDescriptionPrivate3getERK22QCanMessageDescription(
    const QCanMessageDescription *desc) {
  return QCanMessageDescriptionPrivate::get(*desc);
}

//  QCanMessageDescriptionPrivate::~QCanMessageDescriptionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QCanMessageDescriptionPrivateD1Ev(
    QCanMessageDescriptionPrivate *self) {
  delete self;
}
