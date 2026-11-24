//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgnometheme_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgnometheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QGnomeThemePrivate::QGnomeThemePrivate()
extern "C" Q_DECL_EXPORT
QGnomeThemePrivate *ritual_ZN18QGnomeThemePrivateC1Ev() {
  return new QGnomeThemePrivate();
}

//  QGnomeThemePrivate::~QGnomeThemePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGnomeThemePrivateD1Ev(QGnomeThemePrivate *self) {
  delete self;
}

//  void QGnomeThemePrivate::configureFonts(const QString &gtkFontName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QGnomeThemePrivate14configureFontsERK7QString(
    const QGnomeThemePrivate *self,
    const QString *gtkFontName) {
  self->configureFonts(*gtkFontName);
}

//  Qt::ColorScheme QGnomeThemePrivate::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK18QGnomeThemePrivate11colorSchemeEv(
    const QGnomeThemePrivate *self) {
  return self->colorScheme();
}

//  bool QGnomeThemePrivate::hasRequestedColorScheme() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGnomeThemePrivate23hasRequestedColorSchemeEv(
    const QGnomeThemePrivate *self) {
  return self->hasRequestedColorScheme();
}
