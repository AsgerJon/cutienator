//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Moth::BytecodeGenerator::Label::Label()
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::Label *ritual_ZN3QV44Moth17BytecodeGenerator5LabelC1Ev() {
  return new QV4::Moth::BytecodeGenerator::Label();
}

//  QV4::Moth::BytecodeGenerator::Label::Label(BytecodeGenerator *generator,
//      LinkMode mode)
extern "C" Q_DECL_EXPORT
QV4::Moth::BytecodeGenerator::Label *ritual_ZN3QV44Moth17BytecodeGenerator5LabelC1EPS1_NS2_8LinkModeE(
    QV4::Moth::BytecodeGenerator *generator,
    QV4::Moth::BytecodeGenerator::Label::LinkMode mode) {
  return new QV4::Moth::BytecodeGenerator::Label(generator, mode);
}

//  void QV4::Moth::BytecodeGenerator::Label::link() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV44Moth17BytecodeGenerator5Label4linkEv(
    const QV4::Moth::BytecodeGenerator::Label *self) {
  self->link();
}

//  bool QV4::Moth::BytecodeGenerator::Label::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Moth17BytecodeGenerator5Label7isValidEv(
    const QV4::Moth::BytecodeGenerator::Label *self) {
  return self->isValid();
}

//  QV4::Moth::BytecodeGenerator::Label::~Label()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth17BytecodeGenerator5LabelD1Ev(
    QV4::Moth::BytecodeGenerator::Label *self) {
  delete self;
}
