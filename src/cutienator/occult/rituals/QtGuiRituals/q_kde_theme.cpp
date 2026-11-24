//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qkdetheme_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_UNIX) && QT_CONFIG(settings) && QT_CONFIG(dbus) && (QT_CONFIG(xcb) || QT_CONFIG(wayland))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qkdetheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QKdeTheme that Python can take functions over in. Every QKdeTheme
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQKdeThemeCall0)(const void *, int, int *);
typedef const QIcon * (*CuteQKdeThemeCall1)(const void *, const QFileInfo *, int, int *);
typedef void * (*CuteQKdeThemeCall2)(const void *, int, int *);
typedef int (*CuteQKdeThemeCall3)(const void *, int *);
typedef void (*CuteQKdeThemeCall4)(const void *, int, int *);
typedef void * (*CuteQKdeThemeCall5)(const void *, int, int *);
#if QT_CONFIG(dbus)
typedef void * (*CuteQKdeThemeCall6)(const void *, int *);
#endif  // QT_CONFIG(dbus)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
typedef void * (*CuteQKdeThemeCall7)(const void *, int *);
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
typedef void * (*CuteQKdeThemeCall8)(const void *, int *);
typedef void * (*CuteQKdeThemeCall9)(const void *, int *);
typedef void (*CuteQKdeThemeCall10)(const void *, int *);
typedef bool (*CuteQKdeThemeCall11)(const void *, int, int *);
typedef void * (*CuteQKdeThemeCall12)(const void *, int, int *);
typedef const QPixmap * (*CuteQKdeThemeCall13)(const void *, int, const QSizeF *, int *);
typedef void * (*CuteQKdeThemeCall14)(const void *, const QString *, int *);
typedef QString * (*CuteQKdeThemeCall15)(const void *, int, int *);
#if QT_CONFIG(shortcut)
typedef const QKeySequence * (*CuteQKdeThemeCall16)(const void *, int, int *);
#endif  // QT_CONFIG(shortcut)
typedef int (*CuteQKdeThemeCall17)(const void *, int *);
typedef int (*CuteQKdeThemeCall18)(const void *, int *);
class CuteQKdeTheme : public QKdeTheme {
public:
  using QKdeTheme::QKdeTheme;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_10IconOptionEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme7paletteENS_7PaletteE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme11colorSchemeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSchemeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme4fontENS_4FontE")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme21createPlatformMenuBarEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme22createPlatformMenuItemEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18createPlatformMenuEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlatformTheme19showPlatformMenuBarEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTypeE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10DialogTypeE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixmapERK6QSizeF")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme16createIconEngineERK7QString")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18standardButtonTextEi")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme22standardButtonShortcutEi")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(shortcut)
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

  //  QVariant QKdeTheme::themeHint(ThemeHint hint) const
  QVariant themeHint(QPlatformTheme::ThemeHint hint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQKdeThemeCall0 call = reinterpret_cast<CuteQKdeThemeCall0>(taken[0]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QKdeTheme::themeHint(hint);
  }

  //  QIcon QKdeTheme::fileIcon(const QFileInfo &fileInfo,
  //      QPlatformTheme::IconOptions iconOptions) const
  QIcon fileIcon(
      const QFileInfo &fileInfo,
      QPlatformTheme::IconOptions iconOptions) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQKdeThemeCall1 call = reinterpret_cast<CuteQKdeThemeCall1>(taken[1]);
      const QIcon * given = call(this, &fileInfo, static_cast<int>(iconOptions.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QKdeTheme::fileIcon(fileInfo, iconOptions);
  }

  //  const QPalette *QKdeTheme::palette(Palette type) const
  const QPalette *palette(QPlatformTheme::Palette type) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQKdeThemeCall2 call = reinterpret_cast<CuteQKdeThemeCall2>(taken[2]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<const QPalette *>(given);
    }
    return QKdeTheme::palette(type);
  }

  //  Qt::ColorScheme QKdeTheme::colorScheme() const
  Qt::ColorScheme colorScheme() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQKdeThemeCall3 call = reinterpret_cast<CuteQKdeThemeCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ColorScheme>(given);
    }
    return QKdeTheme::colorScheme();
  }

  //  void QKdeTheme::requestColorScheme(Qt::ColorScheme scheme)
  void requestColorScheme(Qt::ColorScheme scheme) override {
    if (taken[4]) {
      int handled = 0;
      CuteQKdeThemeCall4 call = reinterpret_cast<CuteQKdeThemeCall4>(taken[4]);
      call(this, static_cast<int>(scheme), &handled);
      if (handled) return;
    }
    QKdeTheme::requestColorScheme(scheme);
  }

  //  const QFont *QKdeTheme::font(Font type) const
  const QFont *font(QPlatformTheme::Font type) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQKdeThemeCall5 call = reinterpret_cast<CuteQKdeThemeCall5>(taken[5]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<const QFont *>(given);
    }
    return QKdeTheme::font(type);
  }

