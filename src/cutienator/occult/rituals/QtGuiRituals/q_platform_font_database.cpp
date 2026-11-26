//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformfontdatabase.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformfontdatabase.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A QPlatformFontDatabase that Python can take functions over in. Every QPlatformFontDatabase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformFontDatabaseCall0)(const void *, int *);
typedef bool (*CuteQPlatformFontDatabaseCall1)(const void *, const QString *, int *);
typedef void (*CuteQPlatformFontDatabaseCall2)(const void *, const QString *, int *);
typedef void (*CuteQPlatformFontDatabaseCall3)(const void *, int *);
typedef void * (*CuteQPlatformFontDatabaseCall4)(const void *, const QFontDef *, void *, int *);
typedef void * (*CuteQPlatformFontDatabaseCall5)(const void *, const QByteArray *, qreal, int, int *);
typedef void * (*CuteQPlatformFontDatabaseCall6)(const void *, QFontEngine *, int, int *);
typedef void (*CuteQPlatformFontDatabaseCall7)(const void *, void *, int *);
typedef QString * (*CuteQPlatformFontDatabaseCall8)(const void *, int *);
typedef const QFont * (*CuteQPlatformFontDatabaseCall9)(const void *, int *);
typedef bool (*CuteQPlatformFontDatabaseCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQPlatformFontDatabaseCall11)(const void *, const QString *, int *);
typedef bool (*CuteQPlatformFontDatabaseCall12)(const void *, int *);
typedef bool (*CuteQPlatformFontDatabaseCall13)(const void *, int *);
typedef bool (*CuteQPlatformFontDatabaseCall14)(const void *, int *);
class CuteQPlatformFontDatabase : public QPlatformFontDatabase {
public:
  using QPlatformFontDatabase::QPlatformFontDatabase;
  CuteQPlatformFontDatabase(const QPlatformFontDatabase & other) : QPlatformFontDatabase(other) {}
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase20populateFontDatabaseEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase14populateFamilyERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10invalidateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10fontEngineERK8QFontDefPv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase13releaseHandleEPv")) {
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
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase32supportsVariableApplicationFontsEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv")) {
      taken[14] = call;
      return true;
    }
    return false;
  }

  //  void QPlatformFontDatabase::populateFontDatabase()
  void populateFontDatabase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall0 call = reinterpret_cast<CuteQPlatformFontDatabaseCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::populateFontDatabase();
  }

  //  bool QPlatformFontDatabase::populateFamilyAliases(const QString
  //      &missingFamily)
  bool populateFamilyAliases(const QString &missingFamily) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall1 call = reinterpret_cast<CuteQPlatformFontDatabaseCall1>(taken[1]);
      bool given = call(this, &missingFamily, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::populateFamilyAliases(missingFamily);
  }

  //  void QPlatformFontDatabase::populateFamily(const QString &familyName)
  void populateFamily(const QString &familyName) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall2 call = reinterpret_cast<CuteQPlatformFontDatabaseCall2>(taken[2]);
      call(this, &familyName, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::populateFamily(familyName);
  }

  //  void QPlatformFontDatabase::invalidate()
  void invalidate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall3 call = reinterpret_cast<CuteQPlatformFontDatabaseCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::invalidate();
  }

  //  QFontEngine *QPlatformFontDatabase::fontEngine(const QFontDef
  //      &fontDef, void *handle)
  QFontEngine *fontEngine(const QFontDef &fontDef, void *handle) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall4 call = reinterpret_cast<CuteQPlatformFontDatabaseCall4>(taken[4]);
      void * given = call(this, &fontDef, handle, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QPlatformFontDatabase::fontEngine(fontDef, handle);
  }

  //  QFontEngine *QPlatformFontDatabase::fontEngine(const QByteArray
  //      &fontData, qreal pixelSize, QFont::HintingPreference
  //      hintingPreference)
  QFontEngine *fontEngine(
      const QByteArray &fontData,
      qreal pixelSize,
      QFont::HintingPreference hintingPreference) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall5 call = reinterpret_cast<CuteQPlatformFontDatabaseCall5>(taken[5]);
      void * given = call(this, &fontData, pixelSize, static_cast<int>(hintingPreference), &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QPlatformFontDatabase::fontEngine(fontData, pixelSize, hintingPreference);
  }

  //  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
  //      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
  QFontEngineMulti *fontEngineMulti(
      QFontEngine *fontEngine,
      QFontDatabasePrivate::ExtendedScript script) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall6 call = reinterpret_cast<CuteQPlatformFontDatabaseCall6>(taken[6]);
      void * given = call(this, fontEngine, static_cast<int>(script), &handled);
      if (handled) return static_cast<QFontEngineMulti *>(given);
    }
    return QPlatformFontDatabase::fontEngineMulti(fontEngine, script);
  }

  //  void QPlatformFontDatabase::releaseHandle(void *handle)
  void releaseHandle(void *handle) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall7 call = reinterpret_cast<CuteQPlatformFontDatabaseCall7>(taken[7]);
      call(this, handle, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::releaseHandle(handle);
  }

  //  QString QPlatformFontDatabase::fontDir() const
  QString fontDir() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall8 call = reinterpret_cast<CuteQPlatformFontDatabaseCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformFontDatabase::fontDir();
  }

  //  QFont QPlatformFontDatabase::defaultFont() const
  QFont defaultFont() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall9 call = reinterpret_cast<CuteQPlatformFontDatabaseCall9>(taken[9]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformFontDatabase::defaultFont();
  }

  //  bool QPlatformFontDatabase::isPrivateFontFamily(const QString
  //      &family) const
  bool isPrivateFontFamily(const QString &family) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall10 call = reinterpret_cast<CuteQPlatformFontDatabaseCall10>(taken[10]);
      bool given = call(this, &family, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::isPrivateFontFamily(family);
  }

  //  QString QPlatformFontDatabase::resolveFontFamilyAlias(const QString
  //      &family) const
  QString resolveFontFamilyAlias(const QString &family) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall11 call = reinterpret_cast<CuteQPlatformFontDatabaseCall11>(taken[11]);
      QString * given = call(this, &family, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformFontDatabase::resolveFontFamilyAlias(family);
  }

  //  bool QPlatformFontDatabase::fontsAlwaysScalable() const
  bool fontsAlwaysScalable() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall12 call = reinterpret_cast<CuteQPlatformFontDatabaseCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::fontsAlwaysScalable();
  }

  //  bool QPlatformFontDatabase::supportsVariableApplicationFonts() const
  bool supportsVariableApplicationFonts() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall13 call = reinterpret_cast<CuteQPlatformFontDatabaseCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::supportsVariableApplicationFonts();
  }

  //  bool QPlatformFontDatabase::supportsColrv0Fonts() const
  bool supportsColrv0Fonts() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformFontDatabaseCall14 call = reinterpret_cast<CuteQPlatformFontDatabaseCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::supportsColrv0Fonts();
  }
};

