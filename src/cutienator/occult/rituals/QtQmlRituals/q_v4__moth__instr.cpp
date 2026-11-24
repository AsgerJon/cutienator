//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Type QV4::Moth::Instr::wideInstructionType(Type t)
extern "C" Q_DECL_EXPORT
QV4::Moth::Instr::Type ritual_ZN3QV44Moth5Instr19wideInstructionTypeENS1_4TypeE(
    QV4::Moth::Instr::Type t) {
  return QV4::Moth::Instr::wideInstructionType(t);
}

//  Type QV4::Moth::Instr::narrowInstructionType(Type t)
extern "C" Q_DECL_EXPORT
QV4::Moth::Instr::Type ritual_ZN3QV44Moth5Instr21narrowInstructionTypeENS1_4TypeE(
    QV4::Moth::Instr::Type t) {
  return QV4::Moth::Instr::narrowInstructionType(t);
}

//  bool QV4::Moth::Instr::isWide(Type t)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Moth5Instr6isWideENS1_4TypeE(QV4::Moth::Instr::Type t) {
  return QV4::Moth::Instr::isWide(t);
}

//  bool QV4::Moth::Instr::isNarrow(Type t)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Moth5Instr8isNarrowENS1_4TypeE(QV4::Moth::Instr::Type t) {
  return QV4::Moth::Instr::isNarrow(t);
}

//  int QV4::Moth::Instr::encodedLength(Type t)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV44Moth5Instr13encodedLengthENS1_4TypeE(
    QV4::Moth::Instr::Type t) {
  return QV4::Moth::Instr::encodedLength(t);
}

//  QV4::Moth::Instr::~Instr()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth5InstrD1Ev(QV4::Moth::Instr *self) {
  delete self;
}
