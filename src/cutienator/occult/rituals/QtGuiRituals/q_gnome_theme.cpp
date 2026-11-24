//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgnometheme_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgnometheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qicon.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qkeysequence.h>
#include <cstring>

//  Only a class built on QGnomeTheme may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGnomeTheme : QGnomeTheme {
  using QGnomeTheme::updateColorScheme;
  using QGnomeTheme::updateHighContrast;
  using QGnomeTheme::updateReducedMotion;
};

//  A QGnomeTheme that Python can take functions over in. Every QGnomeTheme
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQGnomeThemeCall0)(const void *, int, int *);
typedef const QIcon * (*CuteQGnomeThemeCall1)(const void *, const QFileInfo *, int, int *);
typedef void * (*CuteQGnomeThemeCall2)(const void *, int, int *);
typedef QString * (*CuteQGnomeThemeCall3)(const void *, int, int *);
typedef QString * (*CuteQGnomeThemeCall4)(const void *, int *);
typedef void (*CuteQGnomeThemeCall5)(const void *, int, int *);
typedef int (*CuteQGnomeThemeCall6)(const void *, int *);
#if QT_CONFIG(dbus)
typedef void (*CuteQGnomeThemeCall7)(const void *, int, int *);
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
typedef void (*CuteQGnomeThemeCall8)(const void *, int, int *);
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
typedef void (*CuteQGnomeThemeCall9)(const void *, int, int *);
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
typedef void * (*CuteQGnomeThemeCall10)(const void *, int *);
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
typedef int (*CuteQGnomeThemeCall11)(const void *, int *);
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
typedef int (*CuteQGnomeThemeCall12)(const void *, int *);
#endif  // QT_CONFIG(dbus)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus)
#if QT_CONFIG(systemtrayicon)
typedef void * (*CuteQGnomeThemeCall13)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // QT_CONFIG(dbus)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
typedef void * (*CuteQGnomeThemeCall14)(const void *, int *);
typedef void * (*CuteQGnomeThemeCall15)(const void *, int *);
typedef void (*CuteQGnomeThemeCall16)(const void *, int *);
typedef bool (*CuteQGnomeThemeCall17)(const void *, int, int *);
typedef void * (*CuteQGnomeThemeCall18)(const void *, int, int *);
typedef void * (*CuteQGnomeThemeCall19)(const void *, int, int *);
typedef const QPixmap * (*CuteQGnomeThemeCall20)(const void *, int, const QSizeF *, int *);
typedef void * (*CuteQGnomeThemeCall21)(const void *, const QString *, int *);
#if QT_CONFIG(shortcut)
typedef const QKeySequence * (*CuteQGnomeThemeCall22)(const void *, int, int *);
#endif  // QT_CONFIG(shortcut)
class CuteQGnomeTheme : public QGnomeTheme {
public:
  using QGnomeTheme::QGnomeTheme;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_10IconOptionEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme4fontENS_4FontE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18standardButtonTextEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QGnomeTheme11gtkFontNameEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSchemeE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme11colorSchemeEv")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZN11QGnomeTheme17updateColorSchemeEN2Qt11ColorSchemeE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZN11QGnomeTheme18updateHighContrastEN2Qt18ContrastPreferenceE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZN11QGnomeTheme19updateReducedMotionEN2Qt16MotionPreferenceE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme21createPlatformMenuBarEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18contrastPreferenceEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if QT_CONFIG(dbus)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme16motionPreferenceEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dbus)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // QT_CONFIG(dbus)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme22createPlatformMenuItemEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme18createPlatformMenuEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlatformTheme19showPlatformMenuBarEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTypeE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10DialogTypeE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme7paletteENS_7PaletteE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixmapERK6QSizeF")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlatformTheme16createIconEngineERK7QString")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZNK14QPlatformTheme22standardButtonShortcutEi")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(shortcut)
    return false;
  }

  //  QVariant QGnomeTheme::themeHint(ThemeHint hint) const
  QVariant themeHint(QPlatformTheme::ThemeHint hint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGnomeThemeCall0 call = reinterpret_cast<CuteQGnomeThemeCall0>(taken[0]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QGnomeTheme::themeHint(hint);
  }

  //  QIcon QGnomeTheme::fileIcon(const QFileInfo &fileInfo,
  //      QPlatformTheme::IconOptions a1) const
  QIcon fileIcon(
      const QFileInfo &fileInfo,
      QPlatformTheme::IconOptions a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGnomeThemeCall1 call = reinterpret_cast<CuteQGnomeThemeCall1>(taken[1]);
      const QIcon * given = call(this, &fileInfo, static_cast<int>(a1.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QGnomeTheme::fileIcon(fileInfo, a1);
  }

  //  const QFont *QGnomeTheme::font(Font type) const
  const QFont *font(QPlatformTheme::Font type) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGnomeThemeCall2 call = reinterpret_cast<CuteQGnomeThemeCall2>(taken[2]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<const QFont *>(given);
    }
    return QGnomeTheme::font(type);
  }

  //  QString QGnomeTheme::standardButtonText(int button) const
  QString standardButtonText(int button) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGnomeThemeCall3 call = reinterpret_cast<CuteQGnomeThemeCall3>(taken[3]);
      QString * given = call(this, button, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGnomeTheme::standardButtonText(button);
  }

  //  QString QGnomeTheme::gtkFontName() const
  QString gtkFontName() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGnomeThemeCall4 call = reinterpret_cast<CuteQGnomeThemeCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGnomeTheme::gtkFontName();
  }

  //  void QGnomeTheme::requestColorScheme(Qt::ColorScheme a0)
  void requestColorScheme(Qt::ColorScheme a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGnomeThemeCall5 call = reinterpret_cast<CuteQGnomeThemeCall5>(taken[5]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QGnomeTheme::requestColorScheme(a0);
  }

  //  Qt::ColorScheme QGnomeTheme::colorScheme() const
  Qt::ColorScheme colorScheme() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGnomeThemeCall6 call = reinterpret_cast<CuteQGnomeThemeCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ColorScheme>(given);
    }
    return QGnomeTheme::colorScheme();
  }

