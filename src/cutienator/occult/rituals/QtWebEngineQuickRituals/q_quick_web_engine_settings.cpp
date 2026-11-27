//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginesettings_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginesettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickWebEngineSettings that Python can take functions over in. Every QQuickWebEngineSettings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineSettingsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineSettingsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineSettingsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineSettingsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineSettingsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineSettingsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineSettingsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineSettings : public QQuickWebEngineSettings {
public:
  using QQuickWebEngineSettings::QQuickWebEngineSettings;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWebEngineSettingsCall0 call = reinterpret_cast<CuteQQuickWebEngineSettingsCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWebEngineSettingsCall1 call = reinterpret_cast<CuteQQuickWebEngineSettingsCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWebEngineSettingsCall2 call = reinterpret_cast<CuteQQuickWebEngineSettingsCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWebEngineSettingsCall3 call = reinterpret_cast<CuteQQuickWebEngineSettingsCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWebEngineSettingsCall4 call = reinterpret_cast<CuteQQuickWebEngineSettingsCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWebEngineSettingsCall5 call = reinterpret_cast<CuteQQuickWebEngineSettingsCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWebEngineSettingsCall6 call = reinterpret_cast<CuteQQuickWebEngineSettingsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineSettings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickWebEngineSettings10metaObjectEv(
    const QQuickWebEngineSettings *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineSettings::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickWebEngineSettings11qt_metacastEPKc(
    QQuickWebEngineSettings *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineSettings::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickWebEngineSettings11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineSettings *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineSettings::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickWebEngineSettings2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineSettings::tr(s, c, n));
}

//  void QQuickWebEngineSettings::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineSettings *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineSettings::~QQuickWebEngineSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettingsD1Ev(QQuickWebEngineSettings *self) {
  delete self;
}

//  bool QQuickWebEngineSettings::autoLoadImages() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings14autoLoadImagesEv(
    const QQuickWebEngineSettings *self) {
  return self->autoLoadImages();
}

//  bool QQuickWebEngineSettings::javascriptEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings17javascriptEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->javascriptEnabled();
}

//  bool QQuickWebEngineSettings::javascriptCanOpenWindows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings24javascriptCanOpenWindowsEv(
    const QQuickWebEngineSettings *self) {
  return self->javascriptCanOpenWindows();
}

//  bool QQuickWebEngineSettings::javascriptCanAccessClipboard() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings28javascriptCanAccessClipboardEv(
    const QQuickWebEngineSettings *self) {
  return self->javascriptCanAccessClipboard();
}

//  bool QQuickWebEngineSettings::linksIncludedInFocusChain() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings25linksIncludedInFocusChainEv(
    const QQuickWebEngineSettings *self) {
  return self->linksIncludedInFocusChain();
}

//  bool QQuickWebEngineSettings::localStorageEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings19localStorageEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->localStorageEnabled();
}

//  bool QQuickWebEngineSettings::localContentCanAccessRemoteUrls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings31localContentCanAccessRemoteUrlsEv(
    const QQuickWebEngineSettings *self) {
  return self->localContentCanAccessRemoteUrls();
}

//  bool QQuickWebEngineSettings::spatialNavigationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings24spatialNavigationEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->spatialNavigationEnabled();
}

//  bool QQuickWebEngineSettings::localContentCanAccessFileUrls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings29localContentCanAccessFileUrlsEv(
    const QQuickWebEngineSettings *self) {
  return self->localContentCanAccessFileUrls();
}

//  bool QQuickWebEngineSettings::hyperlinkAuditingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings24hyperlinkAuditingEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->hyperlinkAuditingEnabled();
}

//  bool QQuickWebEngineSettings::errorPageEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings16errorPageEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->errorPageEnabled();
}

//  bool QQuickWebEngineSettings::pluginsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings14pluginsEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->pluginsEnabled();
}

//  bool QQuickWebEngineSettings::fullScreenSupportEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings24fullScreenSupportEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->fullScreenSupportEnabled();
}

//  QString QQuickWebEngineSettings::defaultTextEncoding() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickWebEngineSettings19defaultTextEncodingEv(
    const QQuickWebEngineSettings *self) {
  return new QString(self->defaultTextEncoding());
}

