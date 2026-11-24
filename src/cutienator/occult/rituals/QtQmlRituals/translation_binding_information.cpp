//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#if QT_CONFIG(translation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  TranslationBindingInformation::~TranslationBindingInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN29TranslationBindingInformationD1Ev(
    TranslationBindingInformation *self) {
  delete self;
}

#endif  // QT_CONFIG(translation)
#endif  // !(!QT_CONFIG(qml_debug))
