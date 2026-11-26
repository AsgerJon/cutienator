//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickimageprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickimageprovider.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickImageResponse that Python can take functions over in. Every QQuickImageResponse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickImageResponseCall0)(const void *, int *);
typedef QString * (*CuteQQuickImageResponseCall1)(const void *, int *);
typedef void (*CuteQQuickImageResponseCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageResponseCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageResponseCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageResponseCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageResponseCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageResponseCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageResponseCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageResponseCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImageResponse : public QQuickImageResponse {
public:
  using QQuickImageResponse::QQuickImageResponse;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QQuickImageResponse14textureFactoryEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QQuickImageResponse11errorStringEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageResponse6cancelEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QQuickTextureFactory *QQuickImageResponse::textureFactory() const
  QQuickTextureFactory *textureFactory() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageResponseCall0 call = reinterpret_cast<CuteQQuickImageResponseCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return {};
  }

  //  QString QQuickImageResponse::errorString() const
  QString errorString() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageResponseCall1 call = reinterpret_cast<CuteQQuickImageResponseCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickImageResponse::errorString();
  }

  //  void QQuickImageResponse::cancel()
  void cancel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageResponseCall2 call = reinterpret_cast<CuteQQuickImageResponseCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageResponse::cancel();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageResponseCall3 call = reinterpret_cast<CuteQQuickImageResponseCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImageResponseCall4 call = reinterpret_cast<CuteQQuickImageResponseCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImageResponseCall5 call = reinterpret_cast<CuteQQuickImageResponseCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImageResponseCall6 call = reinterpret_cast<CuteQQuickImageResponseCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickImageResponseCall7 call = reinterpret_cast<CuteQQuickImageResponseCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickImageResponseCall8 call = reinterpret_cast<CuteQQuickImageResponseCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickImageResponseCall9 call = reinterpret_cast<CuteQQuickImageResponseCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickImageResponse::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickImageResponse10metaObjectEv(
    const QQuickImageResponse *self) {
  return self->metaObject();
}

//  void *QQuickImageResponse::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickImageResponse11qt_metacastEPKc(
    QQuickImageResponse *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickImageResponse::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickImageResponse11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickImageResponse *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickImageResponse::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickImageResponse2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImageResponse::tr(s, c, n));
}

//  QQuickImageResponse::QQuickImageResponse()
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_ZN19QQuickImageResponseC1Ev() {
  return new CuteQQuickImageResponse();
}

//  QQuickImageResponse::~QQuickImageResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageResponseD1Ev(QQuickImageResponse *self) {
  delete self;
}

//  QQuickTextureFactory *QQuickImageResponse::textureFactory() const
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZNK19QQuickImageResponse14textureFactoryEv(
    const QQuickImageResponse *self) {
  return self->textureFactory();
}

//  QString QQuickImageResponse::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickImageResponse11errorStringEv(
    const QQuickImageResponse *self) {
  return new QString(self->errorString());
}

//  void QQuickImageResponse::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageResponse6cancelEv(QQuickImageResponse *self) {
  self->cancel();
}

//  void QQuickImageResponse::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageResponse8finishedEv(QQuickImageResponse *self) {
  self->finished();
}

//  QQuickImageResponsePrivate *QQuickImageResponse::d_func()
extern "C" Q_DECL_EXPORT
QQuickImageResponsePrivate *ritual_ZN19QQuickImageResponse6d_funcEv(
    QQuickImageResponse *self) {
  return self->d_func();
}

//  const QQuickImageResponsePrivate *QQuickImageResponse::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickImageResponsePrivate *ritual_ZNK19QQuickImageResponse6d_funcEv(
    const QQuickImageResponse *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickImageResponse, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageResponse(
    QQuickImageResponse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageResponse *>(self)->take(key, call);
}

//  QString QQuickImageResponse::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QQuickImageResponse11errorStringEv(
    const QQuickImageResponse *self) {
  return new QString(self->QQuickImageResponse::errorString());
}

//  void QQuickImageResponse::cancel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickImageResponse6cancelEv(QQuickImageResponse *self) {
  self->QQuickImageResponse::cancel();
}
