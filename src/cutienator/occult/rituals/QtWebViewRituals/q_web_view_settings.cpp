//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebView/qwebviewsettings.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebView/qwebviewsettings.h>

//  bool QWebViewSettings::testAttribute(WebAttribute attribute) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QWebViewSettings13testAttributeENS_12WebAttributeE(
    const QWebViewSettings *self,
    QWebViewSettings::WebAttribute attribute) {
  return self->testAttribute(attribute);
}

//  void QWebViewSettings::setAttribute(WebAttribute attribute, bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebViewSettings12setAttributeENS_12WebAttributeEb(
    QWebViewSettings *self,
    QWebViewSettings::WebAttribute attribute,
    bool value) {
  self->setAttribute(attribute, value);
}

//  void QWebViewSettings::doSetAttribute(WebAttribute a, bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebViewSettings14doSetAttributeENS_12WebAttributeEb(
    QWebViewSettings *self,
    QWebViewSettings::WebAttribute a,
    bool v) {
  self->doSetAttribute(a, v);
}

//  bool QWebViewSettings::doTestAttribute(WebAttribute a) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QWebViewSettings15doTestAttributeENS_12WebAttributeE(
    const QWebViewSettings *self,
    QWebViewSettings::WebAttribute a) {
  return self->doTestAttribute(a);
}

//  QWebViewSettings::~QWebViewSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebViewSettingsD1Ev(QWebViewSettings *self) {
  delete self;
}
