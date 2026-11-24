//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgenericunixtheme_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_UNIX) && (((QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))) || QT_CONFIG(wayland))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgenericunixtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGenericUnixTheme that Python can take functions over in. Every QGenericUnixTheme
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGenericUnixThemeCall0)(const void *, int, int *);
typedef const QVariant * (*CuteQGenericUnixThemeCall1)(const void *, int, int *);
#if QT_CONFIG(dbus)
typedef void * (*CuteQGenericUnixThemeCall2)(const void *, int *);
#endif  // QT_CONFIG(dbus)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
typedef void * (*CuteQGenericUnixThemeCall3)(const void *, int *);
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
typedef void * (*CuteQGenericUnixThemeCall4)(const void *, int *);
typedef void * (*CuteQGenericUnixThemeCall5)(const void *, int *);
typedef void (*CuteQGenericUnixThemeCall6)(const void *, int *);
typedef bool (*CuteQGenericUnixThemeCall7)(const void *, int, int *);
typedef void * (*CuteQGenericUnixThemeCall8)(const void *, int, int *);
typedef int (*CuteQGenericUnixThemeCall9)(const void *, int *);
typedef void * (*CuteQGenericUnixThemeCall10)(const void *, int, int *);
typedef const QPixmap * (*CuteQGenericUnixThemeCall11)(const void *, int, const QSizeF *, int *);
typedef const QIcon * (*CuteQGenericUnixThemeCall12)(const void *, const QFileInfo *, int, int *);
typedef void * (*CuteQGenericUnixThemeCall13)(const void *, const QString *, int *);
typedef QString * (*CuteQGenericUnixThemeCall14)(const void *, int, int *);
#if QT_CONFIG(shortcut)
typedef const QKeySequence * (*CuteQGenericUnixThemeCall15)(const void *, int, int *);
#endif  // QT_CONFIG(shortcut)
typedef void (*CuteQGenericUnixThemeCall16)(const void *, int, int *);
typedef int (*CuteQGenericUnixThemeCall17)(const void *, int *);
typedef int (*CuteQGenericUnixThemeCall18)(const void *, int *);
class CuteQGenericUnixTheme : public QGenericUnixTheme {
public:
  using QGenericUnixTheme::QGenericUnixTheme;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QPlatformTheme4fontENS_4FontE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme21createPlatformMenuBarEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme22createPlatformMenuItemEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18createPlatformMenuEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlatformTheme19showPlatformMenuBarEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTypeE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10DialogTypeE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme11colorSchemeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme7paletteENS_7PaletteE")) {
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

  //  const QFont *QGenericUnixTheme::font(Font type) const
  const QFont *font(QPlatformTheme::Font type) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGenericUnixThemeCall0 call = reinterpret_cast<CuteQGenericUnixThemeCall0>(taken[0]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<const QFont *>(given);
    }
    return QGenericUnixTheme::font(type);
  }

  //  QVariant QGenericUnixTheme::themeHint(ThemeHint hint) const
  QVariant themeHint(QPlatformTheme::ThemeHint hint) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGenericUnixThemeCall1 call = reinterpret_cast<CuteQGenericUnixThemeCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QGenericUnixTheme::themeHint(hint);
  }

#if QT_CONFIG(dbus)
  //  QPlatformMenuBar *QGenericUnixTheme::createPlatformMenuBar() const
  QPlatformMenuBar *createPlatformMenuBar() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGenericUnixThemeCall2 call = reinterpret_cast<CuteQGenericUnixThemeCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuBar *>(given);
    }
    return QGenericUnixTheme::createPlatformMenuBar();
  }
