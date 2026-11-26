//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickDeliveryAgent that Python can take functions over in. Every QQuickDeliveryAgent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDeliveryAgentCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDeliveryAgentCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDeliveryAgentCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDeliveryAgentCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDeliveryAgentCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDeliveryAgentCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDeliveryAgentCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDeliveryAgent : public QQuickDeliveryAgent {
public:
  using QQuickDeliveryAgent::QQuickDeliveryAgent;
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
  //  bool QQuickDeliveryAgent::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDeliveryAgentCall0 call = reinterpret_cast<CuteQQuickDeliveryAgentCall0>(taken[0]);
      bool given = call(this, ev, &handled);
      if (handled) return given;
    }
    return QQuickDeliveryAgent::event(ev);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDeliveryAgentCall1 call = reinterpret_cast<CuteQQuickDeliveryAgentCall1>(taken[1]);
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
      CuteQQuickDeliveryAgentCall2 call = reinterpret_cast<CuteQQuickDeliveryAgentCall2>(taken[2]);
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
      CuteQQuickDeliveryAgentCall3 call = reinterpret_cast<CuteQQuickDeliveryAgentCall3>(taken[3]);
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
      CuteQQuickDeliveryAgentCall4 call = reinterpret_cast<CuteQQuickDeliveryAgentCall4>(taken[4]);
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
      CuteQQuickDeliveryAgentCall5 call = reinterpret_cast<CuteQQuickDeliveryAgentCall5>(taken[5]);
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
      CuteQQuickDeliveryAgentCall6 call = reinterpret_cast<CuteQQuickDeliveryAgentCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDeliveryAgent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickDeliveryAgent10metaObjectEv(
    const QQuickDeliveryAgent *self) {
  return self->metaObject();
}

//  void *QQuickDeliveryAgent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickDeliveryAgent11qt_metacastEPKc(
    QQuickDeliveryAgent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDeliveryAgent::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickDeliveryAgent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDeliveryAgent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDeliveryAgent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickDeliveryAgent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDeliveryAgent::tr(s, c, n));
}

//  QQuickDeliveryAgentPrivate *QQuickDeliveryAgent::d_func()
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgentPrivate *ritual_ZN19QQuickDeliveryAgent6d_funcEv(
    QQuickDeliveryAgent *self) {
  return self->d_func();
}

//  const QQuickDeliveryAgentPrivate *QQuickDeliveryAgent::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDeliveryAgentPrivate *ritual_ZNK19QQuickDeliveryAgent6d_funcEv(
    const QQuickDeliveryAgent *self) {
  return self->d_func();
}

//  QQuickDeliveryAgent::QQuickDeliveryAgent(QQuickItem *rootItem)
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgent *ritual_ZN19QQuickDeliveryAgentC1EP10QQuickItem(
    QQuickItem *rootItem) {
  return new CuteQQuickDeliveryAgent(rootItem);
}

//  QQuickDeliveryAgent::~QQuickDeliveryAgent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDeliveryAgentD1Ev(QQuickDeliveryAgent *self) {
  delete self;
}

//  QQuickItem *QQuickDeliveryAgent::rootItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK19QQuickDeliveryAgent8rootItemEv(
    const QQuickDeliveryAgent *self) {
  return self->rootItem();
}

//  Transform *QQuickDeliveryAgent::sceneTransform() const
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgent::Transform *ritual_ZNK19QQuickDeliveryAgent14sceneTransformEv(
    const QQuickDeliveryAgent *self) {
  return self->sceneTransform();
}

//  void QQuickDeliveryAgent::setSceneTransform(Transform *transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDeliveryAgent17setSceneTransformEPNS_9TransformE(
    QQuickDeliveryAgent *self,
    QQuickDeliveryAgent::Transform *transform) {
  self->setSceneTransform(transform);
}

//  bool QQuickDeliveryAgent::event(QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDeliveryAgent5eventEP6QEvent(
    QQuickDeliveryAgent *self,
    QEvent *ev) {
  return self->event(ev);
}

//  a Python function taken by a CuteQQuickDeliveryAgent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDeliveryAgent(
    QQuickDeliveryAgent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDeliveryAgent *>(self)->take(key, call);
}

//  bool QQuickDeliveryAgent::event(QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickDeliveryAgent5eventEP6QEvent(
    QQuickDeliveryAgent *self,
    QEvent *ev) {
  return self->QQuickDeliveryAgent::event(ev);
}
