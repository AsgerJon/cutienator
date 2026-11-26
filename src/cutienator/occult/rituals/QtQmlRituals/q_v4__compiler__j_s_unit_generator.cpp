//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compiler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  void
//      QV4::Compiler::JSUnitGenerator::generateUnitChecksum(CompiledData::Un
//      it *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler15JSUnitGenerator20generateUnitChecksumEPNS_12CompiledData4UnitE(
    QV4::CompiledData::Unit *unit) {
  QV4::Compiler::JSUnitGenerator::generateUnitChecksum(unit);
}

//  QV4::Compiler::JSUnitGenerator::JSUnitGenerator(Module *module)
extern "C" Q_DECL_EXPORT
QV4::Compiler::JSUnitGenerator *ritual_ZN3QV48Compiler15JSUnitGeneratorC1EPNS0_6ModuleE(
    QV4::Compiler::Module *module) {
  return new QV4::Compiler::JSUnitGenerator(module);
}

//  int QV4::Compiler::JSUnitGenerator::registerString(const QString &str)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator14registerStringERK7QString(
    QV4::Compiler::JSUnitGenerator *self,
    const QString *str) {
  return self->registerString(*str);
}

//  int QV4::Compiler::JSUnitGenerator::getStringId(const QString &string)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48Compiler15JSUnitGenerator11getStringIdERK7QString(
    const QV4::Compiler::JSUnitGenerator *self,
    const QString *string) {
  return self->getStringId(*string);
}

//  bool QV4::Compiler::JSUnitGenerator::hasStringId(const QString &string)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler15JSUnitGenerator11hasStringIdERK7QString(
    const QV4::Compiler::JSUnitGenerator *self,
    const QString *string) {
  return self->hasStringId(*string);
}

//  QString QV4::Compiler::JSUnitGenerator::stringForIndex(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Compiler15JSUnitGenerator14stringForIndexEi(
    const QV4::Compiler::JSUnitGenerator *self,
    int index) {
  return new QString(self->stringForIndex(index));
}

//  int QV4::Compiler::JSUnitGenerator::registerGetterLookup(const QString
//      &name, LookupMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator20registerGetterLookupERK7QStringNS1_10LookupModeE(
    QV4::Compiler::JSUnitGenerator *self,
    const QString *name,
    QV4::Compiler::JSUnitGenerator::LookupMode mode) {
  return self->registerGetterLookup(*name, mode);
}

//  int QV4::Compiler::JSUnitGenerator::registerGetterLookup(int nameIndex,
//      LookupMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator20registerGetterLookupEiNS1_10LookupModeE(
    QV4::Compiler::JSUnitGenerator *self,
    int nameIndex,
    QV4::Compiler::JSUnitGenerator::LookupMode mode) {
  return self->registerGetterLookup(nameIndex, mode);
}

//  int QV4::Compiler::JSUnitGenerator::registerSetterLookup(const QString
//      &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator20registerSetterLookupERK7QString(
    QV4::Compiler::JSUnitGenerator *self,
    const QString *name) {
  return self->registerSetterLookup(*name);
}

//  int QV4::Compiler::JSUnitGenerator::registerSetterLookup(int nameIndex)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator20registerSetterLookupEi(
    QV4::Compiler::JSUnitGenerator *self,
    int nameIndex) {
  return self->registerSetterLookup(nameIndex);
}

//  int QV4::Compiler::JSUnitGenerator::registerGlobalGetterLookup(int
//      nameIndex, LookupMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator26registerGlobalGetterLookupEiNS1_10LookupModeE(
    QV4::Compiler::JSUnitGenerator *self,
    int nameIndex,
    QV4::Compiler::JSUnitGenerator::LookupMode mode) {
  return self->registerGlobalGetterLookup(nameIndex, mode);
}

//  int QV4::Compiler::JSUnitGenerator::registerQmlContextPropertyGetterLooku
//      p(int nameIndex, LookupMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator38registerQmlContextPropertyGetterLookupEiNS1_10LookupModeE(
    QV4::Compiler::JSUnitGenerator *self,
    int nameIndex,
    QV4::Compiler::JSUnitGenerator::LookupMode mode) {
  return self->registerQmlContextPropertyGetterLookup(nameIndex, mode);
}

//  int QV4::Compiler::JSUnitGenerator::lookupNameIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48Compiler15JSUnitGenerator15lookupNameIndexEi(
    const QV4::Compiler::JSUnitGenerator *self,
    int index) {
  return self->lookupNameIndex(index);
}

//  QString QV4::Compiler::JSUnitGenerator::lookupName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Compiler15JSUnitGenerator10lookupNameEi(
    const QV4::Compiler::JSUnitGenerator *self,
    int index) {
  return new QString(self->lookupName(index));
}

