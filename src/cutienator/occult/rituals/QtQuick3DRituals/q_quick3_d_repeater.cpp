//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3drepeater_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3drepeater_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DRepeater may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DRepeater : QQuick3DRepeater {
  using QQuick3DRepeater::componentComplete;
  using QQuick3DRepeater::itemChange;
  using QQuick3DRepeater::initDelegate;
};

//  A QQuick3DRepeater that Python can take functions over in. Every QQuick3DRepeater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DRepeaterCall0)(const void *, int *);
typedef void (*CuteQQuick3DRepeaterCall1)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DRepeaterCall2)(const void *, int, QQuick3DNode *, int *);
typedef void (*CuteQQuick3DRepeaterCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRepeaterCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRepeaterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuick3DRepeaterCall6)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DRepeaterCall7)(const void *, int *);
typedef void (*CuteQQuick3DRepeaterCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DRepeaterCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DRepeaterCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRepeaterCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRepeaterCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRepeaterCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DRepeater : public QQuick3DRepeater {
public:
  using QQuick3DRepeater::QQuick3DRepeater;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DRepeater12initDelegateEiP12QQuick3DNode")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
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

  //  void QQuick3DRepeater::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall0 call = reinterpret_cast<CuteQQuick3DRepeaterCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DRepeater::componentComplete();
  }

  //  void QQuick3DRepeater::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuick3DObject::ItemChange change,
      const QQuick3DObject::ItemChangeData &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall1 call = reinterpret_cast<CuteQQuick3DRepeaterCall1>(taken[1]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuick3DRepeater::itemChange(change, value);
  }

  //  void QQuick3DRepeater::initDelegate(int a0, QQuick3DNode *a1)
  void initDelegate(int a0, QQuick3DNode *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall2 call = reinterpret_cast<CuteQQuick3DRepeaterCall2>(taken[2]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuick3DRepeater::initDelegate(a0, a1);
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall3 call = reinterpret_cast<CuteQQuick3DRepeaterCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall4 call = reinterpret_cast<CuteQQuick3DRepeaterCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall5 call = reinterpret_cast<CuteQQuick3DRepeaterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall6 call = reinterpret_cast<CuteQQuick3DRepeaterCall6>(taken[6]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall7 call = reinterpret_cast<CuteQQuick3DRepeaterCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DRepeaterCall8 call = reinterpret_cast<CuteQQuick3DRepeaterCall8>(taken[8]);
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
      CuteQQuick3DRepeaterCall9 call = reinterpret_cast<CuteQQuick3DRepeaterCall9>(taken[9]);
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
      CuteQQuick3DRepeaterCall10 call = reinterpret_cast<CuteQQuick3DRepeaterCall10>(taken[10]);
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
      CuteQQuick3DRepeaterCall11 call = reinterpret_cast<CuteQQuick3DRepeaterCall11>(taken[11]);
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
      CuteQQuick3DRepeaterCall12 call = reinterpret_cast<CuteQQuick3DRepeaterCall12>(taken[12]);
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
      CuteQQuick3DRepeaterCall13 call = reinterpret_cast<CuteQQuick3DRepeaterCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DRepeater::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DRepeater10metaObjectEv(
    const QQuick3DRepeater *self) {
  return self->metaObject();
}

//  QString QQuick3DRepeater::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DRepeater2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DRepeater::tr(s, c, n));
}

//  QQuick3DRepeater::QQuick3DRepeater(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRepeater *ritual_ZN16QQuick3DRepeaterC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DRepeater(parent);
}

//  QQuick3DRepeater::~QQuick3DRepeater()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeaterD1Ev(QQuick3DRepeater *self) {
  delete self;
}

//  QVariant QQuick3DRepeater::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQuick3DRepeater5modelEv(
    const QQuick3DRepeater *self) {
  return new QVariant(self->model());
}

//  void QQuick3DRepeater::setModel(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater8setModelERK8QVariant(
    QQuick3DRepeater *self,
    const QVariant *a0) {
  self->setModel(*a0);
}

//  QQmlComponent *QQuick3DRepeater::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK16QQuick3DRepeater8delegateEv(
    const QQuick3DRepeater *self) {
  return self->delegate();
}

//  void QQuick3DRepeater::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater11setDelegateEP13QQmlComponent(
    QQuick3DRepeater *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  int QQuick3DRepeater::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DRepeater5countEv(const QQuick3DRepeater *self) {
  return self->count();
}

