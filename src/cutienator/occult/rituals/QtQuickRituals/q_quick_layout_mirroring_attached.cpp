//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1509, as _ZNK29QQuickLayoutMirroringAttached7enabledEv
inline bool QQuickLayoutMirroringAttached::enabled() const
{
    return itemPrivate ? itemPrivate->effectiveLayoutMirror : false;
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1514, as _ZN29QQuickLayoutMirroringAttached10setEnabledEb
inline void QQuickLayoutMirroringAttached::setEnabled(bool enabled)
{
    if (!itemPrivate)
        return;

    itemPrivate->isMirrorImplicit = false;
    if (enabled != itemPrivate->effectiveLayoutMirror) {
        itemPrivate->setLayoutMirror(enabled);
        if (itemPrivate->inheritMirrorFromItem)
             itemPrivate->resolveLayoutMirror();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1527, as _ZN29QQuickLayoutMirroringAttached12resetEnabledEv
inline void QQuickLayoutMirroringAttached::resetEnabled()
{
    if (itemPrivate && !itemPrivate->isMirrorImplicit) {
        itemPrivate->isMirrorImplicit = true;
        itemPrivate->resolveLayoutMirror();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1535, as _ZNK29QQuickLayoutMirroringAttached15childrenInheritEv
inline bool QQuickLayoutMirroringAttached::childrenInherit() const
{
    return itemPrivate ? itemPrivate->inheritMirrorFromItem : false;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickLayoutMirroringAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickLayoutMirroringAttached10metaObjectEv(
    const QQuickLayoutMirroringAttached *self) {
  return self->metaObject();
}

//  void QQuickLayoutMirroringAttached::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached24qt_qmlMarker_uncreatableEv(
    QQuickLayoutMirroringAttached *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickLayoutMirroringAttached::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached21qt_qmlMarker_attachedEv(
    QQuickLayoutMirroringAttached *self) {
  self->qt_qmlMarker_attached();
}

//  bool QQuickLayoutMirroringAttached::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickLayoutMirroringAttached7enabledEv(
    const QQuickLayoutMirroringAttached *self) {
  return self->enabled();
}

//  void QQuickLayoutMirroringAttached::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached10setEnabledEb(
    QQuickLayoutMirroringAttached *self,
    bool a0) {
  self->setEnabled(a0);
}

//  void QQuickLayoutMirroringAttached::resetEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached12resetEnabledEv(
    QQuickLayoutMirroringAttached *self) {
  self->resetEnabled();
}

//  bool QQuickLayoutMirroringAttached::childrenInherit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickLayoutMirroringAttached15childrenInheritEv(
    const QQuickLayoutMirroringAttached *self) {
  return self->childrenInherit();
}
