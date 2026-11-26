//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/qaudioengine.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <cstring>
#include <optional>
#include <QtGui/QVector3D>
#include <QtCore/QSpan>
#include <QtSpatialAudio/QAudioRoom>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/qaudioengine.h>
#include <QtSpatialAudio/private/qaudioengine_p.h>
#include <QtMultimedia/private/qmultimedia_ranges_p.h>
#include <QtSpatialAudio/private/qaudioengine_threaded_p.h>
#include <QtSpatialAudio/private/qaudioengine_withplayer_p.h>
#include <QtCore/qspan.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/private/qaudiosystem_p.h>
#include <QtMultimedia/private/qplatformaudiodevices_p.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtCore/q20vector.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 39, as _ZN19QAudioEnginePrivate16setDistanceScaleEf
inline void QAudioEnginePrivate::setDistanceScale(float scale)
{
    if (scale == m_distanceScale)
        return;
    m_distanceScale = scale;
    Q_Q(QAudioEngine);
    emit q->distanceScaleChanged();
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 48, as _ZNK19QAudioEnginePrivate13distanceScaleEv
inline float QAudioEnginePrivate::distanceScale() const
{
    return m_distanceScale;
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 63, as _ZNK19QAudioEnginePrivate12masterVolumeEv
inline float QAudioEnginePrivate::masterVolume() const
{
    return m_masterVolume;
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 110, as _ZNK19QAudioEnginePrivate10outputModeEv
inline QAudioEngine::OutputMode QAudioEnginePrivate::outputMode() const
{
    return m_outputMode;
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 115, as _ZN19QAudioEnginePrivate7addRoomEP10QAudioRoom
inline void QAudioEnginePrivate::addRoom(QAudioRoom *room)
{
    Q_ASSERT(!QtMultimediaPrivate::ranges::contains(rooms, room));
    rooms.push_back(room);
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 121, as _ZN19QAudioEnginePrivate10removeRoomEP10QAudioRoom
inline void QAudioEnginePrivate::removeRoom(QAudioRoom *room)
{
    Q_ASSERT(QtMultimediaPrivate::ranges::contains(rooms, room));
    q20::erase(rooms, room);
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 127, as _ZNK19QAudioEnginePrivate11currentRoomEv
inline QAudioRoom *QAudioEnginePrivate::currentRoom() const
{
    return m_currentRoom;
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 171, as _ZNK19QAudioEnginePrivate27findSmallestRoomForListenerE5QSpanIP10QAudioRoomLm18446744073709551615EE
inline QAudioEnginePrivate::SmallestRoomForListenerResult
QAudioEnginePrivate::findSmallestRoomForListener(QSpan<QAudioRoom *> rooms) const
{
    const std::optional<QVector3D> listenerPos = listenerPosition();

    if (!listenerPos)
        return SmallestRoomForListenerResult{
            nullptr,
            0.f,
        };

    std::optional<float> roomVolume;
    QAudioRoom *room = nullptr;

    for (QAudioRoom *r : std::as_const(rooms)) {
        QVector3D dim2 = r->dimensions() / 2.;
        float vol = dim2.x() * dim2.y() * dim2.z();
        if (roomVolume && vol > roomVolume)
            continue;
        QVector3D dist = r->position() - *listenerPos;
        // transform into room coordinates
        dist = r->rotation().rotatedVector(dist);
        if (qAbs(dist.x()) <= dim2.x() && qAbs(dist.y()) <= dim2.y()
            && qAbs(dist.z()) <= dim2.z()) {
            room = r;
            roomVolume = vol;
        }
    }

    return SmallestRoomForListenerResult{
        room,
        roomVolume.value_or(0.f),
    };
}
//  -----------------------------------------------------------------------

//  A QAudioEnginePrivate that Python can take functions over in. Every QAudioEnginePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAudioEnginePrivateCall0)(const void *, int, int *);
typedef void (*CuteQAudioEnginePrivateCall1)(const void *, int *);
typedef void (*CuteQAudioEnginePrivateCall2)(const void *, int *);
typedef void (*CuteQAudioEnginePrivateCall3)(const void *, int *);
typedef void (*CuteQAudioEnginePrivateCall4)(const void *, bool, int *);
typedef bool (*CuteQAudioEnginePrivateCall5)(const void *, int *);
typedef void (*CuteQAudioEnginePrivateCall6)(const void *, const QAudioDevice *, int *);
typedef const QAudioDevice * (*CuteQAudioEnginePrivateCall7)(const void *, int *);
typedef void (*CuteQAudioEnginePrivateCall8)(const void *, QSpatialAudioSoundPrivate *, int *);
typedef void (*CuteQAudioEnginePrivateCall9)(const void *, QSpatialAudioSoundPrivate *, int *);
class CuteQAudioEnginePrivate : public QAudioEnginePrivate {
public:
  using QAudioEnginePrivate::QAudioEnginePrivate;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate13setOutputModeEN12QAudioEngine10OutputModeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate17updateRoomEffectsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate5startEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate4stopEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate9setPausedEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAudioEnginePrivate8isPausedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate15setOutputDeviceERK12QAudioDevice")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAudioEnginePrivate12outputDeviceEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate8addSoundEP25QSpatialAudioSoundPrivate")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAudioEnginePrivate11removeSoundEP25QSpatialAudioSoundPrivate")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QAudioEnginePrivate::setOutputMode(QAudioEngine::OutputMode a0)
  void setOutputMode(QAudioEngine::OutputMode a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall0 call = reinterpret_cast<CuteQAudioEnginePrivateCall0>(taken[0]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QAudioEnginePrivate::setOutputMode(a0);
  }

  //  void QAudioEnginePrivate::updateRoomEffects()
  void updateRoomEffects() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall1 call = reinterpret_cast<CuteQAudioEnginePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAudioEnginePrivate::start()
  void start() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall2 call = reinterpret_cast<CuteQAudioEnginePrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAudioEnginePrivate::stop()
  void stop() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall3 call = reinterpret_cast<CuteQAudioEnginePrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAudioEnginePrivate::setPaused(bool a0)
  void setPaused(bool a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall4 call = reinterpret_cast<CuteQAudioEnginePrivateCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QAudioEnginePrivate::isPaused() const
  bool isPaused() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall5 call = reinterpret_cast<CuteQAudioEnginePrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAudioEnginePrivate::setOutputDevice(const QAudioDevice &a0)
  void setOutputDevice(const QAudioDevice &a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall6 call = reinterpret_cast<CuteQAudioEnginePrivateCall6>(taken[6]);
      call(this, &a0, &handled);
      if (handled) return;
    }
  }

  //  QAudioDevice QAudioEnginePrivate::outputDevice() const
  QAudioDevice outputDevice() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall7 call = reinterpret_cast<CuteQAudioEnginePrivateCall7>(taken[7]);
      const QAudioDevice * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QAudioEnginePrivate::addSound(QSpatialAudioSoundPrivate *a0)
  void addSound(QSpatialAudioSoundPrivate *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall8 call = reinterpret_cast<CuteQAudioEnginePrivateCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  void QAudioEnginePrivate::removeSound(QSpatialAudioSoundPrivate *a0)
  void removeSound(QSpatialAudioSoundPrivate *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAudioEnginePrivateCall9 call = reinterpret_cast<CuteQAudioEnginePrivateCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
};

//  QAudioEngine *QAudioEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QAudioEngine *ritual_ZN19QAudioEnginePrivate6q_funcEv(
    QAudioEnginePrivate *self) {
  return self->q_func();
}

//  const QAudioEngine *QAudioEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAudioEngine *ritual_ZNK19QAudioEnginePrivate6q_funcEv(
    const QAudioEnginePrivate *self) {
  return self->q_func();
}

//  QAudioEnginePrivate *QAudioEnginePrivate::get(QAudioEngine *engine)
extern "C" Q_DECL_EXPORT
QAudioEnginePrivate *ritual_ZN19QAudioEnginePrivate3getEP12QAudioEngine(
    QAudioEngine *engine) {
  return QAudioEnginePrivate::get(engine);
}

//  QAudioEnginePrivate::~QAudioEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivateD1Ev(QAudioEnginePrivate *self) {
  delete self;
}

//  int QAudioEnginePrivate::sampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAudioEnginePrivate10sampleRateEv(
    const QAudioEnginePrivate *self) {
  return self->sampleRate();
}

//  void QAudioEnginePrivate::setDistanceScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate16setDistanceScaleEf(
    QAudioEnginePrivate *self,
    float scale) {
  self->setDistanceScale(scale);
}

//  float QAudioEnginePrivate::distanceScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QAudioEnginePrivate13distanceScaleEv(
    const QAudioEnginePrivate *self) {
  return self->distanceScale();
}

//  float QAudioEnginePrivate::masterVolume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QAudioEnginePrivate12masterVolumeEv(
    const QAudioEnginePrivate *self) {
  return self->masterVolume();
}

//  std::optional<QVector3D> QAudioEnginePrivate::listenerPosition() const
extern "C" Q_DECL_EXPORT
std::optional<QVector3D> *ritual_ZNK19QAudioEnginePrivate16listenerPositionEv(
    const QAudioEnginePrivate *self) {
  return new std::optional<QVector3D>(self->listenerPosition());
}

//  void QAudioEnginePrivate::setOutputMode(QAudioEngine::OutputMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate13setOutputModeEN12QAudioEngine10OutputModeE(
    QAudioEnginePrivate *self,
    QAudioEngine::OutputMode a0) {
  self->setOutputMode(a0);
}

//  QAudioEngine::OutputMode QAudioEnginePrivate::outputMode() const
extern "C" Q_DECL_EXPORT
QAudioEngine::OutputMode ritual_ZNK19QAudioEnginePrivate10outputModeEv(
    const QAudioEnginePrivate *self) {
  return self->outputMode();
}

//  void QAudioEnginePrivate::addRoom(QAudioRoom *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate7addRoomEP10QAudioRoom(
    QAudioEnginePrivate *self,
    QAudioRoom *a0) {
  self->addRoom(a0);
}

