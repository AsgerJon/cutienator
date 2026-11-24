//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeocoordinate.h>
#include <cstring>

//  A QDeclarativeCircleMapItemPrivate that Python can take functions over in. Every QDeclarativeCircleMapItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeCircleMapItemPrivateCall0)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCall1)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCall2)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCall3)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCall4)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCall5)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCall6)(const void *, int *);
typedef void * (*CuteQDeclarativeCircleMapItemPrivateCall7)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativeCircleMapItemPrivateCall8)(const void *, const QPointF *, int *);
class CuteQDeclarativeCircleMapItemPrivate : public QDeclarativeCircleMapItemPrivate {
public:
  using QDeclarativeCircleMapItemPrivate::QDeclarativeCircleMapItemPrivate;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate23onLinePropertiesChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate24markSourceDirtyAndUpdateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate8onMapSetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate20onGeoGeometryChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate21onItemGeometryChangedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate12updatePolishEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate20afterViewportChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDeclarativeCircleMapItemPrivate8containsERK7QPointF")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void QDeclarativeCircleMapItemPrivate::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall0 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeCircleMapItemPrivate::markSourceDirtyAndUpdate()
  void markSourceDirtyAndUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall1 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeCircleMapItemPrivate::onMapSet()
  void onMapSet() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall2 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeCircleMapItemPrivate::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall3 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeCircleMapItemPrivate::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall4 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeCircleMapItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall5 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeCircleMapItemPrivate::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall6 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QSGNode
  //      *QDeclarativeCircleMapItemPrivate::updateMapItemPaintNode(QSGNode
  //      *oldNode, QQuickItem::UpdatePaintNodeData *data)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall7 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall7>(taken[7]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return {};
  }

  //  bool QDeclarativeCircleMapItemPrivate::contains(const QPointF &point)
  //      const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCall8 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDeclarativeCircleMapItemPrivate::~QDeclarativeCircleMapItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivateD1Ev(
    QDeclarativeCircleMapItemPrivate *self) {
  delete self;
}

//  void QDeclarativeCircleMapItemPrivate::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate23onLinePropertiesChangedEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativeCircleMapItemPrivate::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate24markSourceDirtyAndUpdateEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativeCircleMapItemPrivate::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate8onMapSetEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->onMapSet();
}

//  void QDeclarativeCircleMapItemPrivate::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate20onGeoGeometryChangedEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativeCircleMapItemPrivate::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate21onItemGeometryChangedEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativeCircleMapItemPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate12updatePolishEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->updatePolish();
}

//  void QDeclarativeCircleMapItemPrivate::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate20afterViewportChangedEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->afterViewportChanged();
}

//  QSGNode *QDeclarativeCircleMapItemPrivate::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN32QDeclarativeCircleMapItemPrivate22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeCircleMapItemPrivate *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updateMapItemPaintNode(oldNode, data);
}

//  bool QDeclarativeCircleMapItemPrivate::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QDeclarativeCircleMapItemPrivate8containsERK7QPointF(
    const QDeclarativeCircleMapItemPrivate *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QDeclarativeCircleMapItemPrivate::updateCirclePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDeclarativeCircleMapItemPrivate16updateCirclePathEv(
    QDeclarativeCircleMapItemPrivate *self) {
  self->updateCirclePath();
}

//  int QDeclarativeCircleMapItemPrivate::crossEarthPole(const QGeoCoordinate
//      &center, qreal distance)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QDeclarativeCircleMapItemPrivate14crossEarthPoleERK14QGeoCoordinated(
    const QGeoCoordinate *center,
    qreal distance) {
  return QDeclarativeCircleMapItemPrivate::crossEarthPole(*center, distance);
}

//  a Python function taken by a CuteQDeclarativeCircleMapItemPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeCircleMapItemPrivate(
    QDeclarativeCircleMapItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeCircleMapItemPrivate *>(self)->take(key, call);
}
