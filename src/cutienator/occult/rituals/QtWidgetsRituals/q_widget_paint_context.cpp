//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtCore/qpoint.h>

//  QWidgetPaintContext::QWidgetPaintContext(QPaintDevice *d, const QRegion
//      &r, const QPoint &o, QWidgetPrivate::DrawWidgetFlags f, QPainter *p,
//      QWidgetRepaintManager *rpm)
extern "C" Q_DECL_EXPORT
QWidgetPaintContext *ritual_ZN19QWidgetPaintContextC1EP12QPaintDeviceRK7QRegionRK6QPoint6QFlagsIN14QWidgetPrivate14DrawWidgetFlagEEP8QPainterP21QWidgetRepaintManager(
    QPaintDevice *d,
    const QRegion *r,
    const QPoint *o,
    int f,
    QPainter *p,
    QWidgetRepaintManager *rpm) {
  return new QWidgetPaintContext(
      d,
      *r,
      *o,
      QFlags<QWidgetPrivate::DrawWidgetFlag>::fromInt(f),
      p,
      rpm);
}

//  QWidgetPaintContext::~QWidgetPaintContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPaintContextD1Ev(QWidgetPaintContext *self) {
  delete self;
}
