//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeoshape.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <cstring>

//  A QGeoProjection that Python can take functions over in. Every QGeoProjection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoProjectionCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQGeoProjectionCall1)(const void *, const QSize *, int *);
typedef void (*CuteQGeoProjectionCall2)(const void *, const QGeoCameraData *, bool, int *);
typedef const QGeoCameraData * (*CuteQGeoProjectionCall3)(const void *, int *);
typedef double (*CuteQGeoProjectionCall4)(const void *, int *);
typedef double (*CuteQGeoProjectionCall5)(const void *, const QGeoCameraData *, int *);
typedef double (*CuteQGeoProjectionCall6)(const void *, const QGeoCameraData *, int *);
typedef const QGeoCoordinate * (*CuteQGeoProjectionCall7)(const void *, const QDoubleVector2D *, bool, int *);
typedef const QDoubleVector2D * (*CuteQGeoProjectionCall8)(const void *, const QGeoCoordinate *, bool, int *);
typedef int (*CuteQGeoProjectionCall9)(const void *, int *);
typedef int (*CuteQGeoProjectionCall10)(const void *, int *);
typedef int (*CuteQGeoProjectionCall11)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoProjectionCall12)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef const QGeoShape * (*CuteQGeoProjectionCall13)(const void *, int *);
typedef bool (*CuteQGeoProjectionCall14)(const void *, qreal, const QGeoCoordinate *, int *);
typedef const QMatrix4x4 * (*CuteQGeoProjectionCall15)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQGeoProjectionCall16)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQGeoProjectionCall17)(const void *, int *);
typedef const QDoubleVector3D * (*CuteQGeoProjectionCall18)(const void *, int *);
typedef const QTransform * (*CuteQGeoProjectionCall19)(const void *, int *);
class CuteQGeoProjection : public QGeoProjection {
public:
  using QGeoProjection::QGeoProjection;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QGeoProjection14setVisibleAreaERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoProjection15setViewportSizeERK5QSize")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoProjection13setCameraDataERK14QGeoCameraDatab")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection10cameraDataEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection11minimumZoomEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection27maximumCenterLatitudeAtZoomERK14QGeoCameraData")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection27minimumCenterLatitudeAtZoomERK14QGeoCameraData")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection24itemPositionToCoordinateERK15QDoubleVector2Db")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection24coordinateToItemPositionERK14QGeoCoordinateb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection15projectionGroupEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection5datumEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection14projectionTypeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection13visibleRegionEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoProjection10setBearingEdRK14QGeoCoordinate")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection24projectionTransformationEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection33projectionTransformation_centeredEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection12qsgTransformEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection14centerMercatorEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection21itemToWindowTransformEv")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  void QGeoProjection::setVisibleArea(const QRectF &visibleArea)
  void setVisibleArea(const QRectF &visibleArea) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoProjectionCall0 call = reinterpret_cast<CuteQGeoProjectionCall0>(taken[0]);
      call(this, &visibleArea, &handled);
      if (handled) return;
    }
  }

  //  void QGeoProjection::setViewportSize(const QSize &size)
  void setViewportSize(const QSize &size) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoProjectionCall1 call = reinterpret_cast<CuteQGeoProjectionCall1>(taken[1]);
      call(this, &size, &handled);
      if (handled) return;
    }
  }

  //  void QGeoProjection::setCameraData(const QGeoCameraData &cameraData,
  //      bool force)
  void setCameraData(const QGeoCameraData &cameraData, bool force) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoProjectionCall2 call = reinterpret_cast<CuteQGeoProjectionCall2>(taken[2]);
      call(this, &cameraData, force, &handled);
      if (handled) return;
    }
  }

  //  QGeoCameraData QGeoProjection::cameraData() const
  QGeoCameraData cameraData() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoProjectionCall3 call = reinterpret_cast<CuteQGeoProjectionCall3>(taken[3]);
      const QGeoCameraData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  double QGeoProjection::minimumZoom() const
  double minimumZoom() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoProjectionCall4 call = reinterpret_cast<CuteQGeoProjectionCall4>(taken[4]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  double QGeoProjection::maximumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double maximumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoProjectionCall5 call = reinterpret_cast<CuteQGeoProjectionCall5>(taken[5]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  double QGeoProjection::minimumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double minimumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoProjectionCall6 call = reinterpret_cast<CuteQGeoProjectionCall6>(taken[6]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QGeoCoordinate QGeoProjection::itemPositionToCoordinate(const
  //      QDoubleVector2D &pos, bool clipToViewport) const
  QGeoCoordinate itemPositionToCoordinate(
      const QDoubleVector2D &pos,
      bool clipToViewport) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoProjectionCall7 call = reinterpret_cast<CuteQGeoProjectionCall7>(taken[7]);
      const QGeoCoordinate * given = call(this, &pos, clipToViewport, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QDoubleVector2D QGeoProjection::coordinateToItemPosition(const
  //      QGeoCoordinate &coordinate, bool clipToViewport) const
  QDoubleVector2D coordinateToItemPosition(
      const QGeoCoordinate &coordinate,
      bool clipToViewport) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoProjectionCall8 call = reinterpret_cast<CuteQGeoProjectionCall8>(taken[8]);
      const QDoubleVector2D * given = call(this, &coordinate, clipToViewport, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  ProjectionGroup QGeoProjection::projectionGroup() const
  QGeoProjection::ProjectionGroup projectionGroup() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoProjectionCall9 call = reinterpret_cast<CuteQGeoProjectionCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoProjection::ProjectionGroup>(given);
    }
    return {};
  }

  //  Datum QGeoProjection::datum() const
  QGeoProjection::Datum datum() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoProjectionCall10 call = reinterpret_cast<CuteQGeoProjectionCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoProjection::Datum>(given);
    }
    return {};
  }

  //  ProjectionType QGeoProjection::projectionType() const
  QGeoProjection::ProjectionType projectionType() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoProjectionCall11 call = reinterpret_cast<CuteQGeoProjectionCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoProjection::ProjectionType>(given);
    }
    return {};
  }

  //  QGeoCoordinate QGeoProjection::anchorCoordinateToPoint(const
  //      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
  QGeoCoordinate anchorCoordinateToPoint(
      const QGeoCoordinate &coordinate,
      const QPointF &anchorPoint) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoProjectionCall12 call = reinterpret_cast<CuteQGeoProjectionCall12>(taken[12]);
      const QGeoCoordinate * given = call(this, &coordinate, &anchorPoint, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjection::anchorCoordinateToPoint(coordinate, anchorPoint);
  }

  //  QGeoShape QGeoProjection::visibleRegion() const
  QGeoShape visibleRegion() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoProjectionCall13 call = reinterpret_cast<CuteQGeoProjectionCall13>(taken[13]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjection::visibleRegion();
  }

  //  bool QGeoProjection::setBearing(qreal bearing, const QGeoCoordinate
  //      &coordinate)
  bool setBearing(qreal bearing, const QGeoCoordinate &coordinate) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoProjectionCall14 call = reinterpret_cast<CuteQGeoProjectionCall14>(taken[14]);
      bool given = call(this, bearing, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoProjection::setBearing(bearing, coordinate);
  }

  //  QMatrix4x4 QGeoProjection::projectionTransformation() const
  QMatrix4x4 projectionTransformation() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoProjectionCall15 call = reinterpret_cast<CuteQGeoProjectionCall15>(taken[15]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QMatrix4x4 QGeoProjection::projectionTransformation_centered() const
  QMatrix4x4 projectionTransformation_centered() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoProjectionCall16 call = reinterpret_cast<CuteQGeoProjectionCall16>(taken[16]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  const QMatrix4x4 &QGeoProjection::qsgTransform() const
  const QMatrix4x4 &qsgTransform() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoProjectionCall17 call = reinterpret_cast<CuteQGeoProjectionCall17>(taken[17]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QDoubleVector3D QGeoProjection::centerMercator() const
  QDoubleVector3D centerMercator() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoProjectionCall18 call = reinterpret_cast<CuteQGeoProjectionCall18>(taken[18]);
      const QDoubleVector3D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QTransform QGeoProjection::itemToWindowTransform() const
  QTransform itemToWindowTransform() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQGeoProjectionCall19 call = reinterpret_cast<CuteQGeoProjectionCall19>(taken[19]);
      const QTransform * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjection::itemToWindowTransform();
  }
};

//  QGeoProjection::~QGeoProjection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoProjectionD1Ev(QGeoProjection *self) {
  delete self;
}

//  void QGeoProjection::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoProjection14setVisibleAreaERK6QRectF(
    QGeoProjection *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  void QGeoProjection::setViewportSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoProjection15setViewportSizeERK5QSize(
    QGeoProjection *self,
    const QSize *size) {
  self->setViewportSize(*size);
}

//  void QGeoProjection::setCameraData(const QGeoCameraData &cameraData, bool
//      force)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoProjection13setCameraDataERK14QGeoCameraDatab(
    QGeoProjection *self,
    const QGeoCameraData *cameraData,
    bool force) {
  self->setCameraData(*cameraData, force);
}

