//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/capsulegeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/capsulegeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A CapsuleGeometry that Python can take functions over in. Every CapsuleGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteCapsuleGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteCapsuleGeometryCall1)(const void *, int *);
typedef void (*CuteCapsuleGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteCapsuleGeometryCall3)(const void *, int *);
typedef void (*CuteCapsuleGeometryCall4)(const void *, int *);
typedef void (*CuteCapsuleGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCapsuleGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCapsuleGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCapsuleGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCapsuleGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCapsuleGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCapsuleGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCapsuleGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteCapsuleGeometry : public CapsuleGeometry {
public:
  using CapsuleGeometry::CapsuleGeometry;
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
      CuteCapsuleGeometryCall0 call = reinterpret_cast<CuteCapsuleGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteCapsuleGeometryCall1 call = reinterpret_cast<CuteCapsuleGeometryCall1>(taken[1]);
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
      CuteCapsuleGeometryCall2 call = reinterpret_cast<CuteCapsuleGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteCapsuleGeometryCall3 call = reinterpret_cast<CuteCapsuleGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteCapsuleGeometryCall4 call = reinterpret_cast<CuteCapsuleGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteCapsuleGeometryCall5 call = reinterpret_cast<CuteCapsuleGeometryCall5>(taken[5]);
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
      CuteCapsuleGeometryCall6 call = reinterpret_cast<CuteCapsuleGeometryCall6>(taken[6]);
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
      CuteCapsuleGeometryCall7 call = reinterpret_cast<CuteCapsuleGeometryCall7>(taken[7]);
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
      CuteCapsuleGeometryCall8 call = reinterpret_cast<CuteCapsuleGeometryCall8>(taken[8]);
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
      CuteCapsuleGeometryCall9 call = reinterpret_cast<CuteCapsuleGeometryCall9>(taken[9]);
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
      CuteCapsuleGeometryCall10 call = reinterpret_cast<CuteCapsuleGeometryCall10>(taken[10]);
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
      CuteCapsuleGeometryCall11 call = reinterpret_cast<CuteCapsuleGeometryCall11>(taken[11]);
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
      CuteCapsuleGeometryCall12 call = reinterpret_cast<CuteCapsuleGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *CapsuleGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15CapsuleGeometry10metaObjectEv(
    const CapsuleGeometry *self) {
  return self->metaObject();
}

//  void *CapsuleGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15CapsuleGeometry11qt_metacastEPKc(
    CapsuleGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int CapsuleGeometry::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15CapsuleGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    CapsuleGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString CapsuleGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15CapsuleGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(CapsuleGeometry::tr(s, c, n));
}

//  CapsuleGeometry::CapsuleGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
CapsuleGeometry *ritual_ZN15CapsuleGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteCapsuleGeometry(parent);
}

//  CapsuleGeometry::~CapsuleGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometryD1Ev(CapsuleGeometry *self) {
  delete self;
}

//  bool CapsuleGeometry::enableNormals() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15CapsuleGeometry13enableNormalsEv(
    const CapsuleGeometry *self) {
  return self->enableNormals();
}

//  void CapsuleGeometry::setEnableNormals(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry16setEnableNormalsEb(
    CapsuleGeometry *self,
    bool enable) {
  self->setEnableNormals(enable);
}

//  bool CapsuleGeometry::enableUV() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15CapsuleGeometry8enableUVEv(const CapsuleGeometry *self) {
  return self->enableUV();
}

//  void CapsuleGeometry::setEnableUV(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry11setEnableUVEb(
    CapsuleGeometry *self,
    bool enable) {
  self->setEnableUV(enable);
}

//  int CapsuleGeometry::longitudes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15CapsuleGeometry10longitudesEv(const CapsuleGeometry *self) {
  return self->longitudes();
}

//  void CapsuleGeometry::setLongitudes(int longitudes)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry13setLongitudesEi(
    CapsuleGeometry *self,
    int longitudes) {
  self->setLongitudes(longitudes);
}

//  int CapsuleGeometry::latitudes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15CapsuleGeometry9latitudesEv(const CapsuleGeometry *self) {
  return self->latitudes();
}

//  void CapsuleGeometry::setLatitudes(int latitudes)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry12setLatitudesEi(
    CapsuleGeometry *self,
    int latitudes) {
  self->setLatitudes(latitudes);
}

//  int CapsuleGeometry::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15CapsuleGeometry5ringsEv(const CapsuleGeometry *self) {
  return self->rings();
}

//  void CapsuleGeometry::setRings(int rings)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry8setRingsEi(
    CapsuleGeometry *self,
    int rings) {
  self->setRings(rings);
}

//  float CapsuleGeometry::height() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15CapsuleGeometry6heightEv(const CapsuleGeometry *self) {
  return self->height();
}

//  void CapsuleGeometry::setHeight(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry9setHeightEf(
    CapsuleGeometry *self,
    float height) {
  self->setHeight(height);
}

//  float CapsuleGeometry::diameter() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15CapsuleGeometry8diameterEv(const CapsuleGeometry *self) {
  return self->diameter();
}

//  void CapsuleGeometry::setDiameter(float diameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry11setDiameterEf(
    CapsuleGeometry *self,
    float diameter) {
  self->setDiameter(diameter);
}

//  UVProfile CapsuleGeometry::uvProfile() const
extern "C" Q_DECL_EXPORT
CapsuleGeometry::UVProfile ritual_ZNK15CapsuleGeometry9uvProfileEv(
    const CapsuleGeometry *self) {
  return self->uvProfile();
}

