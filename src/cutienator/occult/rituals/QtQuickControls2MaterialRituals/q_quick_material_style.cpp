//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Material/6.12.0/QtQuickControls2Material/private/qquickmaterialstyle_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2Material/QtQuickControls2Material>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Material/6.12.0/QtQuickControls2Material/private/qquickmaterialstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuickMaterialStyle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMaterialStyle : QQuickMaterialStyle {
  using QQuickMaterialStyle::attachedParentChange;
};

//  const QMetaObject *QQuickMaterialStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickMaterialStyle10metaObjectEv(
    const QQuickMaterialStyle *self) {
  return self->metaObject();
}

//  void *QQuickMaterialStyle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickMaterialStyle11qt_metacastEPKc(
    QQuickMaterialStyle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMaterialStyle::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickMaterialStyle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMaterialStyle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMaterialStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickMaterialStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMaterialStyle::tr(s, c, n));
}

//  void QQuickMaterialStyle::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle21qt_qmlMarker_attachedEv(
    QQuickMaterialStyle *self) {
  self->qt_qmlMarker_attached();
}

//  void QQuickMaterialStyle::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle24qt_qmlMarker_uncreatableEv(
    QQuickMaterialStyle *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickMaterialStyle::QQuickMaterialStyle(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle *ritual_ZN19QQuickMaterialStyleC1EP7QObject(
    QObject *parent) {
  return new QQuickMaterialStyle(parent);
}

//  QQuickMaterialStyle *QQuickMaterialStyle::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle *ritual_ZN19QQuickMaterialStyle21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickMaterialStyle::qmlAttachedProperties(object);
}

//  Theme QQuickMaterialStyle::theme() const
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle::Theme ritual_ZNK19QQuickMaterialStyle5themeEv(
    const QQuickMaterialStyle *self) {
  return self->theme();
}

//  void QQuickMaterialStyle::setTheme(Theme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle8setThemeENS_5ThemeE(
    QQuickMaterialStyle *self,
    QQuickMaterialStyle::Theme theme) {
  self->setTheme(theme);
}

//  void QQuickMaterialStyle::inheritTheme(Theme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle12inheritThemeENS_5ThemeE(
    QQuickMaterialStyle *self,
    QQuickMaterialStyle::Theme theme) {
  self->inheritTheme(theme);
}

//  void QQuickMaterialStyle::propagateTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle14propagateThemeEv(
    QQuickMaterialStyle *self) {
  self->propagateTheme();
}

//  void QQuickMaterialStyle::resetTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle10resetThemeEv(
    QQuickMaterialStyle *self) {
  self->resetTheme();
}

//  void QQuickMaterialStyle::themeChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle11themeChangeEv(
    QQuickMaterialStyle *self) {
  self->themeChange();
}

//  QVariant QQuickMaterialStyle::primary() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickMaterialStyle7primaryEv(
    const QQuickMaterialStyle *self) {
  return new QVariant(self->primary());
}

//  void QQuickMaterialStyle::setPrimary(const QVariant &accent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle10setPrimaryERK8QVariant(
    QQuickMaterialStyle *self,
    const QVariant *accent) {
  self->setPrimary(*accent);
}

//  void QQuickMaterialStyle::inheritPrimary(uint primary, bool custom)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle14inheritPrimaryEjb(
    QQuickMaterialStyle *self,
    uint primary,
    bool custom) {
  self->inheritPrimary(primary, custom);
}

//  void QQuickMaterialStyle::propagatePrimary()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle16propagatePrimaryEv(
    QQuickMaterialStyle *self) {
  self->propagatePrimary();
}

//  void QQuickMaterialStyle::resetPrimary()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle12resetPrimaryEv(
    QQuickMaterialStyle *self) {
  self->resetPrimary();
}

//  void QQuickMaterialStyle::primaryChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle13primaryChangeEv(
    QQuickMaterialStyle *self) {
  self->primaryChange();
}

//  QVariant QQuickMaterialStyle::accent() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickMaterialStyle6accentEv(
    const QQuickMaterialStyle *self) {
  return new QVariant(self->accent());
}