//  void QAudioEnginePrivate::removeRoom(QAudioRoom *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate10removeRoomEP10QAudioRoom(
    QAudioEnginePrivate *self,
    QAudioRoom *a0) {
  self->removeRoom(a0);
}

//  QAudioRoom *QAudioEnginePrivate::currentRoom() const
extern "C" Q_DECL_EXPORT
QAudioRoom *ritual_ZNK19QAudioEnginePrivate11currentRoomEv(
    const QAudioEnginePrivate *self) {
  return self->currentRoom();
}

//  void QAudioEnginePrivate::updateRoomEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate17updateRoomEffectsEv(
    QAudioEnginePrivate *self) {
  self->updateRoomEffects();
}

//  void QAudioEnginePrivate::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate5startEv(QAudioEnginePrivate *self) {
  self->start();
}

//  void QAudioEnginePrivate::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate4stopEv(QAudioEnginePrivate *self) {
  self->stop();
}

//  void QAudioEnginePrivate::setPaused(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate9setPausedEb(
    QAudioEnginePrivate *self,
    bool a0) {
  self->setPaused(a0);
}

//  bool QAudioEnginePrivate::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAudioEnginePrivate8isPausedEv(
    const QAudioEnginePrivate *self) {
  return self->isPaused();
}

