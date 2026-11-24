//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformtheme.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformtheme.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qicon.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformTheme that Python can take functions over in. Every QPlatformTheme
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformThemeCall0)(const void *, int *);
typedef void * (*CuteQPlatformThemeCall1)(const void *, int *);
typedef void * (*CuteQPlatformThemeCall2)(const void *, int *);
typedef void (*CuteQPlatformThemeCall3)(const void *, int *);
typedef bool (*CuteQPlatformThemeCall4)(const void *, int, int *);
typedef void * (*CuteQPlatformThemeCall5)(const void *, int, int *);
#if !defined(QT_NO_SYSTEMTRAYICON)
typedef void * (*CuteQPlatformThemeCall6)(const void *, int *);
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
typedef int (*CuteQPlatformThemeCall7)(const void *, int *);
typedef void * (*CuteQPlatformThemeCall8)(const void *, int, int *);
typedef void * (*CuteQPlatformThemeCall9)(const void *, int, int *);
typedef const QVariant * (*CuteQPlatformThemeCall10)(const void *, int, int *);
typedef const QPixmap * (*CuteQPlatformThemeCall11)(const void *, int, const QSizeF *, int *);
typedef const QIcon * (*CuteQPlatformThemeCall12)(const void *, const QFileInfo *, int, int *);
typedef void * (*CuteQPlatformThemeCall13)(const void *, const QString *, int *);
typedef QString * (*CuteQPlatformThemeCall14)(const void *, int, int *);
#if QT_CONFIG(shortcut)
typedef const QKeySequence * (*CuteQPlatformThemeCall15)(const void *, int, int *);
#endif  // QT_CONFIG(shortcut)
typedef void (*CuteQPlatformThemeCall16)(const void *, int, int *);
typedef int (*CuteQPlatformThemeCall17)(const void *, int *);
typedef int (*CuteQPlatformThemeCall18)(const void *, int *);
class CuteQPlatformTheme : public QPlatformTheme {
public:
  using QPlatformTheme::QPlatformTheme;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QPlatformTheme22createPlatformMenuItemEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18createPlatformMenuEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme21createPlatformMenuBarEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlatformTheme19showPlatformMenuBarEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTypeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10DialogTypeE")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme11colorSchemeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme7paletteENS_7PaletteE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme4fontENS_4FontE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixmapERK6QSizeF")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_10IconOptionEE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme16createIconEngineERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18standardButtonTextEi")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme22standardButtonShortcutEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSchemeE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18contrastPreferenceEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme16motionPreferenceEv")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem() const
  QPlatformMenuItem *createPlatformMenuItem() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformThemeCall0 call = reinterpret_cast<CuteQPlatformThemeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuItem *>(given);
    }
    return QPlatformTheme::createPlatformMenuItem();
  }

  //  QPlatformMenu *QPlatformTheme::createPlatformMenu() const
  QPlatformMenu *createPlatformMenu() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformThemeCall1 call = reinterpret_cast<CuteQPlatformThemeCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QPlatformTheme::createPlatformMenu();
  }

  //  QPlatformMenuBar *QPlatformTheme::createPlatformMenuBar() const
  QPlatformMenuBar *createPlatformMenuBar() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformThemeCall2 call = reinterpret_cast<CuteQPlatformThemeCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuBar *>(given);
    }
    return QPlatformTheme::createPlatformMenuBar();
  }

  //  void QPlatformTheme::showPlatformMenuBar()
  void showPlatformMenuBar() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformThemeCall3 call = reinterpret_cast<CuteQPlatformThemeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformTheme::showPlatformMenuBar();
  }

  //  bool QPlatformTheme::usePlatformNativeDialog(DialogType type) const
  bool usePlatformNativeDialog(
      QPlatformTheme::DialogType type) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformThemeCall4 call = reinterpret_cast<CuteQPlatformThemeCall4>(taken[4]);
      bool given = call(this, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return QPlatformTheme::usePlatformNativeDialog(type);
  }

  //  QPlatformDialogHelper
  //      *QPlatformTheme::createPlatformDialogHelper(DialogType type)
  //      const
  QPlatformDialogHelper *createPlatformDialogHelper(
      QPlatformTheme::DialogType type) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformThemeCall5 call = reinterpret_cast<CuteQPlatformThemeCall5>(taken[5]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<QPlatformDialogHelper *>(given);
    }
    return QPlatformTheme::createPlatformDialogHelper(type);
  }

