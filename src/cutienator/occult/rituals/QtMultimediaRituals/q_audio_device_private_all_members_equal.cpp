//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiodevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QAudioDevicePrivateAllMembersEqual::operator()(const
//      QAudioDevicePrivate &lhs, const QAudioDevicePrivate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QAudioDevicePrivateAllMembersEqualclERK19QAudioDevicePrivateS2_(
    QAudioDevicePrivateAllMembersEqual *self,
    const QAudioDevicePrivate *lhs,
    const QAudioDevicePrivate *rhs) {
  return self->operator()(*lhs, *rhs);
}

//  QAudioDevicePrivateAllMembersEqual::~QAudioDevicePrivateAllMembersEqual()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QAudioDevicePrivateAllMembersEqualD1Ev(
    QAudioDevicePrivateAllMembersEqual *self) {
  delete self;
}
