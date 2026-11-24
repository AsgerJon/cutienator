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

//  A QRemoteObjectHostBasePrivate that Python can take functions over in. Every QRemoteObjectHostBasePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQRemoteObjectHostBasePrivateCall0)(const void *, const QMetaObject *, QRemoteObjectReplica *, const QString *, int *);
class CuteQRemoteObjectHostBasePrivate : public QRemoteObjectHostBasePrivate {
public:
  using QRemoteObjectHostBasePrivate::QRemoteObjectHostBasePrivate;
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
      CuteQRemoteObjectHostBasePrivateCall0 call = reinterpret_cast<CuteQRemoteObjectHostBasePrivateCall0>(taken[0]);
      void * given = call(this, meta, instance, &name, &handled);
      if (handled) return static_cast<QReplicaImplementationInterface *>(given);
    }
    return QRemoteObjectHostBasePrivate::handleNewAcquire(meta, instance, name);
  }
};

//  QRemoteObjectHostBase *QRemoteObjectHostBasePrivate::q_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectHostBase *ritual_ZN28QRemoteObjectHostBasePrivate6q_funcEv(
    QRemoteObjectHostBasePrivate *self) {
  return self->q_func();
}

//  const QRemoteObjectHostBase *QRemoteObjectHostBasePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectHostBase *ritual_ZNK28QRemoteObjectHostBasePrivate6q_funcEv(
    const QRemoteObjectHostBasePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQRemoteObjectHostBasePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectHostBasePrivate(
    QRemoteObjectHostBasePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectHostBasePrivate *>(self)->take(key, call);
}
