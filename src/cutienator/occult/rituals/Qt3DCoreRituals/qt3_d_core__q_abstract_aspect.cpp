//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qabstractaspect.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qabstractaspect.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DCore::QAbstractAspect that Python can take functions over in. Every Qt3DCore::QAbstractAspect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QAbstractAspectCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectCall1)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectCall2)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectCall3)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectCall4)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAbstractAspectCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAbstractAspectCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractAspectCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractAspectCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractAspectCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractAspectCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractAspectCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QAbstractAspect : public Qt3DCore::QAbstractAspect {
public:
  using Qt3DCore::QAbstractAspect::QAbstractAspect;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect12onRegisteredEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect14onUnregisteredEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect15onEngineStartupEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect9frameDoneEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Qt3DCore::QAbstractAspect::onRegistered()
  void onRegistered() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onRegistered();
  }

  //  void Qt3DCore::QAbstractAspect::onUnregistered()
  void onUnregistered() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall1 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onUnregistered();
  }

  //  void Qt3DCore::QAbstractAspect::onEngineStartup()
  void onEngineStartup() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall2 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onEngineStartup();
  }

  //  void Qt3DCore::QAbstractAspect::onEngineShutdown()
  void onEngineShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall3 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onEngineShutdown();
  }

  //  void Qt3DCore::QAbstractAspect::jobsDone()
  void jobsDone() override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall4 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspect::frameDone()
  void frameDone() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall5 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::frameDone();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall6 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall7 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall8 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall9 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall10 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall11 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectCall12 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QAbstractAspect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore15QAbstractAspect10metaObjectEv(
    const Qt3DCore::QAbstractAspect *self) {
  return self->metaObject();
}

//  QString Qt3DCore::QAbstractAspect::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore15QAbstractAspect2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QAbstractAspect::tr(s, c, n));
}

//  QStringList Qt3DCore::QAbstractAspect::dependencies() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8Qt3DCore15QAbstractAspect12dependenciesEv(
    const Qt3DCore::QAbstractAspect *self) {
  return new QList<QString>(self->dependencies());
}

//  QVariant Qt3DCore::QAbstractAspect::executeCommand(const QStringList
//      &args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore15QAbstractAspect14executeCommandERK5QListI7QStringE(
    Qt3DCore::QAbstractAspect *self,
    const QList<QString> *args) {
  return new QVariant(self->executeCommand(*args));
}

//  void Qt3DCore::QAbstractAspect::onRegistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QAbstractAspect12onRegisteredEv(
    Qt3DCore::QAbstractAspect *self) {
  self->onRegistered();
}

//  void Qt3DCore::QAbstractAspect::onUnregistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QAbstractAspect14onUnregisteredEv(
    Qt3DCore::QAbstractAspect *self) {
  self->onUnregistered();
}

//  void Qt3DCore::QAbstractAspect::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QAbstractAspect15onEngineStartupEv(
    Qt3DCore::QAbstractAspect *self) {
  self->onEngineStartup();
}

//  void Qt3DCore::QAbstractAspect::onEngineShutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv(
    Qt3DCore::QAbstractAspect *self) {
  self->onEngineShutdown();
}

//  void Qt3DCore::QAbstractAspect::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv(
    Qt3DCore::QAbstractAspect *self) {
  self->jobsDone();
}

//  void Qt3DCore::QAbstractAspect::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QAbstractAspect9frameDoneEv(
    Qt3DCore::QAbstractAspect *self) {
  self->frameDone();
}

//  QAbstractAspectPrivate *Qt3DCore::QAbstractAspect::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspectPrivate *ritual_ZN8Qt3DCore15QAbstractAspect6d_funcEv(
    Qt3DCore::QAbstractAspect *self) {
  return self->d_func();
}

//  const QAbstractAspectPrivate *Qt3DCore::QAbstractAspect::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAbstractAspectPrivate *ritual_ZNK8Qt3DCore15QAbstractAspect6d_funcEv(
    const Qt3DCore::QAbstractAspect *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QAbstractAspect, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractAspect(
    Qt3DCore::QAbstractAspect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractAspect *>(self)->take(key, call);
}

//  void Qt3DCore::QAbstractAspect::onRegistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore15QAbstractAspect12onRegisteredEv(
    Qt3DCore::QAbstractAspect *self) {
  self->Qt3DCore::QAbstractAspect::onRegistered();
}

//  void Qt3DCore::QAbstractAspect::onUnregistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore15QAbstractAspect14onUnregisteredEv(
    Qt3DCore::QAbstractAspect *self) {
  self->Qt3DCore::QAbstractAspect::onUnregistered();
}

//  void Qt3DCore::QAbstractAspect::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore15QAbstractAspect15onEngineStartupEv(
    Qt3DCore::QAbstractAspect *self) {
  self->Qt3DCore::QAbstractAspect::onEngineStartup();
}

//  void Qt3DCore::QAbstractAspect::onEngineShutdown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv(
    Qt3DCore::QAbstractAspect *self) {
  self->Qt3DCore::QAbstractAspect::onEngineShutdown();
}

//  void Qt3DCore::QAbstractAspect::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv(
    Qt3DCore::QAbstractAspect *self) {
  self->Qt3DCore::QAbstractAspect::jobsDone();
}

//  void Qt3DCore::QAbstractAspect::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore15QAbstractAspect9frameDoneEv(
    Qt3DCore::QAbstractAspect *self) {
  self->Qt3DCore::QAbstractAspect::frameDone();
}
