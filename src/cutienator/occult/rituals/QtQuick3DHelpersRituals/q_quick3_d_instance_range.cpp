//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/randominstancing_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/randominstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DInstanceRange may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DInstanceRange : QQuick3DInstanceRange {
  using QQuick3DInstanceRange::updateSpatialNode;
};

//  A QQuick3DInstanceRange that Python can take functions over in. Every QQuick3DInstanceRange
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DInstanceRangeCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DInstanceRangeCall1)(const void *, int *);
typedef void (*CuteQQuick3DInstanceRangeCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DInstanceRangeCall3)(const void *, int *);
typedef void (*CuteQQuick3DInstanceRangeCall4)(const void *, int *);
typedef void (*CuteQQuick3DInstanceRangeCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstanceRangeCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstanceRangeCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceRangeCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceRangeCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceRangeCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceRangeCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstanceRangeCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DInstanceRange : public QQuick3DInstanceRange {
public:
  using QQuick3DInstanceRange::QQuick3DInstanceRange;
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
  //      *QQuick3DInstanceRange::updateSpatialNode(QSSGRenderGraphObject
  //      *a0)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DInstanceRangeCall0 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DInstanceRange::updateSpatialNode(a0);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DInstanceRangeCall1 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall1>(taken[1]);
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
      CuteQQuick3DInstanceRangeCall2 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DInstanceRangeCall3 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DInstanceRangeCall4 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DInstanceRangeCall5 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall5>(taken[5]);
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
      CuteQQuick3DInstanceRangeCall6 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall6>(taken[6]);
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
      CuteQQuick3DInstanceRangeCall7 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall7>(taken[7]);
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
      CuteQQuick3DInstanceRangeCall8 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall8>(taken[8]);
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
      CuteQQuick3DInstanceRangeCall9 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall9>(taken[9]);
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
      CuteQQuick3DInstanceRangeCall10 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall10>(taken[10]);
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
      CuteQQuick3DInstanceRangeCall11 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall11>(taken[11]);
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
      CuteQQuick3DInstanceRangeCall12 call = reinterpret_cast<CuteQQuick3DInstanceRangeCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DInstanceRange::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DInstanceRange10metaObjectEv(
    const QQuick3DInstanceRange *self) {
  return self->metaObject();
}

//  void *QQuick3DInstanceRange::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuick3DInstanceRange11qt_metacastEPKc(
    QQuick3DInstanceRange *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DInstanceRange::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuick3DInstanceRange11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DInstanceRange *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DInstanceRange::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DInstanceRange2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DInstanceRange::tr(s, c, n));
}

//  QQuick3DInstanceRange::QQuick3DInstanceRange(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DInstanceRange *ritual_ZN21QQuick3DInstanceRangeC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DInstanceRange(parent);
}

//  QQuick3DInstanceRange::~QQuick3DInstanceRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRangeD1Ev(QQuick3DInstanceRange *self) {
  delete self;
}

//  QVariant QQuick3DInstanceRange::from() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuick3DInstanceRange4fromEv(
    const QQuick3DInstanceRange *self) {
  return new QVariant(self->from());
}

//  QVariant QQuick3DInstanceRange::to() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuick3DInstanceRange2toEv(
    const QQuick3DInstanceRange *self) {
  return new QVariant(self->to());
}

//  bool QQuick3DInstanceRange::proportional() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DInstanceRange12proportionalEv(
    const QQuick3DInstanceRange *self) {
  return self->proportional();
}

//  void QQuick3DInstanceRange::setFrom(QVariant from)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRange7setFromE8QVariant(
    QQuick3DInstanceRange *self,
    const QVariant *from) {
  self->setFrom(*from);
}

//  void QQuick3DInstanceRange::setTo(QVariant to)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRange5setToE8QVariant(
    QQuick3DInstanceRange *self,
    const QVariant *to) {
  self->setTo(*to);
}

//  void QQuick3DInstanceRange::setProportional(bool proportional)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRange15setProportionalEb(
    QQuick3DInstanceRange *self,
    bool proportional) {
  self->setProportional(proportional);
}

//  void QQuick3DInstanceRange::fromChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRange11fromChangedEv(
    QQuick3DInstanceRange *self) {
  self->fromChanged();
}

//  void QQuick3DInstanceRange::toChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRange9toChangedEv(
    QQuick3DInstanceRange *self) {
  self->toChanged();
}

//  void QQuick3DInstanceRange::proportionalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRange19proportionalChangedEv(
    QQuick3DInstanceRange *self) {
  self->proportionalChanged();
}

//  void QQuick3DInstanceRange::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DInstanceRange7changedEv(
    QQuick3DInstanceRange *self) {
  self->changed();
}

//  QSSGRenderGraphObject
//      *QQuick3DInstanceRange::updateSpatialNode(QSSGRenderGraphObject *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QQuick3DInstanceRange17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DInstanceRange *self,
    QSSGRenderGraphObject *a0) {
  return self->updateSpatialNode(a0);
}

//  a Python function taken by a CuteQQuick3DInstanceRange, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DInstanceRange(
    QQuick3DInstanceRange *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DInstanceRange *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DInstanceRange::updateSpatialNode(QSSGRenderGraphObject *a0)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN21QQuick3DInstanceRange17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DInstanceRange *self,
    QSSGRenderGraphObject *a0) {
  return static_cast<OwnQQuick3DInstanceRange *>(self)->OwnQQuick3DInstanceRange::updateSpatialNode(
      a0);
}
