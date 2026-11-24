//  Written by dev_tooling.RitualGenerator from the records of
//  QtTextToSpeech/6.12.0/QtTextToSpeech/private/qvoice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTextToSpeech/QtTextToSpeech>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtTextToSpeech/6.12.0/QtTextToSpeech/private/qvoice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtCore/qvariant.h>

//  QVoicePrivate::QVoicePrivate()
extern "C" Q_DECL_EXPORT
QVoicePrivate *ritual_ZN13QVoicePrivateC1Ev() {
  return new QVoicePrivate();
}

//  QVoicePrivate::QVoicePrivate(const QString &n, const QLocale &l,
//      QVoice::Gender g, QVoice::Age a, const QVariant &d)
extern "C" Q_DECL_EXPORT
QVoicePrivate *ritual_ZN13QVoicePrivateC1ERK7QStringRK7QLocaleN6QVoice6GenderENS6_3AgeERK8QVariant(
    const QString *n,
    const QLocale *l,
    QVoice::Gender g,
    QVoice::Age a,
    const QVariant *d) {
  return new QVoicePrivate(*n, *l, g, a, *d);
}

//  QVoicePrivate::~QVoicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVoicePrivateD1Ev(QVoicePrivate *self) {
  delete self;
}