//  int
//      QV4::Compiler::JSUnitGenerator::registerRegExp(QQmlJS::AST::RegExpLit
//      eral *regexp)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator14registerRegExpEPN6QQmlJS3AST13RegExpLiteralE(
    QV4::Compiler::JSUnitGenerator *self,
    QQmlJS::AST::RegExpLiteral *regexp) {
  return self->registerRegExp(regexp);
}

//  int QV4::Compiler::JSUnitGenerator::registerConstant(ReturnedValue v)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator16registerConstantEy(
    QV4::Compiler::JSUnitGenerator *self,
    QV4::ReturnedValue v) {
  return self->registerConstant(v);
}

//  ReturnedValue QV4::Compiler::JSUnitGenerator::constant(int idx) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV48Compiler15JSUnitGenerator8constantEi(
    const QV4::Compiler::JSUnitGenerator *self,
    int idx) {
  return self->constant(idx);
}

//  int QV4::Compiler::JSUnitGenerator::registerJSClass(const QStringList
//      &members)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator15registerJSClassERK5QListI7QStringE(
    QV4::Compiler::JSUnitGenerator *self,
    const QList<QString> *members) {
  return self->registerJSClass(*members);
}

//  int QV4::Compiler::JSUnitGenerator::jsClassSize(int jsClassId) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48Compiler15JSUnitGenerator11jsClassSizeEi(
    const QV4::Compiler::JSUnitGenerator *self,
    int jsClassId) {
  return self->jsClassSize(jsClassId);
}

//  QString QV4::Compiler::JSUnitGenerator::jsClassMember(int jsClassId, int
//      member) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Compiler15JSUnitGenerator13jsClassMemberEii(
    const QV4::Compiler::JSUnitGenerator *self,
    int jsClassId,
    int member) {
  return new QString(self->jsClassMember(jsClassId, member));
}

//  int QV4::Compiler::JSUnitGenerator::registerTranslation(const
//      CompiledData::TranslationData &translation)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler15JSUnitGenerator19registerTranslationERKNS_12CompiledData15TranslationDataE(
    QV4::Compiler::JSUnitGenerator *self,
    const QV4::CompiledData::TranslationData *translation) {
  return self->registerTranslation(*translation);
}

//  QV4::CompiledData::Unit
//      *QV4::Compiler::JSUnitGenerator::generateUnit(GeneratorOption option)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Unit *ritual_ZN3QV48Compiler15JSUnitGenerator12generateUnitENS1_15GeneratorOptionE(
    QV4::Compiler::JSUnitGenerator *self,
    QV4::Compiler::JSUnitGenerator::GeneratorOption option) {
  return self->generateUnit(option);
}

//  void QV4::Compiler::JSUnitGenerator::writeFunction(char *f, Context
//      *irFunction) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV48Compiler15JSUnitGenerator13writeFunctionEPcPNS0_7ContextE(
    const QV4::Compiler::JSUnitGenerator *self,
    char *f,
    QV4::Compiler::Context *irFunction) {
  self->writeFunction(f, irFunction);
}

//  void QV4::Compiler::JSUnitGenerator::writeClass(char *f, const Class &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler15JSUnitGenerator10writeClassEPcRKNS0_5ClassE(
    QV4::Compiler::JSUnitGenerator *self,
    char *f,
    const QV4::Compiler::Class *c) {
  self->writeClass(f, *c);
}

//  void QV4::Compiler::JSUnitGenerator::writeTemplateObject(char *f, const
//      TemplateObject &o)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler15JSUnitGenerator19writeTemplateObjectEPcRKNS0_14TemplateObjectE(
    QV4::Compiler::JSUnitGenerator *self,
    char *f,
    const QV4::Compiler::TemplateObject *o) {
  self->writeTemplateObject(f, *o);
}

//  void QV4::Compiler::JSUnitGenerator::writeBlock(char *f, Context
//      *irBlock) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV48Compiler15JSUnitGenerator10writeBlockEPcPNS0_7ContextE(
    const QV4::Compiler::JSUnitGenerator *self,
    char *f,
    QV4::Compiler::Context *irBlock) {
  self->writeBlock(f, irBlock);
}

//  CompiledData::Unit
//      QV4::Compiler::JSUnitGenerator::generateHeader(GeneratorOption
//      option, quint32_le *functionOffsets, uint *jsClassDataOffset)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Unit *ritual_ZN3QV48Compiler15JSUnitGenerator14generateHeaderENS1_15GeneratorOptionEP15QSpecialIntegerI24QLittleEndianStorageTypeIjEEPj(
    QV4::Compiler::JSUnitGenerator *self,
    QV4::Compiler::JSUnitGenerator::GeneratorOption option,
    quint32_le *functionOffsets,
    uint *jsClassDataOffset) {
  return new QV4::CompiledData::Unit(
      self->generateHeader(
          option,
          functionOffsets,
          jsClassDataOffset));
}

//  QV4::Compiler::JSUnitGenerator::~JSUnitGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler15JSUnitGeneratorD1Ev(
    QV4::Compiler::JSUnitGenerator *self) {
  delete self;
}
