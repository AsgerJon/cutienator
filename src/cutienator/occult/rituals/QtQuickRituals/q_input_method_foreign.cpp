//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickforeignutils_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(im)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickforeignutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QInputMethodForeign::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputMethodForeign20qt_qmlMarker_foreignEv(
    QInputMethodForeign *self) {
  self->qt_qmlMarker_foreign();
}

//  void QInputMethodForeign::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputMethodForeign24qt_qmlMarker_uncreatableEv(
    QInputMethodForeign *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QInputMethodForeign::~QInputMethodForeign()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputMethodForeignD1Ev(QInputMethodForeign *self) {
  delete self;
}

#endif  // QT_CONFIG(im)
