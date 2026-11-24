//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::Raise::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent5Raise4kindEv() {
  return QScxmlExecutableContent::Raise::kind();
}

//  int QScxmlExecutableContent::Raise::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent5Raise4sizeEv(
    const QScxmlExecutableContent::Raise *self) {
  return self->size();
}

//  QScxmlExecutableContent::Raise::~Raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent5RaiseD1Ev(
    QScxmlExecutableContent::Raise *self) {
  delete self;
}