//  void QQuickMaterialStyle::setAccent(const QVariant &accent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle9setAccentERK8QVariant(
    QQuickMaterialStyle *self,
    const QVariant *accent) {
  self->setAccent(*accent);
}

//  void QQuickMaterialStyle::inheritAccent(uint accent, bool custom)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle13inheritAccentEjb(
    QQuickMaterialStyle *self,
    uint accent,
    bool custom) {
  self->inheritAccent(accent, custom);
}

//  void QQuickMaterialStyle::propagateAccent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle15propagateAccentEv(
    QQuickMaterialStyle *self) {
  self->propagateAccent();
}

//  void QQuickMaterialStyle::resetAccent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle11resetAccentEv(
    QQuickMaterialStyle *self) {
  self->resetAccent();
}

//  void QQuickMaterialStyle::accentChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle12accentChangeEv(
    QQuickMaterialStyle *self) {
  self->accentChange();
}

//  QVariant QQuickMaterialStyle::foreground() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickMaterialStyle10foregroundEv(
    const QQuickMaterialStyle *self) {
  return new QVariant(self->foreground());
}

//  void QQuickMaterialStyle::setForeground(const QVariant &foreground)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle13setForegroundERK8QVariant(
    QQuickMaterialStyle *self,
    const QVariant *foreground) {
  self->setForeground(*foreground);
}

//  void QQuickMaterialStyle::inheritForeground(uint foreground, bool custom,
//      bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle17inheritForegroundEjbb(
    QQuickMaterialStyle *self,
    uint foreground,
    bool custom,
    bool has) {
  self->inheritForeground(foreground, custom, has);
}

//  void QQuickMaterialStyle::propagateForeground()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle19propagateForegroundEv(
    QQuickMaterialStyle *self) {
  self->propagateForeground();
}

//  void QQuickMaterialStyle::resetForeground()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle15resetForegroundEv(
    QQuickMaterialStyle *self) {
  self->resetForeground();
}

//  void QQuickMaterialStyle::foregroundChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle16foregroundChangeEv(
    QQuickMaterialStyle *self) {
  self->foregroundChange();
}

//  QVariant QQuickMaterialStyle::background() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickMaterialStyle10backgroundEv(
    const QQuickMaterialStyle *self) {
  return new QVariant(self->background());
}

//  void QQuickMaterialStyle::setBackground(const QVariant &background)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle13setBackgroundERK8QVariant(
    QQuickMaterialStyle *self,
    const QVariant *background) {
  self->setBackground(*background);
}

//  void QQuickMaterialStyle::inheritBackground(uint background, bool custom,
//      bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle17inheritBackgroundEjbb(
    QQuickMaterialStyle *self,
    uint background,
    bool custom,
    bool has) {
  self->inheritBackground(background, custom, has);
}

//  void QQuickMaterialStyle::propagateBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle19propagateBackgroundEv(
    QQuickMaterialStyle *self) {
  self->propagateBackground();
}

//  void QQuickMaterialStyle::resetBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle15resetBackgroundEv(
    QQuickMaterialStyle *self) {
  self->resetBackground();
}

//  void QQuickMaterialStyle::backgroundChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle16backgroundChangeEv(
    QQuickMaterialStyle *self) {
  self->backgroundChange();
}

//  int QQuickMaterialStyle::elevation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle9elevationEv(
    const QQuickMaterialStyle *self) {
  return self->elevation();
}

//  void QQuickMaterialStyle::setElevation(int elevation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle12setElevationEi(
    QQuickMaterialStyle *self,
    int elevation) {
  self->setElevation(elevation);
}

//  void QQuickMaterialStyle::resetElevation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle14resetElevationEv(
    QQuickMaterialStyle *self) {
  self->resetElevation();
}

//  void QQuickMaterialStyle::elevationChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle15elevationChangeEv(
    QQuickMaterialStyle *self) {
  self->elevationChange();
}

//  RoundedScale QQuickMaterialStyle::roundedScale() const
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle::RoundedScale ritual_ZNK19QQuickMaterialStyle12roundedScaleEv(
    const QQuickMaterialStyle *self) {
  return self->roundedScale();
}

