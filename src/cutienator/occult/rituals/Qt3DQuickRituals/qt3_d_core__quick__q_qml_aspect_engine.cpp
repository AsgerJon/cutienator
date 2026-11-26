//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/qqmlaspectengine.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DQuick/Qt3DQuick>
#include <Qt3DQuick/qqmlaspectengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::Quick::QQmlAspectEngine that Python can take functions over in. Every Qt3DCore::Quick::QQmlAspectEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_QQmlAspectEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_QQmlAspectEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQmlAspectEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQmlAspectEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQmlAspectEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQmlAspectEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQmlAspectEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_Quick_QQmlAspectEngine : public Qt3DCore::Quick::QQmlAspectEngine {
public:
  using Qt3DCore::Quick::QQmlAspectEngine::QQmlAspectEngine;
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
      CuteQt3DCore_Quick_QQmlAspectEngineCall0 call = reinterpret_cast<CuteQt3DCore_Quick_QQmlAspectEngineCall0>(taken[0]);
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
      CuteQt3DCore_Quick_QQmlAspectEngineCall1 call = reinterpret_cast<CuteQt3DCore_Quick_QQmlAspectEngineCall1>(taken[1]);
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
      CuteQt3DCore_Quick_QQmlAspectEngineCall2 call = reinterpret_cast<CuteQt3DCore_Quick_QQmlAspectEngineCall2>(taken[2]);
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
      CuteQt3DCore_Quick_QQmlAspectEngineCall3 call = reinterpret_cast<CuteQt3DCore_Quick_QQmlAspectEngineCall3>(taken[3]);
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
      CuteQt3DCore_Quick_QQmlAspectEngineCall4 call = reinterpret_cast<CuteQt3DCore_Quick_QQmlAspectEngineCall4>(taken[4]);
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
      CuteQt3DCore_Quick_QQmlAspectEngineCall5 call = reinterpret_cast<CuteQt3DCore_Quick_QQmlAspectEngineCall5>(taken[5]);
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
      CuteQt3DCore_Quick_QQmlAspectEngineCall6 call = reinterpret_cast<CuteQt3DCore_Quick_QQmlAspectEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::Quick::QQmlAspectEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine10metaObjectEv(
    const Qt3DCore::Quick::QQmlAspectEngine *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Quick::QQmlAspectEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine11qt_metacastEPKc(
    Qt3DCore::Quick::QQmlAspectEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::Quick::QQmlAspectEngine::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Quick::QQmlAspectEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Quick::QQmlAspectEngine::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::QQmlAspectEngine::tr(s, c, n));
}

//  Qt3DCore::Quick::QQmlAspectEngine::QQmlAspectEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::QQmlAspectEngine *ritual_ZN8Qt3DCore5Quick16QQmlAspectEngineC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DCore_Quick_QQmlAspectEngine(parent);
}

//  Qt3DCore::Quick::QQmlAspectEngine::~QQmlAspectEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick16QQmlAspectEngineD1Ev(
    Qt3DCore::Quick::QQmlAspectEngine *self) {
  delete self;
}

//  Status Qt3DCore::Quick::QQmlAspectEngine::status() const
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::QQmlAspectEngine::Status ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine6statusEv(
    const Qt3DCore::Quick::QQmlAspectEngine *self) {
  return self->status();
}

//  void Qt3DCore::Quick::QQmlAspectEngine::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine9setSourceERK4QUrl(
    Qt3DCore::Quick::QQmlAspectEngine *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QQmlEngine *Qt3DCore::Quick::QQmlAspectEngine::qmlEngine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine9qmlEngineEv(
    const Qt3DCore::Quick::QQmlAspectEngine *self) {
  return self->qmlEngine();
}

//  QAspectEngine *Qt3DCore::Quick::QQmlAspectEngine::aspectEngine() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEngine *ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine12aspectEngineEv(
    const Qt3DCore::Quick::QQmlAspectEngine *self) {
  return self->aspectEngine();
}

//  void Qt3DCore::Quick::QQmlAspectEngine::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine13statusChangedENS1_6StatusE(
    Qt3DCore::Quick::QQmlAspectEngine *self,
    Qt3DCore::Quick::QQmlAspectEngine::Status a0) {
  self->statusChanged(a0);
}

//  void Qt3DCore::Quick::QQmlAspectEngine::sceneCreated(QObject *rootObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine12sceneCreatedEP7QObject(
    Qt3DCore::Quick::QQmlAspectEngine *self,
    QObject *rootObject) {
  self->sceneCreated(rootObject);
}

//  QQmlAspectEnginePrivate *Qt3DCore::Quick::QQmlAspectEngine::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::QQmlAspectEnginePrivate *ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine6d_funcEv(
    Qt3DCore::Quick::QQmlAspectEngine *self) {
  return self->d_func();
}

//  const QQmlAspectEnginePrivate
//      *Qt3DCore::Quick::QQmlAspectEngine::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::Quick::QQmlAspectEnginePrivate *ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine6d_funcEv(
    const Qt3DCore::Quick::QQmlAspectEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_Quick_QQmlAspectEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_Quick_QQmlAspectEngine(
    Qt3DCore::Quick::QQmlAspectEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_Quick_QQmlAspectEngine *>(self)->take(key, call);
}
