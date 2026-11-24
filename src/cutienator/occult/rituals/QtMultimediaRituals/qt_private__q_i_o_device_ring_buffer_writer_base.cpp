//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudio_qiodevice_support_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudio_qiodevice_support_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QtPrivate::QIODeviceRingBufferWriterBase::bytesConsumedFromRingbuffe
//      r(qint64 bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate29QIODeviceRingBufferWriterBase27bytesConsumedFromRingbufferEx(
    QtPrivate::QIODeviceRingBufferWriterBase *self,
    qint64 bytes) {
  self->bytesConsumedFromRingbuffer(bytes);
}

//  bool QtPrivate::QIODeviceRingBufferWriterBase::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate29QIODeviceRingBufferWriterBase12isSequentialEv(
    const QtPrivate::QIODeviceRingBufferWriterBase *self) {
  return self->isSequential();
}

//  bool QtPrivate::QIODeviceRingBufferWriterBase::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QtPrivate29QIODeviceRingBufferWriterBase12isSequentialEv(
    const QtPrivate::QIODeviceRingBufferWriterBase *self) {
  return self->QtPrivate::QIODeviceRingBufferWriterBase::isSequential();
}