#if QT_CONFIG(dbus)
  //  void QGnomeTheme::updateColorScheme(Qt::ColorScheme a0)
  void updateColorScheme(Qt::ColorScheme a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGnomeThemeCall7 call = reinterpret_cast<CuteQGnomeThemeCall7>(taken[7]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QGnomeTheme::updateColorScheme(a0);
  }
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
  //  void QGnomeTheme::updateHighContrast(Qt::ContrastPreference a0)
  void updateHighContrast(Qt::ContrastPreference a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGnomeThemeCall8 call = reinterpret_cast<CuteQGnomeThemeCall8>(taken[8]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QGnomeTheme::updateHighContrast(a0);
  }
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
  //  void QGnomeTheme::updateReducedMotion(Qt::MotionPreference a0)
  void updateReducedMotion(Qt::MotionPreference a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGnomeThemeCall9 call = reinterpret_cast<CuteQGnomeThemeCall9>(taken[9]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QGnomeTheme::updateReducedMotion(a0);
  }
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
  //  QPlatformMenuBar *QGnomeTheme::createPlatformMenuBar() const
  QPlatformMenuBar *createPlatformMenuBar() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGnomeThemeCall10 call = reinterpret_cast<CuteQGnomeThemeCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuBar *>(given);
    }
    return QGnomeTheme::createPlatformMenuBar();
  }
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
  //  Qt::ContrastPreference QGnomeTheme::contrastPreference() const
  Qt::ContrastPreference contrastPreference() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGnomeThemeCall11 call = reinterpret_cast<CuteQGnomeThemeCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ContrastPreference>(given);
    }
    return QGnomeTheme::contrastPreference();
  }
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
  //  Qt::MotionPreference QGnomeTheme::motionPreference() const
  Qt::MotionPreference motionPreference() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGnomeThemeCall12 call = reinterpret_cast<CuteQGnomeThemeCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::MotionPreference>(given);
    }
    return QGnomeTheme::motionPreference();
  }
