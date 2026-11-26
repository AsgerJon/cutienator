//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativerectanglemapitem_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativerectanglemapitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A QDeclarativeRectangleMapItemPrivate that Python can take functions over in. Every QDeclarativeRectangleMapItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCall0)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCall1)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCall2)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCall3)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCall4)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCall5)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCall6)(const void *, int *);
typedef void * (*CuteQDeclarativeRectangleMapItemPrivateCall7)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativeRectangleMapItemPrivateCall8)(const void *, const QPointF *, int *);
class CuteQDeclarativeRectangleMapItemPrivate : public QDeclarativeRectangleMapItemPrivate {
public:
  using QDeclarativeRectangleMapItemPrivate::QDeclarativeRectangleMapItemPrivate;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate23onLinePropertiesChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate24markSourceDirtyAndUpdateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate8onMapSetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate20onGeoGeometryChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate21onItemGeometryChangedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate12updatePolishEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate20afterViewportChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDeclarativeRectangleMapItemPrivate8containsERK7QPointF")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void QDeclarativeRectangleMapItemPrivate::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall0 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeRectangleMapItemPrivate::markSourceDirtyAndUpdate()
  void markSourceDirtyAndUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall1 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeRectangleMapItemPrivate::onMapSet()
  void onMapSet() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall2 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeRectangleMapItemPrivate::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall3 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeRectangleMapItemPrivate::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall4 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeRectangleMapItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall5 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeRectangleMapItemPrivate::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall6 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QSGNode
  //      *QDeclarativeRectangleMapItemPrivate::updateMapItemPaintNode(QSGN
  //      ode *oldNode, QQuickItem::UpdatePaintNodeData *data)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall7 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall7>(taken[7]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return {};
  }

  //  bool QDeclarativeRectangleMapItemPrivate::contains(const QPointF
  //      &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCall8 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDeclarativeRectangleMapItemPrivate::QDeclarativeRectangleMapItemPrivate(
//      QDeclarativeRectangleMapItem &rect)
extern "C" Q_DECL_EXPORT
QDeclarativeRectangleMapItemPrivate *ritual_ZN35QDeclarativeRectangleMapItemPrivateC1ER28QDeclarativeRectangleMapItem(
    QDeclarativeRectangleMapItem *rect) {
  return new CuteQDeclarativeRectangleMapItemPrivate(*rect);
}

//  QDeclarativeRectangleMapItemPrivate::~QDeclarativeRectangleMapItemPrivate
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivateD1Ev(
    QDeclarativeRectangleMapItemPrivate *self) {
  delete self;
}

//  void QDeclarativeRectangleMapItemPrivate::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivate23onLinePropertiesChangedEv(
    QDeclarativeRectangleMapItemPrivate *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativeRectangleMapItemPrivate::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivate24markSourceDirtyAndUpdateEv(
    QDeclarativeRectangleMapItemPrivate *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativeRectangleMapItemPrivate::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivate8onMapSetEv(
    QDeclarativeRectangleMapItemPrivate *self) {
  self->onMapSet();
}

//  void QDeclarativeRectangleMapItemPrivate::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivate20onGeoGeometryChangedEv(
    QDeclarativeRectangleMapItemPrivate *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativeRectangleMapItemPrivate::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivate21onItemGeometryChangedEv(
    QDeclarativeRectangleMapItemPrivate *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativeRectangleMapItemPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivate12updatePolishEv(
    QDeclarativeRectangleMapItemPrivate *self) {
  self->updatePolish();
}

//  void QDeclarativeRectangleMapItemPrivate::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeRectangleMapItemPrivate20afterViewportChangedEv(
    QDeclarativeRectangleMapItemPrivate *self) {
  self->afterViewportChanged();
}

//  QSGNode
//      *QDeclarativeRectangleMapItemPrivate::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN35QDeclarativeRectangleMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeRectangleMapItemPrivate *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updateMapItemPaintNode(oldNode, data);
}

//  bool QDeclarativeRectangleMapItemPrivate::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QDeclarativeRectangleMapItemPrivate8containsERK7QPointF(
    const QDeclarativeRectangleMapItemPrivate *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  a Python function taken by a CuteQDeclarativeRectangleMapItemPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeRectangleMapItemPrivate(
    QDeclarativeRectangleMapItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeRectangleMapItemPrivate *>(self)->take(key, call);
}
