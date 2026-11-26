//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJSRegisterContent QQmlJSCompilePass::State::accumulatorIn() const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK17QQmlJSCompilePass5State13accumulatorInEv(
    const QQmlJSCompilePass::State *self) {
  return new QQmlJSRegisterContent(self->accumulatorIn());
}

//  QQmlJSRegisterContent QQmlJSCompilePass::State::accumulatorOut() const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK17QQmlJSCompilePass5State14accumulatorOutEv(
    const QQmlJSCompilePass::State *self) {
  return new QQmlJSRegisterContent(self->accumulatorOut());
}

//  void QQmlJSCompilePass::State::setRegister(int registerIndex,
//      QQmlJSRegisterContent content)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State11setRegisterEi21QQmlJSRegisterContent(
    QQmlJSCompilePass::State *self,
    int registerIndex,
    const QQmlJSRegisterContent *content) {
  self->setRegister(registerIndex, *content);
}

//  void QQmlJSCompilePass::State::clearChangedRegister()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State20clearChangedRegisterEv(
    QQmlJSCompilePass::State *self) {
  self->clearChangedRegister();
}

//  int QQmlJSCompilePass::State::changedRegisterIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlJSCompilePass5State20changedRegisterIndexEv(
    const QQmlJSCompilePass::State *self) {
  return self->changedRegisterIndex();
}

//  QQmlJSRegisterContent QQmlJSCompilePass::State::changedRegister() const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK17QQmlJSCompilePass5State15changedRegisterEv(
    const QQmlJSCompilePass::State *self) {
  return new QQmlJSRegisterContent(self->changedRegister());
}

//  void QQmlJSCompilePass::State::addReadRegister(int registerIndex,
//      QQmlJSRegisterContent reg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State15addReadRegisterEi21QQmlJSRegisterContent(
    QQmlJSCompilePass::State *self,
    int registerIndex,
    const QQmlJSRegisterContent *reg) {
  self->addReadRegister(registerIndex, *reg);
}

//  void QQmlJSCompilePass::State::addReadAccumulator(QQmlJSRegisterContent
//      reg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State18addReadAccumulatorE21QQmlJSRegisterContent(
    QQmlJSCompilePass::State *self,
    const QQmlJSRegisterContent *reg) {
  self->addReadAccumulator(*reg);
}

//  VirtualRegisters QQmlJSCompilePass::State::takeReadRegisters() const
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::VirtualRegisters *ritual_ZNK17QQmlJSCompilePass5State17takeReadRegistersEv(
    const QQmlJSCompilePass::State *self) {
  return new QQmlJSCompilePass::VirtualRegisters(self->takeReadRegisters());
}

//  void QQmlJSCompilePass::State::setReadRegisters(VirtualRegisters
//      readReagisters)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State16setReadRegistersE8QFlatMapIiNS_15VirtualRegisterESt4lessIiE5QListIiES5_IS2_EE(
    QQmlJSCompilePass::State *self,
    const QQmlJSCompilePass::VirtualRegisters *readReagisters) {
  self->setReadRegisters(*readReagisters);
}

//  QQmlJSRegisterContent QQmlJSCompilePass::State::readRegister(int
//      registerIndex) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK17QQmlJSCompilePass5State12readRegisterEi(
    const QQmlJSCompilePass::State *self,
    int registerIndex) {
  return new QQmlJSRegisterContent(self->readRegister(registerIndex));
}

//  bool QQmlJSCompilePass::State::canMoveReadRegister(int registerIndex)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass5State19canMoveReadRegisterEi(
    const QQmlJSCompilePass::State *self,
    int registerIndex) {
  return self->canMoveReadRegister(registerIndex);
}

//  bool QQmlJSCompilePass::State::isRegisterAffectedBySideEffects(int
//      registerIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass5State31isRegisterAffectedBySideEffectsEi(
    const QQmlJSCompilePass::State *self,
    int registerIndex) {
  return self->isRegisterAffectedBySideEffects(registerIndex);
}

//  QQmlJSRegisterContent QQmlJSCompilePass::State::readAccumulator() const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK17QQmlJSCompilePass5State15readAccumulatorEv(
    const QQmlJSCompilePass::State *self) {
  return new QQmlJSRegisterContent(self->readAccumulator());
}

//  bool QQmlJSCompilePass::State::readsRegister(int registerIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass5State13readsRegisterEi(
    const QQmlJSCompilePass::State *self,
    int registerIndex) {
  return self->readsRegister(registerIndex);
}

//  bool QQmlJSCompilePass::State::hasInternalSideEffects() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass5State22hasInternalSideEffectsEv(
    const QQmlJSCompilePass::State *self) {
  return self->hasInternalSideEffects();
}

//  bool QQmlJSCompilePass::State::hasExternalSideEffects() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass5State22hasExternalSideEffectsEv(
    const QQmlJSCompilePass::State *self) {
  return self->hasExternalSideEffects();
}

//  void QQmlJSCompilePass::State::resetSideEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State16resetSideEffectsEv(
    QQmlJSCompilePass::State *self) {
  self->resetSideEffects();
}

//  void QQmlJSCompilePass::State::applyExternalSideEffects(bool
//      hasExternalSideEffects)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State24applyExternalSideEffectsEb(
    QQmlJSCompilePass::State *self,
    bool hasExternalSideEffects) {
  self->applyExternalSideEffects(hasExternalSideEffects);
}

//  void QQmlJSCompilePass::State::setHasInternalSideEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State25setHasInternalSideEffectsEv(
    QQmlJSCompilePass::State *self) {
  self->setHasInternalSideEffects();
}

//  void QQmlJSCompilePass::State::setHasExternalSideEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State25setHasExternalSideEffectsEv(
    QQmlJSCompilePass::State *self) {
  self->setHasExternalSideEffects();
}

//  bool QQmlJSCompilePass::State::isRename() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass5State8isRenameEv(
    const QQmlJSCompilePass::State *self) {
  return self->isRename();
}

//  void QQmlJSCompilePass::State::setIsRename(bool isRename)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State11setIsRenameEb(
    QQmlJSCompilePass::State *self,
    bool isRename) {
  self->setIsRename(isRename);
}

//  bool QQmlJSCompilePass::State::isShadowable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass5State12isShadowableEv(
    const QQmlJSCompilePass::State *self) {
  return self->isShadowable();
}

//  void QQmlJSCompilePass::State::setIsShadowable(bool isShadowable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State15setIsShadowableEb(
    QQmlJSCompilePass::State *self,
    bool isShadowable) {
  self->setIsShadowable(isShadowable);
}

//  int QQmlJSCompilePass::State::renameSourceRegisterIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlJSCompilePass5State25renameSourceRegisterIndexEv(
    const QQmlJSCompilePass::State *self) {
  return self->renameSourceRegisterIndex();
}

//  void QQmlJSCompilePass::State::applyAnnotation(const
//      InstructionAnnotation &annotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5State15applyAnnotationERKNS_21InstructionAnnotationE(
    QQmlJSCompilePass::State *self,
    const QQmlJSCompilePass::InstructionAnnotation *annotation) {
  self->applyAnnotation(*annotation);
}

//  QQmlJSCompilePass::State::~State()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass5StateD1Ev(QQmlJSCompilePass::State *self) {
  delete self;
}

//  a QQmlJSCompilePass::VirtualRegisters a ritual of
//      QQmlJSCompilePass::State gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSCompilePass_State__QQmlJSCompilePass_VirtualRegisters(
    QQmlJSCompilePass::VirtualRegisters *self) {
  delete self;
}
