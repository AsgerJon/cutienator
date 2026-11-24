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

//  A QGeoMapCircleGeometry that Python can take functions over in. Every QGeoMapCircleGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoMapCircleGeometryCall0)(const void *, const QPointF *, int *);
class CuteQGeoMapCircleGeometry : public QGeoMapCircleGeometry {
public:
  using QGeoMapCircleGeometry::QGeoMapCircleGeometry;
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
      CuteQGeoMapCircleGeometryCall0 call = reinterpret_cast<CuteQGeoMapCircleGeometryCall0>(taken[0]);
      bool given = call(this, &screenPoint, &handled);
      if (handled) return given;
    }
    return QGeoMapItemGeometry::contains(screenPoint);
  }
};

//  QGeoMapCircleGeometry::QGeoMapCircleGeometry()
extern "C" Q_DECL_EXPORT
QGeoMapCircleGeometry *ritual_ZN21QGeoMapCircleGeometryC1Ev() {
  return new CuteQGeoMapCircleGeometry();
}

//  a Python function taken by a CuteQGeoMapCircleGeometry, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMapCircleGeometry(
    QGeoMapCircleGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoMapCircleGeometry *>(self)->take(key, call);
}
