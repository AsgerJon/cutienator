//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FluentWinUI3/6.12.0/QtQuickControls2FluentWinUI3/private/qquickfluentwi
//  nui3theme_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2FluentWinUI3/QtQuickControls2FluentWinUI3>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FluentWinUI3/6.12.0/QtQuickControls2FluentWinUI3/private/qquickfluentwinui3theme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>

//  void QQuickFluentWinUI3Theme::initialize(QQuickTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFluentWinUI3Theme10initializeEP11QQuickTheme(
    QQuickTheme *theme) {
  QQuickFluentWinUI3Theme::initialize(theme);
}

//  QPalette QQuickFluentWinUI3Theme::initializeDefaultPalette()
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN23QQuickFluentWinUI3Theme24initializeDefaultPaletteEv() {
  return new QPalette(QQuickFluentWinUI3Theme::initializeDefaultPalette());
}

//  QQuickFluentWinUI3Theme::~QQuickFluentWinUI3Theme()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFluentWinUI3ThemeD1Ev(QQuickFluentWinUI3Theme *self) {
  delete self;
}
