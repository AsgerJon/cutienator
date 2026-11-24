//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QFontDatabasePrivate::QFontDatabasePrivate()
extern "C" Q_DECL_EXPORT
QFontDatabasePrivate *ritual_ZN20QFontDatabasePrivateC1Ev() {
  return new QFontDatabasePrivate();
}

//  QFontDatabasePrivate::~QFontDatabasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFontDatabasePrivateD1Ev(QFontDatabasePrivate *self) {
  delete self;
}

//  void QFontDatabasePrivate::clearFamilies()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFontDatabasePrivate13clearFamiliesEv(
    QFontDatabasePrivate *self) {
  self->clearFamilies();
}

//  QtFontFamily *QFontDatabasePrivate::family(const QString &f,
//      FamilyRequestFlags flags)
extern "C" Q_DECL_EXPORT
QtFontFamily *ritual_ZN20QFontDatabasePrivate6familyERK7QStringNS_18FamilyRequestFlagsE(
    QFontDatabasePrivate *self,
    const QString *f,
    QFontDatabasePrivate::FamilyRequestFlags flags) {
  return self->family(*f, flags);
}

//  int QFontDatabasePrivate::addAppFont(const QByteArray &fontData, const
//      QString &fileName)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QFontDatabasePrivate10addAppFontERK10QByteArrayRK7QString(
    QFontDatabasePrivate *self,
    const QByteArray *fontData,
    const QString *fileName) {
  return self->addAppFont(*fontData, *fileName);
}

//  bool QFontDatabasePrivate::isApplicationFont(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFontDatabasePrivate17isApplicationFontERK7QString(
    QFontDatabasePrivate *self,
    const QString *fileName) {
  return self->isApplicationFont(*fileName);
}

//  void
//      QFontDatabasePrivate::setApplicationFallbackFontFamilies(ExtendedScri
//      pt script, const QStringList &familyNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFontDatabasePrivate34setApplicationFallbackFontFamiliesENS_14ExtendedScriptERK5QListI7QStringE(
    QFontDatabasePrivate *self,
    QFontDatabasePrivate::ExtendedScript script,
    const QList<QString> *familyNames) {
  self->setApplicationFallbackFontFamilies(script, *familyNames);
}

//  QStringList
//      QFontDatabasePrivate::applicationFallbackFontFamilies(ExtendedScript
//      script)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN20QFontDatabasePrivate31applicationFallbackFontFamiliesENS_14ExtendedScriptE(
    QFontDatabasePrivate *self,
    QFontDatabasePrivate::ExtendedScript script) {
  return new QList<QString>(self->applicationFallbackFontFamilies(script));
}

//  bool
//      QFontDatabasePrivate::removeApplicationFallbackFontFamily(ExtendedScr
//      ipt script, const QString &familyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFontDatabasePrivate35removeApplicationFallbackFontFamilyENS_14ExtendedScriptERK7QString(
    QFontDatabasePrivate *self,
    QFontDatabasePrivate::ExtendedScript script,
    const QString *familyName) {
  return self->removeApplicationFallbackFontFamily(script, *familyName);
}

//  void
//      QFontDatabasePrivate::addApplicationFallbackFontFamily(ExtendedScript
//      script, const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFontDatabasePrivate32addApplicationFallbackFontFamilyENS_14ExtendedScriptERK7QString(
    QFontDatabasePrivate *self,
    QFontDatabasePrivate::ExtendedScript script,
    const QString *familyName) {
  self->addApplicationFallbackFontFamily(script, *familyName);
}

//  QFontDatabasePrivate *QFontDatabasePrivate::instance()
extern "C" Q_DECL_EXPORT
QFontDatabasePrivate *ritual_ZN20QFontDatabasePrivate8instanceEv() {
  return QFontDatabasePrivate::instance();
}

//  QString QFontDatabasePrivate::resolveFontFamilyAlias(const QString
//      &family)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QFontDatabasePrivate22resolveFontFamilyAliasERK7QString(
    const QString *family) {
  return new QString(QFontDatabasePrivate::resolveFontFamilyAlias(*family));
}

//  QFontEngine *QFontDatabasePrivate::findFont(const QFontDef &request, int
//      script, bool preferScriptOverFamily)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN20QFontDatabasePrivate8findFontERK8QFontDefib(
    const QFontDef *request,
    int script,
    bool preferScriptOverFamily) {
  return QFontDatabasePrivate::findFont(
      *request,
      script,
      preferScriptOverFamily);
}

//  void QFontDatabasePrivate::load(const QFontPrivate *d, int script)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFontDatabasePrivate4loadEPK12QFontPrivatei(
    const QFontPrivate *d,
    int script) {
  QFontDatabasePrivate::load(d, script);
}

//  QFontDatabasePrivate *QFontDatabasePrivate::ensureFontDatabase()
extern "C" Q_DECL_EXPORT
QFontDatabasePrivate *ritual_ZN20QFontDatabasePrivate18ensureFontDatabaseEv() {
  return QFontDatabasePrivate::ensureFontDatabase();
}

//  void QFontDatabasePrivate::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFontDatabasePrivate10invalidateEv(
    QFontDatabasePrivate *self) {
  self->invalidate();
}

//  QFontEngine *QFontDatabasePrivate::loadSingleEngine(int script, const
//      QFontDef &request, QtFontFamily *family, QtFontFoundry *foundry,
//      QtFontStyle *style, QtFontSize *size)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN20QFontDatabasePrivate16loadSingleEngineEiRK8QFontDefP12QtFontFamilyP13QtFontFoundryP11QtFontStyleP10QtFontSize(
    int script,
    const QFontDef *request,
    QtFontFamily *family,
    QtFontFoundry *foundry,
    QtFontStyle *style,
    QtFontSize *size) {
  return QFontDatabasePrivate::loadSingleEngine(
      script,
      *request,
      family,
      foundry,
      style,
      size);
}

//  QFontEngine *QFontDatabasePrivate::loadEngine(int script, const QFontDef
//      &request, QtFontFamily *family, QtFontFoundry *foundry, QtFontStyle
//      *style, QtFontSize *size)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN20QFontDatabasePrivate10loadEngineEiRK8QFontDefP12QtFontFamilyP13QtFontFoundryP11QtFontStyleP10QtFontSize(
    int script,
    const QFontDef *request,
    QtFontFamily *family,
    QtFontFoundry *foundry,
    QtFontStyle *style,
    QtFontSize *size) {
  return QFontDatabasePrivate::loadEngine(
      script,
      *request,
      family,
      foundry,
      style,
      size);
}
