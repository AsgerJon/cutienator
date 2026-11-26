//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontconfigdatabase_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(fontconfig) && QT_CONFIG(freetype) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontconfigdatabase_p.h>
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QFontconfigDatabase that Python can take functions over in. Every QFontconfigDatabase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQFontconfigDatabaseCall0)(const void *, int *);
typedef void (*CuteQFontconfigDatabaseCall1)(const void *, int *);
typedef bool (*CuteQFontconfigDatabaseCall2)(const void *, int *);
typedef void * (*CuteQFontconfigDatabaseCall3)(const void *, QFontEngine *, int, int *);
typedef void * (*CuteQFontconfigDatabaseCall4)(const void *, const QFontDef *, void *, int *);
typedef void * (*CuteQFontconfigDatabaseCall5)(const void *, const QByteArray *, qreal, int, int *);
typedef QString * (*CuteQFontconfigDatabaseCall6)(const void *, const QString *, int *);
typedef const QFont * (*CuteQFontconfigDatabaseCall7)(const void *, int *);
typedef void (*CuteQFontconfigDatabaseCall8)(const void *, void *, int *);
typedef bool (*CuteQFontconfigDatabaseCall9)(const void *, int *);
typedef bool (*CuteQFontconfigDatabaseCall10)(const void *, const QString *, int *);
typedef void (*CuteQFontconfigDatabaseCall11)(const void *, const QString *, int *);
typedef QString * (*CuteQFontconfigDatabaseCall12)(const void *, int *);
typedef bool (*CuteQFontconfigDatabaseCall13)(const void *, const QString *, int *);
typedef bool (*CuteQFontconfigDatabaseCall14)(const void *, int *);
class CuteQFontconfigDatabase : public QFontconfigDatabase {
public:
  using QFontconfigDatabase::QFontconfigDatabase;
  CuteQFontconfigDatabase(const QFontconfigDatabase & other) : QFontconfigDatabase(other) {}
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase20populateFontDatabaseEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase10invalidateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase32supportsVariableApplicationFontsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE")) {
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
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase22resolveFontFamilyAliasERK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase11defaultFontEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase13releaseHandleEPv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19supportsColrv0FontsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase21populateFamilyAliasesERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformFontDatabase14populateFamilyERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase7fontDirEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19isPrivateFontFamilyERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformFontDatabase19fontsAlwaysScalableEv")) {
      taken[14] = call;
      return true;
    }
    return false;
  }

  //  void QFontconfigDatabase::populateFontDatabase()
  void populateFontDatabase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall0 call = reinterpret_cast<CuteQFontconfigDatabaseCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QFontconfigDatabase::populateFontDatabase();
  }

  //  void QFontconfigDatabase::invalidate()
  void invalidate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall1 call = reinterpret_cast<CuteQFontconfigDatabaseCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QFontconfigDatabase::invalidate();
  }

  //  bool QFontconfigDatabase::supportsVariableApplicationFonts() const
  bool supportsVariableApplicationFonts() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall2 call = reinterpret_cast<CuteQFontconfigDatabaseCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontconfigDatabase::supportsVariableApplicationFonts();
  }

  //  QFontEngineMulti *QFontconfigDatabase::fontEngineMulti(QFontEngine
  //      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
  QFontEngineMulti *fontEngineMulti(
      QFontEngine *fontEngine,
      QFontDatabasePrivate::ExtendedScript script) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall3 call = reinterpret_cast<CuteQFontconfigDatabaseCall3>(taken[3]);
      void * given = call(this, fontEngine, static_cast<int>(script), &handled);
      if (handled) return static_cast<QFontEngineMulti *>(given);
    }
    return QFontconfigDatabase::fontEngineMulti(fontEngine, script);
  }

  //  QFontEngine *QFontconfigDatabase::fontEngine(const QFontDef &fontDef,
  //      void *handle)
  QFontEngine *fontEngine(const QFontDef &fontDef, void *handle) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall4 call = reinterpret_cast<CuteQFontconfigDatabaseCall4>(taken[4]);
      void * given = call(this, &fontDef, handle, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontconfigDatabase::fontEngine(fontDef, handle);
  }

  //  QFontEngine *QFontconfigDatabase::fontEngine(const QByteArray
  //      &fontData, qreal pixelSize, QFont::HintingPreference
  //      hintingPreference)
  QFontEngine *fontEngine(
      const QByteArray &fontData,
      qreal pixelSize,
      QFont::HintingPreference hintingPreference) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall5 call = reinterpret_cast<CuteQFontconfigDatabaseCall5>(taken[5]);
      void * given = call(this, &fontData, pixelSize, static_cast<int>(hintingPreference), &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontconfigDatabase::fontEngine(fontData, pixelSize, hintingPreference);
  }

  //  QString QFontconfigDatabase::resolveFontFamilyAlias(const QString
  //      &family) const
  QString resolveFontFamilyAlias(const QString &family) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall6 call = reinterpret_cast<CuteQFontconfigDatabaseCall6>(taken[6]);
      QString * given = call(this, &family, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontconfigDatabase::resolveFontFamilyAlias(family);
  }

  //  QFont QFontconfigDatabase::defaultFont() const
  QFont defaultFont() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall7 call = reinterpret_cast<CuteQFontconfigDatabaseCall7>(taken[7]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontconfigDatabase::defaultFont();
  }

  //  void QFreeTypeFontDatabase::releaseHandle(void *handle)
  void releaseHandle(void *handle) override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall8 call = reinterpret_cast<CuteQFontconfigDatabaseCall8>(taken[8]);
      call(this, handle, &handled);
      if (handled) return;
    }
    QFreeTypeFontDatabase::releaseHandle(handle);
  }

  //  bool QFreeTypeFontDatabase::supportsColrv0Fonts() const
  bool supportsColrv0Fonts() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall9 call = reinterpret_cast<CuteQFontconfigDatabaseCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFreeTypeFontDatabase::supportsColrv0Fonts();
  }

  //  bool QPlatformFontDatabase::populateFamilyAliases(const QString
  //      &missingFamily)
  bool populateFamilyAliases(const QString &missingFamily) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall10 call = reinterpret_cast<CuteQFontconfigDatabaseCall10>(taken[10]);
      bool given = call(this, &missingFamily, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::populateFamilyAliases(missingFamily);
  }

  //  void QPlatformFontDatabase::populateFamily(const QString &familyName)
  void populateFamily(const QString &familyName) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall11 call = reinterpret_cast<CuteQFontconfigDatabaseCall11>(taken[11]);
      call(this, &familyName, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::populateFamily(familyName);
  }

  //  QString QPlatformFontDatabase::fontDir() const
  QString fontDir() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall12 call = reinterpret_cast<CuteQFontconfigDatabaseCall12>(taken[12]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformFontDatabase::fontDir();
  }

  //  bool QPlatformFontDatabase::isPrivateFontFamily(const QString
  //      &family) const
  bool isPrivateFontFamily(const QString &family) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall13 call = reinterpret_cast<CuteQFontconfigDatabaseCall13>(taken[13]);
      bool given = call(this, &family, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::isPrivateFontFamily(family);
  }

  //  bool QPlatformFontDatabase::fontsAlwaysScalable() const
  bool fontsAlwaysScalable() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontconfigDatabaseCall14 call = reinterpret_cast<CuteQFontconfigDatabaseCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::fontsAlwaysScalable();
  }
};

