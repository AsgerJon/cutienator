//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectcleanuphandler.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectcleanuphandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QObjectCleanupHandler that Python can take functions over in. Every QObjectCleanupHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectCleanupHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectCleanupHandlerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectCleanupHandlerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectCleanupHandlerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectCleanupHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectCleanupHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectCleanupHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQObjectCleanupHandler : public QObjectCleanupHandler {
public:
  using QObjectCleanupHandler::QObjectCleanupHandler;
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
      CuteQObjectCleanupHandlerCall0 call = reinterpret_cast<CuteQObjectCleanupHandlerCall0>(taken[0]);
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
      CuteQObjectCleanupHandlerCall1 call = reinterpret_cast<CuteQObjectCleanupHandlerCall1>(taken[1]);
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
      CuteQObjectCleanupHandlerCall2 call = reinterpret_cast<CuteQObjectCleanupHandlerCall2>(taken[2]);
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
      CuteQObjectCleanupHandlerCall3 call = reinterpret_cast<CuteQObjectCleanupHandlerCall3>(taken[3]);
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
      CuteQObjectCleanupHandlerCall4 call = reinterpret_cast<CuteQObjectCleanupHandlerCall4>(taken[4]);
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
      CuteQObjectCleanupHandlerCall5 call = reinterpret_cast<CuteQObjectCleanupHandlerCall5>(taken[5]);
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
      CuteQObjectCleanupHandlerCall6 call = reinterpret_cast<CuteQObjectCleanupHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QObjectCleanupHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QObjectCleanupHandler10metaObjectEv(
    const QObjectCleanupHandler *self) {
  return self->metaObject();
}

//  QString QObjectCleanupHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QObjectCleanupHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QObjectCleanupHandler::tr(s, c, n));
}

//  QObjectCleanupHandler::QObjectCleanupHandler()
extern "C" Q_DECL_EXPORT
QObjectCleanupHandler *ritual_ZN21QObjectCleanupHandlerC1Ev() {
  return new CuteQObjectCleanupHandler();
}

//  QObjectCleanupHandler::~QObjectCleanupHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QObjectCleanupHandlerD1Ev(QObjectCleanupHandler *self) {
  delete self;
}

//  QObject *QObjectCleanupHandler::add(QObject *object)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN21QObjectCleanupHandler3addEP7QObject(
    QObjectCleanupHandler *self,
    QObject *object) {
  return self->add(object);
}

//  void QObjectCleanupHandler::remove(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QObjectCleanupHandler6removeEP7QObject(
    QObjectCleanupHandler *self,
    QObject *object) {
  self->remove(object);
}

//  bool QObjectCleanupHandler::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QObjectCleanupHandler7isEmptyEv(
    const QObjectCleanupHandler *self) {
  return self->isEmpty();
}

//  void QObjectCleanupHandler::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QObjectCleanupHandler5clearEv(QObjectCleanupHandler *self) {
  self->clear();
}

//  void QObjectCleanupHandler::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QObjectCleanupHandler15objectDestroyedEP7QObject(
    QObjectCleanupHandler *self,
    QObject *a0) {
  self->objectDestroyed(a0);
}

//  a Python function taken by a CuteQObjectCleanupHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QObjectCleanupHandler(
    QObjectCleanupHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQObjectCleanupHandler *>(self)->take(key, call);
}
