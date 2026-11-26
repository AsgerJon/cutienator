//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Moth::BytecodeGenerator::Jump::Jump(BytecodeGenerator *generator,
//      int instruction)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::Jump *ritual_ZN3QV44Moth17BytecodeGenerator4JumpC1EPS1_i(
    QV4::Moth::BytecodeGenerator *generator,
    int instruction) {
  return new QV4::Moth::BytecodeGenerator::Jump(generator, instruction);
}

//  QV4::Moth::BytecodeGenerator::Jump::~Jump()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator4JumpD1Ev(
    QV4::Moth::BytecodeGenerator::Jump *self) {
  delete self;
}

//  QV4::Moth::BytecodeGenerator::Jump::Jump(Jump &&j)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::Jump *ritual_ZN3QV44Moth17BytecodeGenerator4JumpC1EOS2_(
    QV4::Moth::BytecodeGenerator::Jump *j) {
  return new QV4::Moth::BytecodeGenerator::Jump(std::move(*j));
}

//  void QV4::Moth::BytecodeGenerator::Jump::link()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator4Jump4linkEv(
    QV4::Moth::BytecodeGenerator::Jump *self) {
  self->link();
}

//  void QV4::Moth::BytecodeGenerator::Jump::link(Label l)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator4Jump4linkENS1_5LabelE(
    QV4::Moth::BytecodeGenerator::Jump *self,
    const QV4::Moth::BytecodeGenerator::Label *l) {
  self->link(*l);
}
