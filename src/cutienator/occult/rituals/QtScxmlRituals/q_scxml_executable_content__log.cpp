//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::Log::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent3Log4kindEv() {
  return QScxmlExecutableContent::Log::kind();
}

//  int QScxmlExecutableContent::Log::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent3Log4sizeEv(
    const QScxmlExecutableContent::Log *self) {
  return self->size();
}

//  QScxmlExecutableContent::Log::~Log()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent3LogD1Ev(
    QScxmlExecutableContent::Log *self) {
  delete self;
}
