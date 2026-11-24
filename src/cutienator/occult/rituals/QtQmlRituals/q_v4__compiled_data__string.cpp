//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  int QV4::CompiledData::String::calculateSize(const QString &str)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData6String13calculateSizeERK7QString(
    const QString *str) {
  return QV4::CompiledData::String::calculateSize(*str);
}

//  QV4::CompiledData::String::~String()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6StringD1Ev(
    QV4::CompiledData::String *self) {
  delete self;
}
