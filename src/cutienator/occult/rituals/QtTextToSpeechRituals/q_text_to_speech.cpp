//  Written by dev_tooling.RitualGenerator from the records of
//  QtTextToSpeech/qtexttospeech.h, Qt 6.12.0. Changes made here are lost.
#include <QtTextToSpeech/qtexttospeech.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlocale.h>
#include <QtTextToSpeech/qvoice.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QTextToSpeech that Python can take functions over in. Every QTextToSpeech
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextToSpeechCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextToSpeechCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTextToSpeech : public QTextToSpeech {
public:
  using QTextToSpeech::QTextToSpeech;
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
      CuteQTextToSpeechCall0 call = reinterpret_cast<CuteQTextToSpeechCall0>(taken[0]);
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
      CuteQTextToSpeechCall1 call = reinterpret_cast<CuteQTextToSpeechCall1>(taken[1]);
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
      CuteQTextToSpeechCall2 call = reinterpret_cast<CuteQTextToSpeechCall2>(taken[2]);
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
      CuteQTextToSpeechCall3 call = reinterpret_cast<CuteQTextToSpeechCall3>(taken[3]);
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
      CuteQTextToSpeechCall4 call = reinterpret_cast<CuteQTextToSpeechCall4>(taken[4]);
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
      CuteQTextToSpeechCall5 call = reinterpret_cast<CuteQTextToSpeechCall5>(taken[5]);
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
      CuteQTextToSpeechCall6 call = reinterpret_cast<CuteQTextToSpeechCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTextToSpeech::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QTextToSpeech10metaObjectEv(
    const QTextToSpeech *self) {
  return self->metaObject();
}

//  void *QTextToSpeech::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QTextToSpeech11qt_metacastEPKc(
    QTextToSpeech *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTextToSpeech::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QTextToSpeech11qt_metacallEN11QMetaObject4CallEiPPv(
    QTextToSpeech *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTextToSpeech::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QTextToSpeech2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextToSpeech::tr(s, c, n));
}

//  QTextToSpeechPrivate *QTextToSpeech::d_func()
extern "C" Q_DECL_EXPORT
QTextToSpeechPrivate *ritual_ZN13QTextToSpeech6d_funcEv(
    QTextToSpeech *self) {
  return self->d_func();
}

//  const QTextToSpeechPrivate *QTextToSpeech::d_func() const
extern "C" Q_DECL_EXPORT
const QTextToSpeechPrivate *ritual_ZNK13QTextToSpeech6d_funcEv(
    const QTextToSpeech *self) {
  return self->d_func();
}

//  QTextToSpeech::QTextToSpeech(QObject *parent)
extern "C" Q_DECL_EXPORT
QTextToSpeech *ritual_ZN13QTextToSpeechC1EP7QObject(QObject *parent) {
  return new CuteQTextToSpeech(parent);
}

//  QTextToSpeech::QTextToSpeech(const QString &engine, QObject *parent)
extern "C" Q_DECL_EXPORT
QTextToSpeech *ritual_ZN13QTextToSpeechC1ERK7QStringP7QObject(
    const QString *engine,
    QObject *parent) {
  return new CuteQTextToSpeech(*engine, parent);
}

//  QTextToSpeech::QTextToSpeech(const QString &engine, const QVariantMap
//      &params, QObject *parent)
extern "C" Q_DECL_EXPORT
QTextToSpeech *ritual_ZN13QTextToSpeechC1ERK7QStringRK4QMapIS0_8QVariantEP7QObject(
    const QString *engine,
    const QMap<QString, QVariant> *params,
    QObject *parent) {
  return new CuteQTextToSpeech(*engine, *params, parent);
}

//  QTextToSpeech::~QTextToSpeech()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeechD1Ev(QTextToSpeech *self) {
  delete self;
}

//  bool QTextToSpeech::setEngine(const QString &engine, const QVariantMap
//      &params)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QTextToSpeech9setEngineERK7QStringRK4QMapIS0_8QVariantE(
    QTextToSpeech *self,
    const QString *engine,
    const QMap<QString, QVariant> *params) {
  return self->setEngine(*engine, *params);
}

