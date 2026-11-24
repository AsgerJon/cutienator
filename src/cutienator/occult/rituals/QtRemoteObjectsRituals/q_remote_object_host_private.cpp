//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QRemoteObjectHostPrivate that Python can take functions over in. Every QRemoteObjectHostPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQRemoteObjectHostPrivateCall0)(const void *, const QMetaObject *, QRemoteObjectReplica *, const QString *, int *);
class CuteQRemoteObjectHostPrivate : public QRemoteObjectHostPrivate {
public:
  using QRemoteObjectHostPrivate::QRemoteObjectHostPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QRemoteObjectNodePrivate16handleNewAcquireEPK11QMetaObjectP20QRemoteObjectReplicaRK7QString")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QReplicaImplementationInterface
  //      *QRemoteObjectHostBasePrivate::handleNewAcquire(const QMetaObject
  //      *meta, QRemoteObjectReplica *instance, const QString &name)
  QReplicaImplementationInterface *handleNewAcquire(
      const QMetaObject *meta,
      QRemoteObjectReplica *instance,
      const QString &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectHostPrivateCall0 call = reinterpret_cast<CuteQRemoteObjectHostPrivateCall0>(taken[0]);
      void * given = call(this, meta, instance, &name, &handled);
      if (handled) return static_cast<QReplicaImplementationInterface *>(given);
    }
    return QRemoteObjectHostBasePrivate::handleNewAcquire(meta, instance, name);
  }
};

//  QRemoteObjectHost *QRemoteObjectHostPrivate::q_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectHost *ritual_ZN24QRemoteObjectHostPrivate6q_funcEv(
    QRemoteObjectHostPrivate *self) {
  return self->q_func();
}

//  const QRemoteObjectHost *QRemoteObjectHostPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectHost *ritual_ZNK24QRemoteObjectHostPrivate6q_funcEv(
    const QRemoteObjectHostPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQRemoteObjectHostPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectHostPrivate(
    QRemoteObjectHostPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectHostPrivate *>(self)->take(key, call);
}
