//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 292, as _ZNK19QDockAreaLayoutInfo7isEmptyEv
inline bool QDockAreaLayoutInfo::isEmpty() const
{
    return next(-1) == -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2764, as _ZN15QDockAreaLayout6removeERK5QListIiE
inline void QDockAreaLayout::remove(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    docks[index].remove(path.mid(1));
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2684, as _ZN15QDockAreaLayout4itemERK5QListIiE
inline QDockAreaLayoutItem &QDockAreaLayout::item(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    return docks[index].item(path.mid(1));
}

//  from src/widgets/widgets/qdockwidget.cpp, line 569, as _ZN15QDockWidgetItemC1EP11QDockWidget
inline QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
    : QWidgetItem(dockWidget)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1776, as _ZN19QDockAreaLayoutInfo4itemERK5QListIiE
inline QDockAreaLayoutItem &QDockAreaLayoutInfo::item(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    if (path.size() > 1) {
        const QDockAreaLayoutItem &item = item_list[index];
        Q_ASSERT(item.subinfo != nullptr);
        return item.subinfo->item(path.mid(1));
    }
    return item_list[index];
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1654, as _ZNK19QDockAreaLayoutInfo15separatorRegionEv
inline QRegion QDockAreaLayoutInfo::separatorRegion() const
{
    QRegion result;

    if (isEmpty())
        return result;
#if QT_CONFIG(tabbar)
    if (tabbed)
        return result;
#endif

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);

        if (item.skip())
            continue;

        int next = this->next(i);

        if (item.subinfo)
            result |= item.subinfo->separatorRegion();

        if (next == -1)
            break;
        result |= separatorRect(i);
    }

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1719, as _ZNK19QDockAreaLayoutInfo4nextEi
inline int QDockAreaLayoutInfo::next(int index) const
{
    for (int i = index + 1; i < item_list.size(); ++i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2454, as _ZNK15QDockAreaLayout7isValidEv
inline bool QDockAreaLayout::isValid() const
{
    return rect.isValid();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3163, as _ZN15QDockAreaLayout15constrainedRectE5QRectP7QWidget
inline QRect QDockAreaLayout::constrainedRect(QRect rect, QWidget* widget)
{
    QScreen *screen = nullptr;
    if (QGuiApplication::primaryScreen()->virtualSiblings().size() > 1)
        screen = QGuiApplication::screenAt(rect.topLeft());
    if (!screen)
        screen = widget->screen();

    const QRect screenRect = screen->geometry();
    if (screenRect.isValid()) {
        rect.setWidth(qMin(rect.width(), screenRect.width()));
        rect.setHeight(qMin(rect.height(), screenRect.height()));
        rect.moveLeft(qMax(rect.left(), screenRect.left()));
        rect.moveTop(qMax(rect.top(), screenRect.top()));
        rect.moveRight(qMin(rect.right(), screenRect.right()));
        rect.moveBottom(qMin(rect.bottom(), screenRect.bottom()));
    }

    return rect;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2700, as _ZNK15QDockAreaLayout13separatorRectEi
inline QRect QDockAreaLayout::separatorRect(int index) const
{
    const QDockAreaLayoutInfo &dock = docks[index];
    if (dock.isEmpty())
        return QRect();
    QRect r = dock.rect;
    switch (index) {
        case QInternal::LeftDock:
            return QRect(r.right() + 1, r.top(), sep, r.height());
        case QInternal::RightDock:
            return QRect(r.left() - sep, r.top(), sep, r.height());
        case QInternal::TopDock:
            return QRect(r.left(), r.bottom() + 1, r.width(), sep);
        case QInternal::BottomDock:
            return QRect(r.left(), r.top() - sep, r.width(), sep);
        default:
            break;
    }
    return QRect();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3076, as _ZN15QDockAreaLayout5clearEv
inline void QDockAreaLayout::clear()
{
    for (auto &dock : docks)
        dock.clear();

    rect = QRect();
    centralWidgetRect = QRect();
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
//  -----------------------------------------------------------------------

//  bool QDockAreaLayout::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDockAreaLayout7isValidEv(const QDockAreaLayout *self) {
  return self->isValid();
}

//  QRect QDockAreaLayout::constrainedRect(QRect rect, QWidget *widget)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15QDockAreaLayout15constrainedRectE5QRectP7QWidget(
    const QRect *rect,
    QWidget *widget) {
  return new QRect(QDockAreaLayout::constrainedRect(*rect, widget));
}

//  QRect QDockAreaLayout::separatorRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QDockAreaLayout13separatorRectEi(
    const QDockAreaLayout *self,
    int index) {
  return new QRect(self->separatorRect(index));
}

//  void QDockAreaLayout::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDockAreaLayout5clearEv(QDockAreaLayout *self) {
  self->clear();
}

//  QLayoutItem *QDockAreaLayout::itemAt(int *x, int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK15QDockAreaLayout6itemAtEPii(
    const QDockAreaLayout *self,
    int *x,
    int index) {
  return self->itemAt(x, index);
}

//  QDockAreaLayout::~QDockAreaLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDockAreaLayoutD1Ev(QDockAreaLayout *self) {
  delete self;
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
