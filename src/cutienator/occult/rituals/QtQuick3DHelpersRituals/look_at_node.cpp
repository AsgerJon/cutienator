//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/lookatnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/lookatnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A LookAtNode that Python can take functions over in. Every LookAtNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteLookAtNodeCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLookAtNodeCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLookAtNodeCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteLookAtNodeCall3)(const void *, int *);
typedef void * (*CuteLookAtNodeCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteLookAtNodeCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteLookAtNodeCall6)(const void *, int *);
typedef void (*CuteLookAtNodeCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLookAtNodeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLookAtNodeCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLookAtNodeCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLookAtNodeCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLookAtNodeCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLookAtNode : public LookAtNode {
public:
  using LookAtNode::LookAtNode;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[0]) {
      int handled = 0;
      CuteLookAtNodeCall0 call = reinterpret_cast<CuteLookAtNodeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[1]) {
      int handled = 0;
      CuteLookAtNodeCall1 call = reinterpret_cast<CuteLookAtNodeCall1>(taken[1]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteLookAtNodeCall2 call = reinterpret_cast<CuteLookAtNodeCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteLookAtNodeCall3 call = reinterpret_cast<CuteLookAtNodeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteLookAtNodeCall4 call = reinterpret_cast<CuteLookAtNodeCall4>(taken[4]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteLookAtNodeCall5 call = reinterpret_cast<CuteLookAtNodeCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteLookAtNodeCall6 call = reinterpret_cast<CuteLookAtNodeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteLookAtNodeCall7 call = reinterpret_cast<CuteLookAtNodeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteLookAtNodeCall8 call = reinterpret_cast<CuteLookAtNodeCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteLookAtNodeCall9 call = reinterpret_cast<CuteLookAtNodeCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteLookAtNodeCall10 call = reinterpret_cast<CuteLookAtNodeCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteLookAtNodeCall11 call = reinterpret_cast<CuteLookAtNodeCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteLookAtNodeCall12 call = reinterpret_cast<CuteLookAtNodeCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LookAtNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10LookAtNode10metaObjectEv(
    const LookAtNode *self) {
  return self->metaObject();
}

//  void *LookAtNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10LookAtNode11qt_metacastEPKc(
    LookAtNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LookAtNode::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10LookAtNode11qt_metacallEN11QMetaObject4CallEiPPv(
    LookAtNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString LookAtNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10LookAtNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LookAtNode::tr(s, c, n));
}

//  LookAtNode::LookAtNode()
extern "C" Q_DECL_EXPORT
LookAtNode *ritual_ZN10LookAtNodeC1Ev() {
  return new CuteLookAtNode();
}

//  LookAtNode::~LookAtNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10LookAtNodeD1Ev(LookAtNode *self) {
  delete self;
}

//  QQuick3DNode *LookAtNode::target() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK10LookAtNode6targetEv(const LookAtNode *self) {
  return self->target();
}

//  void LookAtNode::setTarget(QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10LookAtNode9setTargetEP12QQuick3DNode(
    LookAtNode *self,
    QQuick3DNode *node) {
  self->setTarget(node);
}

//  void LookAtNode::targetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10LookAtNode13targetChangedEv(LookAtNode *self) {
  self->targetChanged();
}

//  void LookAtNode::updateLookAt()
extern "C" Q_DECL_EXPORT
void ritual_ZN10LookAtNode12updateLookAtEv(LookAtNode *self) {
  self->updateLookAt();
}

//  a Python function taken by a CuteLookAtNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LookAtNode(LookAtNode *self, const char *key, void *call) {
  return static_cast<CuteLookAtNode *>(self)->take(key, call);
}
