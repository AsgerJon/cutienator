//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <optional>
#include <QtCore/QInternal>
#include <QtCore/QList>
#include <QtCore/QPoint>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/QWidgetItem>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QStyleOption>
#include <QtWidgets/QApplication>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qtoolbararealayout_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 24, as local:qtoolbararealayout.cpp:StateMarkers
using StateMarkers = QMainWindowLayoutState::StateMarkers;

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1174, as local:qtoolbararealayout.cpp:packRect
static void packRect(uint *geom0, uint *geom1, const QRect &rect, bool floating)
{
    *geom0 = 0;
    *geom1 = 0;

    if (!floating)
        return;

    // The 0x7FFF is half of 0xFFFF. We add it so we can handle negative coordinates on
    // dual monitors. It's subtracted when unpacking.

    *geom0 |= qMax(0, rect.width()) & 0x0000ffff;
    *geom1 |= qMax(0, rect.height()) & 0x0000ffff;

    *geom0 <<= 16;
    *geom1 <<= 16;

    *geom0 |= qMax(0, rect.x() + 0x7FFF) & 0x0000ffff;
    *geom1 |= qMax(0, rect.y() + 0x7FFF) & 0x0000ffff;

    // yeah, we chop one bit off the width, but it still has a range up to 32512

    *geom0 <<= 1;
    *geom0 |= 1;
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 224, as _ZN22QToolBarAreaLayoutInfo9fitLayoutEv
inline void QToolBarAreaLayoutInfo::fitLayout()
{
    dirty = false;

    int b = 0;

    bool reverse = dockPos == QInternal::RightDock || dockPos == QInternal::BottomDock;

    int i = reverse ? lines.size() - 1 : 0;
    for (;;) {
        if ((reverse && i < 0) || (!reverse && i == lines.size()))
            break;

        QToolBarAreaLayoutLine &l = lines[i];
        if (!l.skip()) {
            if (o == Qt::Horizontal) {
                l.rect.setLeft(rect.left());
                l.rect.setRight(rect.right());
                l.rect.setTop(b + rect.top());
                b += l.sizeHint().height();
                l.rect.setBottom(b - 1 + rect.top());
            } else {
                l.rect.setTop(rect.top());
                l.rect.setBottom(rect.bottom());
                l.rect.setLeft(b + rect.left());
                b += l.sizeHint().width();
                l.rect.setRight(b - 1 + rect.left());
            }

            l.fitLayout();
        }

        i += reverse ? -1 : 1;
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 359, as _ZN22QToolBarAreaLayoutInfo11moveToolBarEP8QToolBari
inline void QToolBarAreaLayoutInfo::moveToolBar(QToolBar *toolbar, int pos)
{
    if (dirty)
        fitLayout();

    dirty = true;

    if (o == Qt::Vertical)
        pos -= rect.top();

    //here we actually update the preferredSize for the line containing the toolbar so that we move it
    for (int j = 0; j < lines.size(); ++j) {
        QToolBarAreaLayoutLine &line = lines[j];

        int previousIndex = -1;
        int minPos = 0;
        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            QToolBarAreaLayoutItem &current = line.toolBarItems[k];
            if (current.widgetItem->widget() == toolbar) {
                int newPos = current.pos;

                if (previousIndex >= 0) {
                    QToolBarAreaLayoutItem &previous = line.toolBarItems[previousIndex];
                    if (pos < current.pos) {
                        newPos = qMax(pos, minPos);
                    } else {
                        //we check the max value for the position (until everything at the right is "compressed")
                        int maxPos = pick(o, rect.size());
                        for(int l = k; l < line.toolBarItems.size(); ++l) {
                            const QToolBarAreaLayoutItem &item = line.toolBarItems.at(l);
                            if (!item.skip()) {
                                maxPos -= pick(o, item.minimumSize());
                            }
                        }
                        newPos = qMin(pos, maxPos);
                    }

                    //extra is the number of pixels to add to the previous toolbar
                    int extra = newPos - current.pos;

                    //we check if the previous is near its size hint
                    //in which case we try to stick to it
                    const int diff = pick(o, previous.sizeHint()) - (previous.size + extra);
                    if (qAbs(diff) < QApplication::startDragDistance()) {
                        //we stick to the default place and size
                        extra += diff;
                    }

                    //update for the current item
                    current.extendSize(line.o, -extra);

                    if (extra >= 0) {
                        previous.extendSize(line.o, extra);
                    } else {
                        //we need to push the toolbars on the left starting with previous
                        extra = -extra; // we just need to know the number of pixels
                        ///at this point we need to get extra pixels from the toolbars at the left
                        for(int l = previousIndex; l >=0; --l) {
                            QToolBarAreaLayoutItem &item = line.toolBarItems[l];
                            if (!item.skip()) {
                                const int minPreferredSize = pick(o, item.minimumSize());
                                const int margin =  item.size - minPreferredSize;
                                if (margin < extra) {
                                    item.resize(line.o, minPreferredSize);
                                    extra -= margin;
                                } else {
                                    item.extendSize(line.o, -extra);
                                    extra = 0;
                                }
                            }
                        }
                        Q_ASSERT(extra == 0);
                    }
                } else {
                    //the item is the first one, it should be at position 0
                }

                return;

            } else if (!current.skip()) {
                previousIndex = k;
                minPos += pick(o, current.minimumSize());
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 66, as _ZN22QToolBarAreaLayoutLineC1EN2Qt11OrientationE
inline QToolBarAreaLayoutLine::QToolBarAreaLayoutLine(Qt::Orientation orientation)
    : o(orientation)
{
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 447, as _ZNK22QToolBarAreaLayoutInfo8gapIndexERK6QPointPi
inline QList<int> QToolBarAreaLayoutInfo::gapIndex(const QPoint &pos, int *minDistance) const
{
    if (rect.contains(pos)) {
        // <pos> is in QToolBarAreaLayout coordinates.
        // <item.pos> is in local dockarea coordinates (see ~20 lines below)
        // Since we're comparing p with item.pos, we put them in the same coordinate system.
        const int p = pick(o, pos - rect.topLeft());

        for (int j = 0; j < lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = lines.at(j);
            if (line.skip())
                continue;
            if (!line.rect.contains(pos))
                continue;

            int k = 0;
            for (; k < line.toolBarItems.size(); ++k) {
                const QToolBarAreaLayoutItem &item = line.toolBarItems.at(k);
                if (item.skip())
                    continue;

                int size = qMin(item.size, pick(o, item.sizeHint()));

                if (p > item.pos + size)
                    continue;
                if (p > item.pos + size/2)
                    ++k;
                break;
            }

            QList<int> result;
            result << j << k;
            *minDistance = 0; //we found a perfect match
            return result;
        }
    } else {
        const int dist = distance(pos);
        //it will only return a path if the minDistance is higher than the current distance
        if (dist >= 0 && *minDistance > dist) {
            *minDistance = dist;

            QList<int> result;
            result << lines.size() << 0;
            return result;
        }
    }

    return QList<int>();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 497, as _ZN22QToolBarAreaLayoutInfo9insertGapERK5QListIiEP11QLayoutItem
inline bool QToolBarAreaLayoutInfo::insertGap(const QList<int> &path, QLayoutItem *item)
{
    Q_ASSERT(path.size() == 2);
    int j = path.first();
    if (j == lines.size())
        lines.append(QToolBarAreaLayoutLine(o));

    QToolBarAreaLayoutLine &line = lines[j];
    const int k = path.at(1);

    QToolBarAreaLayoutItem gap_item;
    gap_item.gap = true;
    gap_item.widgetItem = item;

    //update the previous item's preferred size
    for(int p = k - 1 ; p >= 0; --p) {
        QToolBarAreaLayoutItem &previous = line.toolBarItems[p];
        if (!previous.skip()) {
            //we found the previous one
            int previousSizeHint = pick(line.o, previous.sizeHint());
            int previousExtraSpace = previous.size - previousSizeHint;

            if (previousExtraSpace > 0) {
                //in this case we reset the space
                previous.preferredSize = -1;
                previous.size = previousSizeHint;

                gap_item.resize(o, previousExtraSpace);
            }

            break;
        }
    }

    line.toolBarItems.insert(k, gap_item);
    return true;

}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 536, as _ZN22QToolBarAreaLayoutInfo5clearEv
inline void QToolBarAreaLayoutInfo::clear()
{
    lines.clear();
    rect = QRect();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 542, as _ZNK22QToolBarAreaLayoutInfo8itemRectERK5QListIiE
inline QRect QToolBarAreaLayoutInfo::itemRect(const QList<int> &path) const
{
    Q_ASSERT(path.size() == 2);
    int j = path.at(0);
    int k = path.at(1);

    const QToolBarAreaLayoutLine &line = lines.at(j);
    const QToolBarAreaLayoutItem &item = line.toolBarItems.at(k);

    QRect result = line.rect;

    if (o == Qt::Horizontal) {
        result.setLeft(item.pos + line.rect.left());
        result.setWidth(item.size);
    } else {
        result.setTop(item.pos + line.rect.top());
        result.setHeight(item.size);
    }

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 26, as _ZNK22QToolBarAreaLayoutItem11minimumSizeEv
inline QSize QToolBarAreaLayoutItem::minimumSize() const
{
    if (skip())
        return QSize(0, 0);
    return qSmartMinSize(static_cast<QWidgetItem*>(widgetItem));
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 594, as _ZN18QToolBarAreaLayoutC1EPK11QMainWindow
inline QToolBarAreaLayout::QToolBarAreaLayout(const QMainWindow *win) : mainWindow(win), visible(true)
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        QInternal::DockPosition pos = static_cast<QInternal::DockPosition>(i);
        docks[i] = QToolBarAreaLayoutInfo(pos);
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 632, as _ZNK18QToolBarAreaLayout11minimumSizeERK5QSize
inline QSize QToolBarAreaLayout::minimumSize(const QSize &centerMin) const
{
    if (!visible)
        return centerMin;

    QSize result = centerMin;

    QSize left_min = docks[QInternal::LeftDock].minimumSize();
    QSize right_min = docks[QInternal::RightDock].minimumSize();
    QSize top_min = docks[QInternal::TopDock].minimumSize();
    QSize bottom_min = docks[QInternal::BottomDock].minimumSize();

    result.setWidth(qMax(top_min.width(), result.width()));
    result.setWidth(qMax(bottom_min.width(), result.width()));
    result.setHeight(qMax(left_min.height(), result.height()));
    result.setHeight(qMax(right_min.height(), result.height()));

    result.rwidth() += left_min.width() + right_min.width();
    result.rheight() += top_min.height() + bottom_min.height();

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 678, as _ZNK18QToolBarAreaLayout8rectHintERK5QRect
inline QRect QToolBarAreaLayout::rectHint(const QRect &r) const
{
    int coef = visible ? 1 : -1;

    QRect result = r;

    QSize left_hint = docks[QInternal::LeftDock].sizeHint();
    QSize right_hint = docks[QInternal::RightDock].sizeHint();
    QSize top_hint = docks[QInternal::TopDock].sizeHint();
    QSize bottom_hint = docks[QInternal::BottomDock].sizeHint();

    result.adjust(-left_hint.width()*coef, -top_hint.height()*coef,
                    right_hint.width()*coef, bottom_hint.height()*coef);

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 655, as _ZNK18QToolBarAreaLayout8sizeHintERK5QSize
inline QSize QToolBarAreaLayout::sizeHint(const QSize &centerHint) const
{
    if (!visible)
        return centerHint;

    QSize result = centerHint;

    QSize left_hint = docks[QInternal::LeftDock].sizeHint();
    QSize right_hint = docks[QInternal::RightDock].sizeHint();
    QSize top_hint = docks[QInternal::TopDock].sizeHint();
    QSize bottom_hint = docks[QInternal::BottomDock].sizeHint();

    result.setWidth(qMax(top_hint.width(), result.width()));
    result.setWidth(qMax(bottom_hint.width(), result.width()));
    result.setHeight(qMax(left_hint.height(), result.height()));
    result.setHeight(qMax(right_hint.height(), result.height()));

    result.rwidth() += left_hint.width() + right_hint.width();
    result.rheight() += top_hint.height() + bottom_hint.height();

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 695, as _ZNK18QToolBarAreaLayout6itemAtEPii
inline QLayoutItem *QToolBarAreaLayout::itemAt(int *x, int index) const
{
    Q_ASSERT(x != nullptr);

    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if ((*x)++ == index)
                    return line.toolBarItems.at(k).widgetItem;
            }
        }
    }

    return nullptr;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 715, as _ZN18QToolBarAreaLayout6takeAtEPii
inline QLayoutItem *QToolBarAreaLayout::takeAt(int *x, int index)
{
    Q_ASSERT(x != nullptr);

    for (int i = 0; i < QInternal::DockCount; ++i) {
        QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            QToolBarAreaLayoutLine &line = dock.lines[j];

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if ((*x)++ == index) {
                    QLayoutItem *result = line.toolBarItems.takeAt(k).widgetItem;
                    if (line.toolBarItems.isEmpty())
                        dock.lines.removeAt(j);
                    return result;
                }
            }
        }
    }

    return nullptr;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 739, as _ZN18QToolBarAreaLayout20deleteAllLayoutItemsEv
inline void QToolBarAreaLayout::deleteAllLayoutItems()
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            QToolBarAreaLayoutLine &line = dock.lines[j];

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                QToolBarAreaLayoutItem &item = line.toolBarItems[k];
                if (!item.gap)
                    delete item.widgetItem;
                item.widgetItem = nullptr;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 771, as _ZN18QToolBarAreaLayout13insertToolBarEP8QToolBarS1_
inline QLayoutItem *QToolBarAreaLayout::insertToolBar(QToolBar *before, QToolBar *toolBar)
{
    if (auto pos = findToolBar(before))
        return docks[*pos].insertToolBar(before, toolBar);
    return nullptr;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 778, as _ZN18QToolBarAreaLayout13removeToolBarEP8QToolBar
inline void QToolBarAreaLayout::removeToolBar(QToolBar *toolBar)
{
    if (auto pos = findToolBar(toolBar))
        docks[*pos].removeToolBar(toolBar);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 784, as _ZN18QToolBarAreaLayout10addToolBarEN9QInternal12DockPositionEP8QToolBar
inline QLayoutItem *QToolBarAreaLayout::addToolBar(QInternal::DockPosition pos, QToolBar *toolBar)
{
    return docks[pos].insertToolBar(nullptr, toolBar);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 789, as _ZN18QToolBarAreaLayout18insertToolBarBreakEP8QToolBar
inline void QToolBarAreaLayout::insertToolBarBreak(QToolBar *before)
{
    if (auto pos = findToolBar(before))
        docks[*pos].insertToolBarBreak(before);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 795, as _ZN18QToolBarAreaLayout18removeToolBarBreakEP8QToolBar
inline void QToolBarAreaLayout::removeToolBarBreak(QToolBar *before)
{
    if (auto pos = findToolBar(before))
        docks[*pos].removeToolBarBreak(before);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 801, as _ZN18QToolBarAreaLayout15addToolBarBreakEN9QInternal12DockPositionE
inline void QToolBarAreaLayout::addToolBarBreak(QInternal::DockPosition pos)
{
    docks[pos].insertToolBarBreak(nullptr);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 813, as _ZN18QToolBarAreaLayout10insertItemEN9QInternal12DockPositionEP11QLayoutItem
inline void QToolBarAreaLayout::insertItem(QInternal::DockPosition pos, QLayoutItem *item)
{
    if (docks[pos].lines.isEmpty())
        docks[pos].lines.append(QToolBarAreaLayoutLine(docks[pos].o));
    docks[pos].lines.last().toolBarItems.append(item);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 820, as _ZN18QToolBarAreaLayout10insertItemEP8QToolBarP11QLayoutItem
inline void QToolBarAreaLayout::insertItem(QToolBar *before, QLayoutItem *item)
{
    if (auto pos = findToolBar(before))
        docks[*pos].insertItem(before, item);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 757, as _ZNK18QToolBarAreaLayout11findToolBarEPK8QToolBar
inline std::optional<QInternal::DockPosition> QToolBarAreaLayout::findToolBar(const QToolBar *toolBar) const
{
    for (std::size_t i = 0; i < docks.size(); ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];
        for (const auto &line : dock.lines) {
            for (const auto &item : line.toolBarItems) {
                if (item.widgetItem->widget() == toolBar)
                    return static_cast<QInternal::DockPosition>(i);
            }
        }
    }
    return {};
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 889, as _ZNK18QToolBarAreaLayout12toolBarBreakEP8QToolBar
inline bool QToolBarAreaLayout::toolBarBreak(QToolBar *toolBar) const
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if (line.toolBarItems.at(k).widgetItem->widget() == toolBar)
                    return j > 0 && k == 0;
            }
        }
    }

    return false;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 907, as _ZNK18QToolBarAreaLayout18getStyleOptionInfoEP19QStyleOptionToolBarP8QToolBar
inline void QToolBarAreaLayout::getStyleOptionInfo(QStyleOptionToolBar *option, QToolBar *toolBar) const
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if (line.toolBarItems.at(k).widgetItem->widget() == toolBar) {
                    if (line.toolBarItems.size() == 1)
                        option->positionWithinLine = QStyleOptionToolBar::OnlyOne;
                    else if (k == 0)
                        option->positionWithinLine = QStyleOptionToolBar::Beginning;
                    else if (k == line.toolBarItems.size() - 1)
                        option->positionWithinLine = QStyleOptionToolBar::End;
                    else
                        option->positionWithinLine = QStyleOptionToolBar::Middle;

                    if (dock.lines.size() == 1)
                        option->positionOfLine = QStyleOptionToolBar::OnlyOne;
                    else if (j == 0)
                        option->positionOfLine = QStyleOptionToolBar::Beginning;
                    else if (j == dock.lines.size() - 1)
                        option->positionOfLine = QStyleOptionToolBar::End;
                    else
                        option->positionOfLine = QStyleOptionToolBar::Middle;

                    return;
                }
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 942, as _ZNK18QToolBarAreaLayout7indexOfEP7QWidget
inline QList<int> QToolBarAreaLayout::indexOf(QWidget *toolBar) const
{
    QList<int> result;

    bool found = false;

    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                const QToolBarAreaLayoutItem &item = line.toolBarItems.at(k);
                if (!item.gap && item.widgetItem->widget() == toolBar) {
                    found = true;
                    result.prepend(k);
                    break;
                }
            }

            if (found) {
                result.prepend(j);
                break;
            }
        }

        if (found) {
            result.prepend(i);
            break;
        }
    }

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 979, as _ZNK18QToolBarAreaLayout8gapIndexERK6QPoint
inline QList<int> QToolBarAreaLayout::gapIndex(const QPoint &pos) const
{
    Qt::LayoutDirection dir = mainWindow->layoutDirection();
    int minDistance = 80; // when a dock area is empty, how "wide" is it?
    QList<int> ret; //return value
    for (int i = 0; i < QInternal::DockCount; ++i) {
        QPoint p = pos;
        if (docks[i].o == Qt::Horizontal)
            p = QStyle::visualPos(dir, docks[i].rect, p);
        QList<int> result = docks[i].gapIndex(p, &minDistance);
        if (!result.isEmpty()) {
            result.prepend(i);
            ret = result;
        }
    }

    return ret;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 998, as _ZNK18QToolBarAreaLayout15currentGapIndexEv
inline QList<int> QToolBarAreaLayout::currentGapIndex() const
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines[j];

            for (int k = 0; k < line.toolBarItems.size(); k++) {
                if (line.toolBarItems[k].gap) {
                    QList<int> result;
                    result << i << j << k;
                    return result;
                }
            }
        }
    }
    return QList<int>();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1018, as _ZN18QToolBarAreaLayout9insertGapERK5QListIiEP11QLayoutItem
inline bool QToolBarAreaLayout::insertGap(const QList<int> &path, QLayoutItem *item)
{
    Q_ASSERT(path.size() == 3);
    const int i = path.first();
    Q_ASSERT(i >= 0 && i < QInternal::DockCount);
    return docks[i].insertGap(path.mid(1), item);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1026, as _ZN18QToolBarAreaLayout6removeERK5QListIiE
inline void QToolBarAreaLayout::remove(const QList<int> &path)
{
    Q_ASSERT(path.size() == 3);
    QToolBarAreaLayoutInfo &dock = docks[path.at(0)];
    QToolBarAreaLayoutLine &line = dock.lines[path.at(1)];
    line.toolBarItems.removeAt(path.at(2));
    if (line.toolBarItems.isEmpty())
        dock.lines.removeAt(path.at(1));
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1036, as _ZN18QToolBarAreaLayout6removeEP11QLayoutItem
inline void QToolBarAreaLayout::remove(QLayoutItem *item)
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            QToolBarAreaLayoutLine &line = dock.lines[j];

            for (int k = 0; k < line.toolBarItems.size(); k++) {
                if (line.toolBarItems[k].widgetItem == item) {
                    line.toolBarItems.removeAt(k);
                    if (line.toolBarItems.isEmpty())
                        dock.lines.removeAt(j);
                    return;
                }
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1056, as _ZN18QToolBarAreaLayout5clearEv
inline void QToolBarAreaLayout::clear()
{
    for (int i = 0; i < QInternal::DockCount; ++i)
        docks[i].clear();
    rect = QRect();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1063, as _ZN18QToolBarAreaLayout4itemERK5QListIiE
inline QToolBarAreaLayoutItem *QToolBarAreaLayout::item(const QList<int> &path)
{
    Q_ASSERT(path.size() == 3);

    if (path.at(0) < 0 || path.at(0) >= QInternal::DockCount)
        return nullptr;
    QToolBarAreaLayoutInfo &info = docks[path.at(0)];
    if (path.at(1) < 0 || path.at(1) >= info.lines.size())
        return nullptr;
    QToolBarAreaLayoutLine &line = info.lines[path.at(1)];
    if (path.at(2) < 0 || path.at(2) >= line.toolBarItems.size())
        return nullptr;
    return &(line.toolBarItems[path.at(2)]);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1078, as _ZNK18QToolBarAreaLayout8itemRectERK5QListIiE
inline QRect QToolBarAreaLayout::itemRect(const QList<int> &path) const
{
    const int i = path.first();

    QRect r = docks[i].itemRect(path.mid(1));
    if (docks[i].o == Qt::Horizontal)
        r = QStyle::visualRect(mainWindow->layoutDirection(),
                                docks[i].rect, r);
    return r;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1089, as _ZN18QToolBarAreaLayout4plugERK5QListIiE
inline QLayoutItem *QToolBarAreaLayout::plug(const QList<int> &path)
{
    QToolBarAreaLayoutItem *item = this->item(path);
    if (Q_UNLIKELY(!item)) {
        qWarning() << "No item at" << path;
        return nullptr;
    }
    Q_ASSERT(item->gap);
    Q_ASSERT(item->widgetItem != nullptr);
    item->gap = false;
    return item->widgetItem;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1102, as _ZN18QToolBarAreaLayout6unplugERK5QListIiEPS_
inline QLayoutItem *QToolBarAreaLayout::unplug(const QList<int> &path, QToolBarAreaLayout *other)
{
    //other needs to be update as well
    Q_ASSERT(path.size() == 3);
    QToolBarAreaLayoutItem *item = this->item(path);
    Q_ASSERT(item);

    //update the leading space here
    QToolBarAreaLayoutInfo &info = docks[path.at(0)];
    QToolBarAreaLayoutLine &line = info.lines[path.at(1)];
    if (item->size != pick(line.o, item->realSizeHint())) {
        //the item doesn't have its default size
        //so we'll give this to the next item
        int newExtraSpace = 0;
        //let's iterate over the siblings of the current item that pare placed before it
        //we need to find just the one before
        for (int i = path.at(2) - 1; i >= 0; --i) {
            QToolBarAreaLayoutItem &previous = line.toolBarItems[i];
            if (!previous.skip()) {
                //we need to check if it has a previous element and a next one
                //the previous will get its size changed
                for (int j = path.at(2) + 1; j < line.toolBarItems.size(); ++j) {
                    const QToolBarAreaLayoutItem &next = line.toolBarItems.at(j);
                    if (!next.skip()) {
                        newExtraSpace = next.pos - previous.pos - pick(line.o, previous.sizeHint());
                        previous.resize(line.o, next.pos - previous.pos);
                        break;
                    }
                }
                break;
            }
        }

        if (other) {
            QToolBarAreaLayoutInfo &info = other->docks[path.at(0)];
            QToolBarAreaLayoutLine &line = info.lines[path.at(1)];
            for (int i = path.at(2) - 1; i >= 0; --i) {
                QToolBarAreaLayoutItem &previous = line.toolBarItems[i];
                if (!previous.skip()) {
                    previous.resize(line.o, pick(line.o, previous.sizeHint()) + newExtraSpace);
                    break;
                }
            }

        }
    }

    Q_ASSERT(!item->gap);
    item->gap = true;
    return item->widgetItem;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1201, as _ZNK18QToolBarAreaLayout9saveStateER11QDataStream
inline void QToolBarAreaLayout::saveState(QDataStream &stream) const
{
    // save toolbar state
    stream << static_cast<uchar>(StateMarkers::ToolBarEx);

    int lineCount = 0;
    for (int i = 0; i < QInternal::DockCount; ++i)
        lineCount += docks[i].lines.size();

    stream << lineCount;

    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            stream << i << int(line.toolBarItems.size());

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                const QToolBarAreaLayoutItem &item = line.toolBarItems.at(k);
                QWidget *widget = const_cast<QLayoutItem*>(item.widgetItem)->widget();
                QString objectName = widget->objectName();
                if (Q_UNLIKELY(objectName.isEmpty())) {
                    qWarning("QMainWindow::saveState(): 'objectName' not set for QToolBar %p '%s'",
                                widget, widget->windowTitle().toLocal8Bit().constData());
                }
                stream << objectName;
                // we store information as:
                // 1st bit: 1 if shown
                // 2nd bit: 1 if orientation is vertical (default is horizontal)
                uchar shownOrientation = (uchar)!widget->isHidden();
                if (QToolBar * tb= qobject_cast<QToolBar*>(widget)) {
                    if (tb->orientation() == Qt::Vertical)
                        shownOrientation |= 2;
                }
                stream << shownOrientation;
                stream << item.pos;
                //we store the preferred size. If the use rdidn't resize the toolbars it will be -1
                stream << item.preferredSize;

                uint geom0, geom1;
                packRect(&geom0, &geom1, widget->geometry(), widget->isWindow());
                stream << geom0 << geom1;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1340, as _ZNK18QToolBarAreaLayout7isEmptyEv
inline bool QToolBarAreaLayout::isEmpty() const
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        if (!docks[i].lines.isEmpty())
            return false;
    }
    return true;
}
//  -----------------------------------------------------------------------

//  QToolBarAreaLayout::QToolBarAreaLayout(const QMainWindow *win)
extern "C" Q_DECL_EXPORT
QToolBarAreaLayout *ritual_ZN18QToolBarAreaLayoutC1EPK11QMainWindow(
    const QMainWindow *win) {
  return new QToolBarAreaLayout(win);
}

//  QSize QToolBarAreaLayout::minimumSize(const QSize &centerMin) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QToolBarAreaLayout11minimumSizeERK5QSize(
    const QToolBarAreaLayout *self,
    const QSize *centerMin) {
  return new QSize(self->minimumSize(*centerMin));
}

//  QRect QToolBarAreaLayout::rectHint(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QToolBarAreaLayout8rectHintERK5QRect(
    const QToolBarAreaLayout *self,
    const QRect *r) {
  return new QRect(self->rectHint(*r));
}

//  QSize QToolBarAreaLayout::sizeHint(const QSize &center) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QToolBarAreaLayout8sizeHintERK5QSize(
    const QToolBarAreaLayout *self,
    const QSize *center) {
  return new QSize(self->sizeHint(*center));
}

//  QLayoutItem *QToolBarAreaLayout::itemAt(int *x, int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK18QToolBarAreaLayout6itemAtEPii(
    const QToolBarAreaLayout *self,
    int *x,
    int index) {
  return self->itemAt(x, index);
}

//  QLayoutItem *QToolBarAreaLayout::takeAt(int *x, int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN18QToolBarAreaLayout6takeAtEPii(
    QToolBarAreaLayout *self,
    int *x,
    int index) {
  return self->takeAt(x, index);
}

//  void QToolBarAreaLayout::deleteAllLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout20deleteAllLayoutItemsEv(
    QToolBarAreaLayout *self) {
  self->deleteAllLayoutItems();
}

//  QLayoutItem *QToolBarAreaLayout::insertToolBar(QToolBar *before, QToolBar
//      *toolBar)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN18QToolBarAreaLayout13insertToolBarEP8QToolBarS1_(
    QToolBarAreaLayout *self,
    QToolBar *before,
    QToolBar *toolBar) {
  return self->insertToolBar(before, toolBar);
}

//  void QToolBarAreaLayout::removeToolBar(QToolBar *toolBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout13removeToolBarEP8QToolBar(
    QToolBarAreaLayout *self,
    QToolBar *toolBar) {
  self->removeToolBar(toolBar);
}

//  QLayoutItem *QToolBarAreaLayout::addToolBar(QInternal::DockPosition pos,
//      QToolBar *toolBar)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN18QToolBarAreaLayout10addToolBarEN9QInternal12DockPositionEP8QToolBar(
    QToolBarAreaLayout *self,
    QInternal::DockPosition pos,
    QToolBar *toolBar) {
  return self->addToolBar(pos, toolBar);
}

//  void QToolBarAreaLayout::insertToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout18insertToolBarBreakEP8QToolBar(
    QToolBarAreaLayout *self,
    QToolBar *before) {
  self->insertToolBarBreak(before);
}

//  void QToolBarAreaLayout::removeToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout18removeToolBarBreakEP8QToolBar(
    QToolBarAreaLayout *self,
    QToolBar *before) {
  self->removeToolBarBreak(before);
}

//  void QToolBarAreaLayout::addToolBarBreak(QInternal::DockPosition pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout15addToolBarBreakEN9QInternal12DockPositionE(
    QToolBarAreaLayout *self,
    QInternal::DockPosition pos) {
  self->addToolBarBreak(pos);
}

//  void QToolBarAreaLayout::insertItem(QInternal::DockPosition pos,
//      QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout10insertItemEN9QInternal12DockPositionEP11QLayoutItem(
    QToolBarAreaLayout *self,
    QInternal::DockPosition pos,
    QLayoutItem *item) {
  self->insertItem(pos, item);
}

//  void QToolBarAreaLayout::insertItem(QToolBar *before, QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout10insertItemEP8QToolBarP11QLayoutItem(
    QToolBarAreaLayout *self,
    QToolBar *before,
    QLayoutItem *item) {
  self->insertItem(before, item);
}

//  std::optional<QInternal::DockPosition>
//      QToolBarAreaLayout::findToolBar(const QToolBar *toolBar) const
extern "C" Q_DECL_EXPORT
std::optional<QInternal::DockPosition> *ritual_ZNK18QToolBarAreaLayout11findToolBarEPK8QToolBar(
    const QToolBarAreaLayout *self,
    const QToolBar *toolBar) {
  return new std::optional<QInternal::DockPosition>(
      self->findToolBar(
          toolBar));
}

//  bool QToolBarAreaLayout::toolBarBreak(QToolBar *toolBar) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QToolBarAreaLayout12toolBarBreakEP8QToolBar(
    const QToolBarAreaLayout *self,
    QToolBar *toolBar) {
  return self->toolBarBreak(toolBar);
}

//  void QToolBarAreaLayout::getStyleOptionInfo(QStyleOptionToolBar *option,
//      QToolBar *toolBar) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QToolBarAreaLayout18getStyleOptionInfoEP19QStyleOptionToolBarP8QToolBar(
    const QToolBarAreaLayout *self,
    QStyleOptionToolBar *option,
    QToolBar *toolBar) {
  self->getStyleOptionInfo(option, toolBar);
}

//  QList<int> QToolBarAreaLayout::indexOf(QWidget *toolBar) const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK18QToolBarAreaLayout7indexOfEP7QWidget(
    const QToolBarAreaLayout *self,
    QWidget *toolBar) {
  return new QList<int>(self->indexOf(toolBar));
}

//  QList<int> QToolBarAreaLayout::gapIndex(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK18QToolBarAreaLayout8gapIndexERK6QPoint(
    const QToolBarAreaLayout *self,
    const QPoint *pos) {
  return new QList<int>(self->gapIndex(*pos));
}

//  QList<int> QToolBarAreaLayout::currentGapIndex() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK18QToolBarAreaLayout15currentGapIndexEv(
    const QToolBarAreaLayout *self) {
  return new QList<int>(self->currentGapIndex());
}

//  bool QToolBarAreaLayout::insertGap(const QList<int> &path, QLayoutItem
//      *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QToolBarAreaLayout9insertGapERK5QListIiEP11QLayoutItem(
    QToolBarAreaLayout *self,
    const QList<int> *path,
    QLayoutItem *item) {
  return self->insertGap(*path, item);
}

