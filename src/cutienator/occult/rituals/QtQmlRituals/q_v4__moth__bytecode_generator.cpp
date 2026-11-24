//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Moth::BytecodeGenerator::BytecodeGenerator(int line, bool debug,
//      bool storeSourceLocation)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator *ritual_ZN3QV44Moth17BytecodeGeneratorC1Eibb(
    int line,
    bool debug,
    bool storeSourceLocation) {
  return new QV4::Moth::BytecodeGenerator(line, debug, storeSourceLocation);
}

//  Label QV4::Moth::BytecodeGenerator::label()
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::Label *ritual_ZN3QV44Moth17BytecodeGenerator5labelEv(
    QV4::Moth::BytecodeGenerator *self) {
  return new QV4::Moth::BytecodeGenerator::Label(self->label());
}

//  Label QV4::Moth::BytecodeGenerator::newLabel()
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::Label *ritual_ZN3QV44Moth17BytecodeGenerator8newLabelEv(
    QV4::Moth::BytecodeGenerator *self) {
  return new QV4::Moth::BytecodeGenerator::Label(self->newLabel());
}

//  ExceptionHandler QV4::Moth::BytecodeGenerator::newExceptionHandler()
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZN3QV44Moth17BytecodeGenerator19newExceptionHandlerEv(
    QV4::Moth::BytecodeGenerator *self) {
  return new QV4::Moth::BytecodeGenerator::ExceptionHandler(
      self->newExceptionHandler());
}

//  ExceptionHandler *QV4::Moth::BytecodeGenerator::exceptionHandler() const
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZNK3QV44Moth17BytecodeGenerator16exceptionHandlerEv(
    const QV4::Moth::BytecodeGenerator *self) {
  return self->exceptionHandler();
}

//  int QV4::Moth::BytecodeGenerator::registerCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Moth17BytecodeGenerator13registerCountEv(
    const QV4::Moth::BytecodeGenerator *self) {
  return self->registerCount();
}

//  int QV4::Moth::BytecodeGenerator::currentRegister() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Moth17BytecodeGenerator15currentRegisterEv(
    const QV4::Moth::BytecodeGenerator *self) {
  return self->currentRegister();
}

//  void QV4::Moth::BytecodeGenerator::clearLastInstruction()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator20clearLastInstructionEv(
    QV4::Moth::BytecodeGenerator *self) {
  self->clearLastInstruction();
}

//  void QV4::Moth::BytecodeGenerator::addLoopStart(const Label &start)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator12addLoopStartERKNS1_5LabelE(
    QV4::Moth::BytecodeGenerator *self,
    const QV4::Moth::BytecodeGenerator::Label *start) {
  self->addLoopStart(*start);
}

//  void QV4::Moth::BytecodeGenerator::setError(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator8setErrorEb(
    QV4::Moth::BytecodeGenerator *self,
    bool b) {
  self->setError(b);
}