//  QPlatformFontDatabase::~QPlatformFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabaseD1Ev(QPlatformFontDatabase *self) {
  delete self;
}

//  void QPlatformFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase20populateFontDatabaseEv(
    QPlatformFontDatabase *self) {
  self->populateFontDatabase();
}

//  bool QPlatformFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString(
    QPlatformFontDatabase *self,
    const QString *missingFamily) {
  return self->populateFamilyAliases(*missingFamily);
}

//  void QPlatformFontDatabase::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase14populateFamilyERK7QString(
    QPlatformFontDatabase *self,
    const QString *familyName) {
  self->populateFamily(*familyName);
}

//  void QPlatformFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase10invalidateEv(
    QPlatformFontDatabase *self) {
  self->invalidate();
}

//  QStringList QPlatformFontDatabase::fallbacksForFamily(const QString
//      &family, QFont::Style style, QFont::StyleHint styleHint,
//      QFontDatabasePrivate::ExtendedScript script) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QPlatformFontDatabase18fallbacksForFamilyERK7QStringN5QFont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScriptE(
    const QPlatformFontDatabase *self,
    const QString *family,
    QFont::Style style,
    QFont::StyleHint styleHint,
    QFontDatabasePrivate::ExtendedScript script) {
  return new QList<QString>(
      self->fallbacksForFamily(
          *family,
          style,
          styleHint,
          script));
}

//  QStringList QPlatformFontDatabase::addApplicationFont(const QByteArray
//      &fontData, const QString &fileName,
//      QFontDatabasePrivate::ApplicationFont *font)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QPlatformFontDatabase18addApplicationFontERK10QByteArrayRK7QStringPN20QFontDatabasePrivate15ApplicationFontE(
    QPlatformFontDatabase *self,
    const QByteArray *fontData,
    const QString *fileName,
    QFontDatabasePrivate::ApplicationFont *font) {
  return new QList<QString>(
      self->addApplicationFont(
          *fontData,
          *fileName,
          font));
}

//  QFontEngine *QPlatformFontDatabase::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN21QPlatformFontDatabase10fontEngineERK8QFontDefPv(
    QPlatformFontDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->fontEngine(*fontDef, handle);
}

