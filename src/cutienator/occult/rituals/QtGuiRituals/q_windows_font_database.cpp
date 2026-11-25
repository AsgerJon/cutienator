//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
//  A 'void *' is passed as an address. Not written: 'createEngine',
//  which takes a 'QSharedPointer', and 'debugFormat', taking a
//  'QDebug &' and a 'LOGFONT'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h>
#include <QtGui/qfont.h>
#include <QtCore/qstringlist.h>
#include <cstring>

//  A QWindowsFontDatabase that Python can take functions over in. Every
//  QWindowsFontDatabase Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQWindowsFontDatabaseCall0)(const void *, int *);
typedef void * (*CuteQWindowsFontDatabaseCall1)(const void *, const QByteArray *, qreal, int, int *);
typedef bool (*CuteQWindowsFontDatabaseCall2)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseCall3)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseCall4)(const void *, const QString *, int *);
typedef void (*CuteQWindowsFontDatabaseCall5)(const void *, const QString *, int *);
typedef void (*CuteQWindowsFontDatabaseCall6)(const void *, int *);
typedef void * (*CuteQWindowsFontDatabaseCall7)(const void *, QFontEngine *, int, int *);
typedef QString * (*CuteQWindowsFontDatabaseCall8)(const void *, int *);
typedef const QFont * (*CuteQWindowsFontDatabaseCall9)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQWindowsFontDatabaseCall11)(const void *, const QString *, int *);
typedef bool (*CuteQWindowsFontDatabaseCall12)(const void *, int *);
class CuteQWindowsFontDatabase : public QWindowsFontDatabase {
public:
  using QWindowsFontDatabase::QWindowsFontDatabase;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase20populateFontDatabaseEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase32supportsVariableApplicationFontsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase14populateFamilyERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10invalidateEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase7fontDirEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase11defaultFontEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  void QWindowsFontDatabase::populateFontDatabase()
  void populateFontDatabase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall0 call = reinterpret_cast<CuteQWindowsFontDatabaseCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsFontDatabase::populateFontDatabase();
  }

  //  QFontEngine *QWindowsFontDatabase::fontEngine(const QByteArray
  //      &fontData, qreal pixelSize, QFont::HintingPreference
  //      hintingPreference)
  QFontEngine *fontEngine(const QByteArray &fontData, qreal pixelSize, QFont::HintingPreference hintingPreference) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall1 call = reinterpret_cast<CuteQWindowsFontDatabaseCall1>(taken[1]);
      void * given = call(this, &fontData, pixelSize, static_cast<int>(hintingPreference), &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QWindowsFontDatabase::fontEngine(fontData, pixelSize, hintingPreference);
  }

  //  bool QPlatformFontDatabase::supportsVariableApplicationFonts() const
  bool supportsVariableApplicationFonts() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall2 call = reinterpret_cast<CuteQWindowsFontDatabaseCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::supportsVariableApplicationFonts();
  }

  //  bool QWindowsFontDatabase::supportsColrv0Fonts() const
  bool supportsColrv0Fonts() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall3 call = reinterpret_cast<CuteQWindowsFontDatabaseCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsFontDatabase::supportsColrv0Fonts();
  }

  //  bool QWindowsFontDatabase::populateFamilyAliases(const QString
  //      &missingFamily)
  bool populateFamilyAliases(const QString &missingFamily) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall4 call = reinterpret_cast<CuteQWindowsFontDatabaseCall4>(taken[4]);
      bool given = call(this, &missingFamily, &handled);
      if (handled) return given;
    }
    return QWindowsFontDatabase::populateFamilyAliases(missingFamily);
  }

  //  void QWindowsFontDatabase::populateFamily(const QString &familyName)
  void populateFamily(const QString &familyName) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall5 call = reinterpret_cast<CuteQWindowsFontDatabaseCall5>(taken[5]);
      call(this, &familyName, &handled);
      if (handled) return;
    }
    QWindowsFontDatabase::populateFamily(familyName);
  }

  //  void QWindowsFontDatabase::invalidate()
  void invalidate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall6 call = reinterpret_cast<CuteQWindowsFontDatabaseCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsFontDatabase::invalidate();
  }

  //  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
  //      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
  QFontEngineMulti *fontEngineMulti(QFontEngine *fontEngine, QFontDatabasePrivate::ExtendedScript script) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall7 call = reinterpret_cast<CuteQWindowsFontDatabaseCall7>(taken[7]);
      void * given = call(this, fontEngine, static_cast<int>(script), &handled);
      if (handled) return static_cast<QFontEngineMulti *>(given);
    }
    return QPlatformFontDatabase::fontEngineMulti(fontEngine, script);
  }

  //  QString QWindowsFontDatabase::fontDir() const
  QString fontDir() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall8 call = reinterpret_cast<CuteQWindowsFontDatabaseCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QWindowsFontDatabase::fontDir();
  }

  //  QFont QWindowsFontDatabase::defaultFont() const
  QFont defaultFont() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall9 call = reinterpret_cast<CuteQWindowsFontDatabaseCall9>(taken[9]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsFontDatabase::defaultFont();
  }

  //  bool QWindowsFontDatabase::isPrivateFontFamily(const QString &family)
  //      const
  bool isPrivateFontFamily(const QString &family) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall10 call = reinterpret_cast<CuteQWindowsFontDatabaseCall10>(taken[10]);
      bool given = call(this, &family, &handled);
      if (handled) return given;
    }
    return QWindowsFontDatabase::isPrivateFontFamily(family);
  }

  //  QString QPlatformFontDatabase::resolveFontFamilyAlias(const QString
  //      &family) const
  QString resolveFontFamilyAlias(const QString &family) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall11 call = reinterpret_cast<CuteQWindowsFontDatabaseCall11>(taken[11]);
      QString * given = call(this, &family, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformFontDatabase::resolveFontFamilyAlias(family);
  }

  //  bool QWindowsFontDatabase::fontsAlwaysScalable() const
  bool fontsAlwaysScalable() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQWindowsFontDatabaseCall12 call = reinterpret_cast<CuteQWindowsFontDatabaseCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsFontDatabase::fontsAlwaysScalable();
  }
};

