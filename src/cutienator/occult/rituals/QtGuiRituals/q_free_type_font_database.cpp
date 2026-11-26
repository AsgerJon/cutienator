//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfreetypefontdatabase_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(freetype)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfreetypefontdatabase_p.h>
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformfontdatabase.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QFreeTypeFontDatabase that Python can take functions over in. Every QFreeTypeFontDatabase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQFreeTypeFontDatabaseCall0)(const void *, int *);
typedef void * (*CuteQFreeTypeFontDatabaseCall1)(const void *, const QFontDef *, void *, int *);
typedef void * (*CuteQFreeTypeFontDatabaseCall2)(const void *, const QByteArray *, qreal, int, int *);
typedef void (*CuteQFreeTypeFontDatabaseCall3)(const void *, void *, int *);
typedef bool (*CuteQFreeTypeFontDatabaseCall4)(const void *, int *);
typedef bool (*CuteQFreeTypeFontDatabaseCall5)(const void *, int *);
typedef bool (*CuteQFreeTypeFontDatabaseCall6)(const void *, const QString *, int *);
typedef void (*CuteQFreeTypeFontDatabaseCall7)(const void *, const QString *, int *);
typedef void (*CuteQFreeTypeFontDatabaseCall8)(const void *, int *);
typedef void * (*CuteQFreeTypeFontDatabaseCall9)(const void *, QFontEngine *, int, int *);
typedef QString * (*CuteQFreeTypeFontDatabaseCall10)(const void *, int *);
typedef const QFont * (*CuteQFreeTypeFontDatabaseCall11)(const void *, int *);
typedef bool (*CuteQFreeTypeFontDatabaseCall12)(const void *, const QString *, int *);
typedef QString * (*CuteQFreeTypeFontDatabaseCall13)(const void *, const QString *, int *);
typedef bool (*CuteQFreeTypeFontDatabaseCall14)(const void *, int *);
class CuteQFreeTypeFontDatabase : public QFreeTypeFontDatabase {
public:
  using QFreeTypeFontDatabase::QFreeTypeFontDatabase;
  CuteQFreeTypeFontDatabase(const QFreeTypeFontDatabase & other) : QFreeTypeFontDatabase(other) {}
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase20populateFontDatabaseEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10fontEngineERK8QFontDefPv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase13releaseHandleEPv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase32supportsVariableApplicationFontsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase14populateFamilyERK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10invalidateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase7fontDirEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase11defaultFontEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QString")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv")) {
      taken[14] = call;
      return true;
    }
    return false;
  }

  //  void QFreeTypeFontDatabase::populateFontDatabase()
  void populateFontDatabase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall0 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QFreeTypeFontDatabase::populateFontDatabase();
  }

  //  QFontEngine *QFreeTypeFontDatabase::fontEngine(const QFontDef
  //      &fontDef, void *handle)
  QFontEngine *fontEngine(const QFontDef &fontDef, void *handle) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall1 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall1>(taken[1]);
      void * given = call(this, &fontDef, handle, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFreeTypeFontDatabase::fontEngine(fontDef, handle);
  }

  //  QFontEngine *QFreeTypeFontDatabase::fontEngine(const QByteArray
  //      &fontData, qreal pixelSize, QFont::HintingPreference
  //      hintingPreference)
  QFontEngine *fontEngine(
      const QByteArray &fontData,
      qreal pixelSize,
      QFont::HintingPreference hintingPreference) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall2 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall2>(taken[2]);
      void * given = call(this, &fontData, pixelSize, static_cast<int>(hintingPreference), &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFreeTypeFontDatabase::fontEngine(fontData, pixelSize, hintingPreference);
  }

  //  void QFreeTypeFontDatabase::releaseHandle(void *handle)
  void releaseHandle(void *handle) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall3 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall3>(taken[3]);
      call(this, handle, &handled);
      if (handled) return;
    }
    QFreeTypeFontDatabase::releaseHandle(handle);
  }

  //  bool QFreeTypeFontDatabase::supportsVariableApplicationFonts() const
  bool supportsVariableApplicationFonts() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall4 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFreeTypeFontDatabase::supportsVariableApplicationFonts();
  }

  //  bool QFreeTypeFontDatabase::supportsColrv0Fonts() const
  bool supportsColrv0Fonts() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall5 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFreeTypeFontDatabase::supportsColrv0Fonts();
  }

  //  bool QPlatformFontDatabase::populateFamilyAliases(const QString
  //      &missingFamily)
  bool populateFamilyAliases(const QString &missingFamily) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall6 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall6>(taken[6]);
      bool given = call(this, &missingFamily, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::populateFamilyAliases(missingFamily);
  }

  //  void QPlatformFontDatabase::populateFamily(const QString &familyName)
  void populateFamily(const QString &familyName) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall7 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall7>(taken[7]);
      call(this, &familyName, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::populateFamily(familyName);
  }

  //  void QPlatformFontDatabase::invalidate()
  void invalidate() override {
    if (taken[8]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall8 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::invalidate();
  }

  //  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
  //      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
  QFontEngineMulti *fontEngineMulti(
      QFontEngine *fontEngine,
      QFontDatabasePrivate::ExtendedScript script) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall9 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall9>(taken[9]);
      void * given = call(this, fontEngine, static_cast<int>(script), &handled);
      if (handled) return static_cast<QFontEngineMulti *>(given);
    }
    return QPlatformFontDatabase::fontEngineMulti(fontEngine, script);
  }

  //  QString QPlatformFontDatabase::fontDir() const
  QString fontDir() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall10 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall11 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall11>(taken[11]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformFontDatabase::defaultFont();
  }

  //  bool QPlatformFontDatabase::isPrivateFontFamily(const QString
  //      &family) const
  bool isPrivateFontFamily(const QString &family) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall12 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall12>(taken[12]);
      bool given = call(this, &family, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::isPrivateFontFamily(family);
  }

  //  QString QPlatformFontDatabase::resolveFontFamilyAlias(const QString
  //      &family) const
  QString resolveFontFamilyAlias(const QString &family) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall13 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQFreeTypeFontDatabaseCall14 call = reinterpret_cast<CuteQFreeTypeFontDatabaseCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::fontsAlwaysScalable();
  }
};

