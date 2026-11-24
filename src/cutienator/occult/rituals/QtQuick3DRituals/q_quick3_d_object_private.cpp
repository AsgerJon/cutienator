//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QQuick3DObjectPrivate that Python can take functions over in. Every QQuick3DObjectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DObjectPrivateCall0)(const void *, int *);
class CuteQQuick3DObjectPrivate : public QQuick3DObjectPrivate {
public:
  using QQuick3DObjectPrivate::QQuick3DObjectPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuick3DObjectPrivate12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuick3DObjectPrivate::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DObjectPrivateCall0 call = reinterpret_cast<CuteQQuick3DObjectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObjectPrivate::updatePolish();
  }
};

//  QQuick3DObject *QQuick3DObjectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZN21QQuick3DObjectPrivate6q_funcEv(
    QQuick3DObjectPrivate *self) {
  return self->q_func();
}

//  const QQuick3DObject *QQuick3DObjectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DObject *ritual_ZNK21QQuick3DObjectPrivate6q_funcEv(
    const QQuick3DObjectPrivate *self) {
  return self->q_func();
}

//  QQuick3DObjectPrivate *QQuick3DObjectPrivate::get(QQuick3DObject *item)
extern "C" Q_DECL_EXPORT
QQuick3DObjectPrivate *ritual_ZN21QQuick3DObjectPrivate3getEP14QQuick3DObject(
    QQuick3DObject *item) {
  return QQuick3DObjectPrivate::get(item);
}

//  const QQuick3DObjectPrivate *QQuick3DObjectPrivate::get(const
//      QQuick3DObject *item)
extern "C" Q_DECL_EXPORT
const QQuick3DObjectPrivate *ritual_ZN21QQuick3DObjectPrivate3getEPK14QQuick3DObject(
    const QQuick3DObject *item) {
  return QQuick3DObjectPrivate::get(item);
}

//  QSSGRenderGraphObject
//      *QQuick3DObjectPrivate::updateSpatialNode(QQuick3DObject *o,
//      QSSGRenderGraphObject *n)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QQuick3DObjectPrivate17updateSpatialNodeEP14QQuick3DObjectP21QSSGRenderGraphObject(
    QQuick3DObject *o,
    QSSGRenderGraphObject *n) {
  return QQuick3DObjectPrivate::updateSpatialNode(o, n);
}

//  QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t, FlagsT f)
extern "C" Q_DECL_EXPORT
QQuick3DObjectPrivate *ritual_ZN21QQuick3DObjectPrivateC1EN21QSSGRenderGraphObject4TypeEj(
    QQuick3DObjectPrivate::Type t,
    QQuick3DObjectPrivate::FlagsT f) {
  return new CuteQQuick3DObjectPrivate(t, f);
}

//  QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t, Flags f)
extern "C" Q_DECL_EXPORT
QQuick3DObjectPrivate *ritual_ZN21QQuick3DObjectPrivateC1EN21QSSGRenderGraphObject4TypeENS_5FlagsE(
    QQuick3DObjectPrivate::Type t,
    QQuick3DObjectPrivate::Flags f) {
  return new CuteQQuick3DObjectPrivate(t, f);
}

//  QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t)
extern "C" Q_DECL_EXPORT
QQuick3DObjectPrivate *ritual_ZN21QQuick3DObjectPrivateC1EN21QSSGRenderGraphObject4TypeE(
    QQuick3DObjectPrivate::Type t) {
  return new CuteQQuick3DObjectPrivate(t);
}

//  QQuick3DObjectPrivate::~QQuick3DObjectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivateD1Ev(QQuick3DObjectPrivate *self) {
  delete self;
}

//  void QQuick3DObjectPrivate::init(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate4initEP14QQuick3DObject(
    QQuick3DObjectPrivate *self,
    QQuick3DObject *parent) {
  self->init(parent);
}

//  QString QQuick3DObjectPrivate::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DObjectPrivate5stateEv(
    const QQuick3DObjectPrivate *self) {
  return new QString(self->state());
}

//  void QQuick3DObjectPrivate::setState(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate8setStateERK7QString(
    QQuick3DObjectPrivate *self,
    const QString *a0) {
  self->setState(*a0);
}

//  void QQuick3DObjectPrivate::_q_resourceObjectDeleted(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate24_q_resourceObjectDeletedEP7QObject(
    QQuick3DObjectPrivate *self,
    QObject *a0) {
  self->_q_resourceObjectDeleted(a0);
}

//  void QQuick3DObjectPrivate::_q_cleanupContentItem2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate23_q_cleanupContentItem2DEv(
    QQuick3DObjectPrivate *self) {
  self->_q_cleanupContentItem2D();
}

//  quint64
//      QQuick3DObjectPrivate::_q_createJSWrapper(QQmlV4ExecutionEnginePtr
//      engine)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN21QQuick3DObjectPrivate18_q_createJSWrapperEPN3QV415ExecutionEngineE(
    QQuick3DObjectPrivate *self,
    QQmlV4ExecutionEnginePtr engine) {
  return self->_q_createJSWrapper(engine);
}

