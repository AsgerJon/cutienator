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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 55, as _ZNK22QToolBarAreaLayoutItem4skipEv
inline bool QToolBarAreaLayoutItem::skip() const
{
    if (gap)
        return false;
    return widgetItem == nullptr || widgetItem->isEmpty();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 26, as _ZNK22QToolBarAreaLayoutItem11minimumSizeEv
inline QSize QToolBarAreaLayoutItem::minimumSize() const
{
    if (skip())
        return QSize(0, 0);
    return qSmartMinSize(static_cast<QWidgetItem*>(widgetItem));
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
//  -----------------------------------------------------------------------

//  QToolBarAreaLayoutItem::QToolBarAreaLayoutItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
QToolBarAreaLayoutItem *ritual_ZN22QToolBarAreaLayoutItemC1EP11QLayoutItem(
    QLayoutItem *item) {
  return new QToolBarAreaLayoutItem(item);
}

//  bool QToolBarAreaLayoutItem::skip() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QToolBarAreaLayoutItem4skipEv(
    const QToolBarAreaLayoutItem *self) {
  return self->skip();
}

//  QSize QToolBarAreaLayoutItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QToolBarAreaLayoutItem11minimumSizeEv(
    const QToolBarAreaLayoutItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QToolBarAreaLayoutItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QToolBarAreaLayoutItem8sizeHintEv(
    const QToolBarAreaLayoutItem *self) {
  return new QSize(self->sizeHint());
}

//  QSize QToolBarAreaLayoutItem::realSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QToolBarAreaLayoutItem12realSizeHintEv(
    const QToolBarAreaLayoutItem *self) {
  return new QSize(self->realSizeHint());
}

//  void QToolBarAreaLayoutItem::resize(Qt::Orientation o, int newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutItem6resizeEN2Qt11OrientationEi(
    QToolBarAreaLayoutItem *self,
    Qt::Orientation o,
    int newSize) {
  self->resize(o, newSize);
}

//  void QToolBarAreaLayoutItem::extendSize(Qt::Orientation o, int extent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutItem10extendSizeEN2Qt11OrientationEi(
    QToolBarAreaLayoutItem *self,
    Qt::Orientation o,
    int extent) {
  self->extendSize(o, extent);
}

//  QToolBarAreaLayoutItem::~QToolBarAreaLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QToolBarAreaLayoutItemD1Ev(QToolBarAreaLayoutItem *self) {
  delete self;
}

#endif  // QT_CONFIG(toolbar)
#endif  // QT_CONFIG(toolbar)
