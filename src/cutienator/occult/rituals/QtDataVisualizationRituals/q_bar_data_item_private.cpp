//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/qbardataitem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qbardataitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qbardataitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qbardataitem.cpp, line 113, as _ZN19QBarDataItemPrivateD1Ev
inline QBarDataItemPrivate::~QBarDataItemPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataitem.cpp, line 109, as _ZN19QBarDataItemPrivateC1Ev
inline QBarDataItemPrivate::QBarDataItemPrivate()
{
}
//  -----------------------------------------------------------------------

//  QBarDataItemPrivate::QBarDataItemPrivate()
extern "C" Q_DECL_EXPORT
QBarDataItemPrivate *ritual_ZN19QBarDataItemPrivateC1Ev() {
  return new QBarDataItemPrivate();
}

//  QBarDataItemPrivate::~QBarDataItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBarDataItemPrivateD1Ev(QBarDataItemPrivate *self) {
  delete self;
}
