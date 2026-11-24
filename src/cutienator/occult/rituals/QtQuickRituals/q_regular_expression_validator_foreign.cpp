//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickforeignutils_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/qglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(validator)
#if QT_CONFIG(regularexpression)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickforeignutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QRegularExpressionValidatorForeign::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRegularExpressionValidatorForeign20qt_qmlMarker_foreignEv(
    QRegularExpressionValidatorForeign *self) {
  self->qt_qmlMarker_foreign();
}

//  QRegularExpressionValidatorForeign::~QRegularExpressionValidatorForeign()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRegularExpressionValidatorForeignD1Ev(
    QRegularExpressionValidatorForeign *self) {
  delete self;
}

#endif  // QT_CONFIG(regularexpression)
#endif  // QT_CONFIG(validator)
