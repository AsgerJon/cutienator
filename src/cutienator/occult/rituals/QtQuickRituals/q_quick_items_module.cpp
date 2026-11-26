//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemsmodule_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickhandlerpoint_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemsmodule_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickitemsmodule_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/private/qquickfocusscope_p.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtQuick/private/qquicktextinput_p.h>
#include <QtQuick/private/qquicktextedit_p.h>
#include <QtQuick/qquicktextdocument.h>
#include <QtQuick/private/qquickimage_p.h>
#include <QtQuick/private/qquickborderimage_p.h>
#include <QtQuick/private/qquickscalegrid_p_p.h>
#include <QtQuick/private/qquickmousearea_p.h>
#include <QtQuick/private/qquickpincharea_p.h>
#include <QtQuick/private/qquickflickable_p.h>
#include <QtQuick/private/qquickflickable_p_p.h>
#if QT_CONFIG(quick_listview)
#include <QtQuick/private/qquicklistview_p.h>
#endif
#if QT_CONFIG(quick_gridview)
#include <QtQuick/private/qquickgridview_p.h>
#endif
#if QT_CONFIG(quick_pathview)
#include <QtQuick/private/qquickpathview_p.h>
#endif
#if QT_CONFIG(quick_tableview)
#include <QtQuick/private/qquicktableview_p.h>
#endif
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuick/private/qquickitemviewtransition_p.h>
#endif
#if QT_CONFIG(quick_path)
#include <QtQuick/private/qquickpath_p.h>
#include <QtQuick/private/qquickpathinterpolator_p.h>
#endif
#if QT_CONFIG(quick_positioners)
#include <QtQuick/private/qquickpositioners_p.h>
#endif
#if QT_CONFIG(quick_repeater)
#include <QtQuick/private/qquickrepeater_p.h>
#endif
#include <QtQuick/private/qquickloader_p.h>
#if QT_CONFIG(quick_animatedimage)
#include <QtQuick/private/qquickanimatedimage_p.h>
#endif
#if QT_CONFIG(quick_flipable)
#include <QtQuick/private/qquickflipable_p.h>
#endif
#include <QtQuick/private/qquicktranslate_p.h>
#include <QtQuick/private/qquickstateoperations_p.h>
#include <QtQuick/private/qquickitemanimation_p.h>
#if QT_CONFIG(quick_canvas)
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQuick/private/qquickcontext2d_p.h>
#endif
#include <QtQuick/qquickitemgrabresult.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/private/qquicksprite_p.h>
#include <QtQuick/private/qquickspritesequence_p.h>
#include <QtQuick/private/qquickanimatedsprite_p.h>
#endif
#include <QtQuick/private/qquickgraphicsinfo_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/private/qquickshadereffectsource_p.h>
#include <QtQuick/private/qquickshadereffect_p.h>
#include <QtQuick/private/qquickshadereffectmesh_p.h>
#endif
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/private/qquickdrag_p.h>
#include <QtQuick/private/qquickdroparea_p.h>
#endif
#include <QtQuick/private/qquickmultipointtoucharea_p.h>
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitemsmodule.cpp, line 91, as local:qquickitemsmodule.cpp:qquickitem_autoParent
static QQmlPrivate::AutoParentResult qquickitem_autoParent(QObject *obj, QObject *parent)
{
    if (QQuickItem *parentItem = qmlobject_cast<QQuickItem *>(parent)) {
        if (QQuickItem *item = qmlobject_cast<QQuickItem *>(obj)) {
            // An Item has another Item
            item->setParentItem(parentItem);
            return QQmlPrivate::Parented;
        } else if (QQuickPointerHandler *handler = qmlobject_cast<QQuickPointerHandler *>(obj)) {
            QQuickItemPrivate::get(parentItem)->addPointerHandler(handler);
            handler->setParent(parent);
            return QQmlPrivate::Parented;
        }
        return QQmlPrivate::IncompatibleObject;
    } else if (QQuickWindow *parentWindow = qmlobject_cast<QQuickWindow *>(parent)) {
        if (QQuickItem *item = qmlobject_cast<QQuickItem *>(obj)) {
            // The parent of an Item inside a Window is actually the implicit content Item
            item->setParentItem(parentWindow->contentItem());
            return QQmlPrivate::Parented;
        } else if (QQuickPointerHandler *handler = qmlobject_cast<QQuickPointerHandler *>(obj)) {
            QQuickItemPrivate::get(parentWindow->contentItem())->addPointerHandler(handler);
            handler->setParent(parentWindow->contentItem());
            return QQmlPrivate::Parented;
        }
        return QQmlPrivate::IncompatibleObject;
    } else if (qmlobject_cast<QQuickItem *>(obj)) {
        return QQmlPrivate::IncompatibleParent;
    }
    return QQmlPrivate::IncompatibleObject;
}

//  from ../qtdeclarative/src/quick/items/qquickitemsmodule.cpp, line 121, as local:qquickitemsmodule.cpp:qt_quickitems_defineModule
static void qt_quickitems_defineModule()
{
    QQmlPrivate::RegisterAutoParent autoparent = { 0, &qquickitem_autoParent };
    QQmlPrivate::qmlregister(QQmlPrivate::AutoParentRegistration, &autoparent);

    qRegisterMetaType<QQuickAnchorLine>("QQuickAnchorLine");
    qRegisterMetaType<QQuickHandlerPoint>();
}

//  from ../qtdeclarative/src/quick/items/qquickitemsmodule.cpp, line 137, as _ZN17QQuickItemsModule12defineModuleEv
inline void QQuickItemsModule::defineModule()
{
//    initResources();
    qt_quickitems_defineModule();
}
//  -----------------------------------------------------------------------

//  void QQuickItemsModule::defineModule()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemsModule12defineModuleEv() {
  QQuickItemsModule::defineModule();
}

//  QQuickItemsModule::~QQuickItemsModule()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemsModuleD1Ev(QQuickItemsModule *self) {
  delete self;
}