//  void QQuickMaterialStyle::setRoundedScale(RoundedScale roundedScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle15setRoundedScaleENS_12RoundedScaleE(
    QQuickMaterialStyle *self,
    QQuickMaterialStyle::RoundedScale roundedScale) {
  self->setRoundedScale(roundedScale);
}

//  void QQuickMaterialStyle::resetRoundedScale()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle17resetRoundedScaleEv(
    QQuickMaterialStyle *self) {
  self->resetRoundedScale();
}

//  ContainerStyle QQuickMaterialStyle::containerStyle() const
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle::ContainerStyle ritual_ZNK19QQuickMaterialStyle14containerStyleEv(
    const QQuickMaterialStyle *self) {
  return self->containerStyle();
}

//  void QQuickMaterialStyle::setContainerStyle(ContainerStyle
//      containerStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle17setContainerStyleENS_14ContainerStyleE(
    QQuickMaterialStyle *self,
    QQuickMaterialStyle::ContainerStyle containerStyle) {
  self->setContainerStyle(containerStyle);
}

//  void QQuickMaterialStyle::resetContainerStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle19resetContainerStyleEv(
    QQuickMaterialStyle *self) {
  self->resetContainerStyle();
}

//  QColor QQuickMaterialStyle::primaryColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle12primaryColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->primaryColor());
}

//  QColor QQuickMaterialStyle::accentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle11accentColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->accentColor());
}

//  QColor QQuickMaterialStyle::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle15backgroundColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->backgroundColor());
}

//  QColor QQuickMaterialStyle::primaryTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle16primaryTextColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->primaryTextColor());
}

//  QColor QQuickMaterialStyle::primaryHighlightedTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle27primaryHighlightedTextColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->primaryHighlightedTextColor());
}

//  QColor QQuickMaterialStyle::secondaryTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle18secondaryTextColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->secondaryTextColor());
}

//  QColor QQuickMaterialStyle::hintTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle13hintTextColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->hintTextColor());
}

//  QColor QQuickMaterialStyle::textSelectionColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle18textSelectionColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->textSelectionColor());
}

//  QColor QQuickMaterialStyle::dropShadowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle15dropShadowColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->dropShadowColor());
}

//  QColor QQuickMaterialStyle::dividerColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle12dividerColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->dividerColor());
}

//  QColor QQuickMaterialStyle::iconColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle9iconColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->iconColor());
}

//  QColor QQuickMaterialStyle::iconDisabledColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle17iconDisabledColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->iconDisabledColor());
}

//  QColor QQuickMaterialStyle::buttonColor(Theme theme, const QVariant
//      &background, const QVariant &accent, bool enabled, bool flat, bool
//      highlighted, bool checked) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle11buttonColorENS_5ThemeERK8QVariantS3_bbbb(
    const QQuickMaterialStyle *self,
    QQuickMaterialStyle::Theme theme,
    const QVariant *background,
    const QVariant *accent,
    bool enabled,
    bool flat,
    bool highlighted,
    bool checked) {
  return new QColor(
      self->buttonColor(
          theme,
          *background,
          *accent,
          enabled,
          flat,
          highlighted,
          checked));
}

//  QColor QQuickMaterialStyle::frameColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle10frameColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->frameColor());
}

//  QColor QQuickMaterialStyle::rippleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle11rippleColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->rippleColor());
}

//  QColor QQuickMaterialStyle::highlightedRippleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle22highlightedRippleColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->highlightedRippleColor());
}

//  QColor QQuickMaterialStyle::switchUncheckedTrackColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle25switchUncheckedTrackColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchUncheckedTrackColor());
}

//  QColor QQuickMaterialStyle::switchCheckedTrackColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle23switchCheckedTrackColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchCheckedTrackColor());
}

//  QColor QQuickMaterialStyle::switchDisabledUncheckedTrackColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle33switchDisabledUncheckedTrackColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchDisabledUncheckedTrackColor());
}

//  QColor QQuickMaterialStyle::switchDisabledCheckedTrackColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle31switchDisabledCheckedTrackColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchDisabledCheckedTrackColor());
}

//  QColor QQuickMaterialStyle::switchDisabledUncheckedTrackBorderColor()
//      const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle39switchDisabledUncheckedTrackBorderColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchDisabledUncheckedTrackBorderColor());
}

