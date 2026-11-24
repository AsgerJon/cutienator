//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeoshape.h>
#include <QtGui/qtransform.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoProjectionWebMercator that Python can take functions over in. Every QGeoProjectionWebMercator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef double (*CuteQGeoProjectionWebMercatorCall0)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQGeoProjectionWebMercatorCall1)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQGeoProjectionWebMercatorCall2)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQGeoProjectionWebMercatorCall3)(const void *, int *);
typedef const QDoubleVector3D * (*CuteQGeoProjectionWebMercatorCall4)(const void *, int *);
typedef double (*CuteQGeoProjectionWebMercatorCall5)(const void *, const QGeoCameraData *, int *);
typedef double (*CuteQGeoProjectionWebMercatorCall6)(const void *, const QGeoCameraData *, int *);
typedef void (*CuteQGeoProjectionWebMercatorCall7)(const void *, const QRectF *, int *);
typedef void (*CuteQGeoProjectionWebMercatorCall8)(const void *, const QSize *, int *);
typedef void (*CuteQGeoProjectionWebMercatorCall9)(const void *, const QGeoCameraData *, bool, int *);
typedef const QGeoCameraData * (*CuteQGeoProjectionWebMercatorCall10)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoProjectionWebMercatorCall11)(const void *, const QDoubleVector2D *, bool, int *);
typedef const QDoubleVector2D * (*CuteQGeoProjectionWebMercatorCall12)(const void *, const QGeoCoordinate *, bool, int *);
typedef int (*CuteQGeoProjectionWebMercatorCall13)(const void *, int *);
typedef int (*CuteQGeoProjectionWebMercatorCall14)(const void *, int *);
typedef int (*CuteQGeoProjectionWebMercatorCall15)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoProjectionWebMercatorCall16)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef bool (*CuteQGeoProjectionWebMercatorCall17)(const void *, qreal, const QGeoCoordinate *, int *);
typedef const QGeoShape * (*CuteQGeoProjectionWebMercatorCall18)(const void *, int *);
typedef const QTransform * (*CuteQGeoProjectionWebMercatorCall19)(const void *, int *);
class CuteQGeoProjectionWebMercator : public QGeoProjectionWebMercator {
public:
  using QGeoProjectionWebMercator::QGeoProjectionWebMercator;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QGeoProjection11minimumZoomEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection24projectionTransformationEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection33projectionTransformation_centeredEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection12qsgTransformEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection14centerMercatorEv")) {
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
    if (!std::strcmp(key, "_ZN14QGeoProjection14setVisibleAreaERK6QRectF")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoProjection15setViewportSizeERK5QSize")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoProjection13setCameraDataERK14QGeoCameraDatab")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection10cameraDataEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection24itemPositionToCoordinateERK15QDoubleVector2Db")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection24coordinateToItemPositionERK14QGeoCoordinateb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection15projectionGroupEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection5datumEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection14projectionTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoProjection10setBearingEdRK14QGeoCoordinate")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection13visibleRegionEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoProjection21itemToWindowTransformEv")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  double QGeoProjectionWebMercator::minimumZoom() const
  double minimumZoom() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall0 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall0>(taken[0]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoProjectionWebMercator::minimumZoom();
  }

  //  QMatrix4x4 QGeoProjectionWebMercator::projectionTransformation()
  //      const
  QMatrix4x4 projectionTransformation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall1 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall1>(taken[1]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::projectionTransformation();
  }

  //  QMatrix4x4
  //      QGeoProjectionWebMercator::projectionTransformation_centered()
  //      const
  QMatrix4x4 projectionTransformation_centered() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall2 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall2>(taken[2]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::projectionTransformation_centered();
  }

  //  const QMatrix4x4 &QGeoProjectionWebMercator::qsgTransform() const
  const QMatrix4x4 &qsgTransform() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall3 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall3>(taken[3]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::qsgTransform();
  }

  //  QDoubleVector3D QGeoProjectionWebMercator::centerMercator() const
  QDoubleVector3D centerMercator() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall4 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall4>(taken[4]);
      const QDoubleVector3D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::centerMercator();
  }

  //  double QGeoProjectionWebMercator::maximumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double maximumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall5 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall5>(taken[5]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return QGeoProjectionWebMercator::maximumCenterLatitudeAtZoom(cameraData);
  }

  //  double QGeoProjectionWebMercator::minimumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double minimumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall6 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall6>(taken[6]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return QGeoProjectionWebMercator::minimumCenterLatitudeAtZoom(cameraData);
  }

  //  void QGeoProjectionWebMercator::setVisibleArea(const QRectF
  //      &visibleArea)
  void setVisibleArea(const QRectF &visibleArea) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall7 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall7>(taken[7]);
      call(this, &visibleArea, &handled);
      if (handled) return;
    }
    QGeoProjectionWebMercator::setVisibleArea(visibleArea);
  }

  //  void QGeoProjectionWebMercator::setViewportSize(const QSize &size)
  void setViewportSize(const QSize &size) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall8 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall8>(taken[8]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QGeoProjectionWebMercator::setViewportSize(size);
  }

  //  void QGeoProjectionWebMercator::setCameraData(const QGeoCameraData
  //      &cameraData, bool force)
  void setCameraData(const QGeoCameraData &cameraData, bool force) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall9 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall9>(taken[9]);
      call(this, &cameraData, force, &handled);
      if (handled) return;
    }
    QGeoProjectionWebMercator::setCameraData(cameraData, force);
  }

  //  QGeoCameraData QGeoProjectionWebMercator::cameraData() const
  QGeoCameraData cameraData() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall10 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall10>(taken[10]);
      const QGeoCameraData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::cameraData();
  }

  //  QGeoCoordinate
  //      QGeoProjectionWebMercator::itemPositionToCoordinate(const
  //      QDoubleVector2D &pos, bool clipToViewport) const
  QGeoCoordinate itemPositionToCoordinate(
      const QDoubleVector2D &pos,
      bool clipToViewport) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall11 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall11>(taken[11]);
      const QGeoCoordinate * given = call(this, &pos, clipToViewport, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::itemPositionToCoordinate(pos, clipToViewport);
  }

  //  QDoubleVector2D
  //      QGeoProjectionWebMercator::coordinateToItemPosition(const
  //      QGeoCoordinate &coordinate, bool clipToViewport) const
  QDoubleVector2D coordinateToItemPosition(
      const QGeoCoordinate &coordinate,
      bool clipToViewport) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall12 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall12>(taken[12]);
      const QDoubleVector2D * given = call(this, &coordinate, clipToViewport, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::coordinateToItemPosition(coordinate, clipToViewport);
  }

  //  QGeoProjection::ProjectionGroup
  //      QGeoProjectionWebMercator::projectionGroup() const
  QGeoProjection::ProjectionGroup projectionGroup() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall13 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoProjection::ProjectionGroup>(given);
    }
    return QGeoProjectionWebMercator::projectionGroup();
  }

  //  QGeoProjection::Datum QGeoProjectionWebMercator::datum() const
  QGeoProjection::Datum datum() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall14 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoProjection::Datum>(given);
    }
    return QGeoProjectionWebMercator::datum();
  }

  //  QGeoProjection::ProjectionType
  //      QGeoProjectionWebMercator::projectionType() const
  QGeoProjection::ProjectionType projectionType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall15 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoProjection::ProjectionType>(given);
    }
    return QGeoProjectionWebMercator::projectionType();
  }

  //  QGeoCoordinate
  //      QGeoProjectionWebMercator::anchorCoordinateToPoint(const
  //      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
  QGeoCoordinate anchorCoordinateToPoint(
      const QGeoCoordinate &coordinate,
      const QPointF &anchorPoint) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall16 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall16>(taken[16]);
      const QGeoCoordinate * given = call(this, &coordinate, &anchorPoint, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::anchorCoordinateToPoint(coordinate, anchorPoint);
  }

  //  bool QGeoProjectionWebMercator::setBearing(qreal bearing, const
  //      QGeoCoordinate &coordinate)
  bool setBearing(qreal bearing, const QGeoCoordinate &coordinate) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall17 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall17>(taken[17]);
      bool given = call(this, bearing, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoProjectionWebMercator::setBearing(bearing, coordinate);
  }

  //  QGeoShape QGeoProjectionWebMercator::visibleRegion() const
  QGeoShape visibleRegion() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall18 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall18>(taken[18]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjectionWebMercator::visibleRegion();
  }

  //  QTransform QGeoProjection::itemToWindowTransform() const
  QTransform itemToWindowTransform() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQGeoProjectionWebMercatorCall19 call = reinterpret_cast<CuteQGeoProjectionWebMercatorCall19>(taken[19]);
      const QTransform * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoProjection::itemToWindowTransform();
  }
};