#endif  // QT_CONFIG(dbus)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(dbus)
#if QT_CONFIG(systemtrayicon)
  //  QPlatformSystemTrayIcon *QGnomeTheme::createPlatformSystemTrayIcon()
  //      const
  QPlatformSystemTrayIcon *createPlatformSystemTrayIcon() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGnomeThemeCall13 call = reinterpret_cast<CuteQGnomeThemeCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSystemTrayIcon *>(given);
    }
    return QGnomeTheme::createPlatformSystemTrayIcon();
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // QT_CONFIG(dbus)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

  //  QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem() const
  QPlatformMenuItem *createPlatformMenuItem() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQGnomeThemeCall14 call = reinterpret_cast<CuteQGnomeThemeCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuItem *>(given);
    }
    return QPlatformTheme::createPlatformMenuItem();
  }

  //  QPlatformMenu *QPlatformTheme::createPlatformMenu() const
  QPlatformMenu *createPlatformMenu() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGnomeThemeCall15 call = reinterpret_cast<CuteQGnomeThemeCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QPlatformTheme::createPlatformMenu();
  }

  //  void QPlatformTheme::showPlatformMenuBar()
  void showPlatformMenuBar() override {
    if (taken[16]) {
      int handled = 0;
      CuteQGnomeThemeCall16 call = reinterpret_cast<CuteQGnomeThemeCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformTheme::showPlatformMenuBar();
  }

  //  bool QPlatformTheme::usePlatformNativeDialog(DialogType type) const
  bool usePlatformNativeDialog(
      QPlatformTheme::DialogType type) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGnomeThemeCall17 call = reinterpret_cast<CuteQGnomeThemeCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQGnomeThemeCall18 call = reinterpret_cast<CuteQGnomeThemeCall18>(taken[18]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<QPlatformDialogHelper *>(given);
    }
    return QPlatformTheme::createPlatformDialogHelper(type);
  }

  //  const QPalette *QPlatformTheme::palette(Palette type) const
  const QPalette *palette(QPlatformTheme::Palette type) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQGnomeThemeCall19 call = reinterpret_cast<CuteQGnomeThemeCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQGnomeThemeCall20 call = reinterpret_cast<CuteQGnomeThemeCall20>(taken[20]);
      const QPixmap * given = call(this, static_cast<int>(sp), &size, &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::standardPixmap(sp, size);
  }

  //  QIconEngine *QPlatformTheme::createIconEngine(const QString
  //      &iconName) const
  QIconEngine *createIconEngine(const QString &iconName) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQGnomeThemeCall21 call = reinterpret_cast<CuteQGnomeThemeCall21>(taken[21]);
      void * given = call(this, &iconName, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QPlatformTheme::createIconEngine(iconName);
  }

#if QT_CONFIG(shortcut)
  //  QKeySequence QPlatformTheme::standardButtonShortcut(int button) const
  QKeySequence standardButtonShortcut(int button) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQGnomeThemeCall22 call = reinterpret_cast<CuteQGnomeThemeCall22>(taken[22]);
      const QKeySequence * given = call(this, button, &handled);
      if (handled && given) return *given;
    }
    return QPlatformTheme::standardButtonShortcut(button);
  }
#endif  // QT_CONFIG(shortcut)
};

//  QGnomeThemePrivate *QGnomeTheme::d_func()
extern "C" Q_DECL_EXPORT
QGnomeThemePrivate *ritual_ZN11QGnomeTheme6d_funcEv(QGnomeTheme *self) {
  return self->d_func();
}

//  const QGnomeThemePrivate *QGnomeTheme::d_func() const
extern "C" Q_DECL_EXPORT
const QGnomeThemePrivate *ritual_ZNK11QGnomeTheme6d_funcEv(
    const QGnomeTheme *self) {
  return self->d_func();
}

//  QGnomeTheme::QGnomeTheme()
extern "C" Q_DECL_EXPORT
QGnomeTheme *ritual_ZN11QGnomeThemeC1Ev() {
  return new CuteQGnomeTheme();
}

//  QVariant QGnomeTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QGnomeTheme9themeHintEN14QPlatformTheme9ThemeHintE(
    const QGnomeTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->themeHint(hint));
}

