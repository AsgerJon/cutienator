//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::Initialize::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent10Initialize4kindEv() {
  return QScxmlExecutableContent::Initialize::kind();
}

//  int QScxmlExecutableContent::Initialize::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent10Initialize4sizeEv(
    const QScxmlExecutableContent::Initialize *self) {
  return self->size();
}

//  QScxmlExecutableContent::Initialize::~Initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent10InitializeD1Ev(
    QScxmlExecutableContent::Initialize *self) {
  delete self;
}
