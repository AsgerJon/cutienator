//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DMaterial : QQuick3DMaterial {
  using QQuick3DMaterial::updateSpatialNode;
  using QQuick3DMaterial::itemChange;
};

//  A QQuick3DMaterial that Python can take functions over in. Every QQuick3DMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DMaterialCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DMaterialCall1)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DMaterialCall2)(const void *, int *);
typedef void (*CuteQQuick3DMaterialCall3)(const void *, int *);
typedef void (*CuteQQuick3DMaterialCall4)(const void *, int *);
typedef void (*CuteQQuick3DMaterialCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DMaterialCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DMaterialCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DMaterialCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DMaterialCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DMaterialCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DMaterialCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DMaterialCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DMaterial : public QQuick3DMaterial {
public:
  using QQuick3DMaterial::QQuick3DMaterial;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DMaterial::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DMaterialCall0 call = reinterpret_cast<CuteQQuick3DMaterialCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DMaterial::updateSpatialNode(node);
  }

  //  void QQuick3DMaterial::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DMaterialCall1 call = reinterpret_cast<CuteQQuick3DMaterialCall1>(taken[1]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DMaterial::itemChange(a0, a1);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DMaterialCall2 call = reinterpret_cast<CuteQQuick3DMaterialCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DMaterialCall3 call = reinterpret_cast<CuteQQuick3DMaterialCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DMaterialCall4 call = reinterpret_cast<CuteQQuick3DMaterialCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DMaterialCall5 call = reinterpret_cast<CuteQQuick3DMaterialCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DMaterialCall6 call = reinterpret_cast<CuteQQuick3DMaterialCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DMaterialCall7 call = reinterpret_cast<CuteQQuick3DMaterialCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DMaterialCall8 call = reinterpret_cast<CuteQQuick3DMaterialCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DMaterialCall9 call = reinterpret_cast<CuteQQuick3DMaterialCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DMaterialCall10 call = reinterpret_cast<CuteQQuick3DMaterialCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DMaterialCall11 call = reinterpret_cast<CuteQQuick3DMaterialCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DMaterialCall12 call = reinterpret_cast<CuteQQuick3DMaterialCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DMaterial10metaObjectEv(
    const QQuick3DMaterial *self) {
  return self->metaObject();
}

//  QString QQuick3DMaterial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DMaterial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DMaterial::tr(s, c, n));
}

//  void QQuick3DMaterial::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DMaterial24qt_qmlMarker_uncreatableEv(
    QQuick3DMaterial *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DMaterial::~QQuick3DMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DMaterialD1Ev(QQuick3DMaterial *self) {
  delete self;
}

//  QQuick3DTexture *QQuick3DMaterial::lightProbe() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK16QQuick3DMaterial10lightProbeEv(
    const QQuick3DMaterial *self) {
  return self->lightProbe();
}

//  CullMode QQuick3DMaterial::cullMode() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::CullMode ritual_ZNK16QQuick3DMaterial8cullModeEv(
    const QQuick3DMaterial *self) {
  return self->cullMode();
}

//  DepthDrawMode QQuick3DMaterial::depthDrawMode() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::DepthDrawMode ritual_ZNK16QQuick3DMaterial13depthDrawModeEv(
    const QQuick3DMaterial *self) {
  return self->depthDrawMode();
}

//  void QQuick3DMaterial::setLightProbe(QQuick3DTexture *lightProbe)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DMaterial13setLightProbeEP15QQuick3DTexture(
    QQuick3DMaterial *self,
    QQuick3DTexture *lightProbe) {
  self->setLightProbe(lightProbe);
}

//  void QQuick3DMaterial::setCullMode(QQuick3DMaterial::CullMode cullMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DMaterial11setCullModeENS_8CullModeE(
    QQuick3DMaterial *self,
    QQuick3DMaterial::CullMode cullMode) {
  self->setCullMode(cullMode);
}

//  void QQuick3DMaterial::setDepthDrawMode(QQuick3DMaterial::DepthDrawMode
//      depthDrawMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DMaterial16setDepthDrawModeENS_13DepthDrawModeE(
    QQuick3DMaterial *self,
    QQuick3DMaterial::DepthDrawMode depthDrawMode) {
  self->setDepthDrawMode(depthDrawMode);
}

//  QSSGRenderGraphObject
//      *QQuick3DMaterial::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN16QQuick3DMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DMaterial *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DMaterial::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DMaterial::updateSceneManager(QQuick3DSceneManager
//      *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DMaterial18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DMaterial *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}

//  a Python function taken by a CuteQQuick3DMaterial, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DMaterial(
    QQuick3DMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DMaterial *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DMaterial::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN16QQuick3DMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DMaterial *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DMaterial *>(self)->OwnQQuick3DMaterial::updateSpatialNode(
      node);
}

//  void QQuick3DMaterial::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DMaterial *>(self)->OwnQQuick3DMaterial::itemChange(
      a0,
      *a1);
}
