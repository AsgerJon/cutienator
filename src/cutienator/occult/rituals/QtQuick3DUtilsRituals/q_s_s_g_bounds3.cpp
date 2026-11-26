//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/private/qssgbounds3_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/utils/qssgbounds3.cpp, line 29, as _ZN11QSSGBounds314boundsOfPointsERK9QVector3DS2_
inline QSSGBounds3 QSSGBounds3::boundsOfPoints(const QVector3D &v0, const QVector3D &v1)
{
    return QSSGBounds3(QSSGUtils::vec3::minimum(v0, v1), QSSGUtils::vec3::maximum(v0, v1));
}

//  from ../qtquick3d/src/utils/qssgbounds3.cpp, line 34, as _ZN11QSSGBounds311basisExtentERK9QVector3DRK14QGenericMatrixILi3ELi3EfES2_
inline QSSGBounds3 QSSGBounds3::basisExtent(const QVector3D &center, const QMatrix3x3 &basis, const QVector3D &extent)
{
    // extended basis vectors
    QVector3D c0 = QVector3D(basis(0, 0), basis(1, 0), basis(2, 0)) * extent.x();
    QVector3D c1 = QVector3D(basis(0, 1), basis(1, 1), basis(2, 1)) * extent.y();
    QVector3D c2 = QVector3D(basis(0, 2), basis(1, 2), basis(2, 2)) * extent.z();

    QVector3D w;
    // find combination of base vectors that produces max. distance for each component = sum of
    // abs()
    w.setX(qAbs(c0.x()) + qAbs(c1.x()) + qAbs(c2.x()));
    w.setY(qAbs(c0.y()) + qAbs(c1.y()) + qAbs(c2.y()));
    w.setZ(qAbs(c0.z()) + qAbs(c1.z()) + qAbs(c2.z()));

    return QSSGBounds3(center - w, center + w);
}
//  -----------------------------------------------------------------------

//  QSSGBounds3::QSSGBounds3()
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds3C1Ev() {
  return new QSSGBounds3();
}

//  QSSGBounds3::QSSGBounds3(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds3C1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QSSGBounds3(a0);
}

//  QSSGBounds3::QSSGBounds3(const QVector3D &minimum, const QVector3D
//      &maximum)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds3C1ERK9QVector3DS2_(
    const QVector3D *minimum,
    const QVector3D *maximum) {
  return new QSSGBounds3(*minimum, *maximum);
}

//  QSSGBounds3::QSSGBounds3(const QSSGBoxPoints &points)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds3C1ERKSt5arrayI9QVector3DLm8EE(
    const QSSGBoxPoints *points) {
  return new QSSGBounds3(*points);
}

//  QSSGBounds3 QSSGBounds3::boundsOfPoints(const QVector3D &v0, const
//      QVector3D &v1)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds314boundsOfPointsERK9QVector3DS2_(
    const QVector3D *v0,
    const QVector3D *v1) {
  return new QSSGBounds3(QSSGBounds3::boundsOfPoints(*v0, *v1));
}

//  QSSGBounds3 QSSGBounds3::centerExtents(const QVector3D &center, const
//      QVector3D &extent)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds313centerExtentsERK9QVector3DS2_(
    const QVector3D *center,
    const QVector3D *extent) {
  return new QSSGBounds3(QSSGBounds3::centerExtents(*center, *extent));
}

//  QSSGBounds3 QSSGBounds3::basisExtent(const QVector3D &center, const
//      QMatrix3x3 &basis, const QVector3D &extent)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds311basisExtentERK9QVector3DRK14QGenericMatrixILi3ELi3EfES2_(
    const QVector3D *center,
    const QMatrix3x3 *basis,
    const QVector3D *extent) {
  return new QSSGBounds3(QSSGBounds3::basisExtent(*center, *basis, *extent));
}

//  QSSGBounds3 QSSGBounds3::transform(const QMatrix3x3 &matrix, const
//      QSSGBounds3 &bounds)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN11QSSGBounds39transformERK14QGenericMatrixILi3ELi3EfERKS_(
    const QMatrix3x3 *matrix,
    const QSSGBounds3 *bounds) {
  return new QSSGBounds3(QSSGBounds3::transform(*matrix, *bounds));
}

//  void QSSGBounds3::setEmpty()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds38setEmptyEv(QSSGBounds3 *self) {
  self->setEmpty();
}

//  void QSSGBounds3::setInfinite()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds311setInfiniteEv(QSSGBounds3 *self) {
  self->setInfinite();
}

