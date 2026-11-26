//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qsurfacedataitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qsurfacedataitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qsurfacedataitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataitem.cpp, line 116, as _ZN23QSurfaceDataItemPrivateD1Ev
inline QSurfaceDataItemPrivate::~QSurfaceDataItemPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataitem.cpp, line 112, as _ZN23QSurfaceDataItemPrivateC1Ev
inline QSurfaceDataItemPrivate::QSurfaceDataItemPrivate()
{
}
//  -----------------------------------------------------------------------

//  QSurfaceDataItemPrivate::QSurfaceDataItemPrivate()
extern "C" Q_DECL_EXPORT
QSurfaceDataItemPrivate *ritual_ZN23QSurfaceDataItemPrivateC1Ev() {
  return new QSurfaceDataItemPrivate();
}

//  QSurfaceDataItemPrivate::~QSurfaceDataItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurfaceDataItemPrivateD1Ev(QSurfaceDataItemPrivate *self) {
  delete self;
}
