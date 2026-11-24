//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformtheme_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPlatformThemePrivate::QPlatformThemePrivate()
extern "C" Q_DECL_EXPORT
QPlatformThemePrivate *ritual_ZN21QPlatformThemePrivateC1Ev() {
  return new QPlatformThemePrivate();
}

//  QPlatformThemePrivate::~QPlatformThemePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformThemePrivateD1Ev(QPlatformThemePrivate *self) {
  delete self;
}

//  void QPlatformThemePrivate::initializeSystemPalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformThemePrivate23initializeSystemPaletteEv(
    QPlatformThemePrivate *self) {
  self->initializeSystemPalette();
}

//  unsigned int QPlatformThemePrivate::currentKeyPlatforms()
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN21QPlatformThemePrivate19currentKeyPlatformsEv() {
  return QPlatformThemePrivate::currentKeyPlatforms();
}