//  QIcon QGnomeTheme::fileIcon(const QFileInfo &fileInfo,
//      QPlatformTheme::IconOptions a1) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK11QGnomeTheme8fileIconERK9QFileInfo6QFlagsIN14QPlatformTheme10IconOptionEE(
    const QGnomeTheme *self,
    const QFileInfo *fileInfo,
    int a1) {
  return new QIcon(
      self->fileIcon(
          *fileInfo,
          QFlags<QPlatformTheme::IconOption>::fromInt(a1)));
}

//  const QFont *QGnomeTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_ZNK11QGnomeTheme4fontEN14QPlatformTheme4FontE(
    const QGnomeTheme *self,
    QPlatformTheme::Font type) {
  return self->font(type);
}

//  QString QGnomeTheme::standardButtonText(int button) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGnomeTheme18standardButtonTextEi(
    const QGnomeTheme *self,
    int button) {
  return new QString(self->standardButtonText(button));
}

//  QString QGnomeTheme::gtkFontName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGnomeTheme11gtkFontNameEv(const QGnomeTheme *self) {
  return new QString(self->gtkFontName());
}

//  void QGnomeTheme::requestColorScheme(Qt::ColorScheme a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGnomeTheme18requestColorSchemeEN2Qt11ColorSchemeE(
    QGnomeTheme *self,
    Qt::ColorScheme a0) {
  self->requestColorScheme(a0);
}

//  Qt::ColorScheme QGnomeTheme::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK11QGnomeTheme11colorSchemeEv(
    const QGnomeTheme *self) {
  return self->colorScheme();
}

#if QT_CONFIG(dbus)
//  void QGnomeTheme::updateColorScheme(Qt::ColorScheme a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGnomeTheme17updateColorSchemeEN2Qt11ColorSchemeE(
    QGnomeTheme *self,
    Qt::ColorScheme a0) {
  self->updateColorScheme(a0);
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  void QGnomeTheme::updateHighContrast(Qt::ContrastPreference a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGnomeTheme18updateHighContrastEN2Qt18ContrastPreferenceE(
    QGnomeTheme *self,
    Qt::ContrastPreference a0) {
  self->updateHighContrast(a0);
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  void QGnomeTheme::updateReducedMotion(Qt::MotionPreference a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGnomeTheme19updateReducedMotionEN2Qt16MotionPreferenceE(
    QGnomeTheme *self,
    Qt::MotionPreference a0) {
  self->updateReducedMotion(a0);
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  QPlatformMenuBar *QGnomeTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_ZNK11QGnomeTheme21createPlatformMenuBarEv(
    const QGnomeTheme *self) {
  return self->createPlatformMenuBar();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  Qt::ContrastPreference QGnomeTheme::contrastPreference() const
extern "C" Q_DECL_EXPORT
Qt::ContrastPreference ritual_ZNK11QGnomeTheme18contrastPreferenceEv(
    const QGnomeTheme *self) {
  return self->contrastPreference();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  Qt::MotionPreference QGnomeTheme::motionPreference() const
extern "C" Q_DECL_EXPORT
Qt::MotionPreference ritual_ZNK11QGnomeTheme16motionPreferenceEv(
    const QGnomeTheme *self) {
  return self->motionPreference();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
#if QT_CONFIG(systemtrayicon)
//  QPlatformSystemTrayIcon *QGnomeTheme::createPlatformSystemTrayIcon()
//      const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_ZNK11QGnomeTheme28createPlatformSystemTrayIconEv(
    const QGnomeTheme *self) {
  return self->createPlatformSystemTrayIcon();
}
#endif  // QT_CONFIG(systemtrayicon)
#endif  // QT_CONFIG(dbus)

//  a Python function taken by a CuteQGnomeTheme, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGnomeTheme(
    QGnomeTheme *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGnomeTheme *>(self)->take(key, call);
}

//  QVariant QGnomeTheme::themeHint(ThemeHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK11QGnomeTheme9themeHintEN14QPlatformTheme9ThemeHintE(
    const QGnomeTheme *self,
    QPlatformTheme::ThemeHint hint) {
  return new QVariant(self->QGnomeTheme::themeHint(hint));
}

//  QIcon QGnomeTheme::fileIcon(const QFileInfo &fileInfo,
//      QPlatformTheme::IconOptions a1) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK11QGnomeTheme8fileIconERK9QFileInfo6QFlagsIN14QPlatformTheme10IconOptionEE(
    const QGnomeTheme *self,
    const QFileInfo *fileInfo,
    int a1) {
  return new QIcon(
      self->QGnomeTheme::fileIcon(
          *fileInfo,
          QFlags<QPlatformTheme::IconOption>::fromInt(a1)));
}

//  const QFont *QGnomeTheme::font(Font type) const
extern "C" Q_DECL_EXPORT
const QFont *ritual_own_ZNK11QGnomeTheme4fontEN14QPlatformTheme4FontE(
    const QGnomeTheme *self,
    QPlatformTheme::Font type) {
  return self->QGnomeTheme::font(type);
}

//  QString QGnomeTheme::standardButtonText(int button) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QGnomeTheme18standardButtonTextEi(
    const QGnomeTheme *self,
    int button) {
  return new QString(self->QGnomeTheme::standardButtonText(button));
}

//  QString QGnomeTheme::gtkFontName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QGnomeTheme11gtkFontNameEv(
    const QGnomeTheme *self) {
  return new QString(self->QGnomeTheme::gtkFontName());
}

//  void QGnomeTheme::requestColorScheme(Qt::ColorScheme a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGnomeTheme18requestColorSchemeEN2Qt11ColorSchemeE(
    QGnomeTheme *self,
    Qt::ColorScheme a0) {
  self->QGnomeTheme::requestColorScheme(a0);
}

//  Qt::ColorScheme QGnomeTheme::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_own_ZNK11QGnomeTheme11colorSchemeEv(
    const QGnomeTheme *self) {
  return self->QGnomeTheme::colorScheme();
}