//  QWindowsFontDatabase::QWindowsFontDatabase()
extern "C" Q_DECL_EXPORT
QWindowsFontDatabase *ritual_ZN20QWindowsFontDatabaseC1Ev() {
  return new CuteQWindowsFontDatabase();
}

//  QWindowsFontDatabase::~QWindowsFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabaseD1Ev(QWindowsFontDatabase *self) {
  delete self;
}

//  void QWindowsFontDatabase::ensureFamilyPopulated(const QString
//      &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase21ensureFamilyPopulatedERK7QString(
    QWindowsFontDatabase *self,
    const QString *familyName) {
  self->ensureFamilyPopulated(*familyName);
}

//  void QWindowsFontDatabase::removeApplicationFonts()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase22removeApplicationFontsEv(
    QWindowsFontDatabase *self) {
  self->removeApplicationFonts();
}

//  QFontEngine *QWindowsFontDatabase::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN20QWindowsFontDatabase10fontEngineERK8QFontDefPv(
    QWindowsFontDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->fontEngine(*fontDef, handle);
}

//  QStringList QWindowsFontDatabase::fallbacksForFamily(const QString
//      &family, QFont::Style style, QFont::StyleHint styleHint,
//      QFontDatabasePrivate::ExtendedScript script) const
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZNK20QWindowsFontDatabase18fallbacksForFamilyERK7QStringN5QFont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScriptE(
    const QWindowsFontDatabase *self,
    const QString *family,
    QFont::Style style,
    QFont::StyleHint styleHint,
    QFontDatabasePrivate::ExtendedScript script) {
  return new QStringList(self->fallbacksForFamily(*family, style, styleHint, script));
}

//  QStringList QWindowsFontDatabase::addApplicationFont(const QByteArray
//      &fontData, const QString &fileName,
//      QFontDatabasePrivate::ApplicationFont *applicationFont)
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZN20QWindowsFontDatabase18addApplicationFontERK10QByteArrayRK7QStringPN20QFontDatabasePrivate15ApplicationFontE(
    QWindowsFontDatabase *self,
    const QByteArray *fontData,
    const QString *fileName,
    QFontDatabasePrivate::ApplicationFont *applicationFont) {
  return new QStringList(self->addApplicationFont(*fontData, *fileName, applicationFont));
}

//  void QWindowsFontDatabase::releaseHandle(void *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase13releaseHandleEPv(
    QWindowsFontDatabase *self,
    void *handle) {
  self->releaseHandle(handle);
}

//  void QWindowsFontDatabase::derefUniqueFont(const QString &uniqueFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase15derefUniqueFontERK7QString(
    QWindowsFontDatabase *self,
    const QString *uniqueFont) {
  self->derefUniqueFont(*uniqueFont);
}

//  void QWindowsFontDatabase::refUniqueFont(const QString &uniqueFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase13refUniqueFontERK7QString(
    QWindowsFontDatabase *self,
    const QString *uniqueFont) {
  self->refUniqueFont(*uniqueFont);
}

//  qreal QWindowsFontDatabase::fontSmoothingGamma()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QWindowsFontDatabase18fontSmoothingGammaEv() {
  return QWindowsFontDatabase::fontSmoothingGamma();
}

//  void QWindowsFontDatabase::setFontOptions(unsigned options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase14setFontOptionsEj(unsigned options) {
  QWindowsFontDatabase::setFontOptions(options);
}

//  unsigned QWindowsFontDatabase::fontOptions()
extern "C" Q_DECL_EXPORT
unsigned ritual_ZN20QWindowsFontDatabase11fontOptionsEv() {
  return QWindowsFontDatabase::fontOptions();
}