//  QColor QQuickMaterialStyle::switchUncheckedHandleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle26switchUncheckedHandleColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchUncheckedHandleColor());
}

//  QColor QQuickMaterialStyle::switchUncheckedHoveredHandleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle33switchUncheckedHoveredHandleColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchUncheckedHoveredHandleColor());
}

//  QColor QQuickMaterialStyle::switchCheckedHandleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle24switchCheckedHandleColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchCheckedHandleColor());
}

//  QColor QQuickMaterialStyle::switchDisabledUncheckedHandleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle34switchDisabledUncheckedHandleColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchDisabledUncheckedHandleColor());
}

//  QColor QQuickMaterialStyle::switchDisabledCheckedHandleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle32switchDisabledCheckedHandleColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchDisabledCheckedHandleColor());
}

//  QColor QQuickMaterialStyle::switchDisabledCheckedIconColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle30switchDisabledCheckedIconColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchDisabledCheckedIconColor());
}

//  QColor QQuickMaterialStyle::switchDisabledUncheckedIconColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle32switchDisabledUncheckedIconColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->switchDisabledUncheckedIconColor());
}

//  QColor QQuickMaterialStyle::scrollBarColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle14scrollBarColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->scrollBarColor());
}

//  QColor QQuickMaterialStyle::scrollBarHoveredColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle21scrollBarHoveredColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->scrollBarHoveredColor());
}

//  QColor QQuickMaterialStyle::scrollBarPressedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle21scrollBarPressedColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->scrollBarPressedColor());
}

//  QColor QQuickMaterialStyle::dialogColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle11dialogColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->dialogColor());
}

//  QColor QQuickMaterialStyle::backgroundDimColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle18backgroundDimColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->backgroundDimColor());
}

//  QColor QQuickMaterialStyle::listHighlightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle18listHighlightColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->listHighlightColor());
}

//  QColor QQuickMaterialStyle::tooltipColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle12tooltipColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->tooltipColor());
}

//  QColor QQuickMaterialStyle::toolBarColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle12toolBarColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->toolBarColor());
}

//  QColor QQuickMaterialStyle::toolTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle13toolTextColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->toolTextColor());
}

//  QColor QQuickMaterialStyle::spinBoxDisabledIconColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle24spinBoxDisabledIconColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->spinBoxDisabledIconColor());
}

//  QColor QQuickMaterialStyle::sliderDisabledColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle19sliderDisabledColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->sliderDisabledColor());
}

//  QColor QQuickMaterialStyle::textFieldFilledContainerColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle29textFieldFilledContainerColorEv(
    const QQuickMaterialStyle *self) {
  return new QColor(self->textFieldFilledContainerColor());
}

//  QColor QQuickMaterialStyle::color(Color color, Shade shade) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle5colorENS_5ColorENS_5ShadeE(
    const QQuickMaterialStyle *self,
    QQuickMaterialStyle::Color color,
    QQuickMaterialStyle::Shade shade) {
  return new QColor(self->color(color, shade));
}

//  QColor QQuickMaterialStyle::shade(const QColor &color, Shade shade) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle5shadeERK6QColorNS_5ShadeE(
    const QQuickMaterialStyle *self,
    const QColor *color,
    QQuickMaterialStyle::Shade shade) {
  return new QColor(self->shade(*color, shade));
}

//  int QQuickMaterialStyle::touchTarget() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle11touchTargetEv(
    const QQuickMaterialStyle *self) {
  return self->touchTarget();
}

//  int QQuickMaterialStyle::buttonVerticalPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle21buttonVerticalPaddingEv(
    const QQuickMaterialStyle *self) {
  return self->buttonVerticalPadding();
}

//  int QQuickMaterialStyle::buttonLeftPadding(bool flat, bool hasIcon) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle17buttonLeftPaddingEbb(
    const QQuickMaterialStyle *self,
    bool flat,
    bool hasIcon) {
  return self->buttonLeftPadding(flat, hasIcon);
}

