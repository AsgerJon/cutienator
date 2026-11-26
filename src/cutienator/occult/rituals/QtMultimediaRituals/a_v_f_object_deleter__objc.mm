//  Written by hand on 2026-11-26 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the header imports AVFoundation, so only a compiler of
//  Objective-C++ on Apple's systems reads it; 'summon' builds this file
//  there only. Each function is Qt's code in the header.
#include <QtMultimedia/qtmultimediaglobal.h>
#if __has_include(<QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h>)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h>

//  AVFObjectDeleter::AVFObjectDeleter()
extern "C" Q_DECL_EXPORT
AVFObjectDeleter *ritual_ZN16AVFObjectDeleterC1Ev() {
  return new AVFObjectDeleter();
}

//  AVFObjectDeleter::~AVFObjectDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16AVFObjectDeleterD1Ev(AVFObjectDeleter *self) {
  delete self;
}

//  void AVFObjectDeleter::operator()(NSObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16AVFObjectDeleterclEP8NSObject(
    AVFObjectDeleter *self, NSObject *a0) {
  self->operator()(a0);
}

#endif  // __has_include(<QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h>)
