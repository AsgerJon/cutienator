//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DPhysi
//  cs/6.12.0/QtQuick3DPhysics/private/qabstractphysicsnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qabstractphysicsnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QAbstractPhysicsNode that Python can take functions over in. Every QAbstractPhysicsNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAbstractPhysicsNodeCall0)(const void *, int *);
typedef void (*CuteQAbstractPhysicsNodeCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractPhysicsNodeCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractPhysicsNodeCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractPhysicsNodeCall4)(const void *, int *);
typedef void * (*CuteQAbstractPhysicsNodeCall5)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQAbstractPhysicsNodeCall6)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQAbstractPhysicsNodeCall7)(const void *, int *);
typedef void (*CuteQAbstractPhysicsNodeCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractPhysicsNodeCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractPhysicsNodeCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractPhysicsNodeCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractPhysicsNodeCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractPhysicsNodeCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractPhysicsNode : public QAbstractPhysicsNode {
public:
  using QAbstractPhysicsNode::QAbstractPhysicsNode;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractPhysicsNode18createPhysXBackendEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractPhysXNode *QAbstractPhysicsNode::createPhysXBackend()
  QAbstractPhysXNode *createPhysXBackend() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall0 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractPhysXNode *>(given);
    }
    return {};
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall1 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall2 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall3 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall4 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall5 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall6 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall6>(taken[6]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall7 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall8 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall9 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall10 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall11 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall12 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractPhysicsNodeCall13 call = reinterpret_cast<CuteQAbstractPhysicsNodeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractPhysicsNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QAbstractPhysicsNode10metaObjectEv(
    const QAbstractPhysicsNode *self) {
  return self->metaObject();
}

//  void *QAbstractPhysicsNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QAbstractPhysicsNode11qt_metacastEPKc(
    QAbstractPhysicsNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractPhysicsNode::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QAbstractPhysicsNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractPhysicsNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractPhysicsNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QAbstractPhysicsNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractPhysicsNode::tr(s, c, n));
}

//  void QAbstractPhysicsNode::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode24qt_qmlMarker_uncreatableEv(
    QAbstractPhysicsNode *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QAbstractPhysicsNode::QAbstractPhysicsNode()
extern "C" Q_DECL_EXPORT
QAbstractPhysicsNode *ritual_ZN20QAbstractPhysicsNodeC1Ev() {
  return new CuteQAbstractPhysicsNode();
}

//  QAbstractPhysicsNode::~QAbstractPhysicsNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNodeD1Ev(QAbstractPhysicsNode *self) {
  delete self;
}

//  QQmlListProperty<QAbstractCollisionShape>
//      QAbstractPhysicsNode::collisionShapes()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QAbstractCollisionShape> *ritual_ZN20QAbstractPhysicsNode15collisionShapesEv(
    QAbstractPhysicsNode *self) {
  return new QQmlListProperty<QAbstractCollisionShape>(
      self->collisionShapes());
}

//  const QVector<QAbstractCollisionShape *>
//      &QAbstractPhysicsNode::getCollisionShapesList() const
extern "C" Q_DECL_EXPORT
const QVector<QAbstractCollisionShape *> *ritual_ZNK20QAbstractPhysicsNode22getCollisionShapesListEv(
    const QAbstractPhysicsNode *self) {
  return &(self->getCollisionShapesList());
}

//  void QAbstractPhysicsNode::updateFromPhysicsTransform(const
//      physx::PxTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode26updateFromPhysicsTransformERKN5physx11PxTransformE(
    QAbstractPhysicsNode *self,
    const physx::PxTransform *transform) {
  self->updateFromPhysicsTransform(*transform);
}

//  void QAbstractPhysicsNode::registerContact(QAbstractPhysicsNode *body,
//      const QVector<QVector3D> &positions, const QVector<QVector3D>
//      &impulses, const QVector<QVector3D> &normals)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode15registerContactEPS_RK5QListI9QVector3DES5_S5_(
    QAbstractPhysicsNode *self,
    QAbstractPhysicsNode *body,
    const QVector<QVector3D> *positions,
    const QVector<QVector3D> *impulses,
    const QVector<QVector3D> *normals) {
  self->registerContact(body, *positions, *impulses, *normals);
}

//  bool QAbstractPhysicsNode::sendContactReports() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractPhysicsNode18sendContactReportsEv(
    const QAbstractPhysicsNode *self) {
  return self->sendContactReports();
}