//  void QToolBarAreaLayout::remove(const QList<int> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout6removeERK5QListIiE(
    QToolBarAreaLayout *self,
    const QList<int> *path) {
  self->remove(*path);
}

//  void QToolBarAreaLayout::remove(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout6removeEP11QLayoutItem(
    QToolBarAreaLayout *self,
    QLayoutItem *item) {
  self->remove(item);
}

//  void QToolBarAreaLayout::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayout5clearEv(QToolBarAreaLayout *self) {
  self->clear();
}

//  QToolBarAreaLayoutItem *QToolBarAreaLayout::item(const QList<int> &path)
extern "C" Q_DECL_EXPORT
QToolBarAreaLayoutItem *ritual_ZN18QToolBarAreaLayout4itemERK5QListIiE(
    QToolBarAreaLayout *self,
    const QList<int> *path) {
  return self->item(*path);
}

//  QRect QToolBarAreaLayout::itemRect(const QList<int> &path) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QToolBarAreaLayout8itemRectERK5QListIiE(
    const QToolBarAreaLayout *self,
    const QList<int> *path) {
  return new QRect(self->itemRect(*path));
}

//  QLayoutItem *QToolBarAreaLayout::plug(const QList<int> &path)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN18QToolBarAreaLayout4plugERK5QListIiE(
    QToolBarAreaLayout *self,
    const QList<int> *path) {
  return self->plug(*path);
}