//  QFontEngine *QPlatformFontDatabase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN21QPlatformFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QPlatformFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->fontEngine(*fontData, pixelSize, hintingPreference);
}

//  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
//      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
extern "C" Q_DECL_EXPORT
QFontEngineMulti *ritual_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE(
    QPlatformFontDatabase *self,
    QFontEngine *fontEngine,
    QFontDatabasePrivate::ExtendedScript script) {
  return self->fontEngineMulti(fontEngine, script);
}

//  void QPlatformFontDatabase::releaseHandle(void *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase13releaseHandleEPv(
    QPlatformFontDatabase *self,
    void *handle) {
  self->releaseHandle(handle);
}

//  QString QPlatformFontDatabase::fontDir() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QPlatformFontDatabase7fontDirEv(
    const QPlatformFontDatabase *self) {
  return new QString(self->fontDir());
}

//  QFont QPlatformFontDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK21QPlatformFontDatabase11defaultFontEv(
    const QPlatformFontDatabase *self) {
  return new QFont(self->defaultFont());
}

//  bool QPlatformFontDatabase::isPrivateFontFamily(const QString &family)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QString(
    const QPlatformFontDatabase *self,
    const QString *family) {
  return self->isPrivateFontFamily(*family);
}

//  QString QPlatformFontDatabase::resolveFontFamilyAlias(const QString
//      &family) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK7QString(
    const QPlatformFontDatabase *self,
    const QString *family) {
  return new QString(self->resolveFontFamilyAlias(*family));
}

//  bool QPlatformFontDatabase::fontsAlwaysScalable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv(
    const QPlatformFontDatabase *self) {
  return self->fontsAlwaysScalable();
}

//  QList<int> QPlatformFontDatabase::standardSizes() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK21QPlatformFontDatabase13standardSizesEv(
    const QPlatformFontDatabase *self) {
  return new QList<int>(self->standardSizes());
}

//  bool QPlatformFontDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformFontDatabase32supportsVariableApplicationFontsEv(
    const QPlatformFontDatabase *self) {
  return self->supportsVariableApplicationFonts();
}

//  bool QPlatformFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv(
    const QPlatformFontDatabase *self) {
  return self->supportsColrv0Fonts();
}

//  QSupportedWritingSystems
//      QPlatformFontDatabase::writingSystemsFromTrueTypeBits(quint32
//      *unicodeRange, quint32 *codePageRange)
extern "C" Q_DECL_EXPORT
QSupportedWritingSystems *ritual_ZN21QPlatformFontDatabase30writingSystemsFromTrueTypeBitsEPjS0_(
    quint32 *unicodeRange,
    quint32 *codePageRange) {
  return new QSupportedWritingSystems(
      QPlatformFontDatabase::writingSystemsFromTrueTypeBits(
          unicodeRange,
          codePageRange));
}

//  QSupportedWritingSystems
//      QPlatformFontDatabase::writingSystemsFromOS2Table(const char
//      *os2Table, size_t length)
extern "C" Q_DECL_EXPORT
QSupportedWritingSystems *ritual_ZN21QPlatformFontDatabase26writingSystemsFromOS2TableEPKcm(
    const char *os2Table,
    size_t length) {
  return new QSupportedWritingSystems(
      QPlatformFontDatabase::writingSystemsFromOS2Table(
          os2Table,
          length));
}

//  void QPlatformFontDatabase::registerFont(const QString &familyname, const
//      QString &stylename, const QString &foundryname, QFont::Weight weight,
//      QFont::Style style, QFont::Stretch stretch, bool antialiased, bool
//      scalable, int pixelSize, bool fixedPitch, bool colorFont, const
//      QSupportedWritingSystems &writingSystems, void *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase12registerFontERK7QStringS2_S2_N5QFont6WeightENS3_5StyleENS3_7StretchEbbibbRK24QSupportedWritingSystemsPv(
    const QString *familyname,
    const QString *stylename,
    const QString *foundryname,
    QFont::Weight weight,
    QFont::Style style,
    QFont::Stretch stretch,
    bool antialiased,
    bool scalable,
    int pixelSize,
    bool fixedPitch,
    bool colorFont,
    const QSupportedWritingSystems *writingSystems,
    void *handle) {
  QPlatformFontDatabase::registerFont(
      *familyname,
      *stylename,
      *foundryname,
      weight,
      style,
      stretch,
      antialiased,
      scalable,
      pixelSize,
      fixedPitch,
      colorFont,
      *writingSystems,
      handle);
}