//  QGeoProjectionWebMercator::QGeoProjectionWebMercator()
extern "C" Q_DECL_EXPORT
QGeoProjectionWebMercator *ritual_ZN25QGeoProjectionWebMercatorC1Ev() {
  return new CuteQGeoProjectionWebMercator();
}

//  QGeoProjectionWebMercator::~QGeoProjectionWebMercator()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercatorD1Ev(
    QGeoProjectionWebMercator *self) {
  delete self;
}

//  double QGeoProjectionWebMercator::minimumZoom() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QGeoProjectionWebMercator11minimumZoomEv(
    const QGeoProjectionWebMercator *self) {
  return self->minimumZoom();
}

//  QMatrix4x4 QGeoProjectionWebMercator::projectionTransformation() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK25QGeoProjectionWebMercator24projectionTransformationEv(
    const QGeoProjectionWebMercator *self) {
  return new QMatrix4x4(self->projectionTransformation());
}

//  QMatrix4x4 QGeoProjectionWebMercator::projectionTransformation_centered()
//      const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK25QGeoProjectionWebMercator33projectionTransformation_centeredEv(
    const QGeoProjectionWebMercator *self) {
  return new QMatrix4x4(self->projectionTransformation_centered());
}

//  const QMatrix4x4 &QGeoProjectionWebMercator::qsgTransform() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK25QGeoProjectionWebMercator12qsgTransformEv(
    const QGeoProjectionWebMercator *self) {
  return new QMatrix4x4(self->qsgTransform());
}