//  void
//      QQuick3DObjectPrivate::addItemChangeListener(QQuick3DObjectChangeList
//      ener *listener, ChangeTypes types)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate21addItemChangeListenerEP28QQuick3DObjectChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuick3DObjectPrivate *self,
    QQuick3DObjectChangeListener *listener,
    int types) {
  self->addItemChangeListener(
      listener,
      QFlags<QQuick3DObjectPrivate::ChangeType>::fromInt(types));
}

//  void QQuick3DObjectPrivate::updateOrAddItemChangeListener(QQuick3DObjectC
//      hangeListener *listener, ChangeTypes types)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate29updateOrAddItemChangeListenerEP28QQuick3DObjectChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuick3DObjectPrivate *self,
    QQuick3DObjectChangeListener *listener,
    int types) {
  self->updateOrAddItemChangeListener(
      listener,
      QFlags<QQuick3DObjectPrivate::ChangeType>::fromInt(types));
}

//  void QQuick3DObjectPrivate::removeItemChangeListener(QQuick3DObjectChange
//      Listener *a0, ChangeTypes types)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate24removeItemChangeListenerEP28QQuick3DObjectChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuick3DObjectPrivate *self,
    QQuick3DObjectChangeListener *a0,
    int types) {
  self->removeItemChangeListener(
      a0,
      QFlags<QQuick3DObjectPrivate::ChangeType>::fromInt(types));
}

//  QQuickStateGroup *QQuick3DObjectPrivate::_states()
extern "C" Q_DECL_EXPORT
QQuickStateGroup *ritual_ZN21QQuick3DObjectPrivate7_statesEv(
    QQuick3DObjectPrivate *self) {
  return self->_states();
}

//  QString QQuick3DObjectPrivate::dirtyToString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DObjectPrivate13dirtyToStringEv(
    const QQuick3DObjectPrivate *self) {
  return new QString(self->dirtyToString());
}

//  void QQuick3DObjectPrivate::dirty(DirtyType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate5dirtyENS_9DirtyTypeE(
    QQuick3DObjectPrivate *self,
    QQuick3DObjectPrivate::DirtyType a0) {
  self->dirty(a0);
}

//  void QQuick3DObjectPrivate::addToDirtyList()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate14addToDirtyListEv(
    QQuick3DObjectPrivate *self) {
  self->addToDirtyList();
}

//  void QQuick3DObjectPrivate::removeFromDirtyList()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate19removeFromDirtyListEv(
    QQuick3DObjectPrivate *self) {
  self->removeFromDirtyList();
}

//  bool QQuick3DObjectPrivate::hasFlag(Flags flag)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuick3DObjectPrivate7hasFlagENS_5FlagsE(
    QQuick3DObjectPrivate *self,
    QQuick3DObjectPrivate::Flags flag) {
  return self->hasFlag(flag);
}

//  void QQuick3DObjectPrivate::setCulled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate9setCulledEb(
    QQuick3DObjectPrivate *self,
    bool a0) {
  self->setCulled(a0);
}

//  void QQuick3DObjectPrivate::addChild(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate8addChildEP14QQuick3DObject(
    QQuick3DObjectPrivate *self,
    QQuick3DObject *a0) {
  self->addChild(a0);
}

//  void QQuick3DObjectPrivate::removeChild(QQuick3DObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate11removeChildEP14QQuick3DObject(
    QQuick3DObjectPrivate *self,
    QQuick3DObject *a0) {
  self->removeChild(a0);
}

//  void QQuick3DObjectPrivate::siblingOrderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate19siblingOrderChangedEv(
    QQuick3DObjectPrivate *self) {
  self->siblingOrderChanged();
}

//  void QQuick3DObjectPrivate::derefSceneManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate17derefSceneManagerEv(
    QQuick3DObjectPrivate *self) {
  self->derefSceneManager();
}

//  void QQuick3DObjectPrivate::derefSceneManager(QQuick3DObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate17derefSceneManagerEP14QQuick3DObject(
    QQuick3DObject *obj) {
  QQuick3DObjectPrivate::derefSceneManager(obj);
}

//  void QQuick3DObjectPrivate::updateSubFocusItem(QQuick3DObject *scope,
//      bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate18updateSubFocusItemEP14QQuick3DObjectb(
    QQuick3DObjectPrivate *self,
    QQuick3DObject *scope,
    bool focus) {
  self->updateSubFocusItem(scope, focus);
}

//  void QQuick3DObjectPrivate::itemChange(QQuick3DObject::ItemChange a0,
//      const QQuick3DObject::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DObjectPrivate *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DObjectPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate12updatePolishEv(
    QQuick3DObjectPrivate *self) {
  self->updatePolish();
}

//  void QQuick3DObjectPrivate::requestSecondaryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate22requestSecondaryUpdateEv(
    QQuick3DObjectPrivate *self) {
  self->requestSecondaryUpdate();
}

//  a Python function taken by a CuteQQuick3DObjectPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DObjectPrivate(
    QQuick3DObjectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DObjectPrivate *>(self)->take(key, call);
}

//  void QQuick3DObjectPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuick3DObjectPrivate12updatePolishEv(
    QQuick3DObjectPrivate *self) {
  self->QQuick3DObjectPrivate::updatePolish();
}
