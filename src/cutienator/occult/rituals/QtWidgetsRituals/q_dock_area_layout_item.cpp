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

//  from src/widgets/widgets/qdockarealayout.cpp, line 307, as _ZNK19QDockAreaLayoutInfo11minimumSizeEv
inline QSize QDockAreaLayoutInfo::minimumSize() const
{
    if (isEmpty())
        return QSize(0, 0);

    int a = 0, b = 0;
    bool first = true;
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

        QSize min_size = item.minimumSize();
#if QT_CONFIG(tabbar)
        if (tabbed) {
            a = qMax(a, pick(o, min_size));
        } else
#endif
        {
            if (!first)
                a += *sep;
            a += pick(o, min_size);
        }
        b = qMax(b, perp(o, min_size));

        first = false;
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

#if QT_CONFIG(tabbar)
    QSize tbm = tabBarMinimumSize();
    if (!tbm.isNull()) {
        switch (tabBarShape) {
            case QTabBar::RoundedNorth:
            case QTabBar::RoundedSouth:
            case QTabBar::TriangularNorth:
            case QTabBar::TriangularSouth:
                result.rheight() += tbm.height();
                result.rwidth() = qMax(tbm.width(), result.width());
                break;
            case QTabBar::RoundedEast:
            case QTabBar::RoundedWest:
            case QTabBar::TriangularEast:
            case QTabBar::TriangularWest:
                result.rheight() = qMax(tbm.height(), result.height());
                result.rwidth() += tbm.width();
                break;
            default:
                break;
        }
    }
#endif // QT_CONFIG(tabbar)

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 366, as _ZNK19QDockAreaLayoutInfo11maximumSizeEv
inline QSize QDockAreaLayoutInfo::maximumSize() const
{
    if (isEmpty())
        return QSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX);

    int a = 0, b = QWIDGETSIZE_MAX;
#if QT_CONFIG(tabbar)
    if (tabbed)
        a = QWIDGETSIZE_MAX;
#endif

    int min_perp = 0;

    bool first = true;
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

        QSize max_size = item.maximumSize();
        min_perp = qMax(min_perp, perp(o, item.minimumSize()));

#if QT_CONFIG(tabbar)
        if (tabbed) {
            a = qMin(a, pick(o, max_size));
        } else
#endif
        {
            if (!first)
                a += *sep;
            a += pick(o, max_size);
        }
        b = qMin(b, perp(o, max_size));

        a = qMin(a, int(QWIDGETSIZE_MAX));
        b = qMin(b, int(QWIDGETSIZE_MAX));

        first = false;
    }

    b = qMax(b, min_perp);

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

#if QT_CONFIG(tabbar)
    QSize tbh = tabBarSizeHint();
    if (!tbh.isNull()) {
        switch (tabBarShape) {
            case QTabBar::RoundedNorth:
            case QTabBar::RoundedSouth:
                result.rheight() += tbh.height();
                break;
            case QTabBar::RoundedEast:
            case QTabBar::RoundedWest:
                result.rwidth() += tbh.width();
                break;
            default:
                break;
        }
    }
#endif // QT_CONFIG(tabbar)

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 433, as _ZNK19QDockAreaLayoutInfo8sizeHintEv
inline QSize QDockAreaLayoutInfo::sizeHint() const
{
    if (isEmpty())
        return QSize(0, 0);

    int a = 0, b = 0;
    int min_perp = 0;
    int max_perp = QWIDGETSIZE_MAX;
    const QDockAreaLayoutItem *previous = nullptr;
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

        bool gap = item.flags & QDockAreaLayoutItem::GapItem;

        QSize size_hint = item.sizeHint();
        min_perp = qMax(min_perp, perp(o, item.minimumSize()));
        max_perp = qMin(max_perp, perp(o, item.maximumSize()));

#if QT_CONFIG(tabbar)
        if (tabbed) {
            a = qMax(a, gap ? item.size : pick(o, size_hint));
        } else
#endif
        {
            if (previous && !gap && !(previous->flags &  QDockAreaLayoutItem::GapItem)
                && !previous->hasFixedSize(o)) {
                a += *sep;
            }
            a += gap ? item.size : pick(o, size_hint);
        }
        b = qMax(b, perp(o, size_hint));

        previous = &item;
    }

    max_perp = qMax(max_perp, min_perp);
    b = qMax(b, min_perp);
    b = qMin(b, max_perp);

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

#if QT_CONFIG(tabbar)
    if (tabbed) {
        QSize tbh = tabBarSizeHint();
        switch (tabBarShape) {
            case QTabBar::RoundedNorth:
            case QTabBar::RoundedSouth:
            case QTabBar::TriangularNorth:
            case QTabBar::TriangularSouth:
                result.rheight() += tbh.height();
                result.rwidth() = qMax(tbh.width(), result.width());
                break;
            case QTabBar::RoundedEast:
            case QTabBar::RoundedWest:
            case QTabBar::TriangularEast:
            case QTabBar::TriangularWest:
                result.rheight() = qMax(tbh.height(), result.height());
                result.rwidth() += tbh.width();
                break;
            default:
                break;
        }
    }
