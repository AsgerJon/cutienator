//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/torusgeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/torusgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A TorusGeometry that Python can take functions over in. Every TorusGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteTorusGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteTorusGeometryCall1)(const void *, int *);
typedef void (*CuteTorusGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteTorusGeometryCall3)(const void *, int *);
typedef void (*CuteTorusGeometryCall4)(const void *, int *);
typedef void (*CuteTorusGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteTorusGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteTorusGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTorusGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTorusGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTorusGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTorusGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTorusGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteTorusGeometry : public TorusGeometry {
public:
  using TorusGeometry::TorusGeometry;
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
      CuteTorusGeometryCall0 call = reinterpret_cast<CuteTorusGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteTorusGeometryCall1 call = reinterpret_cast<CuteTorusGeometryCall1>(taken[1]);
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
      CuteTorusGeometryCall2 call = reinterpret_cast<CuteTorusGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteTorusGeometryCall3 call = reinterpret_cast<CuteTorusGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteTorusGeometryCall4 call = reinterpret_cast<CuteTorusGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteTorusGeometryCall5 call = reinterpret_cast<CuteTorusGeometryCall5>(taken[5]);
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
      CuteTorusGeometryCall6 call = reinterpret_cast<CuteTorusGeometryCall6>(taken[6]);
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
      CuteTorusGeometryCall7 call = reinterpret_cast<CuteTorusGeometryCall7>(taken[7]);
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
      CuteTorusGeometryCall8 call = reinterpret_cast<CuteTorusGeometryCall8>(taken[8]);
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
      CuteTorusGeometryCall9 call = reinterpret_cast<CuteTorusGeometryCall9>(taken[9]);
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
      CuteTorusGeometryCall10 call = reinterpret_cast<CuteTorusGeometryCall10>(taken[10]);
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
      CuteTorusGeometryCall11 call = reinterpret_cast<CuteTorusGeometryCall11>(taken[11]);
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
      CuteTorusGeometryCall12 call = reinterpret_cast<CuteTorusGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *TorusGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13TorusGeometry10metaObjectEv(
    const TorusGeometry *self) {
  return self->metaObject();
}

//  void *TorusGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13TorusGeometry11qt_metacastEPKc(
    TorusGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int TorusGeometry::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13TorusGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    TorusGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString TorusGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13TorusGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(TorusGeometry::tr(s, c, n));
}

//  TorusGeometry::TorusGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
TorusGeometry *ritual_ZN13TorusGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteTorusGeometry(parent);
}

//  TorusGeometry::~TorusGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometryD1Ev(TorusGeometry *self) {
  delete self;
}

//  int TorusGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13TorusGeometry5ringsEv(const TorusGeometry *self) {
  return self->rings();
}

//  void TorusGeometry::setRings(int newRings)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry8setRingsEi(TorusGeometry *self, int newRings) {
  self->setRings(newRings);
}

//  int TorusGeometry::segments() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13TorusGeometry8segmentsEv(const TorusGeometry *self) {
  return self->segments();
}

//  void TorusGeometry::setSegments(int newSegments)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry11setSegmentsEi(
    TorusGeometry *self,
    int newSegments) {
  self->setSegments(newSegments);
}

//  float TorusGeometry::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13TorusGeometry6radiusEv(const TorusGeometry *self) {
  return self->radius();
}

//  void TorusGeometry::setRadius(float newRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry9setRadiusEf(
    TorusGeometry *self,
    float newRadius) {
  self->setRadius(newRadius);
}

//  float TorusGeometry::tubeRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13TorusGeometry10tubeRadiusEv(const TorusGeometry *self) {
  return self->tubeRadius();
}

//  void TorusGeometry::setTubeRadius(float newTubeRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry13setTubeRadiusEf(
    TorusGeometry *self,
    float newTubeRadius) {
  self->setTubeRadius(newTubeRadius);
}

//  bool TorusGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13TorusGeometry12asynchronousEv(const TorusGeometry *self) {
  return self->asynchronous();
}

//  void TorusGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry15setAsynchronousEb(
    TorusGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status TorusGeometry::status() const
extern "C" Q_DECL_EXPORT
TorusGeometry::Status ritual_ZNK13TorusGeometry6statusEv(
    const TorusGeometry *self) {
  return self->status();
}

//  void TorusGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry16doUpdateGeometryEv(TorusGeometry *self) {
  self->doUpdateGeometry();
}

//  void TorusGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry15requestFinishedEv(TorusGeometry *self) {
  self->requestFinished();
}

//  void TorusGeometry::ringsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry12ringsChangedEv(TorusGeometry *self) {
  self->ringsChanged();
}

//  void TorusGeometry::segmentsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry15segmentsChangedEv(TorusGeometry *self) {
  self->segmentsChanged();
}

//  void TorusGeometry::radiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry13radiusChangedEv(TorusGeometry *self) {
  self->radiusChanged();
}

//  void TorusGeometry::tubeRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry17tubeRadiusChangedEv(TorusGeometry *self) {
  self->tubeRadiusChanged();
}

//  void TorusGeometry::asynchronousChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry19asynchronousChangedEv(TorusGeometry *self) {
  self->asynchronousChanged();
}

//  void TorusGeometry::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry13statusChangedEv(TorusGeometry *self) {
  self->statusChanged();
}

//  void TorusGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry22scheduleGeometryUpdateEv(
    TorusGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  void TorusGeometry::updateGeometry(const GeometryData &geometryData)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry14updateGeometryERKNS_12GeometryDataE(
    TorusGeometry *self,
    const TorusGeometry::GeometryData *geometryData) {
  self->updateGeometry(*geometryData);
}

//  TorusGeometry::GeometryData TorusGeometry::generateTorusGeometry(int
//      rings, int segments, float radius, float tubeRadius)
extern "C" Q_DECL_EXPORT
TorusGeometry::GeometryData *ritual_ZN13TorusGeometry21generateTorusGeometryEiiff(
    int rings,
    int segments,
    float radius,
    float tubeRadius) {
  return new TorusGeometry::GeometryData(
      TorusGeometry::generateTorusGeometry(
          rings,
          segments,
          radius,
          tubeRadius));
}

#if QT_CONFIG(concurrent)
//  void TorusGeometry::generateTorusGeometryAsync(QPromise<TorusGeometry::Ge
//      ometryData> &promise, int rings, int segments, float radius, float
//      tubeRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TorusGeometry26generateTorusGeometryAsyncER8QPromiseINS_12GeometryDataEEiiff(
    QPromise<TorusGeometry::GeometryData> *promise,
    int rings,
    int segments,
    float radius,
    float tubeRadius) {
  TorusGeometry::generateTorusGeometryAsync(
      *promise,
      rings,
      segments,
      radius,
      tubeRadius);
}
#endif  // QT_CONFIG(concurrent)

//  a Python function taken by a CuteTorusGeometry, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_TorusGeometry(
    TorusGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteTorusGeometry *>(self)->take(key, call);
}

//  a TorusGeometry::GeometryData a ritual of TorusGeometry gave
extern "C" Q_DECL_EXPORT
void ritual_drop_TorusGeometry__TorusGeometry_GeometryData(
    TorusGeometry::GeometryData *self) {
  delete self;
}
