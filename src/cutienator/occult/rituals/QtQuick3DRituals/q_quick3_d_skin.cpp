//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dskin_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dskin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QQuick3DSkin that Python can take functions over in. Every QQuick3DSkin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DSkinCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DSkinCall1)(const void *, int *);
typedef void (*CuteQQuick3DSkinCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DSkinCall3)(const void *, int *);
typedef void (*CuteQQuick3DSkinCall4)(const void *, int *);
typedef void (*CuteQQuick3DSkinCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSkinCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSkinCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSkinCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSkinCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSkinCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSkinCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSkinCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DSkin : public QQuick3DSkin {
public:
  using QQuick3DSkin::QQuick3DSkin;
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
  //      *QQuick3DSkin::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DSkinCall0 call = reinterpret_cast<CuteQQuick3DSkinCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DSkin::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DSkinCall1 call = reinterpret_cast<CuteQQuick3DSkinCall1>(taken[1]);
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
      CuteQQuick3DSkinCall2 call = reinterpret_cast<CuteQQuick3DSkinCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DSkinCall3 call = reinterpret_cast<CuteQQuick3DSkinCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DSkinCall4 call = reinterpret_cast<CuteQQuick3DSkinCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DSkinCall5 call = reinterpret_cast<CuteQQuick3DSkinCall5>(taken[5]);
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
      CuteQQuick3DSkinCall6 call = reinterpret_cast<CuteQQuick3DSkinCall6>(taken[6]);
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
      CuteQQuick3DSkinCall7 call = reinterpret_cast<CuteQQuick3DSkinCall7>(taken[7]);
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
      CuteQQuick3DSkinCall8 call = reinterpret_cast<CuteQQuick3DSkinCall8>(taken[8]);
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
      CuteQQuick3DSkinCall9 call = reinterpret_cast<CuteQQuick3DSkinCall9>(taken[9]);
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
      CuteQQuick3DSkinCall10 call = reinterpret_cast<CuteQQuick3DSkinCall10>(taken[10]);
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
      CuteQQuick3DSkinCall11 call = reinterpret_cast<CuteQQuick3DSkinCall11>(taken[11]);
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
      CuteQQuick3DSkinCall12 call = reinterpret_cast<CuteQQuick3DSkinCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DSkin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuick3DSkin10metaObjectEv(
    const QQuick3DSkin *self) {
  return self->metaObject();
}

//  void *QQuick3DSkin::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuick3DSkin11qt_metacastEPKc(
    QQuick3DSkin *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DSkin::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuick3DSkin11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DSkin *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DSkin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuick3DSkin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DSkin::tr(s, c, n));
}

//  QQuick3DSkin::QQuick3DSkin(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DSkin *ritual_ZN12QQuick3DSkinC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DSkin(parent);
}

//  QQuick3DSkin::~QQuick3DSkin()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DSkinD1Ev(QQuick3DSkin *self) {
  delete self;
}

//  QQmlListProperty<QQuick3DNode> QQuick3DSkin::joints()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DNode> *ritual_ZN12QQuick3DSkin6jointsEv(
    QQuick3DSkin *self) {
  return new QQmlListProperty<QQuick3DNode>(self->joints());
}

//  QList<QMatrix4x4> QQuick3DSkin::inverseBindPoses() const
extern "C" Q_DECL_EXPORT
QList<QMatrix4x4> *ritual_ZNK12QQuick3DSkin16inverseBindPosesEv(
    const QQuick3DSkin *self) {
  return new QList<QMatrix4x4>(self->inverseBindPoses());
}

//  void QQuick3DSkin::setInverseBindPoses(const QList<QMatrix4x4> &poses)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DSkin19setInverseBindPosesERK5QListI10QMatrix4x4E(
    QQuick3DSkin *self,
    const QList<QMatrix4x4> *poses) {
  self->setInverseBindPoses(*poses);
}

//  void QQuick3DSkin::inverseBindPosesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DSkin23inverseBindPosesChangedEv(QQuick3DSkin *self) {
  self->inverseBindPosesChanged();
}

//  void QQuick3DSkin::qmlAppendJoint(QQmlListProperty<QQuick3DNode> *list,
//      QQuick3DNode *joint)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DSkin14qmlAppendJointEP16QQmlListPropertyI12QQuick3DNodeEPS1_(
    QQmlListProperty<QQuick3DNode> *list,
    QQuick3DNode *joint) {
  QQuick3DSkin::qmlAppendJoint(list, joint);
}

//  QQuick3DNode *QQuick3DSkin::qmlJointAt(QQmlListProperty<QQuick3DNode>
//      *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN12QQuick3DSkin10qmlJointAtEP16QQmlListPropertyI12QQuick3DNodeEx(
    QQmlListProperty<QQuick3DNode> *list,
    qsizetype index) {
  return QQuick3DSkin::qmlJointAt(list, index);
}

//  qsizetype QQuick3DSkin::qmlJointsCount(QQmlListProperty<QQuick3DNode>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN12QQuick3DSkin14qmlJointsCountEP16QQmlListPropertyI12QQuick3DNodeE(
    QQmlListProperty<QQuick3DNode> *list) {
  return QQuick3DSkin::qmlJointsCount(list);
}

//  void QQuick3DSkin::qmlClearJoints(QQmlListProperty<QQuick3DNode> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DSkin14qmlClearJointsEP16QQmlListPropertyI12QQuick3DNodeE(
    QQmlListProperty<QQuick3DNode> *list) {
  QQuick3DSkin::qmlClearJoints(list);
}

//  QSSGRenderGraphObject
//      *QQuick3DSkin::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN12QQuick3DSkin17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSkin *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  a Python function taken by a CuteQQuick3DSkin, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DSkin(
    QQuick3DSkin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DSkin *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DSkin::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN12QQuick3DSkin17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSkin *self,
    QSSGRenderGraphObject *node) {
  return self->QQuick3DSkin::updateSpatialNode(node);
}

//  a QQmlListProperty<QQuick3DNode> a ritual of QQuick3DSkin gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DSkin__QQmlListProperty_QQuick3DNode(
    QQmlListProperty<QQuick3DNode> *self) {
  delete self;
}
