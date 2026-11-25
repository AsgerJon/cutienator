//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsdirectwritefontdatabase_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
//  DirectWrite's interfaces and a 'void *' are passed as addresses, its
//  enums as numbers. Not written: 'localeString', taking a 'wchar_t []',
//  and the template 'collectAdditionalNames'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(directwrite3)
#include <QtGui/6.12.0/QtGui/private/qwindowsdirectwritefontdatabase_p.h>
#include <QtGui/qfont.h>
#include <QtCore/qstringlist.h>
#include <cstring>

//  A QWindowsDirectWriteFontDatabase that Python can take functions over in. Every
//  QWindowsDirectWriteFontDatabase Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQWindowsDirectWriteFontDatabaseCall0)(const void *, int *);
typedef void * (*CuteQWindowsDirectWriteFontDatabaseCall1)(const void *, const QByteArray *, qreal, int, int *);
typedef bool (*CuteQWindowsDirectWriteFontDatabaseCall2)(const void *, int *);
typedef bool (*CuteQWindowsDirectWriteFontDatabaseCall3)(const void *, int *);
typedef bool (*CuteQWindowsDirectWriteFontDatabaseCall4)(const void *, const QString *, int *);
typedef void (*CuteQWindowsDirectWriteFontDatabaseCall5)(const void *, const QString *, int *);
typedef void (*CuteQWindowsDirectWriteFontDatabaseCall6)(const void *, int *);
typedef void * (*CuteQWindowsDirectWriteFontDatabaseCall7)(const void *, QFontEngine *, int, int *);
typedef QString * (*CuteQWindowsDirectWriteFontDatabaseCall8)(const void *, int *);
typedef const QFont * (*CuteQWindowsDirectWriteFontDatabaseCall9)(const void *, int *);
typedef bool (*CuteQWindowsDirectWriteFontDatabaseCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQWindowsDirectWriteFontDatabaseCall11)(const void *, const QString *, int *);
typedef bool (*CuteQWindowsDirectWriteFontDatabaseCall12)(const void *, int *);
class CuteQWindowsDirectWriteFontDatabase : public QWindowsDirectWriteFontDatabase {
public:
  using QWindowsDirectWriteFontDatabase::QWindowsDirectWriteFontDatabase;
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

  //  void QWindowsDirectWriteFontDatabase::populateFontDatabase()
  void populateFontDatabase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall0 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsDirectWriteFontDatabase::populateFontDatabase();
  }

  //  QFontEngine *QWindowsDirectWriteFontDatabase::fontEngine(const
  //      QByteArray &fontData, qreal pixelSize, QFont::HintingPreference
  //      hintingPreference)
  QFontEngine *fontEngine(const QByteArray &fontData, qreal pixelSize, QFont::HintingPreference hintingPreference) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall1 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall1>(taken[1]);
      void * given = call(this, &fontData, pixelSize, static_cast<int>(hintingPreference), &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QWindowsDirectWriteFontDatabase::fontEngine(fontData, pixelSize, hintingPreference);
  }

  //  bool
  //      QWindowsDirectWriteFontDatabase::supportsVariableApplicationFonts()
  //      const
  bool supportsVariableApplicationFonts() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall2 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsDirectWriteFontDatabase::supportsVariableApplicationFonts();
  }

  //  bool QWindowsFontDatabase::supportsColrv0Fonts() const
  bool supportsColrv0Fonts() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall3 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsFontDatabase::supportsColrv0Fonts();
  }

  //  bool QWindowsDirectWriteFontDatabase::populateFamilyAliases(const
  //      QString &missingFamily)
  bool populateFamilyAliases(const QString &missingFamily) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall4 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall4>(taken[4]);
      bool given = call(this, &missingFamily, &handled);
      if (handled) return given;
    }
    return QWindowsDirectWriteFontDatabase::populateFamilyAliases(missingFamily);
  }

  //  void QWindowsDirectWriteFontDatabase::populateFamily(const QString
  //      &familyName)
  void populateFamily(const QString &familyName) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall5 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall5>(taken[5]);
      call(this, &familyName, &handled);
      if (handled) return;
    }
    QWindowsDirectWriteFontDatabase::populateFamily(familyName);
  }

  //  void QWindowsDirectWriteFontDatabase::invalidate()
  void invalidate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall6 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsDirectWriteFontDatabase::invalidate();
  }

  //  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
  //      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
  QFontEngineMulti *fontEngineMulti(QFontEngine *fontEngine, QFontDatabasePrivate::ExtendedScript script) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall7 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall7>(taken[7]);
      void * given = call(this, fontEngine, static_cast<int>(script), &handled);
      if (handled) return static_cast<QFontEngineMulti *>(given);
    }
    return QPlatformFontDatabase::fontEngineMulti(fontEngine, script);
  }

  //  QString QWindowsFontDatabase::fontDir() const
  QString fontDir() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall8 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall8>(taken[8]);
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
      CuteQWindowsDirectWriteFontDatabaseCall9 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall9>(taken[9]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsFontDatabase::defaultFont();
  }

  //  bool QWindowsDirectWriteFontDatabase::isPrivateFontFamily(const QString
  //      &family) const
  bool isPrivateFontFamily(const QString &family) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall10 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall10>(taken[10]);
      bool given = call(this, &family, &handled);
      if (handled) return given;
    }
    return QWindowsDirectWriteFontDatabase::isPrivateFontFamily(family);
  }

  //  QString QPlatformFontDatabase::resolveFontFamilyAlias(const QString
  //      &family) const
  QString resolveFontFamilyAlias(const QString &family) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWindowsDirectWriteFontDatabaseCall11 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall11>(taken[11]);
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
      CuteQWindowsDirectWriteFontDatabaseCall12 call = reinterpret_cast<CuteQWindowsDirectWriteFontDatabaseCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsFontDatabase::fontsAlwaysScalable();
  }
};