#if QT_CONFIG(dbus)
  //  QPlatformMenuBar *QKdeTheme::createPlatformMenuBar() const
  QPlatformMenuBar *createPlatformMenuBar() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQKdeThemeCall6 call = reinterpret_cast<CuteQKdeThemeCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuBar *>(given);
    }
    return QKdeTheme::createPlatformMenuBar();
  }
#endif  // QT_CONFIG(dbus)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
  //  QPlatformSystemTrayIcon *QKdeTheme::createPlatformSystemTrayIcon()
  //      const
  QPlatformSystemTrayIcon *createPlatformSystemTrayIcon() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQKdeThemeCall7 call = reinterpret_cast<CuteQKdeThemeCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSystemTrayIcon *>(given);
    }
    return QKdeTheme::createPlatformSystemTrayIcon();
  }
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

  //  QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem() const
  QPlatformMenuItem *createPlatformMenuItem() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQKdeThemeCall8 call = reinterpret_cast<CuteQKdeThemeCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuItem *>(given);
    }
    return QPlatformTheme::createPlatformMenuItem();
  }

  //  QPlatformMenu *QPlatformTheme::createPlatformMenu() const
  QPlatformMenu *createPlatformMenu() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQKdeThemeCall9 call = reinterpret_cast<CuteQKdeThemeCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QPlatformTheme::createPlatformMenu();
  }

  //  void QPlatformTheme::showPlatformMenuBar()
  void showPlatformMenuBar() override {
    if (taken[10]) {
      int handled = 0;
      CuteQKdeThemeCall10 call = reinterpret_cast<CuteQKdeThemeCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformTheme::showPlatformMenuBar();
  }

  //  bool QPlatformTheme::usePlatformNativeDialog(DialogType type) const
  bool usePlatformNativeDialog(
      QPlatformTheme::DialogType type) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQKdeThemeCall11 call = reinterpret_cast<CuteQKdeThemeCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQKdeThemeCall12 call = reinterpret_cast<CuteQKdeThemeCall12>(taken[12]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<QPlatformDialogHelper *>(given);
    }
    return QPlatformTheme::createPlatformDialogHelper(type);
  }

  //  QPixmap QPlatformTheme::standardPixmap(StandardPixmap sp, const
  //      QSizeF &size) const
  QPixmap standardPixmap(
      QPlatformTheme::StandardPixmap sp,
      const QSizeF &size) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQKdeThemeCall13 call = reinterpret_cast<CuteQKdeThemeCall13>(taken[13]);
      const QPixmap * given = call(this, static_cast<int>(sp), &size, &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::standardPixmap(sp, size);
  }

  //  QIconEngine *QPlatformTheme::createIconEngine(const QString
  //      &iconName) const
  QIconEngine *createIconEngine(const QString &iconName) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQKdeThemeCall14 call = reinterpret_cast<CuteQKdeThemeCall14>(taken[14]);
      void * given = call(this, &iconName, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QPlatformTheme::createIconEngine(iconName);
  }

  //  QString QPlatformTheme::standardButtonText(int button) const
  QString standardButtonText(int button) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQKdeThemeCall15 call = reinterpret_cast<CuteQKdeThemeCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQKdeThemeCall16 call = reinterpret_cast<CuteQKdeThemeCall16>(taken[16]);
      const QKeySequence * given = call(this, button, &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::standardButtonShortcut(button);
  }
#endif  // QT_CONFIG(shortcut)

  //  Qt::ContrastPreference QPlatformTheme::contrastPreference() const
  Qt::ContrastPreference contrastPreference() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQKdeThemeCall17 call = reinterpret_cast<CuteQKdeThemeCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ContrastPreference>(given);
    }
    return QPlatformTheme::contrastPreference();
  }

  //  Qt::MotionPreference QPlatformTheme::motionPreference() const
  Qt::MotionPreference motionPreference() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQKdeThemeCall18 call = reinterpret_cast<CuteQKdeThemeCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::MotionPreference>(given);
    }
    return QPlatformTheme::motionPreference();
  }
};

//  QKdeTheme::QKdeTheme(const QStringList &kdeDirs, int kdeVersion)
extern "C" Q_DECL_EXPORT
QKdeTheme *ritual_ZN9QKdeThemeC1ERK5QListI7QStringEi(
    const QList<QString> *kdeDirs,
    int kdeVersion) {
  return new CuteQKdeTheme(*kdeDirs, kdeVersion);
}

//  QKdeTheme::~QKdeTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QKdeThemeD1Ev(QKdeTheme *self) {
  delete self;
}

//  QPlatformTheme *QKdeTheme::createKdeTheme()
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_ZN9QKdeTheme14createKdeThemeEv() {
  return QKdeTheme::createKdeTheme();
}

//  QVariant QKdeTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QKdeTheme9themeHintEN14QPlatformTheme9ThemeHintE(
    const QKdeTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->themeHint(hint));
}