#if !defined(QT_NO_SYSTEMTRAYICON)
  //  QPlatformSystemTrayIcon
  //      *QPlatformTheme::createPlatformSystemTrayIcon() const
  QPlatformSystemTrayIcon *createPlatformSystemTrayIcon() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformThemeCall6 call = reinterpret_cast<CuteQPlatformThemeCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSystemTrayIcon *>(given);
    }
    return QPlatformTheme::createPlatformSystemTrayIcon();
  }
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

  //  Qt::ColorScheme QPlatformTheme::colorScheme() const
  Qt::ColorScheme colorScheme() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformThemeCall7 call = reinterpret_cast<CuteQPlatformThemeCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ColorScheme>(given);
    }
    return QPlatformTheme::colorScheme();
  }

  //  const QPalette *QPlatformTheme::palette(Palette type) const
  const QPalette *palette(QPlatformTheme::Palette type) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformThemeCall8 call = reinterpret_cast<CuteQPlatformThemeCall8>(taken[8]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<const QPalette *>(given);
    }
    return QPlatformTheme::palette(type);
  }

  //  const QFont *QPlatformTheme::font(Font type) const
  const QFont *font(QPlatformTheme::Font type) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformThemeCall9 call = reinterpret_cast<CuteQPlatformThemeCall9>(taken[9]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<const QFont *>(given);
    }
    return QPlatformTheme::font(type);
  }

  //  QVariant QPlatformTheme::themeHint(ThemeHint hint) const
  QVariant themeHint(QPlatformTheme::ThemeHint hint) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformThemeCall10 call = reinterpret_cast<CuteQPlatformThemeCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::themeHint(hint);
  }

  //  QPixmap QPlatformTheme::standardPixmap(StandardPixmap sp, const
  //      QSizeF &size) const
  QPixmap standardPixmap(
      QPlatformTheme::StandardPixmap sp,
      const QSizeF &size) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformThemeCall11 call = reinterpret_cast<CuteQPlatformThemeCall11>(taken[11]);
      const QPixmap * given = call(this, static_cast<int>(sp), &size, &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::standardPixmap(sp, size);
  }

  //  QIcon QPlatformTheme::fileIcon(const QFileInfo &fileInfo,
  //      QPlatformTheme::IconOptions iconOptions) const
  QIcon fileIcon(
      const QFileInfo &fileInfo,
      QPlatformTheme::IconOptions iconOptions) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformThemeCall12 call = reinterpret_cast<CuteQPlatformThemeCall12>(taken[12]);
      const QIcon * given = call(this, &fileInfo, static_cast<int>(iconOptions.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::fileIcon(fileInfo, iconOptions);
  }

  //  QIconEngine *QPlatformTheme::createIconEngine(const QString
  //      &iconName) const
  QIconEngine *createIconEngine(const QString &iconName) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformThemeCall13 call = reinterpret_cast<CuteQPlatformThemeCall13>(taken[13]);
      void * given = call(this, &iconName, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QPlatformTheme::createIconEngine(iconName);
  }

  //  QString QPlatformTheme::standardButtonText(int button) const
  QString standardButtonText(int button) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformThemeCall14 call = reinterpret_cast<CuteQPlatformThemeCall14>(taken[14]);
      QString * given = call(this, button, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformTheme::standardButtonText(button);
  }

#if QT_CONFIG(shortcut)
  //  QKeySequence QPlatformTheme::standardButtonShortcut(int button) const
  QKeySequence standardButtonShortcut(int button) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformThemeCall15 call = reinterpret_cast<CuteQPlatformThemeCall15>(taken[15]);
      const QKeySequence * given = call(this, button, &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::standardButtonShortcut(button);
  }
#endif  // QT_CONFIG(shortcut)

  //  void QPlatformTheme::requestColorScheme(Qt::ColorScheme scheme)
  void requestColorScheme(Qt::ColorScheme scheme) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformThemeCall16 call = reinterpret_cast<CuteQPlatformThemeCall16>(taken[16]);
      call(this, static_cast<int>(scheme), &handled);
      if (handled) return;
    }
    QPlatformTheme::requestColorScheme(scheme);
  }

  //  Qt::ContrastPreference QPlatformTheme::contrastPreference() const
  Qt::ContrastPreference contrastPreference() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformThemeCall17 call = reinterpret_cast<CuteQPlatformThemeCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ContrastPreference>(given);
    }
    return QPlatformTheme::contrastPreference();
  }

  //  Qt::MotionPreference QPlatformTheme::motionPreference() const
  Qt::MotionPreference motionPreference() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformThemeCall18 call = reinterpret_cast<CuteQPlatformThemeCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::MotionPreference>(given);
    }
    return QPlatformTheme::motionPreference();
  }
};

