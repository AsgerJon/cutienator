//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/conegeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/conegeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A ConeGeometry that Python can take functions over in. Every ConeGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteConeGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteConeGeometryCall1)(const void *, int *);
typedef void (*CuteConeGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteConeGeometryCall3)(const void *, int *);
typedef void (*CuteConeGeometryCall4)(const void *, int *);
typedef void (*CuteConeGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteConeGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteConeGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteConeGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteConeGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteConeGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteConeGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteConeGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteConeGeometry : public ConeGeometry {
public:
  using ConeGeometry::ConeGeometry;
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
      CuteConeGeometryCall0 call = reinterpret_cast<CuteConeGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteConeGeometryCall1 call = reinterpret_cast<CuteConeGeometryCall1>(taken[1]);
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
      CuteConeGeometryCall2 call = reinterpret_cast<CuteConeGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteConeGeometryCall3 call = reinterpret_cast<CuteConeGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteConeGeometryCall4 call = reinterpret_cast<CuteConeGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteConeGeometryCall5 call = reinterpret_cast<CuteConeGeometryCall5>(taken[5]);
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
      CuteConeGeometryCall6 call = reinterpret_cast<CuteConeGeometryCall6>(taken[6]);
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
      CuteConeGeometryCall7 call = reinterpret_cast<CuteConeGeometryCall7>(taken[7]);
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
      CuteConeGeometryCall8 call = reinterpret_cast<CuteConeGeometryCall8>(taken[8]);
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
      CuteConeGeometryCall9 call = reinterpret_cast<CuteConeGeometryCall9>(taken[9]);
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
      CuteConeGeometryCall10 call = reinterpret_cast<CuteConeGeometryCall10>(taken[10]);
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
      CuteConeGeometryCall11 call = reinterpret_cast<CuteConeGeometryCall11>(taken[11]);
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
      CuteConeGeometryCall12 call = reinterpret_cast<CuteConeGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ConeGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12ConeGeometry10metaObjectEv(
    const ConeGeometry *self) {
  return self->metaObject();
}

//  void *ConeGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12ConeGeometry11qt_metacastEPKc(
    ConeGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ConeGeometry::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12ConeGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    ConeGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString ConeGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12ConeGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ConeGeometry::tr(s, c, n));
}

//  ConeGeometry::ConeGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
ConeGeometry *ritual_ZN12ConeGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteConeGeometry(parent);
}

//  ConeGeometry::~ConeGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometryD1Ev(ConeGeometry *self) {
  delete self;
}

//  float ConeGeometry::topRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12ConeGeometry9topRadiusEv(const ConeGeometry *self) {
  return self->topRadius();
}

//  void ConeGeometry::setTopRadius(float newTopRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry12setTopRadiusEf(
    ConeGeometry *self,
    float newTopRadius) {
  self->setTopRadius(newTopRadius);
}

//  float ConeGeometry::bottomRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12ConeGeometry12bottomRadiusEv(const ConeGeometry *self) {
  return self->bottomRadius();
}

//  void ConeGeometry::setBottomRadius(float newBottomRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry15setBottomRadiusEf(
    ConeGeometry *self,
    float newBottomRadius) {
  self->setBottomRadius(newBottomRadius);
}

//  float ConeGeometry::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12ConeGeometry6lengthEv(const ConeGeometry *self) {
  return self->length();
}

//  void ConeGeometry::setLength(float newLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry9setLengthEf(
    ConeGeometry *self,
    float newLength) {
  self->setLength(newLength);
}

//  int ConeGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12ConeGeometry5ringsEv(const ConeGeometry *self) {
  return self->rings();
}

//  void ConeGeometry::setRings(int newRings)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry8setRingsEi(ConeGeometry *self, int newRings) {
  self->setRings(newRings);
}

//  int ConeGeometry::segments() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12ConeGeometry8segmentsEv(const ConeGeometry *self) {
  return self->segments();
}

//  void ConeGeometry::setSegments(int newSegments)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry11setSegmentsEi(
    ConeGeometry *self,
    int newSegments) {
  self->setSegments(newSegments);
}

//  bool ConeGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12ConeGeometry12asynchronousEv(const ConeGeometry *self) {
  return self->asynchronous();
}

//  void ConeGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry15setAsynchronousEb(
    ConeGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status ConeGeometry::status() const
extern "C" Q_DECL_EXPORT
ConeGeometry::Status ritual_ZNK12ConeGeometry6statusEv(
    const ConeGeometry *self) {
  return self->status();
}

//  void ConeGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry16doUpdateGeometryEv(ConeGeometry *self) {
  self->doUpdateGeometry();
}

//  void ConeGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry15requestFinishedEv(ConeGeometry *self) {
  self->requestFinished();
}

//  void ConeGeometry::topRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry16topRadiusChangedEv(ConeGeometry *self) {
  self->topRadiusChanged();
}

//  void ConeGeometry::bottomRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry19bottomRadiusChangedEv(ConeGeometry *self) {
  self->bottomRadiusChanged();
}

//  void ConeGeometry::lengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry13lengthChangedEv(ConeGeometry *self) {
  self->lengthChanged();
}

//  void ConeGeometry::ringsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry12ringsChangedEv(ConeGeometry *self) {
  self->ringsChanged();
}

//  void ConeGeometry::segmentsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry15segmentsChangedEv(ConeGeometry *self) {
  self->segmentsChanged();
}

//  void ConeGeometry::asynchronousChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry19asynchronousChangedEv(ConeGeometry *self) {
  self->asynchronousChanged();
}

//  void ConeGeometry::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry13statusChangedEv(ConeGeometry *self) {
  self->statusChanged();
}

//  void ConeGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry22scheduleGeometryUpdateEv(ConeGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  void ConeGeometry::updateGeometry(const GeometryData &geometryData)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry14updateGeometryERKNS_12GeometryDataE(
    ConeGeometry *self,
    const ConeGeometry::GeometryData *geometryData) {
  self->updateGeometry(*geometryData);
}

//  ConeGeometry::GeometryData ConeGeometry::generateConeGeometry(float
//      topRadius, float bottomRadius, float length, int rings, int slices)
extern "C" Q_DECL_EXPORT
ConeGeometry::GeometryData *ritual_ZN12ConeGeometry20generateConeGeometryEfffii(
    float topRadius,
    float bottomRadius,
    float length,
    int rings,
    int slices) {
  return new ConeGeometry::GeometryData(
      ConeGeometry::generateConeGeometry(
          topRadius,
          bottomRadius,
          length,
          rings,
          slices));
}

#if QT_CONFIG(concurrent)
//  void ConeGeometry::generateConeGeometryAsync(QPromise<ConeGeometry::Geome
//      tryData> &promise, float topRadius, float bottomRadius, float length,
//      int rings, int segments)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ConeGeometry25generateConeGeometryAsyncER8QPromiseINS_12GeometryDataEEfffii(
    QPromise<ConeGeometry::GeometryData> *promise,
    float topRadius,
    float bottomRadius,
    float length,
    int rings,
    int segments) {
  ConeGeometry::generateConeGeometryAsync(
      *promise,
      topRadius,
      bottomRadius,
      length,
      rings,
      segments);
}
#endif  // QT_CONFIG(concurrent)

//  a Python function taken by a CuteConeGeometry, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ConeGeometry(
    ConeGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteConeGeometry *>(self)->take(key, call);
}

//  a ConeGeometry::GeometryData a ritual of ConeGeometry gave
extern "C" Q_DECL_EXPORT
void ritual_drop_ConeGeometry__ConeGeometry_GeometryData(
    ConeGeometry::GeometryData *self) {
  delete self;
}
