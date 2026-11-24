//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_qsettings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  QDesignerQSettings::QDesignerQSettings()
extern "C" Q_DECL_EXPORT
QDesignerQSettings *ritual_ZN18QDesignerQSettingsC1Ev() {
  return new QDesignerQSettings();
}

//  void QDesignerQSettings::beginGroup(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDesignerQSettings10beginGroupERK7QString(
    QDesignerQSettings *self,
    const QString *prefix) {
  self->beginGroup(*prefix);
}

//  void QDesignerQSettings::endGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDesignerQSettings8endGroupEv(QDesignerQSettings *self) {
  self->endGroup();
}

//  bool QDesignerQSettings::contains(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDesignerQSettings8containsERK7QString(
    const QDesignerQSettings *self,
    const QString *key) {
  return self->contains(*key);
}

//  void QDesignerQSettings::setValue(const QString &key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDesignerQSettings8setValueERK7QStringRK8QVariant(
    QDesignerQSettings *self,
    const QString *key,
    const QVariant *value) {
  self->setValue(*key, *value);
}

//  QVariant QDesignerQSettings::value(const QString &key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QDesignerQSettings5valueERK7QStringRK8QVariant(
    const QDesignerQSettings *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->value(*key, *defaultValue));
}

//  void QDesignerQSettings::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDesignerQSettings6removeERK7QString(
    QDesignerQSettings *self,
    const QString *key) {
  self->remove(*key);
}

//  QString QDesignerQSettings::settingsApplicationName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QDesignerQSettings23settingsApplicationNameEv() {
  return new QString(QDesignerQSettings::settingsApplicationName());
}

//  void QDesignerQSettings::beginGroup(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QDesignerQSettings10beginGroupERK7QString(
    QDesignerQSettings *self,
    const QString *prefix) {
  self->QDesignerQSettings::beginGroup(*prefix);
}

//  void QDesignerQSettings::endGroup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QDesignerQSettings8endGroupEv(QDesignerQSettings *self) {
  self->QDesignerQSettings::endGroup();
}

//  bool QDesignerQSettings::contains(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QDesignerQSettings8containsERK7QString(
    const QDesignerQSettings *self,
    const QString *key) {
  return self->QDesignerQSettings::contains(*key);
}

//  void QDesignerQSettings::setValue(const QString &key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QDesignerQSettings8setValueERK7QStringRK8QVariant(
    QDesignerQSettings *self,
    const QString *key,
    const QVariant *value) {
  self->QDesignerQSettings::setValue(*key, *value);
}

//  QVariant QDesignerQSettings::value(const QString &key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK18QDesignerQSettings5valueERK7QStringRK8QVariant(
    const QDesignerQSettings *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->QDesignerQSettings::value(*key, *defaultValue));
}

//  void QDesignerQSettings::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QDesignerQSettings6removeERK7QString(
    QDesignerQSettings *self,
    const QString *key) {
  self->QDesignerQSettings::remove(*key);
}