//  QDoubleVector3D QGeoProjectionWebMercator::centerMercator() const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK25QGeoProjectionWebMercator14centerMercatorEv(
    const QGeoProjectionWebMercator *self) {
  return new QDoubleVector3D(self->centerMercator());
}

//  double QGeoProjectionWebMercator::maximumCenterLatitudeAtZoom(const
//      QGeoCameraData &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QGeoProjectionWebMercator27maximumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoProjectionWebMercator *self,
    const QGeoCameraData *cameraData) {
  return self->maximumCenterLatitudeAtZoom(*cameraData);
}

//  double QGeoProjectionWebMercator::minimumCenterLatitudeAtZoom(const
//      QGeoCameraData &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QGeoProjectionWebMercator27minimumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoProjectionWebMercator *self,
    const QGeoCameraData *cameraData) {
  return self->minimumCenterLatitudeAtZoom(*cameraData);
}

//  void QGeoProjectionWebMercator::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercator14setVisibleAreaERK6QRectF(
    QGeoProjectionWebMercator *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  void QGeoProjectionWebMercator::setViewportSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercator15setViewportSizeERK5QSize(
    QGeoProjectionWebMercator *self,
    const QSize *size) {
  self->setViewportSize(*size);
}

//  void QGeoProjectionWebMercator::setCameraData(const QGeoCameraData
//      &cameraData, bool force)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercator13setCameraDataERK14QGeoCameraDatab(
    QGeoProjectionWebMercator *self,
    const QGeoCameraData *cameraData,
    bool force) {
  self->setCameraData(*cameraData, force);
}

//  QGeoCameraData QGeoProjectionWebMercator::cameraData() const
extern "C" Q_DECL_EXPORT
QGeoCameraData *ritual_ZNK25QGeoProjectionWebMercator10cameraDataEv(
    const QGeoProjectionWebMercator *self) {
  return new QGeoCameraData(self->cameraData());
}