//  QLayoutItem *QToolBarAreaLayout::unplug(const QList<int> &path,
//      QToolBarAreaLayout *other)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN18QToolBarAreaLayout6unplugERK5QListIiEPS_(
    QToolBarAreaLayout *self,
    const QList<int> *path,
    QToolBarAreaLayout *other) {
  return self->unplug(*path, other);
}

//  void QToolBarAreaLayout::saveState(QDataStream &stream) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QToolBarAreaLayout9saveStateER11QDataStream(
    const QToolBarAreaLayout *self,
    QDataStream *stream) {
  self->saveState(*stream);
}

//  bool QToolBarAreaLayout::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QToolBarAreaLayout7isEmptyEv(
    const QToolBarAreaLayout *self) {
  return self->isEmpty();
}

//  QToolBarAreaLayout::~QToolBarAreaLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QToolBarAreaLayoutD1Ev(QToolBarAreaLayout *self) {
  delete self;
}

//  a std::optional<QInternal::DockPosition> a ritual of QToolBarAreaLayout
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QToolBarAreaLayout__std_optional_QInternal_DockPosition(
    std::optional<QInternal::DockPosition> *self) {
  delete self;
}

//  a QList<int> a ritual of QToolBarAreaLayout gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QToolBarAreaLayout__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(toolbar)
#endif  // QT_CONFIG(toolbar)
