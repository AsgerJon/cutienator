//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qsoundeffect.h>
#include <QtMultimedia/private/qaudiosystem_p.h>
#include <QtMultimedia/private/qplatformaudiodevices_p.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtMultimedia/private/qsamplecache_p.h>
#include <QtMultimedia/private/qsoundeffectsynchronous_p.h>
#include <QtMultimedia/private/qsoundeffectwithplayer_p.h>
#include <QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/qaudiobuffer.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtCore/qfuture.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/audio/qsoundeffect.cpp, line 580, as _ZNK19QSoundEffectPrivate3urlEv
inline QUrl QSoundEffectPrivate::url() const
{
    return m_unresolvedUrl;
}
//  -----------------------------------------------------------------------

//  bool QSoundEffectPrivate::setAudioDevice(QAudioDevice device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSoundEffectPrivate14setAudioDeviceE12QAudioDevice(
    QSoundEffectPrivate *self,
    const QAudioDevice *device) {
  return self->setAudioDevice(*device);
}

//  QAudioDevice QSoundEffectPrivate::audioDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK19QSoundEffectPrivate11audioDeviceEv(
    const QSoundEffectPrivate *self) {
  return new QAudioDevice(self->audioDevice());
}

//  QUrl QSoundEffectPrivate::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QSoundEffectPrivate3urlEv(
    const QSoundEffectPrivate *self) {
  return new QUrl(self->url());
}

//  QSoundEffect::Status QSoundEffectPrivate::status() const
extern "C" Q_DECL_EXPORT
QSoundEffect::Status ritual_ZNK19QSoundEffectPrivate6statusEv(
    const QSoundEffectPrivate *self) {
  return self->status();
}

//  int QSoundEffectPrivate::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSoundEffectPrivate9loopCountEv(
    const QSoundEffectPrivate *self) {
  return self->loopCount();
}

//  bool QSoundEffectPrivate::setLoopCount(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSoundEffectPrivate12setLoopCountEi(
    QSoundEffectPrivate *self,
    int a0) {
  return self->setLoopCount(a0);
}

//  int QSoundEffectPrivate::loopsRemaining() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSoundEffectPrivate14loopsRemainingEv(
    const QSoundEffectPrivate *self) {
  return self->loopsRemaining();
}

//  float QSoundEffectPrivate::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QSoundEffectPrivate6volumeEv(
    const QSoundEffectPrivate *self) {
  return self->volume();
}

//  bool QSoundEffectPrivate::setVolume(float a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSoundEffectPrivate9setVolumeEf(
    QSoundEffectPrivate *self,
    float a0) {
  return self->setVolume(a0);
}

//  bool QSoundEffectPrivate::muted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSoundEffectPrivate5mutedEv(
    const QSoundEffectPrivate *self) {
  return self->muted();
}

//  bool QSoundEffectPrivate::setMuted(bool a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSoundEffectPrivate8setMutedEb(
    QSoundEffectPrivate *self,
    bool a0) {
  return self->setMuted(a0);
}

//  void QSoundEffectPrivate::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSoundEffectPrivate4playEv(QSoundEffectPrivate *self) {
  self->play();
}

//  void QSoundEffectPrivate::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSoundEffectPrivate4stopEv(QSoundEffectPrivate *self) {
  self->stop();
}

//  bool QSoundEffectPrivate::playing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSoundEffectPrivate7playingEv(
    const QSoundEffectPrivate *self) {
  return self->playing();
}

//  QSoundEffectPrivate *QSoundEffectPrivate::get(QSoundEffect *a0)
extern "C" Q_DECL_EXPORT
QSoundEffectPrivate *ritual_ZN19QSoundEffectPrivate3getEP12QSoundEffect(
    QSoundEffect *a0) {
  return QSoundEffectPrivate::get(a0);
}