//  QGeoCoordinate QGeoProjectionWebMercator::itemPositionToCoordinate(const
//      QDoubleVector2D &pos, bool clipToViewport) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK25QGeoProjectionWebMercator24itemPositionToCoordinateERK15QDoubleVector2Db(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *pos,
    bool clipToViewport) {
  return new QGeoCoordinate(
      self->itemPositionToCoordinate(
          *pos,
          clipToViewport));
}

//  QDoubleVector2D QGeoProjectionWebMercator::coordinateToItemPosition(const
//      QGeoCoordinate &coordinate, bool clipToViewport) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK25QGeoProjectionWebMercator24coordinateToItemPositionERK14QGeoCoordinateb(
    const QGeoProjectionWebMercator *self,
    const QGeoCoordinate *coordinate,
    bool clipToViewport) {
  return new QDoubleVector2D(
      self->coordinateToItemPosition(
          *coordinate,
          clipToViewport));
}

//  QGeoProjection::ProjectionGroup
//      QGeoProjectionWebMercator::projectionGroup() const
extern "C" Q_DECL_EXPORT
QGeoProjection::ProjectionGroup ritual_ZNK25QGeoProjectionWebMercator15projectionGroupEv(
    const QGeoProjectionWebMercator *self) {
  return self->projectionGroup();
}

//  QGeoProjection::Datum QGeoProjectionWebMercator::datum() const
extern "C" Q_DECL_EXPORT
QGeoProjection::Datum ritual_ZNK25QGeoProjectionWebMercator5datumEv(
    const QGeoProjectionWebMercator *self) {
  return self->datum();
}

//  QGeoProjection::ProjectionType
//      QGeoProjectionWebMercator::projectionType() const
extern "C" Q_DECL_EXPORT
QGeoProjection::ProjectionType ritual_ZNK25QGeoProjectionWebMercator14projectionTypeEv(
    const QGeoProjectionWebMercator *self) {
  return self->projectionType();
}

//  QGeoCoordinate QGeoProjectionWebMercator::anchorCoordinateToPoint(const
//      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK25QGeoProjectionWebMercator23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF(
    const QGeoProjectionWebMercator *self,
    const QGeoCoordinate *coordinate,
    const QPointF *anchorPoint) {
  return new QGeoCoordinate(
      self->anchorCoordinateToPoint(
          *coordinate,
          *anchorPoint));
}

//  bool QGeoProjectionWebMercator::setBearing(qreal bearing, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QGeoProjectionWebMercator10setBearingEdRK14QGeoCoordinate(
    QGeoProjectionWebMercator *self,
    qreal bearing,
    const QGeoCoordinate *coordinate) {
  return self->setBearing(bearing, *coordinate);
}

//  QGeoShape QGeoProjectionWebMercator::visibleRegion() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK25QGeoProjectionWebMercator13visibleRegionEv(
    const QGeoProjectionWebMercator *self) {
  return new QGeoShape(self->visibleRegion());
}

//  double QGeoProjectionWebMercator::mapWidth() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QGeoProjectionWebMercator8mapWidthEv(
    const QGeoProjectionWebMercator *self) {
  return self->mapWidth();
}

//  double QGeoProjectionWebMercator::mapHeight() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QGeoProjectionWebMercator9mapHeightEv(
    const QGeoProjectionWebMercator *self) {
  return self->mapHeight();
}

//  QDoubleVector2D QGeoProjectionWebMercator::geoToMapProjection(const
//      QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK25QGeoProjectionWebMercator18geoToMapProjectionERK14QGeoCoordinate(
    const QGeoProjectionWebMercator *self,
    const QGeoCoordinate *coordinate) {
  return new QDoubleVector2D(self->geoToMapProjection(*coordinate));
}

//  QGeoCoordinate QGeoProjectionWebMercator::mapProjectionToGeo(const
//      QDoubleVector2D &projection) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK25QGeoProjectionWebMercator18mapProjectionToGeoERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *projection) {
  return new QGeoCoordinate(self->mapProjectionToGeo(*projection));
}

