//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/formbuilderextra_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/formbuilderextra_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "formbuilderextra_p.h"
#include "abstractformbuilder.h"
#include "properties_p.h"
#include "resourcebuilder_p.h"
#include "textbuilder_p.h"
#include "ui4_p.h"
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qgridlayout.h>
#if QT_CONFIG(fontcombobox)
#  include <QtWidgets/qfontcombobox.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qversionnumber.h>
#include <climits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttools/src/designer/src/lib/uilib/formbuilderextra.cpp, line 42, as _ZN17QFormBuilderExtra16CustomWidgetDataC1EPK15DomCustomWidget
inline QFormBuilderExtra::CustomWidgetData::CustomWidgetData(const DomCustomWidget *dcw) :
    addPageMethod(dcw->elementAddPageMethod()),
    baseClass(dcw->elementExtends()),
    isContainer(dcw->hasElementContainer() && dcw->elementContainer() != 0)
{
}
//  -----------------------------------------------------------------------

//  QFormBuilderExtra::CustomWidgetData::CustomWidgetData(const
//      DomCustomWidget *dc)
extern "C" Q_DECL_EXPORT
QFormBuilderExtra::CustomWidgetData *ritual_ZN17QFormBuilderExtra16CustomWidgetDataC1EPK15DomCustomWidget(
    const DomCustomWidget *dc) {
  return new QFormBuilderExtra::CustomWidgetData(dc);
}

//  QFormBuilderExtra::CustomWidgetData::~CustomWidgetData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra16CustomWidgetDataD1Ev(
    QFormBuilderExtra::CustomWidgetData *self) {
  delete self;
}
