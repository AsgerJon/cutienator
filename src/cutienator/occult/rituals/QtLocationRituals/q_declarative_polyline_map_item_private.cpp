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

//  A QDeclarativePolylineMapItemPrivate that Python can take functions over in. Every QDeclarativePolylineMapItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall0)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall1)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall2)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall3)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall4)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall5)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall6)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemPrivateCall7)(const void *, int *);
typedef void * (*CuteQDeclarativePolylineMapItemPrivateCall8)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativePolylineMapItemPrivateCall9)(const void *, const QPointF *, int *);
class CuteQDeclarativePolylineMapItemPrivate : public QDeclarativePolylineMapItemPrivate {
public:
  using QDeclarativePolylineMapItemPrivate::QDeclarativePolylineMapItemPrivate;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate24markSourceDirtyAndUpdateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate8onMapSetEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate23onLinePropertiesChangedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate20onGeoGeometryChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate20onGeoGeometryUpdatedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate21onItemGeometryChangedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate12updatePolishEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDeclarativePolylineMapItemPrivate20afterViewportChangedEv")) {
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

  //  void QDeclarativePolylineMapItemPrivate::markSourceDirtyAndUpdate()
  void markSourceDirtyAndUpdate() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall0 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolylineMapItemPrivate::onMapSet()
  void onMapSet() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall1 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolylineMapItemPrivate::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall2 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolylineMapItemPrivate::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall3 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolylineMapItemPrivate::onGeoGeometryUpdated()
  void onGeoGeometryUpdated() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall4 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolylineMapItemPrivate::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall5 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolylineMapItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall6 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativePolylineMapItemPrivate::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall7 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QSGNode
  //      *QDeclarativePolylineMapItemPrivate::updateMapItemPaintNode(QSGNo
  //      de *oldNode, QQuickItem::UpdatePaintNodeData *data)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall8 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall8>(taken[8]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return {};
  }

  //  bool QDeclarativePolylineMapItemPrivate::contains(const QPointF
  //      &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemPrivateCall9 call = reinterpret_cast<CuteQDeclarativePolylineMapItemPrivateCall9>(taken[9]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDeclarativePolylineMapItemPrivate::QDeclarativePolylineMapItemPrivate(QD
//      eclarativePolylineMapItem &poly)
extern "C" Q_DECL_EXPORT
QDeclarativePolylineMapItemPrivate *ritual_ZN34QDeclarativePolylineMapItemPrivateC1ER27QDeclarativePolylineMapItem(
    QDeclarativePolylineMapItem *poly) {
  return new CuteQDeclarativePolylineMapItemPrivate(*poly);
}

//  QDeclarativePolylineMapItemPrivate::~QDeclarativePolylineMapItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivateD1Ev(
    QDeclarativePolylineMapItemPrivate *self) {
  delete self;
}

//  void QDeclarativePolylineMapItemPrivate::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate24markSourceDirtyAndUpdateEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativePolylineMapItemPrivate::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate8onMapSetEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->onMapSet();
}

//  void QDeclarativePolylineMapItemPrivate::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate23onLinePropertiesChangedEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativePolylineMapItemPrivate::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate20onGeoGeometryChangedEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativePolylineMapItemPrivate::onGeoGeometryUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate20onGeoGeometryUpdatedEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->onGeoGeometryUpdated();
}

//  void QDeclarativePolylineMapItemPrivate::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate21onItemGeometryChangedEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativePolylineMapItemPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate12updatePolishEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->updatePolish();
}

//  void QDeclarativePolylineMapItemPrivate::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDeclarativePolylineMapItemPrivate20afterViewportChangedEv(
    QDeclarativePolylineMapItemPrivate *self) {
  self->afterViewportChanged();
}

//  QSGNode
//      *QDeclarativePolylineMapItemPrivate::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN34QDeclarativePolylineMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolylineMapItemPrivate *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updateMapItemPaintNode(oldNode, data);
}

//  bool QDeclarativePolylineMapItemPrivate::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QDeclarativePolylineMapItemPrivate8containsERK7QPointF(
    const QDeclarativePolylineMapItemPrivate *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  a Python function taken by a CuteQDeclarativePolylineMapItemPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePolylineMapItemPrivate(
    QDeclarativePolylineMapItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePolylineMapItemPrivate *>(self)->take(key, call);
}