//  void QAbstractPhysicsNode::setSendContactReports(bool sendContactReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode21setSendContactReportsEb(
    QAbstractPhysicsNode *self,
    bool sendContactReports) {
  self->setSendContactReports(sendContactReports);
}

//  bool QAbstractPhysicsNode::receiveContactReports() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractPhysicsNode21receiveContactReportsEv(
    const QAbstractPhysicsNode *self) {
  return self->receiveContactReports();
}

//  void QAbstractPhysicsNode::setReceiveContactReports(bool
//      receiveContactReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode24setReceiveContactReportsEb(
    QAbstractPhysicsNode *self,
    bool receiveContactReports) {
  self->setReceiveContactReports(receiveContactReports);
}

//  bool QAbstractPhysicsNode::sendTriggerReports() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractPhysicsNode18sendTriggerReportsEv(
    const QAbstractPhysicsNode *self) {
  return self->sendTriggerReports();
}

//  void QAbstractPhysicsNode::setSendTriggerReports(bool sendTriggerReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode21setSendTriggerReportsEb(
    QAbstractPhysicsNode *self,
    bool sendTriggerReports) {
  self->setSendTriggerReports(sendTriggerReports);
}

//  bool QAbstractPhysicsNode::receiveTriggerReports() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractPhysicsNode21receiveTriggerReportsEv(
    const QAbstractPhysicsNode *self) {
  return self->receiveTriggerReports();
}

//  void QAbstractPhysicsNode::setReceiveTriggerReports(bool
//      receiveTriggerReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode24setReceiveTriggerReportsEb(
    QAbstractPhysicsNode *self,
    bool receiveTriggerReports) {
  self->setReceiveTriggerReports(receiveTriggerReports);
}

//  bool QAbstractPhysicsNode::hasStaticShapes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractPhysicsNode15hasStaticShapesEv(
    const QAbstractPhysicsNode *self) {
  return self->hasStaticShapes();
}

//  QAbstractPhysXNode *QAbstractPhysicsNode::createPhysXBackend()
extern "C" Q_DECL_EXPORT
QAbstractPhysXNode *ritual_ZN20QAbstractPhysicsNode18createPhysXBackendEv(
    QAbstractPhysicsNode *self) {
  return self->createPhysXBackend();
}

//  int QAbstractPhysicsNode::filterGroup() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAbstractPhysicsNode11filterGroupEv(
    const QAbstractPhysicsNode *self) {
  return self->filterGroup();
}

//  void QAbstractPhysicsNode::setfilterGroup(int newfilterGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode14setfilterGroupEi(
    QAbstractPhysicsNode *self,
    int newfilterGroup) {
  self->setfilterGroup(newfilterGroup);
}

//  int QAbstractPhysicsNode::filterIgnoreGroups() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAbstractPhysicsNode18filterIgnoreGroupsEv(
    const QAbstractPhysicsNode *self) {
  return self->filterIgnoreGroups();
}

//  void QAbstractPhysicsNode::setFilterIgnoreGroups(int
//      newFilterIgnoreGroups)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode21setFilterIgnoreGroupsEi(
    QAbstractPhysicsNode *self,
    int newFilterIgnoreGroups) {
  self->setFilterIgnoreGroups(newFilterIgnoreGroups);
}

//  void QAbstractPhysicsNode::onShapeDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode16onShapeDestroyedEP7QObject(
    QAbstractPhysicsNode *self,
    QObject *object) {
  self->onShapeDestroyed(object);
}

//  void QAbstractPhysicsNode::onShapeNeedsRebuild(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode19onShapeNeedsRebuildEP7QObject(
    QAbstractPhysicsNode *self,
    QObject *object) {
  self->onShapeNeedsRebuild(object);
}

//  void QAbstractPhysicsNode::bodyContact(QAbstractPhysicsNode *body, const
//      QVector<QVector3D> &positions, const QVector<QVector3D> &impulses,
//      const QVector<QVector3D> &normals)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode11bodyContactEPS_RK5QListI9QVector3DES5_S5_(
    QAbstractPhysicsNode *self,
    QAbstractPhysicsNode *body,
    const QVector<QVector3D> *positions,
    const QVector<QVector3D> *impulses,
    const QVector<QVector3D> *normals) {
  self->bodyContact(body, *positions, *impulses, *normals);
}

