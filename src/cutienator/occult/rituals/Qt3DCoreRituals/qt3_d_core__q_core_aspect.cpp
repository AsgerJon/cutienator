//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qcoreaspect.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qcoreaspect.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <Qt3DCore/Qt3DCore>
#include <vector>

//  A Qt3DCore::QCoreAspect that Python can take functions over in. Every Qt3DCore::QCoreAspect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QCoreAspectCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QCoreAspectCall1)(const void *, int *);
typedef void (*CuteQt3DCore_QCoreAspectCall2)(const void *, int *);
typedef void (*CuteQt3DCore_QCoreAspectCall3)(const void *, int *);
typedef void (*CuteQt3DCore_QCoreAspectCall4)(const void *, int *);
typedef void (*CuteQt3DCore_QCoreAspectCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QCoreAspectCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QCoreAspectCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QCoreAspectCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QCoreAspectCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QCoreAspectCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QCoreAspectCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QCoreAspectCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QCoreAspect : public Qt3DCore::QCoreAspect {
public:
  using Qt3DCore::QCoreAspect::QCoreAspect;
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
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect9frameDoneEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv")) {
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

  //  void Qt3DCore::QCoreAspect::onRegistered()
  void onRegistered() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectCall0 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QCoreAspect::onRegistered();
  }

  //  void Qt3DCore::QCoreAspect::onUnregistered()
  void onUnregistered() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectCall1 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QCoreAspect::onUnregistered();
  }

  //  void Qt3DCore::QCoreAspect::onEngineStartup()
  void onEngineStartup() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectCall2 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QCoreAspect::onEngineStartup();
  }

  //  void Qt3DCore::QCoreAspect::frameDone()
  void frameDone() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectCall3 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QCoreAspect::frameDone();
  }

  //  void Qt3DCore::QAbstractAspect::onEngineShutdown()
  void onEngineShutdown() override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectCall4 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onEngineShutdown();
  }

  //  void Qt3DCore::QAbstractAspect::jobsDone()
  void jobsDone() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectCall5 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::jobsDone();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectCall6 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall6>(taken[6]);
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
      CuteQt3DCore_QCoreAspectCall7 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall7>(taken[7]);
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
      CuteQt3DCore_QCoreAspectCall8 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall8>(taken[8]);
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
      CuteQt3DCore_QCoreAspectCall9 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall9>(taken[9]);
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
      CuteQt3DCore_QCoreAspectCall10 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall10>(taken[10]);
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
      CuteQt3DCore_QCoreAspectCall11 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall11>(taken[11]);
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
      CuteQt3DCore_QCoreAspectCall12 call = reinterpret_cast<CuteQt3DCore_QCoreAspectCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QCoreAspect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore11QCoreAspect10metaObjectEv(
    const Qt3DCore::QCoreAspect *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QCoreAspect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore11QCoreAspect11qt_metacastEPKc(
    Qt3DCore::QCoreAspect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QCoreAspect::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore11QCoreAspect11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QCoreAspect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QCoreAspect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore11QCoreAspect2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QCoreAspect::tr(s, c, n));
}

//  Qt3DCore::QCoreAspect::QCoreAspect(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QCoreAspect *ritual_ZN8Qt3DCore11QCoreAspectC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DCore_QCoreAspect(parent);
}

//  Qt3DCore::QCoreAspect::~QCoreAspect()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore11QCoreAspectD1Ev(Qt3DCore::QCoreAspect *self) {
  delete self;
}

//  QAspectJobPtr Qt3DCore::QCoreAspect::calculateBoundingVolumeJob() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJobPtr *ritual_ZNK8Qt3DCore11QCoreAspect26calculateBoundingVolumeJobEv(
    const Qt3DCore::QCoreAspect *self) {
  return new Qt3DCore::QAspectJobPtr(self->calculateBoundingVolumeJob());
}

//  QCoreAspectPrivate *Qt3DCore::QCoreAspect::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QCoreAspectPrivate *ritual_ZN8Qt3DCore11QCoreAspect6d_funcEv(
    Qt3DCore::QCoreAspect *self) {
  return self->d_func();
}

//  const QCoreAspectPrivate *Qt3DCore::QCoreAspect::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QCoreAspectPrivate *ritual_ZNK8Qt3DCore11QCoreAspect6d_funcEv(
    const Qt3DCore::QCoreAspect *self) {
  return self->d_func();
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DCore::QCoreAspect::jobsToExecute(qint64 time)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN8Qt3DCore11QCoreAspect13jobsToExecuteEx(
    Qt3DCore::QCoreAspect *self,
    qint64 time) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->jobsToExecute(time));
}

//  QVariant Qt3DCore::QCoreAspect::executeCommand(const QStringList &args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore11QCoreAspect14executeCommandERK5QListI7QStringE(
    Qt3DCore::QCoreAspect *self,
    const QList<QString> *args) {
  return new QVariant(self->executeCommand(*args));
}

//  void Qt3DCore::QCoreAspect::onRegistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore11QCoreAspect12onRegisteredEv(
    Qt3DCore::QCoreAspect *self) {
  self->onRegistered();
}

//  void Qt3DCore::QCoreAspect::onUnregistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore11QCoreAspect14onUnregisteredEv(
    Qt3DCore::QCoreAspect *self) {
  self->onUnregistered();
}

//  void Qt3DCore::QCoreAspect::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore11QCoreAspect15onEngineStartupEv(
    Qt3DCore::QCoreAspect *self) {
  self->onEngineStartup();
}

//  void Qt3DCore::QCoreAspect::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore11QCoreAspect9frameDoneEv(
    Qt3DCore::QCoreAspect *self) {
  self->frameDone();
}

//  a Python function taken by a CuteQt3DCore_QCoreAspect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QCoreAspect(
    Qt3DCore::QCoreAspect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QCoreAspect *>(self)->take(key, call);
}

//  void Qt3DCore::QCoreAspect::onRegistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore11QCoreAspect12onRegisteredEv(
    Qt3DCore::QCoreAspect *self) {
  self->Qt3DCore::QCoreAspect::onRegistered();
}

//  void Qt3DCore::QCoreAspect::onUnregistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore11QCoreAspect14onUnregisteredEv(
    Qt3DCore::QCoreAspect *self) {
  self->Qt3DCore::QCoreAspect::onUnregistered();
}

//  void Qt3DCore::QCoreAspect::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore11QCoreAspect15onEngineStartupEv(
    Qt3DCore::QCoreAspect *self) {
  self->Qt3DCore::QCoreAspect::onEngineStartup();
}

//  void Qt3DCore::QCoreAspect::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore11QCoreAspect9frameDoneEv(
    Qt3DCore::QCoreAspect *self) {
  self->Qt3DCore::QCoreAspect::frameDone();
}

//  a Qt3DCore::QAspectJobPtr a ritual of Qt3DCore::QCoreAspect gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QCoreAspect__Qt3DCore_QAspectJobPtr(
    Qt3DCore::QAspectJobPtr *self) {
  delete self;
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of Qt3DCore::QCoreAspect
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QCoreAspect__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}