//  int QQuickMaterialStyle::buttonRightPadding(bool flat, bool hasIcon, bool
//      hasText) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle18buttonRightPaddingEbbb(
    const QQuickMaterialStyle *self,
    bool flat,
    bool hasIcon,
    bool hasText) {
  return self->buttonRightPadding(flat, hasIcon, hasText);
}

//  int QQuickMaterialStyle::buttonHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle12buttonHeightEv(
    const QQuickMaterialStyle *self) {
  return self->buttonHeight();
}

//  int QQuickMaterialStyle::delegateHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle14delegateHeightEv(
    const QQuickMaterialStyle *self) {
  return self->delegateHeight();
}

//  int QQuickMaterialStyle::dialogButtonBoxHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle21dialogButtonBoxHeightEv(
    const QQuickMaterialStyle *self) {
  return self->dialogButtonBoxHeight();
}

//  int QQuickMaterialStyle::dialogTitleFontPixelSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle24dialogTitleFontPixelSizeEv(
    const QQuickMaterialStyle *self) {
  return self->dialogTitleFontPixelSize();
}

//  RoundedScale QQuickMaterialStyle::dialogRoundedScale() const
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle::RoundedScale ritual_ZNK19QQuickMaterialStyle18dialogRoundedScaleEv(
    const QQuickMaterialStyle *self) {
  return self->dialogRoundedScale();
}

//  int QQuickMaterialStyle::frameVerticalPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle20frameVerticalPaddingEv(
    const QQuickMaterialStyle *self) {
  return self->frameVerticalPadding();
}

//  int QQuickMaterialStyle::menuItemHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle14menuItemHeightEv(
    const QQuickMaterialStyle *self) {
  return self->menuItemHeight();
}

//  int QQuickMaterialStyle::menuItemVerticalPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle23menuItemVerticalPaddingEv(
    const QQuickMaterialStyle *self) {
  return self->menuItemVerticalPadding();
}

//  int QQuickMaterialStyle::switchIndicatorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle20switchIndicatorWidthEv(
    const QQuickMaterialStyle *self) {
  return self->switchIndicatorWidth();
}

//  int QQuickMaterialStyle::switchIndicatorHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle21switchIndicatorHeightEv(
    const QQuickMaterialStyle *self) {
  return self->switchIndicatorHeight();
}

//  int QQuickMaterialStyle::switchNormalHandleHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle24switchNormalHandleHeightEv(
    const QQuickMaterialStyle *self) {
  return self->switchNormalHandleHeight();
}

//  int QQuickMaterialStyle::switchCheckedHandleHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle25switchCheckedHandleHeightEv(
    const QQuickMaterialStyle *self) {
  return self->switchCheckedHandleHeight();
}

//  int QQuickMaterialStyle::switchLargestHandleHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle25switchLargestHandleHeightEv(
    const QQuickMaterialStyle *self) {
  return self->switchLargestHandleHeight();
}

//  int QQuickMaterialStyle::switchDelegateVerticalPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle29switchDelegateVerticalPaddingEv(
    const QQuickMaterialStyle *self) {
  return self->switchDelegateVerticalPadding();
}

//  int QQuickMaterialStyle::textFieldHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle15textFieldHeightEv(
    const QQuickMaterialStyle *self) {
  return self->textFieldHeight();
}

//  int QQuickMaterialStyle::textFieldHorizontalPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle26textFieldHorizontalPaddingEv(
    const QQuickMaterialStyle *self) {
  return self->textFieldHorizontalPadding();
}

//  int QQuickMaterialStyle::textFieldVerticalPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle24textFieldVerticalPaddingEv(
    const QQuickMaterialStyle *self) {
  return self->textFieldVerticalPadding();
}

//  int QQuickMaterialStyle::tooltipHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMaterialStyle13tooltipHeightEv(
    const QQuickMaterialStyle *self) {
  return self->tooltipHeight();
}

//  void QQuickMaterialStyle::initGlobals()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle11initGlobalsEv() {
  QQuickMaterialStyle::initGlobals();
}

//  Variant QQuickMaterialStyle::variant()
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle::Variant ritual_ZN19QQuickMaterialStyle7variantEv() {
  return QQuickMaterialStyle::variant();
}

//  void QQuickMaterialStyle::themeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle12themeChangedEv(
    QQuickMaterialStyle *self) {
  self->themeChanged();
}