//  QString QTextToSpeech::engine() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextToSpeech6engineEv(const QTextToSpeech *self) {
  return new QString(self->engine());
}

//  QTextToSpeech::Capabilities QTextToSpeech::engineCapabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextToSpeech18engineCapabilitiesEv(
    const QTextToSpeech *self) {
  return static_cast<int>(self->engineCapabilities().toInt());
}

//  QTextToSpeech::State QTextToSpeech::state() const
extern "C" Q_DECL_EXPORT
QTextToSpeech::State ritual_ZNK13QTextToSpeech5stateEv(
    const QTextToSpeech *self) {
  return self->state();
}

//  QTextToSpeech::ErrorReason QTextToSpeech::errorReason() const
extern "C" Q_DECL_EXPORT
QTextToSpeech::ErrorReason ritual_ZNK13QTextToSpeech11errorReasonEv(
    const QTextToSpeech *self) {
  return self->errorReason();
}

//  QString QTextToSpeech::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextToSpeech11errorStringEv(
    const QTextToSpeech *self) {
  return new QString(self->errorString());
}

//  QList<QLocale> QTextToSpeech::availableLocales() const
extern "C" Q_DECL_EXPORT
QList<QLocale> *ritual_ZNK13QTextToSpeech16availableLocalesEv(
    const QTextToSpeech *self) {
  return new QList<QLocale>(self->availableLocales());
}

//  QLocale QTextToSpeech::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK13QTextToSpeech6localeEv(const QTextToSpeech *self) {
  return new QLocale(self->locale());
}

//  QVoice QTextToSpeech::voice() const
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZNK13QTextToSpeech5voiceEv(const QTextToSpeech *self) {
  return new QVoice(self->voice());
}

//  QList<QVoice> QTextToSpeech::availableVoices() const
extern "C" Q_DECL_EXPORT
QList<QVoice> *ritual_ZNK13QTextToSpeech15availableVoicesEv(
    const QTextToSpeech *self) {
  return new QList<QVoice>(self->availableVoices());
}

//  double QTextToSpeech::rate() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QTextToSpeech4rateEv(const QTextToSpeech *self) {
  return self->rate();
}

//  double QTextToSpeech::pitch() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QTextToSpeech5pitchEv(const QTextToSpeech *self) {
  return self->pitch();
}

//  double QTextToSpeech::volume() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QTextToSpeech6volumeEv(const QTextToSpeech *self) {
  return self->volume();
}

//  QStringList QTextToSpeech::availableEngines()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN13QTextToSpeech16availableEnginesEv() {
  return new QList<QString>(QTextToSpeech::availableEngines());
}

//  void QTextToSpeech::say(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech3sayERK7QString(
    QTextToSpeech *self,
    const QString *text) {
  self->say(*text);
}

//  qsizetype QTextToSpeech::enqueue(const QString &text)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN13QTextToSpeech7enqueueERK7QString(
    QTextToSpeech *self,
    const QString *text) {
  return self->enqueue(*text);
}

//  void QTextToSpeech::stop(QTextToSpeech::BoundaryHint boundaryHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech4stopENS_12BoundaryHintE(
    QTextToSpeech *self,
    QTextToSpeech::BoundaryHint boundaryHint) {
  self->stop(boundaryHint);
}

//  void QTextToSpeech::pause(QTextToSpeech::BoundaryHint boundaryHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech5pauseENS_12BoundaryHintE(
    QTextToSpeech *self,
    QTextToSpeech::BoundaryHint boundaryHint) {
  self->pause(boundaryHint);
}

//  void QTextToSpeech::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech6resumeEv(QTextToSpeech *self) {
  self->resume();
}

