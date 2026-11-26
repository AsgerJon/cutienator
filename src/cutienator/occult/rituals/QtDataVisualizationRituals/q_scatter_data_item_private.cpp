//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qscatterdataitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qscatterdataitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qscatterdataitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataitem.cpp, line 141, as _ZN23QScatterDataItemPrivateD1Ev
inline QScatterDataItemPrivate::~QScatterDataItemPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataitem.cpp, line 137, as _ZN23QScatterDataItemPrivateC1Ev
inline QScatterDataItemPrivate::QScatterDataItemPrivate()
{
}
//  -----------------------------------------------------------------------

//  QScatterDataItemPrivate::QScatterDataItemPrivate()
extern "C" Q_DECL_EXPORT
QScatterDataItemPrivate *ritual_ZN23QScatterDataItemPrivateC1Ev() {
  return new QScatterDataItemPrivate();
}

//  QScatterDataItemPrivate::~QScatterDataItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatterDataItemPrivateD1Ev(QScatterDataItemPrivate *self) {
  delete self;
}
