//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3dobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuick3DObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DObject : QQuick3DObject {
  using QQuick3DObject::updateSpatialNode;
  using QQuick3DObject::markAllDirty;
  using QQuick3DObject::itemChange;
  using QQuick3DObject::classBegin;
  using QQuick3DObject::componentComplete;
  using QQuick3DObject::preSync;
};

//  A QQuick3DObject that Python can take functions over in. Every QQuick3DObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DObjectCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DObjectCall1)(const void *, int *);
typedef void (*CuteQQuick3DObjectCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DObjectCall3)(const void *, int *);
typedef void (*CuteQQuick3DObjectCall4)(const void *, int *);
typedef void (*CuteQQuick3DObjectCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DObjectCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DObjectCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DObjectCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DObjectCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DObjectCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DObjectCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DObjectCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DObject : public QQuick3DObject {
public:
  using QQuick3DObject::QQuick3DObject;
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
  //      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DObjectCall0 call = reinterpret_cast<CuteQQuick3DObjectCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DObject::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DObjectCall1 call = reinterpret_cast<CuteQQuick3DObjectCall1>(taken[1]);
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
      CuteQQuick3DObjectCall2 call = reinterpret_cast<CuteQQuick3DObjectCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DObjectCall3 call = reinterpret_cast<CuteQQuick3DObjectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DObjectCall4 call = reinterpret_cast<CuteQQuick3DObjectCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DObjectCall5 call = reinterpret_cast<CuteQQuick3DObjectCall5>(taken[5]);
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
      CuteQQuick3DObjectCall6 call = reinterpret_cast<CuteQQuick3DObjectCall6>(taken[6]);
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
      CuteQQuick3DObjectCall7 call = reinterpret_cast<CuteQQuick3DObjectCall7>(taken[7]);
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
      CuteQQuick3DObjectCall8 call = reinterpret_cast<CuteQQuick3DObjectCall8>(taken[8]);
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
      CuteQQuick3DObjectCall9 call = reinterpret_cast<CuteQQuick3DObjectCall9>(taken[9]);
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
      CuteQQuick3DObjectCall10 call = reinterpret_cast<CuteQQuick3DObjectCall10>(taken[10]);
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
      CuteQQuick3DObjectCall11 call = reinterpret_cast<CuteQQuick3DObjectCall11>(taken[11]);
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
      CuteQQuick3DObjectCall12 call = reinterpret_cast<CuteQQuick3DObjectCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuick3DObject10metaObjectEv(
    const QQuick3DObject *self) {
  return self->metaObject();
}

//  void *QQuick3DObject::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuick3DObject11qt_metacastEPKc(
    QQuick3DObject *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DObject::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuick3DObject11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DObject *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuick3DObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DObject::tr(s, c, n));
}

//  QQuick3DObjectPrivate *QQuick3DObject::d_func()
extern "C" Q_DECL_EXPORT
QQuick3DObjectPrivate *ritual_ZN14QQuick3DObject6d_funcEv(
    QQuick3DObject *self) {
  return self->d_func();
}

//  const QQuick3DObjectPrivate *QQuick3DObject::d_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DObjectPrivate *ritual_ZNK14QQuick3DObject6d_funcEv(
    const QQuick3DObject *self) {
  return self->d_func();
}

//  void QQuick3DObject::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject24qt_qmlMarker_uncreatableEv(
    QQuick3DObject *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DObject::QQuick3DObject(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZN14QQuick3DObjectC1EPS_(QQuick3DObject *parent) {
  return new CuteQQuick3DObject(parent);
}

//  QQuick3DObject::~QQuick3DObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObjectD1Ev(QQuick3DObject *self) {
  delete self;
}

//  QString QQuick3DObject::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuick3DObject5stateEv(const QQuick3DObject *self) {
  return new QString(self->state());
}

//  void QQuick3DObject::setState(const QString &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject8setStateERK7QString(
    QQuick3DObject *self,
    const QString *state) {
  self->setState(*state);
}

//  QList<QQuick3DObject *> QQuick3DObject::childItems() const
extern "C" Q_DECL_EXPORT
QList<QQuick3DObject *> *ritual_ZNK14QQuick3DObject10childItemsEv(
    const QQuick3DObject *self) {
  return new QList<QQuick3DObject *>(self->childItems());
}