//  void QFreeTypeFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QFreeTypeFontDatabase20populateFontDatabaseEv(
    QFreeTypeFontDatabase *self) {
  self->populateFontDatabase();
}

//  QFontEngine *QFreeTypeFontDatabase::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN21QFreeTypeFontDatabase10fontEngineERK8QFontDefPv(
    QFreeTypeFontDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->fontEngine(*fontDef, handle);
}

//  QFontEngine *QFreeTypeFontDatabase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN21QFreeTypeFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QFreeTypeFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->fontEngine(*fontData, pixelSize, hintingPreference);
}

//  QStringList QFreeTypeFontDatabase::addApplicationFont(const QByteArray
//      &fontData, const QString &fileName,
//      QFontDatabasePrivate::ApplicationFont *applicationFont)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QFreeTypeFontDatabase18addApplicationFontERK10QByteArrayRK7QStringPN20QFontDatabasePrivate15ApplicationFontE(
    QFreeTypeFontDatabase *self,
    const QByteArray *fontData,
    const QString *fileName,
    QFontDatabasePrivate::ApplicationFont *applicationFont) {
  return new QList<QString>(
      self->addApplicationFont(
          *fontData,
          *fileName,
          applicationFont));
}

//  void QFreeTypeFontDatabase::releaseHandle(void *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QFreeTypeFontDatabase13releaseHandleEPv(
    QFreeTypeFontDatabase *self,
    void *handle) {
  self->releaseHandle(handle);
}

//  bool QFreeTypeFontDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QFreeTypeFontDatabase32supportsVariableApplicationFontsEv(
    const QFreeTypeFontDatabase *self) {
  return self->supportsVariableApplicationFonts();
}

