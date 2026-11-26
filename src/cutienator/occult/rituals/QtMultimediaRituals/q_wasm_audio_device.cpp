//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qwasmaudiodevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WASM)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwasmaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qwasmaudiodevice_p.h>
#include <emscripten.h>
#include <emscripten/val.h>
#include <emscripten/bind.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/wasm/qwasmaudiodevice.cpp, line 64, as _ZN16QWasmAudioDeviceC1EPKcS1_bN12QAudioDevice4ModeE
inline QWasmAudioDevice::QWasmAudioDevice(const char *device, const char *desc, bool isDef,
                                   QAudioDevice::Mode mode)
    : QAudioDevicePrivate(device, mode, QString::fromUtf8(desc), isDef,
                          createDefaultWasmAudioDeviceFormat())
{
}
//  -----------------------------------------------------------------------

//  QWasmAudioDevice::QWasmAudioDevice(const char *device, const char
//      *description, bool isDefault, QAudioDevice::Mode mode)
extern "C" Q_DECL_EXPORT
QWasmAudioDevice *ritual_ZN16QWasmAudioDeviceC1EPKcS1_bN12QAudioDevice4ModeE(
    const char *device,
    const char *description,
    bool isDefault,
    QAudioDevice::Mode mode) {
  return new QWasmAudioDevice(device, description, isDefault, mode);
}

//  QWasmAudioDevice::~QWasmAudioDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWasmAudioDeviceD1Ev(QWasmAudioDevice *self) {
  delete self;
}

#endif  // defined(Q_OS_WASM)
