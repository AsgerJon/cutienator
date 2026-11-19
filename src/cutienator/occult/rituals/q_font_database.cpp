//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfontdatabase.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfontdatabase.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtGui/qfontinfo.h>
#include <QtCore/qbytearray.h>

//  QFontDatabase::QFontDatabase()
extern "C" Q_DECL_EXPORT
QFontDatabase *ritual_ZN13QFontDatabaseC1Ev() {
  return new QFontDatabase();
}

//  QString QFontDatabase::styleString(const QFont &font)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFontDatabase11styleStringERK5QFont(const QFont *font) {
  return new QString(QFontDatabase::styleString(*font));
}

//  QString QFontDatabase::styleString(const QFontInfo &fontInfo)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFontDatabase11styleStringERK9QFontInfo(
    const QFontInfo *fontInfo) {
  return new QString(QFontDatabase::styleString(*fontInfo));
}

//  QFont QFontDatabase::font(const QString &family, const QString &style,
//      int pointSize)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN13QFontDatabase4fontERK7QStringS2_i(
    const QString *family,
    const QString *style,
    int pointSize) {
  return new QFont(QFontDatabase::font(*family, *style, pointSize));
}

//  bool QFontDatabase::isBitmapScalable(const QString &family, const QString
//      &style)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase16isBitmapScalableERK7QStringS2_(
    const QString *family,
    const QString *style) {
  return QFontDatabase::isBitmapScalable(*family, *style);
}

//  bool QFontDatabase::isSmoothlyScalable(const QString &family, const
//      QString &style)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase18isSmoothlyScalableERK7QStringS2_(
    const QString *family,
    const QString *style) {
  return QFontDatabase::isSmoothlyScalable(*family, *style);
}

//  bool QFontDatabase::isScalable(const QString &family, const QString
//      &style)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase10isScalableERK7QStringS2_(
    const QString *family,
    const QString *style) {
  return QFontDatabase::isScalable(*family, *style);
}

//  bool QFontDatabase::isFixedPitch(const QString &family, const QString
//      &style)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase12isFixedPitchERK7QStringS2_(
    const QString *family,
    const QString *style) {
  return QFontDatabase::isFixedPitch(*family, *style);
}

//  bool QFontDatabase::italic(const QString &family, const QString &style)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase6italicERK7QStringS2_(
    const QString *family,
    const QString *style) {
  return QFontDatabase::italic(*family, *style);
}

//  bool QFontDatabase::bold(const QString &family, const QString &style)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase4boldERK7QStringS2_(
    const QString *family,
    const QString *style) {
  return QFontDatabase::bold(*family, *style);
}

//  int QFontDatabase::weight(const QString &family, const QString &style)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QFontDatabase6weightERK7QStringS2_(
    const QString *family,
    const QString *style) {
  return QFontDatabase::weight(*family, *style);
}

//  bool QFontDatabase::hasFamily(const QString &family)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase9hasFamilyERK7QString(const QString *family) {
  return QFontDatabase::hasFamily(*family);
}

//  bool QFontDatabase::isPrivateFamily(const QString &family)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase15isPrivateFamilyERK7QString(
    const QString *family) {
  return QFontDatabase::isPrivateFamily(*family);
}

//  QString QFontDatabase::writingSystemName(WritingSystem writingSystem)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFontDatabase17writingSystemNameENS_13WritingSystemE(
    QFontDatabase::WritingSystem writingSystem) {
  return new QString(QFontDatabase::writingSystemName(writingSystem));
}

//  QString QFontDatabase::writingSystemSample(WritingSystem writingSystem)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFontDatabase19writingSystemSampleENS_13WritingSystemE(
    QFontDatabase::WritingSystem writingSystem) {
  return new QString(QFontDatabase::writingSystemSample(writingSystem));
}

//  int QFontDatabase::addApplicationFont(const QString &fileName)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QFontDatabase18addApplicationFontERK7QString(
    const QString *fileName) {
  return QFontDatabase::addApplicationFont(*fileName);
}

//  int QFontDatabase::addApplicationFontFromData(const QByteArray &fontData)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QFontDatabase26addApplicationFontFromDataERK10QByteArray(
    const QByteArray *fontData) {
  return QFontDatabase::addApplicationFontFromData(*fontData);
}

//  bool QFontDatabase::removeApplicationFont(int id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase21removeApplicationFontEi(int id) {
  return QFontDatabase::removeApplicationFont(id);
}

//  bool QFontDatabase::removeAllApplicationFonts()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase25removeAllApplicationFontsEv() {
  return QFontDatabase::removeAllApplicationFonts();
}

//  void QFontDatabase::addApplicationFallbackFontFamily(QChar::Script
//      script, const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontDatabase32addApplicationFallbackFontFamilyEN5QChar6ScriptERK7QString(
    QChar::Script script,
    const QString *familyName) {
  QFontDatabase::addApplicationFallbackFontFamily(script, *familyName);
}

//  bool QFontDatabase::removeApplicationFallbackFontFamily(QChar::Script
//      script, const QString &familyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase35removeApplicationFallbackFontFamilyEN5QChar6ScriptERK7QString(
    QChar::Script script,
    const QString *familyName) {
  return QFontDatabase::removeApplicationFallbackFontFamily(
      script,
      *familyName);
}

//  void QFontDatabase::addApplicationEmojiFontFamily(const QString
//      &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontDatabase29addApplicationEmojiFontFamilyERK7QString(
    const QString *familyName) {
  QFontDatabase::addApplicationEmojiFontFamily(*familyName);
}

//  bool QFontDatabase::removeApplicationEmojiFontFamily(const QString
//      &familyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontDatabase32removeApplicationEmojiFontFamilyERK7QString(
    const QString *familyName) {
  return QFontDatabase::removeApplicationEmojiFontFamily(*familyName);
}

//  QFont QFontDatabase::systemFont(SystemFont type)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN13QFontDatabase10systemFontENS_10SystemFontE(
    QFontDatabase::SystemFont type) {
  return new QFont(QFontDatabase::systemFont(type));
}

//  QFontDatabase::~QFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontDatabaseD1Ev(QFontDatabase *self) {
  delete self;
}
