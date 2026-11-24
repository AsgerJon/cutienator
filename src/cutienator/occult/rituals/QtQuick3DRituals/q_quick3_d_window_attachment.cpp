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

//  A QQuick3DWindowAttachment that Python can take functions over in. Every QQuick3DWindowAttachment
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DWindowAttachmentCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DWindowAttachmentCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DWindowAttachmentCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DWindowAttachmentCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DWindowAttachmentCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DWindowAttachmentCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DWindowAttachmentCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DWindowAttachment : public QQuick3DWindowAttachment {
public:
  using QQuick3DWindowAttachment::QQuick3DWindowAttachment;
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
      CuteQQuick3DWindowAttachmentCall0 call = reinterpret_cast<CuteQQuick3DWindowAttachmentCall0>(taken[0]);
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
      CuteQQuick3DWindowAttachmentCall1 call = reinterpret_cast<CuteQQuick3DWindowAttachmentCall1>(taken[1]);
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
      CuteQQuick3DWindowAttachmentCall2 call = reinterpret_cast<CuteQQuick3DWindowAttachmentCall2>(taken[2]);
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
      CuteQQuick3DWindowAttachmentCall3 call = reinterpret_cast<CuteQQuick3DWindowAttachmentCall3>(taken[3]);
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
      CuteQQuick3DWindowAttachmentCall4 call = reinterpret_cast<CuteQQuick3DWindowAttachmentCall4>(taken[4]);
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
      CuteQQuick3DWindowAttachmentCall5 call = reinterpret_cast<CuteQQuick3DWindowAttachmentCall5>(taken[5]);
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
      CuteQQuick3DWindowAttachmentCall6 call = reinterpret_cast<CuteQQuick3DWindowAttachmentCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DWindowAttachment::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DWindowAttachment10metaObjectEv(
    const QQuick3DWindowAttachment *self) {
  return self->metaObject();
}

//  QString QQuick3DWindowAttachment::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuick3DWindowAttachment2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DWindowAttachment::tr(s, c, n));
}

//  QQuick3DWindowAttachment::QQuick3DWindowAttachment(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QQuick3DWindowAttachment *ritual_ZN24QQuick3DWindowAttachmentC1EP12QQuickWindow(
    QQuickWindow *window) {
  return new CuteQQuick3DWindowAttachment(window);
}

//  QQuick3DWindowAttachment::~QQuick3DWindowAttachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachmentD1Ev(
    QQuick3DWindowAttachment *self) {
  delete self;
}

//  void QQuick3DWindowAttachment::preSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment7preSyncEv(
    QQuick3DWindowAttachment *self) {
  self->preSync();
}

//  void QQuick3DWindowAttachment::cleanupResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment16cleanupResourcesEv(
    QQuick3DWindowAttachment *self) {
  self->cleanupResources();
}

//  void QQuick3DWindowAttachment::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment13requestUpdateEv(
    QQuick3DWindowAttachment *self) {
  self->requestUpdate();
}

//  void QQuick3DWindowAttachment::evaluateEol()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment11evaluateEolEv(
    QQuick3DWindowAttachment *self) {
  self->evaluateEol();
}

//  QQuickWindow *QQuick3DWindowAttachment::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK24QQuick3DWindowAttachment6windowEv(
    const QQuick3DWindowAttachment *self) {
  return self->window();
}

//  QSSGRenderRoot *QQuick3DWindowAttachment::rootNode() const
extern "C" Q_DECL_EXPORT
QSSGRenderRoot *ritual_ZNK24QQuick3DWindowAttachment8rootNodeEv(
    const QQuick3DWindowAttachment *self) {
  return self->rootNode();
}

//  void QQuick3DWindowAttachment::queueForCleanup(QSSGRenderGraphObject
//      *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment15queueForCleanupEP21QSSGRenderGraphObject(
    QQuick3DWindowAttachment *self,
    QSSGRenderGraphObject *obj) {
  self->queueForCleanup(obj);
}

//  void QQuick3DWindowAttachment::queueForCleanup(QQuick3DSceneManager
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment15queueForCleanupEP20QQuick3DSceneManager(
    QQuick3DWindowAttachment *self,
    QQuick3DSceneManager *manager) {
  self->queueForCleanup(manager);
}

//  void QQuick3DWindowAttachment::queueForCleanup(QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment15queueForCleanupEP15QSSGRenderLayer(
    QQuick3DWindowAttachment *self,
    QSSGRenderLayer *layer) {
  self->queueForCleanup(layer);
}

//  void QQuick3DWindowAttachment::onReleaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment24onReleaseCachedResourcesEv(
    QQuick3DWindowAttachment *self) {
  self->onReleaseCachedResources();
}

//  void QQuick3DWindowAttachment::onInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DWindowAttachment13onInvalidatedEv(
    QQuick3DWindowAttachment *self) {
  self->onInvalidated();
}

//  a Python function taken by a CuteQQuick3DWindowAttachment, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DWindowAttachment(
    QQuick3DWindowAttachment *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DWindowAttachment *>(self)->take(key, call);
}
