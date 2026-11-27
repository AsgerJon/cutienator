//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginesettings.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginesettings.h>
#include <QtCore/qstring.h>

//  QWebEngineSettings::~QWebEngineSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettingsD1Ev(QWebEngineSettings *self) {
  delete self;
}

//  void QWebEngineSettings::setFontFamily(FontFamily which, const QString
//      &family)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings13setFontFamilyENS_10FontFamilyERK7QString(
    QWebEngineSettings *self,
    QWebEngineSettings::FontFamily which,
    const QString *family) {
  self->setFontFamily(which, *family);
}

//  QString QWebEngineSettings::fontFamily(FontFamily which) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWebEngineSettings10fontFamilyENS_10FontFamilyE(
    const QWebEngineSettings *self,
    QWebEngineSettings::FontFamily which) {
  return new QString(self->fontFamily(which));
}

//  void QWebEngineSettings::resetFontFamily(FontFamily which)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings15resetFontFamilyENS_10FontFamilyE(
    QWebEngineSettings *self,
    QWebEngineSettings::FontFamily which) {
  self->resetFontFamily(which);
}

//  void QWebEngineSettings::setFontSize(FontSize type, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings11setFontSizeENS_8FontSizeEi(
    QWebEngineSettings *self,
    QWebEngineSettings::FontSize type,
    int size) {
  self->setFontSize(type, size);
}

//  int QWebEngineSettings::fontSize(FontSize type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWebEngineSettings8fontSizeENS_8FontSizeE(
    const QWebEngineSettings *self,
    QWebEngineSettings::FontSize type) {
  return self->fontSize(type);
}

//  void QWebEngineSettings::resetFontSize(FontSize type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings13resetFontSizeENS_8FontSizeE(
    QWebEngineSettings *self,
    QWebEngineSettings::FontSize type) {
  self->resetFontSize(type);
}

//  void QWebEngineSettings::setAttribute(WebAttribute attr, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings12setAttributeENS_12WebAttributeEb(
    QWebEngineSettings *self,
    QWebEngineSettings::WebAttribute attr,
    bool on) {
  self->setAttribute(attr, on);
}

//  bool QWebEngineSettings::testAttribute(WebAttribute attr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWebEngineSettings13testAttributeENS_12WebAttributeE(
    const QWebEngineSettings *self,
    QWebEngineSettings::WebAttribute attr) {
  return self->testAttribute(attr);
}

//  void QWebEngineSettings::resetAttribute(WebAttribute attr)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings14resetAttributeENS_12WebAttributeE(
    QWebEngineSettings *self,
    QWebEngineSettings::WebAttribute attr) {
  self->resetAttribute(attr);
}

//  void QWebEngineSettings::setDefaultTextEncoding(const QString &encoding)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings22setDefaultTextEncodingERK7QString(
    QWebEngineSettings *self,
    const QString *encoding) {
  self->setDefaultTextEncoding(*encoding);
}

//  QString QWebEngineSettings::defaultTextEncoding() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWebEngineSettings19defaultTextEncodingEv(
    const QWebEngineSettings *self) {
  return new QString(self->defaultTextEncoding());
}

//  UnknownUrlSchemePolicy QWebEngineSettings::unknownUrlSchemePolicy() const
extern "C" Q_DECL_EXPORT
QWebEngineSettings::UnknownUrlSchemePolicy ritual_ZNK18QWebEngineSettings22unknownUrlSchemePolicyEv(
    const QWebEngineSettings *self) {
  return self->unknownUrlSchemePolicy();
}

//  void QWebEngineSettings::setUnknownUrlSchemePolicy(UnknownUrlSchemePolicy
//      policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings25setUnknownUrlSchemePolicyENS_22UnknownUrlSchemePolicyE(
    QWebEngineSettings *self,
    QWebEngineSettings::UnknownUrlSchemePolicy policy) {
  self->setUnknownUrlSchemePolicy(policy);
}

//  void QWebEngineSettings::resetUnknownUrlSchemePolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings27resetUnknownUrlSchemePolicyEv(
    QWebEngineSettings *self) {
  self->resetUnknownUrlSchemePolicy();
}

//  void QWebEngineSettings::setImageAnimationPolicy(ImageAnimationPolicy
//      policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings23setImageAnimationPolicyENS_20ImageAnimationPolicyE(
    QWebEngineSettings *self,
    QWebEngineSettings::ImageAnimationPolicy policy) {
  self->setImageAnimationPolicy(policy);
}

//  ImageAnimationPolicy QWebEngineSettings::imageAnimationPolicy() const
extern "C" Q_DECL_EXPORT
QWebEngineSettings::ImageAnimationPolicy ritual_ZNK18QWebEngineSettings20imageAnimationPolicyEv(
    const QWebEngineSettings *self) {
  return self->imageAnimationPolicy();
}

//  void QWebEngineSettings::resetImageAnimationPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings25resetImageAnimationPolicyEv(
    QWebEngineSettings *self) {
  self->resetImageAnimationPolicy();
}

//  QWebEngineSettings::QWebEngineSettings(QWebEngineSettings
//      *parentSettings)
extern "C" Q_DECL_EXPORT
QWebEngineSettings *ritual_ZN18QWebEngineSettingsC1EPS_(
    QWebEngineSettings *parentSettings) {
  return new QWebEngineSettings(parentSettings);
}

//  void QWebEngineSettings::setParentSettings(QWebEngineSettings
//      *parentSettings)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebEngineSettings17setParentSettingsEPS_(
    QWebEngineSettings *self,
    QWebEngineSettings *parentSettings) {
  self->setParentSettings(parentSettings);
}
