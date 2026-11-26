//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DSpati
//  alAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3dspatialsound_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qtquick3daudioglobal_p.h>
#include <QtQuick3DSpatialAudio/QtQuick3DSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3dspatialsound_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DSpatialAudio/private/qquick3dspatialsound_p.h>
#include <QtMultimediaQuick/private/qqmlcontext_source_resolver_p.h>
#include <QtQuick3DSpatialAudio/private/qquick3daudioengine_p.h>
#include <QtSpatialAudio/qspatialsound.h>
#include <QtSpatialAudio/private/qspatialaudiosound_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 68, as _ZN20QQuick3DSpatialSound9setSourceERK4QUrl
inline void QQuick3DSpatialSound::setSource(const QUrl& source)
{
    m_sound->setSource(source);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 63, as _ZNK20QQuick3DSpatialSound6sourceEv
inline QUrl QQuick3DSpatialSound::source() const
{
    return m_sound->source();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 81, as _ZN20QQuick3DSpatialSound9setVolumeEf
inline void QQuick3DSpatialSound::setVolume(float volume)
{
    m_sound->setVolume(volume);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 86, as _ZNK20QQuick3DSpatialSound6volumeEv
inline float QQuick3DSpatialSound::volume() const
{
    return m_sound->volume();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 110, as _ZN20QQuick3DSpatialSound16setDistanceModelENS_13DistanceModelE
inline void QQuick3DSpatialSound::setDistanceModel(DistanceModel model)
{
    m_sound->setDistanceModel(QSpatialSound::DistanceModel(model));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 115, as _ZNK20QQuick3DSpatialSound13distanceModelEv
inline QQuick3DSpatialSound::DistanceModel QQuick3DSpatialSound::distanceModel() const
{
    return DistanceModel(m_sound->distanceModel());
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 127, as _ZN20QQuick3DSpatialSound7setSizeEf
inline void QQuick3DSpatialSound::setSize(float min)
{
    m_sound->setSize(min);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 132, as _ZNK20QQuick3DSpatialSound4sizeEv
inline float QQuick3DSpatialSound::size() const
{
    return m_sound->size();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 144, as _ZN20QQuick3DSpatialSound17setDistanceCutoffEf
inline void QQuick3DSpatialSound::setDistanceCutoff(float max)
{
    m_sound->setDistanceCutoff(max);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 149, as _ZNK20QQuick3DSpatialSound14distanceCutoffEv
inline float QQuick3DSpatialSound::distanceCutoff() const
{
    return m_sound->distanceCutoff();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 160, as _ZN20QQuick3DSpatialSound20setManualAttenuationEf
inline void QQuick3DSpatialSound::setManualAttenuation(float attenuation)
{
    m_sound->setManualAttenuation(attenuation);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 165, as _ZNK20QQuick3DSpatialSound17manualAttenuationEv
inline float QQuick3DSpatialSound::manualAttenuation() const
{
    return m_sound->manualAttenuation();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 178, as _ZN20QQuick3DSpatialSound21setOcclusionIntensityEf
inline void QQuick3DSpatialSound::setOcclusionIntensity(float occlusion)
{
    m_sound->setOcclusionIntensity(occlusion);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 183, as _ZNK20QQuick3DSpatialSound18occlusionIntensityEv
inline float QQuick3DSpatialSound::occlusionIntensity() const
{
    return m_sound->occlusionIntensity();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 197, as _ZN20QQuick3DSpatialSound14setDirectivityEf
inline void QQuick3DSpatialSound::setDirectivity(float alpha)
{
    m_sound->setDirectivity(alpha);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 202, as _ZNK20QQuick3DSpatialSound11directivityEv
inline float QQuick3DSpatialSound::directivity() const
{
    return m_sound->directivity();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 215, as _ZN20QQuick3DSpatialSound19setDirectivityOrderEf
inline void QQuick3DSpatialSound::setDirectivityOrder(float alpha)
{
    m_sound->setDirectivityOrder(alpha);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 220, as _ZNK20QQuick3DSpatialSound16directivityOrderEv
inline float QQuick3DSpatialSound::directivityOrder() const
{
    return m_sound->directivityOrder();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 232, as _ZN20QQuick3DSpatialSound16setNearFieldGainEf
inline void QQuick3DSpatialSound::setNearFieldGain(float gain)
{
    m_sound->setNearFieldGain(gain);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 237, as _ZNK20QQuick3DSpatialSound13nearFieldGainEv
inline float QQuick3DSpatialSound::nearFieldGain() const
{
    return m_sound->nearFieldGain();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 260, as _ZNK20QQuick3DSpatialSound5loopsEv
inline int QQuick3DSpatialSound::loops() const
{
    return m_sound->loops();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 265, as _ZN20QQuick3DSpatialSound8setLoopsEi
inline void QQuick3DSpatialSound::setLoops(int loops)
{
    m_sound->setLoops(loops);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 278, as _ZNK20QQuick3DSpatialSound8autoPlayEv
inline bool QQuick3DSpatialSound::autoPlay() const
{
    return m_sound->autoPlay();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dspatialsound.cpp, line 283, as _ZN20QQuick3DSpatialSound11setAutoPlayEb
inline void QQuick3DSpatialSound::setAutoPlay(bool autoPlay)
{
    m_sound->setAutoPlay(autoPlay);
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuick3DSpatialSound may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DSpatialSound : QQuick3DSpatialSound {
  using QQuick3DSpatialSound::updateSpatialNode;
};

//  A QQuick3DSpatialSound that Python can take functions over in. Every QQuick3DSpatialSound
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DSpatialSoundCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DSpatialSoundCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpatialSoundCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpatialSoundCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpatialSoundCall4)(const void *, int *);
typedef void (*CuteQQuick3DSpatialSoundCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DSpatialSoundCall6)(const void *, int *);
typedef void (*CuteQQuick3DSpatialSoundCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSpatialSoundCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSpatialSoundCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpatialSoundCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpatialSoundCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpatialSoundCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DSpatialSound : public QQuick3DSpatialSound {
public:
  using QQuick3DSpatialSound::QQuick3DSpatialSound;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DSpatialSound::updateSpatialNode(QSSGRenderGraphObject
  //      *a0)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall0 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DSpatialSound::updateSpatialNode(a0);
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall1 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall2 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall3 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall4 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall5 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall6 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall7 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall8 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall9 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall10 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall11 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DSpatialSoundCall12 call = reinterpret_cast<CuteQQuick3DSpatialSoundCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DSpatialSound::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuick3DSpatialSound10metaObjectEv(
    const QQuick3DSpatialSound *self) {
  return self->metaObject();
}

//  void *QQuick3DSpatialSound::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuick3DSpatialSound11qt_metacastEPKc(
    QQuick3DSpatialSound *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DSpatialSound::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuick3DSpatialSound11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DSpatialSound *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DSpatialSound::~QQuick3DSpatialSound()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSoundD1Ev(QQuick3DSpatialSound *self) {
  delete self;
}

//  void QQuick3DSpatialSound::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound9setSourceERK4QUrl(
    QQuick3DSpatialSound *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QUrl QQuick3DSpatialSound::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuick3DSpatialSound6sourceEv(
    const QQuick3DSpatialSound *self) {
  return new QUrl(self->source());
}

//  void QQuick3DSpatialSound::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound9setVolumeEf(
    QQuick3DSpatialSound *self,
    float volume) {
  self->setVolume(volume);
}

//  float QQuick3DSpatialSound::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound6volumeEv(
    const QQuick3DSpatialSound *self) {
  return self->volume();
}

//  void QQuick3DSpatialSound::setDistanceModel(DistanceModel model)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound16setDistanceModelENS_13DistanceModelE(
    QQuick3DSpatialSound *self,
    QQuick3DSpatialSound::DistanceModel model) {
  self->setDistanceModel(model);
}

//  DistanceModel QQuick3DSpatialSound::distanceModel() const
extern "C" Q_DECL_EXPORT
QQuick3DSpatialSound::DistanceModel ritual_ZNK20QQuick3DSpatialSound13distanceModelEv(
    const QQuick3DSpatialSound *self) {
  return self->distanceModel();
}

//  void QQuick3DSpatialSound::setSize(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound7setSizeEf(
    QQuick3DSpatialSound *self,
    float min) {
  self->setSize(min);
}

//  float QQuick3DSpatialSound::size() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound4sizeEv(
    const QQuick3DSpatialSound *self) {
  return self->size();
}

//  void QQuick3DSpatialSound::setDistanceCutoff(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound17setDistanceCutoffEf(
    QQuick3DSpatialSound *self,
    float max) {
  self->setDistanceCutoff(max);
}

//  float QQuick3DSpatialSound::distanceCutoff() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound14distanceCutoffEv(
    const QQuick3DSpatialSound *self) {
  return self->distanceCutoff();
}

//  void QQuick3DSpatialSound::setManualAttenuation(float attenuation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound20setManualAttenuationEf(
    QQuick3DSpatialSound *self,
    float attenuation) {
  self->setManualAttenuation(attenuation);
}

//  float QQuick3DSpatialSound::manualAttenuation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound17manualAttenuationEv(
    const QQuick3DSpatialSound *self) {
  return self->manualAttenuation();
}

//  void QQuick3DSpatialSound::setOcclusionIntensity(float occlusion)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound21setOcclusionIntensityEf(
    QQuick3DSpatialSound *self,
    float occlusion) {
  self->setOcclusionIntensity(occlusion);
}

//  float QQuick3DSpatialSound::occlusionIntensity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound18occlusionIntensityEv(
    const QQuick3DSpatialSound *self) {
  return self->occlusionIntensity();
}

//  void QQuick3DSpatialSound::setDirectivity(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound14setDirectivityEf(
    QQuick3DSpatialSound *self,
    float alpha) {
  self->setDirectivity(alpha);
}

//  float QQuick3DSpatialSound::directivity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound11directivityEv(
    const QQuick3DSpatialSound *self) {
  return self->directivity();
}

//  void QQuick3DSpatialSound::setDirectivityOrder(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound19setDirectivityOrderEf(
    QQuick3DSpatialSound *self,
    float alpha) {
  self->setDirectivityOrder(alpha);
}

//  float QQuick3DSpatialSound::directivityOrder() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound16directivityOrderEv(
    const QQuick3DSpatialSound *self) {
  return self->directivityOrder();
}

//  void QQuick3DSpatialSound::setNearFieldGain(float gain)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound16setNearFieldGainEf(
    QQuick3DSpatialSound *self,
    float gain) {
  self->setNearFieldGain(gain);
}

//  float QQuick3DSpatialSound::nearFieldGain() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DSpatialSound13nearFieldGainEv(
    const QQuick3DSpatialSound *self) {
  return self->nearFieldGain();
}

//  int QQuick3DSpatialSound::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuick3DSpatialSound5loopsEv(
    const QQuick3DSpatialSound *self) {
  return self->loops();
}

//  void QQuick3DSpatialSound::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound8setLoopsEi(
    QQuick3DSpatialSound *self,
    int loops) {
  self->setLoops(loops);
}

//  bool QQuick3DSpatialSound::autoPlay() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuick3DSpatialSound8autoPlayEv(
    const QQuick3DSpatialSound *self) {
  return self->autoPlay();
}

//  void QQuick3DSpatialSound::setAutoPlay(bool autoPlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound11setAutoPlayEb(
    QQuick3DSpatialSound *self,
    bool autoPlay) {
  self->setAutoPlay(autoPlay);
}

//  void QQuick3DSpatialSound::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound4playEv(QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "play()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "play()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound5pauseEv(QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pause()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pause()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound4stopEv(QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "stop()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "stop()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound13sourceChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::volumeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound13volumeChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "volumeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "volumeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::distanceModelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound20distanceModelChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "distanceModelChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "distanceModelChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::sizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound11sizeChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::distanceCutoffChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound21distanceCutoffChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "distanceCutoffChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "distanceCutoffChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::manualAttenuationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound24manualAttenuationChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "manualAttenuationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "manualAttenuationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::occlusionIntensityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound25occlusionIntensityChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "occlusionIntensityChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "occlusionIntensityChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::directivityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound18directivityChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "directivityChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "directivityChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::directivityOrderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound23directivityOrderChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "directivityOrderChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "directivityOrderChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::nearFieldGainChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound20nearFieldGainChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "nearFieldGainChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "nearFieldGainChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::loopsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound12loopsChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "loopsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "loopsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::autoPlayChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound15autoPlayChangedEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "autoPlayChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "autoPlayChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::updatePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound14updatePositionEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updatePosition()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updatePosition()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSpatialSound::updateRotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSpatialSound14updateRotationEv(
    QQuick3DSpatialSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSpatialSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateRotation()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateRotation()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QSSGRenderGraphObject
//      *QQuick3DSpatialSound::updateSpatialNode(QSSGRenderGraphObject *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN20QQuick3DSpatialSound17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSpatialSound *self,
    QSSGRenderGraphObject *a0) {
  return self->updateSpatialNode(a0);
}

//  a Python function taken by a CuteQQuick3DSpatialSound, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DSpatialSound(
    QQuick3DSpatialSound *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DSpatialSound *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DSpatialSound::updateSpatialNode(QSSGRenderGraphObject *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN20QQuick3DSpatialSound17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSpatialSound *self,
    QSSGRenderGraphObject *a0) {
  return static_cast<OwnQQuick3DSpatialSound *>(self)->OwnQQuick3DSpatialSound::updateSpatialNode(
      a0);
}
