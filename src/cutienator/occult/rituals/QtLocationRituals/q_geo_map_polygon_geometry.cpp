//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGeoMapPolygonGeometry that Python can take functions over in. Every QGeoMapPolygonGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoMapPolygonGeometryCall0)(const void *, const QPointF *, int *);
class CuteQGeoMapPolygonGeometry : public QGeoMapPolygonGeometry {
public:
  using QGeoMapPolygonGeometry::QGeoMapPolygonGeometry;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QGeoMapItemGeometry8containsERK7QPointF")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QGeoMapItemGeometry::contains(const QPointF &screenPoint) const
  bool contains(const QPointF &screenPoint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoMapPolygonGeometryCall0 call = reinterpret_cast<CuteQGeoMapPolygonGeometryCall0>(taken[0]);
      bool given = call(this, &screenPoint, &handled);
      if (handled) return given;
    }
    return QGeoMapItemGeometry::contains(screenPoint);
  }
};

//  QGeoMapPolygonGeometry::QGeoMapPolygonGeometry()
extern "C" Q_DECL_EXPORT
QGeoMapPolygonGeometry *ritual_ZN22QGeoMapPolygonGeometryC1Ev() {
  return new CuteQGeoMapPolygonGeometry();
}

//  void QGeoMapPolygonGeometry::setAssumeSimple(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoMapPolygonGeometry15setAssumeSimpleEb(
    QGeoMapPolygonGeometry *self,
    bool value) {
  self->setAssumeSimple(value);
}

//  QPainterPath QGeoMapPolygonGeometry::srcPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK22QGeoMapPolygonGeometry7srcPathEv(
    const QGeoMapPolygonGeometry *self) {
  return new QPainterPath(self->srcPath());
}

//  qreal QGeoMapPolygonGeometry::maxCoord() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGeoMapPolygonGeometry8maxCoordEv(
    const QGeoMapPolygonGeometry *self) {
  return self->maxCoord();
}

//  a Python function taken by a CuteQGeoMapPolygonGeometry, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMapPolygonGeometry(
    QGeoMapPolygonGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoMapPolygonGeometry *>(self)->take(key, call);
}
