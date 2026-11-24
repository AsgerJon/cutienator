//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiodevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(alsa)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  QAlsaAudioDeviceInfo::QAlsaAudioDeviceInfo(const QByteArray &dev, const
//      QString &description, QAudioDevice::Mode mode)
extern "C" Q_DECL_EXPORT
QAlsaAudioDeviceInfo *ritual_ZN20QAlsaAudioDeviceInfoC1ERK10QByteArrayRK7QStringN12QAudioDevice4ModeE(
    const QByteArray *dev,
    const QString *description,
    QAudioDevice::Mode mode) {
  return new QAlsaAudioDeviceInfo(*dev, *description, mode);
}

//  QAlsaAudioDeviceInfo::~QAlsaAudioDeviceInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAlsaAudioDeviceInfoD1Ev(QAlsaAudioDeviceInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(alsa)