//  void QTextToSpeech::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech9setLocaleERK7QLocale(
    QTextToSpeech *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  void QTextToSpeech::setRate(double rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech7setRateEd(QTextToSpeech *self, double rate) {
  self->setRate(rate);
}

//  void QTextToSpeech::setPitch(double pitch)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech8setPitchEd(QTextToSpeech *self, double pitch) {
  self->setPitch(pitch);
}

//  void QTextToSpeech::setVolume(double volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech9setVolumeEd(
    QTextToSpeech *self,
    double volume) {
  self->setVolume(volume);
}

//  void QTextToSpeech::setVoice(const QVoice &voice)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech8setVoiceERK6QVoice(
    QTextToSpeech *self,
    const QVoice *voice) {
  self->setVoice(*voice);
}

//  void QTextToSpeech::engineChanged(const QString &engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech13engineChangedERK7QString(
    QTextToSpeech *self,
    const QString *engine) {
  self->engineChanged(*engine);
}

//  void QTextToSpeech::stateChanged(QTextToSpeech::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech12stateChangedENS_5StateE(
    QTextToSpeech *self,
    QTextToSpeech::State state) {
  self->stateChanged(state);
}

//  void QTextToSpeech::errorOccurred(QTextToSpeech::ErrorReason error, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech13errorOccurredENS_11ErrorReasonERK7QString(
    QTextToSpeech *self,
    QTextToSpeech::ErrorReason error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  void QTextToSpeech::localeChanged(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech13localeChangedERK7QLocale(
    QTextToSpeech *self,
    const QLocale *locale) {
  self->localeChanged(*locale);
}

//  void QTextToSpeech::rateChanged(double rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech11rateChangedEd(
    QTextToSpeech *self,
    double rate) {
  self->rateChanged(rate);
}

//  void QTextToSpeech::pitchChanged(double pitch)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech12pitchChangedEd(
    QTextToSpeech *self,
    double pitch) {
  self->pitchChanged(pitch);
}

//  void QTextToSpeech::volumeChanged(double volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech13volumeChangedEd(
    QTextToSpeech *self,
    double volume) {
  self->volumeChanged(volume);
}

//  void QTextToSpeech::voiceChanged(const QVoice &voice)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech12voiceChangedERK6QVoice(
    QTextToSpeech *self,
    const QVoice *voice) {
  self->voiceChanged(*voice);
}

//  void QTextToSpeech::sayingWord(const QString &word, qsizetype id,
//      qsizetype start, qsizetype length)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech10sayingWordERK7QStringxxx(
    QTextToSpeech *self,
    const QString *word,
    qsizetype id,
    qsizetype start,
    qsizetype length) {
  self->sayingWord(*word, id, start, length);
}

//  void QTextToSpeech::aboutToSynthesize(qsizetype id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech17aboutToSynthesizeEx(
    QTextToSpeech *self,
    qsizetype id) {
  self->aboutToSynthesize(id);
}

//  QList<QVoice> QTextToSpeech::allVoices(const QLocale *locale) const
extern "C" Q_DECL_EXPORT
QList<QVoice> *ritual_ZNK13QTextToSpeech9allVoicesEPK7QLocale(
    const QTextToSpeech *self,
    const QLocale *locale) {
  return new QList<QVoice>(self->allVoices(locale));
}

//  void QTextToSpeech::synthesizeImpl(const QString &text,
//      QtPrivate::QSlotObjectBase *slotObj, const QObject *context,
//      SynthesizeOverload overload)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextToSpeech14synthesizeImplERK7QStringPN9QtPrivate15QSlotObjectBaseEPK7QObjectNS_18SynthesizeOverloadE(
    QTextToSpeech *self,
    const QString *text,
    QtPrivate::QSlotObjectBase *slotObj,
    const QObject *context,
    QTextToSpeech::SynthesizeOverload overload) {
  self->synthesizeImpl(*text, slotObj, context, overload);
}

//  a Python function taken by a CuteQTextToSpeech, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextToSpeech(
    QTextToSpeech *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextToSpeech *>(self)->take(key, call);
}