//  void QPlatformFontDatabase::registerFontFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase18registerFontFamilyERK7QString(
    const QString *familyName) {
  QPlatformFontDatabase::registerFontFamily(*familyName);
}

//  void QPlatformFontDatabase::registerAliasToFontFamily(const QString
//      &familyName, const QString &alias)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase25registerAliasToFontFamilyERK7QStringS2_(
    const QString *familyName,
    const QString *alias) {
  QPlatformFontDatabase::registerAliasToFontFamily(*familyName, *alias);
}

//  void QPlatformFontDatabase::repopulateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformFontDatabase22repopulateFontDatabaseEv() {
  QPlatformFontDatabase::repopulateFontDatabase();
}

//  bool QPlatformFontDatabase::isFamilyPopulated(const QString &familyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QPlatformFontDatabase17isFamilyPopulatedERK7QString(
    const QString *familyName) {
  return QPlatformFontDatabase::isFamilyPopulated(*familyName);
}

//  a Python function taken by a CuteQPlatformFontDatabase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformFontDatabase(
    QPlatformFontDatabase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformFontDatabase *>(self)->take(key, call);
}

//  void QPlatformFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformFontDatabase20populateFontDatabaseEv(
    QPlatformFontDatabase *self) {
  self->QPlatformFontDatabase::populateFontDatabase();
}

//  bool QPlatformFontDatabase::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString(
    QPlatformFontDatabase *self,
    const QString *missingFamily) {
  return self->QPlatformFontDatabase::populateFamilyAliases(*missingFamily);
}

//  void QPlatformFontDatabase::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformFontDatabase14populateFamilyERK7QString(
    QPlatformFontDatabase *self,
    const QString *familyName) {
  self->QPlatformFontDatabase::populateFamily(*familyName);
}

//  void QPlatformFontDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformFontDatabase10invalidateEv(
    QPlatformFontDatabase *self) {
  self->QPlatformFontDatabase::invalidate();
}

//  QFontEngine *QPlatformFontDatabase::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN21QPlatformFontDatabase10fontEngineERK8QFontDefPv(
    QPlatformFontDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->QPlatformFontDatabase::fontEngine(*fontDef, handle);
}

//  QFontEngine *QPlatformFontDatabase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN21QPlatformFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QPlatformFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->QPlatformFontDatabase::fontEngine(
      *fontData,
      pixelSize,
      hintingPreference);
}

//  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
//      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
extern "C" Q_DECL_EXPORT
QFontEngineMulti *ritual_own_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE(
    QPlatformFontDatabase *self,
    QFontEngine *fontEngine,
    QFontDatabasePrivate::ExtendedScript script) {
  return self->QPlatformFontDatabase::fontEngineMulti(fontEngine, script);
}

//  void QPlatformFontDatabase::releaseHandle(void *handle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformFontDatabase13releaseHandleEPv(
    QPlatformFontDatabase *self,
    void *handle) {
  self->QPlatformFontDatabase::releaseHandle(handle);
}

//  QString QPlatformFontDatabase::fontDir() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QPlatformFontDatabase7fontDirEv(
    const QPlatformFontDatabase *self) {
  return new QString(self->QPlatformFontDatabase::fontDir());
}

//  QFont QPlatformFontDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK21QPlatformFontDatabase11defaultFontEv(
    const QPlatformFontDatabase *self) {
  return new QFont(self->QPlatformFontDatabase::defaultFont());
}

//  bool QPlatformFontDatabase::isPrivateFontFamily(const QString &family)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QString(
    const QPlatformFontDatabase *self,
    const QString *family) {
  return self->QPlatformFontDatabase::isPrivateFontFamily(*family);
}

//  QString QPlatformFontDatabase::resolveFontFamilyAlias(const QString
//      &family) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK7QString(
    const QPlatformFontDatabase *self,
    const QString *family) {
  return new QString(
      self->QPlatformFontDatabase::resolveFontFamilyAlias(
          *family));
}

//  bool QPlatformFontDatabase::fontsAlwaysScalable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv(
    const QPlatformFontDatabase *self) {
  return self->QPlatformFontDatabase::fontsAlwaysScalable();
}

//  bool QPlatformFontDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformFontDatabase32supportsVariableApplicationFontsEv(
    const QPlatformFontDatabase *self) {
  return self->QPlatformFontDatabase::supportsVariableApplicationFonts();
}

//  bool QPlatformFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv(
    const QPlatformFontDatabase *self) {
  return self->QPlatformFontDatabase::supportsColrv0Fonts();
}

//  a QList<int> a ritual of QPlatformFontDatabase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformFontDatabase__QList_int(QList<int> *self) {
  delete self;
}
