//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dlight_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dlight_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "q3dlight_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/q3dlight.cpp, line 80, as _ZN15Q3DLightPrivateC1EP8Q3DLight
inline Q3DLightPrivate::Q3DLightPrivate(Q3DLight *q) :
    q_ptr(q),
    m_automaticLight(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dlight.cpp, line 86, as _ZN15Q3DLightPrivateD1Ev
inline Q3DLightPrivate::~Q3DLightPrivate()
{
}
//  -----------------------------------------------------------------------

//  Q3DLightPrivate::Q3DLightPrivate(Q3DLight *q)
extern "C" Q_DECL_EXPORT
Q3DLightPrivate *ritual_ZN15Q3DLightPrivateC1EP8Q3DLight(Q3DLight *q) {
  return new Q3DLightPrivate(q);
}

//  Q3DLightPrivate::~Q3DLightPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DLightPrivateD1Ev(Q3DLightPrivate *self) {
  delete self;
}