//  QQuick3DObject *QQuick3DRepeater::objectAt(int index) const
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZNK16QQuick3DRepeater8objectAtEi(
    const QQuick3DRepeater *self,
    int index) {
  return self->objectAt(index);
}

//  QQmlDelegateModel::DelegateModelAccess
//      QQuick3DRepeater::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK16QQuick3DRepeater19delegateModelAccessEv(
    const QQuick3DRepeater *self) {
  return self->delegateModelAccess();
}

//  void QQuick3DRepeater::setDelegateModelAccess(QQmlDelegateModel::Delegate
//      ModelAccess delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater22setDelegateModelAccessEN17QQmlDelegateModel19DelegateModelAccessE(
    QQuick3DRepeater *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  void QQuick3DRepeater::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater5clearEv(QQuick3DRepeater *self) {
  self->clear();
}

//  void QQuick3DRepeater::regenerate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater10regenerateEv(QQuick3DRepeater *self) {
  self->regenerate();
}

//  void QQuick3DRepeater::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater17componentCompleteEv(
    QQuick3DRepeater *self) {
  self->componentComplete();
}

//  void QQuick3DRepeater::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DRepeater *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuick3DRepeater::initDelegate(int a0, QQuick3DNode *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater12initDelegateEiP12QQuick3DNode(
    QQuick3DRepeater *self,
    int a0,
    QQuick3DNode *a1) {
  self->initDelegate(a0, a1);
}

//  void QQuick3DRepeater::createdObject(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater13createdObjectEiP7QObject(
    QQuick3DRepeater *self,
    int index,
    QObject *item) {
  self->createdObject(index, item);
}

//  void QQuick3DRepeater::initObject(int a0, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater10initObjectEiP7QObject(
    QQuick3DRepeater *self,
    int a0,
    QObject *item) {
  self->initObject(a0, item);
}

//  void QQuick3DRepeater::modelUpdated(const QQmlChangeSet &changeSet, bool
//      reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater12modelUpdatedERK13QQmlChangeSetb(
    QQuick3DRepeater *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->modelUpdated(*changeSet, reset);
}

//  void QQuick3DRepeater::requestItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater12requestItemsEv(QQuick3DRepeater *self) {
  self->requestItems();
}

//  void QQuick3DRepeater::applyDelegateChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater19applyDelegateChangeEv(
    QQuick3DRepeater *self) {
  self->applyDelegateChange();
}

//  QQmlDelegateModel *QQuick3DRepeater::createDelegateModel()
extern "C" Q_DECL_EXPORT
QQmlDelegateModel *ritual_ZN16QQuick3DRepeater19createDelegateModelEv(
    QQuick3DRepeater *self) {
  return self->createDelegateModel();
}

//  void QQuick3DRepeater::connectModel(QQmlDelegateModelPointer *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater12connectModelEP24QQmlDelegateModelPointer(
    QQuick3DRepeater *self,
    QQmlDelegateModelPointer *model) {
  self->connectModel(model);
}

//  void QQuick3DRepeater::disconnectModel(QQmlDelegateModelPointer *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DRepeater15disconnectModelEP24QQmlDelegateModelPointer(
    QQuick3DRepeater *self,
    QQmlDelegateModelPointer *model) {
  self->disconnectModel(model);
}

//  a Python function taken by a CuteQQuick3DRepeater, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DRepeater(
    QQuick3DRepeater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DRepeater *>(self)->take(key, call);
}

//  void QQuick3DRepeater::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DRepeater17componentCompleteEv(
    QQuick3DRepeater *self) {
  static_cast<OwnQQuick3DRepeater *>(self)->OwnQQuick3DRepeater::componentComplete();
}

//  void QQuick3DRepeater::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DRepeater10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DRepeater *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  static_cast<OwnQQuick3DRepeater *>(self)->OwnQQuick3DRepeater::itemChange(
      change,
      *value);
}

//  void QQuick3DRepeater::initDelegate(int a0, QQuick3DNode *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DRepeater12initDelegateEiP12QQuick3DNode(
    QQuick3DRepeater *self,
    int a0,
    QQuick3DNode *a1) {
  static_cast<OwnQQuick3DRepeater *>(self)->OwnQQuick3DRepeater::initDelegate(
      a0,
      a1);
}
