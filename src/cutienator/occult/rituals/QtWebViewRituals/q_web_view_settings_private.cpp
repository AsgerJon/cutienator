//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebView/6.12.0/QtWebView/private/qwebview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebView/QtWebView>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebView/6.12.0/QtWebView/private/qwebview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QWebViewSettingsPrivate that Python can take functions over in. Every QWebViewSettingsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWebViewSettingsPrivateCall0)(const void *, int, bool, int *);
typedef bool (*CuteQWebViewSettingsPrivateCall1)(const void *, int, int *);
class CuteQWebViewSettingsPrivate : public QWebViewSettingsPrivate {
public:
  using QWebViewSettingsPrivate::QWebViewSettingsPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QWebViewSettings14doSetAttributeENS_12WebAttributeEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QWebViewSettings15doTestAttributeENS_12WebAttributeE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QWebViewSettings::doSetAttribute(WebAttribute a, bool v)
  void doSetAttribute(QWebViewSettings::WebAttribute a, bool v) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebViewSettingsPrivateCall0 call = reinterpret_cast<CuteQWebViewSettingsPrivateCall0>(taken[0]);
      call(this, static_cast<int>(a), v, &handled);
      if (handled) return;
    }
  }

  //  bool QWebViewSettings::doTestAttribute(WebAttribute a) const
  bool doTestAttribute(QWebViewSettings::WebAttribute a) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebViewSettingsPrivateCall1 call = reinterpret_cast<CuteQWebViewSettingsPrivateCall1>(taken[1]);
      bool given = call(this, static_cast<int>(a), &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QWebViewSettingsPrivate::~QWebViewSettingsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebViewSettingsPrivateD1Ev(QWebViewSettingsPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQWebViewSettingsPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebViewSettingsPrivate(
    QWebViewSettingsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebViewSettingsPrivate *>(self)->take(key, call);
}
