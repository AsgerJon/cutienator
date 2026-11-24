//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::InstructionSequences::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent20InstructionSequences4kindEv() {
  return QScxmlExecutableContent::InstructionSequences::kind();
}

//  const InstructionSequence
//      *QScxmlExecutableContent::InstructionSequences::sequences() const
extern "C" Q_DECL_EXPORT
const QScxmlExecutableContent::InstructionSequence *ritual_ZNK23QScxmlExecutableContent20InstructionSequences9sequencesEv(
    const QScxmlExecutableContent::InstructionSequences *self) {
  return self->sequences();
}

//  int QScxmlExecutableContent::InstructionSequences::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent20InstructionSequences4sizeEv(
    const QScxmlExecutableContent::InstructionSequences *self) {
  return self->size();
}

//  QScxmlExecutableContent::InstructionSequences::~InstructionSequences()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent20InstructionSequencesD1Ev(
    QScxmlExecutableContent::InstructionSequences *self) {
  delete self;
}
