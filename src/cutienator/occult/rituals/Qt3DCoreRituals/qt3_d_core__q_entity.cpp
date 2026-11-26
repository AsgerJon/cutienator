//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qentity.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 3. Kept as it is when the
//  generator runs again.
#include <Qt3DCore/qentity.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DCore/Qt3DCore>
#include <Qt3DCore/qcomponent.h>
#include <Qt3DCore/qtransform.h>
#include <QtCore/qlist.h>

//  A Qt3DCore::QEntity that Python can take functions over in. Every Qt3DCore::QEntity
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QEntityCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QEntityCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEntityCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEntityCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEntityCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEntityCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QEntityCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QEntity : public Qt3DCore::QEntity {
public:
  using Qt3DCore::QEntity::QEntity;
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
      CuteQt3DCore_QEntityCall0 call = reinterpret_cast<CuteQt3DCore_QEntityCall0>(taken[0]);
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
      CuteQt3DCore_QEntityCall1 call = reinterpret_cast<CuteQt3DCore_QEntityCall1>(taken[1]);
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
      CuteQt3DCore_QEntityCall2 call = reinterpret_cast<CuteQt3DCore_QEntityCall2>(taken[2]);
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
      CuteQt3DCore_QEntityCall3 call = reinterpret_cast<CuteQt3DCore_QEntityCall3>(taken[3]);
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
      CuteQt3DCore_QEntityCall4 call = reinterpret_cast<CuteQt3DCore_QEntityCall4>(taken[4]);
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
      CuteQt3DCore_QEntityCall5 call = reinterpret_cast<CuteQt3DCore_QEntityCall5>(taken[5]);
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
      CuteQt3DCore_QEntityCall6 call = reinterpret_cast<CuteQt3DCore_QEntityCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QEntity::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore7QEntity10metaObjectEv(
    const Qt3DCore::QEntity *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QEntity::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore7QEntity11qt_metacastEPKc(
    Qt3DCore::QEntity *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QEntity::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore7QEntity11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QEntity *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QEntity::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore7QEntity2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QEntity::tr(s, c, n));
}

//  Qt3DCore::QEntity::QEntity(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZN8Qt3DCore7QEntityC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QEntity(parent);
}

//  Qt3DCore::QEntity::~QEntity()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore7QEntityD1Ev(Qt3DCore::QEntity *self) {
  delete self;
}

//  QComponentVector Qt3DCore::QEntity::components() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QComponentVector *ritual_ZNK8Qt3DCore7QEntity10componentsEv(
    const Qt3DCore::QEntity *self) {
  return new Qt3DCore::QComponentVector(self->components());
}

//  void Qt3DCore::QEntity::addComponent(QComponent *comp)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore7QEntity12addComponentEPNS_10QComponentE(
    Qt3DCore::QEntity *self,
    Qt3DCore::QComponent *comp) {
  self->addComponent(comp);
}

//  void Qt3DCore::QEntity::removeComponent(QComponent *comp)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore7QEntity15removeComponentEPNS_10QComponentE(
    Qt3DCore::QEntity *self,
    Qt3DCore::QComponent *comp) {
  self->removeComponent(comp);
}

//  QEntity *Qt3DCore::QEntity::parentEntity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK8Qt3DCore7QEntity12parentEntityEv(
    const Qt3DCore::QEntity *self) {
  return self->parentEntity();
}

//  Qt3DCore::QEntity::QEntity(QEntityPrivate &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZN8Qt3DCore7QEntityC1ERNS_14QEntityPrivateEPNS_5QNodeE(
    Qt3DCore::QEntityPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QEntity(*dd, parent);
}

//  void Qt3DCore::QEntity::onParentChanged(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore7QEntity15onParentChangedEP7QObject(
    Qt3DCore::QEntity *self,
    QObject *a0) {
  self->onParentChanged(a0);
}

//  QEntityPrivate *Qt3DCore::QEntity::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntityPrivate *ritual_ZN8Qt3DCore7QEntity6d_funcEv(
    Qt3DCore::QEntity *self) {
  return self->d_func();
}

//  const QEntityPrivate *Qt3DCore::QEntity::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QEntityPrivate *ritual_ZNK8Qt3DCore7QEntity6d_funcEv(
    const Qt3DCore::QEntity *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QEntity, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QEntity(
    Qt3DCore::QEntity *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QEntity *>(self)->take(key, call);
}

//  a Qt3DCore::QComponentVector a ritual of Qt3DCore::QEntity gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QEntity__Qt3DCore_QComponentVector(
    Qt3DCore::QComponentVector *self) {
  delete self;
}

//  QList<QObject *> Qt3DCore::QEntity::componentsOfType<QObject>() const
extern "C" Q_DECL_EXPORT
QList<QObject *> * ritual_ZNK8Qt3DCore7QEntity16componentsOfTypeI7QObjectEE5QListIPT_Ev(
    const Qt3DCore::QEntity *self) {
  return new QList<QObject *>(self->componentsOfType<QObject>());
}

//  QList<Qt3DCore::QComponent *>
//      Qt3DCore::QEntity::componentsOfType<Qt3DCore::QComponent>() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QComponent *> * ritual_ZNK8Qt3DCore7QEntity16componentsOfTypeINS_10QComponentEEE5QListIPT_Ev(
    const Qt3DCore::QEntity *self) {
  return new QList<Qt3DCore::QComponent *>(self->componentsOfType<Qt3DCore::QComponent>());
}

//  QList<Qt3DCore::QTransform *>
//      Qt3DCore::QEntity::componentsOfType<Qt3DCore::QTransform>() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QTransform *> * ritual_ZNK8Qt3DCore7QEntity16componentsOfTypeINS_10QTransformEEE5QListIPT_Ev(
    const Qt3DCore::QEntity *self) {
  return new QList<Qt3DCore::QTransform *>(self->componentsOfType<Qt3DCore::QTransform>());
}