//  bool QFreeTypeFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QFreeTypeFontDatabase19supportsColrv0FontsEv(
    const QFreeTypeFontDatabase *self) {
  return self->supportsColrv0Fonts();
}

//  void QFreeTypeFontDatabase::addNamedInstancesForFace(void *face, int
//      faceIndex, const QString &family, const QString &styleName,
//      QFont::Weight weight, QFont::Stretch stretch, QFont::Style style,
//      bool fixedPitch, bool isColor, const QSupportedWritingSystems
//      &writingSystems, const QByteArray &fileName, const QByteArray
//      &fontData)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QFreeTypeFontDatabase24addNamedInstancesForFaceEPviRK7QStringS3_N5QFont6WeightENS4_7StretchENS4_5StyleEbbRK24QSupportedWritingSystemsRK10QByteArraySD_(
    void *face,
    int faceIndex,
    const QString *family,
    const QString *styleName,
    QFont::Weight weight,
    QFont::Stretch stretch,
    QFont::Style style,
    bool fixedPitch,
    bool isColor,
    const QSupportedWritingSystems *writingSystems,
    const QByteArray *fileName,
    const QByteArray *fontData) {
  QFreeTypeFontDatabase::addNamedInstancesForFace(
      face,
      faceIndex,
      *family,
      *styleName,
      weight,
      stretch,
      style,
      fixedPitch,
      isColor,
      *writingSystems,
      *fileName,
      *fontData);
}

//  QStringList QFreeTypeFontDatabase::addTTFile(const QByteArray &fontData,
//      const QByteArray &file, QFontDatabasePrivate::ApplicationFont
//      *applicationFont)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QFreeTypeFontDatabase9addTTFileERK10QByteArrayS2_PN20QFontDatabasePrivate15ApplicationFontE(
    const QByteArray *fontData,
    const QByteArray *file,
    QFontDatabasePrivate::ApplicationFont *applicationFont) {
  return new QList<QString>(
      QFreeTypeFontDatabase::addTTFile(
          *fontData,
          *file,
          applicationFont));
}

//  QFreeTypeFontDatabase::~QFreeTypeFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QFreeTypeFontDatabaseD1Ev(QFreeTypeFontDatabase *self) {
  delete self;
}

//  a Python function taken by a CuteQFreeTypeFontDatabase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFreeTypeFontDatabase(
    QFreeTypeFontDatabase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFreeTypeFontDatabase *>(self)->take(key, call);
}

//  void QFreeTypeFontDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QFreeTypeFontDatabase20populateFontDatabaseEv(
    QFreeTypeFontDatabase *self) {
  self->QFreeTypeFontDatabase::populateFontDatabase();
}

//  QFontEngine *QFreeTypeFontDatabase::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN21QFreeTypeFontDatabase10fontEngineERK8QFontDefPv(
    QFreeTypeFontDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->QFreeTypeFontDatabase::fontEngine(*fontDef, handle);
}

//  QFontEngine *QFreeTypeFontDatabase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN21QFreeTypeFontDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QFreeTypeFontDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->QFreeTypeFontDatabase::fontEngine(
      *fontData,
      pixelSize,
      hintingPreference);
}

//  void QFreeTypeFontDatabase::releaseHandle(void *handle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QFreeTypeFontDatabase13releaseHandleEPv(
    QFreeTypeFontDatabase *self,
    void *handle) {
  self->QFreeTypeFontDatabase::releaseHandle(handle);
}

//  bool QFreeTypeFontDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QFreeTypeFontDatabase32supportsVariableApplicationFontsEv(
    const QFreeTypeFontDatabase *self) {
  return self->QFreeTypeFontDatabase::supportsVariableApplicationFonts();
}

//  bool QFreeTypeFontDatabase::supportsColrv0Fonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QFreeTypeFontDatabase19supportsColrv0FontsEv(
    const QFreeTypeFontDatabase *self) {
  return self->QFreeTypeFontDatabase::supportsColrv0Fonts();
}

#endif  // QT_CONFIG(freetype)
