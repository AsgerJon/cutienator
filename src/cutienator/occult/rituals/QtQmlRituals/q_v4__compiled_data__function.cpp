//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const Parameter *QV4::CompiledData::Function::formalsTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Parameter *ritual_ZNK3QV412CompiledData8Function12formalsTableEv(
    const QV4::CompiledData::Function *self) {
  return self->formalsTable();
}

//  const CodeOffsetToLineAndStatement
//      *QV4::CompiledData::Function::lineAndStatementNumberTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::CodeOffsetToLineAndStatement *ritual_ZNK3QV412CompiledData8Function27lineAndStatementNumberTableEv(
    const QV4::CompiledData::Function *self) {
  return self->lineAndStatementNumberTable();
}

//  const Parameter *QV4::CompiledData::Function::formalsBegin() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Parameter *ritual_ZNK3QV412CompiledData8Function12formalsBeginEv(
    const QV4::CompiledData::Function *self) {
  return self->formalsBegin();
}

//  const Parameter *QV4::CompiledData::Function::formalsEnd() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Parameter *ritual_ZNK3QV412CompiledData8Function10formalsEndEv(
    const QV4::CompiledData::Function *self) {
  return self->formalsEnd();
}

//  const char *QV4::CompiledData::Function::code() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK3QV412CompiledData8Function4codeEv(
    const QV4::CompiledData::Function *self) {
  return self->code();
}

//  int QV4::CompiledData::Function::calculateSize(int nFormals, int nLocals,
//      int nLinesAndStatements, int labelInfoSize, int codeSize)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData8Function13calculateSizeEiiiii(
    int nFormals,
    int nLocals,
    int nLinesAndStatements,
    int labelInfoSize,
    int codeSize) {
  return QV4::CompiledData::Function::calculateSize(
      nFormals,
      nLocals,
      nLinesAndStatements,
      labelInfoSize,
      codeSize);
}

//  QV4::CompiledData::Function::~Function()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData8FunctionD1Ev(
    QV4::CompiledData::Function *self) {
  delete self;
}
