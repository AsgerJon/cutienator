//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dobject_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/q3dobject_p.h>
#include <QtDataVisualization/private/q3dscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/q3dobject.cpp, line 121, as _ZN16Q3DObjectPrivateC1EP9Q3DObject
inline Q3DObjectPrivate::Q3DObjectPrivate(Q3DObject *q) :
    q_ptr(q),
    m_isDirty(true)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dobject.cpp, line 127, as _ZN16Q3DObjectPrivateD1Ev
inline Q3DObjectPrivate::~Q3DObjectPrivate()
{

}
//  -----------------------------------------------------------------------

//  Q3DObjectPrivate::Q3DObjectPrivate(Q3DObject *q)
extern "C" Q_DECL_EXPORT
Q3DObjectPrivate *ritual_ZN16Q3DObjectPrivateC1EP9Q3DObject(Q3DObject *q) {
  return new Q3DObjectPrivate(q);
}

//  Q3DObjectPrivate::~Q3DObjectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DObjectPrivateD1Ev(Q3DObjectPrivate *self) {
  delete self;
}
