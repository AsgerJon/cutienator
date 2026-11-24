//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A QDeclarativePolylineMapItemPrivateCPU that Python can take functions over in. Every QDeclarativePolylineMapItemPrivateCPU
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall0)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall1)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall2)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall3)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall4)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall5)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall6)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCPUCall7)(const void *, int *);
typedef void * (*CuteQDeclarativePolylineMapItemPrivateCPUCall8)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativePolylineMapItemPrivateCPUCall9)(const void *, const QPointF *, int *);
class CuteQDeclarativePolylineMapItemPrivateCPU : public QDeclarativePolylineMapItemPrivateCPU {
public:
  using QDeclarativePolylineMapItemPrivateCPU::QDeclarativePolylineMapItemPrivateCPU;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate23onLinePropertiesChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate24markSourceDirtyAndUpdateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate20afterViewportChangedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate8onMapSetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate20onGeoGeometryChangedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate20onGeoGeometryUpdatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate21onItemGeometryChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate12updatePolishEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDeclarativePolylineMapItemPrivate8containsERK7QPointF")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QDeclarativePolylineMapItemPrivateCPU::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall0 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::onLinePropertiesChanged();
  }

  //  void
  //      QDeclarativePolylineMapItemPrivateCPU::markSourceDirtyAndUpdate()
  void markSourceDirtyAndUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall1 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::markSourceDirtyAndUpdate();
  }

  //  void QDeclarativePolylineMapItemPrivateCPU::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall2 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::afterViewportChanged();
  }

  //  void QDeclarativePolylineMapItemPrivateCPU::onMapSet()
  void onMapSet() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall3 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::onMapSet();
  }

  //  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall4 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryChanged();
  }

  //  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryUpdated()
  void onGeoGeometryUpdated() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall5 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryUpdated();
  }

  //  void QDeclarativePolylineMapItemPrivateCPU::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall6 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::onItemGeometryChanged();
  }

  //  void QDeclarativePolylineMapItemPrivateCPU::updatePolish()
  void updatePolish() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall7 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItemPrivateCPU::updatePolish();
  }

  //  QSGNode *QDeclarativePolylineMapItemPrivateCPU::updateMapItemPaintNod
  //      e(QSGNode *oldNode, QQuickItem::UpdatePaintNodeData *a1)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall8 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall8>(taken[8]);
      void * given = call(this, oldNode, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativePolylineMapItemPrivateCPU::updateMapItemPaintNode(oldNode, a1);
  }

  //  bool QDeclarativePolylineMapItemPrivateCPU::contains(const QPointF
  //      &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCPUCall9 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCPUCall9>(taken[9]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativePolylineMapItemPrivateCPU::contains(point);
  }
};

//  QDeclarativePolylineMapItemPrivateCPU::~QDeclarativePolylineMapItemPrivat
//      eCPU()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPUD1Ev(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  delete self;
}

//  void QDeclarativePolylineMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativePolylineMapItemPrivateCPU::regenerateCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU15regenerateCacheEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->regenerateCache();
}

//  void QDeclarativePolylineMapItemPrivateCPU::updateCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU11updateCacheEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->updateCache();
}

//  void QDeclarativePolylineMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->afterViewportChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU8onMapSetEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->onMapSet();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeometryChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeometryUpdatedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->onGeoGeometryUpdated();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDeclarativePolylineMapItemPrivateCPU12updatePolishEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->updatePolish();
}

//  QSGNode
//      *QDeclarativePolylineMapItemPrivateCPU::updateMapItemPaintNode(QSGNod
//      e *oldNode, QQuickItem::UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN37QDeclarativePolylineMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolylineMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updateMapItemPaintNode(oldNode, a1);
}

//  bool QDeclarativePolylineMapItemPrivateCPU::contains(const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK37QDeclarativePolylineMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativePolylineMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  a Python function taken by a CuteQDeclarativePolylineMapItemPrivateCPU,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePolylineMapItemPrivateCPU(
    QDeclarativePolylineMapItemPrivateCPU *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePolylineMapItemPrivateCPU *>(self)->take(key, call);
}

//  void QDeclarativePolylineMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::onLinePropertiesChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::markSourceDirtyAndUpdate();
}

//  void QDeclarativePolylineMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::afterViewportChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU8onMapSetEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::onMapSet();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeometryChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeometryUpdatedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryUpdated();
}

//  void QDeclarativePolylineMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::onItemGeometryChanged();
}

//  void QDeclarativePolylineMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU12updatePolishEv(
    QDeclarativePolylineMapItemPrivateCPU *self) {
  self->QDeclarativePolylineMapItemPrivateCPU::updatePolish();
}

//  QSGNode
//      *QDeclarativePolylineMapItemPrivateCPU::updateMapItemPaintNode(QSGNod
//      e *oldNode, QQuickItem::UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolylineMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->QDeclarativePolylineMapItemPrivateCPU::updateMapItemPaintNode(
      oldNode,
      a1);
}

//  bool QDeclarativePolylineMapItemPrivateCPU::contains(const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK37QDeclarativePolylineMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativePolylineMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->QDeclarativePolylineMapItemPrivateCPU::contains(*point);
}
