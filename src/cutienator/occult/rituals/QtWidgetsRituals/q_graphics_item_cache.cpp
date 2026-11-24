//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgraphicsitem.h"
#include "qgraphicsscene.h"
#include "qgraphicsscene_p.h"
#include "qgraphicssceneevent.h"
#include "qgraphicsview.h"
#include "qgraphicswidget.h"
#include "qgraphicsproxywidget.h"
#include "qgraphicsscenebsptreeindex_p.h"
#include <QtCore/qbitarray.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstack.h>
#include <QtCore/qvariant.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qnumeric.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmapcache.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtGui/qinputmethod.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/qgraphicseffect.h>
#endif
#include <private/qgraphicsitem_p.h>
#include <private/qgraphicswidget_p.h>
#include <private/qwidgettextcontrol_p.h>
#include <private/qtextdocumentlayout_p.h>
#include <private/qtextengine_p.h>
#include <private/qwidget_p.h>
#include <private/qapplication_p.h>
#include <private/qgesturemanager_p.h>
#include <private/qdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsitem.cpp, line 1484, as _ZN18QGraphicsItemCache5purgeEv
inline void QGraphicsItemCache::purge()
{
    QPixmapCache::remove(key);
    key = QPixmapCache::Key();
    const auto &constDeviceData = deviceData; // avoid detach
    for (const auto &data : constDeviceData)
        QPixmapCache::remove(data.key);
    deviceData.clear();
    allExposed = true;
    exposed.clear();
}
//  -----------------------------------------------------------------------

//  QGraphicsItemCache::QGraphicsItemCache()
extern "C" Q_DECL_EXPORT
QGraphicsItemCache *ritual_ZN18QGraphicsItemCacheC1Ev() {
  return new QGraphicsItemCache();
}

//  void QGraphicsItemCache::purge()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsItemCache5purgeEv(QGraphicsItemCache *self) {
  self->purge();
}

//  QGraphicsItemCache::~QGraphicsItemCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsItemCacheD1Ev(QGraphicsItemCache *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
