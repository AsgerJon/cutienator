//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "QtWidgets/qapplication.h"
#include "QtWidgets/qwidget.h"
#if QT_CONFIG(tabbar)
#include "QtWidgets/qtabbar.h"
#endif
#include "QtWidgets/qstyle.h"
#include "QtWidgets/qapplication.h"
#include "QtCore/qvariant.h"
#include "qdockarealayout_p.h"
#include "qdockwidget.h"
#include "qmainwindow.h"
#include "qmainwindowlayout_p.h"
#include "qmenu_p.h"
#include "qdockwidget_p.h"
#include <private/qlayoutengine_p.h>
#if QT_CONFIG(toolbar)
#include "qtoolbar.h"
#include "qtoolbarlayout_p.h"
#endif
#include <qpainter.h>
#include <qstyleoption.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qdockarealayout.cpp, line 52, as _ZN16QPlaceHolderItemC1EP7QWidget
inline QPlaceHolderItem::QPlaceHolderItem(QWidget *w)
{
    objectName = w->objectName();
    hidden = w->isHidden();
    window = w->isWindow();
    if (window)
        topLevelRect = w->geometry();
}
//  -----------------------------------------------------------------------

//  QPlaceHolderItem::QPlaceHolderItem()
extern "C" Q_DECL_EXPORT
QPlaceHolderItem *ritual_ZN16QPlaceHolderItemC1Ev() {
  return new QPlaceHolderItem();
}

//  QPlaceHolderItem::QPlaceHolderItem(QWidget *w)
extern "C" Q_DECL_EXPORT
QPlaceHolderItem *ritual_ZN16QPlaceHolderItemC1EP7QWidget(QWidget *w) {
  return new QPlaceHolderItem(w);
}

//  QPlaceHolderItem::~QPlaceHolderItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaceHolderItemD1Ev(QPlaceHolderItem *self) {
  delete self;
}

#endif  // QT_CONFIG(dockwidget)
