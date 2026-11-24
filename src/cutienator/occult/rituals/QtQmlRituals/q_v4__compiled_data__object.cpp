//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Flags QV4::CompiledData::Object::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object5flagsEv(
    const QV4::CompiledData::Object *self) {
  return static_cast<int>(self->flags().toInt());
}

//  bool QV4::CompiledData::Object::hasFlag(Flag flag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData6Object7hasFlagENS1_4FlagE(
    const QV4::CompiledData::Object *self,
    QV4::CompiledData::Object::Flag flag) {
  return self->hasFlag(flag);
}

//  void QV4::CompiledData::Object::setFlag(Flag flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6Object7setFlagENS1_4FlagE(
    QV4::CompiledData::Object *self,
    QV4::CompiledData::Object::Flag flag) {
  self->setFlag(flag);
}

//  void QV4::CompiledData::Object::setFlags(Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6Object8setFlagsE6QFlagsINS1_4FlagEE(
    QV4::CompiledData::Object *self,
    int flags) {
  self->setFlags(QFlags<QV4::CompiledData::Object::Flag>::fromInt(flags));
}

//  bool QV4::CompiledData::Object::hasAliasAsDefaultProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData6Object25hasAliasAsDefaultPropertyEv(
    const QV4::CompiledData::Object *self) {
  return self->hasAliasAsDefaultProperty();
}

//  void QV4::CompiledData::Object::setHasAliasAsDefaultProperty(bool
//      defaultAlias)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6Object28setHasAliasAsDefaultPropertyEb(
    QV4::CompiledData::Object *self,
    bool defaultAlias) {
  self->setHasAliasAsDefaultProperty(defaultAlias);
}

//  qint32 QV4::CompiledData::Object::objectId() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK3QV412CompiledData6Object8objectIdEv(
    const QV4::CompiledData::Object *self) {
  return self->objectId();
}

//  void QV4::CompiledData::Object::setObjectId(qint32 id)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6Object11setObjectIdEi(
    QV4::CompiledData::Object *self,
    qint32 id) {
  self->setObjectId(id);
}

//  int QV4::CompiledData::Object::calculateSizeExcludingSignalsAndEnums(int
//      nFunctions, int nProperties, int nAliases, int nEnums, int nSignals,
//      int nBindings, int nNamedObjectsInComponent, int nInlineComponents,
//      int nRequiredPropertyExtraData)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData6Object37calculateSizeExcludingSignalsAndEnumsEiiiiiiiii(
    int nFunctions,
    int nProperties,
    int nAliases,
    int nEnums,
    int nSignals,
    int nBindings,
    int nNamedObjectsInComponent,
    int nInlineComponents,
    int nRequiredPropertyExtraData) {
  return QV4::CompiledData::Object::calculateSizeExcludingSignalsAndEnums(
      nFunctions,
      nProperties,
      nAliases,
      nEnums,
      nSignals,
      nBindings,
      nNamedObjectsInComponent,
      nInlineComponents,
      nRequiredPropertyExtraData);
}

//  const Property *QV4::CompiledData::Object::propertyTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Property *ritual_ZNK3QV412CompiledData6Object13propertyTableEv(
    const QV4::CompiledData::Object *self) {
  return self->propertyTable();
}

//  const Alias *QV4::CompiledData::Object::aliasTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Alias *ritual_ZNK3QV412CompiledData6Object10aliasTableEv(
    const QV4::CompiledData::Object *self) {
  return self->aliasTable();
}

//  const Binding *QV4::CompiledData::Object::bindingTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Binding *ritual_ZNK3QV412CompiledData6Object12bindingTableEv(
    const QV4::CompiledData::Object *self) {
  return self->bindingTable();
}

//  const Enum *QV4::CompiledData::Object::enumAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Enum *ritual_ZNK3QV412CompiledData6Object6enumAtEi(
    const QV4::CompiledData::Object *self,
    int idx) {
  return self->enumAt(idx);
}

//  const Signal *QV4::CompiledData::Object::signalAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Signal *ritual_ZNK3QV412CompiledData6Object8signalAtEi(
    const QV4::CompiledData::Object *self,
    int idx) {
  return self->signalAt(idx);
}

