//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A QDeclarativePolygonMapItemPrivateCPU that Python can take functions over in. Every QDeclarativePolygonMapItemPrivateCPU
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall0)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall1)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall2)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall3)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall4)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall5)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall6)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCPUCall7)(const void *, int *);
typedef void * (*CuteQDeclarativePolygonMapItemPrivateCPUCall8)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativePolygonMapItemPrivateCPUCall9)(const void *, const QPointF *, int *);
class CuteQDeclarativePolygonMapItemPrivateCPU : public QDeclarativePolygonMapItemPrivateCPU {
public:
  using QDeclarativePolygonMapItemPrivateCPU::QDeclarativePolygonMapItemPrivateCPU;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate23onLinePropertiesChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate24markSourceDirtyAndUpdateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate20afterViewportChangedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate8onMapSetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryChangedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryUpdatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate21onItemGeometryChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate12updatePolishEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK33QDeclarativePolygonMapItemPrivate8containsERK7QPointF")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall0 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::onLinePropertiesChanged();
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::markSourceDirtyAndUpdate()
  void markSourceDirtyAndUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall1 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::markSourceDirtyAndUpdate();
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall2 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::afterViewportChanged();
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::onMapSet()
  void onMapSet() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall3 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::onMapSet();
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall4 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryChanged();
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryUpdated()
  void onGeoGeometryUpdated() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall5 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryUpdated();
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall6 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::onItemGeometryChanged();
  }

  //  void QDeclarativePolygonMapItemPrivateCPU::updatePolish()
  void updatePolish() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall7 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolygonMapItemPrivateCPU::updatePolish();
  }

  //  QSGNode
  //      *QDeclarativePolygonMapItemPrivateCPU::updateMapItemPaintNode(QSG
  //      Node *oldNode, QQuickItem::UpdatePaintNodeData *data)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall8 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall8>(taken[8]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativePolygonMapItemPrivateCPU::updateMapItemPaintNode(oldNode, data);
  }

  //  bool QDeclarativePolygonMapItemPrivateCPU::contains(const QPointF
  //      &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCPUCall9 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCPUCall9>(taken[9]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativePolygonMapItemPrivateCPU::contains(point);
  }
};

//  QDeclarativePolygonMapItemPrivateCPU::~QDeclarativePolygonMapItemPrivateC
//      PU()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPUD1Ev(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  delete self;
}

//  void QDeclarativePolygonMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativePolygonMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativePolygonMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->afterViewportChanged();
}

//  void QDeclarativePolygonMapItemPrivateCPU::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU8onMapSetEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->onMapSet();
}

//  void QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU20onGeoGeometryChangedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU20onGeoGeometryUpdatedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->onGeoGeometryUpdated();
}

//  void QDeclarativePolygonMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativePolygonMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDeclarativePolygonMapItemPrivateCPU12updatePolishEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->updatePolish();
}

//  QSGNode
//      *QDeclarativePolygonMapItemPrivateCPU::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN36QDeclarativePolygonMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolygonMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updateMapItemPaintNode(oldNode, data);
}

//  bool QDeclarativePolygonMapItemPrivateCPU::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK36QDeclarativePolygonMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativePolygonMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  a Python function taken by a CuteQDeclarativePolygonMapItemPrivateCPU,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePolygonMapItemPrivateCPU(
    QDeclarativePolygonMapItemPrivateCPU *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePolygonMapItemPrivateCPU *>(self)->take(key, call);
}

//  void QDeclarativePolygonMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->QDeclarativePolygonMapItemPrivateCPU::onLinePropertiesChanged();
}

//  void QDeclarativePolygonMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->QDeclarativePolygonMapItemPrivateCPU::markSourceDirtyAndUpdate();
}

//  void QDeclarativePolygonMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->QDeclarativePolygonMapItemPrivateCPU::afterViewportChanged();
}

//  void QDeclarativePolygonMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->QDeclarativePolygonMapItemPrivateCPU::onItemGeometryChanged();
}

//  void QDeclarativePolygonMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU12updatePolishEv(
    QDeclarativePolygonMapItemPrivateCPU *self) {
  self->QDeclarativePolygonMapItemPrivateCPU::updatePolish();
}

//  QSGNode
//      *QDeclarativePolygonMapItemPrivateCPU::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolygonMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->QDeclarativePolygonMapItemPrivateCPU::updateMapItemPaintNode(
      oldNode,
      data);
}

//  bool QDeclarativePolygonMapItemPrivateCPU::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK36QDeclarativePolygonMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativePolygonMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->QDeclarativePolygonMapItemPrivateCPU::contains(*point);
}