//  QIcon QKdeTheme::fileIcon(const QFileInfo &fileInfo,
//      QPlatformTheme::IconOptions iconOptions) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK9QKdeTheme8fileIconERK9QFileInfo6QFlagsIN14QPlatformTheme10IconOptionEE(
    const QKdeTheme *self,
    const QFileInfo *fileInfo,
    int iconOptions) {
  return new QIcon(
      self->fileIcon(
          *fileInfo,
          QFlags<QPlatformTheme::IconOption>::fromInt(iconOptions)));
}

//  const QPalette *QKdeTheme::palette(Palette type) const
extern "C" Q_DECL_EXPORT
const QPalette *ritual_ZNK9QKdeTheme7paletteEN14QPlatformTheme7PaletteE(
    const QKdeTheme *self,
    QPlatformTheme::Palette type) {
  return self->palette(type);
}

//  Qt::ColorScheme QKdeTheme::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK9QKdeTheme11colorSchemeEv(const QKdeTheme *self) {
  return self->colorScheme();
}

//  void QKdeTheme::requestColorScheme(Qt::ColorScheme scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QKdeTheme18requestColorSchemeEN2Qt11ColorSchemeE(
    QKdeTheme *self,
    Qt::ColorScheme scheme) {
  self->requestColorScheme(scheme);
}

//  const QFont *QKdeTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_ZNK9QKdeTheme4fontEN14QPlatformTheme4FontE(
    const QKdeTheme *self,
    QPlatformTheme::Font type) {
  return self->font(type);
}

#if QT_CONFIG(dbus)
//  QPlatformMenuBar *QKdeTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_ZNK9QKdeTheme21createPlatformMenuBarEv(
    const QKdeTheme *self) {
  return self->createPlatformMenuBar();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
//  QPlatformSystemTrayIcon *QKdeTheme::createPlatformSystemTrayIcon() const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_ZNK9QKdeTheme28createPlatformSystemTrayIconEv(
    const QKdeTheme *self) {
  return self->createPlatformSystemTrayIcon();
}
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)

//  a Python function taken by a CuteQKdeTheme, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QKdeTheme(QKdeTheme *self, const char *key, void *call) {
  return static_cast<CuteQKdeTheme *>(self)->take(key, call);
}

//  QVariant QKdeTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK9QKdeTheme9themeHintEN14QPlatformTheme9ThemeHintE(
    const QKdeTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->QKdeTheme::themeHint(hint));
}

//  QIcon QKdeTheme::fileIcon(const QFileInfo &fileInfo,
//      QPlatformTheme::IconOptions iconOptions) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK9QKdeTheme8fileIconERK9QFileInfo6QFlagsIN14QPlatformTheme10IconOptionEE(
    const QKdeTheme *self,
    const QFileInfo *fileInfo,
    int iconOptions) {
  return new QIcon(
      self->QKdeTheme::fileIcon(
          *fileInfo,
          QFlags<QPlatformTheme::IconOption>::fromInt(iconOptions)));
}

//  const QPalette *QKdeTheme::palette(Palette type) const
extern "C" Q_DECL_EXPORT
const QPalette *ritual_own_ZNK9QKdeTheme7paletteEN14QPlatformTheme7PaletteE(
    const QKdeTheme *self,
    QPlatformTheme::Palette type) {
  return self->QKdeTheme::palette(type);
}

//  Qt::ColorScheme QKdeTheme::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_own_ZNK9QKdeTheme11colorSchemeEv(
    const QKdeTheme *self) {
  return self->QKdeTheme::colorScheme();
}

//  void QKdeTheme::requestColorScheme(Qt::ColorScheme scheme)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QKdeTheme18requestColorSchemeEN2Qt11ColorSchemeE(
    QKdeTheme *self,
    Qt::ColorScheme scheme) {
  self->QKdeTheme::requestColorScheme(scheme);
}

//  const QFont *QKdeTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_own_ZNK9QKdeTheme4fontEN14QPlatformTheme4FontE(
    const QKdeTheme *self,
    QPlatformTheme::Font type) {
  return self->QKdeTheme::font(type);
}

#if QT_CONFIG(dbus)
//  QPlatformMenuBar *QKdeTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_own_ZNK9QKdeTheme21createPlatformMenuBarEv(
    const QKdeTheme *self) {
  return self->QKdeTheme::createPlatformMenuBar();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
//  QPlatformSystemTrayIcon *QKdeTheme::createPlatformSystemTrayIcon() const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_own_ZNK9QKdeTheme28createPlatformSystemTrayIconEv(
    const QKdeTheme *self) {
  return self->QKdeTheme::createPlatformSystemTrayIcon();
}
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)

#endif  // defined(Q_OS_UNIX) && QT_CONFIG(settings) && QT_CONFIG(dbus) && (QT_CONFIG(xcb) || QT_CONFIG(wayland))