#endif  // QT_CONFIG(dbus)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
  //  QPlatformSystemTrayIcon
  //      *QGenericUnixTheme::createPlatformSystemTrayIcon() const
  QPlatformSystemTrayIcon *createPlatformSystemTrayIcon() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGenericUnixThemeCall3 call = reinterpret_cast<CuteQGenericUnixThemeCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSystemTrayIcon *>(given);
    }
    return QGenericUnixTheme::createPlatformSystemTrayIcon();
  }
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

  //  QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem() const
  QPlatformMenuItem *createPlatformMenuItem() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGenericUnixThemeCall4 call = reinterpret_cast<CuteQGenericUnixThemeCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuItem *>(given);
    }
    return QPlatformTheme::createPlatformMenuItem();
  }

  //  QPlatformMenu *QPlatformTheme::createPlatformMenu() const
  QPlatformMenu *createPlatformMenu() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGenericUnixThemeCall5 call = reinterpret_cast<CuteQGenericUnixThemeCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QPlatformTheme::createPlatformMenu();
  }

  //  void QPlatformTheme::showPlatformMenuBar()
  void showPlatformMenuBar() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGenericUnixThemeCall6 call = reinterpret_cast<CuteQGenericUnixThemeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformTheme::showPlatformMenuBar();
  }

  //  bool QPlatformTheme::usePlatformNativeDialog(DialogType type) const
  bool usePlatformNativeDialog(
      QPlatformTheme::DialogType type) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGenericUnixThemeCall7 call = reinterpret_cast<CuteQGenericUnixThemeCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQGenericUnixThemeCall8 call = reinterpret_cast<CuteQGenericUnixThemeCall8>(taken[8]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<QPlatformDialogHelper *>(given);
    }
    return QPlatformTheme::createPlatformDialogHelper(type);
  }

  //  Qt::ColorScheme QPlatformTheme::colorScheme() const
  Qt::ColorScheme colorScheme() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGenericUnixThemeCall9 call = reinterpret_cast<CuteQGenericUnixThemeCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ColorScheme>(given);
    }
    return QPlatformTheme::colorScheme();
  }

  //  const QPalette *QPlatformTheme::palette(Palette type) const
  const QPalette *palette(QPlatformTheme::Palette type) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGenericUnixThemeCall10 call = reinterpret_cast<CuteQGenericUnixThemeCall10>(taken[10]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<const QPalette *>(given);
    }
    return QPlatformTheme::palette(type);
  }

  //  QPixmap QPlatformTheme::standardPixmap(StandardPixmap sp, const
  //      QSizeF &size) const
  QPixmap standardPixmap(
      QPlatformTheme::StandardPixmap sp,
      const QSizeF &size) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGenericUnixThemeCall11 call = reinterpret_cast<CuteQGenericUnixThemeCall11>(taken[11]);
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
      CuteQGenericUnixThemeCall12 call = reinterpret_cast<CuteQGenericUnixThemeCall12>(taken[12]);
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
      CuteQGenericUnixThemeCall13 call = reinterpret_cast<CuteQGenericUnixThemeCall13>(taken[13]);
      void * given = call(this, &iconName, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QPlatformTheme::createIconEngine(iconName);
  }

  //  QString QPlatformTheme::standardButtonText(int button) const
  QString standardButtonText(int button) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQGenericUnixThemeCall14 call = reinterpret_cast<CuteQGenericUnixThemeCall14>(taken[14]);
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
      CuteQGenericUnixThemeCall15 call = reinterpret_cast<CuteQGenericUnixThemeCall15>(taken[15]);
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
      CuteQGenericUnixThemeCall16 call = reinterpret_cast<CuteQGenericUnixThemeCall16>(taken[16]);
      call(this, static_cast<int>(scheme), &handled);
      if (handled) return;
    }
    QPlatformTheme::requestColorScheme(scheme);
  }

  //  Qt::ContrastPreference QPlatformTheme::contrastPreference() const
  Qt::ContrastPreference contrastPreference() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGenericUnixThemeCall17 call = reinterpret_cast<CuteQGenericUnixThemeCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ContrastPreference>(given);
    }
    return QPlatformTheme::contrastPreference();
  }

  //  Qt::MotionPreference QPlatformTheme::motionPreference() const
  Qt::MotionPreference motionPreference() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQGenericUnixThemeCall18 call = reinterpret_cast<CuteQGenericUnixThemeCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::MotionPreference>(given);
    }
    return QPlatformTheme::motionPreference();
  }
};

//  QGenericUnixThemePrivate *QGenericUnixTheme::d_func()
extern "C" Q_DECL_EXPORT
QGenericUnixThemePrivate *ritual_ZN17QGenericUnixTheme6d_funcEv(
    QGenericUnixTheme *self) {
  return self->d_func();
}

//  const QGenericUnixThemePrivate *QGenericUnixTheme::d_func() const
extern "C" Q_DECL_EXPORT
const QGenericUnixThemePrivate *ritual_ZNK17QGenericUnixTheme6d_funcEv(
    const QGenericUnixTheme *self) {
  return self->d_func();
}

//  QGenericUnixTheme::QGenericUnixTheme(QGenericUnixThemePrivate *p)
extern "C" Q_DECL_EXPORT
QGenericUnixTheme *ritual_ZN17QGenericUnixThemeC1EP24QGenericUnixThemePrivate(
    QGenericUnixThemePrivate *p) {
  return new CuteQGenericUnixTheme(p);
}

//  QGenericUnixTheme::QGenericUnixTheme()
extern "C" Q_DECL_EXPORT
QGenericUnixTheme *ritual_ZN17QGenericUnixThemeC1Ev() {
  return new CuteQGenericUnixTheme();
}

//  const QFont *QGenericUnixTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_ZNK17QGenericUnixTheme4fontEN14QPlatformTheme4FontE(
    const QGenericUnixTheme *self,
    QPlatformTheme::Font type) {
  return self->font(type);
}