//  QGeoCameraData QGeoProjection::cameraData() const
extern "C" Q_DECL_EXPORT
QGeoCameraData *ritual_ZNK14QGeoProjection10cameraDataEv(
    const QGeoProjection *self) {
  return new QGeoCameraData(self->cameraData());
}

//  double QGeoProjection::minimumZoom() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoProjection11minimumZoomEv(
    const QGeoProjection *self) {
  return self->minimumZoom();
}

//  double QGeoProjection::maximumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoProjection27maximumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoProjection *self,
    const QGeoCameraData *cameraData) {
  return self->maximumCenterLatitudeAtZoom(*cameraData);
}

//  double QGeoProjection::minimumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoProjection27minimumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoProjection *self,
    const QGeoCameraData *cameraData) {
  return self->minimumCenterLatitudeAtZoom(*cameraData);
}

//  QGeoCoordinate QGeoProjection::itemPositionToCoordinate(const
//      QDoubleVector2D &pos, bool clipToViewport) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK14QGeoProjection24itemPositionToCoordinateERK15QDoubleVector2Db(
    const QGeoProjection *self,
    const QDoubleVector2D *pos,
    bool clipToViewport) {
  return new QGeoCoordinate(
      self->itemPositionToCoordinate(
          *pos,
          clipToViewport));
}