//  void QAudioEnginePrivate::setOutputDevice(const QAudioDevice &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate15setOutputDeviceERK12QAudioDevice(
    QAudioEnginePrivate *self,
    const QAudioDevice *a0) {
  self->setOutputDevice(*a0);
}

//  QAudioDevice QAudioEnginePrivate::outputDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK19QAudioEnginePrivate12outputDeviceEv(
    const QAudioEnginePrivate *self) {
  return new QAudioDevice(self->outputDevice());
}

//  void QAudioEnginePrivate::addSound(QSpatialAudioSoundPrivate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate8addSoundEP25QSpatialAudioSoundPrivate(
    QAudioEnginePrivate *self,
    QSpatialAudioSoundPrivate *a0) {
  self->addSound(a0);
}

//  void QAudioEnginePrivate::removeSound(QSpatialAudioSoundPrivate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate11removeSoundEP25QSpatialAudioSoundPrivate(
    QAudioEnginePrivate *self,
    QSpatialAudioSoundPrivate *a0) {
  self->removeSound(a0);
}

//  void QAudioEnginePrivate::setSoundPlaybackData(QSpatialAudioSoundPrivate
//      *a0, SharedPlaybackState a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioEnginePrivate20setSoundPlaybackDataEP25QSpatialAudioSoundPrivateSt10shared_ptrIN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateEE(
    QAudioEnginePrivate *self,
    QSpatialAudioSoundPrivate *a0,
    const QAudioEnginePrivate::SharedPlaybackState *a1) {
  self->setSoundPlaybackData(a0, *a1);
}

//  SmallestRoomForListenerResult
//      QAudioEnginePrivate::findSmallestRoomForListener(QSpan<QAudioRoom *>
//      rooms) const
extern "C" Q_DECL_EXPORT
QAudioEnginePrivate::SmallestRoomForListenerResult *ritual_ZNK19QAudioEnginePrivate27findSmallestRoomForListenerE5QSpanIP10QAudioRoomLm18446744073709551615EE(
    const QAudioEnginePrivate *self,
    const QSpan<QAudioRoom *> *rooms) {
  return new QAudioEnginePrivate::SmallestRoomForListenerResult(
      self->findSmallestRoomForListener(
          *rooms));
}

//  a Python function taken by a CuteQAudioEnginePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioEnginePrivate(
    QAudioEnginePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioEnginePrivate *>(self)->take(key, call);
}

//  a std::optional<QVector3D> a ritual of QAudioEnginePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioEnginePrivate__std_optional_QVector3D(
    std::optional<QVector3D> *self) {
  delete self;
}

//  a QAudioEnginePrivate::SmallestRoomForListenerResult a ritual of
//      QAudioEnginePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioEnginePrivate__QAudioEnginePrivate_SmallestRoomForListenerResult(
    QAudioEnginePrivate::SmallestRoomForListenerResult *self) {
  delete self;
}