//  QQuick3DObject *QQuick3DObject::parentItem() const
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZNK14QQuick3DObject10parentItemEv(
    const QQuick3DObject *self) {
  return self->parentItem();
}

//  void QQuick3DObject::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject6updateEv(QQuick3DObject *self) {
  self->update();
}

//  void QQuick3DObject::setParentItem(QQuick3DObject *parentItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject13setParentItemEPS_(
    QQuick3DObject *self,
    QQuick3DObject *parentItem) {
  self->setParentItem(parentItem);
}

//  void QQuick3DObject::parentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject13parentChangedEv(QQuick3DObject *self) {
  self->parentChanged();
}

//  void QQuick3DObject::childrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject15childrenChangedEv(QQuick3DObject *self) {
  self->childrenChanged();
}

//  void QQuick3DObject::stateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject12stateChangedEv(QQuick3DObject *self) {
  self->stateChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DObject *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DObject::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject12markAllDirtyEv(QQuick3DObject *self) {
  self->markAllDirty();
}

//  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE(
    QQuick3DObject *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  QQuick3DObject::QQuick3DObject(QQuick3DObjectPrivate &dd, QQuick3DObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZN14QQuick3DObjectC1ER21QQuick3DObjectPrivatePS_(
    QQuick3DObjectPrivate *dd,
    QQuick3DObject *parent) {
  return new CuteQQuick3DObject(*dd, parent);
}

//  void QQuick3DObject::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject10classBeginEv(QQuick3DObject *self) {
  self->classBegin();
}

//  void QQuick3DObject::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject17componentCompleteEv(QQuick3DObject *self) {
  self->componentComplete();
}

//  bool QQuick3DObject::isComponentComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DObject19isComponentCompleteEv(
    const QQuick3DObject *self) {
  return self->isComponentComplete();
}

//  void QQuick3DObject::preSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject7preSyncEv(QQuick3DObject *self) {
  self->preSync();
}

//  QQuick3DObject as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuick3DObject_QQmlParserStatus(
    QQuick3DObject *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuick3DObject, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DObject(
    QQuick3DObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DObject *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DObject *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DObject *>(self)->OwnQQuick3DObject::updateSpatialNode(
      node);
}

//  void QQuick3DObject::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DObject12markAllDirtyEv(QQuick3DObject *self) {
  static_cast<OwnQQuick3DObject *>(self)->OwnQQuick3DObject::markAllDirty();
}

//  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE(
    QQuick3DObject *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DObject *>(self)->OwnQQuick3DObject::itemChange(
      a0,
      *a1);
}

//  void QQuick3DObject::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DObject10classBeginEv(QQuick3DObject *self) {
  static_cast<OwnQQuick3DObject *>(self)->OwnQQuick3DObject::classBegin();
}

//  void QQuick3DObject::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DObject17componentCompleteEv(
    QQuick3DObject *self) {
  static_cast<OwnQQuick3DObject *>(self)->OwnQQuick3DObject::componentComplete();
}

//  void QQuick3DObject::preSync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DObject7preSyncEv(QQuick3DObject *self) {
  static_cast<OwnQQuick3DObject *>(self)->OwnQQuick3DObject::preSync();
}

//  QList<QQuick3DObject *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuick3DObject *> *ritual_list_make_QQuick3DObject_ptr() {
  return new QList<QQuick3DObject *>();
}

//  void QList<QQuick3DObject *>::append(const QQuick3DObject * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuick3DObject_ptr(
    QList<QQuick3DObject *> *self,
    QQuick3DObject *element) {
  self->append(element);
}

//  qsizetype QList<QQuick3DObject *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuick3DObject_ptr(
    const QList<QQuick3DObject *> *self) {
  return self->size();
}

//  const QQuick3DObject * &QList<QQuick3DObject *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_list_at_QQuick3DObject_ptr(
    const QList<QQuick3DObject *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuick3DObject *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuick3DObject_ptr(QList<QQuick3DObject *> *self) {
  delete self;
}
