//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickrendercontrol.h>
#include <QtQml/qjsengine.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <QtQuick/private/qquickscreen_p.h>
#include <QtQuick/private/qquicksafearea_p.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qpen.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qstylehints.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtGui/qinputmethod.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQuick/private/qquickstategroup_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickaccessibleattached_p.h>
#include <QtQuick/private/qquickattachedpropertypropagator_p.h>
#include <QtQuick/private/qquickhoverhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtCore/private/qdebug_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#if QT_CONFIG(cursor)
# include <QtGui/qcursor.h>
#endif
#if QT_CONFIG(accessibility)
# include <QtGui/private/qaccessiblecache_p.h>
#endif
#include <QtCore/qpointer.h>
#include <algorithm>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 4046, as _ZN10QQuickItem19UpdatePaintNodeDataC1Ev
inline QQuickItem::UpdatePaintNodeData::UpdatePaintNodeData()
: transformNode(nullptr)
{
}
//  -----------------------------------------------------------------------

//  QQuickItem::UpdatePaintNodeData::UpdatePaintNodeData()
extern "C" Q_DECL_EXPORT
QQuickItem::UpdatePaintNodeData *ritual_ZN10QQuickItem19UpdatePaintNodeDataC1Ev() {
  return new QQuickItem::UpdatePaintNodeData();
}

//  QQuickItem::UpdatePaintNodeData::~UpdatePaintNodeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem19UpdatePaintNodeDataD1Ev(
    QQuickItem::UpdatePaintNodeData *self) {
  delete self;
}
