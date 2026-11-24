//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudiodevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoreaudiodevice_p.h"
#include <QtCore/private/qcore_mac_p.h>
#include <QtMultimedia/private/qcoreaudioutils_p.h>
#include <QtMultimedia/private/qaudioformat_p.h>
#ifdef Q_OS_MACOS
#include <QtMultimedia/private/qmacosaudiodatautils_p.h>
#endif
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/coreaudio/qcoreaudiodevice.cpp, line 197, as _ZN20QCoreAudioDeviceInfoC1ERK10QByteArrayN12QAudioDevice4ModeE
#if !(defined(Q_OS_MACOS))
inline QCoreAudioDeviceInfo::QCoreAudioDeviceInfo(const QByteArray &device, QAudioDevice::Mode mode)
    : QAudioDevicePrivate(device, mode, qGetDefaultDescription(device), false,
                          createDefaultCoreAudioDeviceFormat(mode))
{
}
#endif  // !(defined(Q_OS_MACOS))
//  -----------------------------------------------------------------------

#if !(defined(Q_OS_MACOS))
//  QCoreAudioDeviceInfo::QCoreAudioDeviceInfo(const QByteArray &device,
//      QAudioDevice::Mode mode)
extern "C" Q_DECL_EXPORT
QCoreAudioDeviceInfo *ritual_ZN20QCoreAudioDeviceInfoC1ERK10QByteArrayN12QAudioDevice4ModeE(
    const QByteArray *device,
    QAudioDevice::Mode mode) {
  return new QCoreAudioDeviceInfo(*device, mode);
}
#endif  // !(defined(Q_OS_MACOS))

//  QCoreAudioDeviceInfo::~QCoreAudioDeviceInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoreAudioDeviceInfoD1Ev(QCoreAudioDeviceInfo *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
