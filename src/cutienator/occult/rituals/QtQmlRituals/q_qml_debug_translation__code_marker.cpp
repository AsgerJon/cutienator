//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugtranslationprotocol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_debug)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugtranslationprotocol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator<(const CodeMarker &first, const CodeMarker &second)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlDebugTranslationltERKNS_10CodeMarkerES2_(
    const QQmlDebugTranslation::CodeMarker *first,
    const QQmlDebugTranslation::CodeMarker *second) {
  return operator<(*first, *second);
}

//  bool operator==(const CodeMarker &first, const CodeMarker &second)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlDebugTranslationeqERKNS_10CodeMarkerES2_(
    const QQmlDebugTranslation::CodeMarker *first,
    const QQmlDebugTranslation::CodeMarker *second) {
  return operator==(*first, *second);
}

//  QQmlDebugTranslation::CodeMarker::~CodeMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDebugTranslation10CodeMarkerD1Ev(
    QQmlDebugTranslation::CodeMarker *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_debug)