//  bool QQuickWebEngineSettings::screenCaptureEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings20screenCaptureEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->screenCaptureEnabled();
}

//  bool QQuickWebEngineSettings::webGLEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings12webGLEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->webGLEnabled();
}

//  bool QQuickWebEngineSettings::accelerated2dCanvasEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings26accelerated2dCanvasEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->accelerated2dCanvasEnabled();
}

//  bool QQuickWebEngineSettings::autoLoadIconsForPage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings20autoLoadIconsForPageEv(
    const QQuickWebEngineSettings *self) {
  return self->autoLoadIconsForPage();
}

//  bool QQuickWebEngineSettings::touchIconsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings17touchIconsEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->touchIconsEnabled();
}

//  bool QQuickWebEngineSettings::focusOnNavigationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings24focusOnNavigationEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->focusOnNavigationEnabled();
}

//  bool QQuickWebEngineSettings::printElementBackgrounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings23printElementBackgroundsEv(
    const QQuickWebEngineSettings *self) {
  return self->printElementBackgrounds();
}

//  bool QQuickWebEngineSettings::allowRunningInsecureContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings27allowRunningInsecureContentEv(
    const QQuickWebEngineSettings *self) {
  return self->allowRunningInsecureContent();
}

//  bool QQuickWebEngineSettings::allowGeolocationOnInsecureOrigins() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings33allowGeolocationOnInsecureOriginsEv(
    const QQuickWebEngineSettings *self) {
  return self->allowGeolocationOnInsecureOrigins();
}

//  bool QQuickWebEngineSettings::allowWindowActivationFromJavaScript() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings35allowWindowActivationFromJavaScriptEv(
    const QQuickWebEngineSettings *self) {
  return self->allowWindowActivationFromJavaScript();
}

//  bool QQuickWebEngineSettings::showScrollBars() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings14showScrollBarsEv(
    const QQuickWebEngineSettings *self) {
  return self->showScrollBars();
}

//  UnknownUrlSchemePolicy QQuickWebEngineSettings::unknownUrlSchemePolicy()
//      const
extern "C" Q_DECL_EXPORT
QQuickWebEngineSettings::UnknownUrlSchemePolicy ritual_ZNK23QQuickWebEngineSettings22unknownUrlSchemePolicyEv(
    const QQuickWebEngineSettings *self) {
  return self->unknownUrlSchemePolicy();
}

//  bool QQuickWebEngineSettings::playbackRequiresUserGesture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings27playbackRequiresUserGestureEv(
    const QQuickWebEngineSettings *self) {
  return self->playbackRequiresUserGesture();
}

//  bool QQuickWebEngineSettings::webRTCPublicInterfacesOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings26webRTCPublicInterfacesOnlyEv(
    const QQuickWebEngineSettings *self) {
  return self->webRTCPublicInterfacesOnly();
}

//  bool QQuickWebEngineSettings::javascriptCanPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings18javascriptCanPasteEv(
    const QQuickWebEngineSettings *self) {
  return self->javascriptCanPaste();
}

//  bool QQuickWebEngineSettings::dnsPrefetchEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings18dnsPrefetchEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->dnsPrefetchEnabled();
}

//  bool QQuickWebEngineSettings::pdfViewerEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings16pdfViewerEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->pdfViewerEnabled();
}

//  bool QQuickWebEngineSettings::navigateOnDropEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings21navigateOnDropEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->navigateOnDropEnabled();
}

//  bool QQuickWebEngineSettings::readingFromCanvasEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings24readingFromCanvasEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->readingFromCanvasEnabled();
}

//  bool QQuickWebEngineSettings::forceDarkMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings13forceDarkModeEv(
    const QQuickWebEngineSettings *self) {
  return self->forceDarkMode();
}

//  bool QQuickWebEngineSettings::scrollAnimatorEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings21scrollAnimatorEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->scrollAnimatorEnabled();
}

//  ImageAnimationPolicy QQuickWebEngineSettings::imageAnimationPolicy()
//      const
extern "C" Q_DECL_EXPORT
QQuickWebEngineSettings::ImageAnimationPolicy ritual_ZNK23QQuickWebEngineSettings20imageAnimationPolicyEv(
    const QQuickWebEngineSettings *self) {
  return self->imageAnimationPolicy();
}