//  QFontconfigDatabase::~QFontconfigDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFontconfigDatabaseD1Ev(QFontconfigDatabase *self) {
  delete self;
}

//  void QFontconfigDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFontconfigDatabase20populateFontDatabaseEv(
    QFontconfigDatabase *self) {
  self->populateFontDatabase();
}

//  void QFontconfigDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFontconfigDatabase10invalidateEv(
    QFontconfigDatabase *self) {
  self->invalidate();
}

//  bool QFontconfigDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFontconfigDatabase32supportsVariableApplicationFontsEv(
    const QFontconfigDatabase *self) {
  return self->supportsVariableApplicationFonts();
}

//  QFontEngineMulti *QFontconfigDatabase::fontEngineMulti(QFontEngine
//      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
extern "C" Q_DECL_EXPORT
QFontEngineMulti *ritual_ZN19QFontconfigDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE(
    QFontconfigDatabase *self,
    QFontEngine *fontEngine,
    QFontDatabasePrivate::ExtendedScript script) {
  return self->fontEngineMulti(fontEngine, script);
}

//  QFontEngine *QFontconfigDatabase::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN19QFontconfigDatabase10fontEngineERK8QFontDefPv(
    QFontconfigDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->fontEngine(*fontDef, handle);
}

//  QFontEngine *QFontconfigDatabase::fontEngine(const QByteArray &fontData,
//      qreal pixelSize, QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN19QFontconfigDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QFontconfigDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->fontEngine(*fontData, pixelSize, hintingPreference);
}

