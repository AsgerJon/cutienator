//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qelfparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(library)
#if defined(Q_OF_ELF)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qelfparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QElfParser::~QElfParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QElfParserD1Ev(QElfParser *self) {
  delete self;
}

#endif  // defined(Q_OF_ELF)
#endif  // QT_CONFIG(library)
