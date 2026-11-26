//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qnode.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qnode.h>
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DCore::QNode that Python can take functions over in. Every Qt3DCore::QNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QNodeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QNodeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QNodeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QNodeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QNodeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QNodeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QNodeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QNode : public Qt3DCore::QNode {
public:
  using Qt3DCore::QNode::QNode;
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
      CuteQt3DCore_QNodeCall0 call = reinterpret_cast<CuteQt3DCore_QNodeCall0>(taken[0]);
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
      CuteQt3DCore_QNodeCall1 call = reinterpret_cast<CuteQt3DCore_QNodeCall1>(taken[1]);
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
      CuteQt3DCore_QNodeCall2 call = reinterpret_cast<CuteQt3DCore_QNodeCall2>(taken[2]);
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
      CuteQt3DCore_QNodeCall3 call = reinterpret_cast<CuteQt3DCore_QNodeCall3>(taken[3]);
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
      CuteQt3DCore_QNodeCall4 call = reinterpret_cast<CuteQt3DCore_QNodeCall4>(taken[4]);
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
      CuteQt3DCore_QNodeCall5 call = reinterpret_cast<CuteQt3DCore_QNodeCall5>(taken[5]);
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
      CuteQt3DCore_QNodeCall6 call = reinterpret_cast<CuteQt3DCore_QNodeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5QNode10metaObjectEv(
    const Qt3DCore::QNode *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5QNode11qt_metacastEPKc(
    Qt3DCore::QNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QNode::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5QNode11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5QNode2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QNode::tr(s, c, n));
}

//  Qt3DCore::QNode::QNode(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN8Qt3DCore5QNodeC1EPS0_(Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QNode(parent);
}

//  Qt3DCore::QNode::~QNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5QNodeD1Ev(Qt3DCore::QNode *self) {
  delete self;
}

//  QNodeId Qt3DCore::QNode::id() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK8Qt3DCore5QNode2idEv(
    const Qt3DCore::QNode *self) {
  return new Qt3DCore::QNodeId(self->id());
}

//  QNode *Qt3DCore::QNode::parentNode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore5QNode10parentNodeEv(
    const Qt3DCore::QNode *self) {
  return self->parentNode();
}

//  bool Qt3DCore::QNode::notificationsBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5QNode20notificationsBlockedEv(
    const Qt3DCore::QNode *self) {
  return self->notificationsBlocked();
}

//  bool Qt3DCore::QNode::blockNotifications(bool block)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore5QNode18blockNotificationsEb(
    Qt3DCore::QNode *self,
    bool block) {
  return self->blockNotifications(block);
}

//  QNodeVector Qt3DCore::QNode::childNodes() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeVector *ritual_ZNK8Qt3DCore5QNode10childNodesEv(
    const Qt3DCore::QNode *self) {
  return new Qt3DCore::QNodeVector(self->childNodes());
}

//  bool Qt3DCore::QNode::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5QNode9isEnabledEv(const Qt3DCore::QNode *self) {
  return self->isEnabled();
}

//  void Qt3DCore::QNode::setParent(QNode *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5QNode9setParentEPS0_(
    Qt3DCore::QNode *self,
    Qt3DCore::QNode *parent) {
  self->setParent(parent);
}

//  void Qt3DCore::QNode::setEnabled(bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5QNode10setEnabledEb(
    Qt3DCore::QNode *self,
    bool isEnabled) {
  self->setEnabled(isEnabled);
}

//  void Qt3DCore::QNode::parentChanged(QObject *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5QNode13parentChangedEP7QObject(
    Qt3DCore::QNode *self,
    QObject *parent) {
  self->parentChanged(parent);
}

//  void Qt3DCore::QNode::enabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5QNode14enabledChangedEb(
    Qt3DCore::QNode *self,
    bool enabled) {
  self->enabledChanged(enabled);
}

//  void Qt3DCore::QNode::nodeDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5QNode13nodeDestroyedEv(Qt3DCore::QNode *self) {
  self->nodeDestroyed();
}

//  Qt3DCore::QNode::QNode(QNodePrivate &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN8Qt3DCore5QNodeC1ERNS_12QNodePrivateEPS0_(
    Qt3DCore::QNodePrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QNode(*dd, parent);
}

//  QNodePrivate *Qt3DCore::QNode::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodePrivate *ritual_ZN8Qt3DCore5QNode6d_funcEv(
    Qt3DCore::QNode *self) {
  return self->d_func();
}

//  const QNodePrivate *Qt3DCore::QNode::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QNodePrivate *ritual_ZNK8Qt3DCore5QNode6d_funcEv(
    const Qt3DCore::QNode *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QNode(
    Qt3DCore::QNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QNode *>(self)->take(key, call);
}

//  a Qt3DCore::QNodeVector a ritual of Qt3DCore::QNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QNode__Qt3DCore_QNodeVector(
    Qt3DCore::QNodeVector *self) {
  delete self;
}
