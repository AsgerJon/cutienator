//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qguiapplication_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGuiApplicationPrivate::TabletPointData::TabletPointData(qint64 devId)
extern "C" Q_DECL_EXPORT
QGuiApplicationPrivate::TabletPointData *ritual_ZN22QGuiApplicationPrivate15TabletPointDataC1Ex(
    qint64 devId) {
  return new QGuiApplicationPrivate::TabletPointData(devId);
}

//  QGuiApplicationPrivate::TabletPointData::~TabletPointData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate15TabletPointDataD1Ev(
    QGuiApplicationPrivate::TabletPointData *self) {
  delete self;
}
