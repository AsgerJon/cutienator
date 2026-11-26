//  Written by dev_tooling.RitualGenerator from the records of
//  QtTextToSpeech/qtexttospeechengine.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtTextToSpeech/qtexttospeechengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtTextToSpeech/qvoice.h>
#include <QtCore/qvariant.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QTextToSpeechEngine that Python can take functions over in. Every QTextToSpeechEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQTextToSpeechEngineCall0)(const void *, int *);
typedef void (*CuteQTextToSpeechEngineCall1)(const void *, const QString *, int *);
typedef void (*CuteQTextToSpeechEngineCall2)(const void *, const QString *, int *);
typedef void (*CuteQTextToSpeechEngineCall3)(const void *, int, int *);
typedef void (*CuteQTextToSpeechEngineCall4)(const void *, int, int *);
typedef void (*CuteQTextToSpeechEngineCall5)(const void *, int *);
typedef double (*CuteQTextToSpeechEngineCall6)(const void *, int *);
typedef bool (*CuteQTextToSpeechEngineCall7)(const void *, double, int *);
typedef double (*CuteQTextToSpeechEngineCall8)(const void *, int *);
typedef bool (*CuteQTextToSpeechEngineCall9)(const void *, double, int *);
typedef const QLocale * (*CuteQTextToSpeechEngineCall10)(const void *, int *);
typedef bool (*CuteQTextToSpeechEngineCall11)(const void *, const QLocale *, int *);
typedef double (*CuteQTextToSpeechEngineCall12)(const void *, int *);
typedef bool (*CuteQTextToSpeechEngineCall13)(const void *, double, int *);
typedef const QVoice * (*CuteQTextToSpeechEngineCall14)(const void *, int *);
typedef bool (*CuteQTextToSpeechEngineCall15)(const void *, const QVoice *, int *);
typedef int (*CuteQTextToSpeechEngineCall16)(const void *, int *);
typedef int (*CuteQTextToSpeechEngineCall17)(const void *, int *);
typedef QString * (*CuteQTextToSpeechEngineCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextToSpeechEngineCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextToSpeechEngineCall20)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechEngineCall21)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechEngineCall22)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechEngineCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechEngineCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextToSpeechEngineCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTextToSpeechEngine : public QTextToSpeechEngine {
public:
  using QTextToSpeechEngine::QTextToSpeechEngine;
  void *taken[26] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine12capabilitiesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine3sayERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine10synthesizeERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine4stopEN13QTextToSpeech12BoundaryHintE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine5pauseEN13QTextToSpeech12BoundaryHintE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine6resumeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine4rateEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine7setRateEd")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine5pitchEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine8setPitchEd")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine6localeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine9setLocaleERK7QLocale")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine6volumeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine9setVolumeEd")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine5voiceEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QTextToSpeechEngine8setVoiceERK6QVoice")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine5stateEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine11errorReasonEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QTextToSpeechEngine11errorStringEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QTextToSpeech::Capabilities QTextToSpeechEngine::capabilities() const
  QTextToSpeech::Capabilities capabilities() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall0 call = reinterpret_cast<CuteQTextToSpeechEngineCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return QFlags<QTextToSpeech::Capability>::fromInt(given);
    }
    return QTextToSpeechEngine::capabilities();
  }

  //  void QTextToSpeechEngine::say(const QString &text)
  void say(const QString &text) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall1 call = reinterpret_cast<CuteQTextToSpeechEngineCall1>(taken[1]);
      call(this, &text, &handled);
      if (handled) return;
    }
  }

  //  void QTextToSpeechEngine::synthesize(const QString &text)
  void synthesize(const QString &text) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall2 call = reinterpret_cast<CuteQTextToSpeechEngineCall2>(taken[2]);
      call(this, &text, &handled);
      if (handled) return;
    }
  }

  //  void QTextToSpeechEngine::stop(QTextToSpeech::BoundaryHint
  //      boundaryHint)
  void stop(QTextToSpeech::BoundaryHint boundaryHint) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall3 call = reinterpret_cast<CuteQTextToSpeechEngineCall3>(taken[3]);
      call(this, static_cast<int>(boundaryHint), &handled);
      if (handled) return;
    }
  }

  //  void QTextToSpeechEngine::pause(QTextToSpeech::BoundaryHint
  //      boundaryHint)
  void pause(QTextToSpeech::BoundaryHint boundaryHint) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall4 call = reinterpret_cast<CuteQTextToSpeechEngineCall4>(taken[4]);
      call(this, static_cast<int>(boundaryHint), &handled);
      if (handled) return;
    }
  }

  //  void QTextToSpeechEngine::resume()
  void resume() override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall5 call = reinterpret_cast<CuteQTextToSpeechEngineCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  double QTextToSpeechEngine::rate() const
  double rate() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall6 call = reinterpret_cast<CuteQTextToSpeechEngineCall6>(taken[6]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QTextToSpeechEngine::setRate(double rate)
  bool setRate(double rate) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall7 call = reinterpret_cast<CuteQTextToSpeechEngineCall7>(taken[7]);
      bool given = call(this, rate, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  double QTextToSpeechEngine::pitch() const
  double pitch() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall8 call = reinterpret_cast<CuteQTextToSpeechEngineCall8>(taken[8]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QTextToSpeechEngine::setPitch(double pitch)
  bool setPitch(double pitch) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall9 call = reinterpret_cast<CuteQTextToSpeechEngineCall9>(taken[9]);
      bool given = call(this, pitch, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QLocale QTextToSpeechEngine::locale() const
  QLocale locale() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall10 call = reinterpret_cast<CuteQTextToSpeechEngineCall10>(taken[10]);
      const QLocale * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QTextToSpeechEngine::setLocale(const QLocale &locale)
  bool setLocale(const QLocale &locale) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall11 call = reinterpret_cast<CuteQTextToSpeechEngineCall11>(taken[11]);
      bool given = call(this, &locale, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  double QTextToSpeechEngine::volume() const
  double volume() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall12 call = reinterpret_cast<CuteQTextToSpeechEngineCall12>(taken[12]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QTextToSpeechEngine::setVolume(double volume)
  bool setVolume(double volume) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall13 call = reinterpret_cast<CuteQTextToSpeechEngineCall13>(taken[13]);
      bool given = call(this, volume, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QVoice QTextToSpeechEngine::voice() const
  QVoice voice() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall14 call = reinterpret_cast<CuteQTextToSpeechEngineCall14>(taken[14]);
      const QVoice * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QTextToSpeechEngine::setVoice(const QVoice &voice)
  bool setVoice(const QVoice &voice) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall15 call = reinterpret_cast<CuteQTextToSpeechEngineCall15>(taken[15]);
      bool given = call(this, &voice, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QTextToSpeech::State QTextToSpeechEngine::state() const
  QTextToSpeech::State state() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall16 call = reinterpret_cast<CuteQTextToSpeechEngineCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return static_cast<QTextToSpeech::State>(given);
    }
    return {};
  }

  //  QTextToSpeech::ErrorReason QTextToSpeechEngine::errorReason() const
  QTextToSpeech::ErrorReason errorReason() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall17 call = reinterpret_cast<CuteQTextToSpeechEngineCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QTextToSpeech::ErrorReason>(given);
    }
    return {};
  }

  //  QString QTextToSpeechEngine::errorString() const
  QString errorString() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall18 call = reinterpret_cast<CuteQTextToSpeechEngineCall18>(taken[18]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall19 call = reinterpret_cast<CuteQTextToSpeechEngineCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall20 call = reinterpret_cast<CuteQTextToSpeechEngineCall20>(taken[20]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall21 call = reinterpret_cast<CuteQTextToSpeechEngineCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall22 call = reinterpret_cast<CuteQTextToSpeechEngineCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall23 call = reinterpret_cast<CuteQTextToSpeechEngineCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall24 call = reinterpret_cast<CuteQTextToSpeechEngineCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTextToSpeechEngineCall25 call = reinterpret_cast<CuteQTextToSpeechEngineCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTextToSpeechEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QTextToSpeechEngine10metaObjectEv(
    const QTextToSpeechEngine *self) {
  return self->metaObject();
}

//  void *QTextToSpeechEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QTextToSpeechEngine11qt_metacastEPKc(
    QTextToSpeechEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTextToSpeechEngine::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QTextToSpeechEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QTextToSpeechEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTextToSpeechEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QTextToSpeechEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextToSpeechEngine::tr(s, c, n));
}

//  QTextToSpeechEngine::~QTextToSpeechEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngineD1Ev(QTextToSpeechEngine *self) {
  delete self;
}

//  QTextToSpeech::Capabilities QTextToSpeechEngine::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextToSpeechEngine12capabilitiesEv(
    const QTextToSpeechEngine *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  QList<QLocale> QTextToSpeechEngine::availableLocales() const
extern "C" Q_DECL_EXPORT
QList<QLocale> *ritual_ZNK19QTextToSpeechEngine16availableLocalesEv(
    const QTextToSpeechEngine *self) {
  return new QList<QLocale>(self->availableLocales());
}

//  QList<QVoice> QTextToSpeechEngine::availableVoices() const
extern "C" Q_DECL_EXPORT
QList<QVoice> *ritual_ZNK19QTextToSpeechEngine15availableVoicesEv(
    const QTextToSpeechEngine *self) {
  return new QList<QVoice>(self->availableVoices());
}

//  void QTextToSpeechEngine::say(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine3sayERK7QString(
    QTextToSpeechEngine *self,
    const QString *text) {
  self->say(*text);
}

//  void QTextToSpeechEngine::synthesize(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine10synthesizeERK7QString(
    QTextToSpeechEngine *self,
    const QString *text) {
  self->synthesize(*text);
}

//  void QTextToSpeechEngine::stop(QTextToSpeech::BoundaryHint boundaryHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine4stopEN13QTextToSpeech12BoundaryHintE(
    QTextToSpeechEngine *self,
    QTextToSpeech::BoundaryHint boundaryHint) {
  self->stop(boundaryHint);
}

