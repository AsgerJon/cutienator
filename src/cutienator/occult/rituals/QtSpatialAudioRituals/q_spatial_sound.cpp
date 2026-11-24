//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/qspatialsound.h, Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/qspatialsound.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSpatialSound that Python can take functions over in. Every QSpatialSound
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpatialSoundCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpatialSoundCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpatialSoundCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpatialSoundCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpatialSoundCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpatialSoundCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpatialSoundCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSpatialSound : public QSpatialSound {
public:
  using QSpatialSound::QSpatialSound;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpatialSoundCall0 call = reinterpret_cast<CuteQSpatialSoundCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpatialSoundCall1 call = reinterpret_cast<CuteQSpatialSoundCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSpatialSoundCall2 call = reinterpret_cast<CuteQSpatialSoundCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSpatialSoundCall3 call = reinterpret_cast<CuteQSpatialSoundCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSpatialSoundCall4 call = reinterpret_cast<CuteQSpatialSoundCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSpatialSoundCall5 call = reinterpret_cast<CuteQSpatialSoundCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSpatialSoundCall6 call = reinterpret_cast<CuteQSpatialSoundCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSpatialSound::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSpatialSound10metaObjectEv(
    const QSpatialSound *self) {
  return self->metaObject();
}

//  QString QSpatialSound::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSpatialSound2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSpatialSound::tr(s, c, n));
}

//  QSpatialSound::QSpatialSound(QAudioEngine *engine)
extern "C" Q_DECL_EXPORT
QSpatialSound *ritual_ZN13QSpatialSoundC1EP12QAudioEngine(
    QAudioEngine *engine) {
  return new CuteQSpatialSound(engine);
}

//  QSpatialSound::~QSpatialSound()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSoundD1Ev(QSpatialSound *self) {
  delete self;
}

//  void QSpatialSound::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound9setSourceERK4QUrl(
    QSpatialSound *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  QUrl QSpatialSound::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QSpatialSound6sourceEv(const QSpatialSound *self) {
  return new QUrl(self->source());
}

//  int QSpatialSound::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSpatialSound5loopsEv(const QSpatialSound *self) {
  return self->loops();
}

//  void QSpatialSound::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound8setLoopsEi(QSpatialSound *self, int loops) {
  self->setLoops(loops);
}

//  bool QSpatialSound::autoPlay() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSpatialSound8autoPlayEv(const QSpatialSound *self) {
  return self->autoPlay();
}

//  void QSpatialSound::setAutoPlay(bool autoPlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound11setAutoPlayEb(
    QSpatialSound *self,
    bool autoPlay) {
  self->setAutoPlay(autoPlay);
}

//  void QSpatialSound::setPosition(QVector3D pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound11setPositionE9QVector3D(
    QSpatialSound *self,
    const QVector3D *pos) {
  self->setPosition(*pos);
}

//  QVector3D QSpatialSound::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13QSpatialSound8positionEv(const QSpatialSound *self) {
  return new QVector3D(self->position());
}

//  void QSpatialSound::setRotation(const QQuaternion &q)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound11setRotationERK11QQuaternion(
    QSpatialSound *self,
    const QQuaternion *q) {
  self->setRotation(*q);
}

//  QQuaternion QSpatialSound::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK13QSpatialSound8rotationEv(
    const QSpatialSound *self) {
  return new QQuaternion(self->rotation());
}

//  void QSpatialSound::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound9setVolumeEf(
    QSpatialSound *self,
    float volume) {
  self->setVolume(volume);
}

//  float QSpatialSound::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound6volumeEv(const QSpatialSound *self) {
  return self->volume();
}

//  void QSpatialSound::setDistanceModel(DistanceModel model)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound16setDistanceModelENS_13DistanceModelE(
    QSpatialSound *self,
    QSpatialSound::DistanceModel model) {
  self->setDistanceModel(model);
}

//  DistanceModel QSpatialSound::distanceModel() const
extern "C" Q_DECL_EXPORT
QSpatialSound::DistanceModel ritual_ZNK13QSpatialSound13distanceModelEv(
    const QSpatialSound *self) {
  return self->distanceModel();
}

//  void QSpatialSound::setSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound7setSizeEf(QSpatialSound *self, float size) {
  self->setSize(size);
}

//  float QSpatialSound::size() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound4sizeEv(const QSpatialSound *self) {
  return self->size();
}

//  void QSpatialSound::setDistanceCutoff(float cutoff)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound17setDistanceCutoffEf(
    QSpatialSound *self,
    float cutoff) {
  self->setDistanceCutoff(cutoff);
}

//  float QSpatialSound::distanceCutoff() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound14distanceCutoffEv(
    const QSpatialSound *self) {
  return self->distanceCutoff();
}

//  void QSpatialSound::setManualAttenuation(float attenuation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound20setManualAttenuationEf(
    QSpatialSound *self,
    float attenuation) {
  self->setManualAttenuation(attenuation);
}

//  float QSpatialSound::manualAttenuation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound17manualAttenuationEv(
    const QSpatialSound *self) {
  return self->manualAttenuation();
}

//  void QSpatialSound::setOcclusionIntensity(float occlusion)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound21setOcclusionIntensityEf(
    QSpatialSound *self,
    float occlusion) {
  self->setOcclusionIntensity(occlusion);
}

//  float QSpatialSound::occlusionIntensity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound18occlusionIntensityEv(
    const QSpatialSound *self) {
  return self->occlusionIntensity();
}

//  void QSpatialSound::setDirectivity(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound14setDirectivityEf(
    QSpatialSound *self,
    float alpha) {
  self->setDirectivity(alpha);
}

//  float QSpatialSound::directivity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound11directivityEv(const QSpatialSound *self) {
  return self->directivity();
}

//  void QSpatialSound::setDirectivityOrder(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound19setDirectivityOrderEf(
    QSpatialSound *self,
    float alpha) {
  self->setDirectivityOrder(alpha);
}

//  float QSpatialSound::directivityOrder() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound16directivityOrderEv(
    const QSpatialSound *self) {
  return self->directivityOrder();
}

//  void QSpatialSound::setNearFieldGain(float gain)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound16setNearFieldGainEf(
    QSpatialSound *self,
    float gain) {
  self->setNearFieldGain(gain);
}

//  float QSpatialSound::nearFieldGain() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSpatialSound13nearFieldGainEv(const QSpatialSound *self) {
  return self->nearFieldGain();
}

//  QAudioEngine *QSpatialSound::engine() const
extern "C" Q_DECL_EXPORT
QAudioEngine *ritual_ZNK13QSpatialSound6engineEv(const QSpatialSound *self) {
  return self->engine();
}

//  void QSpatialSound::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound4playEv(QSpatialSound *self) {
  self->play();
}

//  void QSpatialSound::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound5pauseEv(QSpatialSound *self) {
  self->pause();
}

//  void QSpatialSound::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpatialSound4stopEv(QSpatialSound *self) {
  self->stop();
}

//  a Python function taken by a CuteQSpatialSound, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpatialSound(
    QSpatialSound *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpatialSound *>(self)->take(key, call);
}