//  bool QQuickWebEngineSettings::printHeaderAndFooter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings20printHeaderAndFooterEv(
    const QQuickWebEngineSettings *self) {
  return self->printHeaderAndFooter();
}

//  bool QQuickWebEngineSettings::preferCSSMarginsForPrinting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings27preferCSSMarginsForPrintingEv(
    const QQuickWebEngineSettings *self) {
  return self->preferCSSMarginsForPrinting();
}

//  bool QQuickWebEngineSettings::touchEventsApiEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings21touchEventsApiEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->touchEventsApiEnabled();
}

//  bool QQuickWebEngineSettings::backForwardCacheEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings23backForwardCacheEnabledEv(
    const QQuickWebEngineSettings *self) {
  return self->backForwardCacheEnabled();
}

//  bool QQuickWebEngineSettings::trimAccessibilityIdentifiers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickWebEngineSettings28trimAccessibilityIdentifiersEv(
    const QQuickWebEngineSettings *self) {
  return self->trimAccessibilityIdentifiers();
}

//  void QQuickWebEngineSettings::setAutoLoadImages(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings17setAutoLoadImagesEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setAutoLoadImages(on);
}

//  void QQuickWebEngineSettings::setJavascriptEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings20setJavascriptEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setJavascriptEnabled(on);
}

//  void QQuickWebEngineSettings::setJavascriptCanOpenWindows(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27setJavascriptCanOpenWindowsEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setJavascriptCanOpenWindows(on);
}

//  void QQuickWebEngineSettings::setJavascriptCanAccessClipboard(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31setJavascriptCanAccessClipboardEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setJavascriptCanAccessClipboard(on);
}

//  void QQuickWebEngineSettings::setLinksIncludedInFocusChain(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings28setLinksIncludedInFocusChainEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setLinksIncludedInFocusChain(on);
}

//  void QQuickWebEngineSettings::setLocalStorageEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings22setLocalStorageEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setLocalStorageEnabled(on);
}

//  void QQuickWebEngineSettings::setLocalContentCanAccessRemoteUrls(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings34setLocalContentCanAccessRemoteUrlsEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setLocalContentCanAccessRemoteUrls(on);
}

//  void QQuickWebEngineSettings::setSpatialNavigationEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27setSpatialNavigationEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setSpatialNavigationEnabled(on);
}

//  void QQuickWebEngineSettings::setLocalContentCanAccessFileUrls(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings32setLocalContentCanAccessFileUrlsEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setLocalContentCanAccessFileUrls(on);
}

//  void QQuickWebEngineSettings::setHyperlinkAuditingEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27setHyperlinkAuditingEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setHyperlinkAuditingEnabled(on);
}

//  void QQuickWebEngineSettings::setErrorPageEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings19setErrorPageEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setErrorPageEnabled(on);
}

//  void QQuickWebEngineSettings::setPluginsEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings17setPluginsEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setPluginsEnabled(on);
}

//  void QQuickWebEngineSettings::setFullScreenSupportEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27setFullScreenSupportEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setFullScreenSupportEnabled(on);
}

//  void QQuickWebEngineSettings::setDefaultTextEncoding(QString encoding)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings22setDefaultTextEncodingE7QString(
    QQuickWebEngineSettings *self,
    const QString *encoding) {
  self->setDefaultTextEncoding(*encoding);
}

//  void QQuickWebEngineSettings::setScreenCaptureEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings23setScreenCaptureEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setScreenCaptureEnabled(on);
}

//  void QQuickWebEngineSettings::setWebGLEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings15setWebGLEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setWebGLEnabled(on);
}

//  void QQuickWebEngineSettings::setAccelerated2dCanvasEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings29setAccelerated2dCanvasEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setAccelerated2dCanvasEnabled(on);
}

//  void QQuickWebEngineSettings::setAutoLoadIconsForPage(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings23setAutoLoadIconsForPageEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setAutoLoadIconsForPage(on);
}

//  void QQuickWebEngineSettings::setTouchIconsEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings20setTouchIconsEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setTouchIconsEnabled(on);
}

