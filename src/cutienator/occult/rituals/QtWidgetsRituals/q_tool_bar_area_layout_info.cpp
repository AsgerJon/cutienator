//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QWidgetItem>
#include <QToolBar>
#include <QStyleOption>
#include <QApplication>
#include <qdebug.h>
#include "qtoolbararealayout_p.h"
#include "qmainwindowlayout_p.h"
#include "qtoolbarlayout_p.h"
#include "qtoolbar_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 153, as _ZNK22QToolBarAreaLayoutLine4skipEv
inline bool QToolBarAreaLayoutLine::skip() const
{
    for (int i = 0; i < toolBarItems.size(); ++i) {
        if (!toolBarItems.at(i).skip())
            return false;
    }
    return true;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 71, as _ZNK22QToolBarAreaLayoutLine8sizeHintEv
inline QSize QToolBarAreaLayoutLine::sizeHint() const
{
    int a = 0, b = 0;
    for (int i = 0; i < toolBarItems.size(); ++i) {
        const QToolBarAreaLayoutItem &item = toolBarItems.at(i);
        if (item.skip())
            continue;

        QSize sh = item.sizeHint();
        a += item.preferredSize > 0 ? item.preferredSize : pick(o, sh);
        b = qMax(b, perp(o, sh));
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 91, as _ZNK22QToolBarAreaLayoutLine11minimumSizeEv
inline QSize QToolBarAreaLayoutLine::minimumSize() const
{
    int a = 0, b = 0;
    for (int i = 0; i < toolBarItems.size(); ++i) {
        const QToolBarAreaLayoutItem &item = toolBarItems[i];
        if (item.skip())
            continue;

        QSize ms = item.minimumSize();
        a += pick(o, ms);
        b = qMax(b, perp(o, ms));
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 111, as _ZN22QToolBarAreaLayoutLine9fitLayoutEv
inline void QToolBarAreaLayoutLine::fitLayout()
{
    int last = -1;
    int min = pick(o, minimumSize());
    int space = pick(o, rect.size());
    int extra = qMax(0, space - min);

    for (int i = 0; i < toolBarItems.size(); ++i) {
        QToolBarAreaLayoutItem &item = toolBarItems[i];
        if (item.skip())
            continue;

        if (QToolBarLayout *tblayout = qobject_cast<QToolBarLayout*>(item.widgetItem->widget()->layout()))
            tblayout->checkUsePopupMenu();

        const int itemMin = pick(o, item.minimumSize());
        //preferredSize is the default if it is set, otherwise, we take the sizehint
        item.size = item.preferredSize > 0 ? item.preferredSize : pick(o, item.sizeHint());

        //the extraspace is the space above the item minimum sizehint
        const int extraSpace = qMin(item.size - itemMin, extra);
        item.size = itemMin + extraSpace; //that is the real size

        extra -= extraSpace;

        last = i;
    }

    // calculate the positions from the sizes
    int pos = 0;
    for (int i = 0; i < toolBarItems.size(); ++i) {
        QToolBarAreaLayoutItem &item = toolBarItems[i];
        if (item.skip())
            continue;

        item.pos = pos;
        if (i == last) // stretch the last item to the end of the line
            item.size = qMax(0, pick(o, rect.size()) - item.pos);
        pos += item.size;
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 66, as _ZN22QToolBarAreaLayoutLineC1EN2Qt11OrientationE
inline QToolBarAreaLayoutLine::QToolBarAreaLayoutLine(Qt::Orientation orientation)
    : o(orientation)
{
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 26, as _ZNK22QToolBarAreaLayoutItem11minimumSizeEv
inline QSize QToolBarAreaLayoutItem::minimumSize() const
{
    if (skip())
        return QSize(0, 0);
    return qSmartMinSize(static_cast<QWidgetItem*>(widgetItem));
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 55, as _ZNK22QToolBarAreaLayoutItem4skipEv
inline bool QToolBarAreaLayoutItem::skip() const
{
    if (gap)
        return false;
    return widgetItem == nullptr || widgetItem->isEmpty();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 33, as _ZNK22QToolBarAreaLayoutItem8sizeHintEv
inline QSize QToolBarAreaLayoutItem::sizeHint() const
{
    if (skip())
        return QSize(0, 0);

    return realSizeHint();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 42, as _ZNK22QToolBarAreaLayoutItem12realSizeHintEv
inline QSize QToolBarAreaLayoutItem::realSizeHint() const
{
    QWidget *wid = widgetItem->widget();
    QSize s = wid->sizeHint().expandedTo(wid->minimumSizeHint());
    if (wid->sizePolicy().horizontalPolicy() == QSizePolicy::Ignored)
        s.setWidth(0);
    if (wid->sizePolicy().verticalPolicy() == QSizePolicy::Ignored)
        s.setHeight(0);
    s = s.boundedTo(wid->maximumSize())
        .expandedTo(wid->minimumSize());
    return s;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 166, as _ZN22QToolBarAreaLayoutInfoC1EN9QInternal12DockPositionE
inline QToolBarAreaLayoutInfo::QToolBarAreaLayoutInfo(QInternal::DockPosition pos)
    : dockPos(pos), dirty(false)
{
    switch (pos) {
        case QInternal::LeftDock:
        case QInternal::RightDock:
            o = Qt::Vertical;
            break;
        case QInternal::TopDock:
        case QInternal::BottomDock:
            o = Qt::Horizontal;
            break;
        default:
            o = Qt::Horizontal;
            break;
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 184, as _ZNK22QToolBarAreaLayoutInfo8sizeHintEv
inline QSize QToolBarAreaLayoutInfo::sizeHint() const
{
    int a = 0, b = 0;
    for (int i = 0; i < lines.size(); ++i) {
        const QToolBarAreaLayoutLine &l = lines.at(i);
        if (l.skip())
            continue;

        QSize hint = l.sizeHint();
        a = qMax(a, pick(o, hint));
        b += perp(o, hint);
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 204, as _ZNK22QToolBarAreaLayoutInfo11minimumSizeEv
inline QSize QToolBarAreaLayoutInfo::minimumSize() const
{
    int a = 0, b = 0;
    for (int i = 0; i < lines.size(); ++i) {
        const QToolBarAreaLayoutLine &l = lines.at(i);
        if (l.skip())
            continue;

        QSize m = l.minimumSize();
        a = qMax(a, pick(o, m));
        b += perp(o, m);
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 260, as _ZN22QToolBarAreaLayoutInfo13insertToolBarEP8QToolBarS1_
inline QLayoutItem *QToolBarAreaLayoutInfo::insertToolBar(QToolBar *before, QToolBar *toolBar)
{
    toolBar->setOrientation(o);
    QLayoutItem *item = new QWidgetItemV2(toolBar);
    insertItem(before, item);
    return item;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 268, as _ZN22QToolBarAreaLayoutInfo10insertItemEP8QToolBarP11QLayoutItem
inline void QToolBarAreaLayoutInfo::insertItem(QToolBar *before, QLayoutItem *item)
{
    if (before == nullptr) {
        if (lines.isEmpty())
            lines.append(QToolBarAreaLayoutLine(o));
        lines.last().toolBarItems.append(item);
        return;
    }

    for (int j = 0; j < lines.size(); ++j) {
        QToolBarAreaLayoutLine &line = lines[j];

        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            if (line.toolBarItems.at(k).widgetItem->widget() == before) {
                line.toolBarItems.insert(k, item);
                return;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 289, as _ZN22QToolBarAreaLayoutInfo13removeToolBarEP8QToolBar
inline void QToolBarAreaLayoutInfo::removeToolBar(QToolBar *toolBar)
{
    for (int j = 0; j < lines.size(); ++j) {
        QToolBarAreaLayoutLine &line = lines[j];

        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            QToolBarAreaLayoutItem &item = line.toolBarItems[k];
            if (item.widgetItem->widget() == toolBar) {
                delete item.widgetItem;
                item.widgetItem = nullptr;
                line.toolBarItems.removeAt(k);

                if (line.toolBarItems.isEmpty() && j < lines.size() - 1)
                    lines.removeAt(j);

                return;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 310, as _ZN22QToolBarAreaLayoutInfo18insertToolBarBreakEP8QToolBar
inline void QToolBarAreaLayoutInfo::insertToolBarBreak(QToolBar *before)
{
    if (before == nullptr) {
        if (!lines.isEmpty() && lines.constLast().toolBarItems.isEmpty())
            return;
        lines.append(QToolBarAreaLayoutLine(o));
        return;
    }

    for (int j = 0; j < lines.size(); ++j) {
        QToolBarAreaLayoutLine &line = lines[j];

        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            if (line.toolBarItems.at(k).widgetItem->widget() == before) {
                if (k == 0)
                    return;

                QToolBarAreaLayoutLine newLine(o);
                newLine.toolBarItems = line.toolBarItems.mid(k);
                line.toolBarItems = line.toolBarItems.mid(0, k);
                lines.insert(j + 1, newLine);

                return;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 338, as _ZN22QToolBarAreaLayoutInfo18removeToolBarBreakEP8QToolBar
inline void QToolBarAreaLayoutInfo::removeToolBarBreak(QToolBar *before)
{
    for (int j = 0; j < lines.size(); ++j) {
        const QToolBarAreaLayoutLine &line = lines.at(j);

        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            if (line.toolBarItems.at(k).widgetItem->widget() == before) {
                if (k != 0)
                    return;
                if (j == 0)
                    return;

                lines[j - 1].toolBarItems += lines[j].toolBarItems;
                lines.removeAt(j);

                return;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 536, as _ZN22QToolBarAreaLayoutInfo5clearEv
inline void QToolBarAreaLayoutInfo::clear()
{
    lines.clear();
    rect = QRect();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 564, as _ZNK22QToolBarAreaLayoutInfo8distanceERK6QPoint
inline int QToolBarAreaLayoutInfo::distance(const QPoint &pos) const
{
    switch (dockPos) {
        case QInternal::LeftDock:
            if (pos.y() > 0 && pos.y() < rect.bottom())
                return pos.x() - rect.right();
            break;
        case QInternal::RightDock:
            if (pos.y() > 0 && pos.y() < rect.bottom())
                return rect.left() - pos.x();
            break;
        case QInternal::TopDock:
            if (pos.x() > 0 && pos.x() < rect.right())
                return pos.y() - rect.bottom();
            break;
        case QInternal::BottomDock:
            if (pos.x() > 0 && pos.x() < rect.right())
                return rect.top() - pos.y();
            break;

        case QInternal::DockCount:
            break;
    }
    return -1;
}
//  -----------------------------------------------------------------------

//  QToolBarAreaLayoutInfo::QToolBarAreaLayoutInfo(QInternal::DockPosition
//      pos)
extern "C" Q_DECL_EXPORT
QToolBarAreaLayoutInfo *ritual_ZN22QToolBarAreaLayoutInfoC1EN9QInternal12DockPositionE(
    QInternal::DockPosition pos) {
  return new QToolBarAreaLayoutInfo(pos);
}

//  QSize QToolBarAreaLayoutInfo::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QToolBarAreaLayoutInfo8sizeHintEv(
    const QToolBarAreaLayoutInfo *self) {
  return new QSize(self->sizeHint());
}

//  QSize QToolBarAreaLayoutInfo::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QToolBarAreaLayoutInfo11minimumSizeEv(
    const QToolBarAreaLayoutInfo *self) {
  return new QSize(self->minimumSize());
}

//  QLayoutItem *QToolBarAreaLayoutInfo::insertToolBar(QToolBar *before,
//      QToolBar *toolBar)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN22QToolBarAreaLayoutInfo13insertToolBarEP8QToolBarS1_(
    QToolBarAreaLayoutInfo *self,
    QToolBar *before,
    QToolBar *toolBar) {
  return self->insertToolBar(before, toolBar);
}

//  void QToolBarAreaLayoutInfo::insertItem(QToolBar *before, QLayoutItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutInfo10insertItemEP8QToolBarP11QLayoutItem(
    QToolBarAreaLayoutInfo *self,
    QToolBar *before,
    QLayoutItem *item) {
  self->insertItem(before, item);
}

//  void QToolBarAreaLayoutInfo::removeToolBar(QToolBar *toolBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutInfo13removeToolBarEP8QToolBar(
    QToolBarAreaLayoutInfo *self,
    QToolBar *toolBar) {
  self->removeToolBar(toolBar);
}

//  void QToolBarAreaLayoutInfo::insertToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutInfo18insertToolBarBreakEP8QToolBar(
    QToolBarAreaLayoutInfo *self,
    QToolBar *before) {
  self->insertToolBarBreak(before);
}

//  void QToolBarAreaLayoutInfo::removeToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutInfo18removeToolBarBreakEP8QToolBar(
    QToolBarAreaLayoutInfo *self,
    QToolBar *before) {
  self->removeToolBarBreak(before);
}

//  void QToolBarAreaLayoutInfo::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutInfo5clearEv(
    QToolBarAreaLayoutInfo *self) {
  self->clear();
}

//  int QToolBarAreaLayoutInfo::distance(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QToolBarAreaLayoutInfo8distanceERK6QPoint(
    const QToolBarAreaLayoutInfo *self,
    const QPoint *pos) {
  return self->distance(*pos);
}

//  QToolBarAreaLayoutInfo::~QToolBarAreaLayoutInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutInfoD1Ev(QToolBarAreaLayoutInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(toolbar)