//  int QGeoProjectionWebMercator::projectionWrapFactor(const QDoubleVector2D
//      &projection) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QGeoProjectionWebMercator20projectionWrapFactorERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *projection) {
  return self->projectionWrapFactor(*projection);
}

//  QDoubleVector2D QGeoProjectionWebMercator::wrapMapProjection(const
//      QDoubleVector2D &projection) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK25QGeoProjectionWebMercator17wrapMapProjectionERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *projection) {
  return new QDoubleVector2D(self->wrapMapProjection(*projection));
}

//  QDoubleVector2D QGeoProjectionWebMercator::unwrapMapProjection(const
//      QDoubleVector2D &wrappedProjection) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK25QGeoProjectionWebMercator19unwrapMapProjectionERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *wrappedProjection) {
  return new QDoubleVector2D(self->unwrapMapProjection(*wrappedProjection));
}

//  QDoubleVector2D
//      QGeoProjectionWebMercator::wrappedMapProjectionToItemPosition(const
//      QDoubleVector2D &wrappedProjection) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK25QGeoProjectionWebMercator34wrappedMapProjectionToItemPositionERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *wrappedProjection) {
  return new QDoubleVector2D(
      self->wrappedMapProjectionToItemPosition(
          *wrappedProjection));
}

//  QDoubleVector2D
//      QGeoProjectionWebMercator::itemPositionToWrappedMapProjection(const
//      QDoubleVector2D &itemPosition) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK25QGeoProjectionWebMercator34itemPositionToWrappedMapProjectionERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *itemPosition) {
  return new QDoubleVector2D(
      self->itemPositionToWrappedMapProjection(
          *itemPosition));
}

//  QDoubleVector2D
//      QGeoProjectionWebMercator::geoToWrappedMapProjection(const
//      QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK25QGeoProjectionWebMercator25geoToWrappedMapProjectionERK14QGeoCoordinate(
    const QGeoProjectionWebMercator *self,
    const QGeoCoordinate *coordinate) {
  return new QDoubleVector2D(self->geoToWrappedMapProjection(*coordinate));
}

//  QGeoCoordinate QGeoProjectionWebMercator::wrappedMapProjectionToGeo(const
//      QDoubleVector2D &wrappedProjection) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK25QGeoProjectionWebMercator25wrappedMapProjectionToGeoERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *wrappedProjection) {
  return new QGeoCoordinate(
      self->wrappedMapProjectionToGeo(
          *wrappedProjection));
}

//  QMatrix4x4 QGeoProjectionWebMercator::quickItemTransformation(const
//      QGeoCoordinate &coordinate, const QPointF &anchorPoint, qreal
//      zoomLevel) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK25QGeoProjectionWebMercator23quickItemTransformationERK14QGeoCoordinateRK7QPointFd(
    const QGeoProjectionWebMercator *self,
    const QGeoCoordinate *coordinate,
    const QPointF *anchorPoint,
    qreal zoomLevel) {
  return new QMatrix4x4(
      self->quickItemTransformation(
          *coordinate,
          *anchorPoint,
          zoomLevel));
}

//  bool QGeoProjectionWebMercator::isProjectable(const QDoubleVector2D
//      &wrappedProjection) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QGeoProjectionWebMercator13isProjectableERK15QDoubleVector2D(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *wrappedProjection) {
  return self->isProjectable(*wrappedProjection);
}

//  QList<QDoubleVector2D> QGeoProjectionWebMercator::visibleGeometry() const
extern "C" Q_DECL_EXPORT
QList<QDoubleVector2D> *ritual_ZNK25QGeoProjectionWebMercator15visibleGeometryEv(
    const QGeoProjectionWebMercator *self) {
  return new QList<QDoubleVector2D>(self->visibleGeometry());
}

//  QList<QDoubleVector2D>
//      QGeoProjectionWebMercator::visibleGeometryExpanded() const
extern "C" Q_DECL_EXPORT
QList<QDoubleVector2D> *ritual_ZNK25QGeoProjectionWebMercator23visibleGeometryExpandedEv(
    const QGeoProjectionWebMercator *self) {
  return new QList<QDoubleVector2D>(self->visibleGeometryExpanded());
}

