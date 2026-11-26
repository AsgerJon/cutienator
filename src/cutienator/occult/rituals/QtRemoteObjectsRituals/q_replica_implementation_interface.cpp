//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QReplicaImplementationInterface that Python can take functions over in. Every QReplicaImplementationInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQReplicaImplementationInterfaceCall0)(const void *, int, int *);
typedef void (*CuteQReplicaImplementationInterfaceCall1)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQReplicaImplementationInterfaceCall2)(const void *, int *);
typedef int (*CuteQReplicaImplementationInterfaceCall3)(const void *, int *);
typedef bool (*CuteQReplicaImplementationInterfaceCall4)(const void *, int, int *);
typedef void * (*CuteQReplicaImplementationInterfaceCall5)(const void *, int *);
class CuteQReplicaImplementationInterface : public QReplicaImplementationInterface {
public:
  using QReplicaImplementationInterface::QReplicaImplementationInterface;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface11getPropertyEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QReplicaImplementationInterface11setPropertyEiRK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface13isInitializedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface5stateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QReplicaImplementationInterface13waitForSourceEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface4nodeEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  const QVariant QReplicaImplementationInterface::getProperty(int i)
  //      const
  const QVariant getProperty(int i) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQReplicaImplementationInterfaceCall0 call = reinterpret_cast<CuteQReplicaImplementationInterfaceCall0>(taken[0]);
      const QVariant * given = call(this, i, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QReplicaImplementationInterface::setProperty(int i, const
  //      QVariant &a1)
  void setProperty(int i, const QVariant &a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQReplicaImplementationInterfaceCall1 call = reinterpret_cast<CuteQReplicaImplementationInterfaceCall1>(taken[1]);
      call(this, i, &a1, &handled);
      if (handled) return;
    }
  }

  //  bool QReplicaImplementationInterface::isInitialized() const
  bool isInitialized() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQReplicaImplementationInterfaceCall2 call = reinterpret_cast<CuteQReplicaImplementationInterfaceCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRemoteObjectReplica::State QReplicaImplementationInterface::state()
  //      const
  QRemoteObjectReplica::State state() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQReplicaImplementationInterfaceCall3 call = reinterpret_cast<CuteQReplicaImplementationInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRemoteObjectReplica::State>(given);
    }
    return {};
  }

  //  bool QReplicaImplementationInterface::waitForSource(int a0)
  bool waitForSource(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQReplicaImplementationInterfaceCall4 call = reinterpret_cast<CuteQReplicaImplementationInterfaceCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRemoteObjectNode *QReplicaImplementationInterface::node() const
  QRemoteObjectNode *node() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQReplicaImplementationInterfaceCall5 call = reinterpret_cast<CuteQReplicaImplementationInterfaceCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRemoteObjectNode *>(given);
    }
    return {};
  }
};

//  QReplicaImplementationInterface::~QReplicaImplementationInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QReplicaImplementationInterfaceD1Ev(
    QReplicaImplementationInterface *self) {
  delete self;
}

//  const QVariant QReplicaImplementationInterface::getProperty(int i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK31QReplicaImplementationInterface11getPropertyEi(
    const QReplicaImplementationInterface *self,
    int i) {
  return new QVariant(self->getProperty(i));
}

//  void QReplicaImplementationInterface::setProperties(QVariantList &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QReplicaImplementationInterface13setPropertiesEO5QListI8QVariantE(
    QReplicaImplementationInterface *self,
    QVariantList *a0) {
  self->setProperties(std::move(*a0));
}

//  void QReplicaImplementationInterface::setProperty(int i, const QVariant
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QReplicaImplementationInterface11setPropertyEiRK8QVariant(
    QReplicaImplementationInterface *self,
    int i,
    const QVariant *a1) {
  self->setProperty(i, *a1);
}

//  bool QReplicaImplementationInterface::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QReplicaImplementationInterface13isInitializedEv(
    const QReplicaImplementationInterface *self) {
  return self->isInitialized();
}

//  QRemoteObjectReplica::State QReplicaImplementationInterface::state()
//      const
extern "C" Q_DECL_EXPORT
QRemoteObjectReplica::State ritual_ZNK31QReplicaImplementationInterface5stateEv(
    const QReplicaImplementationInterface *self) {
  return self->state();
}

//  bool QReplicaImplementationInterface::waitForSource(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QReplicaImplementationInterface13waitForSourceEi(
    QReplicaImplementationInterface *self,
    int a0) {
  return self->waitForSource(a0);
}

//  QRemoteObjectNode *QReplicaImplementationInterface::node() const
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_ZNK31QReplicaImplementationInterface4nodeEv(
    const QReplicaImplementationInterface *self) {
  return self->node();
}

//  void QReplicaImplementationInterface::_q_send(QMetaObject::Call call, int
//      index, const QVariantList &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QReplicaImplementationInterface7_q_sendEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QReplicaImplementationInterface *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  self->_q_send(call, index, *args);
}

//  QRemoteObjectPendingCall
//      QReplicaImplementationInterface::_q_sendWithReply(QMetaObject::Call
//      call, int index, const QVariantList &args)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN31QReplicaImplementationInterface16_q_sendWithReplyEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QReplicaImplementationInterface *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  return new QRemoteObjectPendingCall(
      self->_q_sendWithReply(
          call,
          index,
          *args));
}

//  a Python function taken by a CuteQReplicaImplementationInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QReplicaImplementationInterface(
    QReplicaImplementationInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQReplicaImplementationInterface *>(self)->take(key, call);
}
