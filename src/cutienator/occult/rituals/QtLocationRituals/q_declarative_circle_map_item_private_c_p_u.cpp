//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A QDeclarativeCircleMapItemPrivateCPU that Python can take functions over in. Every QDeclarativeCircleMapItemPrivateCPU
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeCircleMapItemPrivateCPUCall0)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCPUCall1)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCPUCall2)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCPUCall3)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCPUCall4)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCPUCall5)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemPrivateCPUCall6)(const void *, int *);
typedef void * (*CuteQDeclarativeCircleMapItemPrivateCPUCall7)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativeCircleMapItemPrivateCPUCall8)(const void *, const QPointF *, int *);
class CuteQDeclarativeCircleMapItemPrivateCPU : public QDeclarativeCircleMapItemPrivateCPU {
public:
  using QDeclarativeCircleMapItemPrivateCPU::QDeclarativeCircleMapItemPrivateCPU;
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
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate20afterViewportChangedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDeclarativeCircleMapItemPrivate12updatePolishEv")) {
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

  //  void QDeclarativeCircleMapItemPrivateCPU::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall0 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItemPrivateCPU::onLinePropertiesChanged();
  }

  //  void QDeclarativeCircleMapItemPrivateCPU::markSourceDirtyAndUpdate()
  void markSourceDirtyAndUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall1 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItemPrivateCPU::markSourceDirtyAndUpdate();
  }

  //  void QDeclarativeCircleMapItemPrivateCPU::onMapSet()
  void onMapSet() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall2 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItemPrivateCPU::onMapSet();
  }

  //  void QDeclarativeCircleMapItemPrivateCPU::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall3 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItemPrivateCPU::onGeoGeometryChanged();
  }

  //  void QDeclarativeCircleMapItemPrivateCPU::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall4 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItemPrivateCPU::onItemGeometryChanged();
  }

  //  void QDeclarativeCircleMapItemPrivateCPU::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall5 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItemPrivateCPU::afterViewportChanged();
  }

  //  void QDeclarativeCircleMapItemPrivateCPU::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall6 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItemPrivateCPU::updatePolish();
  }

  //  QSGNode
  //      *QDeclarativeCircleMapItemPrivateCPU::updateMapItemPaintNode(QSGN
  //      ode *oldNode, QQuickItem::UpdatePaintNodeData *data)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall7 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall7>(taken[7]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeCircleMapItemPrivateCPU::updateMapItemPaintNode(oldNode, data);
  }

  //  bool QDeclarativeCircleMapItemPrivateCPU::contains(const QPointF
  //      &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemPrivateCPUCall8 call = reinterpret_cast<CuteQDeclarativeCircleMapItemPrivateCPUCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativeCircleMapItemPrivateCPU::contains(point);
  }
};

//  QDeclarativeCircleMapItemPrivateCPU::~QDeclarativeCircleMapItemPrivateCPU
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPUD1Ev(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  delete self;
}

//  void QDeclarativeCircleMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativeCircleMapItemPrivateCPU::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPU8onMapSetEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->onMapSet();
}

//  void QDeclarativeCircleMapItemPrivateCPU::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPU20onGeoGeometryChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->afterViewportChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDeclarativeCircleMapItemPrivateCPU12updatePolishEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->updatePolish();
}

//  QSGNode
//      *QDeclarativeCircleMapItemPrivateCPU::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN35QDeclarativeCircleMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeCircleMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updateMapItemPaintNode(oldNode, data);
}

//  bool QDeclarativeCircleMapItemPrivateCPU::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QDeclarativeCircleMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativeCircleMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  a Python function taken by a CuteQDeclarativeCircleMapItemPrivateCPU, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeCircleMapItemPrivateCPU(
    QDeclarativeCircleMapItemPrivateCPU *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeCircleMapItemPrivateCPU *>(self)->take(key, call);
}

//  void QDeclarativeCircleMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->QDeclarativeCircleMapItemPrivateCPU::onLinePropertiesChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->QDeclarativeCircleMapItemPrivateCPU::markSourceDirtyAndUpdate();
}

//  void QDeclarativeCircleMapItemPrivateCPU::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU8onMapSetEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->QDeclarativeCircleMapItemPrivateCPU::onMapSet();
}

//  void QDeclarativeCircleMapItemPrivateCPU::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU20onGeoGeometryChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->QDeclarativeCircleMapItemPrivateCPU::onGeoGeometryChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->QDeclarativeCircleMapItemPrivateCPU::onItemGeometryChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->QDeclarativeCircleMapItemPrivateCPU::afterViewportChanged();
}

//  void QDeclarativeCircleMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU12updatePolishEv(
    QDeclarativeCircleMapItemPrivateCPU *self) {
  self->QDeclarativeCircleMapItemPrivateCPU::updatePolish();
}

//  QSGNode
//      *QDeclarativeCircleMapItemPrivateCPU::updateMapItemPaintNode(QSGNode
//      *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN35QDeclarativeCircleMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeCircleMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->QDeclarativeCircleMapItemPrivateCPU::updateMapItemPaintNode(
      oldNode,
      data);
}

//  bool QDeclarativeCircleMapItemPrivateCPU::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK35QDeclarativeCircleMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativeCircleMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->QDeclarativeCircleMapItemPrivateCPU::contains(*point);
}