//  QWindowsDirectWriteFontDatabase::QWindowsDirectWriteFontDatabase()
extern "C" Q_DECL_EXPORT
QWindowsDirectWriteFontDatabase *ritual_ZN31QWindowsDirectWriteFontDatabaseC1Ev() {
  return new CuteQWindowsDirectWriteFontDatabase();
}

//  QWindowsDirectWriteFontDatabase::~QWindowsDirectWriteFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsDirectWriteFontDatabaseD1Ev(
    QWindowsDirectWriteFontDatabase *self) {
  delete self;
}

//  QFontEngine *QWindowsDirectWriteFontDatabase::fontEngine(const QFontDef
//      &fontDef, void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN31QWindowsDirectWriteFontDatabase10fontEngineERK8QFontDefPv(
    QWindowsDirectWriteFontDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->fontEngine(*fontDef, handle);
}

//  QStringList QWindowsDirectWriteFontDatabase::fallbacksForFamily(const
//      QString &family, QFont::Style style, QFont::StyleHint styleHint,
//      QFontDatabasePrivate::ExtendedScript script) const
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZNK31QWindowsDirectWriteFontDatabase18fallbacksForFamilyERK7QStringN5QFont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScriptE(
    const QWindowsDirectWriteFontDatabase *self,
    const QString *family,
    QFont::Style style,
    QFont::StyleHint styleHint,
    QFontDatabasePrivate::ExtendedScript script) {
  return new QStringList(self->fallbacksForFamily(*family, style, styleHint, script));
}

//  QStringList QWindowsDirectWriteFontDatabase::addApplicationFont(const
//      QByteArray &fontData, const QString &fileName,
//      QFontDatabasePrivate::ApplicationFont *applicationFont)
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZN31QWindowsDirectWriteFontDatabase18addApplicationFontERK10QByteArrayRK7QStringPN20QFontDatabasePrivate15ApplicationFontE(
    QWindowsDirectWriteFontDatabase *self,
    const QByteArray *fontData,
    const QString *fileName,
    QFontDatabasePrivate::ApplicationFont *applicationFont) {
  return new QStringList(self->addApplicationFont(*fontData, *fileName, applicationFont));
}

//  void QWindowsDirectWriteFontDatabase::registerBitmapFont(const QString
//      &bitmapFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsDirectWriteFontDatabase18registerBitmapFontERK7QString(
    QWindowsDirectWriteFontDatabase *self,
    const QString *bitmapFont) {
  self->registerBitmapFont(*bitmapFont);
}

//  bool QWindowsDirectWriteFontDatabase::hasPopulatedFont(const QString
//      &fontFamily) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QWindowsDirectWriteFontDatabase16hasPopulatedFontERK7QString(
    const QWindowsDirectWriteFontDatabase *self,
    const QString *fontFamily) {
  return self->hasPopulatedFont(*fontFamily);
}

//  QFont::Stretch QWindowsDirectWriteFontDatabase::fromDirectWriteStretch(DW
//      RITE_FONT_STRETCH stretch)
extern "C" Q_DECL_EXPORT
QFont::Stretch ritual_ZN31QWindowsDirectWriteFontDatabase22fromDirectWriteStretchE19DWRITE_FONT_STRETCH(
    DWRITE_FONT_STRETCH stretch) {
  return QWindowsDirectWriteFontDatabase::fromDirectWriteStretch(stretch);
}

//  QFont::Weight
//      QWindowsDirectWriteFontDatabase::fromDirectWriteWeight(DWRITE_FONT_WE
//      IGHT weight)
extern "C" Q_DECL_EXPORT
QFont::Weight ritual_ZN31QWindowsDirectWriteFontDatabase21fromDirectWriteWeightE18DWRITE_FONT_WEIGHT(
    DWRITE_FONT_WEIGHT weight) {
  return QWindowsDirectWriteFontDatabase::fromDirectWriteWeight(weight);
}

