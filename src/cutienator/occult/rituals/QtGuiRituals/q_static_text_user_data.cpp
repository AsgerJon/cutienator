//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstatictext_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstatictext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QStaticTextUserData::QStaticTextUserData(Type t)
extern "C" Q_DECL_EXPORT
QStaticTextUserData *ritual_ZN19QStaticTextUserDataC1ENS_4TypeE(
    QStaticTextUserData::Type t) {
  return new QStaticTextUserData(t);
}

//  QStaticTextUserData::~QStaticTextUserData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStaticTextUserDataD1Ev(QStaticTextUserData *self) {
  delete self;
}
