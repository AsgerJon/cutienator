//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h>
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
#include <QtWidgets/private/qdockarealayout_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtWidgets/private/qmenu_p.h>
#include <QtWidgets/private/qdockwidget_p.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#endif
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/QWidgetItem>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QStyleOption>
#include <QtWidgets/QApplication>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qtoolbararealayout_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbar_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(dockwidget)
#include <QtWidgets/private/qdockarealayout_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/private/qdockwidget_p.h>
#endif
#if QT_CONFIG(toolbar)
#include <QtWidgets/private/qtoolbar_p.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#endif
#include <QtWidgets/qmainwindow.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/qrubberband.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/private/qtabbar_p.h>
#endif
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtCore/qmimedata.h>
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#endif
#include <QtCore/qstring.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstylepainter.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qstack.h>
#include <QtCore/qmap.h>
#include <QtCore/qpointer.h>
#ifndef QT_NO_DEBUG_STREAM
#  include <QtCore/qdebug.h>
#  include <QtCore/qtextstream.h>
#endif
#include <QtWidgets/private/qmenu_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtCore/QScopedValueRollback>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qdockarealayout.cpp, line 2428, as _ZN15QDockAreaLayoutC1EP11QMainWindow
inline QDockAreaLayout::QDockAreaLayout(QMainWindow *win) : fallbackToSizeHints(true)
{
    mainWindow = win;
    sep = win->style()->pixelMetric(QStyle::PM_DockWidgetSeparatorExtent, nullptr, win);
#if QT_CONFIG(tabbar)
    const int tabShape = QTabBar::RoundedSouth;
#else
    const int tabShape = 0;
#endif
    docks[QInternal::LeftDock]
        = QDockAreaLayoutInfo(&sep, QInternal::LeftDock, Qt::Vertical, tabShape, win);
    docks[QInternal::RightDock]
        = QDockAreaLayoutInfo(&sep, QInternal::RightDock, Qt::Vertical, tabShape, win);
    docks[QInternal::TopDock]
        = QDockAreaLayoutInfo(&sep, QInternal::TopDock, Qt::Horizontal, tabShape, win);
    docks[QInternal::BottomDock]
        = QDockAreaLayoutInfo(&sep, QInternal::BottomDock, Qt::Horizontal, tabShape, win);
    centralWidgetItem = nullptr;


    corners[Qt::TopLeftCorner] = Qt::TopDockWidgetArea;
    corners[Qt::TopRightCorner] = Qt::TopDockWidgetArea;
    corners[Qt::BottomLeftCorner] = Qt::BottomDockWidgetArea;
    corners[Qt::BottomRightCorner] = Qt::BottomDockWidgetArea;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 594, as _ZN18QToolBarAreaLayoutC1EPK11QMainWindow
inline QToolBarAreaLayout::QToolBarAreaLayout(const QMainWindow *win) : mainWindow(win), visible(true)
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        QInternal::DockPosition pos = static_cast<QInternal::DockPosition>(i);
        docks[i] = QToolBarAreaLayoutInfo(pos);
    }
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3527, as _ZN15QDockAreaLayout20deleteAllLayoutItemsEv
inline void QDockAreaLayout::deleteAllLayoutItems()
{
    for (auto &dock : docks)
        dock.deleteAllLayoutItems();
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3137, as _ZNK15QDockAreaLayout8sizeHintEv
inline QSize QDockAreaLayout::sizeHint() const
{
    return size_helper(&QDockAreaLayoutInfo::sizeHint, &QLayoutItem::sizeHint);
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3142, as _ZNK15QDockAreaLayout11minimumSizeEv
inline QSize QDockAreaLayout::minimumSize() const
{
    return size_helper(&QDockAreaLayoutInfo::minimumSize, &QLayoutItem::minimumSize);
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3152, as _ZNK15QDockAreaLayout17minimumStableSizeEv
inline QSize QDockAreaLayout::minimumStableSize() const
{
    return size_helper(&QDockAreaLayoutInfo::size, &QLayoutItem::minimumSize);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3064, as _ZN15QDockAreaLayout9fitLayoutEv
inline void QDockAreaLayout::fitLayout()
{
    QList<QLayoutStruct> ver_struct_list(3);
    QList<QLayoutStruct> hor_struct_list(3);
    getGrid(&ver_struct_list, &hor_struct_list);

    qGeomCalc(ver_struct_list, 0, 3, rect.top(), rect.height(), sep);
    qGeomCalc(hor_struct_list, 0, 3, rect.left(), rect.width(), sep);

    setGrid(&ver_struct_list, &hor_struct_list);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 602, as _ZN18QToolBarAreaLayout9fitLayoutEv
inline QRect QToolBarAreaLayout::fitLayout()
{
    if (!visible)
        return rect;

    QSize left_hint = docks[QInternal::LeftDock].sizeHint();
    QSize right_hint = docks[QInternal::RightDock].sizeHint();
    QSize top_hint = docks[QInternal::TopDock].sizeHint();
    QSize bottom_hint = docks[QInternal::BottomDock].sizeHint();

    QRect center = rect.adjusted(left_hint.width(), top_hint.height(),
                                    -right_hint.width(), -bottom_hint.height());

    docks[QInternal::TopDock].rect = QRect(rect.left(), rect.top(),
                                rect.width(), top_hint.height());
    docks[QInternal::LeftDock].rect = QRect(rect.left(), center.top(),
                                left_hint.width(), center.height());
    docks[QInternal::RightDock].rect = QRect(center.right() + 1, center.top(),
                                    right_hint.width(), center.height());
    docks[QInternal::BottomDock].rect = QRect(rect.left(), center.bottom() + 1,
                                    rect.width(), bottom_hint.height());

    docks[QInternal::TopDock].fitLayout();
    docks[QInternal::LeftDock].fitLayout();
    docks[QInternal::RightDock].fitLayout();
    docks[QInternal::BottomDock].fitLayout();

    return center;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3494, as _ZNK15QDockAreaLayout6itemAtEPii
inline QLayoutItem *QDockAreaLayout::itemAt(int *x, int index) const
{
    Q_ASSERT(x != nullptr);

    for (const auto &dock : docks) {
        if (QLayoutItem *ret = dock.itemAt(x, index))
            return ret;
    }

    if (centralWidgetItem && (*x)++ == index)
        return centralWidgetItem;

    return nullptr;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3509, as _ZN15QDockAreaLayout6takeAtEPii
inline QLayoutItem *QDockAreaLayout::takeAt(int *x, int index)
{
    Q_ASSERT(x != nullptr);

    for (auto &dock : docks) {
        if (QLayoutItem *ret = dock.takeAt(x, index))
            return ret;
    }

    if (centralWidgetItem && (*x)++ == index) {
        QLayoutItem *ret = centralWidgetItem;
        centralWidgetItem = nullptr;
        return ret;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2534, as _ZNK15QDockAreaLayout7indexOfEPK7QWidget
inline QList<int> QDockAreaLayout::indexOf(const QWidget *dockWidget) const
{
    for (std::size_t i = 0; i < docks.size(); ++i) {
        QList<int> result = docks[i].indexOf(dockWidget);
        if (!result.isEmpty()) {
            result.prepend(int(i));
            return result;
        }
    }
    return QList<int>();
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2764, as _ZN15QDockAreaLayout6removeERK5QListIiE
inline void QDockAreaLayout::remove(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    docks[index].remove(path.mid(1));
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3076, as _ZN15QDockAreaLayout5clearEv
inline void QDockAreaLayout::clear()
{
    for (auto &dock : docks)
        dock.clear();

    rect = QRect();
    centralWidgetRect = QRect();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1056, as _ZN18QToolBarAreaLayout5clearEv
inline void QToolBarAreaLayout::clear()
{
    for (int i = 0; i < QInternal::DockCount; ++i)
        docks[i].clear();
    rect = QRect();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 264, as _ZN19QDockAreaLayoutInfoC1EPKiN9QInternal12DockPositionEN2Qt11OrientationEiP11QMainWindow
inline QDockAreaLayoutInfo::QDockAreaLayoutInfo(const int *_sep, QInternal::DockPosition _dockPos,
                                            Qt::Orientation _o, int tbshape,
                                            QMainWindow *window)
    : sep(_sep), dockPos(_dockPos), o(_o), mainWindow(window)
#if QT_CONFIG(tabbar)
    , tabbed(false), tabBar(nullptr), tabBarShape(static_cast<QTabBar::Shape>(tbshape))
#endif
{
#if !QT_CONFIG(tabbar)
    Q_UNUSED(tbshape);
#endif
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1854, as _ZN19QDockAreaLayoutInfo20deleteAllLayoutItemsEv
inline void QDockAreaLayoutInfo::deleteAllLayoutItems()
{
    for (int i = 0; i < item_list.size(); ++i) {
        QDockAreaLayoutItem &item= item_list[i];
        if (item.subinfo) {
            item.subinfo->deleteAllLayoutItems();
        } else {
            delete item.widgetItem;
            item.widgetItem = nullptr;
        }
    }
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2968, as _ZN15QDockAreaLayout7setGridEP5QListI13QLayoutStructES3_
inline void QDockAreaLayout::setGrid(QList<QLayoutStruct> *ver_struct_list,
                              QList<QLayoutStruct> *hor_struct_list)
{

    // top ---------------------------------------------------

    if (!docks[QInternal::TopDock].isEmpty()) {
        QRect r = docks[QInternal::TopDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(corners[Qt::TopLeftCorner] == Qt::TopDockWidgetArea
                || docks[QInternal::LeftDock].isEmpty()
                ? rect.left() : hor_struct_list->at(1).pos);
            r.setRight(corners[Qt::TopRightCorner] == Qt::TopDockWidgetArea
                || docks[QInternal::RightDock].isEmpty()
                ? rect.right() : hor_struct_list->at(2).pos - sep - 1);
        }
        if (ver_struct_list != nullptr) {
            r.setTop(rect.top());
            r.setBottom(ver_struct_list->at(1).pos - sep - 1);
        }
        docks[QInternal::TopDock].rect = r;
        docks[QInternal::TopDock].fitItems();
    }

    // bottom ---------------------------------------------------

    if (!docks[QInternal::BottomDock].isEmpty()) {
        QRect r = docks[QInternal::BottomDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(corners[Qt::BottomLeftCorner] == Qt::BottomDockWidgetArea
                        || docks[QInternal::LeftDock].isEmpty()
                            ? rect.left() : hor_struct_list->at(1).pos);
            r.setRight(corners[Qt::BottomRightCorner] == Qt::BottomDockWidgetArea
                        || docks[QInternal::RightDock].isEmpty()
                            ? rect.right() : hor_struct_list->at(2).pos - sep - 1);
        }
        if (ver_struct_list != nullptr) {
            r.setTop(ver_struct_list->at(2).pos);
            r.setBottom(rect.bottom());
        }
        docks[QInternal::BottomDock].rect = r;
        docks[QInternal::BottomDock].fitItems();
    }

    // left ---------------------------------------------------

    if (!docks[QInternal::LeftDock].isEmpty()) {
        QRect r = docks[QInternal::LeftDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(rect.left());
            r.setRight(hor_struct_list->at(1).pos - sep - 1);
        }
        if (ver_struct_list != nullptr) {
            r.setTop(corners[Qt::TopLeftCorner] == Qt::LeftDockWidgetArea
                || docks[QInternal::TopDock].isEmpty()
                ? rect.top() : ver_struct_list->at(1).pos);
            r.setBottom(corners[Qt::BottomLeftCorner] == Qt::LeftDockWidgetArea
                || docks[QInternal::BottomDock].isEmpty()
                ? rect.bottom() : ver_struct_list->at(2).pos - sep - 1);
        }
        docks[QInternal::LeftDock].rect = r;
        docks[QInternal::LeftDock].fitItems();
    }

    // right ---------------------------------------------------

    if (!docks[QInternal::RightDock].isEmpty()) {
        QRect r = docks[QInternal::RightDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(hor_struct_list->at(2).pos);
            r.setRight(rect.right());
        }
        if (ver_struct_list != nullptr) {
            r.setTop(corners[Qt::TopRightCorner] == Qt::RightDockWidgetArea
                        || docks[QInternal::TopDock].isEmpty()
                            ? rect.top() : ver_struct_list->at(1).pos);
            r.setBottom(corners[Qt::BottomRightCorner] == Qt::RightDockWidgetArea
                        || docks[QInternal::BottomDock].isEmpty()
                            ? rect.bottom() : ver_struct_list->at(2).pos - sep - 1);
        }
        docks[QInternal::RightDock].rect = r;
        docks[QInternal::RightDock].fitItems();
    }

    // center ---------------------------------------------------

    if (hor_struct_list != nullptr) {
        centralWidgetRect.setLeft(hor_struct_list->at(1).pos);
        centralWidgetRect.setWidth(hor_struct_list->at(1).size);
    }
    if (ver_struct_list != nullptr) {
        centralWidgetRect.setTop(ver_struct_list->at(1).pos);
        centralWidgetRect.setHeight(ver_struct_list->at(1).size);
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1788, as _ZNK19QDockAreaLayoutInfo6itemAtEPii
inline QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.placeHolderItem != nullptr)
            continue;
        if (item.subinfo) {
            if (QLayoutItem *ret = item.subinfo->itemAt(x, index))
                return ret;
        } else if (item.widgetItem) {
            if ((*x)++ == index)
                return item.widgetItem;
        }
    }
    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1805, as _ZN19QDockAreaLayoutInfo6takeAtEPii
inline QLayoutItem *QDockAreaLayoutInfo::takeAt(int *x, int index)
{
    for (int i = 0; i < item_list.size(); ++i) {
        QDockAreaLayoutItem &item = item_list[i];
        if (item.placeHolderItem != nullptr)
            continue;
        else if (item.subinfo) {
            if (QLayoutItem *ret = item.subinfo->takeAt(x, index)) {
                unnest(i);
                return ret;
            }
        } else if (item.widgetItem) {
            if ((*x)++ == index) {
                QWidget *widget = item.widgetItem->widget();
                if (widget->isWidgetType())
                    item.placeHolderItem = new QPlaceHolderItem(widget);
                else
                    qCDebug(lcQpaDockWidgets) << widget << "is in destruction. No gap created.";
                QLayoutItem *ret = item.widgetItem;
                item.widgetItem = nullptr;
                if (item.size != -1)
                    item.flags |= QDockAreaLayoutItem::KeepSize;
                return ret;
            }
        }
    }
    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1507, as _ZNK19QDockAreaLayoutInfo7indexOfEPK7QWidget
inline QList<int> QDockAreaLayoutInfo::indexOf(const QWidget *widget) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);

        if (item.placeHolderItem != nullptr)
            continue;

        if (item.subinfo != nullptr) {
            QList<int> result = item.subinfo->indexOf(widget);
            if (!result.isEmpty()) {
                result.prepend(i);
                return result;
            }
            continue;
        }

        if (!(item.flags & QDockAreaLayoutItem::GapItem) && item.widgetItem && item.widgetItem->widget() == widget) {
            QList<int> result;
            result << i;
            return result;
        }
    }

    return QList<int>();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 282, as _ZN19QDockAreaLayoutInfo5clearEv
inline void QDockAreaLayoutInfo::clear()
{
    item_list.clear();
    rect = QRect();
#if QT_CONFIG(tabbar)
    tabbed = false;
    tabBar = nullptr;
#endif
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 536, as _ZN22QToolBarAreaLayoutInfo5clearEv
inline void QToolBarAreaLayoutInfo::clear()
{
    lines.clear();
    rect = QRect();
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 969, as _ZN22QMainWindowLayoutState23deleteCentralWidgetItemEv
inline void QMainWindowLayoutState::deleteCentralWidgetItem()
{
#if QT_CONFIG(dockwidget)
    delete dockAreaLayout.centralWidgetItem;
    dockAreaLayout.centralWidgetItem = nullptr;
#else
    delete centralWidgetItem;
    centralWidgetItem = 0;
#endif
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 980, as _ZNK22QMainWindowLayoutState6itemAtEiPi
inline QLayoutItem *QMainWindowLayoutState::itemAt(int index, int *x) const
{
#if QT_CONFIG(toolbar)
    if (QLayoutItem *ret = toolBarAreaLayout.itemAt(x, index))
        return ret;
#endif

#if QT_CONFIG(dockwidget)
    if (QLayoutItem *ret = dockAreaLayout.itemAt(x, index))
        return ret;
#else
    if (centralWidgetItem  && (*x)++ == index)
        return centralWidgetItem;
#endif

    return nullptr;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1046, as _ZNK22QMainWindowLayoutState8containsEP7QWidget
inline bool QMainWindowLayoutState::contains(QWidget *widget) const
{
#if QT_CONFIG(dockwidget)
    if (dockAreaLayout.centralWidgetItem != nullptr && dockAreaLayout.centralWidgetItem->widget() == widget)
        return true;
    if (!dockAreaLayout.indexOf(widget).isEmpty())
        return true;
#else
    if (centralWidgetItem && centralWidgetItem->widget() == widget)
        return true;
#endif

#if QT_CONFIG(toolbar)
    if (!toolBarAreaLayout.indexOf(widget).isEmpty())
        return true;
#endif
    return false;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1065, as _ZN22QMainWindowLayoutState16setCentralWidgetEP7QWidget
inline void QMainWindowLayoutState::setCentralWidget(QWidget *widget)
{
    QLayoutItem *item = nullptr;
    //make sure we remove the widget
    deleteCentralWidgetItem();

    if (widget != nullptr)
        item = new QWidgetItemV2(widget);

#if QT_CONFIG(dockwidget)
    dockAreaLayout.centralWidgetItem = item;
#else
    centralWidgetItem = item;
#endif
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1081, as _ZNK22QMainWindowLayoutState13centralWidgetEv
inline QWidget *QMainWindowLayoutState::centralWidget() const
{
    QLayoutItem *item = nullptr;

#if QT_CONFIG(dockwidget)
    item = dockAreaLayout.centralWidgetItem;
#else
    item = centralWidgetItem;
#endif

    if (item != nullptr)
        return item->widget();
    return nullptr;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1187, as _ZN22QMainWindowLayoutState5clearEv
inline void QMainWindowLayoutState::clear()
{
#if QT_CONFIG(toolbar)
    toolBarAreaLayout.clear();
#endif

#if QT_CONFIG(dockwidget)
    dockAreaLayout.clear();
#else
    centralWidgetRect = QRect();
#endif

    rect = QRect();
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1202, as _ZNK22QMainWindowLayoutState7isValidEv
inline bool QMainWindowLayoutState::isValid() const
{
    return rect.isValid();
}
//  -----------------------------------------------------------------------

//  void QMainWindowLayoutState::deleteCentralWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutState23deleteCentralWidgetItemEv(
    QMainWindowLayoutState *self) {
  self->deleteCentralWidgetItem();
}

//  QLayoutItem *QMainWindowLayoutState::itemAt(int index, int *x) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK22QMainWindowLayoutState6itemAtEiPi(
    const QMainWindowLayoutState *self,
    int index,
    int *x) {
  return self->itemAt(index, x);
}

//  bool QMainWindowLayoutState::contains(QWidget *widget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QMainWindowLayoutState8containsEP7QWidget(
    const QMainWindowLayoutState *self,
    QWidget *widget) {
  return self->contains(widget);
}

//  void QMainWindowLayoutState::setCentralWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutState16setCentralWidgetEP7QWidget(
    QMainWindowLayoutState *self,
    QWidget *widget) {
  self->setCentralWidget(widget);
}

//  QWidget *QMainWindowLayoutState::centralWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK22QMainWindowLayoutState13centralWidgetEv(
    const QMainWindowLayoutState *self) {
  return self->centralWidget();
}

//  void QMainWindowLayoutState::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutState5clearEv(
    QMainWindowLayoutState *self) {
  self->clear();
}

//  bool QMainWindowLayoutState::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QMainWindowLayoutState7isValidEv(
    const QMainWindowLayoutState *self) {
  return self->isValid();
}

//  QMainWindowLayoutState::~QMainWindowLayoutState()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutStateD1Ev(QMainWindowLayoutState *self) {
  delete self;
}

#endif  // QT_CONFIG(mainwindow)
#endif  // QT_CONFIG(mainwindow)
