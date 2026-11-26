//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstringconverter.h>

//  QStringConverterBase::State::State(Flags f)
extern "C" Q_DECL_EXPORT
QStringConverterBase::State *ritual_ZN20QStringConverterBase5StateC1E6QFlagsINS_4FlagEE(
    int f) {
  return new QStringConverterBase::State(
      QFlags<QStringConverterBase::Flag>::fromInt(f));
}

//  QStringConverterBase::State::~State()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStringConverterBase5StateD1Ev(
    QStringConverterBase::State *self) {
  delete self;
}

//  QStringConverterBase::State::State(State &&other)
extern "C" Q_DECL_EXPORT
QStringConverterBase::State *ritual_ZN20QStringConverterBase5StateC1EOS0_(
    QStringConverterBase::State *other) {
  return new QStringConverterBase::State(std::move(*other));
}

//  State &QStringConverterBase::State::operator=(State &&other)
extern "C" Q_DECL_EXPORT
QStringConverterBase::State *ritual_ZN20QStringConverterBase5StateaSEOS0_(
    QStringConverterBase::State *self,
    QStringConverterBase::State *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QStringConverterBase::State::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStringConverterBase5State5clearEv(
    QStringConverterBase::State *self) {
  self->clear();
}

//  void QStringConverterBase::State::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStringConverterBase5State5resetEv(
    QStringConverterBase::State *self) {
  self->reset();
}
