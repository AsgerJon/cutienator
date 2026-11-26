//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qabstract3dseries_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qabstract3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAbstract3DSeriesChangeBitField::QAbstract3DSeriesChangeBitField()
extern "C" Q_DECL_EXPORT
QAbstract3DSeriesChangeBitField *ritual_ZN31QAbstract3DSeriesChangeBitFieldC1Ev() {
  return new QAbstract3DSeriesChangeBitField();
}

//  QAbstract3DSeriesChangeBitField::~QAbstract3DSeriesChangeBitField()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstract3DSeriesChangeBitFieldD1Ev(
    QAbstract3DSeriesChangeBitField *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
