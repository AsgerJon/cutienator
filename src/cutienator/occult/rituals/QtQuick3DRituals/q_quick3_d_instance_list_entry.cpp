//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qcolor.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DInstanceListEntry may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DInstanceListEntry : QQuick3DInstanceListEntry {
  using QQuick3DInstanceListEntry::updateSpatialNode;
};

//  A QQuick3DInstanceListEntry that Python can take functions over in. Every QQuick3DInstanceListEntry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DInstanceListEntryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DInstanceListEntryCall1)(const void *, int *);
typedef void (*CuteQQuick3DInstanceListEntryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DInstanceListEntryCall3)(const void *, int *);
typedef void (*CuteQQuick3DInstanceListEntryCall4)(const void *, int *);
typedef void (*CuteQQuick3DInstanceListEntryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstanceListEntryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstanceListEntryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListEntryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListEntryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListEntryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListEntryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceListEntryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DInstanceListEntry : public QQuick3DInstanceListEntry {
public:
  using QQuick3DInstanceListEntry::QQuick3DInstanceListEntry;
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
  //      *QQuick3DInstanceListEntry::updateSpatialNode(QSSGRenderGraphObje
  //      ct *a0)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DInstanceListEntryCall0 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DInstanceListEntry::updateSpatialNode(a0);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DInstanceListEntryCall1 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall1>(taken[1]);
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
      CuteQQuick3DInstanceListEntryCall2 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DInstanceListEntryCall3 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DInstanceListEntryCall4 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DInstanceListEntryCall5 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall5>(taken[5]);
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
      CuteQQuick3DInstanceListEntryCall6 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall6>(taken[6]);
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
      CuteQQuick3DInstanceListEntryCall7 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall7>(taken[7]);
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
      CuteQQuick3DInstanceListEntryCall8 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall8>(taken[8]);
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
      CuteQQuick3DInstanceListEntryCall9 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall9>(taken[9]);
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
      CuteQQuick3DInstanceListEntryCall10 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall10>(taken[10]);
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
      CuteQQuick3DInstanceListEntryCall11 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall11>(taken[11]);
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
      CuteQQuick3DInstanceListEntryCall12 call = reinterpret_cast<CuteQQuick3DInstanceListEntryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DInstanceListEntry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuick3DInstanceListEntry10metaObjectEv(
    const QQuick3DInstanceListEntry *self) {
  return self->metaObject();
}

//  void *QQuick3DInstanceListEntry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuick3DInstanceListEntry11qt_metacastEPKc(
    QQuick3DInstanceListEntry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DInstanceListEntry::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuick3DInstanceListEntry11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DInstanceListEntry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DInstanceListEntry::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuick3DInstanceListEntry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DInstanceListEntry::tr(s, c, n));
}

//  QQuick3DInstanceListEntry::QQuick3DInstanceListEntry(QQuick3DObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DInstanceListEntry *ritual_ZN25QQuick3DInstanceListEntryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DInstanceListEntry(parent);
}

//  QQuick3DInstanceListEntry::~QQuick3DInstanceListEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntryD1Ev(
    QQuick3DInstanceListEntry *self) {
  delete self;
}

//  QVector3D QQuick3DInstanceListEntry::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK25QQuick3DInstanceListEntry8positionEv(
    const QQuick3DInstanceListEntry *self) {
  return new QVector3D(self->position());
}

//  QVector3D QQuick3DInstanceListEntry::scale() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK25QQuick3DInstanceListEntry5scaleEv(
    const QQuick3DInstanceListEntry *self) {
  return new QVector3D(self->scale());
}

//  QVector3D QQuick3DInstanceListEntry::eulerRotation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK25QQuick3DInstanceListEntry13eulerRotationEv(
    const QQuick3DInstanceListEntry *self) {
  return new QVector3D(self->eulerRotation());
}

//  QQuaternion QQuick3DInstanceListEntry::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuick3DInstanceListEntry8rotationEv(
    const QQuick3DInstanceListEntry *self) {
  return new QQuaternion(self->rotation());
}

//  QColor QQuick3DInstanceListEntry::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuick3DInstanceListEntry5colorEv(
    const QQuick3DInstanceListEntry *self) {
  return new QColor(self->color());
}

//  QVector4D QQuick3DInstanceListEntry::customData() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK25QQuick3DInstanceListEntry10customDataEv(
    const QQuick3DInstanceListEntry *self) {
  return new QVector4D(self->customData());
}

//  void QQuick3DInstanceListEntry::setPosition(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry11setPositionE9QVector3D(
    QQuick3DInstanceListEntry *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  void QQuick3DInstanceListEntry::setScale(QVector3D scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry8setScaleE9QVector3D(
    QQuick3DInstanceListEntry *self,
    const QVector3D *scale) {
  self->setScale(*scale);
}

//  void QQuick3DInstanceListEntry::setEulerRotation(QVector3D eulerRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry16setEulerRotationE9QVector3D(
    QQuick3DInstanceListEntry *self,
    const QVector3D *eulerRotation) {
  self->setEulerRotation(*eulerRotation);
}

//  void QQuick3DInstanceListEntry::setRotation(QQuaternion rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry11setRotationE11QQuaternion(
    QQuick3DInstanceListEntry *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}

//  void QQuick3DInstanceListEntry::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry8setColorE6QColor(
    QQuick3DInstanceListEntry *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuick3DInstanceListEntry::setCustomData(QVector4D customData)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry13setCustomDataE9QVector4D(
    QQuick3DInstanceListEntry *self,
    const QVector4D *customData) {
  self->setCustomData(*customData);
}

//  void QQuick3DInstanceListEntry::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry15positionChangedEv(
    QQuick3DInstanceListEntry *self) {
  self->positionChanged();
}

//  void QQuick3DInstanceListEntry::scaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry12scaleChangedEv(
    QQuick3DInstanceListEntry *self) {
  self->scaleChanged();
}

//  void QQuick3DInstanceListEntry::eulerRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry20eulerRotationChangedEv(
    QQuick3DInstanceListEntry *self) {
  self->eulerRotationChanged();
}

//  void QQuick3DInstanceListEntry::rotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry15rotationChangedEv(
    QQuick3DInstanceListEntry *self) {
  self->rotationChanged();
}

//  void QQuick3DInstanceListEntry::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry12colorChangedEv(
    QQuick3DInstanceListEntry *self) {
  self->colorChanged();
}

//  void QQuick3DInstanceListEntry::customDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry17customDataChangedEv(
    QQuick3DInstanceListEntry *self) {
  self->customDataChanged();
}

//  void QQuick3DInstanceListEntry::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DInstanceListEntry7changedEv(
    QQuick3DInstanceListEntry *self) {
  self->changed();
}

//  QSSGRenderGraphObject
//      *QQuick3DInstanceListEntry::updateSpatialNode(QSSGRenderGraphObject
//      *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN25QQuick3DInstanceListEntry17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DInstanceListEntry *self,
    QSSGRenderGraphObject *a0) {
  return self->updateSpatialNode(a0);
}

//  a Python function taken by a CuteQQuick3DInstanceListEntry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DInstanceListEntry(
    QQuick3DInstanceListEntry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DInstanceListEntry *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DInstanceListEntry::updateSpatialNode(QSSGRenderGraphObject
//      *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN25QQuick3DInstanceListEntry17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DInstanceListEntry *self,
    QSSGRenderGraphObject *a0) {
  return static_cast<OwnQQuick3DInstanceListEntry *>(self)->OwnQQuick3DInstanceListEntry::updateSpatialNode(
      a0);
}