//  QStringList QFontconfigDatabase::fallbacksForFamily(const QString
//      &family, QFont::Style style, QFont::StyleHint styleHint,
//      QFontDatabasePrivate::ExtendedScript script) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QFontconfigDatabase18fallbacksForFamilyERK7QStringN5QFont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScriptE(
    const QFontconfigDatabase *self,
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

//  QStringList QFontconfigDatabase::addApplicationFont(const QByteArray
//      &fontData, const QString &fileName,
//      QFontDatabasePrivate::ApplicationFont *applicationFont)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QFontconfigDatabase18addApplicationFontERK10QByteArrayRK7QStringPN20QFontDatabasePrivate15ApplicationFontE(
    QFontconfigDatabase *self,
    const QByteArray *fontData,
    const QString *fileName,
    QFontDatabasePrivate::ApplicationFont *applicationFont) {
  return new QList<QString>(
      self->addApplicationFont(
          *fontData,
          *fileName,
          applicationFont));
}

//  QString QFontconfigDatabase::resolveFontFamilyAlias(const QString
//      &family) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QFontconfigDatabase22resolveFontFamilyAliasERK7QString(
    const QFontconfigDatabase *self,
    const QString *family) {
  return new QString(self->resolveFontFamilyAlias(*family));
}

//  QFont QFontconfigDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QFontconfigDatabase11defaultFontEv(
    const QFontconfigDatabase *self) {
  return new QFont(self->defaultFont());
}

//  void QFontconfigDatabase::setupFontEngine(QFontEngineFT *engine, const
//      QFontDef &fontDef) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QFontconfigDatabase15setupFontEngineEP13QFontEngineFTRK8QFontDef(
    const QFontconfigDatabase *self,
    QFontEngineFT *engine,
    const QFontDef *fontDef) {
  self->setupFontEngine(engine, *fontDef);
}

//  a Python function taken by a CuteQFontconfigDatabase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontconfigDatabase(
    QFontconfigDatabase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontconfigDatabase *>(self)->take(key, call);
}

//  void QFontconfigDatabase::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFontconfigDatabase20populateFontDatabaseEv(
    QFontconfigDatabase *self) {
  self->QFontconfigDatabase::populateFontDatabase();
}

//  void QFontconfigDatabase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFontconfigDatabase10invalidateEv(
    QFontconfigDatabase *self) {
  self->QFontconfigDatabase::invalidate();
}

//  bool QFontconfigDatabase::supportsVariableApplicationFonts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QFontconfigDatabase32supportsVariableApplicationFontsEv(
    const QFontconfigDatabase *self) {
  return self->QFontconfigDatabase::supportsVariableApplicationFonts();
}

//  QFontEngineMulti *QFontconfigDatabase::fontEngineMulti(QFontEngine
//      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
extern "C" Q_DECL_EXPORT
QFontEngineMulti *ritual_own_ZN19QFontconfigDatabase15fontEngineMultiEP11QFontEngineN20QFontDatabasePrivate14ExtendedScriptE(
    QFontconfigDatabase *self,
    QFontEngine *fontEngine,
    QFontDatabasePrivate::ExtendedScript script) {
  return self->QFontconfigDatabase::fontEngineMulti(fontEngine, script);
}

//  QFontEngine *QFontconfigDatabase::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN19QFontconfigDatabase10fontEngineERK8QFontDefPv(
    QFontconfigDatabase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->QFontconfigDatabase::fontEngine(*fontDef, handle);
}

//  QFontEngine *QFontconfigDatabase::fontEngine(const QByteArray &fontData,
//      qreal pixelSize, QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN19QFontconfigDatabase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QFontconfigDatabase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->QFontconfigDatabase::fontEngine(
      *fontData,
      pixelSize,
      hintingPreference);
}

//  QString QFontconfigDatabase::resolveFontFamilyAlias(const QString
//      &family) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QFontconfigDatabase22resolveFontFamilyAliasERK7QString(
    const QFontconfigDatabase *self,
    const QString *family) {
  return new QString(
      self->QFontconfigDatabase::resolveFontFamilyAlias(
          *family));
}

//  QFont QFontconfigDatabase::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK19QFontconfigDatabase11defaultFontEv(
    const QFontconfigDatabase *self) {
  return new QFont(self->QFontconfigDatabase::defaultFont());
}

#endif  // QT_CONFIG(fontconfig) && QT_CONFIG(freetype) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN)
