//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qkeyframe.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qkeyframe.h>
#include <QtGui/qvectornd.h>

//  Qt3DAnimation::QKeyFrame::QKeyFrame()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyFrame *ritual_ZN13Qt3DAnimation9QKeyFrameC1Ev() {
  return new Qt3DAnimation::QKeyFrame();
}

//  Qt3DAnimation::QKeyFrame::QKeyFrame(QVector2D coords)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyFrame *ritual_ZN13Qt3DAnimation9QKeyFrameC1E9QVector2D(
    const QVector2D *coords) {
  return new Qt3DAnimation::QKeyFrame(*coords);
}

//  Qt3DAnimation::QKeyFrame::QKeyFrame(QVector2D coords, QVector2D lh,
//      QVector2D rh)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyFrame *ritual_ZN13Qt3DAnimation9QKeyFrameC1E9QVector2DS1_S1_(
    const QVector2D *coords,
    const QVector2D *lh,
    const QVector2D *rh) {
  return new Qt3DAnimation::QKeyFrame(*coords, *lh, *rh);
}

//  void Qt3DAnimation::QKeyFrame::setCoordinates(QVector2D coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9QKeyFrame14setCoordinatesE9QVector2D(
    Qt3DAnimation::QKeyFrame *self,
    const QVector2D *coords) {
  self->setCoordinates(*coords);
}

//  QVector2D Qt3DAnimation::QKeyFrame::coordinates() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK13Qt3DAnimation9QKeyFrame11coordinatesEv(
    const Qt3DAnimation::QKeyFrame *self) {
  return new QVector2D(self->coordinates());
}

//  void Qt3DAnimation::QKeyFrame::setLeftControlPoint(QVector2D lh)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9QKeyFrame19setLeftControlPointE9QVector2D(
    Qt3DAnimation::QKeyFrame *self,
    const QVector2D *lh) {
  self->setLeftControlPoint(*lh);
}

//  QVector2D Qt3DAnimation::QKeyFrame::leftControlPoint() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK13Qt3DAnimation9QKeyFrame16leftControlPointEv(
    const Qt3DAnimation::QKeyFrame *self) {
  return new QVector2D(self->leftControlPoint());
}

//  void Qt3DAnimation::QKeyFrame::setRightControlPoint(QVector2D rh)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9QKeyFrame20setRightControlPointE9QVector2D(
    Qt3DAnimation::QKeyFrame *self,
    const QVector2D *rh) {
  self->setRightControlPoint(*rh);
}

//  QVector2D Qt3DAnimation::QKeyFrame::rightControlPoint() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK13Qt3DAnimation9QKeyFrame17rightControlPointEv(
    const Qt3DAnimation::QKeyFrame *self) {
  return new QVector2D(self->rightControlPoint());
}

//  void Qt3DAnimation::QKeyFrame::setInterpolationType(InterpolationType
//      interp)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9QKeyFrame20setInterpolationTypeENS0_17InterpolationTypeE(
    Qt3DAnimation::QKeyFrame *self,
    Qt3DAnimation::QKeyFrame::InterpolationType interp) {
  self->setInterpolationType(interp);
}

//  InterpolationType Qt3DAnimation::QKeyFrame::interpolationType() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyFrame::InterpolationType ritual_ZNK13Qt3DAnimation9QKeyFrame17interpolationTypeEv(
    const Qt3DAnimation::QKeyFrame *self) {
  return self->interpolationType();
}

//  bool operator==(const QKeyFrame &a0, const QKeyFrame &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationeqERKNS_9QKeyFrameES2_(
    const Qt3DAnimation::QKeyFrame *a0,
    const Qt3DAnimation::QKeyFrame *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(const QKeyFrame &a0, const QKeyFrame &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationneERKNS_9QKeyFrameES2_(
    const Qt3DAnimation::QKeyFrame *a0,
    const Qt3DAnimation::QKeyFrame *a1) {
  return operator!=(*a0, *a1);
}

//  Qt3DAnimation::QKeyFrame::~QKeyFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9QKeyFrameD1Ev(Qt3DAnimation::QKeyFrame *self) {
  delete self;
}
