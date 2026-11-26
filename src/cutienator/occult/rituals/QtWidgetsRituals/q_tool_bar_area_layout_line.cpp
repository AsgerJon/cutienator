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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 66, as _ZN22QToolBarAreaLayoutLineC1EN2Qt11OrientationE
inline QToolBarAreaLayoutLine::QToolBarAreaLayoutLine(Qt::Orientation orientation)
    : o(orientation)
{
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 153, as _ZNK22QToolBarAreaLayoutLine4skipEv
inline bool QToolBarAreaLayoutLine::skip() const
{
    for (int i = 0; i < toolBarItems.size(); ++i) {
        if (!toolBarItems.at(i).skip())
            return false;
    }
    return true;
}
//  -----------------------------------------------------------------------

//  QToolBarAreaLayoutLine::QToolBarAreaLayoutLine()
extern "C" Q_DECL_EXPORT
QToolBarAreaLayoutLine *ritual_ZN22QToolBarAreaLayoutLineC1Ev() {
  return new QToolBarAreaLayoutLine();
}

//  QToolBarAreaLayoutLine::QToolBarAreaLayoutLine(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
QToolBarAreaLayoutLine *ritual_ZN22QToolBarAreaLayoutLineC1EN2Qt11OrientationE(
    Qt::Orientation orientation) {
  return new QToolBarAreaLayoutLine(orientation);
}

//  QSize QToolBarAreaLayoutLine::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QToolBarAreaLayoutLine8sizeHintEv(
    const QToolBarAreaLayoutLine *self) {
  return new QSize(self->sizeHint());
}

//  QSize QToolBarAreaLayoutLine::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QToolBarAreaLayoutLine11minimumSizeEv(
    const QToolBarAreaLayoutLine *self) {
  return new QSize(self->minimumSize());
}

//  bool QToolBarAreaLayoutLine::skip() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QToolBarAreaLayoutLine4skipEv(
    const QToolBarAreaLayoutLine *self) {
  return self->skip();
}

//  QToolBarAreaLayoutLine::~QToolBarAreaLayoutLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutLineD1Ev(QToolBarAreaLayoutLine *self) {
  delete self;
}

#endif  // QT_CONFIG(toolbar)
#endif  // QT_CONFIG(toolbar)
