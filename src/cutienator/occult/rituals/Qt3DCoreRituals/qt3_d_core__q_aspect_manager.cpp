//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qaspectmanager_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qaspectmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QAspectManager that Python can take functions over in. Every Qt3DCore::QAspectManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DCore_QAspectManagerCall0)(const void *, const Qt3DCore::QNodeId *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAspectManagerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAspectManagerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectManagerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectManagerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectManagerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectManagerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QAspectManager : public Qt3DCore::QAspectManager {
public:
  using Qt3DCore::QAspectManager::QAspectManager;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore28QAbstractFrontEndNodeManager10lookupNodeENS_7QNodeIdE")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QNode *Qt3DCore::QAspectManager::lookupNode(QNodeId id) const
  Qt3DCore::QNode *lookupNode(Qt3DCore::QNodeId id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall0 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall0>(taken[0]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QNode *>(given);
    }
    return Qt3DCore::QAspectManager::lookupNode(id);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall1 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall2 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall3 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall4 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall5 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall6 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_QAspectManagerCall7 call = reinterpret_cast<CuteQt3DCore_QAspectManagerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QAspectManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore14QAspectManager10metaObjectEv(
    const Qt3DCore::QAspectManager *self) {
  return self->metaObject();
}

//  QString Qt3DCore::QAspectManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore14QAspectManager2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QAspectManager::tr(s, c, n));
}

//  QAspectEngine *Qt3DCore::QAspectManager::engine() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEngine *ritual_ZNK8Qt3DCore14QAspectManager6engineEv(
    const Qt3DCore::QAspectManager *self) {
  return self->engine();
}

//  QScheduler *Qt3DCore::QAspectManager::scheduler() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QScheduler *ritual_ZNK8Qt3DCore14QAspectManager9schedulerEv(
    const Qt3DCore::QAspectManager *self) {
  return self->scheduler();
}

//  int Qt3DCore::QAspectManager::jobsInLastFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore14QAspectManager15jobsInLastFrameEv(
    const Qt3DCore::QAspectManager *self) {
  return self->jobsInLastFrame();
}

//  Qt3DCore::QAspectManager as the Qt3DCore::QAbstractFrontEndNodeManager it
//      is built on
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFrontEndNodeManager *ritual_cast_Qt3DCore_QAspectManager_Qt3DCore_QAbstractFrontEndNodeManager(
    Qt3DCore::QAspectManager *self) {
  return static_cast<Qt3DCore::QAbstractFrontEndNodeManager *>(self);
}

//  a Python function taken by a CuteQt3DCore_QAspectManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAspectManager(
    Qt3DCore::QAspectManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAspectManager *>(self)->take(key, call);
}

//  QNode *Qt3DCore::QAspectManager::lookupNode(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_own_ZNK8Qt3DCore14QAspectManager10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QAspectManager *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DCore::QAspectManager::lookupNode(*id);
}
