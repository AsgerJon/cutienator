//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickScrollBarPrivate::VisualArea::VisualArea(qreal pos, qreal sz)
extern "C" Q_DECL_EXPORT
QQuickScrollBarPrivate::VisualArea *ritual_ZN22QQuickScrollBarPrivate10VisualAreaC1Edd(
    qreal pos,
    qreal sz) {
  return new QQuickScrollBarPrivate::VisualArea(pos, sz);
}

//  QQuickScrollBarPrivate::VisualArea::~VisualArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate10VisualAreaD1Ev(
    QQuickScrollBarPrivate::VisualArea *self) {
  delete self;
}
