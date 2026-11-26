//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/q3dscene_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/q3dscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Q3DSceneChangeBitField::Q3DSceneChangeBitField()
extern "C" Q_DECL_EXPORT
Q3DSceneChangeBitField *ritual_ZN22Q3DSceneChangeBitFieldC1Ev() {
  return new Q3DSceneChangeBitField();
}

//  Q3DSceneChangeBitField::~Q3DSceneChangeBitField()
extern "C" Q_DECL_EXPORT
void ritual_ZN22Q3DSceneChangeBitFieldD1Ev(Q3DSceneChangeBitField *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