//  void QSSGBounds3::include(const QVector3D &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds37includeERK9QVector3D(
    QSSGBounds3 *self,
    const QVector3D *v) {
  self->include(*v);
}

//  void QSSGBounds3::include(const QSSGBounds3 &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds37includeERKS_(
    QSSGBounds3 *self,
    const QSSGBounds3 *b) {
  self->include(*b);
}

//  bool QSSGBounds3::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSSGBounds37isEmptyEv(const QSSGBounds3 *self) {
  return self->isEmpty();
}

//  bool QSSGBounds3::intersects(const QSSGBounds3 &b) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSSGBounds310intersectsERKS_(
    const QSSGBounds3 *self,
    const QSSGBounds3 *b) {
  return self->intersects(*b);
}

//  bool QSSGBounds3::intersects1D(const QSSGBounds3 &a, quint32 axis) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSSGBounds312intersects1DERKS_j(
    const QSSGBounds3 *self,
    const QSSGBounds3 *a,
    quint32 axis) {
  return self->intersects1D(*a, axis);
}

//  bool QSSGBounds3::contains(const QVector3D &v) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSSGBounds38containsERK9QVector3D(
    const QSSGBounds3 *self,
    const QVector3D *v) {
  return self->contains(*v);
}

//  bool QSSGBounds3::isInside(const QSSGBounds3 &box) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSSGBounds38isInsideERKS_(
    const QSSGBounds3 *self,
    const QSSGBounds3 *box) {
  return self->isInside(*box);
}

//  QVector3D QSSGBounds3::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QSSGBounds36centerEv(const QSSGBounds3 *self) {
  return new QVector3D(self->center());
}

//  float QSSGBounds3::center(quint32 axis) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QSSGBounds36centerEj(
    const QSSGBounds3 *self,
    quint32 axis) {
  return self->center(axis);
}

//  float QSSGBounds3::extents(quint32 axis) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QSSGBounds37extentsEj(
    const QSSGBounds3 *self,
    quint32 axis) {
  return self->extents(axis);
}

//  QVector3D QSSGBounds3::dimensions() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QSSGBounds310dimensionsEv(const QSSGBounds3 *self) {
  return new QVector3D(self->dimensions());
}

//  QVector3D QSSGBounds3::extents() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QSSGBounds37extentsEv(const QSSGBounds3 *self) {
  return new QVector3D(self->extents());
}

//  void QSSGBounds3::scale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds35scaleEf(QSSGBounds3 *self, float scale) {
  self->scale(scale);
}

//  void QSSGBounds3::fatten(double distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds36fattenEd(QSSGBounds3 *self, double distance) {
  self->fatten(distance);
}

//  bool QSSGBounds3::isFinite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSSGBounds38isFiniteEv(const QSSGBounds3 *self) {
  return self->isFinite();
}

//  QSSGBoxPoints QSSGBounds3::toQSSGBoxPointsNoEmptyCheck() const
extern "C" Q_DECL_EXPORT
QSSGBoxPoints *ritual_ZNK11QSSGBounds327toQSSGBoxPointsNoEmptyCheckEv(
    const QSSGBounds3 *self) {
  return new QSSGBoxPoints(self->toQSSGBoxPointsNoEmptyCheck());
}

//  QSSGBoxPoints QSSGBounds3::toQSSGBoxPoints() const
extern "C" Q_DECL_EXPORT
QSSGBoxPoints *ritual_ZNK11QSSGBounds315toQSSGBoxPointsEv(
    const QSSGBounds3 *self) {
  return new QSSGBoxPoints(self->toQSSGBoxPoints());
}

//  void QSSGBounds3::transform(const QMatrix4x4 &inMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds39transformERK10QMatrix4x4(
    QSSGBounds3 *self,
    const QMatrix4x4 *inMatrix) {
  self->transform(*inMatrix);
}

//  QVector3D QSSGBounds3::getSupport(const QVector3D &direction) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QSSGBounds310getSupportERK9QVector3D(
    const QSSGBounds3 *self,
    const QVector3D *direction) {
  return new QVector3D(self->getSupport(*direction));
}

//  QSSGBounds3::~QSSGBounds3()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGBounds3D1Ev(QSSGBounds3 *self) {
  delete self;
}

//  a QSSGBoxPoints a ritual of QSSGBounds3 gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGBounds3__QSSGBoxPoints(QSSGBoxPoints *self) {
  delete self;
}
