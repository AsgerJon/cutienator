//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QString QmlIR::Object::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QmlIR6Object2trEPKcS2_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QmlIR::Object::tr(sourceText, disambiguation, n));
}

//  const Property *QmlIR::Object::firstProperty() const
extern "C" Q_DECL_EXPORT
const QmlIR::Property *ritual_ZNK5QmlIR6Object13firstPropertyEv(
    const QmlIR::Object *self) {
  return self->firstProperty();
}

//  int QmlIR::Object::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object13propertyCountEv(const QmlIR::Object *self) {
  return self->propertyCount();
}

//  Alias *QmlIR::Object::firstAlias() const
extern "C" Q_DECL_EXPORT
QmlIR::Alias *ritual_ZNK5QmlIR6Object10firstAliasEv(
    const QmlIR::Object *self) {
  return self->firstAlias();
}

//  int QmlIR::Object::aliasCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object10aliasCountEv(const QmlIR::Object *self) {
  return self->aliasCount();
}

//  const Enum *QmlIR::Object::firstEnum() const
extern "C" Q_DECL_EXPORT
const QmlIR::Enum *ritual_ZNK5QmlIR6Object9firstEnumEv(
    const QmlIR::Object *self) {
  return self->firstEnum();
}

//  int QmlIR::Object::enumCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object9enumCountEv(const QmlIR::Object *self) {
  return self->enumCount();
}

//  const Signal *QmlIR::Object::firstSignal() const
extern "C" Q_DECL_EXPORT
const QmlIR::Signal *ritual_ZNK5QmlIR6Object11firstSignalEv(
    const QmlIR::Object *self) {
  return self->firstSignal();
}

//  int QmlIR::Object::signalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object11signalCountEv(const QmlIR::Object *self) {
  return self->signalCount();
}

//  Binding *QmlIR::Object::firstBinding() const
extern "C" Q_DECL_EXPORT
QmlIR::Binding *ritual_ZNK5QmlIR6Object12firstBindingEv(
    const QmlIR::Object *self) {
  return self->firstBinding();
}

//  int QmlIR::Object::bindingCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object12bindingCountEv(const QmlIR::Object *self) {
  return self->bindingCount();
}

//  const Function *QmlIR::Object::firstFunction() const
extern "C" Q_DECL_EXPORT
const QmlIR::Function *ritual_ZNK5QmlIR6Object13firstFunctionEv(
    const QmlIR::Object *self) {
  return self->firstFunction();
}

//  int QmlIR::Object::functionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object13functionCountEv(const QmlIR::Object *self) {
  return self->functionCount();
}

//  const InlineComponent *QmlIR::Object::inlineComponent() const
extern "C" Q_DECL_EXPORT
const QmlIR::InlineComponent *ritual_ZNK5QmlIR6Object15inlineComponentEv(
    const QmlIR::Object *self) {
  return self->inlineComponent();
}

//  int QmlIR::Object::inlineComponentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object20inlineComponentCountEv(
    const QmlIR::Object *self) {
  return self->inlineComponentCount();
}

//  const RequiredPropertyExtraData
//      *QmlIR::Object::requiredPropertyExtraData() const
extern "C" Q_DECL_EXPORT
const QmlIR::RequiredPropertyExtraData *ritual_ZNK5QmlIR6Object25requiredPropertyExtraDataEv(
    const QmlIR::Object *self) {
  return self->requiredPropertyExtraData();
}

//  int QmlIR::Object::requiredPropertyExtraDataCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object30requiredPropertyExtraDataCountEv(
    const QmlIR::Object *self) {
  return self->requiredPropertyExtraDataCount();
}

//  void QmlIR::Object::simplifyRequiredProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6Object26simplifyRequiredPropertiesEv(
    QmlIR::Object *self) {
  self->simplifyRequiredProperties();
}

//  void QmlIR::Object::sortAliasDependencies(const Document *doc,
//      QList<QQmlJS::DiagnosticMessage> *errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6Object21sortAliasDependenciesEPKNS_8DocumentEP5QListIN6QQmlJS17DiagnosticMessageEE(
    QmlIR::Object *self,
    const QmlIR::Document *doc,
    QList<QQmlJS::DiagnosticMessage> *errors) {
  self->sortAliasDependencies(doc, errors);
}

//  void QmlIR::Object::init(QQmlJS::MemoryPool *pool, int typeNameIndex, int
//      idIndex, const QV4::CompiledData::Location &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6Object4initEPN6QQmlJS10MemoryPoolEiiRKN3QV412CompiledData8LocationE(
    QmlIR::Object *self,
    QQmlJS::MemoryPool *pool,
    int typeNameIndex,
    int idIndex,
    const QV4::CompiledData::Location *location) {
  self->init(pool, typeNameIndex, idIndex, *location);
}

//  QString QmlIR::Object::appendEnum(Enum *enumeration)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QmlIR6Object10appendEnumEPNS_4EnumE(
    QmlIR::Object *self,
    QmlIR::Enum *enumeration) {
  return new QString(self->appendEnum(enumeration));
}

//  QString QmlIR::Object::appendSignal(Signal *signal)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QmlIR6Object12appendSignalEPNS_6SignalE(
    QmlIR::Object *self,
    QmlIR::Signal *signal) {
  return new QString(self->appendSignal(signal));
}

