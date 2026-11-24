//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicswidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicswidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGraphicsWidgetPrivate::WindowData::WindowData()
extern "C" Q_DECL_EXPORT
QGraphicsWidgetPrivate::WindowData *ritual_ZN22QGraphicsWidgetPrivate10WindowDataC1Ev() {
  return new QGraphicsWidgetPrivate::WindowData();
}

//  QGraphicsWidgetPrivate::WindowData::~WindowData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate10WindowDataD1Ev(
    QGraphicsWidgetPrivate::WindowData *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
