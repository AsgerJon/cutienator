//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlconnections_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlMeta/QtQmlMeta>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlconnections_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQmlConnections may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlConnections : QQmlConnections {
  using QQmlConnections::classBegin;
  using QQmlConnections::componentComplete;
};

//  A QQmlConnections that Python can take functions over in. Every QQmlConnections
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlConnectionsCall0)(const void *, int *);
typedef void (*CuteQQmlConnectionsCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlConnectionsCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlConnectionsCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlConnectionsCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlConnectionsCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlConnectionsCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlConnectionsCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlConnectionsCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlConnections : public QQmlConnections {
public:
  using QQmlConnections::QQmlConnections;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQmlConnections::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlConnectionsCall0 call = reinterpret_cast<CuteQQmlConnectionsCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlConnections::classBegin();
  }

  //  void QQmlConnections::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlConnectionsCall1 call = reinterpret_cast<CuteQQmlConnectionsCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlConnections::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlConnectionsCall2 call = reinterpret_cast<CuteQQmlConnectionsCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlConnectionsCall3 call = reinterpret_cast<CuteQQmlConnectionsCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlConnectionsCall4 call = reinterpret_cast<CuteQQmlConnectionsCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlConnectionsCall5 call = reinterpret_cast<CuteQQmlConnectionsCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlConnectionsCall6 call = reinterpret_cast<CuteQQmlConnectionsCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlConnectionsCall7 call = reinterpret_cast<CuteQQmlConnectionsCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlConnectionsCall8 call = reinterpret_cast<CuteQQmlConnectionsCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlConnections::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlConnections10metaObjectEv(
    const QQmlConnections *self) {
  return self->metaObject();
}

//  void *QQmlConnections::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQmlConnections11qt_metacastEPKc(
    QQmlConnections *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlConnections::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlConnections11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlConnections *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlConnections::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlConnections2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlConnections::tr(s, c, n));
}

//  QQmlConnectionsPrivate *QQmlConnections::d_func()
extern "C" Q_DECL_EXPORT
QQmlConnectionsPrivate *ritual_ZN15QQmlConnections6d_funcEv(
    QQmlConnections *self) {
  return self->d_func();
}

//  const QQmlConnectionsPrivate *QQmlConnections::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlConnectionsPrivate *ritual_ZNK15QQmlConnections6d_funcEv(
    const QQmlConnections *self) {
  return self->d_func();
}

//  QQmlConnections::QQmlConnections(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlConnections *ritual_ZN15QQmlConnectionsC1EP7QObject(QObject *parent) {
  return new CuteQQmlConnections(parent);
}

//  QQmlConnections::~QQmlConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnectionsD1Ev(QQmlConnections *self) {
  delete self;
}

//  QObject *QQmlConnections::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QQmlConnections6targetEv(const QQmlConnections *self) {
  return self->target();
}

//  void QQmlConnections::setTarget(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections9setTargetEP7QObject(
    QQmlConnections *self,
    QObject *a0) {
  self->setTarget(a0);
}

//  bool QQmlConnections::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlConnections9isEnabledEv(const QQmlConnections *self) {
  return self->isEnabled();
}

//  void QQmlConnections::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections10setEnabledEb(
    QQmlConnections *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QQmlConnections::ignoreUnknownSignals() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlConnections20ignoreUnknownSignalsEv(
    const QQmlConnections *self) {
  return self->ignoreUnknownSignals();
}

//  void QQmlConnections::setIgnoreUnknownSignals(bool ignore)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections23setIgnoreUnknownSignalsEb(
    QQmlConnections *self,
    bool ignore) {
  self->setIgnoreUnknownSignals(ignore);
}

//  void QQmlConnections::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections10classBeginEv(QQmlConnections *self) {
  self->classBegin();
}

//  void QQmlConnections::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections17componentCompleteEv(QQmlConnections *self) {
  self->componentComplete();
}

//  void QQmlConnections::targetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections13targetChangedEv(QQmlConnections *self) {
  self->targetChanged();
}

//  void QQmlConnections::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections14enabledChangedEv(QQmlConnections *self) {
  self->enabledChanged();
}

//  void QQmlConnections::connectSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections14connectSignalsEv(QQmlConnections *self) {
  self->connectSignals();
}

//  void QQmlConnections::connectSignalsToMethods()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections23connectSignalsToMethodsEv(
    QQmlConnections *self) {
  self->connectSignalsToMethods();
}

//  void QQmlConnections::connectSignalsToBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlConnections24connectSignalsToBindingsEv(
    QQmlConnections *self) {
  self->connectSignalsToBindings();
}

//  QQmlConnections as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlConnections_QQmlParserStatus(
    QQmlConnections *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlConnections, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlConnections(
    QQmlConnections *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlConnections *>(self)->take(key, call);
}

//  void QQmlConnections::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQmlConnections10classBeginEv(QQmlConnections *self) {
  static_cast<OwnQQmlConnections *>(self)->OwnQQmlConnections::classBegin();
}

//  void QQmlConnections::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQmlConnections17componentCompleteEv(
    QQmlConnections *self) {
  static_cast<OwnQQmlConnections *>(self)->OwnQQmlConnections::componentComplete();
}
