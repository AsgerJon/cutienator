//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenemanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DSceneManager that Python can take functions over in. Every QQuick3DSceneManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSceneManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSceneManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DSceneManager : public QQuick3DSceneManager {
public:
  using QQuick3DSceneManager::QQuick3DSceneManager;
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
      CuteQQuick3DSceneManagerCall0 call = reinterpret_cast<CuteQQuick3DSceneManagerCall0>(taken[0]);
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
      CuteQQuick3DSceneManagerCall1 call = reinterpret_cast<CuteQQuick3DSceneManagerCall1>(taken[1]);
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
      CuteQQuick3DSceneManagerCall2 call = reinterpret_cast<CuteQQuick3DSceneManagerCall2>(taken[2]);
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
      CuteQQuick3DSceneManagerCall3 call = reinterpret_cast<CuteQQuick3DSceneManagerCall3>(taken[3]);
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
      CuteQQuick3DSceneManagerCall4 call = reinterpret_cast<CuteQQuick3DSceneManagerCall4>(taken[4]);
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
      CuteQQuick3DSceneManagerCall5 call = reinterpret_cast<CuteQQuick3DSceneManagerCall5>(taken[5]);
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
      CuteQQuick3DSceneManagerCall6 call = reinterpret_cast<CuteQQuick3DSceneManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DSceneManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuick3DSceneManager10metaObjectEv(
    const QQuick3DSceneManager *self) {
  return self->metaObject();
}

//  QString QQuick3DSceneManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuick3DSceneManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DSceneManager::tr(s, c, n));
}

//  QQuick3DSceneManager::QQuick3DSceneManager(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DSceneManager *ritual_ZN20QQuick3DSceneManagerC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DSceneManager(parent);
}

//  QQuick3DSceneManager::~QQuick3DSceneManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManagerD1Ev(QQuick3DSceneManager *self) {
  delete self;
}

//  void QQuick3DSceneManager::setWindow(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager9setWindowEP12QQuickWindow(
    QQuick3DSceneManager *self,
    QQuickWindow *window) {
  self->setWindow(window);
}

//  QQuickWindow *QQuick3DSceneManager::window()
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZN20QQuick3DSceneManager6windowEv(
    QQuick3DSceneManager *self) {
  return self->window();
}

//  void QQuick3DSceneManager::dirtyItem(QQuick3DObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager9dirtyItemEP14QQuick3DObject(
    QQuick3DSceneManager *self,
    QQuick3DObject *item) {
  self->dirtyItem(item);
}

//  void QQuick3DSceneManager::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager13requestUpdateEv(
    QQuick3DSceneManager *self) {
  self->requestUpdate();
}

//  void QQuick3DSceneManager::cleanup(QSSGRenderGraphObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager7cleanupEP21QSSGRenderGraphObject(
    QQuick3DSceneManager *self,
    QSSGRenderGraphObject *item) {
  self->cleanup(item);
}

//  void QQuick3DSceneManager::polishItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager11polishItemsEv(
    QQuick3DSceneManager *self) {
  self->polishItems();
}

//  void QQuick3DSceneManager::forcePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager11forcePolishEv(
    QQuick3DSceneManager *self) {
  self->forcePolish();
}

//  void QQuick3DSceneManager::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager4syncEv(QQuick3DSceneManager *self) {
  self->sync();
}

//  void QQuick3DSceneManager::preSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager7preSyncEv(QQuick3DSceneManager *self) {
  self->preSync();
}

//  SyncResult QQuick3DSceneManager::cleanupNodes()
extern "C" Q_DECL_EXPORT
QQuick3DSceneManager::SyncResult ritual_ZN20QQuick3DSceneManager12cleanupNodesEv(
    QQuick3DSceneManager *self) {
  return self->cleanupNodes();
}

//  SyncResult QQuick3DSceneManager::updateDirtyResourceNodes()
extern "C" Q_DECL_EXPORT
QQuick3DSceneManager::SyncResult ritual_ZN20QQuick3DSceneManager24updateDirtyResourceNodesEv(
    QQuick3DSceneManager *self) {
  return self->updateDirtyResourceNodes();
}

//  void QQuick3DSceneManager::updateDirtySpatialNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager23updateDirtySpatialNodesEv(
    QQuick3DSceneManager *self) {
  self->updateDirtySpatialNodes();
}

//  SyncResult QQuick3DSceneManager::updateDiryExtensions()
extern "C" Q_DECL_EXPORT
QQuick3DSceneManager::SyncResult ritual_ZN20QQuick3DSceneManager20updateDiryExtensionsEv(
    QQuick3DSceneManager *self) {
  return self->updateDiryExtensions();
}

//  SyncResult QQuick3DSceneManager::updateDirtyResourceSecondPass()
extern "C" Q_DECL_EXPORT
QQuick3DSceneManager::SyncResult ritual_ZN20QQuick3DSceneManager29updateDirtyResourceSecondPassEv(
    QQuick3DSceneManager *self) {
  return self->updateDirtyResourceSecondPass();
}

//  void QQuick3DSceneManager::updateDirtyResource(QQuick3DObject
//      *resourceObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager19updateDirtyResourceEP14QQuick3DObject(
    QQuick3DSceneManager *self,
    QQuick3DObject *resourceObject) {
  self->updateDirtyResource(resourceObject);
}

//  void QQuick3DSceneManager::updateDirtySpatialNode(QQuick3DNode
//      *spatialNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DSceneManager22updateDirtySpatialNodeEP12QQuick3DNode(
    QQuick3DSceneManager *self,
    QQuick3DNode *spatialNode) {
  self->updateDirtySpatialNode(spatialNode);
}

//  QQuick3DObject *QQuick3DSceneManager::lookUpNode(const
//      QSSGRenderGraphObject *node) const
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZNK20QQuick3DSceneManager10lookUpNodeEPK21QSSGRenderGraphObject(
    const QQuick3DSceneManager *self,
    const QSSGRenderGraphObject *node) {
  return self->lookUpNode(node);
}

//  a Python function taken by a CuteQQuick3DSceneManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DSceneManager(
    QQuick3DSceneManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DSceneManager *>(self)->take(key, call);
}
