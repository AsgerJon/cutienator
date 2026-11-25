//  Written by hand on 2026-11-25 from
//  QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimageincubator_p_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only
//  what its header writes out. Not written: the constructor,
//  which only a QQuickVectorImageIncubator has a use for.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimageincubator_p_p.h>
#include <QtQml/qqmlcomponent.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickVectorImageIncubatorPrivate
//      *QQuickVectorImageIncubatorPrivate::get(QQuickVectorImageIncubator
//      *incubator)
extern "C" Q_DECL_EXPORT
QQuickVectorImageIncubatorPrivate *ritual_ZN33QQuickVectorImageIncubatorPrivate3getEP26QQuickVectorImageIncubator(
    QQuickVectorImageIncubator *incubator) {
  return QQuickVectorImageIncubatorPrivate::get(incubator);
}

//  QQuickVectorImageIncubatorPrivate::~QQuickVectorImageIncubatorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickVectorImageIncubatorPrivateD1Ev(
    QQuickVectorImageIncubatorPrivate *self) {
  delete self;
}
