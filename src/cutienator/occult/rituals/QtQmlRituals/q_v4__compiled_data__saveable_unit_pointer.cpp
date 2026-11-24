//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QV4::CompiledData::SaveableUnitPointer::SaveableUnitPointer(const Unit
//      *unit, quint32 temporaryFlags)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::SaveableUnitPointer *ritual_ZN3QV412CompiledData19SaveableUnitPointerC1EPKNS0_4UnitEj(
    const QV4::CompiledData::Unit *unit,
    quint32 temporaryFlags) {
  return new QV4::CompiledData::SaveableUnitPointer(unit, temporaryFlags);
}

//  QV4::CompiledData::SaveableUnitPointer::~SaveableUnitPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData19SaveableUnitPointerD1Ev(
    QV4::CompiledData::SaveableUnitPointer *self) {
  delete self;
}

//  bool QV4::CompiledData::SaveableUnitPointer::writeDataToFile(const
//      QString &outputFileName, const char *data, quint32 size, QString
//      *errorString)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV412CompiledData19SaveableUnitPointer15writeDataToFileERK7QStringPKcjPS2_(
    const QString *outputFileName,
    const char *data,
    quint32 size,
    QString *errorString) {
  return QV4::CompiledData::SaveableUnitPointer::writeDataToFile(
      *outputFileName,
      data,
      size,
      errorString);
}

//  quint32 QV4::CompiledData::SaveableUnitPointer::size() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData19SaveableUnitPointer4sizeEv(
    const QV4::CompiledData::SaveableUnitPointer *self) {
  return self->size();
}
