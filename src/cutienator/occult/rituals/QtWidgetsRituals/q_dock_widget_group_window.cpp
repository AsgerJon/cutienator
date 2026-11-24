//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mainwindow)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qdockwidget.h>
#include <QtCore/qlist.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qdockarealayout.cpp, line 96, as _ZNK19QDockAreaLayoutItem4skipEv
inline bool QDockAreaLayoutItem::skip() const
{
    if (placeHolderItem != nullptr)
        return true;

    if (flags & GapItem)
        return false;

    if (widgetItem != nullptr)
        return widgetItem->isEmpty();

    if (subinfo != nullptr) {
        for (int i = 0; i < subinfo->item_list.size(); ++i) {
            if (!subinfo->item_list.at(i).skip())
                return false;
        }
    }

    return true;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 543, as _ZNK22QDockWidgetGroupWindow21hasVisibleDockWidgetsEv
#if QT_CONFIG(dockwidget)
inline bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const
{
    const auto &children = findChildren<QDockWidget *>(Qt::FindChildrenRecursively);
    for (auto child : children) {
        // WA_WState_Visible is set on the dock widget, associated to the active tab
        // and unset on all others.
        // WA_WState_Hidden is set if the dock widgets have been explicitly hidden.
        // This is the relevant information to check (equivalent to !child->isHidden()).
        if (!child->testAttribute(Qt::WA_WState_Hidden))
            return true;
    }
    return false;
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 723, as _ZN22QDockWidgetGroupWindow10childEventEP11QChildEvent
#if QT_CONFIG(dockwidget)
inline void QDockWidgetGroupWindow::childEvent(QChildEvent *event)
{
    switch (event->type()) {
    case QEvent::ChildRemoved:
        if (auto *dockWidget = qobject_cast<QDockWidget *>(event->child()))
            dockWidget->removeEventFilter(this);
        destroyIfSingleItemLeft();
        break;
    case QEvent::ChildAdded:
        if (auto *dockWidget = qobject_cast<QDockWidget *>(event->child())) {
            dockWidget->installEventFilter(this);
            if (objectName().isEmpty())
                setObjectName(dockWidget->objectName() + QLatin1String("_groupWindow"));
        }
        break;
    default:
        break;
    }
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 743, as _ZN22QDockWidgetGroupWindow11eventFilterEP7QObjectP6QEvent
#if QT_CONFIG(dockwidget)
inline bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent *event)
{
    auto *dockWidget = qobject_cast<QDockWidget *>(obj);
    if (!dockWidget)
        return QWidget::eventFilter(obj, event);

    switch (event->type()) {
    case QEvent::Close:
        // We don't want closed dock widgets in a floating tab
        // => dock it to the main dock, before closing;
        reparentToMainWindow(dockWidget);
        dockWidget->setFloating(false);
        break;

    case QEvent::Hide:
        // if the dock widget is not an active tab, it is hidden anyway.
        // if it is the active tab, hide the whole group.
        if (dockWidget->isVisible())
            hide();
        break;

    default:
        break;
    }
    return QWidget::eventFilter(obj, event);
}
#endif  // QT_CONFIG(dockwidget)
//  -----------------------------------------------------------------------

//  const QMetaObject *QDockWidgetGroupWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDockWidgetGroupWindow10metaObjectEv(
    const QDockWidgetGroupWindow *self) {
  return self->metaObject();
}

#if QT_CONFIG(dockwidget)
//  bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDockWidgetGroupWindow21hasVisibleDockWidgetsEv(
    const QDockWidgetGroupWindow *self) {
  return self->hasVisibleDockWidgets();
}
#endif  // QT_CONFIG(dockwidget)

//  void QDockWidgetGroupWindow::childEvent(QChildEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDockWidgetGroupWindow10childEventEP11QChildEvent(
    QDockWidgetGroupWindow *self,
    QChildEvent *event) {
  self->childEvent(event);
}

//  QList<QDockWidget *> QDockWidgetGroupWindow::dockWidgets() const
extern "C" Q_DECL_EXPORT
QList<QDockWidget *> *ritual_ZNK22QDockWidgetGroupWindow11dockWidgetsEv(
    const QDockWidgetGroupWindow *self) {
  return new QList<QDockWidget *>(self->dockWidgets());
}

//  bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDockWidgetGroupWindow11eventFilterEP7QObjectP6QEvent(
    QDockWidgetGroupWindow *self,
    QObject *obj,
    QEvent *event) {
  return self->eventFilter(obj, event);
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(mainwindow)
