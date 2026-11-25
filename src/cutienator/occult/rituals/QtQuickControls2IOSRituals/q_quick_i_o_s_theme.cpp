//  Written by hand on 2026-11-25 from
//  QtQuickControls2IOS/6.12.0/QtQuickControls2IOS/private/
//  qquickiostheme_p.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again.
//  Qt builds this part only with its feature 'quickcontrols2-ios',
//  for macOS and iOS. The class line has no export macro, but its one
//  function, 'initialize', carries Q_QUICKCONTROLS2IOS_EXPORT itself,
//  so Qt's library offers it by name.
//  Not written: nothing; the class has no other function.
#include <QtCore/qglobal.h>
#include <QtQuickControls2/6.12.0/QtQuickControls2/private/qtquickcontrols2-config_p.h>
#if QT_CONFIG(quickcontrols2_ios)
#include <QtQuickControls2IOS/qtquickcontrols2iosexports.h>
#include <QtQuickControls2IOS/6.12.0/QtQuickControls2IOS/private/qquickiostheme_p.h>

//  void QQuickIOSTheme::initialize(QQuickTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickIOSTheme10initializeEP11QQuickTheme(
    QQuickTheme *theme) {
  QQuickIOSTheme::initialize(theme);
}

#endif  // QT_CONFIG(quickcontrols2_ios)