//  QList<QDoubleVector2D> QGeoProjectionWebMercator::projectableGeometry()
//      const
extern "C" Q_DECL_EXPORT
QList<QDoubleVector2D> *ritual_ZNK25QGeoProjectionWebMercator19projectableGeometryEv(
    const QGeoProjectionWebMercator *self) {
  return new QList<QDoubleVector2D>(self->projectableGeometry());
}

//  void QGeoProjectionWebMercator::setupCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercator11setupCameraEv(
    QGeoProjectionWebMercator *self) {
  self->setupCamera();
}

//  void QGeoProjectionWebMercator::updateVisibleRegion()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercator19updateVisibleRegionEv(
    QGeoProjectionWebMercator *self) {
  self->updateVisibleRegion();
}

//  a Python function taken by a CuteQGeoProjectionWebMercator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoProjectionWebMercator(
    QGeoProjectionWebMercator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoProjectionWebMercator *>(self)->take(key, call);
}

//  double QGeoProjectionWebMercator::minimumZoom() const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK25QGeoProjectionWebMercator11minimumZoomEv(
    const QGeoProjectionWebMercator *self) {
  return self->QGeoProjectionWebMercator::minimumZoom();
}

//  QMatrix4x4 QGeoProjectionWebMercator::projectionTransformation() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_own_ZNK25QGeoProjectionWebMercator24projectionTransformationEv(
    const QGeoProjectionWebMercator *self) {
  return new QMatrix4x4(
      self->QGeoProjectionWebMercator::projectionTransformation());
}

//  QMatrix4x4 QGeoProjectionWebMercator::projectionTransformation_centered()
//      const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_own_ZNK25QGeoProjectionWebMercator33projectionTransformation_centeredEv(
    const QGeoProjectionWebMercator *self) {
  return new QMatrix4x4(
      self->QGeoProjectionWebMercator::projectionTransformation_centered());
}

//  const QMatrix4x4 &QGeoProjectionWebMercator::qsgTransform() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_own_ZNK25QGeoProjectionWebMercator12qsgTransformEv(
    const QGeoProjectionWebMercator *self) {
  return new QMatrix4x4(self->QGeoProjectionWebMercator::qsgTransform());
}

//  QDoubleVector3D QGeoProjectionWebMercator::centerMercator() const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_own_ZNK25QGeoProjectionWebMercator14centerMercatorEv(
    const QGeoProjectionWebMercator *self) {
  return new QDoubleVector3D(
      self->QGeoProjectionWebMercator::centerMercator());
}

//  double QGeoProjectionWebMercator::maximumCenterLatitudeAtZoom(const
//      QGeoCameraData &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK25QGeoProjectionWebMercator27maximumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoProjectionWebMercator *self,
    const QGeoCameraData *cameraData) {
  return self->QGeoProjectionWebMercator::maximumCenterLatitudeAtZoom(
      *cameraData);
}

//  double QGeoProjectionWebMercator::minimumCenterLatitudeAtZoom(const
//      QGeoCameraData &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK25QGeoProjectionWebMercator27minimumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoProjectionWebMercator *self,
    const QGeoCameraData *cameraData) {
  return self->QGeoProjectionWebMercator::minimumCenterLatitudeAtZoom(
      *cameraData);
}

//  void QGeoProjectionWebMercator::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGeoProjectionWebMercator14setVisibleAreaERK6QRectF(
    QGeoProjectionWebMercator *self,
    const QRectF *visibleArea) {
  self->QGeoProjectionWebMercator::setVisibleArea(*visibleArea);
}

//  void QGeoProjectionWebMercator::setViewportSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGeoProjectionWebMercator15setViewportSizeERK5QSize(
    QGeoProjectionWebMercator *self,
    const QSize *size) {
  self->QGeoProjectionWebMercator::setViewportSize(*size);
}

