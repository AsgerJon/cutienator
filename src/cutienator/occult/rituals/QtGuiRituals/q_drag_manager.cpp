//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdnd_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdnd_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDragManager that Python can take functions over in. Every QDragManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDragManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDragManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDragManager : public QDragManager {
public:
  using QDragManager::QDragManager;
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
      CuteQDragManagerCall0 call = reinterpret_cast<CuteQDragManagerCall0>(taken[0]);
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
      CuteQDragManagerCall1 call = reinterpret_cast<CuteQDragManagerCall1>(taken[1]);
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
      CuteQDragManagerCall2 call = reinterpret_cast<CuteQDragManagerCall2>(taken[2]);
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
      CuteQDragManagerCall3 call = reinterpret_cast<CuteQDragManagerCall3>(taken[3]);
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
      CuteQDragManagerCall4 call = reinterpret_cast<CuteQDragManagerCall4>(taken[4]);
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
      CuteQDragManagerCall5 call = reinterpret_cast<CuteQDragManagerCall5>(taken[5]);
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
      CuteQDragManagerCall6 call = reinterpret_cast<CuteQDragManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDragManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QDragManager10metaObjectEv(
    const QDragManager *self) {
  return self->metaObject();
}

//  QString QDragManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QDragManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDragManager::tr(s, c, n));
}

//  QDragManager::QDragManager()
extern "C" Q_DECL_EXPORT
QDragManager *ritual_ZN12QDragManagerC1Ev() {
  return new CuteQDragManager();
}

//  QDragManager::~QDragManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDragManagerD1Ev(QDragManager *self) {
  delete self;
}

//  QDragManager *QDragManager::self()
extern "C" Q_DECL_EXPORT
QDragManager *ritual_ZN12QDragManager4selfEv() {
  return QDragManager::self();
}

//  Qt::DropAction QDragManager::drag(QDrag *a0)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN12QDragManager4dragEP5QDrag(
    QDragManager *self,
    QDrag *a0) {
  return self->drag(a0);
}

//  void QDragManager::setCurrentTarget(QObject *target, bool dropped)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDragManager16setCurrentTargetEP7QObjectb(
    QDragManager *self,
    QObject *target,
    bool dropped) {
  self->setCurrentTarget(target, dropped);
}

//  QObject *QDragManager::currentTarget() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK12QDragManager13currentTargetEv(
    const QDragManager *self) {
  return self->currentTarget();
}

//  QObject *QDragManager::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK12QDragManager6sourceEv(const QDragManager *self) {
  return self->source();
}

//  a Python function taken by a CuteQDragManager, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDragManager(
    QDragManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDragManager *>(self)->take(key, call);
}

#endif  // QT_CONFIG(draganddrop)
