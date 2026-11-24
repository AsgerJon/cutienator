//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::Foreach::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent7Foreach4kindEv() {
  return QScxmlExecutableContent::Foreach::kind();
}

//  int QScxmlExecutableContent::Foreach::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent7Foreach4sizeEv(
    const QScxmlExecutableContent::Foreach *self) {
  return self->size();
}

//  QScxmlExecutableContent::Foreach::~Foreach()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent7ForeachD1Ev(
    QScxmlExecutableContent::Foreach *self) {
  delete self;
}