//  QPlatformThemePrivate *QPlatformTheme::d_func()
extern "C" Q_DECL_EXPORT
QPlatformThemePrivate *ritual_ZN14QPlatformTheme6d_funcEv(
    QPlatformTheme *self) {
  return self->d_func();
}

//  const QPlatformThemePrivate *QPlatformTheme::d_func() const
extern "C" Q_DECL_EXPORT
const QPlatformThemePrivate *ritual_ZNK14QPlatformTheme6d_funcEv(
    const QPlatformTheme *self) {
  return self->d_func();
}

//  QPlatformTheme::QPlatformTheme()
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_ZN14QPlatformThemeC1Ev() {
  return new CuteQPlatformTheme();
}

//  QPlatformTheme::~QPlatformTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlatformThemeD1Ev(QPlatformTheme *self) {
  delete self;
}

//  QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK14QPlatformTheme22createPlatformMenuItemEv(
    const QPlatformTheme *self) {
  return self->createPlatformMenuItem();
}

//  QPlatformMenu *QPlatformTheme::createPlatformMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK14QPlatformTheme18createPlatformMenuEv(
    const QPlatformTheme *self) {
  return self->createPlatformMenu();
}

//  QPlatformMenuBar *QPlatformTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_ZNK14QPlatformTheme21createPlatformMenuBarEv(
    const QPlatformTheme *self) {
  return self->createPlatformMenuBar();
}

//  void QPlatformTheme::showPlatformMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlatformTheme19showPlatformMenuBarEv(QPlatformTheme *self) {
  self->showPlatformMenuBar();
}

//  bool QPlatformTheme::usePlatformNativeDialog(DialogType type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTypeE(
    const QPlatformTheme *self,
    QPlatformTheme::DialogType type) {
  return self->usePlatformNativeDialog(type);
}

//  QPlatformDialogHelper
//      *QPlatformTheme::createPlatformDialogHelper(DialogType type) const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper *ritual_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10DialogTypeE(
    const QPlatformTheme *self,
    QPlatformTheme::DialogType type) {
  return self->createPlatformDialogHelper(type);
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QPlatformSystemTrayIcon *QPlatformTheme::createPlatformSystemTrayIcon()
//      const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv(
    const QPlatformTheme *self) {
  return self->createPlatformSystemTrayIcon();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  Qt::ColorScheme QPlatformTheme::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK14QPlatformTheme11colorSchemeEv(
    const QPlatformTheme *self) {
  return self->colorScheme();
}

//  const QPalette *QPlatformTheme::palette(Palette type) const
extern "C" Q_DECL_EXPORT
const QPalette *ritual_ZNK14QPlatformTheme7paletteENS_7PaletteE(
    const QPlatformTheme *self,
    QPlatformTheme::Palette type) {
  return self->palette(type);
}

//  const QFont *QPlatformTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_ZNK14QPlatformTheme4fontENS_4FontE(
    const QPlatformTheme *self,
    QPlatformTheme::Font type) {
  return self->font(type);
}

//  QVariant QPlatformTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE(
    const QPlatformTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->themeHint(hint));
}

//  QPixmap QPlatformTheme::standardPixmap(StandardPixmap sp, const QSizeF
//      &size) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixmapERK6QSizeF(
    const QPlatformTheme *self,
    QPlatformTheme::StandardPixmap sp,
    const QSizeF *size) {
  return new QPixmap(self->standardPixmap(sp, *size));
}

//  QIcon QPlatformTheme::fileIcon(const QFileInfo &fileInfo,
//      QPlatformTheme::IconOptions iconOptions) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_10IconOptionEE(
    const QPlatformTheme *self,
    const QFileInfo *fileInfo,
    int iconOptions) {
  return new QIcon(
      self->fileIcon(
          *fileInfo,
          QFlags<QPlatformTheme::IconOption>::fromInt(iconOptions)));
}

