//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::InstructionSequence::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent19InstructionSequence4kindEv() {
  return QScxmlExecutableContent::InstructionSequence::kind();
}

//  int QScxmlExecutableContent::InstructionSequence::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent19InstructionSequence4sizeEv(
    const QScxmlExecutableContent::InstructionSequence *self) {
  return self->size();
}

//  QScxmlExecutableContent::InstructionSequence::~InstructionSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent19InstructionSequenceD1Ev(
    QScxmlExecutableContent::InstructionSequence *self) {
  delete self;
}
