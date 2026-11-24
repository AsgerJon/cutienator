//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergyadvertisingparameters.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtBluetooth/qlowenergyadvertisingparameters.h>
#include <QtBluetooth/qbluetoothaddress.h>

//  QLowEnergyAdvertisingParameters::AddressInfo::AddressInfo(const
//      QBluetoothAddress &addr, QLowEnergyController::RemoteAddressType t)
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingParameters::AddressInfo *ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfoC1ERK17QBluetoothAddressN20QLowEnergyController17RemoteAddressTypeE(
    const QBluetoothAddress *addr,
    QLowEnergyController::RemoteAddressType t) {
  return new QLowEnergyAdvertisingParameters::AddressInfo(*addr, t);
}

//  QLowEnergyAdvertisingParameters::AddressInfo::AddressInfo()
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingParameters::AddressInfo *ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfoC1Ev() {
  return new QLowEnergyAdvertisingParameters::AddressInfo();
}

//  bool operator==(const AddressInfo &a, const AddressInfo &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN31QLowEnergyAdvertisingParameters11AddressInfoES2_(
    const QLowEnergyAdvertisingParameters::AddressInfo *a,
    const QLowEnergyAdvertisingParameters::AddressInfo *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const AddressInfo &a, const AddressInfo &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN31QLowEnergyAdvertisingParameters11AddressInfoES2_(
    const QLowEnergyAdvertisingParameters::AddressInfo *a,
    const QLowEnergyAdvertisingParameters::AddressInfo *b) {
  return operator!=(*a, *b);
}

//  bool QLowEnergyAdvertisingParameters::AddressInfo::equals(const
//      AddressInfo &a, const AddressInfo &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfo6equalsERKS0_S2_(
    const QLowEnergyAdvertisingParameters::AddressInfo *a,
    const QLowEnergyAdvertisingParameters::AddressInfo *b) {
  return QLowEnergyAdvertisingParameters::AddressInfo::equals(*a, *b);
}

//  QLowEnergyAdvertisingParameters::AddressInfo::~AddressInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfoD1Ev(
    QLowEnergyAdvertisingParameters::AddressInfo *self) {
  delete self;
}
