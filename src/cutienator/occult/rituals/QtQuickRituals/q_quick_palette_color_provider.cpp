//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpalettecolorprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpalettecolorprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtGui/qpalette.h>

//  QQuickPaletteColorProvider::QQuickPaletteColorProvider()
extern "C" Q_DECL_EXPORT
QQuickPaletteColorProvider *ritual_ZN26QQuickPaletteColorProviderC1Ev() {
  return new QQuickPaletteColorProvider();
}

//  const QColor &QQuickPaletteColorProvider::color(QPalette::ColorGroup
//      group, QPalette::ColorRole role) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QQuickPaletteColorProvider5colorEN8QPalette10ColorGroupENS0_9ColorRoleE(
    const QQuickPaletteColorProvider *self,
    QPalette::ColorGroup group,
    QPalette::ColorRole role) {
  return new QColor(self->color(group, role));
}

//  bool QQuickPaletteColorProvider::setColor(QPalette::ColorGroup group,
//      QPalette::ColorRole role, QColor color)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider8setColorEN8QPalette10ColorGroupENS0_9ColorRoleE6QColor(
    QQuickPaletteColorProvider *self,
    QPalette::ColorGroup group,
    QPalette::ColorRole role,
    const QColor *color) {
  return self->setColor(group, role, *color);
}

//  bool QQuickPaletteColorProvider::resetColor(QPalette::ColorGroup group,
//      QPalette::ColorRole role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider10resetColorEN8QPalette10ColorGroupENS0_9ColorRoleE(
    QQuickPaletteColorProvider *self,
    QPalette::ColorGroup group,
    QPalette::ColorRole role) {
  return self->resetColor(group, role);
}

//  bool QQuickPaletteColorProvider::resetColor(QPalette::ColorGroup group)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider10resetColorEN8QPalette10ColorGroupE(
    QQuickPaletteColorProvider *self,
    QPalette::ColorGroup group) {
  return self->resetColor(group);
}

//  bool QQuickPaletteColorProvider::fromQPalette(QPalette p)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider12fromQPaletteE8QPalette(
    QQuickPaletteColorProvider *self,
    const QPalette *p) {
  return self->fromQPalette(*p);
}

//  QPalette QQuickPaletteColorProvider::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK26QQuickPaletteColorProvider7paletteEv(
    const QQuickPaletteColorProvider *self) {
  return new QPalette(self->palette());
}

//  const QQuickAbstractPaletteProvider
//      *QQuickPaletteColorProvider::paletteProvider() const
extern "C" Q_DECL_EXPORT
const QQuickAbstractPaletteProvider *ritual_ZNK26QQuickPaletteColorProvider15paletteProviderEv(
    const QQuickPaletteColorProvider *self) {
  return self->paletteProvider();
}

//  void QQuickPaletteColorProvider::setPaletteProvider(const
//      QQuickAbstractPaletteProvider *paletteProvider)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPaletteColorProvider18setPaletteProviderEPK29QQuickAbstractPaletteProvider(
    QQuickPaletteColorProvider *self,
    const QQuickAbstractPaletteProvider *paletteProvider) {
  self->setPaletteProvider(paletteProvider);
}

//  bool QQuickPaletteColorProvider::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider5resetEv(
    QQuickPaletteColorProvider *self) {
  return self->reset();
}

//  bool QQuickPaletteColorProvider::inheritPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider14inheritPaletteERK8QPalette(
    QQuickPaletteColorProvider *self,
    const QPalette *palette) {
  return self->inheritPalette(*palette);
}

//  bool QQuickPaletteColorProvider::doInheritPalette(const QPalette
//      &palette)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider16doInheritPaletteERK8QPalette(
    QQuickPaletteColorProvider *self,
    const QPalette *palette) {
  return self->doInheritPalette(*palette);
}

//  bool QQuickPaletteColorProvider::updateInheritedPalette()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPaletteColorProvider22updateInheritedPaletteEv(
    QQuickPaletteColorProvider *self) {
  return self->updateInheritedPalette();
}

//  void QQuickPaletteColorProvider::ensureRequestedPalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPaletteColorProvider22ensureRequestedPaletteEv(
    QQuickPaletteColorProvider *self) {
  self->ensureRequestedPalette();
}
