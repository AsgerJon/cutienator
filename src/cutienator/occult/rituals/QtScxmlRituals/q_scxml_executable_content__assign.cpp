//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::Assign::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent6Assign4kindEv() {
  return QScxmlExecutableContent::Assign::kind();
}

//  int QScxmlExecutableContent::Assign::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent6Assign4sizeEv(
    const QScxmlExecutableContent::Assign *self) {
  return self->size();
}

//  QScxmlExecutableContent::Assign::~Assign()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent6AssignD1Ev(
    QScxmlExecutableContent::Assign *self) {
  delete self;
}
