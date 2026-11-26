//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Moth::BytecodeGenerator::ExceptionHandler::ExceptionHandler()
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZN3QV44Moth17BytecodeGenerator16ExceptionHandlerC1Ev() {
  return new QV4::Moth::BytecodeGenerator::ExceptionHandler();
}

//  QV4::Moth::BytecodeGenerator::ExceptionHandler::ExceptionHandler(Bytecode
//      Generator *generator)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZN3QV44Moth17BytecodeGenerator16ExceptionHandlerC1EPS1_(
    QV4::Moth::BytecodeGenerator *generator) {
  return new QV4::Moth::BytecodeGenerator::ExceptionHandler(generator);
}

//  QV4::Moth::BytecodeGenerator::ExceptionHandler::~ExceptionHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator16ExceptionHandlerD1Ev(
    QV4::Moth::BytecodeGenerator::ExceptionHandler *self) {
  delete self;
}

//  QV4::Moth::BytecodeGenerator::ExceptionHandler::ExceptionHandler(const
//      ExceptionHandler &a0)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZN3QV44Moth17BytecodeGenerator16ExceptionHandlerC1ERKS2_(
    const QV4::Moth::BytecodeGenerator::ExceptionHandler *a0) {
  return new QV4::Moth::BytecodeGenerator::ExceptionHandler(*a0);
}

//  QV4::Moth::BytecodeGenerator::ExceptionHandler::ExceptionHandler(Exceptio
//      nHandler &&a0)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZN3QV44Moth17BytecodeGenerator16ExceptionHandlerC1EOS2_(
    QV4::Moth::BytecodeGenerator::ExceptionHandler *a0) {
  return new QV4::Moth::BytecodeGenerator::ExceptionHandler(std::move(*a0));
}

//  ExceptionHandler
//      &QV4::Moth::BytecodeGenerator::ExceptionHandler::operator=(const
//      ExceptionHandler &a0)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZN3QV44Moth17BytecodeGenerator16ExceptionHandleraSERKS2_(
    QV4::Moth::BytecodeGenerator::ExceptionHandler *self,
    const QV4::Moth::BytecodeGenerator::ExceptionHandler *a0) {
  return &(self->operator=(*a0));
}

//  ExceptionHandler &QV4::Moth::BytecodeGenerator::ExceptionHandler::operato
//      r=(ExceptionHandler &&a0)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::ExceptionHandler *ritual_ZN3QV44Moth17BytecodeGenerator16ExceptionHandleraSEOS2_(
    QV4::Moth::BytecodeGenerator::ExceptionHandler *self,
    QV4::Moth::BytecodeGenerator::ExceptionHandler *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  bool QV4::Moth::BytecodeGenerator::ExceptionHandler::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Moth17BytecodeGenerator16ExceptionHandler7isValidEv(
    const QV4::Moth::BytecodeGenerator::ExceptionHandler *self) {
  return self->isValid();
}