//  QDoubleVector2D QGeoProjection::coordinateToItemPosition(const
//      QGeoCoordinate &coordinate, bool clipToViewport) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK14QGeoProjection24coordinateToItemPositionERK14QGeoCoordinateb(
    const QGeoProjection *self,
    const QGeoCoordinate *coordinate,
    bool clipToViewport) {
  return new QDoubleVector2D(
      self->coordinateToItemPosition(
          *coordinate,
          clipToViewport));
}

//  ProjectionGroup QGeoProjection::projectionGroup() const
extern "C" Q_DECL_EXPORT
QGeoProjection::ProjectionGroup ritual_ZNK14QGeoProjection15projectionGroupEv(
    const QGeoProjection *self) {
  return self->projectionGroup();
}

//  Datum QGeoProjection::datum() const
extern "C" Q_DECL_EXPORT
QGeoProjection::Datum ritual_ZNK14QGeoProjection5datumEv(
    const QGeoProjection *self) {
  return self->datum();
}

//  ProjectionType QGeoProjection::projectionType() const
extern "C" Q_DECL_EXPORT
QGeoProjection::ProjectionType ritual_ZNK14QGeoProjection14projectionTypeEv(
    const QGeoProjection *self) {
  return self->projectionType();
}

//  QGeoCoordinate QGeoProjection::anchorCoordinateToPoint(const
//      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK14QGeoProjection23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF(
    const QGeoProjection *self,
    const QGeoCoordinate *coordinate,
    const QPointF *anchorPoint) {
  return new QGeoCoordinate(
      self->anchorCoordinateToPoint(
          *coordinate,
          *anchorPoint));
}

//  QGeoShape QGeoProjection::visibleRegion() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK14QGeoProjection13visibleRegionEv(
    const QGeoProjection *self) {
  return new QGeoShape(self->visibleRegion());
}

//  bool QGeoProjection::setBearing(qreal bearing, const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGeoProjection10setBearingEdRK14QGeoCoordinate(
    QGeoProjection *self,
    qreal bearing,
    const QGeoCoordinate *coordinate) {
  return self->setBearing(bearing, *coordinate);
}

//  QMatrix4x4 QGeoProjection::projectionTransformation() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK14QGeoProjection24projectionTransformationEv(
    const QGeoProjection *self) {
  return new QMatrix4x4(self->projectionTransformation());
}

//  QMatrix4x4 QGeoProjection::projectionTransformation_centered() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK14QGeoProjection33projectionTransformation_centeredEv(
    const QGeoProjection *self) {
  return new QMatrix4x4(self->projectionTransformation_centered());
}

//  const QMatrix4x4 &QGeoProjection::qsgTransform() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK14QGeoProjection12qsgTransformEv(
    const QGeoProjection *self) {
  return new QMatrix4x4(self->qsgTransform());
}

//  QDoubleVector3D QGeoProjection::centerMercator() const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK14QGeoProjection14centerMercatorEv(
    const QGeoProjection *self) {
  return new QDoubleVector3D(self->centerMercator());
}

//  void QGeoProjection::setItemToWindowTransform(const QTransform
//      &itemToWindowTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoProjection24setItemToWindowTransformERK10QTransform(
    QGeoProjection *self,
    const QTransform *itemToWindowTransform) {
  self->setItemToWindowTransform(*itemToWindowTransform);
}

//  QTransform QGeoProjection::itemToWindowTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK14QGeoProjection21itemToWindowTransformEv(
    const QGeoProjection *self) {
  return new QTransform(self->itemToWindowTransform());
}

//  a Python function taken by a CuteQGeoProjection, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoProjection(
    QGeoProjection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoProjection *>(self)->take(key, call);
}

//  QGeoCoordinate QGeoProjection::anchorCoordinateToPoint(const
//      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_own_ZNK14QGeoProjection23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF(
    const QGeoProjection *self,
    const QGeoCoordinate *coordinate,
    const QPointF *anchorPoint) {
  return new QGeoCoordinate(
      self->QGeoProjection::anchorCoordinateToPoint(
          *coordinate,
          *anchorPoint));
}

//  QGeoShape QGeoProjection::visibleRegion() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_own_ZNK14QGeoProjection13visibleRegionEv(
    const QGeoProjection *self) {
  return new QGeoShape(self->QGeoProjection::visibleRegion());
}

//  bool QGeoProjection::setBearing(qreal bearing, const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QGeoProjection10setBearingEdRK14QGeoCoordinate(
    QGeoProjection *self,
    qreal bearing,
    const QGeoCoordinate *coordinate) {
  return self->QGeoProjection::setBearing(bearing, *coordinate);
}

//  QTransform QGeoProjection::itemToWindowTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_own_ZNK14QGeoProjection21itemToWindowTransformEv(
    const QGeoProjection *self) {
  return new QTransform(self->QGeoProjection::itemToWindowTransform());
}
