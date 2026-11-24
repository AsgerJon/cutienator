//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanbusdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanbusdevice.h>

//  bool operator==(const Filter &a, const Filter &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN13QCanBusDevice6FilterES2_(
    const QCanBusDevice::Filter *a,
    const QCanBusDevice::Filter *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const Filter &a, const Filter &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN13QCanBusDevice6FilterES2_(
    const QCanBusDevice::Filter *a,
    const QCanBusDevice::Filter *b) {
  return operator!=(*a, *b);
}

//  QCanBusDevice::Filter::~Filter()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice6FilterD1Ev(QCanBusDevice::Filter *self) {
  delete self;
}
