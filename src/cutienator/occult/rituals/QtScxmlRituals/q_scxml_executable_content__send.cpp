//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  InstructionType QScxmlExecutableContent::Send::kind()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Instruction::InstructionType ritual_ZN23QScxmlExecutableContent4Send4kindEv() {
  return QScxmlExecutableContent::Send::kind();
}

//  int QScxmlExecutableContent::Send::paramsOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent4Send12paramsOffsetEv(
    const QScxmlExecutableContent::Send *self) {
  return self->paramsOffset();
}

//  int QScxmlExecutableContent::Send::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent4Send4sizeEv(
    const QScxmlExecutableContent::Send *self) {
  return self->size();
}

//  int QScxmlExecutableContent::Send::calculateExtraSize(int paramCount, int
//      nameCount)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QScxmlExecutableContent4Send18calculateExtraSizeEii(
    int paramCount,
    int nameCount) {
  return QScxmlExecutableContent::Send::calculateExtraSize(
      paramCount,
      nameCount);
}

//  QScxmlExecutableContent::Send::~Send()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent4SendD1Ev(
    QScxmlExecutableContent::Send *self) {
  delete self;
}
