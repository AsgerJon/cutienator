//  Written by hand on 2026-11-26 from
//  QtBluetooth/6.12.0/QtBluetooth/private/btcentralmanager_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the header declares Objective-C classes and pulls in
//  Foundation and CoreBluetooth without asking for '__OBJC__', so only a
//  compiler of Objective-C++ on Apple's systems reads it; 'summon' builds
//  this file there only. The constructor is Qt's code in the header.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btcentralmanager_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/btcentralmanager_p.h>

//  DarwinBluetooth::LERequest::LERequest()
extern "C" Q_DECL_EXPORT
DarwinBluetooth::LERequest *ritual_ZN15DarwinBluetooth9LERequestC1Ev() {
  return new DarwinBluetooth::LERequest();
}

//  DarwinBluetooth::LERequest::~LERequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth9LERequestD1Ev(
    DarwinBluetooth::LERequest *self) {
  delete self;
}

#endif  // __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btcentralmanager_p.h>)
