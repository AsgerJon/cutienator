//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qanimationaspect.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qanimationaspect.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <vector>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DAnimation::QAnimationAspect that Python can take functions over in. Every Qt3DAnimation::QAnimationAspect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QAnimationAspectCall0)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectCall1)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectCall2)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectCall3)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectCall4)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QAnimationAspectCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QAnimationAspectCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAnimationAspectCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAnimationAspectCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAnimationAspectCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAnimationAspectCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAnimationAspectCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QAnimationAspect : public Qt3DAnimation::QAnimationAspect {
public:
  using Qt3DAnimation::QAnimationAspect::QAnimationAspect;
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
      CuteQt3DAnimation_QAnimationAspectCall0 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onRegistered();
  }

  //  void Qt3DCore::QAbstractAspect::onUnregistered()
  void onUnregistered() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectCall1 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onUnregistered();
  }

  //  void Qt3DCore::QAbstractAspect::onEngineStartup()
  void onEngineStartup() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectCall2 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onEngineStartup();
  }

  //  void Qt3DCore::QAbstractAspect::onEngineShutdown()
  void onEngineShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectCall3 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onEngineShutdown();
  }

  //  void Qt3DCore::QAbstractAspect::jobsDone()
  void jobsDone() override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectCall4 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspect::frameDone()
  void frameDone() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectCall5 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall5>(taken[5]);
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
      CuteQt3DAnimation_QAnimationAspectCall6 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall6>(taken[6]);
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
      CuteQt3DAnimation_QAnimationAspectCall7 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall7>(taken[7]);
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
      CuteQt3DAnimation_QAnimationAspectCall8 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall8>(taken[8]);
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
      CuteQt3DAnimation_QAnimationAspectCall9 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall9>(taken[9]);
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
      CuteQt3DAnimation_QAnimationAspectCall10 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall10>(taken[10]);
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
      CuteQt3DAnimation_QAnimationAspectCall11 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall11>(taken[11]);
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
      CuteQt3DAnimation_QAnimationAspectCall12 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QAnimationAspect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation16QAnimationAspect10metaObjectEv(
    const Qt3DAnimation::QAnimationAspect *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QAnimationAspect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation16QAnimationAspect11qt_metacastEPKc(
    Qt3DAnimation::QAnimationAspect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QAnimationAspect::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation16QAnimationAspect11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QAnimationAspect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QAnimationAspect::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation16QAnimationAspect2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAnimationAspect::tr(s, c, n));
}

//  Qt3DAnimation::QAnimationAspect::QAnimationAspect(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationAspect *ritual_ZN13Qt3DAnimation16QAnimationAspectC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DAnimation_QAnimationAspect(parent);
}

//  Qt3DAnimation::QAnimationAspect::~QAnimationAspect()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation16QAnimationAspectD1Ev(
    Qt3DAnimation::QAnimationAspect *self) {
  delete self;
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DAnimation::QAnimationAspect::jobsToExecute(qint64 time)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN13Qt3DAnimation16QAnimationAspect13jobsToExecuteEx(
    Qt3DAnimation::QAnimationAspect *self,
    qint64 time) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->jobsToExecute(time));
}

//  QAnimationAspectPrivate *Qt3DAnimation::QAnimationAspect::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationAspectPrivate *ritual_ZN13Qt3DAnimation16QAnimationAspect6d_funcEv(
    Qt3DAnimation::QAnimationAspect *self) {
  return self->d_func();
}

//  const QAnimationAspectPrivate *Qt3DAnimation::QAnimationAspect::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationAspectPrivate *ritual_ZNK13Qt3DAnimation16QAnimationAspect6d_funcEv(
    const Qt3DAnimation::QAnimationAspect *self) {
  return self->d_func();
}

//  Qt3DAnimation::QAnimationAspect::QAnimationAspect(QAnimationAspectPrivate
//      &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationAspect *ritual_ZN13Qt3DAnimation16QAnimationAspectC1ERNS_23QAnimationAspectPrivateEP7QObject(
    Qt3DAnimation::QAnimationAspectPrivate *dd,
    QObject *parent) {
  return new CuteQt3DAnimation_QAnimationAspect(*dd, parent);
}

//  a Python function taken by a CuteQt3DAnimation_QAnimationAspect, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAnimationAspect(
    Qt3DAnimation::QAnimationAspect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAnimationAspect *>(self)->take(key, call);
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DAnimation::QAnimationAspect gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QAnimationAspect__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}
