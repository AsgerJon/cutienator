//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DSpati
//  alAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3daudiolistener_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qtquick3daudioglobal_p.h>
#include <QtQuick3DSpatialAudio/QtQuick3DSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3daudiolistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DAudioListener may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DAudioListener : QQuick3DAudioListener {
  using QQuick3DAudioListener::updateSpatialNode;
};

//  A QQuick3DAudioListener that Python can take functions over in. Every QQuick3DAudioListener
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DAudioListenerCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DAudioListenerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioListenerCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioListenerCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioListenerCall4)(const void *, int *);
typedef void (*CuteQQuick3DAudioListenerCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DAudioListenerCall6)(const void *, int *);
typedef void (*CuteQQuick3DAudioListenerCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAudioListenerCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAudioListenerCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioListenerCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioListenerCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioListenerCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DAudioListener : public QQuick3DAudioListener {
public:
  using QQuick3DAudioListener::QQuick3DAudioListener;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
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

  //  QSSGRenderGraphObject
  //      *QQuick3DAudioListener::updateSpatialNode(QSSGRenderGraphObject
  //      *a0)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DAudioListenerCall0 call = reinterpret_cast<CuteQQuick3DAudioListenerCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DAudioListener::updateSpatialNode(a0);
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DAudioListenerCall1 call = reinterpret_cast<CuteQQuick3DAudioListenerCall1>(taken[1]);
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
      CuteQQuick3DAudioListenerCall2 call = reinterpret_cast<CuteQQuick3DAudioListenerCall2>(taken[2]);
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
      CuteQQuick3DAudioListenerCall3 call = reinterpret_cast<CuteQQuick3DAudioListenerCall3>(taken[3]);
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
      CuteQQuick3DAudioListenerCall4 call = reinterpret_cast<CuteQQuick3DAudioListenerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DAudioListenerCall5 call = reinterpret_cast<CuteQQuick3DAudioListenerCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DAudioListenerCall6 call = reinterpret_cast<CuteQQuick3DAudioListenerCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DAudioListenerCall7 call = reinterpret_cast<CuteQQuick3DAudioListenerCall7>(taken[7]);
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
      CuteQQuick3DAudioListenerCall8 call = reinterpret_cast<CuteQQuick3DAudioListenerCall8>(taken[8]);
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
      CuteQQuick3DAudioListenerCall9 call = reinterpret_cast<CuteQQuick3DAudioListenerCall9>(taken[9]);
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
      CuteQQuick3DAudioListenerCall10 call = reinterpret_cast<CuteQQuick3DAudioListenerCall10>(taken[10]);
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
      CuteQQuick3DAudioListenerCall11 call = reinterpret_cast<CuteQQuick3DAudioListenerCall11>(taken[11]);
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
      CuteQQuick3DAudioListenerCall12 call = reinterpret_cast<CuteQQuick3DAudioListenerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DAudioListener::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DAudioListener10metaObjectEv(
    const QQuick3DAudioListener *self) {
  return self->metaObject();
}

//  void *QQuick3DAudioListener::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuick3DAudioListener11qt_metacastEPKc(
    QQuick3DAudioListener *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DAudioListener::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuick3DAudioListener11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DAudioListener *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DAudioListener::~QQuick3DAudioListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAudioListenerD1Ev(QQuick3DAudioListener *self) {
  delete self;
}

//  QAudioListener *QQuick3DAudioListener::listener()
extern "C" Q_DECL_EXPORT
QAudioListener *ritual_ZN21QQuick3DAudioListener8listenerEv(
    QQuick3DAudioListener *self) {
  return self->listener();
}

//  QSSGRenderGraphObject
//      *QQuick3DAudioListener::updateSpatialNode(QSSGRenderGraphObject *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QQuick3DAudioListener17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DAudioListener *self,
    QSSGRenderGraphObject *a0) {
  return self->updateSpatialNode(a0);
}

//  void QQuick3DAudioListener::updatePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAudioListener14updatePositionEv(
    QQuick3DAudioListener *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAudioListener")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updatePosition()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updatePosition()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DAudioListener::updateRotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAudioListener14updateRotationEv(
    QQuick3DAudioListener *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAudioListener")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateRotation()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateRotation()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuick3DAudioListener, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DAudioListener(
    QQuick3DAudioListener *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DAudioListener *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DAudioListener::updateSpatialNode(QSSGRenderGraphObject *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN21QQuick3DAudioListener17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DAudioListener *self,
    QSSGRenderGraphObject *a0) {
  return static_cast<OwnQQuick3DAudioListener *>(self)->OwnQQuick3DAudioListener::updateSpatialNode(
      a0);
}
