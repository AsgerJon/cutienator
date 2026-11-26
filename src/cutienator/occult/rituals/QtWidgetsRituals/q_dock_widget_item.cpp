//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qproxystyle.h>
#include <QtGui/qwindow.h>
#include <QtGui/qscreen.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qtoolbutton.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qdockwidget_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qdockwidget.cpp, line 569, as _ZN15QDockWidgetItemC1EP11QDockWidget
inline QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
    : QWidgetItem(dockWidget)
{
}

//  from src/widgets/widgets/qdockwidget.cpp, line 574, as _ZNK15QDockWidgetItem11minimumSizeEv
inline QSize QDockWidgetItem::minimumSize() const
{
    QSize widgetMin(0, 0);
    if (QLayoutItem *item = dockWidgetChildItem())
        widgetMin = item->minimumSize();
    return dockWidgetLayout()->sizeFromContent(widgetMin, false);
}

//  from src/widgets/widgets/qdockwidget.cpp, line 582, as _ZNK15QDockWidgetItem11maximumSizeEv
inline QSize QDockWidgetItem::maximumSize() const
{
    if (QLayoutItem *item = dockWidgetChildItem()) {
        return dockWidgetLayout()->sizeFromContent(item->maximumSize(), false);
    } else {
        return QSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX);
    }
}

//  from src/widgets/widgets/qdockwidget.cpp, line 592, as _ZNK15QDockWidgetItem8sizeHintEv
inline QSize QDockWidgetItem::sizeHint() const
{
    if (QLayoutItem *item = dockWidgetChildItem()) {
         return dockWidgetLayout()->sizeFromContent(item->sizeHint(), false);
    } else {
        return QWidgetItem::sizeHint();
    }
}
//  -----------------------------------------------------------------------

//  QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
extern "C" Q_DECL_EXPORT
QDockWidgetItem *ritual_ZN15QDockWidgetItemC1EP11QDockWidget(
    QDockWidget *dockWidget) {
  return new QDockWidgetItem(dockWidget);
}

//  QSize QDockWidgetItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QDockWidgetItem11minimumSizeEv(
    const QDockWidgetItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QDockWidgetItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QDockWidgetItem11maximumSizeEv(
    const QDockWidgetItem *self) {
  return new QSize(self->maximumSize());
}

//  QSize QDockWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QDockWidgetItem8sizeHintEv(const QDockWidgetItem *self) {
  return new QSize(self->sizeHint());
}

//  QLayoutItem *QDockWidgetItem::dockWidgetChildItem() const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK15QDockWidgetItem19dockWidgetChildItemEv(
    const QDockWidgetItem *self) {
  return self->dockWidgetChildItem();
}

//  QDockWidgetLayout *QDockWidgetItem::dockWidgetLayout() const
extern "C" Q_DECL_EXPORT
QDockWidgetLayout *ritual_ZNK15QDockWidgetItem16dockWidgetLayoutEv(
    const QDockWidgetItem *self) {
  return self->dockWidgetLayout();
}

//  QSize QDockWidgetItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QDockWidgetItem11minimumSizeEv(
    const QDockWidgetItem *self) {
  return new QSize(self->QDockWidgetItem::minimumSize());
}

//  QSize QDockWidgetItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QDockWidgetItem11maximumSizeEv(
    const QDockWidgetItem *self) {
  return new QSize(self->QDockWidgetItem::maximumSize());
}

//  QSize QDockWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QDockWidgetItem8sizeHintEv(
    const QDockWidgetItem *self) {
  return new QSize(self->QDockWidgetItem::sizeHint());
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