//  QIconEngine *QPlatformTheme::createIconEngine(const QString &iconName)
//      const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK14QPlatformTheme16createIconEngineERK7QString(
    const QPlatformTheme *self,
    const QString *iconName) {
  return self->createIconEngine(*iconName);
}

#if QT_CONFIG(shortcut)
//  QList<QKeySequence> QPlatformTheme::keyBindings(QKeySequence::StandardKey
//      key) const
extern "C" Q_DECL_EXPORT
QList<QKeySequence> *ritual_ZNK14QPlatformTheme11keyBindingsEN12QKeySequence11StandardKeyE(
    const QPlatformTheme *self,
    QKeySequence::StandardKey key) {
  return new QList<QKeySequence>(self->keyBindings(key));
}
#endif  // QT_CONFIG(shortcut)

//  QString QPlatformTheme::standardButtonText(int button) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlatformTheme18standardButtonTextEi(
    const QPlatformTheme *self,
    int button) {
  return new QString(self->standardButtonText(button));
}

#if QT_CONFIG(shortcut)
//  QKeySequence QPlatformTheme::standardButtonShortcut(int button) const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK14QPlatformTheme22standardButtonShortcutEi(
    const QPlatformTheme *self,
    int button) {
  return new QKeySequence(self->standardButtonShortcut(button));
}
#endif  // QT_CONFIG(shortcut)

//  void QPlatformTheme::requestColorScheme(Qt::ColorScheme scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSchemeE(
    QPlatformTheme *self,
    Qt::ColorScheme scheme) {
  self->requestColorScheme(scheme);
}

//  Qt::ContrastPreference QPlatformTheme::contrastPreference() const
extern "C" Q_DECL_EXPORT
Qt::ContrastPreference ritual_ZNK14QPlatformTheme18contrastPreferenceEv(
    const QPlatformTheme *self) {
  return self->contrastPreference();
}

//  Qt::MotionPreference QPlatformTheme::motionPreference() const
extern "C" Q_DECL_EXPORT
Qt::MotionPreference ritual_ZNK14QPlatformTheme16motionPreferenceEv(
    const QPlatformTheme *self) {
  return self->motionPreference();
}

//  QVariant QPlatformTheme::defaultThemeHint(ThemeHint hint)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QPlatformTheme16defaultThemeHintENS_9ThemeHintE(
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(QPlatformTheme::defaultThemeHint(hint));
}

//  QString QPlatformTheme::defaultStandardButtonText(int button)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QPlatformTheme25defaultStandardButtonTextEi(int button) {
  return new QString(QPlatformTheme::defaultStandardButtonText(button));
}

//  QString QPlatformTheme::removeMnemonics(const QString &original)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QPlatformTheme15removeMnemonicsERK7QString(
    const QString *original) {
  return new QString(QPlatformTheme::removeMnemonics(*original));
}

//  QString QPlatformTheme::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlatformTheme4nameEv(const QPlatformTheme *self) {
  return new QString(self->name());
}

//  QPlatformTheme::QPlatformTheme(QPlatformThemePrivate *priv)
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_ZN14QPlatformThemeC1EP21QPlatformThemePrivate(
    QPlatformThemePrivate *priv) {
  return new CuteQPlatformTheme(priv);
}

//  a Python function taken by a CuteQPlatformTheme, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformTheme(
    QPlatformTheme *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformTheme *>(self)->take(key, call);
}

//  QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_own_ZNK14QPlatformTheme22createPlatformMenuItemEv(
    const QPlatformTheme *self) {
  return self->QPlatformTheme::createPlatformMenuItem();
}

//  QPlatformMenu *QPlatformTheme::createPlatformMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_own_ZNK14QPlatformTheme18createPlatformMenuEv(
    const QPlatformTheme *self) {
  return self->QPlatformTheme::createPlatformMenu();
}

//  QPlatformMenuBar *QPlatformTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_own_ZNK14QPlatformTheme21createPlatformMenuBarEv(
    const QPlatformTheme *self) {
  return self->QPlatformTheme::createPlatformMenuBar();
}

//  void QPlatformTheme::showPlatformMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlatformTheme19showPlatformMenuBarEv(
    QPlatformTheme *self) {
  self->QPlatformTheme::showPlatformMenuBar();
}

