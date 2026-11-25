//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontdatabasebase_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
//  What Windows has, as 'HFONT', 'void *' and DirectWrite's interfaces,
//  is passed as an address. Not written: 'data' and 'init', which pass a
//  'QSharedPointer'; 'fontDefToLOGFONT' and 'LOGFONT_to_QFont', whose
//  'LOGFONT' is another type where 'UNICODE' is defined than where not;
//  and 'createDirectWriteFaces', giving a list of DirectWrite's faces.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontdatabasebase_p.h>
#include <QtGui/qfont.h>
#include <QtCore/qstringlist.h>
#include <cstring>

//  A QWindowsFontDatabaseBase that Python can take functions over in. Every
//  QWindowsFontDatabaseBase Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQWindowsFontDatabaseBaseCall0)(const void *, int *);
typedef void * (*CuteQWindowsFontDatabaseBaseCall1)(const void *, const QByteArray *, qreal, int, int *);
typedef bool (*CuteQWindowsFontDatabaseBaseCall2)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseBaseCall3)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseBaseCall4)(const void *, const QString *, int *);
typedef void (*CuteQWindowsFontDatabaseBaseCall5)(const void *, const QString *, int *);
typedef void (*CuteQWindowsFontDatabaseBaseCall6)(const void *, int *);
typedef void * (*CuteQWindowsFontDatabaseBaseCall7)(const void *, QFontEngine *, int, int *);
typedef QString * (*CuteQWindowsFontDatabaseBaseCall8)(const void *, int *);
typedef const QFont * (*CuteQWindowsFontDatabaseBaseCall9)(const void *, int *);
typedef bool (*CuteQWindowsFontDatabaseBaseCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQWindowsFontDatabaseBaseCall11)(const void *, const QString *, int *);
typedef bool (*CuteQWindowsFontDatabaseBaseCall12)(const void *, int *);
class CuteQWindowsFontDatabaseBase : public QWindowsFontDatabaseBase {
public:
  using QWindowsFontDatabaseBase::QWindowsFontDatabaseBase;
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

  //  void QPlatformFontDatabase::populateFontDatabase()
  void populateFontDatabase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall0 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::populateFontDatabase();
  }

  //  QFontEngine *QWindowsFontDatabaseBase::fontEngine(const QByteArray
  //      &fontData, qreal pixelSize, QFont::HintingPreference
  //      hintingPreference)
  QFontEngine *fontEngine(const QByteArray &fontData, qreal pixelSize, QFont::HintingPreference hintingPreference) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall1 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall1>(taken[1]);
      void * given = call(this, &fontData, pixelSize, static_cast<int>(hintingPreference), &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QWindowsFontDatabaseBase::fontEngine(fontData, pixelSize, hintingPreference);
  }

  //  bool QPlatformFontDatabase::supportsVariableApplicationFonts() const
  bool supportsVariableApplicationFonts() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall2 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::supportsVariableApplicationFonts();
  }

  //  bool QPlatformFontDatabase::supportsColrv0Fonts() const
  bool supportsColrv0Fonts() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall3 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::supportsColrv0Fonts();
  }

  //  bool QPlatformFontDatabase::populateFamilyAliases(const QString
  //      &missingFamily)
  bool populateFamilyAliases(const QString &missingFamily) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall4 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall4>(taken[4]);
      bool given = call(this, &missingFamily, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::populateFamilyAliases(missingFamily);
  }

  //  void QPlatformFontDatabase::populateFamily(const QString &familyName)
  void populateFamily(const QString &familyName) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall5 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall5>(taken[5]);
      call(this, &familyName, &handled);
      if (handled) return;
    }
    QPlatformFontDatabase::populateFamily(familyName);
  }

  //  void QWindowsFontDatabaseBase::invalidate()
  void invalidate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall6 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsFontDatabaseBase::invalidate();
  }

  //  QFontEngineMulti *QPlatformFontDatabase::fontEngineMulti(QFontEngine
  //      *fontEngine, QFontDatabasePrivate::ExtendedScript script)
  QFontEngineMulti *fontEngineMulti(QFontEngine *fontEngine, QFontDatabasePrivate::ExtendedScript script) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall7 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall7>(taken[7]);
      void * given = call(this, fontEngine, static_cast<int>(script), &handled);
      if (handled) return static_cast<QFontEngineMulti *>(given);
    }
    return QPlatformFontDatabase::fontEngineMulti(fontEngine, script);
  }

  //  QString QPlatformFontDatabase::fontDir() const
  QString fontDir() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall8 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall8>(taken[8]);
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
      CuteQWindowsFontDatabaseBaseCall9 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall9>(taken[9]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformFontDatabase::defaultFont();
  }

  //  bool QPlatformFontDatabase::isPrivateFontFamily(const QString &family)
  //      const
  bool isPrivateFontFamily(const QString &family) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowsFontDatabaseBaseCall10 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall10>(taken[10]);
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
      CuteQWindowsFontDatabaseBaseCall11 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall11>(taken[11]);
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
      CuteQWindowsFontDatabaseBaseCall12 call = reinterpret_cast<CuteQWindowsFontDatabaseBaseCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformFontDatabase::fontsAlwaysScalable();
  }
};

