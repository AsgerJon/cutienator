//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(QT_QSETTINGS_ALWAYS_CASE_SENSITIVE_AND_FORGET_ORIGINAL_KEY_ORDER)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSettingsKey::QSettingsKey(const QString &key, Qt::CaseSensitivity cs,
//      qsizetype a2)
extern "C" Q_DECL_EXPORT
QSettingsKey *ritual_ZN12QSettingsKeyC1ERK7QStringN2Qt15CaseSensitivityEx(
    const QString *key,
    Qt::CaseSensitivity cs,
    qsizetype a2) {
  return new QSettingsKey(*key, cs, a2);
}

//  QString QSettingsKey::originalCaseKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSettingsKey15originalCaseKeyEv(
    const QSettingsKey *self) {
  return new QString(self->originalCaseKey());
}

//  qsizetype QSettingsKey::originalKeyPosition() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QSettingsKey19originalKeyPositionEv(
    const QSettingsKey *self) {
  return self->originalKeyPosition();
}

//  QSettingsKey::~QSettingsKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSettingsKeyD1Ev(QSettingsKey *self) {
  delete self;
}

#endif  // defined(QT_QSETTINGS_ALWAYS_CASE_SENSITIVE_AND_FORGET_ORIGINAL_KEY_ORDER)
