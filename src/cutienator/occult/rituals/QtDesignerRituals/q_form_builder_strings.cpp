//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/formbuilderextra_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/formbuilderextra_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QFormBuilderStrings::QFormBuilderStrings()
extern "C" Q_DECL_EXPORT
QFormBuilderStrings *ritual_ZN19QFormBuilderStringsC1Ev() {
  return new QFormBuilderStrings();
}

//  const QFormBuilderStrings &QFormBuilderStrings::instance()
extern "C" Q_DECL_EXPORT
QFormBuilderStrings *ritual_ZN19QFormBuilderStrings8instanceEv() {
  return new QFormBuilderStrings(QFormBuilderStrings::instance());
}

//  QFormBuilderStrings::~QFormBuilderStrings()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFormBuilderStringsD1Ev(QFormBuilderStrings *self) {
  delete self;
}
