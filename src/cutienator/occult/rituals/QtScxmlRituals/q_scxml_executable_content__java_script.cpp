//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::JavaScript::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent10JavaScript4kindEv() {
  return QScxmlExecutableContent::JavaScript::kind();
}

//  int QScxmlExecutableContent::JavaScript::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent10JavaScript4sizeEv(
    const QScxmlExecutableContent::JavaScript *self) {
  return self->size();
}

//  QScxmlExecutableContent::JavaScript::~JavaScript()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent10JavaScriptD1Ev(
    QScxmlExecutableContent::JavaScript *self) {
  delete self;
}
