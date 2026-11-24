//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcanuniqueiddescription_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcanuniqueiddescription_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qcanuniqueiddescription.h>

//  bool QCanUniqueIdDescriptionPrivate::isShared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QCanUniqueIdDescriptionPrivate8isSharedEv(
    const QCanUniqueIdDescriptionPrivate *self) {
  return self->isShared();
}

//  QCanUniqueIdDescriptionPrivate *QCanUniqueIdDescriptionPrivate::get(const
//      QCanUniqueIdDescription &desc)
extern "C" Q_DECL_EXPORT
QCanUniqueIdDescriptionPrivate *ritual_ZN30QCanUniqueIdDescriptionPrivate3getERK23QCanUniqueIdDescription(
    const QCanUniqueIdDescription *desc) {
  return QCanUniqueIdDescriptionPrivate::get(*desc);
}

//  QCanUniqueIdDescriptionPrivate::~QCanUniqueIdDescriptionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCanUniqueIdDescriptionPrivateD1Ev(
    QCanUniqueIdDescriptionPrivate *self) {
  delete self;
}