//  QString QmlIR::Object::appendProperty(Property *prop, const QString
//      &propertyName, bool isDefaultProperty, const QQmlJS::SourceLocation
//      &defaultToken, QQmlJS::SourceLocation *errorLocation)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QmlIR6Object14appendPropertyEPNS_8PropertyERK7QStringbRKN6QQmlJS14SourceLocationEPS7_(
    QmlIR::Object *self,
    QmlIR::Property *prop,
    const QString *propertyName,
    bool isDefaultProperty,
    const QQmlJS::SourceLocation *defaultToken,
    QQmlJS::SourceLocation *errorLocation) {
  return new QString(
      self->appendProperty(
          prop,
          *propertyName,
          isDefaultProperty,
          *defaultToken,
          errorLocation));
}

//  QString QmlIR::Object::appendAlias(Alias *prop, const QString &aliasName,
//      bool isDefaultProperty, const QQmlJS::SourceLocation &defaultToken,
//      QQmlJS::SourceLocation *errorLocation)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QmlIR6Object11appendAliasEPNS_5AliasERK7QStringbRKN6QQmlJS14SourceLocationEPS7_(
    QmlIR::Object *self,
    QmlIR::Alias *prop,
    const QString *aliasName,
    bool isDefaultProperty,
    const QQmlJS::SourceLocation *defaultToken,
    QQmlJS::SourceLocation *errorLocation) {
  return new QString(
      self->appendAlias(
          prop,
          *aliasName,
          isDefaultProperty,
          *defaultToken,
          errorLocation));
}

//  void QmlIR::Object::setFirstAlias(Alias *alias)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6Object13setFirstAliasEPNS_5AliasE(
    QmlIR::Object *self,
    QmlIR::Alias *alias) {
  self->setFirstAlias(alias);
}

//  void QmlIR::Object::appendFunction(QmlIR::Function *f)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6Object14appendFunctionEPNS_8FunctionE(
    QmlIR::Object *self,
    QmlIR::Function *f) {
  self->appendFunction(f);
}

//  void QmlIR::Object::appendInlineComponent(InlineComponent *ic)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6Object21appendInlineComponentEPNS_15InlineComponentE(
    QmlIR::Object *self,
    QmlIR::InlineComponent *ic) {
  self->appendInlineComponent(ic);
}

//  void
//      QmlIR::Object::appendRequiredPropertyExtraData(RequiredPropertyExtraD
//      ata *extraData)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6Object31appendRequiredPropertyExtraDataEPNS_25RequiredPropertyExtraDataE(
    QmlIR::Object *self,
    QmlIR::RequiredPropertyExtraData *extraData) {
  self->appendRequiredPropertyExtraData(extraData);
}

//  QString QmlIR::Object::appendBinding(Binding *b, bool isListBinding)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QmlIR6Object13appendBindingEPNS_7BindingEb(
    QmlIR::Object *self,
    QmlIR::Binding *b,
    bool isListBinding) {
  return new QString(self->appendBinding(b, isListBinding));
}

//  Binding *QmlIR::Object::findBinding(quint32 nameIndex) const
extern "C" Q_DECL_EXPORT
QmlIR::Binding *ritual_ZNK5QmlIR6Object11findBindingEj(
    const QmlIR::Object *self,
    quint32 nameIndex) {
  return self->findBinding(nameIndex);
}

//  Binding *QmlIR::Object::unlinkBinding(Binding *before, Binding *binding)
extern "C" Q_DECL_EXPORT
QmlIR::Binding *ritual_ZN5QmlIR6Object13unlinkBindingEPNS_7BindingES2_(
    QmlIR::Object *self,
    QmlIR::Binding *before,
    QmlIR::Binding *binding) {
  return self->unlinkBinding(before, binding);
}

//  QString QmlIR::Object::bindingAsString(Document *doc, int scriptIndex)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QmlIR6Object15bindingAsStringEPNS_8DocumentEi(
    const QmlIR::Object *self,
    QmlIR::Document *doc,
    int scriptIndex) {
  return new QString(self->bindingAsString(doc, scriptIndex));
}

//  int QmlIR::Object::namedObjectsInComponentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Object28namedObjectsInComponentCountEv(
    const QmlIR::Object *self) {
  return self->namedObjectsInComponentCount();
}

//  const quint32 *QmlIR::Object::namedObjectsInComponentTable() const
extern "C" Q_DECL_EXPORT
const quint32 *ritual_ZNK5QmlIR6Object28namedObjectsInComponentTableEv(
    const QmlIR::Object *self) {
  return self->namedObjectsInComponentTable();
}

//  bool QmlIR::Object::hasFlag(QV4::CompiledData::Object::Flag flag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QmlIR6Object7hasFlagEN3QV412CompiledData6Object4FlagE(
    const QmlIR::Object *self,
    QV4::CompiledData::Object::Flag flag) {
  return self->hasFlag(flag);
}

//  qint32 QmlIR::Object::objectId() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK5QmlIR6Object8objectIdEv(const QmlIR::Object *self) {
  return self->objectId();
}

//  bool QmlIR::Object::hasAliasAsDefaultProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QmlIR6Object25hasAliasAsDefaultPropertyEv(
    const QmlIR::Object *self) {
  return self->hasAliasAsDefaultProperty();
}

//  QmlIR::Object::~Object()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6ObjectD1Ev(QmlIR::Object *self) {
  delete self;
}
