//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qnearfieldmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qnearfieldmanager.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNearFieldManager that Python can take functions over in. Every QNearFieldManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNearFieldManager : public QNearFieldManager {
public:
  using QNearFieldManager::QNearFieldManager;
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
      CuteQNearFieldManagerCall0 call = reinterpret_cast<CuteQNearFieldManagerCall0>(taken[0]);
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
      CuteQNearFieldManagerCall1 call = reinterpret_cast<CuteQNearFieldManagerCall1>(taken[1]);
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
      CuteQNearFieldManagerCall2 call = reinterpret_cast<CuteQNearFieldManagerCall2>(taken[2]);
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
      CuteQNearFieldManagerCall3 call = reinterpret_cast<CuteQNearFieldManagerCall3>(taken[3]);
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
      CuteQNearFieldManagerCall4 call = reinterpret_cast<CuteQNearFieldManagerCall4>(taken[4]);
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
      CuteQNearFieldManagerCall5 call = reinterpret_cast<CuteQNearFieldManagerCall5>(taken[5]);
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
      CuteQNearFieldManagerCall6 call = reinterpret_cast<CuteQNearFieldManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNearFieldManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QNearFieldManager10metaObjectEv(
    const QNearFieldManager *self) {
  return self->metaObject();
}

//  void *QNearFieldManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QNearFieldManager11qt_metacastEPKc(
    QNearFieldManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNearFieldManager::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QNearFieldManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QNearFieldManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNearFieldManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QNearFieldManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNearFieldManager::tr(s, c, n));
}

//  QNearFieldManagerPrivate *QNearFieldManager::d_func()
extern "C" Q_DECL_EXPORT
QNearFieldManagerPrivate *ritual_ZN17QNearFieldManager6d_funcEv(
    QNearFieldManager *self) {
  return self->d_func();
}

//  const QNearFieldManagerPrivate *QNearFieldManager::d_func() const
extern "C" Q_DECL_EXPORT
const QNearFieldManagerPrivate *ritual_ZNK17QNearFieldManager6d_funcEv(
    const QNearFieldManager *self) {
  return self->d_func();
}

//  QNearFieldManager::QNearFieldManager(QObject *parent)
extern "C" Q_DECL_EXPORT
QNearFieldManager *ritual_ZN17QNearFieldManagerC1EP7QObject(
    QObject *parent) {
  return new CuteQNearFieldManager(parent);
}

//  QNearFieldManager::QNearFieldManager(QNearFieldManagerPrivate *backend,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QNearFieldManager *ritual_ZN17QNearFieldManagerC1EP24QNearFieldManagerPrivateP7QObject(
    QNearFieldManagerPrivate *backend,
    QObject *parent) {
  return new CuteQNearFieldManager(backend, parent);
}

//  QNearFieldManager::~QNearFieldManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNearFieldManagerD1Ev(QNearFieldManager *self) {
  delete self;
}

//  bool QNearFieldManager::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QNearFieldManager9isEnabledEv(
    const QNearFieldManager *self) {
  return self->isEnabled();
}

//  bool QNearFieldManager::isSupported(QNearFieldTarget::AccessMethod
//      accessMethod) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QNearFieldManager11isSupportedEN16QNearFieldTarget12AccessMethodE(
    const QNearFieldManager *self,
    QNearFieldTarget::AccessMethod accessMethod) {
  return self->isSupported(accessMethod);
}

//  bool
//      QNearFieldManager::startTargetDetection(QNearFieldTarget::AccessMetho
//      d accessMethod)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNearFieldManager20startTargetDetectionEN16QNearFieldTarget12AccessMethodE(
    QNearFieldManager *self,
    QNearFieldTarget::AccessMethod accessMethod) {
  return self->startTargetDetection(accessMethod);
}

//  void QNearFieldManager::stopTargetDetection(const QString &errorMessage)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNearFieldManager19stopTargetDetectionERK7QString(
    QNearFieldManager *self,
    const QString *errorMessage) {
  self->stopTargetDetection(*errorMessage);
}

//  void QNearFieldManager::setUserInformation(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNearFieldManager18setUserInformationERK7QString(
    QNearFieldManager *self,
    const QString *message) {
  self->setUserInformation(*message);
}

//  void
//      QNearFieldManager::adapterStateChanged(QNearFieldManager::AdapterStat
//      e state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNearFieldManager19adapterStateChangedENS_12AdapterStateE(
    QNearFieldManager *self,
    QNearFieldManager::AdapterState state) {
  self->adapterStateChanged(state);
}

//  void QNearFieldManager::targetDetectionStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNearFieldManager22targetDetectionStoppedEv(
    QNearFieldManager *self) {
  self->targetDetectionStopped();
}

//  void QNearFieldManager::targetDetected(QNearFieldTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNearFieldManager14targetDetectedEP16QNearFieldTarget(
    QNearFieldManager *self,
    QNearFieldTarget *target) {
  self->targetDetected(target);
}

//  void QNearFieldManager::targetLost(QNearFieldTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNearFieldManager10targetLostEP16QNearFieldTarget(
    QNearFieldManager *self,
    QNearFieldTarget *target) {
  self->targetLost(target);
}

//  a Python function taken by a CuteQNearFieldManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNearFieldManager(
    QNearFieldManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNearFieldManager *>(self)->take(key, call);
}
