//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qchangearbiter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qchangearbiter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DCore::QChangeArbiter that Python can take functions over in. Every Qt3DCore::QChangeArbiter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QChangeArbiterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QChangeArbiterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QChangeArbiterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QChangeArbiterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QChangeArbiterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QChangeArbiterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QChangeArbiterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QChangeArbiter : public Qt3DCore::QChangeArbiter {
public:
  using Qt3DCore::QChangeArbiter::QChangeArbiter;
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
      CuteQt3DCore_QChangeArbiterCall0 call = reinterpret_cast<CuteQt3DCore_QChangeArbiterCall0>(taken[0]);
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
      CuteQt3DCore_QChangeArbiterCall1 call = reinterpret_cast<CuteQt3DCore_QChangeArbiterCall1>(taken[1]);
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
      CuteQt3DCore_QChangeArbiterCall2 call = reinterpret_cast<CuteQt3DCore_QChangeArbiterCall2>(taken[2]);
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
      CuteQt3DCore_QChangeArbiterCall3 call = reinterpret_cast<CuteQt3DCore_QChangeArbiterCall3>(taken[3]);
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
      CuteQt3DCore_QChangeArbiterCall4 call = reinterpret_cast<CuteQt3DCore_QChangeArbiterCall4>(taken[4]);
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
      CuteQt3DCore_QChangeArbiterCall5 call = reinterpret_cast<CuteQt3DCore_QChangeArbiterCall5>(taken[5]);
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
      CuteQt3DCore_QChangeArbiterCall6 call = reinterpret_cast<CuteQt3DCore_QChangeArbiterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QChangeArbiter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore14QChangeArbiter10metaObjectEv(
    const Qt3DCore::QChangeArbiter *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QChangeArbiter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore14QChangeArbiter11qt_metacastEPKc(
    Qt3DCore::QChangeArbiter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QChangeArbiter::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore14QChangeArbiter11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QChangeArbiter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QChangeArbiter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore14QChangeArbiter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QChangeArbiter::tr(s, c, n));
}

//  Qt3DCore::QChangeArbiter::QChangeArbiter(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QChangeArbiter *ritual_ZN8Qt3DCore14QChangeArbiterC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DCore_QChangeArbiter(parent);
}

//  Qt3DCore::QChangeArbiter::~QChangeArbiter()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QChangeArbiterD1Ev(Qt3DCore::QChangeArbiter *self) {
  delete self;
}

//  void Qt3DCore::QChangeArbiter::addDirtyFrontEndNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QChangeArbiter20addDirtyFrontEndNodeEPNS_5QNodeE(
    Qt3DCore::QChangeArbiter *self,
    Qt3DCore::QNode *node) {
  self->addDirtyFrontEndNode(node);
}

//  void Qt3DCore::QChangeArbiter::addDirtyEntityComponentNodes(QEntity
//      *entity, QComponent *component,
//      ComponentRelationshipChange::RelationShip change)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QChangeArbiter28addDirtyEntityComponentNodesEPNS_7QEntityEPNS_10QComponentENS_27ComponentRelationshipChange12RelationShipE(
    Qt3DCore::QChangeArbiter *self,
    Qt3DCore::QEntity *entity,
    Qt3DCore::QComponent *component,
    Qt3DCore::ComponentRelationshipChange::RelationShip change) {
  self->addDirtyEntityComponentNodes(entity, component, change);
}

//  void Qt3DCore::QChangeArbiter::removeDirtyFrontEndNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QChangeArbiter23removeDirtyFrontEndNodeEPNS_5QNodeE(
    Qt3DCore::QChangeArbiter *self,
    Qt3DCore::QNode *node) {
  self->removeDirtyFrontEndNode(node);
}

//  QList<QNode *> Qt3DCore::QChangeArbiter::takeDirtyFrontEndNodes()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNode *> *ritual_ZN8Qt3DCore14QChangeArbiter22takeDirtyFrontEndNodesEv(
    Qt3DCore::QChangeArbiter *self) {
  return new QList<Qt3DCore::QNode *>(self->takeDirtyFrontEndNodes());
}

//  QList<ComponentRelationshipChange>
//      Qt3DCore::QChangeArbiter::takeDirtyEntityComponentNodes()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::ComponentRelationshipChange> *ritual_ZN8Qt3DCore14QChangeArbiter29takeDirtyEntityComponentNodesEv(
    Qt3DCore::QChangeArbiter *self) {
  return new QList<Qt3DCore::ComponentRelationshipChange>(
      self->takeDirtyEntityComponentNodes());
}

//  void Qt3DCore::QChangeArbiter::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QChangeArbiter8setSceneEPNS_6QSceneE(
    Qt3DCore::QChangeArbiter *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  QScene *Qt3DCore::QChangeArbiter::scene() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QScene *ritual_ZNK8Qt3DCore14QChangeArbiter5sceneEv(
    const Qt3DCore::QChangeArbiter *self) {
  return self->scene();
}

//  void Qt3DCore::QChangeArbiter::receivedChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QChangeArbiter14receivedChangeEv(
    Qt3DCore::QChangeArbiter *self) {
  self->receivedChange();
}

//  a Python function taken by a CuteQt3DCore_QChangeArbiter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QChangeArbiter(
    Qt3DCore::QChangeArbiter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QChangeArbiter *>(self)->take(key, call);
}

//  a QList<Qt3DCore::QNode *> a ritual of Qt3DCore::QChangeArbiter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QChangeArbiter__QList_Qt3DCore_QNode(
    QList<Qt3DCore::QNode *> *self) {
  delete self;
}

//  a QList<Qt3DCore::ComponentRelationshipChange> a ritual of
//      Qt3DCore::QChangeArbiter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QChangeArbiter__QList_Qt3DCore_ComponentRelationshipChange(
    QList<Qt3DCore::ComponentRelationshipChange> *self) {
  delete self;
}
