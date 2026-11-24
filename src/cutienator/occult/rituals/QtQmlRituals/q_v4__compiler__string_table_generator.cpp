//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compiler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QV4::Compiler::StringTableGenerator::StringTableGenerator()
extern "C" Q_DECL_EXPORT
QV4::Compiler::StringTableGenerator *ritual_ZN3QV48Compiler20StringTableGeneratorC1Ev() {
  return new QV4::Compiler::StringTableGenerator();
}

//  int QV4::Compiler::StringTableGenerator::registerString(const QString
//      &str)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler20StringTableGenerator14registerStringERK7QString(
    QV4::Compiler::StringTableGenerator *self,
    const QString *str) {
  return self->registerString(*str);
}

//  int QV4::Compiler::StringTableGenerator::getStringId(const QString
//      &string) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48Compiler20StringTableGenerator11getStringIdERK7QString(
    const QV4::Compiler::StringTableGenerator *self,
    const QString *string) {
  return self->getStringId(*string);
}

//  bool QV4::Compiler::StringTableGenerator::hasStringId(const QString
//      &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler20StringTableGenerator11hasStringIdERK7QString(
    const QV4::Compiler::StringTableGenerator *self,
    const QString *string) {
  return self->hasStringId(*string);
}

//  QString QV4::Compiler::StringTableGenerator::stringForIndex(int index)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Compiler20StringTableGenerator14stringForIndexEi(
    const QV4::Compiler::StringTableGenerator *self,
    int index) {
  return new QString(self->stringForIndex(index));
}

//  uint QV4::Compiler::StringTableGenerator::stringCount() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV48Compiler20StringTableGenerator11stringCountEv(
    const QV4::Compiler::StringTableGenerator *self) {
  return self->stringCount();
}

//  uint QV4::Compiler::StringTableGenerator::sizeOfTableAndData() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV48Compiler20StringTableGenerator18sizeOfTableAndDataEv(
    const QV4::Compiler::StringTableGenerator *self) {
  return self->sizeOfTableAndData();
}

//  void QV4::Compiler::StringTableGenerator::freeze()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler20StringTableGenerator6freezeEv(
    QV4::Compiler::StringTableGenerator *self) {
  self->freeze();
}

//  void QV4::Compiler::StringTableGenerator::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler20StringTableGenerator5clearEv(
    QV4::Compiler::StringTableGenerator *self) {
  self->clear();
}

//  void QV4::Compiler::StringTableGenerator::initializeFromBackingUnit(const
//      CompiledData::Unit *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler20StringTableGenerator25initializeFromBackingUnitEPKNS_12CompiledData4UnitE(
    QV4::Compiler::StringTableGenerator *self,
    const QV4::CompiledData::Unit *unit) {
  self->initializeFromBackingUnit(unit);
}

//  void QV4::Compiler::StringTableGenerator::serialize(CompiledData::Unit
//      *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler20StringTableGenerator9serializeEPNS_12CompiledData4UnitE(
    QV4::Compiler::StringTableGenerator *self,
    QV4::CompiledData::Unit *unit) {
  self->serialize(unit);
}

//  QStringList QV4::Compiler::StringTableGenerator::allStrings() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK3QV48Compiler20StringTableGenerator10allStringsEv(
    const QV4::Compiler::StringTableGenerator *self) {
  return new QList<QString>(self->allStrings());
}

//  QV4::Compiler::StringTableGenerator::~StringTableGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler20StringTableGeneratorD1Ev(
    QV4::Compiler::StringTableGenerator *self) {
  delete self;
}
