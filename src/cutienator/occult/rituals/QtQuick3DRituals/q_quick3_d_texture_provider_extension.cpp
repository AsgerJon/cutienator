//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3dtextureproviderextension.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick3D/qquick3dtextureproviderextension.h>
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DTextureProviderExtension may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DTextureProviderExtension : QQuick3DTextureProviderExtension {
  using QQuick3DTextureProviderExtension::event;
  using QQuick3DTextureProviderExtension::updateSpatialNode;
};

//  A QQuick3DTextureProviderExtension that Python can take functions over in. Every QQuick3DTextureProviderExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureProviderExtensionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuick3DTextureProviderExtensionCall1)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DTextureProviderExtensionCall2)(const void *, int *);
typedef void (*CuteQQuick3DTextureProviderExtensionCall3)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DTextureProviderExtensionCall4)(const void *, int *);
typedef void (*CuteQQuick3DTextureProviderExtensionCall5)(const void *, int *);
typedef void (*CuteQQuick3DTextureProviderExtensionCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureProviderExtensionCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureProviderExtensionCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureProviderExtensionCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureProviderExtensionCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureProviderExtensionCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureProviderExtensionCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DTextureProviderExtension : public QQuick3DTextureProviderExtension {
public:
  using QQuick3DTextureProviderExtension::QQuick3DTextureProviderExtension;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[6] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
  //  bool QQuick3DTextureProviderExtension::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall0 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuick3DTextureProviderExtension::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSSGRenderGraphObject *QQuick3DTextureProviderExtension::updateSpatia
  //      lNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall1 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall1>(taken[1]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DTextureProviderExtension::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall2 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall3 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall3>(taken[3]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall4 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall5 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall6 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DTextureProviderExtensionCall7 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall7>(taken[7]);
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
      CuteQQuick3DTextureProviderExtensionCall8 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall8>(taken[8]);
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
      CuteQQuick3DTextureProviderExtensionCall9 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall9>(taken[9]);
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
      CuteQQuick3DTextureProviderExtensionCall10 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall10>(taken[10]);
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
      CuteQQuick3DTextureProviderExtensionCall11 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall11>(taken[11]);
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
      CuteQQuick3DTextureProviderExtensionCall12 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DTextureProviderExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuick3DTextureProviderExtension10metaObjectEv(
    const QQuick3DTextureProviderExtension *self) {
  return self->metaObject();
}

//  QString QQuick3DTextureProviderExtension::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuick3DTextureProviderExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DTextureProviderExtension::tr(s, c, n));
}

//  QQuick3DTextureProviderExtensionPrivate
//      *QQuick3DTextureProviderExtension::d_func()
extern "C" Q_DECL_EXPORT
QQuick3DTextureProviderExtensionPrivate *ritual_ZN32QQuick3DTextureProviderExtension6d_funcEv(
    QQuick3DTextureProviderExtension *self) {
  return self->d_func();
}

//  const QQuick3DTextureProviderExtensionPrivate
//      *QQuick3DTextureProviderExtension::d_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DTextureProviderExtensionPrivate *ritual_ZNK32QQuick3DTextureProviderExtension6d_funcEv(
    const QQuick3DTextureProviderExtension *self) {
  return self->d_func();
}

//  void QQuick3DTextureProviderExtension::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DTextureProviderExtension24qt_qmlMarker_uncreatableEv(
    QQuick3DTextureProviderExtension *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DTextureProviderExtension::QQuick3DTextureProviderExtension(QQuick
//      3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DTextureProviderExtension *ritual_ZN32QQuick3DTextureProviderExtensionC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DTextureProviderExtension(parent);
}

//  QQuick3DTextureProviderExtension::~QQuick3DTextureProviderExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DTextureProviderExtensionD1Ev(
    QQuick3DTextureProviderExtension *self) {
  delete self;
}

//  SamplerHint QQuick3DTextureProviderExtension::samplerHint() const
extern "C" Q_DECL_EXPORT
QQuick3DTextureProviderExtension::SamplerHint ritual_ZNK32QQuick3DTextureProviderExtension11samplerHintEv(
    const QQuick3DTextureProviderExtension *self) {
  return self->samplerHint();
}

//  void QQuick3DTextureProviderExtension::setSamplerHint(SamplerHint
//      newSamplerHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DTextureProviderExtension14setSamplerHintENS_11SamplerHintE(
    QQuick3DTextureProviderExtension *self,
    QQuick3DTextureProviderExtension::SamplerHint newSamplerHint) {
  self->setSamplerHint(newSamplerHint);
}

//  bool QQuick3DTextureProviderExtension::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QQuick3DTextureProviderExtension5eventEP6QEvent(
    QQuick3DTextureProviderExtension *self,
    QEvent *event) {
  return self->event(event);
}

//  QSSGRenderGraphObject *QQuick3DTextureProviderExtension::updateSpatialNod
//      e(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN32QQuick3DTextureProviderExtension17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DTextureProviderExtension *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  a Python function taken by a CuteQQuick3DTextureProviderExtension, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DTextureProviderExtension(
    QQuick3DTextureProviderExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DTextureProviderExtension *>(self)->take(key, call);
}

//  bool QQuick3DTextureProviderExtension::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN32QQuick3DTextureProviderExtension5eventEP6QEvent(
    QQuick3DTextureProviderExtension *self,
    QEvent *event) {
  return static_cast<OwnQQuick3DTextureProviderExtension *>(self)->OwnQQuick3DTextureProviderExtension::event(
      event);
}

//  QSSGRenderGraphObject *QQuick3DTextureProviderExtension::updateSpatialNod
//      e(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN32QQuick3DTextureProviderExtension17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DTextureProviderExtension *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DTextureProviderExtension *>(self)->OwnQQuick3DTextureProviderExtension::updateSpatialNode(
      node);
}
