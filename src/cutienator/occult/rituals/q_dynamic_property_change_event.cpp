//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>
#include <QtCore/qbytearray.h>

//  QDynamicPropertyChangeEvent *QDynamicPropertyChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QDynamicPropertyChangeEvent *ritual_ZNK27QDynamicPropertyChangeEvent5cloneEv(
    const QDynamicPropertyChangeEvent *self) {
  return self->clone();
}

//  QDynamicPropertyChangeEvent::~QDynamicPropertyChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDynamicPropertyChangeEventD1Ev(
    QDynamicPropertyChangeEvent *self) {
  delete self;
}

//  QDynamicPropertyChangeEvent::QDynamicPropertyChangeEvent(const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
QDynamicPropertyChangeEvent *ritual_ZN27QDynamicPropertyChangeEventC1ERK10QByteArray(
    const QByteArray *name) {
  return new QDynamicPropertyChangeEvent(*name);
}

//  QByteArray QDynamicPropertyChangeEvent::propertyName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK27QDynamicPropertyChangeEvent12propertyNameEv(
    const QDynamicPropertyChangeEvent *self) {
  return new QByteArray(self->propertyName());
}