//  const InlineComponent *QV4::CompiledData::Object::inlineComponentAt(int
//      idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::InlineComponent *ritual_ZNK3QV412CompiledData6Object17inlineComponentAtEi(
    const QV4::CompiledData::Object *self,
    int idx) {
  return self->inlineComponentAt(idx);
}

//  const InlineComponent *QV4::CompiledData::Object::inlineComponentTable()
//      const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::InlineComponent *ritual_ZNK3QV412CompiledData6Object20inlineComponentTableEv(
    const QV4::CompiledData::Object *self) {
  return self->inlineComponentTable();
}

//  const RequiredPropertyExtraData
//      *QV4::CompiledData::Object::requiredPropertyExtraDataAt(int idx)
//      const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::RequiredPropertyExtraData *ritual_ZNK3QV412CompiledData6Object27requiredPropertyExtraDataAtEi(
    const QV4::CompiledData::Object *self,
    int idx) {
  return self->requiredPropertyExtraDataAt(idx);
}

//  const RequiredPropertyExtraData
//      *QV4::CompiledData::Object::requiredPropertyExtraDataTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::RequiredPropertyExtraData *ritual_ZNK3QV412CompiledData6Object30requiredPropertyExtraDataTableEv(
    const QV4::CompiledData::Object *self) {
  return self->requiredPropertyExtraDataTable();
}

//  int QV4::CompiledData::Object::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object13propertyCountEv(
    const QV4::CompiledData::Object *self) {
  return self->propertyCount();
}

//  int QV4::CompiledData::Object::aliasCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object10aliasCountEv(
    const QV4::CompiledData::Object *self) {
  return self->aliasCount();
}

//  int QV4::CompiledData::Object::enumCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object9enumCountEv(
    const QV4::CompiledData::Object *self) {
  return self->enumCount();
}

//  int QV4::CompiledData::Object::signalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object11signalCountEv(
    const QV4::CompiledData::Object *self) {
  return self->signalCount();
}

//  int QV4::CompiledData::Object::functionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object13functionCountEv(
    const QV4::CompiledData::Object *self) {
  return self->functionCount();
}

//  int QV4::CompiledData::Object::inlineComponentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object20inlineComponentCountEv(
    const QV4::CompiledData::Object *self) {
  return self->inlineComponentCount();
}

//  const Binding *QV4::CompiledData::Object::bindingsBegin() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Binding *ritual_ZNK3QV412CompiledData6Object13bindingsBeginEv(
    const QV4::CompiledData::Object *self) {
  return self->bindingsBegin();
}

//  const Binding *QV4::CompiledData::Object::bindingsEnd() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Binding *ritual_ZNK3QV412CompiledData6Object11bindingsEndEv(
    const QV4::CompiledData::Object *self) {
  return self->bindingsEnd();
}

//  int QV4::CompiledData::Object::bindingCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object12bindingCountEv(
    const QV4::CompiledData::Object *self) {
  return self->bindingCount();
}

//  const Property *QV4::CompiledData::Object::propertiesBegin() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Property *ritual_ZNK3QV412CompiledData6Object15propertiesBeginEv(
    const QV4::CompiledData::Object *self) {
  return self->propertiesBegin();
}

//  const Property *QV4::CompiledData::Object::propertiesEnd() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Property *ritual_ZNK3QV412CompiledData6Object13propertiesEndEv(
    const QV4::CompiledData::Object *self) {
  return self->propertiesEnd();
}

//  const Alias *QV4::CompiledData::Object::aliasesBegin() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Alias *ritual_ZNK3QV412CompiledData6Object12aliasesBeginEv(
    const QV4::CompiledData::Object *self) {
  return self->aliasesBegin();
}

//  const Alias *QV4::CompiledData::Object::aliasesEnd() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Alias *ritual_ZNK3QV412CompiledData6Object10aliasesEndEv(
    const QV4::CompiledData::Object *self) {
  return self->aliasesEnd();
}

//  int QV4::CompiledData::Object::namedObjectsInComponentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Object28namedObjectsInComponentCountEv(
    const QV4::CompiledData::Object *self) {
  return self->namedObjectsInComponentCount();
}

//  QV4::CompiledData::Object::~Object()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6ObjectD1Ev(
    QV4::CompiledData::Object *self) {
  delete self;
}
