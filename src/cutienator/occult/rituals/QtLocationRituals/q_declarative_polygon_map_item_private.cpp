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

//  A QDeclarativePolygonMapItemPrivate that Python can take functions over in. Every QDeclarativePolygonMapItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall0)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall1)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall2)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall3)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall4)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall5)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall6)(const void *, int *);
typedef void (*CuteQDeclarativePolygonMapItemPrivateCall7)(const void *, int *);
typedef void * (*CuteQDeclarativePolygonMapItemPrivateCall8)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativePolygonMapItemPrivateCall9)(const void *, const QPointF *, int *);
class CuteQDeclarativePolygonMapItemPrivate : public QDeclarativePolygonMapItemPrivate {
public:
  using QDeclarativePolygonMapItemPrivate::QDeclarativePolygonMapItemPrivate;
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
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate8onMapSetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryUpdatedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate21onItemGeometryChangedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate12updatePolishEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN33QDeclarativePolygonMapItemPrivate20afterViewportChangedEv")) {
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

  //  void QDeclarativePolygonMapItemPrivate::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall0 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolygonMapItemPrivate::markSourceDirtyAndUpdate()
  void markSourceDirtyAndUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall1 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolygonMapItemPrivate::onMapSet()
  void onMapSet() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall2 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolygonMapItemPrivate::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall3 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolygonMapItemPrivate::onGeoGeometryUpdated()
  void onGeoGeometryUpdated() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall4 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolygonMapItemPrivate::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall5 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolygonMapItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall6 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolygonMapItemPrivate::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall7 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QSGNode
  //      *QDeclarativePolygonMapItemPrivate::updateMapItemPaintNode(QSGNod
  //      e *oldNode, QQuickItem::UpdatePaintNodeData *data)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall8 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall8>(taken[8]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return {};
  }

  //  bool QDeclarativePolygonMapItemPrivate::contains(const QPointF
  //      &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativePolygonMapItemPrivateCall9 call = reinterpret_cast<CuteQDeclarativePolygonMapItemPrivateCall9>(taken[9]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDeclarativePolygonMapItemPrivate::~QDeclarativePolygonMapItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivateD1Ev(
    QDeclarativePolygonMapItemPrivate *self) {
  delete self;
}

//  void QDeclarativePolygonMapItemPrivate::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate23onLinePropertiesChangedEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativePolygonMapItemPrivate::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate24markSourceDirtyAndUpdateEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativePolygonMapItemPrivate::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate8onMapSetEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->onMapSet();
}

//  void QDeclarativePolygonMapItemPrivate::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryChangedEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativePolygonMapItemPrivate::onGeoGeometryUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryUpdatedEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->onGeoGeometryUpdated();
}

//  void QDeclarativePolygonMapItemPrivate::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate21onItemGeometryChangedEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativePolygonMapItemPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate12updatePolishEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->updatePolish();
}

//  void QDeclarativePolygonMapItemPrivate::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativePolygonMapItemPrivate20afterViewportChangedEv(
    QDeclarativePolygonMapItemPrivate *self) {
  self->afterViewportChanged();
}

//  QSGNode
//      *QDeclarativePolygonMapItemPrivate::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN33QDeclarativePolygonMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolygonMapItemPrivate *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updateMapItemPaintNode(oldNode, data);
}

//  bool QDeclarativePolygonMapItemPrivate::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QDeclarativePolygonMapItemPrivate8containsERK7QPointF(
    const QDeclarativePolygonMapItemPrivate *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  a Python function taken by a CuteQDeclarativePolygonMapItemPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePolygonMapItemPrivate(
    QDeclarativePolygonMapItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePolygonMapItemPrivate *>(self)->take(key, call);
}