#if QT_CONFIG(dbus)
//  void QGnomeTheme::updateColorScheme(Qt::ColorScheme a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGnomeTheme17updateColorSchemeEN2Qt11ColorSchemeE(
    QGnomeTheme *self,
    Qt::ColorScheme a0) {
  static_cast<OwnQGnomeTheme *>(self)->OwnQGnomeTheme::updateColorScheme(a0);
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  void QGnomeTheme::updateHighContrast(Qt::ContrastPreference a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGnomeTheme18updateHighContrastEN2Qt18ContrastPreferenceE(
    QGnomeTheme *self,
    Qt::ContrastPreference a0) {
  static_cast<OwnQGnomeTheme *>(self)->OwnQGnomeTheme::updateHighContrast(
      a0);
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  void QGnomeTheme::updateReducedMotion(Qt::MotionPreference a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGnomeTheme19updateReducedMotionEN2Qt16MotionPreferenceE(
    QGnomeTheme *self,
    Qt::MotionPreference a0) {
  static_cast<OwnQGnomeTheme *>(self)->OwnQGnomeTheme::updateReducedMotion(
      a0);
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  QPlatformMenuBar *QGnomeTheme::createPlatformMenuBar() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_own_ZNK11QGnomeTheme21createPlatformMenuBarEv(
    const QGnomeTheme *self) {
  return self->QGnomeTheme::createPlatformMenuBar();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  Qt::ContrastPreference QGnomeTheme::contrastPreference() const
extern "C" Q_DECL_EXPORT
Qt::ContrastPreference ritual_own_ZNK11QGnomeTheme18contrastPreferenceEv(
    const QGnomeTheme *self) {
  return self->QGnomeTheme::contrastPreference();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
//  Qt::MotionPreference QGnomeTheme::motionPreference() const
extern "C" Q_DECL_EXPORT
Qt::MotionPreference ritual_own_ZNK11QGnomeTheme16motionPreferenceEv(
    const QGnomeTheme *self) {
  return self->QGnomeTheme::motionPreference();
}
#endif  // QT_CONFIG(dbus)

#if QT_CONFIG(dbus)
#if QT_CONFIG(systemtrayicon)
//  QPlatformSystemTrayIcon *QGnomeTheme::createPlatformSystemTrayIcon()
//      const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_own_ZNK11QGnomeTheme28createPlatformSystemTrayIconEv(
    const QGnomeTheme *self) {
  return self->QGnomeTheme::createPlatformSystemTrayIcon();
}
#endif  // QT_CONFIG(systemtrayicon)
#endif  // QT_CONFIG(dbus)
