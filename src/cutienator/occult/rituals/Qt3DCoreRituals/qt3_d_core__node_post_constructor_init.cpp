//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qnode_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/QComponent>
#include <Qt3DCore/qaspectengine.h>
#include <Qt3DCore/qentity.h>
#include <QtCore/QChildEvent>
#include <QtCore/QEvent>
#include <QtCore/QMetaObject>
#include <QtCore/QMetaProperty>
#include <QtCore/QThread>
#include <Qt3DCore/private/corelogging_p.h>
#include <Qt3DCore/private/qdestructionidandtypecollector_p.h>
#include <Qt3DCore/private/qnodevisitor_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/private/qaspectengine_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <QtCore/private/qmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/core/nodes/qnode.cpp, line 875, as _ZN8Qt3DCore23NodePostConstructorInit10removeNodeEPNS_5QNodeE
namespace Qt3DCore {
inline void NodePostConstructorInit::removeNode(QNode *node)
{
    Q_ASSERT(node);
    m_nodesToConstruct.removeAll(QNodePrivate::get(node));
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/nodes/qnode.cpp, line 850, as _ZN8Qt3DCore23NodePostConstructorInit7addNodeEPNS_5QNodeE
namespace Qt3DCore {
inline void NodePostConstructorInit::addNode(QNode *node)
{
    Q_ASSERT(node);
    QNode *nextNode = node;
    while (nextNode != nullptr && !m_nodesToConstruct.contains(QNodePrivate::get(nextNode)))
        nextNode = nextNode->parentNode();

    // An ancestor in the m_nodesToConstruct may already have been created (m_hasBackendNode)
    // at this point (e.g. when a QComponent calls _q_ensureBackendNodeCreated()),
    // that's why we also queue a creation request in this case.
    if (!nextNode || QNodePrivate::get(nextNode)->m_hasBackendNode) {
        m_nodesToConstruct.append(QNodePrivate::get(node));
        if (!m_requestedProcessing){
            QMetaObject::invokeMethod(this, "processNodes", Qt::QueuedConnection);
            m_requestedProcessing = true;
        }
    }
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  A Qt3DCore::NodePostConstructorInit that Python can take functions over in. Every Qt3DCore::NodePostConstructorInit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_NodePostConstructorInitCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_NodePostConstructorInitCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_NodePostConstructorInit : public Qt3DCore::NodePostConstructorInit {
public:
  using Qt3DCore::NodePostConstructorInit::NodePostConstructorInit;
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
      CuteQt3DCore_NodePostConstructorInitCall0 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall0>(taken[0]);
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
      CuteQt3DCore_NodePostConstructorInitCall1 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall1>(taken[1]);
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
      CuteQt3DCore_NodePostConstructorInitCall2 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall2>(taken[2]);
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
      CuteQt3DCore_NodePostConstructorInitCall3 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall3>(taken[3]);
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
      CuteQt3DCore_NodePostConstructorInitCall4 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall4>(taken[4]);
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
      CuteQt3DCore_NodePostConstructorInitCall5 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall5>(taken[5]);
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
      CuteQt3DCore_NodePostConstructorInitCall6 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::NodePostConstructorInit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore23NodePostConstructorInit10metaObjectEv(
    const Qt3DCore::NodePostConstructorInit *self) {
  return self->metaObject();
}

//  void *Qt3DCore::NodePostConstructorInit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore23NodePostConstructorInit11qt_metacastEPKc(
    Qt3DCore::NodePostConstructorInit *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::NodePostConstructorInit::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore23NodePostConstructorInit11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::NodePostConstructorInit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DCore::NodePostConstructorInit::~NodePostConstructorInit()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInitD1Ev(
    Qt3DCore::NodePostConstructorInit *self) {
  delete self;
}

//  void Qt3DCore::NodePostConstructorInit::removeNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInit10removeNodeEPNS_5QNodeE(
    Qt3DCore::NodePostConstructorInit *self,
    Qt3DCore::QNode *node) {
  self->removeNode(node);
}

//  void Qt3DCore::NodePostConstructorInit::addNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInit7addNodeEPNS_5QNodeE(
    Qt3DCore::NodePostConstructorInit *self,
    Qt3DCore::QNode *node) {
  self->addNode(node);
}

//  void Qt3DCore::NodePostConstructorInit::processNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInit12processNodesEv(
    Qt3DCore::NodePostConstructorInit *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::NodePostConstructorInit")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "processNodes()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "processNodes()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQt3DCore_NodePostConstructorInit, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_NodePostConstructorInit(
    Qt3DCore::NodePostConstructorInit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_NodePostConstructorInit *>(self)->take(key, call);
}
