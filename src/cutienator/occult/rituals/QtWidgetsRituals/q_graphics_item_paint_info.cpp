//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGraphicsItemPaintInfo::QGraphicsItemPaintInfo(const QTransform *const
//      xform1, const QTransform *const xform2, const QTransform *const
//      xform3, QRegion *r, QWidget *w, QStyleOptionGraphicsItem *opt,
//      QPainter *p, qreal o, bool b1, bool b2)
extern "C" Q_DECL_EXPORT
QGraphicsItemPaintInfo *ritual_ZN22QGraphicsItemPaintInfoC1EPK10QTransformS2_S2_P7QRegionP7QWidgetP24QStyleOptionGraphicsItemP8QPainterdbb(
    const QTransform *const xform1,
    const QTransform *const xform2,
    const QTransform *const xform3,
    QRegion *r,
    QWidget *w,
    QStyleOptionGraphicsItem *opt,
    QPainter *p,
    qreal o,
    bool b1,
    bool b2) {
  return new QGraphicsItemPaintInfo(
      xform1,
      xform2,
      xform3,
      r,
      w,
      opt,
      p,
      o,
      b1,
      b2);
}

//  QGraphicsItemPaintInfo::~QGraphicsItemPaintInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemPaintInfoD1Ev(QGraphicsItemPaintInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
