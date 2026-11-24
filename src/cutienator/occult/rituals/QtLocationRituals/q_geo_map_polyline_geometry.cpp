//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGeoMapPolylineGeometry that Python can take functions over in. Every QGeoMapPolylineGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoMapPolylineGeometryCall0)(const void *, const QPointF *, int *);
class CuteQGeoMapPolylineGeometry : public QGeoMapPolylineGeometry {
public:
  using QGeoMapPolylineGeometry::QGeoMapPolylineGeometry;
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
      CuteQGeoMapPolylineGeometryCall0 call = reinterpret_cast<CuteQGeoMapPolylineGeometryCall0>(taken[0]);
      bool given = call(this, &screenPoint, &handled);
      if (handled) return given;
    }
    return QGeoMapItemGeometry::contains(screenPoint);
  }
};

//  QPainterPath QGeoMapPolylineGeometry::srcPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK23QGeoMapPolylineGeometry7srcPathEv(
    const QGeoMapPolylineGeometry *self) {
  return new QPainterPath(self->srcPath());
}

//  a Python function taken by a CuteQGeoMapPolylineGeometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMapPolylineGeometry(
    QGeoMapPolylineGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoMapPolylineGeometry *>(self)->take(key, call);
}
