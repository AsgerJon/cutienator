//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const InstructionSequences *QScxmlExecutableContent::If::blocks() const
extern "C" Q_DECL_EXPORT
const QScxmlExecutableContent::InstructionSequences *ritual_ZNK23QScxmlExecutableContent2If6blocksEv(
    const QScxmlExecutableContent::If *self) {
  return self->blocks();
}

//  InstructionType QScxmlExecutableContent::If::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent2If4kindEv() {
  return QScxmlExecutableContent::If::kind();
}

//  int QScxmlExecutableContent::If::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent2If4sizeEv(
    const QScxmlExecutableContent::If *self) {
  return self->size();
}

//  QScxmlExecutableContent::If::~If()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent2IfD1Ev(
    QScxmlExecutableContent::If *self) {
  delete self;
}