//  void QWindowsFontDatabase::addDefaultEUDCFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase18addDefaultEUDCFontEv(
    QWindowsFontDatabase *self) {
  self->addDefaultEUDCFont();
}

//  void QWindowsFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase20populateFontDatabaseEv(
    QWindowsFontDatabase *self) {
  self->populateFontDatabase();
}

//  QFontEngine *QWindowsFontDatabase::fontEngine(const QByteArray &fontData,
//      qreal pixelSize, QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN20QWindowsFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->fontEngine(*fontData, pixelSize, hintingPreference);
}

//  bool QWindowsFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWindowsFontDatabase19supportsColrv0FontsEv(
    const QWindowsFontDatabase *self) {
  return self->supportsColrv0Fonts();
}

//  bool QWindowsFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QWindowsFontDatabase21populateFamilyAliasesERK7QString(
    QWindowsFontDatabase *self,
    const QString *missingFamily) {
  return self->populateFamilyAliases(*missingFamily);
}

//  void QWindowsFontDatabase::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase14populateFamilyERK7QString(
    QWindowsFontDatabase *self,
    const QString *familyName) {
  self->populateFamily(*familyName);
}

//  void QWindowsFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase10invalidateEv(
    QWindowsFontDatabase *self) {
  self->invalidate();
}

//  QString QWindowsFontDatabase::fontDir() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QWindowsFontDatabase7fontDirEv(
    const QWindowsFontDatabase *self) {
  return new QString(self->fontDir());
}

//  QFont QWindowsFontDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK20QWindowsFontDatabase11defaultFontEv(
    const QWindowsFontDatabase *self) {
  return new QFont(self->defaultFont());
}

//  bool QWindowsFontDatabase::isPrivateFontFamily(const QString &family)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWindowsFontDatabase19isPrivateFontFamilyERK7QString(
    const QWindowsFontDatabase *self,
    const QString *family) {
  return self->isPrivateFontFamily(*family);
}

//  bool QWindowsFontDatabase::fontsAlwaysScalable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWindowsFontDatabase19fontsAlwaysScalableEv(
    const QWindowsFontDatabase *self) {
  return self->fontsAlwaysScalable();
}

//  a Python function taken by a CuteQWindowsFontDatabase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsFontDatabase(
    QWindowsFontDatabase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsFontDatabase *>(self)->take(key, call);
}

//  void QWindowsFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWindowsFontDatabase20populateFontDatabaseEv(
    QWindowsFontDatabase *self) {
  self->QWindowsFontDatabase::populateFontDatabase();
}

//  QFontEngine *QWindowsFontDatabase::fontEngine(const QByteArray &fontData,
//      qreal pixelSize, QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN20QWindowsFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->QWindowsFontDatabase::fontEngine(*fontData, pixelSize, hintingPreference);
}

//  bool QWindowsFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QWindowsFontDatabase19supportsColrv0FontsEv(
    const QWindowsFontDatabase *self) {
  return self->QWindowsFontDatabase::supportsColrv0Fonts();
}

//  bool QWindowsFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QWindowsFontDatabase21populateFamilyAliasesERK7QString(
    QWindowsFontDatabase *self,
    const QString *missingFamily) {
  return self->QWindowsFontDatabase::populateFamilyAliases(*missingFamily);
}

//  void QWindowsFontDatabase::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWindowsFontDatabase14populateFamilyERK7QString(
    QWindowsFontDatabase *self,
    const QString *familyName) {
  self->QWindowsFontDatabase::populateFamily(*familyName);
}

//  void QWindowsFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWindowsFontDatabase10invalidateEv(
    QWindowsFontDatabase *self) {
  self->QWindowsFontDatabase::invalidate();
}

//  QString QWindowsFontDatabase::fontDir() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QWindowsFontDatabase7fontDirEv(
    const QWindowsFontDatabase *self) {
  return new QString(self->QWindowsFontDatabase::fontDir());
}

//  QFont QWindowsFontDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK20QWindowsFontDatabase11defaultFontEv(
    const QWindowsFontDatabase *self) {
  return new QFont(self->QWindowsFontDatabase::defaultFont());
}

//  bool QWindowsFontDatabase::isPrivateFontFamily(const QString &family)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QWindowsFontDatabase19isPrivateFontFamilyERK7QString(
    const QWindowsFontDatabase *self,
    const QString *family) {
  return self->QWindowsFontDatabase::isPrivateFontFamily(*family);
}

//  bool QWindowsFontDatabase::fontsAlwaysScalable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QWindowsFontDatabase19fontsAlwaysScalableEv(
    const QWindowsFontDatabase *self) {
  return self->QWindowsFontDatabase::fontsAlwaysScalable();
}

#endif  // defined(Q_OS_WIN)
