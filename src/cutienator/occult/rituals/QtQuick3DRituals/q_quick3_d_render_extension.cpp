//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3drenderextensions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQuick3D/qquick3drenderextensions.h>
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DRenderExtension that Python can take functions over in. Every QQuick3DRenderExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DRenderExtensionCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DRenderExtensionCall1)(const void *, int *);
typedef void (*CuteQQuick3DRenderExtensionCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DRenderExtensionCall3)(const void *, int *);
typedef void (*CuteQQuick3DRenderExtensionCall4)(const void *, int *);
typedef void (*CuteQQuick3DRenderExtensionCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DRenderExtensionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DRenderExtensionCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRenderExtensionCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRenderExtensionCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRenderExtensionCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRenderExtensionCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRenderExtensionCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DRenderExtension : public QQuick3DRenderExtension {
public:
  using QQuick3DRenderExtension::QQuick3DRenderExtension;
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
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
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
  //      *QQuick3DRenderExtension::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DRenderExtensionCall0 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DRenderExtension::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DRenderExtensionCall1 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DRenderExtensionCall2 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DRenderExtensionCall3 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DRenderExtensionCall4 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DRenderExtensionCall5 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall5>(taken[5]);
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
      CuteQQuick3DRenderExtensionCall6 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall6>(taken[6]);
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
      CuteQQuick3DRenderExtensionCall7 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall7>(taken[7]);
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
      CuteQQuick3DRenderExtensionCall8 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall8>(taken[8]);
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
      CuteQQuick3DRenderExtensionCall9 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall9>(taken[9]);
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
      CuteQQuick3DRenderExtensionCall10 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall10>(taken[10]);
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
      CuteQQuick3DRenderExtensionCall11 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall11>(taken[11]);
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
      CuteQQuick3DRenderExtensionCall12 call = reinterpret_cast<CuteQQuick3DRenderExtensionCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DRenderExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DRenderExtension10metaObjectEv(
    const QQuick3DRenderExtension *self) {
  return self->metaObject();
}

//  QString QQuick3DRenderExtension::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DRenderExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DRenderExtension::tr(s, c, n));
}

//  void QQuick3DRenderExtension::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DRenderExtension24qt_qmlMarker_uncreatableEv(
    QQuick3DRenderExtension *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DRenderExtension::QQuick3DRenderExtension(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRenderExtension *ritual_ZN23QQuick3DRenderExtensionC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DRenderExtension(parent);
}

//  QQuick3DRenderExtension::~QQuick3DRenderExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DRenderExtensionD1Ev(QQuick3DRenderExtension *self) {
  delete self;
}

//  QSSGRenderGraphObject
//      *QQuick3DRenderExtension::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN23QQuick3DRenderExtension17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRenderExtension *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  a Python function taken by a CuteQQuick3DRenderExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DRenderExtension(
    QQuick3DRenderExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DRenderExtension *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DRenderExtension::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN23QQuick3DRenderExtension17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRenderExtension *self,
    QSSGRenderGraphObject *node) {
  return self->QQuick3DRenderExtension::updateSpatialNode(node);
}
