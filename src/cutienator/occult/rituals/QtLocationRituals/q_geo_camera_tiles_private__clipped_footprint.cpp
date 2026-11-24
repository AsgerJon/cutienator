//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QGeoCameraTilesPrivate::ClippedFootprint::ClippedFootprint()
extern "C" Q_DECL_EXPORT
QGeoCameraTilesPrivate::ClippedFootprint *ritual_ZN22QGeoCameraTilesPrivate16ClippedFootprintC1Ev() {
  return new QGeoCameraTilesPrivate::ClippedFootprint();
}

//  QGeoCameraTilesPrivate::ClippedFootprint::ClippedFootprint(const
//      PolygonVector &left_, const PolygonVector &mid_, const PolygonVector
//      &right_)
extern "C" Q_DECL_EXPORT
QGeoCameraTilesPrivate::ClippedFootprint *ritual_ZN22QGeoCameraTilesPrivate16ClippedFootprintC1ERK5QListI15QDoubleVector3DES5_S5_(
    const QList<QDoubleVector3D> *left_,
    const QList<QDoubleVector3D> *mid_,
    const QList<QDoubleVector3D> *right_) {
  return new QGeoCameraTilesPrivate::ClippedFootprint(
      *left_,
      *mid_,
      *right_);
}

//  QGeoCameraTilesPrivate::ClippedFootprint::~ClippedFootprint()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraTilesPrivate16ClippedFootprintD1Ev(
    QGeoCameraTilesPrivate::ClippedFootprint *self) {
  delete self;
}