//  void QTextToSpeechEngine::pause(QTextToSpeech::BoundaryHint boundaryHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine5pauseEN13QTextToSpeech12BoundaryHintE(
    QTextToSpeechEngine *self,
    QTextToSpeech::BoundaryHint boundaryHint) {
  self->pause(boundaryHint);
}

//  void QTextToSpeechEngine::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine6resumeEv(QTextToSpeechEngine *self) {
  self->resume();
}

//  double QTextToSpeechEngine::rate() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK19QTextToSpeechEngine4rateEv(
    const QTextToSpeechEngine *self) {
  return self->rate();
}

//  bool QTextToSpeechEngine::setRate(double rate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextToSpeechEngine7setRateEd(
    QTextToSpeechEngine *self,
    double rate) {
  return self->setRate(rate);
}

//  double QTextToSpeechEngine::pitch() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK19QTextToSpeechEngine5pitchEv(
    const QTextToSpeechEngine *self) {
  return self->pitch();
}

//  bool QTextToSpeechEngine::setPitch(double pitch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextToSpeechEngine8setPitchEd(
    QTextToSpeechEngine *self,
    double pitch) {
  return self->setPitch(pitch);
}

//  QLocale QTextToSpeechEngine::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK19QTextToSpeechEngine6localeEv(
    const QTextToSpeechEngine *self) {
  return new QLocale(self->locale());
}

