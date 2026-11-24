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

//  A QDeclarativeRectangleMapItemPrivateCPU that Python can take functions over in. Every QDeclarativeRectangleMapItemPrivateCPU
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCPUCall0)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCPUCall1)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCPUCall2)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCPUCall3)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCPUCall4)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCPUCall5)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemPrivateCPUCall6)(const void *, int *);
typedef void * (*CuteQDeclarativeRectangleMapItemPrivateCPUCall7)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativeRectangleMapItemPrivateCPUCall8)(const void *, const QPointF *, int *);
class CuteQDeclarativeRectangleMapItemPrivateCPU : public QDeclarativeRectangleMapItemPrivateCPU {
public:
  using QDeclarativeRectangleMapItemPrivateCPU::QDeclarativeRectangleMapItemPrivateCPU;
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
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate20afterViewportChangedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDeclarativeRectangleMapItemPrivate12updatePolishEv")) {
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

  //  void
  //      QDeclarativeRectangleMapItemPrivateCPU::onLinePropertiesChanged()
  void onLinePropertiesChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall0 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItemPrivateCPU::onLinePropertiesChanged();
  }

  //  void
  //      QDeclarativeRectangleMapItemPrivateCPU::markSourceDirtyAndUpdate(
  //      )
  void markSourceDirtyAndUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall1 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItemPrivateCPU::markSourceDirtyAndUpdate();
  }

  //  void QDeclarativeRectangleMapItemPrivateCPU::onMapSet()
  void onMapSet() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall2 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItemPrivateCPU::onMapSet();
  }

  //  void QDeclarativeRectangleMapItemPrivateCPU::onGeoGeometryChanged()
  void onGeoGeometryChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall3 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItemPrivateCPU::onGeoGeometryChanged();
  }

  //  void QDeclarativeRectangleMapItemPrivateCPU::onItemGeometryChanged()
  void onItemGeometryChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall4 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItemPrivateCPU::onItemGeometryChanged();
  }

  //  void QDeclarativeRectangleMapItemPrivateCPU::afterViewportChanged()
  void afterViewportChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall5 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItemPrivateCPU::afterViewportChanged();
  }

  //  void QDeclarativeRectangleMapItemPrivateCPU::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall6 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItemPrivateCPU::updatePolish();
  }

  //  QSGNode *QDeclarativeRectangleMapItemPrivateCPU::updateMapItemPaintNo
  //      de(QSGNode *oldNode, QQuickItem::UpdatePaintNodeData *data)
  QSGNode *updateMapItemPaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall7 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall7>(taken[7]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeRectangleMapItemPrivateCPU::updateMapItemPaintNode(oldNode, data);
  }

  //  bool QDeclarativeRectangleMapItemPrivateCPU::contains(const QPointF
  //      &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemPrivateCPUCall8 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemPrivateCPUCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativeRectangleMapItemPrivateCPU::contains(point);
  }
};

//  QDeclarativeRectangleMapItemPrivateCPU::~QDeclarativeRectangleMapItemPriv
//      ateCPU()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPUD1Ev(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  delete self;
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU8onMapSetEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->onMapSet();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU20onGeoGeometryChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->onGeoGeometryChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->onItemGeometryChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->afterViewportChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU12updatePolishEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->updatePolish();
}

//  QSGNode
//      *QDeclarativeRectangleMapItemPrivateCPU::updateMapItemPaintNode(QSGNo
//      de *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeRectangleMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updateMapItemPaintNode(oldNode, data);
}

//  bool QDeclarativeRectangleMapItemPrivateCPU::contains(const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QDeclarativeRectangleMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativeRectangleMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  a Python function taken by a CuteQDeclarativeRectangleMapItemPrivateCPU,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeRectangleMapItemPrivateCPU(
    QDeclarativeRectangleMapItemPrivateCPU *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeRectangleMapItemPrivateCPU *>(self)->take(key, call);
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU23onLinePropertiesChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->QDeclarativeRectangleMapItemPrivateCPU::onLinePropertiesChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU24markSourceDirtyAndUpdateEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->QDeclarativeRectangleMapItemPrivateCPU::markSourceDirtyAndUpdate();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onMapSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU8onMapSetEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->QDeclarativeRectangleMapItemPrivateCPU::onMapSet();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onGeoGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU20onGeoGeometryChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->QDeclarativeRectangleMapItemPrivateCPU::onGeoGeometryChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::onItemGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU21onItemGeometryChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->QDeclarativeRectangleMapItemPrivateCPU::onItemGeometryChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::afterViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU20afterViewportChangedEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->QDeclarativeRectangleMapItemPrivateCPU::afterViewportChanged();
}

//  void QDeclarativeRectangleMapItemPrivateCPU::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU12updatePolishEv(
    QDeclarativeRectangleMapItemPrivateCPU *self) {
  self->QDeclarativeRectangleMapItemPrivateCPU::updatePolish();
}

//  QSGNode
//      *QDeclarativeRectangleMapItemPrivateCPU::updateMapItemPaintNode(QSGNo
//      de *oldNode, QQuickItem::UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeRectangleMapItemPrivateCPU *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->QDeclarativeRectangleMapItemPrivateCPU::updateMapItemPaintNode(
      oldNode,
      data);
}

//  bool QDeclarativeRectangleMapItemPrivateCPU::contains(const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK38QDeclarativeRectangleMapItemPrivateCPU8containsERK7QPointF(
    const QDeclarativeRectangleMapItemPrivateCPU *self,
    const QPointF *point) {
  return self->QDeclarativeRectangleMapItemPrivateCPU::contains(*point);
}