//  void QQuickMaterialStyle::primaryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle14primaryChangedEv(
    QQuickMaterialStyle *self) {
  self->primaryChanged();
}

//  void QQuickMaterialStyle::accentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle13accentChangedEv(
    QQuickMaterialStyle *self) {
  self->accentChanged();
}

//  void QQuickMaterialStyle::foregroundChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle17foregroundChangedEv(
    QQuickMaterialStyle *self) {
  self->foregroundChanged();
}

//  void QQuickMaterialStyle::backgroundChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle17backgroundChangedEv(
    QQuickMaterialStyle *self) {
  self->backgroundChanged();
}

//  void QQuickMaterialStyle::elevationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle16elevationChangedEv(
    QQuickMaterialStyle *self) {
  self->elevationChanged();
}

//  void QQuickMaterialStyle::themeOrAccentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle20themeOrAccentChangedEv(
    QQuickMaterialStyle *self) {
  self->themeOrAccentChanged();
}

//  void QQuickMaterialStyle::primaryHighlightedTextColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle34primaryHighlightedTextColorChangedEv(
    QQuickMaterialStyle *self) {
  self->primaryHighlightedTextColorChanged();
}

//  void QQuickMaterialStyle::dialogColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle18dialogColorChangedEv(
    QQuickMaterialStyle *self) {
  self->dialogColorChanged();
}

//  void QQuickMaterialStyle::tooltipColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle19tooltipColorChangedEv(
    QQuickMaterialStyle *self) {
  self->tooltipColorChanged();
}

//  void QQuickMaterialStyle::toolBarColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle19toolBarColorChangedEv(
    QQuickMaterialStyle *self) {
  self->toolBarColorChanged();
}

//  void QQuickMaterialStyle::toolTextColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle20toolTextColorChangedEv(
    QQuickMaterialStyle *self) {
  self->toolTextColorChanged();
}

//  void QQuickMaterialStyle::roundedScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle19roundedScaleChangedEv(
    QQuickMaterialStyle *self) {
  self->roundedScaleChanged();
}

//  void QQuickMaterialStyle::containerStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle21containerStyleChangedEv(
    QQuickMaterialStyle *self) {
  self->containerStyleChanged();
}

//  void QQuickMaterialStyle::attachedParentChange(QQuickAttachedPropertyProp
//      agator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMaterialStyle20attachedParentChangeEP32QQuickAttachedPropertyPropagatorS1_(
    QQuickMaterialStyle *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  self->attachedParentChange(newParent, oldParent);
}

//  bool QQuickMaterialStyle::variantToRgba(const QVariant &var, const char
//      *name, QRgb *rgba, bool *custom) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickMaterialStyle13variantToRgbaERK8QVariantPKcPjPb(
    const QQuickMaterialStyle *self,
    const QVariant *var,
    const char *name,
    QRgb *rgba,
    bool *custom) {
  return self->variantToRgba(*var, name, rgba, custom);
}

//  QColor QQuickMaterialStyle::backgroundColor(Shade shade) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle15backgroundColorENS_5ShadeE(
    const QQuickMaterialStyle *self,
    QQuickMaterialStyle::Shade shade) {
  return new QColor(self->backgroundColor(shade));
}

//  QColor QQuickMaterialStyle::accentColor(Shade shade) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickMaterialStyle11accentColorENS_5ShadeE(
    const QQuickMaterialStyle *self,
    QQuickMaterialStyle::Shade shade) {
  return new QColor(self->accentColor(shade));
}

//  Shade QQuickMaterialStyle::themeShade() const
extern "C" Q_DECL_EXPORT
QQuickMaterialStyle::Shade ritual_ZNK19QQuickMaterialStyle10themeShadeEv(
    const QQuickMaterialStyle *self) {
  return self->themeShade();
}

//  void QQuickMaterialStyle::attachedParentChange(QQuickAttachedPropertyProp
//      agator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickMaterialStyle20attachedParentChangeEP32QQuickAttachedPropertyPropagatorS1_(
    QQuickMaterialStyle *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  static_cast<OwnQQuickMaterialStyle *>(self)->OwnQQuickMaterialStyle::attachedParentChange(
      newParent,
      oldParent);
}