//  QVariant QGenericUnixTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QGenericUnixTheme9themeHintEN14QPlatformTheme9ThemeHintE(
    const QGenericUnixTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->themeHint(hint));
}

#if QT_CONFIG(dbus)
//  QPlatformMenuBar *QGenericUnixTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_ZNK17QGenericUnixTheme21createPlatformMenuBarEv(
    const QGenericUnixTheme *self) {
  return self->createPlatformMenuBar();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
//  QPlatformSystemTrayIcon
//      *QGenericUnixTheme::createPlatformSystemTrayIcon() const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_ZNK17QGenericUnixTheme28createPlatformSystemTrayIconEv(
    const QGenericUnixTheme *self) {
  return self->createPlatformSystemTrayIcon();
}
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)

//  QStringList QGenericUnixTheme::xdgIconThemePaths()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN17QGenericUnixTheme17xdgIconThemePathsEv() {
  return new QList<QString>(QGenericUnixTheme::xdgIconThemePaths());
}

//  QPlatformTheme *QGenericUnixTheme::createUnixTheme(const QString &name)
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_ZN17QGenericUnixTheme15createUnixThemeERK7QString(
    const QString *name) {
  return QGenericUnixTheme::createUnixTheme(*name);
}

//  QStringList QGenericUnixTheme::themeNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN17QGenericUnixTheme10themeNamesEv() {
  return new QList<QString>(QGenericUnixTheme::themeNames());
}

//  QStringList QGenericUnixTheme::iconFallbackPaths()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN17QGenericUnixTheme17iconFallbackPathsEv() {
  return new QList<QString>(QGenericUnixTheme::iconFallbackPaths());
}

//  bool QGenericUnixTheme::isDBusGlobalMenuAvailable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGenericUnixTheme25isDBusGlobalMenuAvailableEv() {
  return QGenericUnixTheme::isDBusGlobalMenuAvailable();
}

//  QString QGenericUnixTheme::mouseCursorTheme()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGenericUnixTheme16mouseCursorThemeEv() {
  return new QString(QGenericUnixTheme::mouseCursorTheme());
}

//  QSize QGenericUnixTheme::mouseCursorSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN17QGenericUnixTheme15mouseCursorSizeEv() {
  return new QSize(QGenericUnixTheme::mouseCursorSize());
}

//  QList<QSize> QGenericUnixTheme::availableXdgFileIconSizes()
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN17QGenericUnixTheme25availableXdgFileIconSizesEv() {
  return new QList<QSize>(QGenericUnixTheme::availableXdgFileIconSizes());
}

#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
//  bool QGenericUnixTheme::shouldUseDBusTray()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGenericUnixTheme17shouldUseDBusTrayEv() {
  return QGenericUnixTheme::shouldUseDBusTray();
}
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)

#if QT_CONFIG(mimetype)
//  QIcon QGenericUnixTheme::xdgFileIcon(const QFileInfo &fileInfo)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN17QGenericUnixTheme11xdgFileIconERK9QFileInfo(
    const QFileInfo *fileInfo) {
  return new QIcon(QGenericUnixTheme::xdgFileIcon(*fileInfo));
}
#endif  // QT_CONFIG(mimetype)

//  a Python function taken by a CuteQGenericUnixTheme, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGenericUnixTheme(
    QGenericUnixTheme *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGenericUnixTheme *>(self)->take(key, call);
}

//  const QFont *QGenericUnixTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_own_ZNK17QGenericUnixTheme4fontEN14QPlatformTheme4FontE(
    const QGenericUnixTheme *self,
    QPlatformTheme::Font type) {
  return self->QGenericUnixTheme::font(type);
}

//  QVariant QGenericUnixTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QGenericUnixTheme9themeHintEN14QPlatformTheme9ThemeHintE(
    const QGenericUnixTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->QGenericUnixTheme::themeHint(hint));
}

#if QT_CONFIG(dbus)
//  QPlatformMenuBar *QGenericUnixTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_own_ZNK17QGenericUnixTheme21createPlatformMenuBarEv(
    const QGenericUnixTheme *self) {
  return self->QGenericUnixTheme::createPlatformMenuBar();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
//  QPlatformSystemTrayIcon
//      *QGenericUnixTheme::createPlatformSystemTrayIcon() const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_own_ZNK17QGenericUnixTheme28createPlatformSystemTrayIconEv(
    const QGenericUnixTheme *self) {
  return self->QGenericUnixTheme::createPlatformSystemTrayIcon();
}
#endif  // QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)

#endif  // defined(Q_OS_UNIX) && (((QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))) || QT_CONFIG(wayland))
