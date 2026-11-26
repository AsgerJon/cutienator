//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qaxisalignedboundingbox_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qaxisalignedboundingbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>

//  Qt3DRender::QAxisAlignedBoundingBox::QAxisAlignedBoundingBox()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAxisAlignedBoundingBox *ritual_ZN10Qt3DRender23QAxisAlignedBoundingBoxC1Ev() {
  return new Qt3DRender::QAxisAlignedBoundingBox();
}

//  Qt3DRender::QAxisAlignedBoundingBox::QAxisAlignedBoundingBox(const
//      std::vector<QVector3D> &points)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAxisAlignedBoundingBox *ritual_ZN10Qt3DRender23QAxisAlignedBoundingBoxC1ERKSt6vectorI9QVector3DSaIS2_EE(
    const std::vector<QVector3D> *points) {
  return new Qt3DRender::QAxisAlignedBoundingBox(*points);
}

//  void Qt3DRender::QAxisAlignedBoundingBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox5clearEv(
    Qt3DRender::QAxisAlignedBoundingBox *self) {
  self->clear();
}

//  bool Qt3DRender::QAxisAlignedBoundingBox::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox6isNullEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return self->isNull();
}

//  void Qt3DRender::QAxisAlignedBoundingBox::update(const
//      std::vector<QVector3D> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox6updateERKSt6vectorI9QVector3DSaIS2_EE(
    Qt3DRender::QAxisAlignedBoundingBox *self,
    const std::vector<QVector3D> *points) {
  self->update(*points);
}

//  QVector3D Qt3DRender::QAxisAlignedBoundingBox::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox6centerEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return new QVector3D(self->center());
}

//  QVector3D Qt3DRender::QAxisAlignedBoundingBox::radii() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox5radiiEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return new QVector3D(self->radii());
}

//  QVector3D Qt3DRender::QAxisAlignedBoundingBox::minPoint() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox8minPointEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return new QVector3D(self->minPoint());
}

//  QVector3D Qt3DRender::QAxisAlignedBoundingBox::maxPoint() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox8maxPointEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return new QVector3D(self->maxPoint());
}

//  float Qt3DRender::QAxisAlignedBoundingBox::xExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox7xExtentEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return self->xExtent();
}

//  float Qt3DRender::QAxisAlignedBoundingBox::yExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox7yExtentEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return self->yExtent();
}

//  float Qt3DRender::QAxisAlignedBoundingBox::zExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox7zExtentEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return self->zExtent();
}

//  float Qt3DRender::QAxisAlignedBoundingBox::maxExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox9maxExtentEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return self->maxExtent();
}

//  float Qt3DRender::QAxisAlignedBoundingBox::minExtent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox9minExtentEv(
    const Qt3DRender::QAxisAlignedBoundingBox *self) {
  return self->minExtent();
}

//  bool Qt3DRender::QAxisAlignedBoundingBox::contains(const QVector3D &pt)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox8containsERK9QVector3D(
    const Qt3DRender::QAxisAlignedBoundingBox *self,
    const QVector3D *pt) {
  return self->contains(*pt);
}

//  void Qt3DRender::QAxisAlignedBoundingBox::expandToContain(const QVector3D
//      &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox15expandToContainERK9QVector3D(
    Qt3DRender::QAxisAlignedBoundingBox *self,
    const QVector3D *pt) {
  self->expandToContain(*pt);
}

//  void Qt3DRender::QAxisAlignedBoundingBox::expandToContain(const
//      QAxisAlignedBoundingBox &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox15expandToContainERKS0_(
    Qt3DRender::QAxisAlignedBoundingBox *self,
    const Qt3DRender::QAxisAlignedBoundingBox *other) {
  self->expandToContain(*other);
}

//  QAxisAlignedBoundingBox
//      Qt3DRender::QAxisAlignedBoundingBox::transformBy(const QMatrix4x4
//      &mat) const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAxisAlignedBoundingBox *ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox11transformByERK10QMatrix4x4(
    const Qt3DRender::QAxisAlignedBoundingBox *self,
    const QMatrix4x4 *mat) {
  return new Qt3DRender::QAxisAlignedBoundingBox(self->transformBy(*mat));
}

//  QAxisAlignedBoundingBox
//      &Qt3DRender::QAxisAlignedBoundingBox::transform(const QMatrix4x4
//      &mat)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAxisAlignedBoundingBox *ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox9transformERK10QMatrix4x4(
    Qt3DRender::QAxisAlignedBoundingBox *self,
    const QMatrix4x4 *mat) {
  return &(self->transform(*mat));
}

//  Qt3DRender::QAxisAlignedBoundingBox::~QAxisAlignedBoundingBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAxisAlignedBoundingBoxD1Ev(
    Qt3DRender::QAxisAlignedBoundingBox *self) {
  delete self;
}
