//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_ft_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
//  A 'void *' is passed as an address. It declares no constructor, and
//  none is written, as for QFreeTypeFontDatabase.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(freetype)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_ft_p.h>
#include <QtGui/qfont.h>
#include <QtCore/qstringlist.h>
#include <cstring>

//  A QWindowsFontDatabaseFT that Python can take functions over in. Every
//  QWindowsFontDatabaseFT Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQWindowsFontDatabaseFTCall0)(const void *, int *);
typedef void * (*CuteQWindowsFontDatabaseFTCall1)(const void *, const QByteArray *, qreal, int, int *);
typedef bool (*CuteQWindowsFontDatabaseFTCall2)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseFTCall3)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseFTCall4)(const void *, const QString *, int *);
typedef void (*CuteQWindowsFontDatabaseFTCall5)(const void *, const QString *, int *);
typedef void (*CuteQWindowsFontDatabaseFTCall6)(const void *, int *);
typedef void * (*CuteQWindowsFontDatabaseFTCall7)(const void *, QFontEngine *, int, int *);
typedef QString * (*CuteQWindowsFontDatabaseFTCall8)(const void *, int *);
typedef const QFont * (*CuteQWindowsFontDatabaseFTCall9)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseFTCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQWindowsFontDatabaseFTCall11)(const void *, const QString *, int *);
typedef bool (*CuteQWindowsFontDatabaseFTCall12)(const void *, int *);
class CuteQWindowsFontDatabaseFT : public QWindowsFontDatabaseFT {
public:
  using QWindowsFontDatabaseFT::QWindowsFontDatabaseFT;
  CuteQWindowsFontDatabaseFT(const QWindowsFontDatabaseFT &other) : QWindowsFontDatabaseFT(other) {}
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

  //  void QWindowsFontDatabaseFT::populateFontDatabase()
  void populateFontDatabase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall0 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsFontDatabaseFT::populateFontDatabase();
  }

  //  QFontEngine *QWindowsFontDatabaseFT::fontEngine(const QByteArray
  //      &fontData, qreal pixelSize, QFont::HintingPreference
  //      hintingPreference)
  QFontEngine *fontEngine(const QByteArray &fontData, qreal pixelSize, QFont::HintingPreference hintingPreference) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall1 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall1>(taken[1]);
      void * given = call(this, &fontData, pixelSize, static_cast<int>(hintingPreference), &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QWindowsFontDatabaseFT::fontEngine(fontData, pixelSize, hintingPreference);
  }

  //  bool QFreeTypeFontDatabase::supportsVariableApplicationFonts() const
  bool supportsVariableApplicationFonts() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall2 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFreeTypeFontDatabase::supportsVariableApplicationFonts();
  }

  //  bool QFreeTypeFontDatabase::supportsColrv0Fonts() const
  bool supportsColrv0Fonts() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall3 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFreeTypeFontDatabase::supportsColrv0Fonts();
  }

  //  bool QWindowsFontDatabaseFT::populateFamilyAliases(const QString
  //      &missingFamily)
  bool populateFamilyAliases(const QString &missingFamily) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall4 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall4>(taken[4]);
      bool given = call(this, &missingFamily, &handled);
      if (handled) return given;
    }
    return QWindowsFontDatabaseFT::populateFamilyAliases(missingFamily);
  }

  //  void QWindowsFontDatabaseFT::populateFamily(const QString &familyName)
  void populateFamily(const QString &familyName) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall5 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall5>(taken[5]);
      call(this, &familyName, &handled);
      if (handled) return;
    }
    QWindowsFontDatabaseFT::populateFamily(familyName);
  }

  //  void QPlatformFontDatabase::invalidate()
  void invalidate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall6 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::invalidate();
  }

  //  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
  //      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
  QFontEngineMulti *fontEngineMulti(QFontEngine *fontEngine, QFontDatabasePrivate::ExtendedScript script) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall7 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall7>(taken[7]);
      void * given = call(this, fontEngine, static_cast<int>(script), &handled);
      if (handled) return static_cast<QFontEngineMulti *>(given);
    }
    return QPlatformFontDatabase::fontEngineMulti(fontEngine, script);
  }

  //  QString QWindowsFontDatabaseFT::fontDir() const
  QString fontDir() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall8 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QWindowsFontDatabaseFT::fontDir();
  }

  //  QFont QWindowsFontDatabaseFT::defaultFont() const
  QFont defaultFont() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall9 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall9>(taken[9]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsFontDatabaseFT::defaultFont();
  }

  //  bool QPlatformFontDatabase::isPrivateFontFamily(const QString &family)
  //      const
  bool isPrivateFontFamily(const QString &family) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowsFontDatabaseFTCall10 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall10>(taken[10]);
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
      CuteQWindowsFontDatabaseFTCall11 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall11>(taken[11]);
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
      CuteQWindowsFontDatabaseFTCall12 call = reinterpret_cast<CuteQWindowsFontDatabaseFTCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::fontsAlwaysScalable();
  }
};