//  void QQuickWebEngineSettings::setFocusOnNavigationEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27setFocusOnNavigationEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setFocusOnNavigationEnabled(on);
}

//  void QQuickWebEngineSettings::setPrintElementBackgrounds(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings26setPrintElementBackgroundsEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setPrintElementBackgrounds(on);
}

//  void QQuickWebEngineSettings::setAllowRunningInsecureContent(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings30setAllowRunningInsecureContentEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setAllowRunningInsecureContent(on);
}

//  void QQuickWebEngineSettings::setAllowGeolocationOnInsecureOrigins(bool
//      on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings36setAllowGeolocationOnInsecureOriginsEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setAllowGeolocationOnInsecureOrigins(on);
}

//  void QQuickWebEngineSettings::setAllowWindowActivationFromJavaScript(bool
//      on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings38setAllowWindowActivationFromJavaScriptEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setAllowWindowActivationFromJavaScript(on);
}

//  void QQuickWebEngineSettings::setShowScrollBars(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings17setShowScrollBarsEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setShowScrollBars(on);
}

//  void
//      QQuickWebEngineSettings::setUnknownUrlSchemePolicy(UnknownUrlSchemePo
//      licy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings25setUnknownUrlSchemePolicyENS_22UnknownUrlSchemePolicyE(
    QQuickWebEngineSettings *self,
    QQuickWebEngineSettings::UnknownUrlSchemePolicy policy) {
  self->setUnknownUrlSchemePolicy(policy);
}

//  void QQuickWebEngineSettings::setPlaybackRequiresUserGesture(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings30setPlaybackRequiresUserGestureEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setPlaybackRequiresUserGesture(on);
}

//  void QQuickWebEngineSettings::setWebRTCPublicInterfacesOnly(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings29setWebRTCPublicInterfacesOnlyEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setWebRTCPublicInterfacesOnly(on);
}

//  void QQuickWebEngineSettings::setJavascriptCanPaste(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings21setJavascriptCanPasteEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setJavascriptCanPaste(on);
}

//  void QQuickWebEngineSettings::setDnsPrefetchEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings21setDnsPrefetchEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setDnsPrefetchEnabled(on);
}

//  void QQuickWebEngineSettings::setPdfViewerEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings19setPdfViewerEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setPdfViewerEnabled(on);
}

//  void QQuickWebEngineSettings::setNavigateOnDropEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings24setNavigateOnDropEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setNavigateOnDropEnabled(on);
}

//  void QQuickWebEngineSettings::setReadingFromCanvasEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27setReadingFromCanvasEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setReadingFromCanvasEnabled(on);
}

//  void QQuickWebEngineSettings::setForceDarkMode(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings16setForceDarkModeEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setForceDarkMode(on);
}

//  void QQuickWebEngineSettings::setScrollAnimatorEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings24setScrollAnimatorEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setScrollAnimatorEnabled(on);
}

//  void
//      QQuickWebEngineSettings::setImageAnimationPolicy(ImageAnimationPolicy
//      policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings23setImageAnimationPolicyENS_20ImageAnimationPolicyE(
    QQuickWebEngineSettings *self,
    QQuickWebEngineSettings::ImageAnimationPolicy policy) {
  self->setImageAnimationPolicy(policy);
}

//  void QQuickWebEngineSettings::setPrintHeaderAndFooter(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings23setPrintHeaderAndFooterEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setPrintHeaderAndFooter(on);
}

//  void QQuickWebEngineSettings::setPreferCSSMarginsForPrinting(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings30setPreferCSSMarginsForPrintingEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setPreferCSSMarginsForPrinting(on);
}

//  void QQuickWebEngineSettings::setTouchEventsApiEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings24setTouchEventsApiEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setTouchEventsApiEnabled(on);
}

//  void QQuickWebEngineSettings::setBackForwardCacheEnabled(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings26setBackForwardCacheEnabledEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setBackForwardCacheEnabled(on);
}

//  void QQuickWebEngineSettings::setTrimAccessibilityIdentifiers(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31setTrimAccessibilityIdentifiersEb(
    QQuickWebEngineSettings *self,
    bool on) {
  self->setTrimAccessibilityIdentifiers(on);
}

