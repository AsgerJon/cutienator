//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qguiapplication_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QGuiApplicationPrivate::SynthesizedMouseData::SynthesizedMouseData(const
//      QPointF &p, const QPointF &sp, QWindow *w)
extern "C" Q_DECL_EXPORT
QGuiApplicationPrivate::SynthesizedMouseData *ritual_ZN22QGuiApplicationPrivate20SynthesizedMouseDataC1ERK7QPointFS3_P7QWindow(
    const QPointF *p,
    const QPointF *sp,
    QWindow *w) {
  return new QGuiApplicationPrivate::SynthesizedMouseData(*p, *sp, w);
}

//  QGuiApplicationPrivate::SynthesizedMouseData::~SynthesizedMouseData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate20SynthesizedMouseDataD1Ev(
    QGuiApplicationPrivate::SynthesizedMouseData *self) {
  delete self;
}
