//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const Parameter *QV4::CompiledData::Signal::parameterAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Parameter *ritual_ZNK3QV412CompiledData6Signal11parameterAtEi(
    const QV4::CompiledData::Signal *self,
    int idx) {
  return self->parameterAt(idx);
}

//  int QV4::CompiledData::Signal::calculateSize(int nParameters)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData6Signal13calculateSizeEi(int nParameters) {
  return QV4::CompiledData::Signal::calculateSize(nParameters);
}

//  const Parameter *QV4::CompiledData::Signal::parametersBegin() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Parameter *ritual_ZNK3QV412CompiledData6Signal15parametersBeginEv(
    const QV4::CompiledData::Signal *self) {
  return self->parametersBegin();
}

//  const Parameter *QV4::CompiledData::Signal::parametersEnd() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Parameter *ritual_ZNK3QV412CompiledData6Signal13parametersEndEv(
    const QV4::CompiledData::Signal *self) {
  return self->parametersEnd();
}

//  int QV4::CompiledData::Signal::parameterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData6Signal14parameterCountEv(
    const QV4::CompiledData::Signal *self) {
  return self->parameterCount();
}

//  QV4::CompiledData::Signal::~Signal()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6SignalD1Ev(
    QV4::CompiledData::Signal *self) {
  delete self;
}