//  bool QTextToSpeechEngine::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextToSpeechEngine9setLocaleERK7QLocale(
    QTextToSpeechEngine *self,
    const QLocale *locale) {
  return self->setLocale(*locale);
}

//  double QTextToSpeechEngine::volume() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK19QTextToSpeechEngine6volumeEv(
    const QTextToSpeechEngine *self) {
  return self->volume();
}

//  bool QTextToSpeechEngine::setVolume(double volume)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextToSpeechEngine9setVolumeEd(
    QTextToSpeechEngine *self,
    double volume) {
  return self->setVolume(volume);
}

//  QVoice QTextToSpeechEngine::voice() const
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZNK19QTextToSpeechEngine5voiceEv(
    const QTextToSpeechEngine *self) {
  return new QVoice(self->voice());
}

//  bool QTextToSpeechEngine::setVoice(const QVoice &voice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextToSpeechEngine8setVoiceERK6QVoice(
    QTextToSpeechEngine *self,
    const QVoice *voice) {
  return self->setVoice(*voice);
}

//  QTextToSpeech::State QTextToSpeechEngine::state() const
extern "C" Q_DECL_EXPORT
QTextToSpeech::State ritual_ZNK19QTextToSpeechEngine5stateEv(
    const QTextToSpeechEngine *self) {
  return self->state();
}

