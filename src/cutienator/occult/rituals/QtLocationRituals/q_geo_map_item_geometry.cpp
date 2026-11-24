//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomapitemgeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomapitemgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeorectangle.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoMapItemGeometry that Python can take functions over in. Every QGeoMapItemGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoMapItemGeometryCall0)(const void *, const QPointF *, int *);
class CuteQGeoMapItemGeometry : public QGeoMapItemGeometry {
public:
  using QGeoMapItemGeometry::QGeoMapItemGeometry;
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
      CuteQGeoMapItemGeometryCall0 call = reinterpret_cast<CuteQGeoMapItemGeometryCall0>(taken[0]);
      bool given = call(this, &screenPoint, &handled);
      if (handled) return given;
    }
    return QGeoMapItemGeometry::contains(screenPoint);
  }
};

//  QList<QGeoCoordinate> QGeoMapItemGeometry::path(const QGeoRectangle
//      &rect)
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZN19QGeoMapItemGeometry4pathERK13QGeoRectangle(
    const QGeoRectangle *rect) {
  return new QList<QGeoCoordinate>(QGeoMapItemGeometry::path(*rect));
}

//  QList<QGeoCoordinate> QGeoMapItemGeometry::perimeter(const QGeoRectangle
//      &rect)
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZN19QGeoMapItemGeometry9perimeterERK13QGeoRectangle(
    const QGeoRectangle *rect) {
  return new QList<QGeoCoordinate>(QGeoMapItemGeometry::perimeter(*rect));
}

//  QList<QDoubleVector2D> QGeoMapItemGeometry::pathMercator(const
//      QList<QGeoCoordinate> &p)
extern "C" Q_DECL_EXPORT
QList<QDoubleVector2D> *ritual_ZN19QGeoMapItemGeometry12pathMercatorERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *p) {
  return new QList<QDoubleVector2D>(QGeoMapItemGeometry::pathMercator(*p));
}

//  QGeoMapItemGeometry::QGeoMapItemGeometry()
extern "C" Q_DECL_EXPORT
QGeoMapItemGeometry *ritual_ZN19QGeoMapItemGeometryC1Ev() {
  return new CuteQGeoMapItemGeometry();
}

//  QGeoMapItemGeometry::~QGeoMapItemGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometryD1Ev(QGeoMapItemGeometry *self) {
  delete self;
}

//  bool QGeoMapItemGeometry::isSourceDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoMapItemGeometry13isSourceDirtyEv(
    const QGeoMapItemGeometry *self) {
  return self->isSourceDirty();
}

//  bool QGeoMapItemGeometry::isScreenDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoMapItemGeometry13isScreenDirtyEv(
    const QGeoMapItemGeometry *self) {
  return self->isScreenDirty();
}

//  void QGeoMapItemGeometry::markSourceDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometry15markSourceDirtyEv(
    QGeoMapItemGeometry *self) {
  self->markSourceDirty();
}

//  void QGeoMapItemGeometry::markScreenDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometry15markScreenDirtyEv(
    QGeoMapItemGeometry *self) {
  self->markScreenDirty();
}

//  void QGeoMapItemGeometry::markFullScreenDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometry19markFullScreenDirtyEv(
    QGeoMapItemGeometry *self) {
  self->markFullScreenDirty();
}

//  void QGeoMapItemGeometry::markClean()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometry9markCleanEv(QGeoMapItemGeometry *self) {
  self->markClean();
}

//  void QGeoMapItemGeometry::clearScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometry11clearScreenEv(
    QGeoMapItemGeometry *self) {
  self->clearScreen();
}

//  QGeoCoordinate QGeoMapItemGeometry::geoLeftBound()
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN19QGeoMapItemGeometry12geoLeftBoundEv(
    QGeoMapItemGeometry *self) {
  return new QGeoCoordinate(self->geoLeftBound());
}

//  QRectF QGeoMapItemGeometry::sourceBoundingBox() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGeoMapItemGeometry17sourceBoundingBoxEv(
    const QGeoMapItemGeometry *self) {
  return new QRectF(self->sourceBoundingBox());
}

//  QRectF QGeoMapItemGeometry::screenBoundingBox() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGeoMapItemGeometry17screenBoundingBoxEv(
    const QGeoMapItemGeometry *self) {
  return new QRectF(self->screenBoundingBox());
}

//  void QGeoMapItemGeometry::clearBounds()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometry11clearBoundsEv(
    QGeoMapItemGeometry *self) {
  self->clearBounds();
}

//  QPointF QGeoMapItemGeometry::firstPointOffset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QGeoMapItemGeometry16firstPointOffsetEv(
    const QGeoMapItemGeometry *self) {
  return new QPointF(self->firstPointOffset());
}

//  const QGeoCoordinate &QGeoMapItemGeometry::origin() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK19QGeoMapItemGeometry6originEv(
    const QGeoMapItemGeometry *self) {
  return new QGeoCoordinate(self->origin());
}

//  QPainterPath QGeoMapItemGeometry::screenOutline() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK19QGeoMapItemGeometry13screenOutlineEv(
    const QGeoMapItemGeometry *self) {
  return new QPainterPath(self->screenOutline());
}

//  bool QGeoMapItemGeometry::contains(const QPointF &screenPoint) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoMapItemGeometry8containsERK7QPointF(
    const QGeoMapItemGeometry *self,
    const QPointF *screenPoint) {
  return self->contains(*screenPoint);
}

//  QVector2D QGeoMapItemGeometry::vertex(quint32 index) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK19QGeoMapItemGeometry6vertexEj(
    const QGeoMapItemGeometry *self,
    quint32 index) {
  return new QVector2D(self->vertex(index));
}

//  QList<QPointF> QGeoMapItemGeometry::vertices() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK19QGeoMapItemGeometry8verticesEv(
    const QGeoMapItemGeometry *self) {
  return new QList<QPointF>(self->vertices());
}

//  bool QGeoMapItemGeometry::isIndexed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoMapItemGeometry9isIndexedEv(
    const QGeoMapItemGeometry *self) {
  return self->isIndexed();
}

//  quint32 QGeoMapItemGeometry::size() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK19QGeoMapItemGeometry4sizeEv(
    const QGeoMapItemGeometry *self) {
  return self->size();
}

//  void QGeoMapItemGeometry::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoMapItemGeometry5clearEv(QGeoMapItemGeometry *self) {
  self->clear();
}

//  a Python function taken by a CuteQGeoMapItemGeometry, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMapItemGeometry(
    QGeoMapItemGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoMapItemGeometry *>(self)->take(key, call);
}

//  bool QGeoMapItemGeometry::contains(const QPointF &screenPoint) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QGeoMapItemGeometry8containsERK7QPointF(
    const QGeoMapItemGeometry *self,
    const QPointF *screenPoint) {
  return self->QGeoMapItemGeometry::contains(*screenPoint);
}
