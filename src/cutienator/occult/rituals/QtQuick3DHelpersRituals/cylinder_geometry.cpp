//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/cylindergeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/cylindergeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A CylinderGeometry that Python can take functions over in. Every CylinderGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteCylinderGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteCylinderGeometryCall1)(const void *, int *);
typedef void (*CuteCylinderGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteCylinderGeometryCall3)(const void *, int *);
typedef void (*CuteCylinderGeometryCall4)(const void *, int *);
typedef void (*CuteCylinderGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCylinderGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCylinderGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCylinderGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCylinderGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCylinderGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCylinderGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCylinderGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteCylinderGeometry : public CylinderGeometry {
public:
  using CylinderGeometry::CylinderGeometry;
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
      CuteCylinderGeometryCall0 call = reinterpret_cast<CuteCylinderGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteCylinderGeometryCall1 call = reinterpret_cast<CuteCylinderGeometryCall1>(taken[1]);
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
      CuteCylinderGeometryCall2 call = reinterpret_cast<CuteCylinderGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteCylinderGeometryCall3 call = reinterpret_cast<CuteCylinderGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteCylinderGeometryCall4 call = reinterpret_cast<CuteCylinderGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteCylinderGeometryCall5 call = reinterpret_cast<CuteCylinderGeometryCall5>(taken[5]);
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
      CuteCylinderGeometryCall6 call = reinterpret_cast<CuteCylinderGeometryCall6>(taken[6]);
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
      CuteCylinderGeometryCall7 call = reinterpret_cast<CuteCylinderGeometryCall7>(taken[7]);
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
      CuteCylinderGeometryCall8 call = reinterpret_cast<CuteCylinderGeometryCall8>(taken[8]);
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
      CuteCylinderGeometryCall9 call = reinterpret_cast<CuteCylinderGeometryCall9>(taken[9]);
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
      CuteCylinderGeometryCall10 call = reinterpret_cast<CuteCylinderGeometryCall10>(taken[10]);
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
      CuteCylinderGeometryCall11 call = reinterpret_cast<CuteCylinderGeometryCall11>(taken[11]);
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
      CuteCylinderGeometryCall12 call = reinterpret_cast<CuteCylinderGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *CylinderGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16CylinderGeometry10metaObjectEv(
    const CylinderGeometry *self) {
  return self->metaObject();
}

//  void *CylinderGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16CylinderGeometry11qt_metacastEPKc(
    CylinderGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int CylinderGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16CylinderGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    CylinderGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString CylinderGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16CylinderGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(CylinderGeometry::tr(s, c, n));
}

//  CylinderGeometry::CylinderGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
CylinderGeometry *ritual_ZN16CylinderGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteCylinderGeometry(parent);
}

//  CylinderGeometry::~CylinderGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometryD1Ev(CylinderGeometry *self) {
  delete self;
}

//  float CylinderGeometry::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16CylinderGeometry6radiusEv(const CylinderGeometry *self) {
  return self->radius();
}

//  void CylinderGeometry::setRadius(float newRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry9setRadiusEf(
    CylinderGeometry *self,
    float newRadius) {
  self->setRadius(newRadius);
}

//  float CylinderGeometry::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16CylinderGeometry6lengthEv(const CylinderGeometry *self) {
  return self->length();
}

//  void CylinderGeometry::setLength(float newLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry9setLengthEf(
    CylinderGeometry *self,
    float newLength) {
  self->setLength(newLength);
}

//  int CylinderGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CylinderGeometry5ringsEv(const CylinderGeometry *self) {
  return self->rings();
}

//  void CylinderGeometry::setRings(int newRings)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry8setRingsEi(
    CylinderGeometry *self,
    int newRings) {
  self->setRings(newRings);
}

//  int CylinderGeometry::segments() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CylinderGeometry8segmentsEv(const CylinderGeometry *self) {
  return self->segments();
}

//  void CylinderGeometry::setSegments(int newSegments)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry11setSegmentsEi(
    CylinderGeometry *self,
    int newSegments) {
  self->setSegments(newSegments);
}

//  bool CylinderGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CylinderGeometry12asynchronousEv(
    const CylinderGeometry *self) {
  return self->asynchronous();
}

//  void CylinderGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry15setAsynchronousEb(
    CylinderGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status CylinderGeometry::status() const
extern "C" Q_DECL_EXPORT
CylinderGeometry::Status ritual_ZNK16CylinderGeometry6statusEv(
    const CylinderGeometry *self) {
  return self->status();
}

//  void CylinderGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry16doUpdateGeometryEv(
    CylinderGeometry *self) {
  self->doUpdateGeometry();
}

//  void CylinderGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry15requestFinishedEv(CylinderGeometry *self) {
  self->requestFinished();
}

//  void CylinderGeometry::radiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry13radiusChangedEv(CylinderGeometry *self) {
  self->radiusChanged();
}

//  void CylinderGeometry::lengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry13lengthChangedEv(CylinderGeometry *self) {
  self->lengthChanged();
}

//  void CylinderGeometry::ringsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry12ringsChangedEv(CylinderGeometry *self) {
  self->ringsChanged();
}

//  void CylinderGeometry::segmentsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry15segmentsChangedEv(CylinderGeometry *self) {
  self->segmentsChanged();
}

//  void CylinderGeometry::asynchronousChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry19asynchronousChangedEv(
    CylinderGeometry *self) {
  self->asynchronousChanged();
}

//  void CylinderGeometry::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry13statusChangedEv(CylinderGeometry *self) {
  self->statusChanged();
}

//  void CylinderGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry22scheduleGeometryUpdateEv(
    CylinderGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  void CylinderGeometry::updateGeometry(const GeometryData &geometryData)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry14updateGeometryERKNS_12GeometryDataE(
    CylinderGeometry *self,
    const CylinderGeometry::GeometryData *geometryData) {
  self->updateGeometry(*geometryData);
}

//  CylinderGeometry::GeometryData
//      CylinderGeometry::generateCylinderGeometry(float radius, float
//      length, int rings, int slices)
extern "C" Q_DECL_EXPORT
CylinderGeometry::GeometryData *ritual_ZN16CylinderGeometry24generateCylinderGeometryEffii(
    float radius,
    float length,
    int rings,
    int slices) {
  return new CylinderGeometry::GeometryData(
      CylinderGeometry::generateCylinderGeometry(
          radius,
          length,
          rings,
          slices));
}

#if QT_CONFIG(concurrent)
//  void CylinderGeometry::generateCylinderGeometryAsync(QPromise<CylinderGeo
//      metry::GeometryData> &promise, float radius, float length, int rings,
//      int segments)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CylinderGeometry29generateCylinderGeometryAsyncER8QPromiseINS_12GeometryDataEEffii(
    QPromise<CylinderGeometry::GeometryData> *promise,
    float radius,
    float length,
    int rings,
    int segments) {
  CylinderGeometry::generateCylinderGeometryAsync(
      *promise,
      radius,
      length,
      rings,
      segments);
}
#endif  // QT_CONFIG(concurrent)

//  a Python function taken by a CuteCylinderGeometry, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_CylinderGeometry(
    CylinderGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteCylinderGeometry *>(self)->take(key, call);
}

//  a CylinderGeometry::GeometryData a ritual of CylinderGeometry gave
extern "C" Q_DECL_EXPORT
void ritual_drop_CylinderGeometry__CylinderGeometry_GeometryData(
    CylinderGeometry::GeometryData *self) {
  delete self;
}
