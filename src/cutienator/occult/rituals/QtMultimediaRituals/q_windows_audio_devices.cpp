//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiodevices_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object. Not written: the constructor,
//  which Qt's library offers not; with no constructor to make one, no Cute
//  class either.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiodevices_p.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qlist.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>

//  QWindowsAudioDevices::~QWindowsAudioDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsAudioDevicesD1Ev(QWindowsAudioDevices *self) {
  delete self;
}

//  QPlatformAudioSource *QWindowsAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN20QWindowsAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QWindowsAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QWindowsAudioDevices::createAudioSink(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_ZN20QWindowsAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QWindowsAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QWindowsAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK20QWindowsAudioDevices11backendNameEv(
    const QWindowsAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QWindowsAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWindowsAudioDevices14hasCallbackApiEv(
    const QWindowsAudioDevices *self) {
  return self->hasCallbackApi();
}

//  QList<QAudioDevice> QWindowsAudioDevices::findAudioInputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK20QWindowsAudioDevices15findAudioInputsEv(
    const QWindowsAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioInputs());
}

//  QList<QAudioDevice> QWindowsAudioDevices::findAudioOutputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK20QWindowsAudioDevices16findAudioOutputsEv(
    const QWindowsAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioOutputs());
}

#endif  // defined(Q_OS_WIN)