//  void QQuickWebEngineSettings::autoLoadImagesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings21autoLoadImagesChangedEv(
    QQuickWebEngineSettings *self) {
  self->autoLoadImagesChanged();
}

//  void QQuickWebEngineSettings::javascriptEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings24javascriptEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->javascriptEnabledChanged();
}

//  void QQuickWebEngineSettings::javascriptCanOpenWindowsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31javascriptCanOpenWindowsChangedEv(
    QQuickWebEngineSettings *self) {
  self->javascriptCanOpenWindowsChanged();
}

//  void QQuickWebEngineSettings::javascriptCanAccessClipboardChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings35javascriptCanAccessClipboardChangedEv(
    QQuickWebEngineSettings *self) {
  self->javascriptCanAccessClipboardChanged();
}

//  void QQuickWebEngineSettings::linksIncludedInFocusChainChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings32linksIncludedInFocusChainChangedEv(
    QQuickWebEngineSettings *self) {
  self->linksIncludedInFocusChainChanged();
}

//  void QQuickWebEngineSettings::localStorageEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings26localStorageEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->localStorageEnabledChanged();
}

//  void QQuickWebEngineSettings::localContentCanAccessRemoteUrlsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings38localContentCanAccessRemoteUrlsChangedEv(
    QQuickWebEngineSettings *self) {
  self->localContentCanAccessRemoteUrlsChanged();
}

//  void QQuickWebEngineSettings::spatialNavigationEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31spatialNavigationEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->spatialNavigationEnabledChanged();
}

//  void QQuickWebEngineSettings::localContentCanAccessFileUrlsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings36localContentCanAccessFileUrlsChangedEv(
    QQuickWebEngineSettings *self) {
  self->localContentCanAccessFileUrlsChanged();
}

//  void QQuickWebEngineSettings::hyperlinkAuditingEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31hyperlinkAuditingEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->hyperlinkAuditingEnabledChanged();
}

//  void QQuickWebEngineSettings::errorPageEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings23errorPageEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->errorPageEnabledChanged();
}

//  void QQuickWebEngineSettings::pluginsEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings21pluginsEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->pluginsEnabledChanged();
}

//  void QQuickWebEngineSettings::fullScreenSupportEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31fullScreenSupportEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->fullScreenSupportEnabledChanged();
}

//  void QQuickWebEngineSettings::defaultTextEncodingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings26defaultTextEncodingChangedEv(
    QQuickWebEngineSettings *self) {
  self->defaultTextEncodingChanged();
}

//  void QQuickWebEngineSettings::screenCaptureEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27screenCaptureEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->screenCaptureEnabledChanged();
}

//  void QQuickWebEngineSettings::webGLEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings19webGLEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->webGLEnabledChanged();
}

//  void QQuickWebEngineSettings::accelerated2dCanvasEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings33accelerated2dCanvasEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->accelerated2dCanvasEnabledChanged();
}

//  void QQuickWebEngineSettings::autoLoadIconsForPageChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27autoLoadIconsForPageChangedEv(
    QQuickWebEngineSettings *self) {
  self->autoLoadIconsForPageChanged();
}

//  void QQuickWebEngineSettings::touchIconsEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings24touchIconsEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->touchIconsEnabledChanged();
}

//  void QQuickWebEngineSettings::focusOnNavigationEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31focusOnNavigationEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->focusOnNavigationEnabledChanged();
}

//  void QQuickWebEngineSettings::printElementBackgroundsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings30printElementBackgroundsChangedEv(
    QQuickWebEngineSettings *self) {
  self->printElementBackgroundsChanged();
}

//  void QQuickWebEngineSettings::allowRunningInsecureContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings34allowRunningInsecureContentChangedEv(
    QQuickWebEngineSettings *self) {
  self->allowRunningInsecureContentChanged();
}

//  void QQuickWebEngineSettings::allowGeolocationOnInsecureOriginsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings40allowGeolocationOnInsecureOriginsChangedEv(
    QQuickWebEngineSettings *self) {
  self->allowGeolocationOnInsecureOriginsChanged();
}

//  void
//      QQuickWebEngineSettings::allowWindowActivationFromJavaScriptChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings42allowWindowActivationFromJavaScriptChangedEv(
    QQuickWebEngineSettings *self) {
  self->allowWindowActivationFromJavaScriptChanged();
}

