//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSettingsGroup::QSettingsGroup()
extern "C" Q_DECL_EXPORT
QSettingsGroup *ritual_ZN14QSettingsGroupC1Ev() {
  return new QSettingsGroup();
}

//  QSettingsGroup::QSettingsGroup(const QString &s)
extern "C" Q_DECL_EXPORT
QSettingsGroup *ritual_ZN14QSettingsGroupC1ERK7QString(const QString *s) {
  return new QSettingsGroup(*s);
}

//  QSettingsGroup::QSettingsGroup(const QString &s, bool guessArraySize)
extern "C" Q_DECL_EXPORT
QSettingsGroup *ritual_ZN14QSettingsGroupC1ERK7QStringb(
    const QString *s,
    bool guessArraySize) {
  return new QSettingsGroup(*s, guessArraySize);
}

//  QString QSettingsGroup::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSettingsGroup4nameEv(const QSettingsGroup *self) {
  return new QString(self->name());
}

//  QString QSettingsGroup::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSettingsGroup8toStringEv(const QSettingsGroup *self) {
  return new QString(self->toString());
}

//  bool QSettingsGroup::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSettingsGroup7isArrayEv(const QSettingsGroup *self) {
  return self->isArray();
}

//  qsizetype QSettingsGroup::arraySizeGuess() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QSettingsGroup14arraySizeGuessEv(
    const QSettingsGroup *self) {
  return self->arraySizeGuess();
}

//  void QSettingsGroup::setArrayIndex(qsizetype i)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSettingsGroup13setArrayIndexEx(
    QSettingsGroup *self,
    qsizetype i) {
  self->setArrayIndex(i);
}

//  QSettingsGroup::~QSettingsGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSettingsGroupD1Ev(QSettingsGroup *self) {
  delete self;
}
