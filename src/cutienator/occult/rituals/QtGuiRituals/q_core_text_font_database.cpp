//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qcoretextfontdatabase_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  Core Text's descriptors, a 'CFArrayRef' and a 'void *' are passed
//  as addresses. It declares 'shouldForceColorFont' with nothing to
//  run, so no object is made of it here and it has no Cute class: its
//  functions are called through objects Qt made. Not written:
//  'standardSizes', giving a list of numbers, as the generator leaves
//  it out of QPlatformFontDatabase; and the template
//  'QCoreTextFontDatabaseEngineFactory'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qcoretextfontdatabase_p.h>
#include <QtGui/qfont.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstringlist.h>

//  QCoreTextFontDatabase::~QCoreTextFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCoreTextFontDatabaseD1Ev(QCoreTextFontDatabase *self) {
  delete self;
}

//  void QCoreTextFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCoreTextFontDatabase20populateFontDatabaseEv(
    QCoreTextFontDatabase *self) {
  self->populateFontDatabase();
}

//  bool QCoreTextFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QCoreTextFontDatabase21populateFamilyAliasesERK7QString(
    QCoreTextFontDatabase *self,
    const QString *missingFamily) {
  return self->populateFamilyAliases(*missingFamily);
}

//  void QCoreTextFontDatabase::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCoreTextFontDatabase14populateFamilyERK7QString(
    QCoreTextFontDatabase *self,
    const QString *familyName) {
  self->populateFamily(*familyName);
}

//  void QCoreTextFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCoreTextFontDatabase10invalidateEv(
    QCoreTextFontDatabase *self) {
  self->invalidate();
}

//  QStringList QCoreTextFontDatabase::fallbacksForFamily(const QString
//      &family, QFont::Style style, QFont::StyleHint styleHint,
//      QFontDatabasePrivate::ExtendedScript script) const
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZNK21QCoreTextFontDatabase18fallbacksForFamilyERK7QStringN5QFont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScriptE(
    const QCoreTextFontDatabase *self,
    const QString *family,
    QFont::Style style,
    QFont::StyleHint styleHint,
    QFontDatabasePrivate::ExtendedScript script) {
  return new QStringList(self->fallbacksForFamily(*family, style, styleHint, script));
}

//  QStringList QCoreTextFontDatabase::addApplicationFont(const QByteArray
//      &fontData, const QString &fileName,
//      QFontDatabasePrivate::ApplicationFont *applicationFont)
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZN21QCoreTextFontDatabase18addApplicationFontERK10QByteArrayRK7QStringPN20QFontDatabasePrivate15ApplicationFontE(
    QCoreTextFontDatabase *self,
    const QByteArray *fontData,
    const QString *fileName,
    QFontDatabasePrivate::ApplicationFont *applicationFont) {
  return new QStringList(self->addApplicationFont(*fontData, *fileName, applicationFont));
}

//  void QCoreTextFontDatabase::releaseHandle(void *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCoreTextFontDatabase13releaseHandleEPv(
    QCoreTextFontDatabase *self,
    void *handle) {
  self->releaseHandle(handle);
}

//  bool QCoreTextFontDatabase::isPrivateFontFamily(const QString &family)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QCoreTextFontDatabase19isPrivateFontFamilyERK7QString(
    const QCoreTextFontDatabase *self,
    const QString *family) {
  return self->isPrivateFontFamily(*family);
}

//  QFont QCoreTextFontDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK21QCoreTextFontDatabase11defaultFontEv(
    const QCoreTextFontDatabase *self) {
  return new QFont(self->defaultFont());
}

//  bool QCoreTextFontDatabase::fontsAlwaysScalable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QCoreTextFontDatabase19fontsAlwaysScalableEv(
    const QCoreTextFontDatabase *self) {
  return self->fontsAlwaysScalable();
}

//  bool QCoreTextFontDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QCoreTextFontDatabase32supportsVariableApplicationFontsEv(
    const QCoreTextFontDatabase *self) {
  return self->supportsVariableApplicationFonts();
}

//  bool QCoreTextFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QCoreTextFontDatabase19supportsColrv0FontsEv(
    const QCoreTextFontDatabase *self) {
  return self->supportsColrv0Fonts();
}

//  QFont *QCoreTextFontDatabase::themeFont(QPlatformTheme::Font a0) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK21QCoreTextFontDatabase9themeFontEN14QPlatformTheme4FontE(
    const QCoreTextFontDatabase *self,
    QPlatformTheme::Font a0) {
  return self->themeFont(a0);
}

