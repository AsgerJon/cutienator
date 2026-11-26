//  Written by hand on 2026-11-25 from
//  Qt3DCore/6.12.0/Qt3DCore/private/qeventfilterservice_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/6.12.0/Qt3DCore/private/qeventfilterservice_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QEventFilterService that Python can take functions over in.
//  Every Qt3DCore::QEventFilterService Python makes is one. Each function
//  below asks the Python function handed over for it, and runs Qt's own
//  without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QEventFilterServiceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QEventFilterServiceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEventFilterServiceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEventFilterServiceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEventFilterServiceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEventFilterServiceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEventFilterServiceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QEventFilterService : public Qt3DCore::QEventFilterService {
public:
  using Qt3DCore::QEventFilterService::QEventFilterService;
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
      CuteQt3DCore_QEventFilterServiceCall0 call = reinterpret_cast<CuteQt3DCore_QEventFilterServiceCall0>(taken[0]);
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
      CuteQt3DCore_QEventFilterServiceCall1 call = reinterpret_cast<CuteQt3DCore_QEventFilterServiceCall1>(taken[1]);
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
      CuteQt3DCore_QEventFilterServiceCall2 call = reinterpret_cast<CuteQt3DCore_QEventFilterServiceCall2>(taken[2]);
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
      CuteQt3DCore_QEventFilterServiceCall3 call = reinterpret_cast<CuteQt3DCore_QEventFilterServiceCall3>(taken[3]);
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
      CuteQt3DCore_QEventFilterServiceCall4 call = reinterpret_cast<CuteQt3DCore_QEventFilterServiceCall4>(taken[4]);
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
      CuteQt3DCore_QEventFilterServiceCall5 call = reinterpret_cast<CuteQt3DCore_QEventFilterServiceCall5>(taken[5]);
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
      CuteQt3DCore_QEventFilterServiceCall6 call = reinterpret_cast<CuteQt3DCore_QEventFilterServiceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QEventFilterService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore19QEventFilterService10metaObjectEv(
    const Qt3DCore::QEventFilterService *self) {
  return self->metaObject();
}

//  QString Qt3DCore::QEventFilterService::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore19QEventFilterService2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QEventFilterService::tr(s, c, n));
}

//  QEventFilterService::QEventFilterService()
extern "C" Q_DECL_EXPORT
Qt3DCore::QEventFilterService *ritual_ZN8Qt3DCore19QEventFilterServiceC1Ev() {
  return new CuteQt3DCore_QEventFilterService();
}

//  QEventFilterService::~QEventFilterService()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QEventFilterServiceD1Ev(
    Qt3DCore::QEventFilterService *self) {
  delete self;
}

//  void QEventFilterService::initialize(QObject *eventSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QEventFilterService10initializeEP7QObject(
    Qt3DCore::QEventFilterService *self,
    QObject *eventSource) {
  self->initialize(eventSource);
}

//  void QEventFilterService::shutdown(QObject *eventSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QEventFilterService8shutdownEP7QObject(
    Qt3DCore::QEventFilterService *self,
    QObject *eventSource) {
  self->shutdown(eventSource);
}

//  void QEventFilterService::registerEventFilter(QObject *eventFilter,
//      int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QEventFilterService19registerEventFilterEP7QObjecti(
    Qt3DCore::QEventFilterService *self,
    QObject *eventFilter,
    int priority) {
  self->registerEventFilter(eventFilter, priority);
}

//  void QEventFilterService::unregisterEventFilter(QObject *eventFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QEventFilterService21unregisterEventFilterEP7QObject(
    Qt3DCore::QEventFilterService *self,
    QObject *eventFilter) {
  self->unregisterEventFilter(eventFilter);
}

//  QEventFilterServicePrivate *Qt3DCore::QEventFilterService::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QEventFilterServicePrivate *ritual_ZN8Qt3DCore19QEventFilterService6d_funcEv(
    Qt3DCore::QEventFilterService *self) {
  return self->d_func();
}

//  const QEventFilterServicePrivate *Qt3DCore::QEventFilterService::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QEventFilterServicePrivate *ritual_ZNK8Qt3DCore19QEventFilterService6d_funcEv(
    const Qt3DCore::QEventFilterService *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QEventFilterService, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QEventFilterService(
    Qt3DCore::QEventFilterService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QEventFilterService *>(self)->take(key, call);
}