//  QWindowsFontDatabaseBase::QWindowsFontDatabaseBase()
extern "C" Q_DECL_EXPORT
QWindowsFontDatabaseBase *ritual_ZN24QWindowsFontDatabaseBaseC1Ev() {
  return new CuteQWindowsFontDatabaseBase();
}

//  QWindowsFontDatabaseBase::~QWindowsFontDatabaseBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWindowsFontDatabaseBaseD1Ev(
    QWindowsFontDatabaseBase *self) {
  delete self;
}

//  QFontEngine *QWindowsFontDatabaseBase::fontEngine(const QFontDef
//      &fontDef, void *handle)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN24QWindowsFontDatabaseBase10fontEngineERK8QFontDefPv(
    QWindowsFontDatabaseBase *self,
    const QFontDef *fontDef,
    void *handle) {
  return self->fontEngine(*fontDef, handle);
}

//  QFontEngine *QWindowsFontDatabaseBase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN24QWindowsFontDatabaseBase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsFontDatabaseBase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->fontEngine(*fontData, pixelSize, hintingPreference);
}

//  void QWindowsFontDatabaseBase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWindowsFontDatabaseBase10invalidateEv(
    QWindowsFontDatabaseBase *self) {
  self->invalidate();
}

//  int QWindowsFontDatabaseBase::defaultVerticalDPI()
extern "C" Q_DECL_EXPORT
int ritual_ZN24QWindowsFontDatabaseBase18defaultVerticalDPIEv() {
  return QWindowsFontDatabaseBase::defaultVerticalDPI();
}

#if QT_CONFIG(directwrite)
//  void QWindowsFontDatabaseBase::createDirectWriteFactory(IDWriteFactory
//      **factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWindowsFontDatabaseBase24createDirectWriteFactoryEPP14IDWriteFactory(
    IDWriteFactory **factory) {
  QWindowsFontDatabaseBase::createDirectWriteFactory(factory);
}
#endif  // QT_CONFIG(directwrite)

//  QFont QWindowsFontDatabaseBase::systemDefaultFont()
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN24QWindowsFontDatabaseBase17systemDefaultFontEv() {
  return new QFont(QWindowsFontDatabaseBase::systemDefaultFont());
}

//  HFONT QWindowsFontDatabaseBase::systemFont()
extern "C" Q_DECL_EXPORT
HFONT ritual_ZN24QWindowsFontDatabaseBase10systemFontEv() {
  return QWindowsFontDatabaseBase::systemFont();
}

//  QString QWindowsFontDatabaseBase::familyForStyleHint(QFont::StyleHint
//      styleHint)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QWindowsFontDatabaseBase18familyForStyleHintEN5QFont9StyleHintE(
    QFont::StyleHint styleHint) {
  return new QString(QWindowsFontDatabaseBase::familyForStyleHint(styleHint));
}

//  QStringList QWindowsFontDatabaseBase::extraTryFontsForFamily(const
//      QString &family)
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZN24QWindowsFontDatabaseBase22extraTryFontsForFamilyERK7QString(
    const QString *family) {
  return new QStringList(QWindowsFontDatabaseBase::extraTryFontsForFamily(*family));
}

//  QStringList QWindowsFontDatabaseBase::familiesForScript(QFontDatabasePriv
//      ate::ExtendedScript script)
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZN24QWindowsFontDatabaseBase17familiesForScriptEN20QFontDatabasePrivate14ExtendedScriptE(
    QFontDatabasePrivate::ExtendedScript script) {
  return new QStringList(QWindowsFontDatabaseBase::familiesForScript(script));
}

//  QFontDef QWindowsFontDatabaseBase::sanitizeRequest(QFontDef request)
//      const
extern "C" Q_DECL_EXPORT
QFontDef *ritual_ZNK24QWindowsFontDatabaseBase15sanitizeRequestE8QFontDef(
    const QWindowsFontDatabaseBase *self,
    const QFontDef *request) {
  return new QFontDef(self->sanitizeRequest(*request));
}

#if QT_CONFIG(directwrite)
//  IDWriteFontFace *QWindowsFontDatabaseBase::createDirectWriteFace(const
//      QByteArray &fontData)
extern "C" Q_DECL_EXPORT
IDWriteFontFace *ritual_ZN24QWindowsFontDatabaseBase21createDirectWriteFaceERK10QByteArray(
    QWindowsFontDatabaseBase *self,
    const QByteArray *fontData) {
  return self->createDirectWriteFace(*fontData);
}
#endif  // QT_CONFIG(directwrite)

//  a Python function taken by a CuteQWindowsFontDatabaseBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsFontDatabaseBase(
    QWindowsFontDatabaseBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsFontDatabaseBase *>(self)->take(key, call);
}

//  QFontEngine *QWindowsFontDatabaseBase::fontEngine(const QByteArray
//      &fontData, qreal pixelSize, QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN24QWindowsFontDatabaseBase10fontEngineERK10QByteArraydN5QFont17HintingPreferenceE(
    QWindowsFontDatabaseBase *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return self->QWindowsFontDatabaseBase::fontEngine(*fontData, pixelSize, hintingPreference);
}

//  void QWindowsFontDatabaseBase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QWindowsFontDatabaseBase10invalidateEv(
    QWindowsFontDatabaseBase *self) {
  self->QWindowsFontDatabaseBase::invalidate();
}

#endif  // defined(Q_OS_WIN)
