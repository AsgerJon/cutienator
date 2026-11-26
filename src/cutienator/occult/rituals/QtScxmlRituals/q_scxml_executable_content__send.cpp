//  Written by hand on 2026-11-25 from
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  The two 'params' functions are written, with the Array named in full
//  (QScxmlExecutableContent::Array), as the generator wrote it without
//  its namespace. Array itself is a template and gets none.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>

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

//  const Array<ParameterInfo> *QScxmlExecutableContent::Send::params() const
extern "C" Q_DECL_EXPORT
const QScxmlExecutableContent::Array<QScxmlExecutableContent::ParameterInfo> *ritual_ZNK23QScxmlExecutableContent4Send6paramsEv(
    const QScxmlExecutableContent::Send *self) {
  return self->params();
}

//  Array<ParameterInfo> *QScxmlExecutableContent::Send::params()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::Array<QScxmlExecutableContent::ParameterInfo> *ritual_ZN23QScxmlExecutableContent4Send6paramsEv(
    QScxmlExecutableContent::Send *self) {
  return self->params();
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
