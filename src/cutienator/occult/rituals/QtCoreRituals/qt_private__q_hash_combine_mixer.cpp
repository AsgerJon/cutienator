//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qhashfunctions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qhashfunctions.h>

//  result_type QtPrivate::QHashCombineMixer::operator()(result_type result,
//      result_type hash) const
extern "C" Q_DECL_EXPORT
unsigned long long ritual_ZNK9QtPrivate17QHashCombineMixerclEmm(
    const QtPrivate::QHashCombineMixer *self,
    unsigned long long result,
    unsigned long long hash) {
  return self->operator()(result, hash);
}

//  QtPrivate::QHashCombineMixer::~QHashCombineMixer()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate17QHashCombineMixerD1Ev(
    QtPrivate::QHashCombineMixer *self) {
  delete self;
}
