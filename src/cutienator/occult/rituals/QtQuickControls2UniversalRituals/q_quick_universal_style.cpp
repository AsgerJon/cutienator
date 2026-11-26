//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Universal/6.12.0/QtQuickControls2Universal/private/qquickuniversalstyle
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2Universal/QtQuickControls2Universal>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Universal/6.12.0/QtQuickControls2Universal/private/qquickuniversalstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuickUniversalStyle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickUniversalStyle : QQuickUniversalStyle {
  using QQuickUniversalStyle::attachedParentChange;
};

//  const QMetaObject *QQuickUniversalStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickUniversalStyle10metaObjectEv(
    const QQuickUniversalStyle *self) {
  return self->metaObject();
}

//  void *QQuickUniversalStyle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickUniversalStyle11qt_metacastEPKc(
    QQuickUniversalStyle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickUniversalStyle::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickUniversalStyle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickUniversalStyle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickUniversalStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickUniversalStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickUniversalStyle::tr(s, c, n));
}

//  void QQuickUniversalStyle::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle21qt_qmlMarker_attachedEv(
    QQuickUniversalStyle *self) {
  self->qt_qmlMarker_attached();
}

//  void QQuickUniversalStyle::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle24qt_qmlMarker_uncreatableEv(
    QQuickUniversalStyle *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickUniversalStyle::QQuickUniversalStyle(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickUniversalStyle *ritual_ZN20QQuickUniversalStyleC1EP7QObject(
    QObject *parent) {
  return new QQuickUniversalStyle(parent);
}

//  QQuickUniversalStyle *QQuickUniversalStyle::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickUniversalStyle *ritual_ZN20QQuickUniversalStyle21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickUniversalStyle::qmlAttachedProperties(object);
}

//  Theme QQuickUniversalStyle::theme() const
extern "C" Q_DECL_EXPORT
QQuickUniversalStyle::Theme ritual_ZNK20QQuickUniversalStyle5themeEv(
    const QQuickUniversalStyle *self) {
  return self->theme();
}

//  void QQuickUniversalStyle::setTheme(Theme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle8setThemeENS_5ThemeE(
    QQuickUniversalStyle *self,
    QQuickUniversalStyle::Theme theme) {
  self->setTheme(theme);
}

//  void QQuickUniversalStyle::inheritTheme(Theme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle12inheritThemeENS_5ThemeE(
    QQuickUniversalStyle *self,
    QQuickUniversalStyle::Theme theme) {
  self->inheritTheme(theme);
}

//  void QQuickUniversalStyle::propagateTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle14propagateThemeEv(
    QQuickUniversalStyle *self) {
  self->propagateTheme();
}

//  void QQuickUniversalStyle::resetTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle10resetThemeEv(
    QQuickUniversalStyle *self) {
  self->resetTheme();
}

//  QVariant QQuickUniversalStyle::accent() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQuickUniversalStyle6accentEv(
    const QQuickUniversalStyle *self) {
  return new QVariant(self->accent());
}

//  void QQuickUniversalStyle::setAccent(const QVariant &accent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle9setAccentERK8QVariant(
    QQuickUniversalStyle *self,
    const QVariant *accent) {
  self->setAccent(*accent);
}

//  void QQuickUniversalStyle::inheritAccent(QRgb accent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle13inheritAccentEj(
    QQuickUniversalStyle *self,
    QRgb accent) {
  self->inheritAccent(accent);
}

//  void QQuickUniversalStyle::propagateAccent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle15propagateAccentEv(
    QQuickUniversalStyle *self) {
  self->propagateAccent();
}

//  void QQuickUniversalStyle::resetAccent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle11resetAccentEv(
    QQuickUniversalStyle *self) {
  self->resetAccent();
}

//  QVariant QQuickUniversalStyle::foreground() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQuickUniversalStyle10foregroundEv(
    const QQuickUniversalStyle *self) {
  return new QVariant(self->foreground());
}

//  void QQuickUniversalStyle::setForeground(const QVariant &foreground)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle13setForegroundERK8QVariant(
    QQuickUniversalStyle *self,
    const QVariant *foreground) {
  self->setForeground(*foreground);
}

//  void QQuickUniversalStyle::inheritForeground(QRgb foreground, bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle17inheritForegroundEjb(
    QQuickUniversalStyle *self,
    QRgb foreground,
    bool has) {
  self->inheritForeground(foreground, has);
}

//  void QQuickUniversalStyle::propagateForeground()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle19propagateForegroundEv(
    QQuickUniversalStyle *self) {
  self->propagateForeground();
}

//  void QQuickUniversalStyle::resetForeground()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle15resetForegroundEv(
    QQuickUniversalStyle *self) {
  self->resetForeground();
}

//  QVariant QQuickUniversalStyle::background() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQuickUniversalStyle10backgroundEv(
    const QQuickUniversalStyle *self) {
  return new QVariant(self->background());
}

//  void QQuickUniversalStyle::setBackground(const QVariant &background)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle13setBackgroundERK8QVariant(
    QQuickUniversalStyle *self,
    const QVariant *background) {
  self->setBackground(*background);
}

//  void QQuickUniversalStyle::inheritBackground(QRgb background, bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle17inheritBackgroundEjb(
    QQuickUniversalStyle *self,
    QRgb background,
    bool has) {
  self->inheritBackground(background, has);
}

//  void QQuickUniversalStyle::propagateBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle19propagateBackgroundEv(
    QQuickUniversalStyle *self) {
  self->propagateBackground();
}