//  void QAbstractPhysicsNode::sendContactReportsChanged(float
//      sendContactReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode25sendContactReportsChangedEf(
    QAbstractPhysicsNode *self,
    float sendContactReports) {
  self->sendContactReportsChanged(sendContactReports);
}

//  void QAbstractPhysicsNode::receiveContactReportsChanged(float
//      receiveContactReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode28receiveContactReportsChangedEf(
    QAbstractPhysicsNode *self,
    float receiveContactReports) {
  self->receiveContactReportsChanged(receiveContactReports);
}

//  void QAbstractPhysicsNode::sendTriggerReportsChanged(float
//      sendTriggerReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode25sendTriggerReportsChangedEf(
    QAbstractPhysicsNode *self,
    float sendTriggerReports) {
  self->sendTriggerReportsChanged(sendTriggerReports);
}

//  void QAbstractPhysicsNode::receiveTriggerReportsChanged(float
//      receiveTriggerReports)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode28receiveTriggerReportsChangedEf(
    QAbstractPhysicsNode *self,
    float receiveTriggerReports) {
  self->receiveTriggerReportsChanged(receiveTriggerReports);
}

//  void QAbstractPhysicsNode::enteredTriggerBody(QAbstractPhysicsNode *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode18enteredTriggerBodyEPS_(
    QAbstractPhysicsNode *self,
    QAbstractPhysicsNode *body) {
  self->enteredTriggerBody(body);
}

//  void QAbstractPhysicsNode::exitedTriggerBody(QAbstractPhysicsNode *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode17exitedTriggerBodyEPS_(
    QAbstractPhysicsNode *self,
    QAbstractPhysicsNode *body) {
  self->exitedTriggerBody(body);
}

//  void QAbstractPhysicsNode::filterGroupChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode18filterGroupChangedEv(
    QAbstractPhysicsNode *self) {
  self->filterGroupChanged();
}

//  void QAbstractPhysicsNode::filterIgnoreGroupsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode25filterIgnoreGroupsChangedEv(
    QAbstractPhysicsNode *self) {
  self->filterIgnoreGroupsChanged();
}

//  void QAbstractPhysicsNode::qmlAppendShape(QQmlListProperty<QAbstractColli
//      sionShape> *list, QAbstractCollisionShape *shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode14qmlAppendShapeEP16QQmlListPropertyI23QAbstractCollisionShapeEPS1_(
    QQmlListProperty<QAbstractCollisionShape> *list,
    QAbstractCollisionShape *shape) {
  QAbstractPhysicsNode::qmlAppendShape(list, shape);
}

//  QAbstractCollisionShape *QAbstractPhysicsNode::qmlShapeAt(QQmlListPropert
//      y<QAbstractCollisionShape> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QAbstractCollisionShape *ritual_ZN20QAbstractPhysicsNode10qmlShapeAtEP16QQmlListPropertyI23QAbstractCollisionShapeEx(
    QQmlListProperty<QAbstractCollisionShape> *list,
    qsizetype index) {
  return QAbstractPhysicsNode::qmlShapeAt(list, index);
}

//  qsizetype QAbstractPhysicsNode::qmlShapeCount(QQmlListProperty<QAbstractC
//      ollisionShape> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QAbstractPhysicsNode13qmlShapeCountEP16QQmlListPropertyI23QAbstractCollisionShapeE(
    QQmlListProperty<QAbstractCollisionShape> *list) {
  return QAbstractPhysicsNode::qmlShapeCount(list);
}

//  void QAbstractPhysicsNode::qmlClearShapes(QQmlListProperty<QAbstractColli
//      sionShape> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsNode14qmlClearShapesEP16QQmlListPropertyI23QAbstractCollisionShapeE(
    QQmlListProperty<QAbstractCollisionShape> *list) {
  QAbstractPhysicsNode::qmlClearShapes(list);
}

//  a Python function taken by a CuteQAbstractPhysicsNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractPhysicsNode(
    QAbstractPhysicsNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractPhysicsNode *>(self)->take(key, call);
}

//  a QQmlListProperty<QAbstractCollisionShape> a ritual of
//      QAbstractPhysicsNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractPhysicsNode__QQmlListProperty_QAbstractCollisionShape(
    QQmlListProperty<QAbstractCollisionShape> *self) {
  delete self;
}
