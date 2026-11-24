//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/spheregeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/spheregeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A SphereGeometry that Python can take functions over in. Every SphereGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteSphereGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteSphereGeometryCall1)(const void *, int *);
typedef void (*CuteSphereGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteSphereGeometryCall3)(const void *, int *);
typedef void (*CuteSphereGeometryCall4)(const void *, int *);
typedef void (*CuteSphereGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSphereGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSphereGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSphereGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSphereGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSphereGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSphereGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSphereGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteSphereGeometry : public SphereGeometry {
public:
  using SphereGeometry::SphereGeometry;
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
  //      *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteSphereGeometryCall0 call = reinterpret_cast<CuteSphereGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteSphereGeometryCall1 call = reinterpret_cast<CuteSphereGeometryCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DGeometry::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteSphereGeometryCall2 call = reinterpret_cast<CuteSphereGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteSphereGeometryCall3 call = reinterpret_cast<CuteSphereGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteSphereGeometryCall4 call = reinterpret_cast<CuteSphereGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteSphereGeometryCall5 call = reinterpret_cast<CuteSphereGeometryCall5>(taken[5]);
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
      CuteSphereGeometryCall6 call = reinterpret_cast<CuteSphereGeometryCall6>(taken[6]);
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
      CuteSphereGeometryCall7 call = reinterpret_cast<CuteSphereGeometryCall7>(taken[7]);
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
      CuteSphereGeometryCall8 call = reinterpret_cast<CuteSphereGeometryCall8>(taken[8]);
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
      CuteSphereGeometryCall9 call = reinterpret_cast<CuteSphereGeometryCall9>(taken[9]);
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
      CuteSphereGeometryCall10 call = reinterpret_cast<CuteSphereGeometryCall10>(taken[10]);
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
      CuteSphereGeometryCall11 call = reinterpret_cast<CuteSphereGeometryCall11>(taken[11]);
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
      CuteSphereGeometryCall12 call = reinterpret_cast<CuteSphereGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *SphereGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14SphereGeometry10metaObjectEv(
    const SphereGeometry *self) {
  return self->metaObject();
}

//  QString SphereGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14SphereGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(SphereGeometry::tr(s, c, n));
}

//  SphereGeometry::SphereGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
SphereGeometry *ritual_ZN14SphereGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteSphereGeometry(parent);
}

//  SphereGeometry::~SphereGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometryD1Ev(SphereGeometry *self) {
  delete self;
}

//  float SphereGeometry::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14SphereGeometry6radiusEv(const SphereGeometry *self) {
  return self->radius();
}

//  void SphereGeometry::setRadius(float newRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometry9setRadiusEf(
    SphereGeometry *self,
    float newRadius) {
  self->setRadius(newRadius);
}

//  int SphereGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14SphereGeometry5ringsEv(const SphereGeometry *self) {
  return self->rings();
}

//  void SphereGeometry::setRings(int newRings)
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometry8setRingsEi(
    SphereGeometry *self,
    int newRings) {
  self->setRings(newRings);
}

//  int SphereGeometry::segments() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14SphereGeometry8segmentsEv(const SphereGeometry *self) {
  return self->segments();
}

//  void SphereGeometry::setSegments(int newSegments)
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometry11setSegmentsEi(
    SphereGeometry *self,
    int newSegments) {
  self->setSegments(newSegments);
}

//  bool SphereGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14SphereGeometry12asynchronousEv(const SphereGeometry *self) {
  return self->asynchronous();
}

//  void SphereGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometry15setAsynchronousEb(
    SphereGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status SphereGeometry::status() const
extern "C" Q_DECL_EXPORT
SphereGeometry::Status ritual_ZNK14SphereGeometry6statusEv(
    const SphereGeometry *self) {
  return self->status();
}

//  void SphereGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometry16doUpdateGeometryEv(SphereGeometry *self) {
  self->doUpdateGeometry();
}

//  void SphereGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometry15requestFinishedEv(SphereGeometry *self) {
  self->requestFinished();
}

//  void SphereGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14SphereGeometry22scheduleGeometryUpdateEv(
    SphereGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  a Python function taken by a CuteSphereGeometry, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SphereGeometry(
    SphereGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteSphereGeometry *>(self)->take(key, call);
}