//  QFont::Style
//      QWindowsDirectWriteFontDatabase::fromDirectWriteStyle(DWRITE_FONT_STY
//      LE style)
extern "C" Q_DECL_EXPORT
QFont::Style ritual_ZN31QWindowsDirectWriteFontDatabase20fromDirectWriteStyleE17DWRITE_FONT_STYLE(
    DWRITE_FONT_STYLE style) {
  return QWindowsDirectWriteFontDatabase::fromDirectWriteStyle(style);
}

//  QSupportedWritingSystems
//      QWindowsDirectWriteFontDatabase::supportedWritingSystems(IDWriteFontF
//      ace *face) const
extern "C" Q_DECL_EXPORT
QSupportedWritingSystems *ritual_ZNK31QWindowsDirectWriteFontDatabase23supportedWritingSystemsEP15IDWriteFontFace(
    const QWindowsDirectWriteFontDatabase *self,
    IDWriteFontFace *face) {
  return new QSupportedWritingSystems(self->supportedWritingSystems(face));
}

//  void QWindowsDirectWriteFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsDirectWriteFontDatabase20populateFontDatabaseEv(
    QWindowsDirectWriteFontDatabase *self) {
  self->populateFontDatabase();
}

//  QFontEngine *QWindowsDirectWriteFontDatabase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN31QWindowsDirectWriteFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsDirectWriteFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->fontEngine(*fontData, pixelSize, hintingPreference);
}

//  bool QWindowsDirectWriteFontDatabase::supportsVariableApplicationFonts()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QWindowsDirectWriteFontDatabase32supportsVariableApplicationFontsEv(
    const QWindowsDirectWriteFontDatabase *self) {
  return self->supportsVariableApplicationFonts();
}

//  bool QWindowsDirectWriteFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QWindowsDirectWriteFontDatabase21populateFamilyAliasesERK7QString(
    QWindowsDirectWriteFontDatabase *self,
    const QString *missingFamily) {
  return self->populateFamilyAliases(*missingFamily);
}

//  void QWindowsDirectWriteFontDatabase::populateFamily(const QString
//      &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsDirectWriteFontDatabase14populateFamilyERK7QString(
    QWindowsDirectWriteFontDatabase *self,
    const QString *familyName) {
  self->populateFamily(*familyName);
}

//  void QWindowsDirectWriteFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsDirectWriteFontDatabase10invalidateEv(
    QWindowsDirectWriteFontDatabase *self) {
  self->invalidate();
}

//  bool QWindowsDirectWriteFontDatabase::isPrivateFontFamily(const QString
//      &family) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QWindowsDirectWriteFontDatabase19isPrivateFontFamilyERK7QString(
    const QWindowsDirectWriteFontDatabase *self,
    const QString *family) {
  return self->isPrivateFontFamily(*family);
}

//  a Python function taken by a CuteQWindowsDirectWriteFontDatabase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsDirectWriteFontDatabase(
    QWindowsDirectWriteFontDatabase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsDirectWriteFontDatabase *>(self)->take(key, call);
}

//  void QWindowsDirectWriteFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QWindowsDirectWriteFontDatabase20populateFontDatabaseEv(
    QWindowsDirectWriteFontDatabase *self) {
  self->QWindowsDirectWriteFontDatabase::populateFontDatabase();
}

//  QFontEngine *QWindowsDirectWriteFontDatabase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN31QWindowsDirectWriteFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsDirectWriteFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->QWindowsDirectWriteFontDatabase::fontEngine(*fontData, pixelSize, hintingPreference);
}

//  bool QWindowsDirectWriteFontDatabase::supportsVariableApplicationFonts()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QWindowsDirectWriteFontDatabase32supportsVariableApplicationFontsEv(
    const QWindowsDirectWriteFontDatabase *self) {
  return self->QWindowsDirectWriteFontDatabase::supportsVariableApplicationFonts();
}

//  bool QWindowsDirectWriteFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN31QWindowsDirectWriteFontDatabase21populateFamilyAliasesERK7QString(
    QWindowsDirectWriteFontDatabase *self,
    const QString *missingFamily) {
  return self->QWindowsDirectWriteFontDatabase::populateFamilyAliases(*missingFamily);
}

//  void QWindowsDirectWriteFontDatabase::populateFamily(const QString
//      &familyName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QWindowsDirectWriteFontDatabase14populateFamilyERK7QString(
    QWindowsDirectWriteFontDatabase *self,
    const QString *familyName) {
  self->QWindowsDirectWriteFontDatabase::populateFamily(*familyName);
}

//  void QWindowsDirectWriteFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QWindowsDirectWriteFontDatabase10invalidateEv(
    QWindowsDirectWriteFontDatabase *self) {
  self->QWindowsDirectWriteFontDatabase::invalidate();
}

//  bool QWindowsDirectWriteFontDatabase::isPrivateFontFamily(const QString
//      &family) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QWindowsDirectWriteFontDatabase19isPrivateFontFamilyERK7QString(
    const QWindowsDirectWriteFontDatabase *self,
    const QString *family) {
  return self->QWindowsDirectWriteFontDatabase::isPrivateFontFamily(*family);
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(directwrite3)
