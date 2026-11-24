//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetanimator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmainwindowlayout_p.h"
#if QT_CONFIG(dockwidget)
#include "qdockarealayout_p.h"
#include "qdockwidget.h"
#include "qdockwidget_p.h"
#endif
#if QT_CONFIG(toolbar)
#include "qtoolbar_p.h"
#include "qtoolbar.h"
#include "qtoolbarlayout_p.h"
#endif
#include "qmainwindow.h"
#if QT_CONFIG(rubberband)
#include "qrubberband.h"
#endif
#if QT_CONFIG(tabbar)
#include "qtabbar_p.h"
#endif
#include <qapplication.h>
#if QT_CONFIG(draganddrop)
#include <qdrag.h>
#endif
#include <qmimedata.h>
#if QT_CONFIG(statusbar)
#include <qstatusbar.h>
#endif
#include <qstring.h>
#include <qstyle.h>
#include <qstylepainter.h>
#include <qvarlengtharray.h>
#include <qstack.h>
#include <qmap.h>
#include <qpointer.h>
#ifndef QT_NO_DEBUG_STREAM
#  include <qdebug.h>
#  include <qtextstream.h>
#endif
#include <private/qmenu_p.h>
#include <private/qapplication_p.h>
#include <private/qlayoutengine_p.h>
#include <private/qwidgetresizehandler_p.h>
#include <qpa/qplatformwindow_p.h>
#include <QScopedValueRollback>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <optional>
#include "qwidgetanimator_p.h"
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qstyle.h>
#if QT_CONFIG(mainwindow)
#include <private/qmainwindowlayout_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2749, as _ZN17QMainWindowLayout17animationFinishedEP7QWidget
inline void QMainWindowLayout::animationFinished(QWidget *widget)
{
    //this function is called from within the Widget Animator whenever an animation is finished
    //on a certain widget
#if QT_CONFIG(toolbar)
    if (QToolBar *tb = qobject_cast<QToolBar*>(widget)) {
        QToolBarLayout *tbl = qobject_cast<QToolBarLayout*>(tb->layout());
        if (tbl->animating) {
            tbl->animating = false;
            if (tbl->expanded)
                tbl->layoutActions(tb->size());
            tb->update();
        }
    }
#endif

    if (widget == pluggingWidget) {

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
        if (QDockWidgetGroupWindow *dwgw = qobject_cast<QDockWidgetGroupWindow *>(widget)) {
            // When the animated widget was a QDockWidgetGroupWindow, it means each of the
            // embedded QDockWidget needs to be plugged back into the QMainWindow layout.
            savedState.clear();
            QDockAreaLayoutInfo *srcInfo = dwgw->layoutInfo();
            const QDockAreaLayoutInfo *srcTabInfo = dwgw->tabLayoutInfo();
            QDockAreaLayoutInfo *dstParentInfo;
            QList<int> dstPath;

            if (currentHoveredFloat) {
                dstPath = currentHoveredFloat->layoutInfo()->indexOf(widget);
                Q_ASSERT(dstPath.size() >= 1);
                dstParentInfo = currentHoveredFloat->layoutInfo()->info(dstPath);
            } else {
                dstPath = layoutState.dockAreaLayout.indexOf(widget);
                Q_ASSERT(dstPath.size() >= 2);
                dstParentInfo = layoutState.dockAreaLayout.info(dstPath);
            }
            Q_ASSERT(dstParentInfo);
            int idx = dstPath.constLast();
            Q_ASSERT(dstParentInfo->item_list[idx].widgetItem->widget() == dwgw);
            if (dstParentInfo->tabbed && srcTabInfo) {
                // merge the two tab widgets
                delete dstParentInfo->item_list[idx].widgetItem;
                dstParentInfo->item_list.removeAt(idx);
                std::copy(srcTabInfo->item_list.cbegin(), srcTabInfo->item_list.cend(),
                          std::inserter(dstParentInfo->item_list,
                                        dstParentInfo->item_list.begin() + idx));
                quintptr currentId = srcTabInfo->currentTabId();
                *srcInfo = QDockAreaLayoutInfo();
                dstParentInfo->reparentWidgets(currentHoveredFloat ? currentHoveredFloat.data()
                                                                   : parentWidget());
                dstParentInfo->updateTabBar();
                dstParentInfo->setCurrentTabId(currentId);
            } else {
                QDockAreaLayoutItem &item = dstParentInfo->item_list[idx];
                Q_ASSERT(item.widgetItem->widget() == dwgw);
                delete item.widgetItem;
                item.widgetItem = nullptr;
                item.subinfo = new QDockAreaLayoutInfo(std::move(*srcInfo));
                *srcInfo = QDockAreaLayoutInfo();
                item.subinfo->reparentWidgets(currentHoveredFloat ? currentHoveredFloat.data()
                                                                  : parentWidget());
                item.subinfo->setTabBarShape(dstParentInfo->tabBarShape);
            }
            dwgw->destroyOrHideIfEmpty();
        }
#endif

        if (QDockWidget *dw = qobject_cast<QDockWidget*>(widget)) {
            dw->setParent(currentHoveredFloat ? currentHoveredFloat.data() : parentWidget());
            dw->show();
            dw->d_func()->plug(currentGapRect);
        }
#endif
#if QT_CONFIG(toolbar)
        if (QToolBar *tb = qobject_cast<QToolBar*>(widget))
            tb->d_func()->plug(currentGapRect);
#endif

        savedState.clear();
        currentGapPos.clear();
        pluggingWidget = nullptr;
#if QT_CONFIG(dockwidget)
        setCurrentHoveredFloat(nullptr);
#endif
        //applying the state will make sure that the currentGap is updated correctly
        //and all the geometries (especially the one from the central widget) is correct
        layoutState.apply(QWidgetAnimator::AnimationRule::Stop);

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
        if (qobject_cast<QDockWidget*>(widget) != nullptr) {
            // info() might return null if the widget is destroyed while
            // animating but before the animationFinished signal is received.
            if (QDockAreaLayoutInfo *info = dockInfo(widget))
                info->setCurrentTab(widget);
        }
#endif
#endif
    }

    if (!widgetAnimator.animating()) {
        //all animations are finished
#if QT_CONFIG(dockwidget)
        parentWidget()->update(layoutState.dockAreaLayout.separatorRegion());
#if QT_CONFIG(tabbar)
        showTabBars();
#endif // QT_CONFIG(tabbar)
#endif // QT_CONFIG(dockwidget)
    }

    updateGapIndicator();
}

//  from src/widgets/widgets/qwidgetanimator.cpp, line 78, as _ZNK15QWidgetAnimator9animatingEv
inline bool QWidgetAnimator::animating() const
{
    auto isActiveAnimation = [](const QPointer<QPropertyAnimation> &p) { return !p.isNull(); };
    return !std::all_of(m_animation_map.begin(), m_animation_map.end(), isActiveAnimation);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWidgetAnimator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QWidgetAnimator10metaObjectEv(
    const QWidgetAnimator *self) {
  return self->metaObject();
}

//  bool QWidgetAnimator::animating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWidgetAnimator9animatingEv(const QWidgetAnimator *self) {
  return self->animating();
}
