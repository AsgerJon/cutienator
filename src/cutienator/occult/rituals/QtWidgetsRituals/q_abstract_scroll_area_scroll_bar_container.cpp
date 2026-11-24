//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qwidget.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractscrollarea.h"
#if QT_CONFIG(scrollarea)
#include "qscrollbar.h"
#include "qapplication.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qevent.h"
#include "qdebug.h"
#include "qboxlayout.h"
#include "qpainter.h"
#include "qmargins.h"
#if QT_CONFIG(itemviews)
#include "qheaderview.h"
#endif
#include <QDebug>
#include "qabstractscrollarea_p.h"
#include "qscrollbar_p.h"
#include <qwidget.h>
#include <private/qguiapplication_p.h>
#include <qpa/qplatformtheme.h>
#include <private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <qt_windows.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 145, as _ZN37QAbstractScrollAreaScrollBarContainerC1EN2Qt11OrientationEP7QWidget
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaScrollBarContainer::QAbstractScrollAreaScrollBarContainer(Qt::Orientation orientation, QWidget *parent)
    :QWidget(parent), scrollBar(new QScrollBar(orientation, this)),
     layout(new QBoxLayout(orientation == Qt::Horizontal ? QBoxLayout::LeftToRight : QBoxLayout::TopToBottom)),
     orientation(orientation)
{
    setLayout(layout);
    layout->setContentsMargins(QMargins());
    layout->setSpacing(0);
    layout->addWidget(scrollBar);
    layout->setSizeConstraint(QLayout::SetMaximumSize);
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 160, as _ZN37QAbstractScrollAreaScrollBarContainer9addWidgetEP7QWidgetNS_15LogicalPositionE
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaScrollBarContainer::addWidget(QWidget *widget, LogicalPosition position)
{
    QSizePolicy policy = widget->sizePolicy();
    if (orientation == Qt::Vertical)
        policy.setHorizontalPolicy(QSizePolicy::Ignored);
    else
        policy.setVerticalPolicy(QSizePolicy::Ignored);
    widget->setSizePolicy(policy);
    widget->setParent(this);

    const int insertIndex = (position & LogicalLeft) ? 0 : scrollBarLayoutIndex() + 1;
    layout->insertWidget(insertIndex, widget);
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 178, as _ZN37QAbstractScrollAreaScrollBarContainer7widgetsENS_15LogicalPositionE
#if QT_CONFIG(scrollarea)
inline QWidgetList QAbstractScrollAreaScrollBarContainer::widgets(LogicalPosition position)
{
    QWidgetList list;
    const int scrollBarIndex = scrollBarLayoutIndex();
    if (position == LogicalLeft) {
        list.reserve(scrollBarIndex);
        for (int i = 0; i < scrollBarIndex; ++i)
            list.append(layout->itemAt(i)->widget());
    } else if (position == LogicalRight) {
        const int layoutItemCount = layout->count();
        list.reserve(layoutItemCount - (scrollBarIndex + 1));
        for (int i = scrollBarIndex + 1; i < layoutItemCount; ++i)
            list.append(layout->itemAt(i)->widget());
    }
    return list;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 201, as _ZNK37QAbstractScrollAreaScrollBarContainer20scrollBarLayoutIndexEv
#if QT_CONFIG(scrollarea)
inline int QAbstractScrollAreaScrollBarContainer::scrollBarLayoutIndex() const
{
    const int layoutItemCount = layout->count();
    for (int i = 0; i < layoutItemCount; ++i) {
        if (qobject_cast<QScrollBar *>(layout->itemAt(i)->widget()))
            return i;
    }
    return -1;
}
#endif  // QT_CONFIG(scrollarea)
//  -----------------------------------------------------------------------

//  QAbstractScrollAreaScrollBarContainer::QAbstractScrollAreaScrollBarContai
//      ner(Qt::Orientation orientation, QWidget *parent)
extern "C" Q_DECL_EXPORT
QAbstractScrollAreaScrollBarContainer *ritual_ZN37QAbstractScrollAreaScrollBarContainerC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation orientation,
    QWidget *parent) {
  return new QAbstractScrollAreaScrollBarContainer(orientation, parent);
}

#if QT_CONFIG(scrollarea)
//  void QAbstractScrollAreaScrollBarContainer::addWidget(QWidget *widget,
//      LogicalPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QAbstractScrollAreaScrollBarContainer9addWidgetEP7QWidgetNS_15LogicalPositionE(
    QAbstractScrollAreaScrollBarContainer *self,
    QWidget *widget,
    QAbstractScrollAreaScrollBarContainer::LogicalPosition position) {
  self->addWidget(widget, position);
}
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
//  QWidgetList
//      QAbstractScrollAreaScrollBarContainer::widgets(LogicalPosition
//      position)
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZN37QAbstractScrollAreaScrollBarContainer7widgetsENS_15LogicalPositionE(
    QAbstractScrollAreaScrollBarContainer *self,
    QAbstractScrollAreaScrollBarContainer::LogicalPosition position) {
  return new QList<QWidget *>(self->widgets(position));
}
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
//  int QAbstractScrollAreaScrollBarContainer::scrollBarLayoutIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK37QAbstractScrollAreaScrollBarContainer20scrollBarLayoutIndexEv(
    const QAbstractScrollAreaScrollBarContainer *self) {
  return self->scrollBarLayoutIndex();
}
#endif  // QT_CONFIG(scrollarea)

#endif  // QT_CONFIG(scrollarea)