//  void QQuickUniversalStyle::resetBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle15resetBackgroundEv(
    QQuickUniversalStyle *self) {
  self->resetBackground();
}

//  QColor QQuickUniversalStyle::color(Color color) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle5colorENS_5ColorE(
    const QQuickUniversalStyle *self,
    QQuickUniversalStyle::Color color) {
  return new QColor(self->color(color));
}

//  QColor QQuickUniversalStyle::altHighColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle12altHighColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->altHighColor());
}

//  QColor QQuickUniversalStyle::altLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle11altLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->altLowColor());
}

//  QColor QQuickUniversalStyle::altMediumColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle14altMediumColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->altMediumColor());
}

//  QColor QQuickUniversalStyle::altMediumHighColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle18altMediumHighColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->altMediumHighColor());
}

//  QColor QQuickUniversalStyle::altMediumLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle17altMediumLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->altMediumLowColor());
}

//  QColor QQuickUniversalStyle::baseHighColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle13baseHighColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->baseHighColor());
}

//  QColor QQuickUniversalStyle::baseLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle12baseLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->baseLowColor());
}

//  QColor QQuickUniversalStyle::baseMediumColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle15baseMediumColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->baseMediumColor());
}

//  QColor QQuickUniversalStyle::baseMediumHighColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle19baseMediumHighColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->baseMediumHighColor());
}

//  QColor QQuickUniversalStyle::baseMediumLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle18baseMediumLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->baseMediumLowColor());
}

//  QColor QQuickUniversalStyle::chromeAltLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle17chromeAltLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeAltLowColor());
}

//  QColor QQuickUniversalStyle::chromeBlackHighColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle20chromeBlackHighColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeBlackHighColor());
}

//  QColor QQuickUniversalStyle::chromeBlackLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle19chromeBlackLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeBlackLowColor());
}

//  QColor QQuickUniversalStyle::chromeBlackMediumLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle25chromeBlackMediumLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeBlackMediumLowColor());
}

//  QColor QQuickUniversalStyle::chromeBlackMediumColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle22chromeBlackMediumColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeBlackMediumColor());
}

//  QColor QQuickUniversalStyle::chromeDisabledHighColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle23chromeDisabledHighColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeDisabledHighColor());
}

//  QColor QQuickUniversalStyle::chromeDisabledLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle22chromeDisabledLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeDisabledLowColor());
}

//  QColor QQuickUniversalStyle::chromeHighColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle15chromeHighColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeHighColor());
}

//  QColor QQuickUniversalStyle::chromeLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle14chromeLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeLowColor());
}

//  QColor QQuickUniversalStyle::chromeMediumColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle17chromeMediumColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeMediumColor());
}

//  QColor QQuickUniversalStyle::chromeMediumLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle20chromeMediumLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeMediumLowColor());
}

//  QColor QQuickUniversalStyle::chromeWhiteColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle16chromeWhiteColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->chromeWhiteColor());
}

//  QColor QQuickUniversalStyle::listLowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle12listLowColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->listLowColor());
}

//  QColor QQuickUniversalStyle::listMediumColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle15listMediumColorEv(
    const QQuickUniversalStyle *self) {
  return new QColor(self->listMediumColor());
}

//  QColor QQuickUniversalStyle::systemColor(SystemColor role) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickUniversalStyle11systemColorENS_11SystemColorE(
    const QQuickUniversalStyle *self,
    QQuickUniversalStyle::SystemColor role) {
  return new QColor(self->systemColor(role));
}

//  void QQuickUniversalStyle::initGlobals()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle11initGlobalsEv() {
  QQuickUniversalStyle::initGlobals();
}

//  void QQuickUniversalStyle::themeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle12themeChangedEv(
    QQuickUniversalStyle *self) {
  self->themeChanged();
}

//  void QQuickUniversalStyle::accentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle13accentChangedEv(
    QQuickUniversalStyle *self) {
  self->accentChanged();
}

//  void QQuickUniversalStyle::foregroundChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle17foregroundChangedEv(
    QQuickUniversalStyle *self) {
  self->foregroundChanged();
}

//  void QQuickUniversalStyle::backgroundChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle17backgroundChangedEv(
    QQuickUniversalStyle *self) {
  self->backgroundChanged();
}

//  void QQuickUniversalStyle::paletteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle14paletteChangedEv(
    QQuickUniversalStyle *self) {
  self->paletteChanged();
}

//  void QQuickUniversalStyle::attachedParentChange(QQuickAttachedPropertyPro
//      pagator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickUniversalStyle20attachedParentChangeEP32QQuickAttachedPropertyPropagatorS1_(
    QQuickUniversalStyle *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  self->attachedParentChange(newParent, oldParent);
}

//  bool QQuickUniversalStyle::variantToRgba(const QVariant &var, const char
//      *name, QRgb *rgba) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickUniversalStyle13variantToRgbaERK8QVariantPKcPj(
    const QQuickUniversalStyle *self,
    const QVariant *var,
    const char *name,
    QRgb *rgba) {
  return self->variantToRgba(*var, name, rgba);
}

//  void QQuickUniversalStyle::attachedParentChange(QQuickAttachedPropertyPro
//      pagator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickUniversalStyle20attachedParentChangeEP32QQuickAttachedPropertyPropagatorS1_(
    QQuickUniversalStyle *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  static_cast<OwnQQuickUniversalStyle *>(self)->OwnQQuickUniversalStyle::attachedParentChange(
      newParent,
      oldParent);
}
