//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/qambientsound.h, Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/qambientsound.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAmbientSound that Python can take functions over in. Every QAmbientSound
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientSoundCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientSoundCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientSoundCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientSoundCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientSoundCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientSoundCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientSoundCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAmbientSound : public QAmbientSound {
public:
  using QAmbientSound::QAmbientSound;
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
      CuteQAmbientSoundCall0 call = reinterpret_cast<CuteQAmbientSoundCall0>(taken[0]);
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
      CuteQAmbientSoundCall1 call = reinterpret_cast<CuteQAmbientSoundCall1>(taken[1]);
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
      CuteQAmbientSoundCall2 call = reinterpret_cast<CuteQAmbientSoundCall2>(taken[2]);
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
      CuteQAmbientSoundCall3 call = reinterpret_cast<CuteQAmbientSoundCall3>(taken[3]);
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
      CuteQAmbientSoundCall4 call = reinterpret_cast<CuteQAmbientSoundCall4>(taken[4]);
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
      CuteQAmbientSoundCall5 call = reinterpret_cast<CuteQAmbientSoundCall5>(taken[5]);
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
      CuteQAmbientSoundCall6 call = reinterpret_cast<CuteQAmbientSoundCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAmbientSound::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QAmbientSound10metaObjectEv(
    const QAmbientSound *self) {
  return self->metaObject();
}

//  void *QAmbientSound::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QAmbientSound11qt_metacastEPKc(
    QAmbientSound *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAmbientSound::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QAmbientSound11qt_metacallEN11QMetaObject4CallEiPPv(
    QAmbientSound *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAmbientSound::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QAmbientSound2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAmbientSound::tr(s, c, n));
}

//  QAmbientSound::QAmbientSound(QAudioEngine *engine)
extern "C" Q_DECL_EXPORT
QAmbientSound *ritual_ZN13QAmbientSoundC1EP12QAudioEngine(
    QAudioEngine *engine) {
  return new CuteQAmbientSound(engine);
}

//  QAmbientSound::~QAmbientSound()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSoundD1Ev(QAmbientSound *self) {
  delete self;
}

//  void QAmbientSound::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound9setSourceERK4QUrl(
    QAmbientSound *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  QUrl QAmbientSound::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QAmbientSound6sourceEv(const QAmbientSound *self) {
  return new QUrl(self->source());
}

//  int QAmbientSound::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QAmbientSound5loopsEv(const QAmbientSound *self) {
  return self->loops();
}

//  void QAmbientSound::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound8setLoopsEi(QAmbientSound *self, int loops) {
  self->setLoops(loops);
}

//  bool QAmbientSound::autoPlay() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAmbientSound8autoPlayEv(const QAmbientSound *self) {
  return self->autoPlay();
}

//  void QAmbientSound::setAutoPlay(bool autoPlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound11setAutoPlayEb(
    QAmbientSound *self,
    bool autoPlay) {
  self->setAutoPlay(autoPlay);
}

//  void QAmbientSound::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound9setVolumeEf(
    QAmbientSound *self,
    float volume) {
  self->setVolume(volume);
}

//  float QAmbientSound::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QAmbientSound6volumeEv(const QAmbientSound *self) {
  return self->volume();
}

//  QAudioEngine *QAmbientSound::engine() const
extern "C" Q_DECL_EXPORT
QAudioEngine *ritual_ZNK13QAmbientSound6engineEv(const QAmbientSound *self) {
  return self->engine();
}

//  void QAmbientSound::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound13sourceChangedEv(QAmbientSound *self) {
  self->sourceChanged();
}

//  void QAmbientSound::loopsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound12loopsChangedEv(QAmbientSound *self) {
  self->loopsChanged();
}

//  void QAmbientSound::autoPlayChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound15autoPlayChangedEv(QAmbientSound *self) {
  self->autoPlayChanged();
}

//  void QAmbientSound::volumeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound13volumeChangedEv(QAmbientSound *self) {
  self->volumeChanged();
}

//  void QAmbientSound::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound4playEv(QAmbientSound *self) {
  self->play();
}

//  void QAmbientSound::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound5pauseEv(QAmbientSound *self) {
  self->pause();
}

//  void QAmbientSound::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAmbientSound4stopEv(QAmbientSound *self) {
  self->stop();
}

//  QAmbientSoundPrivate *QAmbientSound::d_func()
extern "C" Q_DECL_EXPORT
QAmbientSoundPrivate *ritual_ZN13QAmbientSound6d_funcEv(
    QAmbientSound *self) {
  return self->d_func();
}

//  const QAmbientSoundPrivate *QAmbientSound::d_func() const
extern "C" Q_DECL_EXPORT
const QAmbientSoundPrivate *ritual_ZNK13QAmbientSound6d_funcEv(
    const QAmbientSound *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAmbientSound, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAmbientSound(
    QAmbientSound *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAmbientSound *>(self)->take(key, call);
}