#endif // QT_CONFIG(tabbar)

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 505, as _ZNK19QDockAreaLayoutInfo9expansiveEN2Qt11OrientationE
inline bool QDockAreaLayoutInfo::expansive(Qt::Orientation o) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        if (item_list.at(i).expansive(o))
            return true;
    }
    return false;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2319, as _ZNK19QDockAreaLayoutInfo17tabBarMinimumSizeEv
#if QT_CONFIG(tabbar)
inline QSize QDockAreaLayoutInfo::tabBarMinimumSize() const
{
    if (!updateTabBar())
        return QSize(0, 0);

    return tabBar->minimumSizeHint();
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 292, as _ZNK19QDockAreaLayoutInfo7isEmptyEv
inline bool QDockAreaLayoutInfo::isEmpty() const
{
    return next(-1) == -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2327, as _ZNK19QDockAreaLayoutInfo14tabBarSizeHintEv
#if QT_CONFIG(tabbar)
inline QSize QDockAreaLayoutInfo::tabBarSizeHint() const
{
    if (!updateTabBar())
        return QSize(0, 0);

    return tabBar->sizeHint();
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1719, as _ZNK19QDockAreaLayoutInfo4nextEi
inline int QDockAreaLayoutInfo::next(int index) const
{
    for (int i = index + 1; i < item_list.size(); ++i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 65, as _ZN19QDockAreaLayoutItemC1EP11QLayoutItem
inline QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem *_widgetItem)
    : widgetItem(_widgetItem), subinfo(nullptr), placeHolderItem(nullptr), pos(0), size(-1), flags(NoFlags)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 70, as _ZN19QDockAreaLayoutItemC1EP19QDockAreaLayoutInfo
inline QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutInfo *_subinfo)
    : widgetItem(nullptr), subinfo(_subinfo), placeHolderItem(nullptr), pos(0), size(-1), flags(NoFlags)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 75, as _ZN19QDockAreaLayoutItemC1EP16QPlaceHolderItem
inline QDockAreaLayoutItem::QDockAreaLayoutItem(QPlaceHolderItem *_placeHolderItem)
    : widgetItem(nullptr), subinfo(nullptr), placeHolderItem(_placeHolderItem), pos(0), size(-1), flags(NoFlags)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 80, as _ZN19QDockAreaLayoutItemC1ERKS_
inline QDockAreaLayoutItem::QDockAreaLayoutItem(const QDockAreaLayoutItem &other)
    : widgetItem(other.widgetItem), subinfo(nullptr), placeHolderItem(nullptr), pos(other.pos),
        size(other.size), flags(other.flags)
{
    if (other.subinfo != nullptr)
        subinfo = new QDockAreaLayoutInfo(*other.subinfo);
    else if (other.placeHolderItem != nullptr)
        placeHolderItem = new QPlaceHolderItem(*other.placeHolderItem);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 140, as _ZNK19QDockAreaLayoutItem9expansiveEN2Qt11OrientationE
inline bool QDockAreaLayoutItem::expansive(Qt::Orientation o) const
{
    if ((flags & GapItem) || placeHolderItem != nullptr)
        return false;
    if (widgetItem != nullptr)
        return ((widgetItem->expandingDirections() & o) == o);
    if (subinfo != nullptr)
        return subinfo->expansive(o);
    return false;
}
//  -----------------------------------------------------------------------

//  QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem *_widgetItem)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1EP11QLayoutItem(
    QLayoutItem *_widgetItem) {
  return new QDockAreaLayoutItem(_widgetItem);
}

//  QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutInfo *_subinfo)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1EP19QDockAreaLayoutInfo(
    QDockAreaLayoutInfo *_subinfo) {
  return new QDockAreaLayoutItem(_subinfo);
}

//  QDockAreaLayoutItem::QDockAreaLayoutItem(QPlaceHolderItem
//      *_placeHolderItem)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1EP16QPlaceHolderItem(
    QPlaceHolderItem *_placeHolderItem) {
  return new QDockAreaLayoutItem(_placeHolderItem);
}

//  QDockAreaLayoutItem::QDockAreaLayoutItem(const QDockAreaLayoutItem
//      &other)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1ERKS_(
    const QDockAreaLayoutItem *other) {
  return new QDockAreaLayoutItem(*other);
}

//  QDockAreaLayoutItem::~QDockAreaLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutItemD1Ev(QDockAreaLayoutItem *self) {
  delete self;
}

//  bool QDockAreaLayoutItem::skip() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutItem4skipEv(
    const QDockAreaLayoutItem *self) {
  return self->skip();
}

//  bool QDockAreaLayoutItem::expansive(Qt::Orientation o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutItem9expansiveEN2Qt11OrientationE(
    const QDockAreaLayoutItem *self,
    Qt::Orientation o) {
  return self->expansive(o);
}

#endif  // QT_CONFIG(dockwidget)
