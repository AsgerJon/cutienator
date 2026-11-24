//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktheme_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>

//  QQuickTheme::QQuickTheme()
extern "C" Q_DECL_EXPORT
QQuickTheme *ritual_ZN11QQuickThemeC1Ev() {
  return new QQuickTheme();
}

//  QQuickTheme::~QQuickTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickThemeD1Ev(QQuickTheme *self) {
  delete self;
}

//  QQuickTheme *QQuickTheme::instance()
extern "C" Q_DECL_EXPORT
QQuickTheme *ritual_ZN11QQuickTheme8instanceEv() {
  return QQuickTheme::instance();
}

//  QFont QQuickTheme::font(Scope scope)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN11QQuickTheme4fontENS_5ScopeE(QQuickTheme::Scope scope) {
  return new QFont(QQuickTheme::font(scope));
}

//  QPalette QQuickTheme::palette(Scope scope)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN11QQuickTheme7paletteENS_5ScopeE(
    QQuickTheme::Scope scope) {
  return new QPalette(QQuickTheme::palette(scope));
}

//  void QQuickTheme::setFont(Scope scope, const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickTheme7setFontENS_5ScopeERK5QFont(
    QQuickTheme *self,
    QQuickTheme::Scope scope,
    const QFont *font) {
  self->setFont(scope, *font);
}

//  void QQuickTheme::setPalette(Scope scope, const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickTheme10setPaletteENS_5ScopeERK8QPalette(
    QQuickTheme *self,
    QQuickTheme::Scope scope,
    const QPalette *palette) {
  self->setPalette(scope, *palette);
}

//  void QQuickTheme::setUsePlatformPalette(const bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickTheme21setUsePlatformPaletteEb(
    QQuickTheme *self,
    bool enable) {
  self->setUsePlatformPalette(enable);
}

//  bool QQuickTheme::usePlatformPalette()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickTheme18usePlatformPaletteEv(QQuickTheme *self) {
  return self->usePlatformPalette();
}

//  QQuickThemePrivate *QQuickTheme::d_func()
extern "C" Q_DECL_EXPORT
QQuickThemePrivate *ritual_ZN11QQuickTheme6d_funcEv(QQuickTheme *self) {
  return self->d_func();
}

//  const QQuickThemePrivate *QQuickTheme::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickThemePrivate *ritual_ZNK11QQuickTheme6d_funcEv(
    const QQuickTheme *self) {
  return self->d_func();
}
