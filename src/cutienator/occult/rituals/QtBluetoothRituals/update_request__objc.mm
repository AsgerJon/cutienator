//  Written by hand on 2026-11-26 from
//  QtBluetooth/6.12.0/QtBluetooth/private/btperipheralmanager_p.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the header declares Objective-C classes and pulls in
//  Foundation without asking for '__OBJC__', so only a compiler of
//  Objective-C++ on Apple's systems reads it; 'summon' builds this file
//  there only. The constructor taking 'ObjCStrongReference<NSData>' gets
//  no ritual: Python has nothing for an instance of that template.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btperipheralmanager_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/btperipheralmanager_p.h>

//  UpdateRequest::UpdateRequest()
extern "C" Q_DECL_EXPORT
UpdateRequest *ritual_ZN13UpdateRequestC1Ev() {
  return new UpdateRequest();
}

//  UpdateRequest::~UpdateRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN13UpdateRequestD1Ev(UpdateRequest *self) {
  delete self;
}

#endif  // __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btperipheralmanager_p.h>)
