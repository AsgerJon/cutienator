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
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  QList<int> QToolBarAreaLayoutInfo::gapIndex(const QPoint &pos, int
//      *maxDistance) const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK22QToolBarAreaLayoutInfo8gapIndexERK6QPointPi(
    const QToolBarAreaLayoutInfo *self,
    const QPoint *pos,
    int *maxDistance) {
  return new QList<int>(self->gapIndex(*pos, maxDistance));
}

//  bool QToolBarAreaLayoutInfo::insertGap(const QList<int> &path,
//      QLayoutItem *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QToolBarAreaLayoutInfo9insertGapERK5QListIiEP11QLayoutItem(
    QToolBarAreaLayoutInfo *self,
    const QList<int> *path,
    QLayoutItem *item) {
  return self->insertGap(*path, item);
}

//  void QToolBarAreaLayoutInfo::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutInfo5clearEv(
    QToolBarAreaLayoutInfo *self) {
  self->clear();
}

//  QRect QToolBarAreaLayoutInfo::itemRect(const QList<int> &path) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK22QToolBarAreaLayoutInfo8itemRectERK5QListIiE(
    const QToolBarAreaLayoutInfo *self,
    const QList<int> *path) {
  return new QRect(self->itemRect(*path));
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

//  a QList<int> a ritual of QToolBarAreaLayoutInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QToolBarAreaLayoutInfo__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(toolbar)
#endif  // QT_CONFIG(toolbar)