//  void QGeoProjectionWebMercator::setCameraData(const QGeoCameraData
//      &cameraData, bool force)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGeoProjectionWebMercator13setCameraDataERK14QGeoCameraDatab(
    QGeoProjectionWebMercator *self,
    const QGeoCameraData *cameraData,
    bool force) {
  self->QGeoProjectionWebMercator::setCameraData(*cameraData, force);
}

//  QGeoCameraData QGeoProjectionWebMercator::cameraData() const
extern "C" Q_DECL_EXPORT
QGeoCameraData *ritual_own_ZNK25QGeoProjectionWebMercator10cameraDataEv(
    const QGeoProjectionWebMercator *self) {
  return new QGeoCameraData(self->QGeoProjectionWebMercator::cameraData());
}

//  QGeoCoordinate QGeoProjectionWebMercator::itemPositionToCoordinate(const
//      QDoubleVector2D &pos, bool clipToViewport) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_own_ZNK25QGeoProjectionWebMercator24itemPositionToCoordinateERK15QDoubleVector2Db(
    const QGeoProjectionWebMercator *self,
    const QDoubleVector2D *pos,
    bool clipToViewport) {
  return new QGeoCoordinate(
      self->QGeoProjectionWebMercator::itemPositionToCoordinate(
          *pos,
          clipToViewport));
}

//  QDoubleVector2D QGeoProjectionWebMercator::coordinateToItemPosition(const
//      QGeoCoordinate &coordinate, bool clipToViewport) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_own_ZNK25QGeoProjectionWebMercator24coordinateToItemPositionERK14QGeoCoordinateb(
    const QGeoProjectionWebMercator *self,
    const QGeoCoordinate *coordinate,
    bool clipToViewport) {
  return new QDoubleVector2D(
      self->QGeoProjectionWebMercator::coordinateToItemPosition(
          *coordinate,
          clipToViewport));
}

//  QGeoProjection::ProjectionGroup
//      QGeoProjectionWebMercator::projectionGroup() const
extern "C" Q_DECL_EXPORT
QGeoProjection::ProjectionGroup ritual_own_ZNK25QGeoProjectionWebMercator15projectionGroupEv(
    const QGeoProjectionWebMercator *self) {
  return self->QGeoProjectionWebMercator::projectionGroup();
}

//  QGeoProjection::Datum QGeoProjectionWebMercator::datum() const
extern "C" Q_DECL_EXPORT
QGeoProjection::Datum ritual_own_ZNK25QGeoProjectionWebMercator5datumEv(
    const QGeoProjectionWebMercator *self) {
  return self->QGeoProjectionWebMercator::datum();
}

//  QGeoProjection::ProjectionType
//      QGeoProjectionWebMercator::projectionType() const
extern "C" Q_DECL_EXPORT
QGeoProjection::ProjectionType ritual_own_ZNK25QGeoProjectionWebMercator14projectionTypeEv(
    const QGeoProjectionWebMercator *self) {
  return self->QGeoProjectionWebMercator::projectionType();
}

//  QGeoCoordinate QGeoProjectionWebMercator::anchorCoordinateToPoint(const
//      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_own_ZNK25QGeoProjectionWebMercator23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF(
    const QGeoProjectionWebMercator *self,
    const QGeoCoordinate *coordinate,
    const QPointF *anchorPoint) {
  return new QGeoCoordinate(
      self->QGeoProjectionWebMercator::anchorCoordinateToPoint(
          *coordinate,
          *anchorPoint));
}

//  bool QGeoProjectionWebMercator::setBearing(qreal bearing, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QGeoProjectionWebMercator10setBearingEdRK14QGeoCoordinate(
    QGeoProjectionWebMercator *self,
    qreal bearing,
    const QGeoCoordinate *coordinate) {
  return self->QGeoProjectionWebMercator::setBearing(bearing, *coordinate);
}

//  QGeoShape QGeoProjectionWebMercator::visibleRegion() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_own_ZNK25QGeoProjectionWebMercator13visibleRegionEv(
    const QGeoProjectionWebMercator *self) {
  return new QGeoShape(self->QGeoProjectionWebMercator::visibleRegion());
}
