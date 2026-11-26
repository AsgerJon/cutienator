//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qinputaspect.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qinputaspect.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <vector>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DInput::QInputAspect that Python can take functions over in. Every Qt3DInput::QInputAspect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QInputAspectCall0)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectCall1)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectCall2)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectCall3)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectCall4)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QInputAspectCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QInputAspectCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputAspectCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputAspectCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputAspectCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputAspectCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputAspectCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QInputAspect : public Qt3DInput::QInputAspect {
public:
  using Qt3DInput::QInputAspect::QInputAspect;
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
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv")) {
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

  //  void Qt3DInput::QInputAspect::onRegistered()
  void onRegistered() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectCall0 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::QInputAspect::onRegistered();
  }

  //  void Qt3DInput::QInputAspect::onUnregistered()
  void onUnregistered() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectCall1 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::QInputAspect::onUnregistered();
  }

  //  void Qt3DInput::QInputAspect::onEngineStartup()
  void onEngineStartup() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectCall2 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::QInputAspect::onEngineStartup();
  }

  //  void Qt3DInput::QInputAspect::jobsDone()
  void jobsDone() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectCall3 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::QInputAspect::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspect::onEngineShutdown()
  void onEngineShutdown() override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectCall4 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onEngineShutdown();
  }

  //  void Qt3DCore::QAbstractAspect::frameDone()
  void frameDone() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectCall5 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall5>(taken[5]);
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
      CuteQt3DInput_QInputAspectCall6 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall6>(taken[6]);
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
      CuteQt3DInput_QInputAspectCall7 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall7>(taken[7]);
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
      CuteQt3DInput_QInputAspectCall8 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall8>(taken[8]);
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
      CuteQt3DInput_QInputAspectCall9 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall9>(taken[9]);
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
      CuteQt3DInput_QInputAspectCall10 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall10>(taken[10]);
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
      CuteQt3DInput_QInputAspectCall11 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall11>(taken[11]);
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
      CuteQt3DInput_QInputAspectCall12 call = reinterpret_cast<CuteQt3DInput_QInputAspectCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QInputAspect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput12QInputAspect10metaObjectEv(
    const Qt3DInput::QInputAspect *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QInputAspect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput12QInputAspect11qt_metacastEPKc(
    Qt3DInput::QInputAspect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QInputAspect::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput12QInputAspect11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QInputAspect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QInputAspect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput12QInputAspect2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QInputAspect::tr(s, c, n));
}

//  Qt3DInput::QInputAspect::QInputAspect(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputAspect *ritual_ZN9Qt3DInput12QInputAspectC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DInput_QInputAspect(parent);
}

//  Qt3DInput::QInputAspect::~QInputAspect()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QInputAspectD1Ev(Qt3DInput::QInputAspect *self) {
  delete self;
}

//  QAbstractPhysicalDevice
//      *Qt3DInput::QInputAspect::createPhysicalDevice(const QString &name)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZN9Qt3DInput12QInputAspect20createPhysicalDeviceERK7QString(
    Qt3DInput::QInputAspect *self,
    const QString *name) {
  return self->createPhysicalDevice(*name);
}

//  QStringList Qt3DInput::QInputAspect::availablePhysicalDevices() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput12QInputAspect24availablePhysicalDevicesEv(
    const Qt3DInput::QInputAspect *self) {
  return new QList<QString>(self->availablePhysicalDevices());
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DInput::QInputAspect::jobsToExecute(qint64 time)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN9Qt3DInput12QInputAspect13jobsToExecuteEx(
    Qt3DInput::QInputAspect *self,
    qint64 time) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->jobsToExecute(time));
}

//  void Qt3DInput::QInputAspect::onRegistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QInputAspect12onRegisteredEv(
    Qt3DInput::QInputAspect *self) {
  self->onRegistered();
}

//  void Qt3DInput::QInputAspect::onUnregistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QInputAspect14onUnregisteredEv(
    Qt3DInput::QInputAspect *self) {
  self->onUnregistered();
}

//  void Qt3DInput::QInputAspect::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QInputAspect15onEngineStartupEv(
    Qt3DInput::QInputAspect *self) {
  self->onEngineStartup();
}

//  void Qt3DInput::QInputAspect::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QInputAspect8jobsDoneEv(
    Qt3DInput::QInputAspect *self) {
  self->jobsDone();
}

//  QInputAspectPrivate *Qt3DInput::QInputAspect::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputAspectPrivate *ritual_ZN9Qt3DInput12QInputAspect6d_funcEv(
    Qt3DInput::QInputAspect *self) {
  return self->d_func();
}

//  const QInputAspectPrivate *Qt3DInput::QInputAspect::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QInputAspectPrivate *ritual_ZNK9Qt3DInput12QInputAspect6d_funcEv(
    const Qt3DInput::QInputAspect *self) {
  return self->d_func();
}

//  Qt3DInput::QInputAspect::QInputAspect(QInputAspectPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputAspect *ritual_ZN9Qt3DInput12QInputAspectC1ERNS_19QInputAspectPrivateEP7QObject(
    Qt3DInput::QInputAspectPrivate *dd,
    QObject *parent) {
  return new CuteQt3DInput_QInputAspect(*dd, parent);
}

//  a Python function taken by a CuteQt3DInput_QInputAspect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QInputAspect(
    Qt3DInput::QInputAspect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QInputAspect *>(self)->take(key, call);
}

//  void Qt3DInput::QInputAspect::onRegistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput12QInputAspect12onRegisteredEv(
    Qt3DInput::QInputAspect *self) {
  self->Qt3DInput::QInputAspect::onRegistered();
}

//  void Qt3DInput::QInputAspect::onUnregistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput12QInputAspect14onUnregisteredEv(
    Qt3DInput::QInputAspect *self) {
  self->Qt3DInput::QInputAspect::onUnregistered();
}

//  void Qt3DInput::QInputAspect::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput12QInputAspect15onEngineStartupEv(
    Qt3DInput::QInputAspect *self) {
  self->Qt3DInput::QInputAspect::onEngineStartup();
}

//  void Qt3DInput::QInputAspect::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput12QInputAspect8jobsDoneEv(
    Qt3DInput::QInputAspect *self) {
  self->Qt3DInput::QInputAspect::jobsDone();
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DInput::QInputAspect gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QInputAspect__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}