//  void QQuickWebEngineSettings::showScrollBarsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings21showScrollBarsChangedEv(
    QQuickWebEngineSettings *self) {
  self->showScrollBarsChanged();
}

//  void QQuickWebEngineSettings::unknownUrlSchemePolicyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings29unknownUrlSchemePolicyChangedEv(
    QQuickWebEngineSettings *self) {
  self->unknownUrlSchemePolicyChanged();
}

//  void QQuickWebEngineSettings::playbackRequiresUserGestureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings34playbackRequiresUserGestureChangedEv(
    QQuickWebEngineSettings *self) {
  self->playbackRequiresUserGestureChanged();
}

//  void QQuickWebEngineSettings::webRTCPublicInterfacesOnlyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings33webRTCPublicInterfacesOnlyChangedEv(
    QQuickWebEngineSettings *self) {
  self->webRTCPublicInterfacesOnlyChanged();
}

//  void QQuickWebEngineSettings::javascriptCanPasteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings25javascriptCanPasteChangedEv(
    QQuickWebEngineSettings *self) {
  self->javascriptCanPasteChanged();
}

//  void QQuickWebEngineSettings::dnsPrefetchEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings25dnsPrefetchEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->dnsPrefetchEnabledChanged();
}

//  void QQuickWebEngineSettings::pdfViewerEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings23pdfViewerEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->pdfViewerEnabledChanged();
}

//  void QQuickWebEngineSettings::navigateOnDropEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings28navigateOnDropEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->navigateOnDropEnabledChanged();
}

//  void QQuickWebEngineSettings::readingFromCanvasEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings31readingFromCanvasEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->readingFromCanvasEnabledChanged();
}

//  void QQuickWebEngineSettings::forceDarkModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings20forceDarkModeChangedEv(
    QQuickWebEngineSettings *self) {
  self->forceDarkModeChanged();
}

//  void QQuickWebEngineSettings::scrollAnimatorEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings28scrollAnimatorEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->scrollAnimatorEnabledChanged();
}

//  void QQuickWebEngineSettings::imageAnimationPolicyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27imageAnimationPolicyChangedEv(
    QQuickWebEngineSettings *self) {
  self->imageAnimationPolicyChanged();
}

//  void QQuickWebEngineSettings::printHeaderAndFooterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings27printHeaderAndFooterChangedEv(
    QQuickWebEngineSettings *self) {
  self->printHeaderAndFooterChanged();
}

//  void QQuickWebEngineSettings::preferCSSMarginsForPrintingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings34preferCSSMarginsForPrintingChangedEv(
    QQuickWebEngineSettings *self) {
  self->preferCSSMarginsForPrintingChanged();
}

//  void QQuickWebEngineSettings::touchEventsApiEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings28touchEventsApiEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->touchEventsApiEnabledChanged();
}

//  void QQuickWebEngineSettings::backForwardCacheEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings30backForwardCacheEnabledChangedEv(
    QQuickWebEngineSettings *self) {
  self->backForwardCacheEnabledChanged();
}

//  void QQuickWebEngineSettings::trimAccessibilityIdentifiersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings35trimAccessibilityIdentifiersChangedEv(
    QQuickWebEngineSettings *self) {
  self->trimAccessibilityIdentifiersChanged();
}

//  QQuickWebEngineSettings::QQuickWebEngineSettings(QQuickWebEngineSettings
//      *parentSettings)
extern "C" Q_DECL_EXPORT
QQuickWebEngineSettings *ritual_ZN23QQuickWebEngineSettingsC1EPS_(
    QQuickWebEngineSettings *parentSettings) {
  return new CuteQQuickWebEngineSettings(parentSettings);
}

//  void QQuickWebEngineSettings::setParentSettings(QQuickWebEngineSettings
//      *parentSettings)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickWebEngineSettings17setParentSettingsEPS_(
    QQuickWebEngineSettings *self,
    QQuickWebEngineSettings *parentSettings) {
  self->setParentSettings(parentSettings);
}

//  a Python function taken by a CuteQQuickWebEngineSettings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineSettings(
    QQuickWebEngineSettings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineSettings *>(self)->take(key, call);
}