//  bool QPlatformTheme::usePlatformNativeDialog(DialogType type) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTypeE(
    const QPlatformTheme *self,
    QPlatformTheme::DialogType type) {
  return self->QPlatformTheme::usePlatformNativeDialog(type);
}

//  QPlatformDialogHelper
//      *QPlatformTheme::createPlatformDialogHelper(DialogType type) const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper *ritual_own_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10DialogTypeE(
    const QPlatformTheme *self,
    QPlatformTheme::DialogType type) {
  return self->QPlatformTheme::createPlatformDialogHelper(type);
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QPlatformSystemTrayIcon *QPlatformTheme::createPlatformSystemTrayIcon()
//      const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_own_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv(
    const QPlatformTheme *self) {
  return self->QPlatformTheme::createPlatformSystemTrayIcon();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  Qt::ColorScheme QPlatformTheme::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_own_ZNK14QPlatformTheme11colorSchemeEv(
    const QPlatformTheme *self) {
  return self->QPlatformTheme::colorScheme();
}

//  const QPalette *QPlatformTheme::palette(Palette type) const
extern "C" Q_DECL_EXPORT
const QPalette *ritual_own_ZNK14QPlatformTheme7paletteENS_7PaletteE(
    const QPlatformTheme *self,
    QPlatformTheme::Palette type) {
  return self->QPlatformTheme::palette(type);
}

//  const QFont *QPlatformTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_own_ZNK14QPlatformTheme4fontENS_4FontE(
    const QPlatformTheme *self,
    QPlatformTheme::Font type) {
  return self->QPlatformTheme::font(type);
}

//  QVariant QPlatformTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE(
    const QPlatformTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->QPlatformTheme::themeHint(hint));
}

//  QPixmap QPlatformTheme::standardPixmap(StandardPixmap sp, const QSizeF
//      &size) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixmapERK6QSizeF(
    const QPlatformTheme *self,
    QPlatformTheme::StandardPixmap sp,
    const QSizeF *size) {
  return new QPixmap(self->QPlatformTheme::standardPixmap(sp, *size));
}

//  QIcon QPlatformTheme::fileIcon(const QFileInfo &fileInfo,
//      QPlatformTheme::IconOptions iconOptions) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_10IconOptionEE(
    const QPlatformTheme *self,
    const QFileInfo *fileInfo,
    int iconOptions) {
  return new QIcon(
      self->QPlatformTheme::fileIcon(
          *fileInfo,
          QFlags<QPlatformTheme::IconOption>::fromInt(iconOptions)));
}

//  QIconEngine *QPlatformTheme::createIconEngine(const QString &iconName)
//      const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_own_ZNK14QPlatformTheme16createIconEngineERK7QString(
    const QPlatformTheme *self,
    const QString *iconName) {
  return self->QPlatformTheme::createIconEngine(*iconName);
}

//  QString QPlatformTheme::standardButtonText(int button) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QPlatformTheme18standardButtonTextEi(
    const QPlatformTheme *self,
    int button) {
  return new QString(self->QPlatformTheme::standardButtonText(button));
}

#if QT_CONFIG(shortcut)
//  QKeySequence QPlatformTheme::standardButtonShortcut(int button) const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_own_ZNK14QPlatformTheme22standardButtonShortcutEi(
    const QPlatformTheme *self,
    int button) {
  return new QKeySequence(
      self->QPlatformTheme::standardButtonShortcut(
          button));
}
#endif  // QT_CONFIG(shortcut)

//  void QPlatformTheme::requestColorScheme(Qt::ColorScheme scheme)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSchemeE(
    QPlatformTheme *self,
    Qt::ColorScheme scheme) {
  self->QPlatformTheme::requestColorScheme(scheme);
}

//  Qt::ContrastPreference QPlatformTheme::contrastPreference() const
extern "C" Q_DECL_EXPORT
Qt::ContrastPreference ritual_own_ZNK14QPlatformTheme18contrastPreferenceEv(
    const QPlatformTheme *self) {
  return self->QPlatformTheme::contrastPreference();
}

//  Qt::MotionPreference QPlatformTheme::motionPreference() const
extern "C" Q_DECL_EXPORT
Qt::MotionPreference ritual_own_ZNK14QPlatformTheme16motionPreferenceEv(
    const QPlatformTheme *self) {
  return self->QPlatformTheme::motionPreference();
}