//  void CapsuleGeometry::setUVProfile(UVProfile newUVProfile)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry12setUVProfileENS_9UVProfileE(
    CapsuleGeometry *self,
    CapsuleGeometry::UVProfile newUVProfile) {
  self->setUVProfile(newUVProfile);
}

//  bool CapsuleGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15CapsuleGeometry12asynchronousEv(
    const CapsuleGeometry *self) {
  return self->asynchronous();
}

//  void CapsuleGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry15setAsynchronousEb(
    CapsuleGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status CapsuleGeometry::status() const
extern "C" Q_DECL_EXPORT
CapsuleGeometry::Status ritual_ZNK15CapsuleGeometry6statusEv(
    const CapsuleGeometry *self) {
  return self->status();
}

//  void CapsuleGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry16doUpdateGeometryEv(CapsuleGeometry *self) {
  self->doUpdateGeometry();
}

//  void CapsuleGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry15requestFinishedEv(CapsuleGeometry *self) {
  self->requestFinished();
}

//  void CapsuleGeometry::enableNormalsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry20enableNormalsChangedEv(
    CapsuleGeometry *self) {
  self->enableNormalsChanged();
}

//  void CapsuleGeometry::enableUVChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry15enableUVChangedEv(CapsuleGeometry *self) {
  self->enableUVChanged();
}

//  void CapsuleGeometry::longitudesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry17longitudesChangedEv(CapsuleGeometry *self) {
  self->longitudesChanged();
}

//  void CapsuleGeometry::latitudesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry16latitudesChangedEv(CapsuleGeometry *self) {
  self->latitudesChanged();
}

//  void CapsuleGeometry::ringsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry12ringsChangedEv(CapsuleGeometry *self) {
  self->ringsChanged();
}

//  void CapsuleGeometry::heightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry13heightChangedEv(CapsuleGeometry *self) {
  self->heightChanged();
}

//  void CapsuleGeometry::diameterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry15diameterChangedEv(CapsuleGeometry *self) {
  self->diameterChanged();
}

//  void CapsuleGeometry::uvProfileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry16uvProfileChangedEv(CapsuleGeometry *self) {
  self->uvProfileChanged();
}

//  void CapsuleGeometry::asynchronousChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry19asynchronousChangedEv(
    CapsuleGeometry *self) {
  self->asynchronousChanged();
}

//  void CapsuleGeometry::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry13statusChangedEv(CapsuleGeometry *self) {
  self->statusChanged();
}

//  void CapsuleGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry22scheduleGeometryUpdateEv(
    CapsuleGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  void CapsuleGeometry::updateGeometry(const GeometryData &geometryData)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry14updateGeometryERKNS_12GeometryDataE(
    CapsuleGeometry *self,
    const CapsuleGeometry::GeometryData *geometryData) {
  self->updateGeometry(*geometryData);
}

//  CapsuleGeometry::GeometryData
//      CapsuleGeometry::generateCapsuleGeometry(bool enableNormals, bool
//      enableUV, int longitudes, int latitudes, int rings, float height,
//      float diameter, UVProfile uvProfile)
extern "C" Q_DECL_EXPORT
CapsuleGeometry::GeometryData *ritual_ZN15CapsuleGeometry23generateCapsuleGeometryEbbiiiffNS_9UVProfileE(
    bool enableNormals,
    bool enableUV,
    int longitudes,
    int latitudes,
    int rings,
    float height,
    float diameter,
    CapsuleGeometry::UVProfile uvProfile) {
  return new CapsuleGeometry::GeometryData(
      CapsuleGeometry::generateCapsuleGeometry(
          enableNormals,
          enableUV,
          longitudes,
          latitudes,
          rings,
          height,
          diameter,
          uvProfile));
}

#if QT_CONFIG(concurrent)
//  void CapsuleGeometry::generateCapsuleGeometryAsync(QPromise<CapsuleGeomet
//      ry::GeometryData> &promise, bool enableNormals, bool enableUV, int
//      longitudes, int latitudes, int rings, float height, float diameter,
//      UVProfile uvProfile)
extern "C" Q_DECL_EXPORT
void ritual_ZN15CapsuleGeometry28generateCapsuleGeometryAsyncER8QPromiseINS_12GeometryDataEEbbiiiffNS_9UVProfileE(
    QPromise<CapsuleGeometry::GeometryData> *promise,
    bool enableNormals,
    bool enableUV,
    int longitudes,
    int latitudes,
    int rings,
    float height,
    float diameter,
    CapsuleGeometry::UVProfile uvProfile) {
  CapsuleGeometry::generateCapsuleGeometryAsync(
      *promise,
      enableNormals,
      enableUV,
      longitudes,
      latitudes,
      rings,
      height,
      diameter,
      uvProfile);
}
#endif  // QT_CONFIG(concurrent)

//  a Python function taken by a CuteCapsuleGeometry, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_CapsuleGeometry(
    CapsuleGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteCapsuleGeometry *>(self)->take(key, call);
}

//  a CapsuleGeometry::GeometryData a ritual of CapsuleGeometry gave
extern "C" Q_DECL_EXPORT
void ritual_drop_CapsuleGeometry__CapsuleGeometry_GeometryData(
    CapsuleGeometry::GeometryData *self) {
  delete self;
}