//  QTextToSpeech::ErrorReason QTextToSpeechEngine::errorReason() const
extern "C" Q_DECL_EXPORT
QTextToSpeech::ErrorReason ritual_ZNK19QTextToSpeechEngine11errorReasonEv(
    const QTextToSpeechEngine *self) {
  return self->errorReason();
}

//  QString QTextToSpeechEngine::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QTextToSpeechEngine11errorStringEv(
    const QTextToSpeechEngine *self) {
  return new QString(self->errorString());
}

//  QVoice QTextToSpeechEngine::createVoice(const QString &name, const
//      QLocale &locale, QVoice::Gender gender, QVoice::Age age, const
//      QVariant &data)
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZN19QTextToSpeechEngine11createVoiceERK7QStringRK7QLocaleN6QVoice6GenderENS6_3AgeERK8QVariant(
    const QString *name,
    const QLocale *locale,
    QVoice::Gender gender,
    QVoice::Age age,
    const QVariant *data) {
  return new QVoice(
      QTextToSpeechEngine::createVoice(
          *name,
          *locale,
          gender,
          age,
          *data));
}

//  QVariant QTextToSpeechEngine::voiceData(const QVoice &voice)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN19QTextToSpeechEngine9voiceDataERK6QVoice(
    const QVoice *voice) {
  return new QVariant(QTextToSpeechEngine::voiceData(*voice));
}

//  void QTextToSpeechEngine::stateChanged(QTextToSpeech::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine12stateChangedEN13QTextToSpeech5StateE(
    QTextToSpeechEngine *self,
    QTextToSpeech::State state) {
  self->stateChanged(state);
}

//  void QTextToSpeechEngine::errorOccurred(QTextToSpeech::ErrorReason error,
//      const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine13errorOccurredEN13QTextToSpeech11ErrorReasonERK7QString(
    QTextToSpeechEngine *self,
    QTextToSpeech::ErrorReason error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  void QTextToSpeechEngine::sayingWord(const QString &word, qsizetype
//      start, qsizetype length)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine10sayingWordERK7QStringxx(
    QTextToSpeechEngine *self,
    const QString *word,
    qsizetype start,
    qsizetype length) {
  self->sayingWord(*word, start, length);
}

//  void QTextToSpeechEngine::synthesized(const QAudioFormat &format, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechEngine11synthesizedERK12QAudioFormatRK10QByteArray(
    QTextToSpeechEngine *self,
    const QAudioFormat *format,
    const QByteArray *data) {
  self->synthesized(*format, *data);
}

//  a Python function taken by a CuteQTextToSpeechEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextToSpeechEngine(
    QTextToSpeechEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextToSpeechEngine *>(self)->take(key, call);
}

//  QTextToSpeech::Capabilities QTextToSpeechEngine::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QTextToSpeechEngine12capabilitiesEv(
    const QTextToSpeechEngine *self) {
  return static_cast<int>(self->QTextToSpeechEngine::capabilities().toInt());
}
