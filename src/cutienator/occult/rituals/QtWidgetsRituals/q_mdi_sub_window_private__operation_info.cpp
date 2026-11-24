//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mdiarea)
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QMdiSubWindowPrivate::OperationInfo::OperationInfo(uint changeFlags,
//      Qt::CursorShape cursorShape, bool hover)
extern "C" Q_DECL_EXPORT
QMdiSubWindowPrivate::OperationInfo *ritual_ZN20QMdiSubWindowPrivate13OperationInfoC1EjN2Qt11CursorShapeEb(
    uint changeFlags,
    Qt::CursorShape cursorShape,
    bool hover) {
  return new QMdiSubWindowPrivate::OperationInfo(
      changeFlags,
      cursorShape,
      hover);
}

//  QMdiSubWindowPrivate::OperationInfo::~OperationInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate13OperationInfoD1Ev(
    QMdiSubWindowPrivate::OperationInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