//  QFontEngine *QWindowsFontDatabaseFT::fontEngine(const QFontDef &fontDef,
//      void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN22QWindowsFontDatabaseFT10fontEngineERK8QFontDefPv(
    QWindowsFontDatabaseFT *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->fontEngine(*fontDef, handle);
}

//  QStringList QWindowsFontDatabaseFT::fallbacksForFamily(const QString
//      &family, QFont::Style style, QFont::StyleHint styleHint,
//      QFontDatabasePrivate::ExtendedScript script) const
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZNK22QWindowsFontDatabaseFT18fallbacksForFamilyERK7QStringN5QFont5StyleENS3_9StyleHintEN20QFontDatabasePrivate14ExtendedScriptE(
    const QWindowsFontDatabaseFT *self,
    const QString *family,
    QFont::Style style,
    QFont::StyleHint styleHint,
    QFontDatabasePrivate::ExtendedScript script) {
  return new QStringList(self->fallbacksForFamily(*family, style, styleHint, script));
}

//  void QWindowsFontDatabaseFT::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowsFontDatabaseFT20populateFontDatabaseEv(
    QWindowsFontDatabaseFT *self) {
  self->populateFontDatabase();
}

//  QFontEngine *QWindowsFontDatabaseFT::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN22QWindowsFontDatabaseFT10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsFontDatabaseFT *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->fontEngine(*fontData, pixelSize, hintingPreference);
}

//  bool QWindowsFontDatabaseFT::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowsFontDatabaseFT21populateFamilyAliasesERK7QString(
    QWindowsFontDatabaseFT *self,
    const QString *missingFamily) {
  return self->populateFamilyAliases(*missingFamily);
}

//  void QWindowsFontDatabaseFT::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowsFontDatabaseFT14populateFamilyERK7QString(
    QWindowsFontDatabaseFT *self,
    const QString *familyName) {
  self->populateFamily(*familyName);
}

//  QString QWindowsFontDatabaseFT::fontDir() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWindowsFontDatabaseFT7fontDirEv(
    const QWindowsFontDatabaseFT *self) {
  return new QString(self->fontDir());
}

//  QFont QWindowsFontDatabaseFT::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK22QWindowsFontDatabaseFT11defaultFontEv(
    const QWindowsFontDatabaseFT *self) {
  return new QFont(self->defaultFont());
}

//  QWindowsFontDatabaseFT::~QWindowsFontDatabaseFT()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowsFontDatabaseFTD1Ev(QWindowsFontDatabaseFT *self) {
  delete self;
}

//  a Python function taken by a CuteQWindowsFontDatabaseFT, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsFontDatabaseFT(
    QWindowsFontDatabaseFT *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsFontDatabaseFT *>(self)->take(key, call);
}

//  void QWindowsFontDatabaseFT::populateFontDatabase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QWindowsFontDatabaseFT20populateFontDatabaseEv(
    QWindowsFontDatabaseFT *self) {
  self->QWindowsFontDatabaseFT::populateFontDatabase();
}

//  QFontEngine *QWindowsFontDatabaseFT::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN22QWindowsFontDatabaseFT10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsFontDatabaseFT *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->QWindowsFontDatabaseFT::fontEngine(*fontData, pixelSize, hintingPreference);
}

//  bool QWindowsFontDatabaseFT::populateFamilyAliases(const QString
//      &missingFamily)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QWindowsFontDatabaseFT21populateFamilyAliasesERK7QString(
    QWindowsFontDatabaseFT *self,
    const QString *missingFamily) {
  return self->QWindowsFontDatabaseFT::populateFamilyAliases(*missingFamily);
}

//  void QWindowsFontDatabaseFT::populateFamily(const QString &familyName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QWindowsFontDatabaseFT14populateFamilyERK7QString(
    QWindowsFontDatabaseFT *self,
    const QString *familyName) {
  self->QWindowsFontDatabaseFT::populateFamily(*familyName);
}

//  QString QWindowsFontDatabaseFT::fontDir() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QWindowsFontDatabaseFT7fontDirEv(
    const QWindowsFontDatabaseFT *self) {
  return new QString(self->QWindowsFontDatabaseFT::fontDir());
}

//  QFont QWindowsFontDatabaseFT::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK22QWindowsFontDatabaseFT11defaultFontEv(
    const QWindowsFontDatabaseFT *self) {
  return new QFont(self->QWindowsFontDatabaseFT::defaultFont());
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(freetype)
