//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcustom3dvolume_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustom3dvolume_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCustomVolumeDirtyBitField::QCustomVolumeDirtyBitField()
extern "C" Q_DECL_EXPORT
QCustomVolumeDirtyBitField *ritual_ZN26QCustomVolumeDirtyBitFieldC1Ev() {
  return new QCustomVolumeDirtyBitField();
}

//  QCustomVolumeDirtyBitField::~QCustomVolumeDirtyBitField()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCustomVolumeDirtyBitFieldD1Ev(
    QCustomVolumeDirtyBitField *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