//  bool QCoreTextFontDatabase::shouldForceColorFont(CTFontDescriptorRef
//      descriptor) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QCoreTextFontDatabase20shouldForceColorFontEPK18__CTFontDescriptor(
    const QCoreTextFontDatabase *self,
    CTFontDescriptorRef descriptor) {
  return self->shouldForceColorFont(descriptor);
}

//  void QCoreTextFontDatabase::populateThemeFonts()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCoreTextFontDatabase18populateThemeFontsEv(
    QCoreTextFontDatabase *self) {
  self->populateThemeFonts();
}

//  void QCoreTextFontDatabase::populateFromDescriptor(CTFontDescriptorRef
//      font, const QString &familyName,
//      QFontDatabasePrivate::ApplicationFont *applicationFont,
//      PopulateDescriptorFlag a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCoreTextFontDatabase22populateFromDescriptorEPK18__CTFontDescriptorRK7QStringPN20QFontDatabasePrivate15ApplicationFontENS_22PopulateDescriptorFlagE(
    QCoreTextFontDatabase *self,
    CTFontDescriptorRef font,
    const QString *familyName,
    QFontDatabasePrivate::ApplicationFont *applicationFont,
    int a3) {
  self->populateFromDescriptor(
      font, *familyName, applicationFont,
      static_cast<QCoreTextFontDatabase::PopulateDescriptorFlag>(a3));
}

//  CFArrayRef QCoreTextFontDatabase::fallbacksForFamily(const QString
//      &family)
extern "C" Q_DECL_EXPORT
CFArrayRef ritual_ZN21QCoreTextFontDatabase18fallbacksForFamilyERK7QString(
    const QString *family) {
  return QCoreTextFontDatabase::fallbacksForFamily(*family);
}

//  QStringList QCoreTextFontDatabase::fallbacksForScript(QFontDatabasePrivat
//      e::ExtendedScript script) const
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZNK21QCoreTextFontDatabase18fallbacksForScriptEN20QFontDatabasePrivate14ExtendedScriptE(
    const QCoreTextFontDatabase *self,
    QFontDatabasePrivate::ExtendedScript script) {
  return new QStringList(self->fallbacksForScript(script));
}

//  void QCoreTextFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QCoreTextFontDatabase20populateFontDatabaseEv(
    QCoreTextFontDatabase *self) {
  self->QCoreTextFontDatabase::populateFontDatabase();
}

//  bool QCoreTextFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QCoreTextFontDatabase21populateFamilyAliasesERK7QString(
    QCoreTextFontDatabase *self,
    const QString *missingFamily) {
  return self->QCoreTextFontDatabase::populateFamilyAliases(*missingFamily);
}

//  void QCoreTextFontDatabase::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QCoreTextFontDatabase14populateFamilyERK7QString(
    QCoreTextFontDatabase *self,
    const QString *familyName) {
  self->QCoreTextFontDatabase::populateFamily(*familyName);
}

//  void QCoreTextFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QCoreTextFontDatabase10invalidateEv(
    QCoreTextFontDatabase *self) {
  self->QCoreTextFontDatabase::invalidate();
}

//  bool QCoreTextFontDatabase::isPrivateFontFamily(const QString &family)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QCoreTextFontDatabase19isPrivateFontFamilyERK7QString(
    const QCoreTextFontDatabase *self,
    const QString *family) {
  return self->QCoreTextFontDatabase::isPrivateFontFamily(*family);
}

//  QFont QCoreTextFontDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK21QCoreTextFontDatabase11defaultFontEv(
    const QCoreTextFontDatabase *self) {
  return new QFont(self->QCoreTextFontDatabase::defaultFont());
}

//  bool QCoreTextFontDatabase::fontsAlwaysScalable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QCoreTextFontDatabase19fontsAlwaysScalableEv(
    const QCoreTextFontDatabase *self) {
  return self->QCoreTextFontDatabase::fontsAlwaysScalable();
}

//  bool QCoreTextFontDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QCoreTextFontDatabase32supportsVariableApplicationFontsEv(
    const QCoreTextFontDatabase *self) {
  return self->QCoreTextFontDatabase::supportsVariableApplicationFonts();
}

//  bool QCoreTextFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QCoreTextFontDatabase19supportsColrv0FontsEv(
    const QCoreTextFontDatabase *self) {
  return self->QCoreTextFontDatabase::supportsColrv0Fonts();
}

#endif  // defined(Q_OS_DARWIN)
