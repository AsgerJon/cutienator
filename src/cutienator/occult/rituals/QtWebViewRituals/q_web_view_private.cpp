//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebView/6.12.0/QtWebView/private/qwebview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebView/QtWebView>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebView/6.12.0/QtWebView/private/qwebview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebViewPrivate that Python can take functions over in. Every QWebViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWebViewPrivateCall0)(const void *, QObject *, int *);
typedef void * (*CuteQWebViewPrivateCall1)(const void *, int *);
typedef QString * (*CuteQWebViewPrivateCall2)(const void *, int *);
typedef void (*CuteQWebViewPrivateCall3)(const void *, const QString *, int *);
typedef void (*CuteQWebViewPrivateCall4)(const void *, const QUrl *, int *);
typedef bool (*CuteQWebViewPrivateCall5)(const void *, int *);
typedef bool (*CuteQWebViewPrivateCall6)(const void *, int *);
typedef QString * (*CuteQWebViewPrivateCall7)(const void *, int *);
typedef const QUrl * (*CuteQWebViewPrivateCall8)(const void *, int *);
typedef int (*CuteQWebViewPrivateCall9)(const void *, int *);
typedef bool (*CuteQWebViewPrivateCall10)(const void *, int *);
typedef void (*CuteQWebViewPrivateCall11)(const void *, int *);
typedef void (*CuteQWebViewPrivateCall12)(const void *, int *);
typedef void (*CuteQWebViewPrivateCall13)(const void *, int *);
typedef void (*CuteQWebViewPrivateCall14)(const void *, int *);
typedef void (*CuteQWebViewPrivateCall15)(const void *, const QString *, const QUrl *, int *);
typedef void (*CuteQWebViewPrivateCall16)(const void *, const QString *, const QString *, const QString *, int *);
typedef void (*CuteQWebViewPrivateCall17)(const void *, const QString *, const QString *, int *);
typedef void (*CuteQWebViewPrivateCall18)(const void *, int *);
typedef void * (*CuteQWebViewPrivateCall19)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebViewPrivateCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebViewPrivateCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPrivateCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPrivateCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPrivateCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPrivateCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPrivateCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebViewPrivate : public QWebViewPrivate {
public:
  using QWebViewPrivate::QWebViewPrivate;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QWebViewPrivate10initializeEP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate8settingsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate13httpUserAgentEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate16setHttpUserAgentERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate6setUrlERK4QUrl")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate9canGoBackEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate12canGoForwardEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate5titleEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate3urlEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate12loadProgressEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate9isLoadingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate6goBackEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate9goForwardEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate4stopEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate6reloadEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate8loadHtmlERK7QStringRK4QUrl")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate9setCookieERK7QStringS2_S2_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate12deleteCookieERK7QStringS2_")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QWebViewPrivate16deleteAllCookiesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QWebViewPrivate12nativeWindowEv")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QWebViewPrivate::initialize(QObject *context)
  void initialize(QObject *context) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebViewPrivateCall0 call = reinterpret_cast<CuteQWebViewPrivateCall0>(taken[0]);
      call(this, context, &handled);
      if (handled) return;
    }
  }

  //  QWebViewSettingsPrivate *QWebViewPrivate::settings() const
  QWebViewSettingsPrivate *settings() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebViewPrivateCall1 call = reinterpret_cast<CuteQWebViewPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWebViewSettingsPrivate *>(given);
    }
    return {};
  }

  //  QString QWebViewPrivate::httpUserAgent() const
  QString httpUserAgent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebViewPrivateCall2 call = reinterpret_cast<CuteQWebViewPrivateCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QWebViewPrivate::setHttpUserAgent(const QString &httpUserAgent)
  void setHttpUserAgent(const QString &httpUserAgent) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebViewPrivateCall3 call = reinterpret_cast<CuteQWebViewPrivateCall3>(taken[3]);
      call(this, &httpUserAgent, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::setUrl(const QUrl &url)
  void setUrl(const QUrl &url) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebViewPrivateCall4 call = reinterpret_cast<CuteQWebViewPrivateCall4>(taken[4]);
      call(this, &url, &handled);
      if (handled) return;
    }
  }

  //  bool QWebViewPrivate::canGoBack() const
  bool canGoBack() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebViewPrivateCall5 call = reinterpret_cast<CuteQWebViewPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QWebViewPrivate::canGoForward() const
  bool canGoForward() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebViewPrivateCall6 call = reinterpret_cast<CuteQWebViewPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QWebViewPrivate::title() const
  QString title() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWebViewPrivateCall7 call = reinterpret_cast<CuteQWebViewPrivateCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QUrl QWebViewPrivate::url() const
  QUrl url() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWebViewPrivateCall8 call = reinterpret_cast<CuteQWebViewPrivateCall8>(taken[8]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QWebViewPrivate::loadProgress() const
  int loadProgress() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWebViewPrivateCall9 call = reinterpret_cast<CuteQWebViewPrivateCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QWebViewPrivate::isLoading() const
  bool isLoading() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWebViewPrivateCall10 call = reinterpret_cast<CuteQWebViewPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QWebViewPrivate::goBack()
  void goBack() override {
    if (taken[11]) {
      int handled = 0;
      CuteQWebViewPrivateCall11 call = reinterpret_cast<CuteQWebViewPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::goForward()
  void goForward() override {
    if (taken[12]) {
      int handled = 0;
      CuteQWebViewPrivateCall12 call = reinterpret_cast<CuteQWebViewPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::stop()
  void stop() override {
    if (taken[13]) {
      int handled = 0;
      CuteQWebViewPrivateCall13 call = reinterpret_cast<CuteQWebViewPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::reload()
  void reload() override {
    if (taken[14]) {
      int handled = 0;
      CuteQWebViewPrivateCall14 call = reinterpret_cast<CuteQWebViewPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::loadHtml(const QString &html, const QUrl
  //      &baseUrl)
  void loadHtml(const QString &html, const QUrl &baseUrl) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWebViewPrivateCall15 call = reinterpret_cast<CuteQWebViewPrivateCall15>(taken[15]);
      call(this, &html, &baseUrl, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::setCookie(const QString &domain, const QString
  //      &name, const QString &value)
  void setCookie(
      const QString &domain,
      const QString &name,
      const QString &value) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWebViewPrivateCall16 call = reinterpret_cast<CuteQWebViewPrivateCall16>(taken[16]);
      call(this, &domain, &name, &value, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::deleteCookie(const QString &domain, const
  //      QString &name)
  void deleteCookie(const QString &domain, const QString &name) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWebViewPrivateCall17 call = reinterpret_cast<CuteQWebViewPrivateCall17>(taken[17]);
      call(this, &domain, &name, &handled);
      if (handled) return;
    }
  }

  //  void QWebViewPrivate::deleteAllCookies()
  void deleteAllCookies() override {
    if (taken[18]) {
      int handled = 0;
      CuteQWebViewPrivateCall18 call = reinterpret_cast<CuteQWebViewPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QWindow *QWebViewPrivate::nativeWindow() const
  QWindow *nativeWindow() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQWebViewPrivateCall19 call = reinterpret_cast<CuteQWebViewPrivateCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWebViewPrivateCall20 call = reinterpret_cast<CuteQWebViewPrivateCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWebViewPrivateCall21 call = reinterpret_cast<CuteQWebViewPrivateCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWebViewPrivateCall22 call = reinterpret_cast<CuteQWebViewPrivateCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWebViewPrivateCall23 call = reinterpret_cast<CuteQWebViewPrivateCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWebViewPrivateCall24 call = reinterpret_cast<CuteQWebViewPrivateCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWebViewPrivateCall25 call = reinterpret_cast<CuteQWebViewPrivateCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWebViewPrivateCall26 call = reinterpret_cast<CuteQWebViewPrivateCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  void QWebViewPrivate::initialize(QObject *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate10initializeEP7QObject(
    QWebViewPrivate *self,
    QObject *context) {
  self->initialize(context);
}

//  QWebViewSettingsPrivate *QWebViewPrivate::settings() const
extern "C" Q_DECL_EXPORT
QWebViewSettingsPrivate *ritual_ZNK15QWebViewPrivate8settingsEv(
    const QWebViewPrivate *self) {
  return self->settings();
}

//  QString QWebViewPrivate::httpUserAgent() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QWebViewPrivate13httpUserAgentEv(
    const QWebViewPrivate *self) {
  return new QString(self->httpUserAgent());
}

//  void QWebViewPrivate::setHttpUserAgent(const QString &httpUserAgent)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate16setHttpUserAgentERK7QString(
    QWebViewPrivate *self,
    const QString *httpUserAgent) {
  self->setHttpUserAgent(*httpUserAgent);
}

//  void QWebViewPrivate::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate6setUrlERK4QUrl(
    QWebViewPrivate *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  bool QWebViewPrivate::canGoBack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebViewPrivate9canGoBackEv(const QWebViewPrivate *self) {
  return self->canGoBack();
}

//  bool QWebViewPrivate::canGoForward() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebViewPrivate12canGoForwardEv(
    const QWebViewPrivate *self) {
  return self->canGoForward();
}

//  QString QWebViewPrivate::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QWebViewPrivate5titleEv(const QWebViewPrivate *self) {
  return new QString(self->title());
}

//  QUrl QWebViewPrivate::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QWebViewPrivate3urlEv(const QWebViewPrivate *self) {
  return new QUrl(self->url());
}

//  int QWebViewPrivate::loadProgress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QWebViewPrivate12loadProgressEv(
    const QWebViewPrivate *self) {
  return self->loadProgress();
}

//  bool QWebViewPrivate::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebViewPrivate9isLoadingEv(const QWebViewPrivate *self) {
  return self->isLoading();
}

//  void QWebViewPrivate::goBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate6goBackEv(QWebViewPrivate *self) {
  self->goBack();
}

//  void QWebViewPrivate::goForward()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate9goForwardEv(QWebViewPrivate *self) {
  self->goForward();
}

//  void QWebViewPrivate::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate4stopEv(QWebViewPrivate *self) {
  self->stop();
}

//  void QWebViewPrivate::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate6reloadEv(QWebViewPrivate *self) {
  self->reload();
}

//  void QWebViewPrivate::loadHtml(const QString &html, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate8loadHtmlERK7QStringRK4QUrl(
    QWebViewPrivate *self,
    const QString *html,
    const QUrl *baseUrl) {
  self->loadHtml(*html, *baseUrl);
}

//  void QWebViewPrivate::setCookie(const QString &domain, const QString
//      &name, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate9setCookieERK7QStringS2_S2_(
    QWebViewPrivate *self,
    const QString *domain,
    const QString *name,
    const QString *value) {
  self->setCookie(*domain, *name, *value);
}

//  void QWebViewPrivate::deleteCookie(const QString &domain, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate12deleteCookieERK7QStringS2_(
    QWebViewPrivate *self,
    const QString *domain,
    const QString *name) {
  self->deleteCookie(*domain, *name);
}

//  void QWebViewPrivate::deleteAllCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewPrivate16deleteAllCookiesEv(QWebViewPrivate *self) {
  self->deleteAllCookies();
}

//  QWindow *QWebViewPrivate::nativeWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK15QWebViewPrivate12nativeWindowEv(
    const QWebViewPrivate *self) {
  return self->nativeWindow();
}

//  a Python function taken by a CuteQWebViewPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebViewPrivate(
    QWebViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebViewPrivate *>(self)->take(key, call);
}
