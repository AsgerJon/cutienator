//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QQuick3DInstanceList that Python can take functions over in. Every QQuick3DInstanceList
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DInstanceListCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DInstanceListCall1)(const void *, int *);
typedef void (*CuteQQuick3DInstanceListCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DInstanceListCall3)(const void *, int *);
typedef void (*CuteQQuick3DInstanceListCall4)(const void *, int *);
typedef void (*CuteQQuick3DInstanceListCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstanceListCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstanceListCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DInstanceList : public QQuick3DInstanceList {
public:
  using QQuick3DInstanceList::QQuick3DInstanceList;
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
  //      *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DInstanceListCall0 call = reinterpret_cast<CuteQQuick3DInstanceListCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DInstancing::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DInstanceListCall1 call = reinterpret_cast<CuteQQuick3DInstanceListCall1>(taken[1]);
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
      CuteQQuick3DInstanceListCall2 call = reinterpret_cast<CuteQQuick3DInstanceListCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DInstanceListCall3 call = reinterpret_cast<CuteQQuick3DInstanceListCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DInstanceListCall4 call = reinterpret_cast<CuteQQuick3DInstanceListCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DInstanceListCall5 call = reinterpret_cast<CuteQQuick3DInstanceListCall5>(taken[5]);
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
      CuteQQuick3DInstanceListCall6 call = reinterpret_cast<CuteQQuick3DInstanceListCall6>(taken[6]);
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
      CuteQQuick3DInstanceListCall7 call = reinterpret_cast<CuteQQuick3DInstanceListCall7>(taken[7]);
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
      CuteQQuick3DInstanceListCall8 call = reinterpret_cast<CuteQQuick3DInstanceListCall8>(taken[8]);
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
      CuteQQuick3DInstanceListCall9 call = reinterpret_cast<CuteQQuick3DInstanceListCall9>(taken[9]);
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
      CuteQQuick3DInstanceListCall10 call = reinterpret_cast<CuteQQuick3DInstanceListCall10>(taken[10]);
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
      CuteQQuick3DInstanceListCall11 call = reinterpret_cast<CuteQQuick3DInstanceListCall11>(taken[11]);
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
      CuteQQuick3DInstanceListCall12 call = reinterpret_cast<CuteQQuick3DInstanceListCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DInstanceList::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuick3DInstanceList10metaObjectEv(
    const QQuick3DInstanceList *self) {
  return self->metaObject();
}

//  void *QQuick3DInstanceList::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuick3DInstanceList11qt_metacastEPKc(
    QQuick3DInstanceList *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DInstanceList::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuick3DInstanceList11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DInstanceList *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DInstanceList::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuick3DInstanceList2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DInstanceList::tr(s, c, n));
}

//  QQuick3DInstanceList::QQuick3DInstanceList(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DInstanceList *ritual_ZN20QQuick3DInstanceListC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DInstanceList(parent);
}

//  QQuick3DInstanceList::~QQuick3DInstanceList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInstanceListD1Ev(QQuick3DInstanceList *self) {
  delete self;
}

//  QByteArray QQuick3DInstanceList::getInstanceBuffer(int *instanceCount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN20QQuick3DInstanceList17getInstanceBufferEPi(
    QQuick3DInstanceList *self,
    int *instanceCount) {
  return new QByteArray(self->getInstanceBuffer(instanceCount));
}

//  QQmlListProperty<QQuick3DInstanceListEntry>
//      QQuick3DInstanceList::instances()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DInstanceListEntry> *ritual_ZN20QQuick3DInstanceList9instancesEv(
    QQuick3DInstanceList *self) {
  return new QQmlListProperty<QQuick3DInstanceListEntry>(self->instances());
}

//  int QQuick3DInstanceList::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuick3DInstanceList13instanceCountEv(
    const QQuick3DInstanceList *self) {
  return self->instanceCount();
}

//  void QQuick3DInstanceList::instanceCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInstanceList20instanceCountChangedEv(
    QQuick3DInstanceList *self) {
  self->instanceCountChanged();
}

//  void QQuick3DInstanceList::handleInstanceChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInstanceList20handleInstanceChangeEv(
    QQuick3DInstanceList *self) {
  self->handleInstanceChange();
}

//  void QQuick3DInstanceList::onInstanceDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInstanceList19onInstanceDestroyedEP7QObject(
    QQuick3DInstanceList *self,
    QObject *object) {
  self->onInstanceDestroyed(object);
}

//  void QQuick3DInstanceList::generateInstanceData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInstanceList20generateInstanceDataEv(
    QQuick3DInstanceList *self) {
  self->generateInstanceData();
}

//  void QQuick3DInstanceList::qmlAppendInstanceListEntry(QQmlListProperty<QQ
//      uick3DInstanceListEntry> *list, QQuick3DInstanceListEntry *material)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInstanceList26qmlAppendInstanceListEntryEP16QQmlListPropertyI25QQuick3DInstanceListEntryEPS1_(
    QQmlListProperty<QQuick3DInstanceListEntry> *list,
    QQuick3DInstanceListEntry *material) {
  QQuick3DInstanceList::qmlAppendInstanceListEntry(list, material);
}

//  QQuick3DInstanceListEntry *QQuick3DInstanceList::qmlInstanceListEntryAt(Q
//      QmlListProperty<QQuick3DInstanceListEntry> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DInstanceListEntry *ritual_ZN20QQuick3DInstanceList22qmlInstanceListEntryAtEP16QQmlListPropertyI25QQuick3DInstanceListEntryEx(
    QQmlListProperty<QQuick3DInstanceListEntry> *list,
    qsizetype index) {
  return QQuick3DInstanceList::qmlInstanceListEntryAt(list, index);
}

//  qsizetype QQuick3DInstanceList::qmlInstanceListEntriesCount(QQmlListPrope
//      rty<QQuick3DInstanceListEntry> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QQuick3DInstanceList27qmlInstanceListEntriesCountEP16QQmlListPropertyI25QQuick3DInstanceListEntryE(
    QQmlListProperty<QQuick3DInstanceListEntry> *list) {
  return QQuick3DInstanceList::qmlInstanceListEntriesCount(list);
}

//  void QQuick3DInstanceList::qmlClearInstanceListEntries(QQmlListProperty<Q
//      Quick3DInstanceListEntry> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInstanceList27qmlClearInstanceListEntriesEP16QQmlListPropertyI25QQuick3DInstanceListEntryE(
    QQmlListProperty<QQuick3DInstanceListEntry> *list) {
  QQuick3DInstanceList::qmlClearInstanceListEntries(list);
}

//  a Python function taken by a CuteQQuick3DInstanceList, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DInstanceList(
    QQuick3DInstanceList *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DInstanceList *>(self)->take(key, call);
}

//  a QQmlListProperty<QQuick3DInstanceListEntry> a ritual of
//      QQuick3DInstanceList gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DInstanceList__QQmlListProperty_QQuick3DInstanceListEntry(
    QQmlListProperty<QQuick3DInstanceListEntry> *self) {
  delete self;
}
