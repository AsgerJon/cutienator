//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiodevice_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(qnx_io_snd)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  QQnxSndAudioDeviceInfo::QQnxSndAudioDeviceInfo(const QByteArray &dev,
//      const QString &description, QAudioDevice::Mode mode)
extern "C" Q_DECL_EXPORT
QQnxSndAudioDeviceInfo *ritual_ZN22QQnxSndAudioDeviceInfoC1ERK10QByteArrayRK7QStringN12QAudioDevice4ModeE(
    const QByteArray *dev,
    const QString *description,
    QAudioDevice::Mode mode) {
  return new QQnxSndAudioDeviceInfo(*dev, *description, mode);
}

//  QQnxSndAudioDeviceInfo::~QQnxSndAudioDeviceInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQnxSndAudioDeviceInfoD1Ev(QQnxSndAudioDeviceInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(qnx_io_snd)
