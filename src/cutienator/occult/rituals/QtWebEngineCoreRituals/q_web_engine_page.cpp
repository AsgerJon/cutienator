//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginepage.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWebEngineCore/qwebenginepage.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtWebEngineCore/qwebenginehttprequest.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qicon.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpageranges.h>
#include <QtWebEngineCore/qwebengineframe.h>
#include <QtCore/qanystringview.h>
#include <QtWebEngineCore/qwebengineloadinginfo.h>
#include <QtCore/qrect.h>
#include <QtWebEngineCore/qwebenginefullscreenrequest.h>
#include <QtWebEngineCore/qwebenginepermission.h>
#include <QtWebEngineCore/qwebenginequotarequest.h>
#include <QtWebEngineCore/qwebengineregisterprotocolhandlerrequest.h>
#include <QtWebEngineCore/qwebenginefilesystemaccessrequest.h>
#include <QtWebEngineCore/qwebengineclientcertificateselection.h>
#include <QtWebEngineCore/qwebenginedesktopmediarequest.h>
#include <QtWebEngineCore/qwebenginecertificateerror.h>
#include <QtWebEngineCore/qwebenginefindtextresult.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <optional>
#include <QtWebEngineCore/QWebEngineFrame>
#include <QtCore/QAnyStringView>

//  Only a class built on QWebEnginePage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWebEnginePage : QWebEnginePage {
  using QWebEnginePage::createWindow;
  using QWebEnginePage::javaScriptAlert;
  using QWebEnginePage::javaScriptConfirm;
  using QWebEnginePage::javaScriptPrompt;
  using QWebEnginePage::javaScriptConsoleMessage;
  using QWebEnginePage::acceptNavigationRequest;
};

//  A QWebEnginePage that Python can take functions over in. Every QWebEnginePage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWebEnginePageCall0)(const void *, int, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEnginePageCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQWebEnginePageCall2)(const void *, int, int *);
typedef void (*CuteQWebEnginePageCall3)(const void *, const QUrl *, const QString *, int *);
typedef bool (*CuteQWebEnginePageCall4)(const void *, const QUrl *, const QString *, int *);
typedef bool (*CuteQWebEnginePageCall5)(const void *, const QUrl *, const QString *, const QString *, QString *, int *);
typedef void (*CuteQWebEnginePageCall6)(const void *, int, const QString *, int, const QString *, int *);
typedef bool (*CuteQWebEnginePageCall7)(const void *, const QUrl *, int, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEnginePageCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEnginePageCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEnginePageCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEnginePageCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEnginePageCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEnginePageCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEnginePage : public QWebEnginePage {
public:
  using QWebEnginePage::QWebEnginePage;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWebEnginePage13triggerActionENS_9WebActionEb")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QWebEnginePage12createWindowENS_13WebWindowTypeE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWebEnginePage15javaScriptAlertERK4QUrlRK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWebEnginePage17javaScriptConfirmERK4QUrlRK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWebEnginePage16javaScriptPromptERK4QUrlRK7QStringS5_PS3_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWebEnginePage24javaScriptConsoleMessageENS_29JavaScriptConsoleMessageLevelERK7QStringiS3_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWebEnginePage23acceptNavigationRequestERK4QUrlNS_14NavigationTypeEb")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QWebEnginePage::triggerAction(WebAction action, bool checked)
  void triggerAction(
      QWebEnginePage::WebAction action,
      bool checked) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEnginePageCall0 call = reinterpret_cast<CuteQWebEnginePageCall0>(taken[0]);
      call(this, static_cast<int>(action), checked, &handled);
      if (handled) return;
    }
    QWebEnginePage::triggerAction(action, checked);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWebEnginePage::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEnginePageCall1 call = reinterpret_cast<CuteQWebEnginePageCall1>(taken[1]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWebEnginePage::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QWebEnginePage *QWebEnginePage::createWindow(WebWindowType type)
  QWebEnginePage *createWindow(QWebEnginePage::WebWindowType type) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebEnginePageCall2 call = reinterpret_cast<CuteQWebEnginePageCall2>(taken[2]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<QWebEnginePage *>(given);
    }
    return QWebEnginePage::createWindow(type);
  }

  //  void QWebEnginePage::javaScriptAlert(const QUrl &securityOrigin,
  //      const QString &msg)
  void javaScriptAlert(
      const QUrl &securityOrigin,
      const QString &msg) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebEnginePageCall3 call = reinterpret_cast<CuteQWebEnginePageCall3>(taken[3]);
      call(this, &securityOrigin, &msg, &handled);
      if (handled) return;
    }
    QWebEnginePage::javaScriptAlert(securityOrigin, msg);
  }

  //  bool QWebEnginePage::javaScriptConfirm(const QUrl &securityOrigin,
  //      const QString &msg)
  bool javaScriptConfirm(
      const QUrl &securityOrigin,
      const QString &msg) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebEnginePageCall4 call = reinterpret_cast<CuteQWebEnginePageCall4>(taken[4]);
      bool given = call(this, &securityOrigin, &msg, &handled);
      if (handled) return given;
    }
    return QWebEnginePage::javaScriptConfirm(securityOrigin, msg);
  }

  //  bool QWebEnginePage::javaScriptPrompt(const QUrl &securityOrigin,
  //      const QString &msg, const QString &defaultValue, QString *result)
  bool javaScriptPrompt(
      const QUrl &securityOrigin,
      const QString &msg,
      const QString &defaultValue,
      QString *result) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebEnginePageCall5 call = reinterpret_cast<CuteQWebEnginePageCall5>(taken[5]);
      bool given = call(this, &securityOrigin, &msg, &defaultValue, result, &handled);
      if (handled) return given;
    }
    return QWebEnginePage::javaScriptPrompt(securityOrigin, msg, defaultValue, result);
  }

  //  void QWebEnginePage::javaScriptConsoleMessage(JavaScriptConsoleMessag
  //      eLevel level, const QString &message, int lineNumber, const
  //      QString &sourceID)
  void javaScriptConsoleMessage(
      QWebEnginePage::JavaScriptConsoleMessageLevel level,
      const QString &message,
      int lineNumber,
      const QString &sourceID) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebEnginePageCall6 call = reinterpret_cast<CuteQWebEnginePageCall6>(taken[6]);
      call(this, static_cast<int>(level), &message, lineNumber, &sourceID, &handled);
      if (handled) return;
    }
    QWebEnginePage::javaScriptConsoleMessage(level, message, lineNumber, sourceID);
  }

  //  bool QWebEnginePage::acceptNavigationRequest(const QUrl &url,
  //      NavigationType type, bool isMainFrame)
  bool acceptNavigationRequest(
      const QUrl &url,
      QWebEnginePage::NavigationType type,
      bool isMainFrame) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWebEnginePageCall7 call = reinterpret_cast<CuteQWebEnginePageCall7>(taken[7]);
      bool given = call(this, &url, static_cast<int>(type), isMainFrame, &handled);
      if (handled) return given;
    }
    return QWebEnginePage::acceptNavigationRequest(url, type, isMainFrame);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWebEnginePageCall8 call = reinterpret_cast<CuteQWebEnginePageCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWebEnginePageCall9 call = reinterpret_cast<CuteQWebEnginePageCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWebEnginePageCall10 call = reinterpret_cast<CuteQWebEnginePageCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWebEnginePageCall11 call = reinterpret_cast<CuteQWebEnginePageCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWebEnginePageCall12 call = reinterpret_cast<CuteQWebEnginePageCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWebEnginePageCall13 call = reinterpret_cast<CuteQWebEnginePageCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEnginePage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWebEnginePage10metaObjectEv(
    const QWebEnginePage *self) {
  return self->metaObject();
}

//  void *QWebEnginePage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QWebEnginePage11qt_metacastEPKc(
    QWebEnginePage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEnginePage::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QWebEnginePage11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEnginePage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEnginePage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWebEnginePage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEnginePage::tr(s, c, n));
}

//  QWebEnginePage::QWebEnginePage(QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_ZN14QWebEnginePageC1EP7QObject(QObject *parent) {
  return new CuteQWebEnginePage(parent);
}

//  QWebEnginePage::QWebEnginePage(QWebEngineProfile *profile, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_ZN14QWebEnginePageC1EP17QWebEngineProfileP7QObject(
    QWebEngineProfile *profile,
    QObject *parent) {
  return new CuteQWebEnginePage(profile, parent);
}

//  QWebEnginePage::~QWebEnginePage()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePageD1Ev(QWebEnginePage *self) {
  delete self;
}

//  QWebEngineHistory *QWebEnginePage::history() const
extern "C" Q_DECL_EXPORT
QWebEngineHistory *ritual_ZNK14QWebEnginePage7historyEv(
    const QWebEnginePage *self) {
  return self->history();
}

//  bool QWebEnginePage::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWebEnginePage12hasSelectionEv(const QWebEnginePage *self) {
  return self->hasSelection();
}

//  QString QWebEnginePage::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWebEnginePage12selectedTextEv(
    const QWebEnginePage *self) {
  return new QString(self->selectedText());
}

//  QWebEngineProfile *QWebEnginePage::profile() const
extern "C" Q_DECL_EXPORT
QWebEngineProfile *ritual_ZNK14QWebEnginePage7profileEv(
    const QWebEnginePage *self) {
  return self->profile();
}

#if QT_CONFIG(action)
//  QAction *QWebEnginePage::action(WebAction action) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK14QWebEnginePage6actionENS_9WebActionE(
    const QWebEnginePage *self,
    QWebEnginePage::WebAction action) {
  return self->action(action);
}
#endif  // QT_CONFIG(action)

//  void QWebEnginePage::triggerAction(WebAction action, bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage13triggerActionENS_9WebActionEb(
    QWebEnginePage *self,
    QWebEnginePage::WebAction action,
    bool checked) {
  self->triggerAction(action, checked);
}

//  void QWebEnginePage::replaceMisspelledWord(const QString &replacement)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage21replaceMisspelledWordERK7QString(
    QWebEnginePage *self,
    const QString *replacement) {
  self->replaceMisspelledWord(*replacement);
}

//  bool QWebEnginePage::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWebEnginePage5eventEP6QEvent(
    QWebEnginePage *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QWebEnginePage::findText(const QString &subString, FindFlags
//      options, const std::function<void (const QWebEngineFindTextResult &)>
//      &resultCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage8findTextERK7QString6QFlagsINS_8FindFlagEERKSt8functionIFvRK24QWebEngineFindTextResultEE(
    QWebEnginePage *self,
    const QString *subString,
    int options,
    const std::function<void (const QWebEngineFindTextResult &)> *resultCallback) {
  self->findText(
      *subString,
      QFlags<QWebEnginePage::FindFlag>::fromInt(options),
      *resultCallback);
}

#if QT_DEPRECATED_SINCE(6, 8)
//  void QWebEnginePage::setFeaturePermission(const QUrl &securityOrigin,
//      Feature feature, PermissionPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage20setFeaturePermissionERK4QUrlNS_7FeatureENS_16PermissionPolicyE(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    QWebEnginePage::Feature feature,
    QWebEnginePage::PermissionPolicy policy) {
  self->setFeaturePermission(*securityOrigin, feature, policy);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  bool QWebEnginePage::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWebEnginePage9isLoadingEv(const QWebEnginePage *self) {
  return self->isLoading();
}

//  void QWebEnginePage::load(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage4loadERK4QUrl(
    QWebEnginePage *self,
    const QUrl *url) {
  self->load(*url);
}

//  void QWebEnginePage::load(const QWebEngineHttpRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage4loadERK21QWebEngineHttpRequest(
    QWebEnginePage *self,
    const QWebEngineHttpRequest *request) {
  self->load(*request);
}

//  void QWebEnginePage::download(const QUrl &url, const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage8downloadERK4QUrlRK7QString(
    QWebEnginePage *self,
    const QUrl *url,
    const QString *filename) {
  self->download(*url, *filename);
}

//  void QWebEnginePage::setHtml(const QString &html, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage7setHtmlERK7QStringRK4QUrl(
    QWebEnginePage *self,
    const QString *html,
    const QUrl *baseUrl) {
  self->setHtml(*html, *baseUrl);
}

//  void QWebEnginePage::setContent(const QByteArray &data, const QString
//      &mimeType, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage10setContentERK10QByteArrayRK7QStringRK4QUrl(
    QWebEnginePage *self,
    const QByteArray *data,
    const QString *mimeType,
    const QUrl *baseUrl) {
  self->setContent(*data, *mimeType, *baseUrl);
}

//  void QWebEnginePage::toHtml(const std::function<void (const QString &)>
//      &resultCallback) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWebEnginePage6toHtmlERKSt8functionIFvRK7QStringEE(
    const QWebEnginePage *self,
    const std::function<void (const QString &)> *resultCallback) {
  self->toHtml(*resultCallback);
}

//  void QWebEnginePage::toPlainText(const std::function<void (const QString
//      &)> &resultCallback) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWebEnginePage11toPlainTextERKSt8functionIFvRK7QStringEE(
    const QWebEnginePage *self,
    const std::function<void (const QString &)> *resultCallback) {
  self->toPlainText(*resultCallback);
}

//  QString QWebEnginePage::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWebEnginePage5titleEv(const QWebEnginePage *self) {
  return new QString(self->title());
}

//  void QWebEnginePage::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage6setUrlERK4QUrl(
    QWebEnginePage *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  QUrl QWebEnginePage::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QWebEnginePage3urlEv(const QWebEnginePage *self) {
  return new QUrl(self->url());
}

//  QUrl QWebEnginePage::requestedUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QWebEnginePage12requestedUrlEv(
    const QWebEnginePage *self) {
  return new QUrl(self->requestedUrl());
}

//  QUrl QWebEnginePage::iconUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QWebEnginePage7iconUrlEv(const QWebEnginePage *self) {
  return new QUrl(self->iconUrl());
}

//  QIcon QWebEnginePage::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK14QWebEnginePage4iconEv(const QWebEnginePage *self) {
  return new QIcon(self->icon());
}

//  qreal QWebEnginePage::zoomFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QWebEnginePage10zoomFactorEv(const QWebEnginePage *self) {
  return self->zoomFactor();
}

//  void QWebEnginePage::setZoomFactor(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage13setZoomFactorEd(
    QWebEnginePage *self,
    qreal factor) {
  self->setZoomFactor(factor);
}

//  QPointF QWebEnginePage::scrollPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14QWebEnginePage14scrollPositionEv(
    const QWebEnginePage *self) {
  return new QPointF(self->scrollPosition());
}

//  QSizeF QWebEnginePage::contentsSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK14QWebEnginePage12contentsSizeEv(
    const QWebEnginePage *self) {
  return new QSizeF(self->contentsSize());
}

//  void QWebEnginePage::runJavaScript(const QString &scriptSource, quint32
//      worldId)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage13runJavaScriptERK7QStringj(
    QWebEnginePage *self,
    const QString *scriptSource,
    quint32 worldId) {
  self->runJavaScript(*scriptSource, worldId);
}

//  QWebEngineScriptCollection &QWebEnginePage::scripts()
extern "C" Q_DECL_EXPORT
QWebEngineScriptCollection *ritual_ZN14QWebEnginePage7scriptsEv(
    QWebEnginePage *self) {
  return &(self->scripts());
}

//  QWebEngineSettings *QWebEnginePage::settings() const
extern "C" Q_DECL_EXPORT
QWebEngineSettings *ritual_ZNK14QWebEnginePage8settingsEv(
    const QWebEnginePage *self) {
  return self->settings();
}

//  QWebChannel *QWebEnginePage::webChannel() const
extern "C" Q_DECL_EXPORT
QWebChannel *ritual_ZNK14QWebEnginePage10webChannelEv(
    const QWebEnginePage *self) {
  return self->webChannel();
}

//  void QWebEnginePage::setWebChannel(QWebChannel *a0, quint32 worldId)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage13setWebChannelEP11QWebChannelj(
    QWebEnginePage *self,
    QWebChannel *a0,
    quint32 worldId) {
  self->setWebChannel(a0, worldId);
}

//  QColor QWebEnginePage::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QWebEnginePage15backgroundColorEv(
    const QWebEnginePage *self) {
  return new QColor(self->backgroundColor());
}

//  void QWebEnginePage::setBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage18setBackgroundColorERK6QColor(
    QWebEnginePage *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  void QWebEnginePage::save(const QString &filePath,
//      QWebEngineDownloadRequest::SavePageFormat format) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWebEnginePage4saveERK7QStringN25QWebEngineDownloadRequest14SavePageFormatE(
    const QWebEnginePage *self,
    const QString *filePath,
    QWebEngineDownloadRequest::SavePageFormat format) {
  self->save(*filePath, format);
}

//  bool QWebEnginePage::isAudioMuted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWebEnginePage12isAudioMutedEv(const QWebEnginePage *self) {
  return self->isAudioMuted();
}

//  void QWebEnginePage::setAudioMuted(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage13setAudioMutedEb(
    QWebEnginePage *self,
    bool muted) {
  self->setAudioMuted(muted);
}

//  bool QWebEnginePage::recentlyAudible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWebEnginePage15recentlyAudibleEv(
    const QWebEnginePage *self) {
  return self->recentlyAudible();
}

//  qint64 QWebEnginePage::renderProcessPid() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QWebEnginePage16renderProcessPidEv(
    const QWebEnginePage *self) {
  return self->renderProcessPid();
}

//  void QWebEnginePage::printToPdf(const QString &filePath, const
//      QPageLayout &layout, const QPageRanges &ranges)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage10printToPdfERK7QStringRK11QPageLayoutRK11QPageRanges(
    QWebEnginePage *self,
    const QString *filePath,
    const QPageLayout *layout,
    const QPageRanges *ranges) {
  self->printToPdf(*filePath, *layout, *ranges);
}

//  void QWebEnginePage::printToPdf(const std::function<void (const
//      QByteArray &)> &resultCallback, const QPageLayout &layout, const
//      QPageRanges &ranges)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage10printToPdfERKSt8functionIFvRK10QByteArrayEERK11QPageLayoutRK11QPageRanges(
    QWebEnginePage *self,
    const std::function<void (const QByteArray &)> *resultCallback,
    const QPageLayout *layout,
    const QPageRanges *ranges) {
  self->printToPdf(*resultCallback, *layout, *ranges);
}

//  void QWebEnginePage::setInspectedPage(QWebEnginePage *page)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage16setInspectedPageEPS_(
    QWebEnginePage *self,
    QWebEnginePage *page) {
  self->setInspectedPage(page);
}

//  QWebEnginePage *QWebEnginePage::inspectedPage() const
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_ZNK14QWebEnginePage13inspectedPageEv(
    const QWebEnginePage *self) {
  return self->inspectedPage();
}

//  void QWebEnginePage::setDevToolsPage(QWebEnginePage *page)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage15setDevToolsPageEPS_(
    QWebEnginePage *self,
    QWebEnginePage *page) {
  self->setDevToolsPage(page);
}

//  QWebEnginePage *QWebEnginePage::devToolsPage() const
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_ZNK14QWebEnginePage12devToolsPageEv(
    const QWebEnginePage *self) {
  return self->devToolsPage();
}

//  QString QWebEnginePage::devToolsId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWebEnginePage10devToolsIdEv(
    const QWebEnginePage *self) {
  return new QString(self->devToolsId());
}

//  void
//      QWebEnginePage::setUrlRequestInterceptor(QWebEngineUrlRequestIntercep
//      tor *interceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage24setUrlRequestInterceptorEP31QWebEngineUrlRequestInterceptor(
    QWebEnginePage *self,
    QWebEngineUrlRequestInterceptor *interceptor) {
  self->setUrlRequestInterceptor(interceptor);
}

//  LifecycleState QWebEnginePage::lifecycleState() const
extern "C" Q_DECL_EXPORT
QWebEnginePage::LifecycleState ritual_ZNK14QWebEnginePage14lifecycleStateEv(
    const QWebEnginePage *self) {
  return self->lifecycleState();
}

//  void QWebEnginePage::setLifecycleState(LifecycleState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage17setLifecycleStateENS_14LifecycleStateE(
    QWebEnginePage *self,
    QWebEnginePage::LifecycleState state) {
  self->setLifecycleState(state);
}

//  LifecycleState QWebEnginePage::recommendedState() const
extern "C" Q_DECL_EXPORT
QWebEnginePage::LifecycleState ritual_ZNK14QWebEnginePage16recommendedStateEv(
    const QWebEnginePage *self) {
  return self->recommendedState();
}

//  bool QWebEnginePage::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWebEnginePage9isVisibleEv(const QWebEnginePage *self) {
  return self->isVisible();
}

//  void QWebEnginePage::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage10setVisibleEb(
    QWebEnginePage *self,
    bool visible) {
  self->setVisible(visible);
}

//  QWebEngineFrame QWebEnginePage::mainFrame()
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_ZN14QWebEnginePage9mainFrameEv(
    QWebEnginePage *self) {
  return new QWebEngineFrame(self->mainFrame());
}

//  std::optional<QWebEngineFrame>
//      QWebEnginePage::findFrameByName(QAnyStringView name)
extern "C" Q_DECL_EXPORT
std::optional<QWebEngineFrame> *ritual_ZN14QWebEnginePage15findFrameByNameE14QAnyStringView(
    QWebEnginePage *self,
    const QString *name) {
  return new std::optional<QWebEngineFrame>(
      self->findFrameByName(
          QAnyStringView(*name)));
}

//  void QWebEnginePage::acceptAsNewWindow(QWebEngineNewWindowRequest
//      &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage17acceptAsNewWindowER26QWebEngineNewWindowRequest(
    QWebEnginePage *self,
    QWebEngineNewWindowRequest *request) {
  self->acceptAsNewWindow(*request);
}

//  void QWebEnginePage::loadStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage11loadStartedEv(QWebEnginePage *self) {
  self->loadStarted();
}

//  void QWebEnginePage::loadProgress(int progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage12loadProgressEi(
    QWebEnginePage *self,
    int progress) {
  self->loadProgress(progress);
}

//  void QWebEnginePage::loadFinished(bool ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage12loadFinishedEb(
    QWebEnginePage *self,
    bool ok) {
  self->loadFinished(ok);
}

//  void QWebEnginePage::loadingChanged(const QWebEngineLoadingInfo
//      &loadingInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage14loadingChangedERK21QWebEngineLoadingInfo(
    QWebEnginePage *self,
    const QWebEngineLoadingInfo *loadingInfo) {
  self->loadingChanged(*loadingInfo);
}

//  void QWebEnginePage::linkHovered(const QString &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage11linkHoveredERK7QString(
    QWebEnginePage *self,
    const QString *url) {
  self->linkHovered(*url);
}

//  void QWebEnginePage::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage16selectionChangedEv(QWebEnginePage *self) {
  self->selectionChanged();
}

//  void QWebEnginePage::geometryChangeRequested(const QRect &geom)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage23geometryChangeRequestedERK5QRect(
    QWebEnginePage *self,
    const QRect *geom) {
  self->geometryChangeRequested(*geom);
}

//  void QWebEnginePage::windowCloseRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage20windowCloseRequestedEv(
    QWebEnginePage *self) {
  self->windowCloseRequested();
}

#if QT_DEPRECATED_SINCE(6, 8)
//  void QWebEnginePage::featurePermissionRequested(const QUrl
//      &securityOrigin, QWebEnginePage::Feature feature)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage26featurePermissionRequestedERK4QUrlNS_7FeatureE(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    QWebEnginePage::Feature feature) {
  self->featurePermissionRequested(*securityOrigin, feature);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  void QWebEnginePage::featurePermissionRequestCanceled(const QUrl
//      &securityOrigin, QWebEnginePage::Feature feature)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage32featurePermissionRequestCanceledERK4QUrlNS_7FeatureE(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    QWebEnginePage::Feature feature) {
  self->featurePermissionRequestCanceled(*securityOrigin, feature);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  void QWebEnginePage::fullScreenRequested(QWebEngineFullScreenRequest
//      fullScreenRequest)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage19fullScreenRequestedE27QWebEngineFullScreenRequest(
    QWebEnginePage *self,
    const QWebEngineFullScreenRequest *fullScreenRequest) {
  self->fullScreenRequested(*fullScreenRequest);
}

//  void QWebEnginePage::permissionRequested(QWebEnginePermission
//      permissionRequest)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage19permissionRequestedE20QWebEnginePermission(
    QWebEnginePage *self,
    const QWebEnginePermission *permissionRequest) {
  self->permissionRequested(*permissionRequest);
}

#if QT_DEPRECATED_SINCE(6, 5)
//  void QWebEnginePage::quotaRequested(QWebEngineQuotaRequest quotaRequest)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage14quotaRequestedE22QWebEngineQuotaRequest(
    QWebEnginePage *self,
    const QWebEngineQuotaRequest *quotaRequest) {
  self->quotaRequested(*quotaRequest);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  void QWebEnginePage::registerProtocolHandlerRequested(QWebEngineRegisterP
//      rotocolHandlerRequest request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage32registerProtocolHandlerRequestedE40QWebEngineRegisterProtocolHandlerRequest(
    QWebEnginePage *self,
    const QWebEngineRegisterProtocolHandlerRequest *request) {
  self->registerProtocolHandlerRequested(*request);
}

//  void QWebEnginePage::fileSystemAccessRequested(QWebEngineFileSystemAccess
//      Request request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage25fileSystemAccessRequestedE33QWebEngineFileSystemAccessRequest(
    QWebEnginePage *self,
    const QWebEngineFileSystemAccessRequest *request) {
  self->fileSystemAccessRequested(*request);
}

//  void QWebEnginePage::selectClientCertificate(QWebEngineClientCertificateS
//      election clientCertSelection)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage23selectClientCertificateE36QWebEngineClientCertificateSelection(
    QWebEnginePage *self,
    const QWebEngineClientCertificateSelection *clientCertSelection) {
  self->selectClientCertificate(*clientCertSelection);
}

//  void QWebEnginePage::authenticationRequired(const QUrl &requestUrl,
//      QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage22authenticationRequiredERK4QUrlP14QAuthenticator(
    QWebEnginePage *self,
    const QUrl *requestUrl,
    QAuthenticator *authenticator) {
  self->authenticationRequired(*requestUrl, authenticator);
}

//  void QWebEnginePage::proxyAuthenticationRequired(const QUrl &requestUrl,
//      QAuthenticator *authenticator, const QString &proxyHost)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage27proxyAuthenticationRequiredERK4QUrlP14QAuthenticatorRK7QString(
    QWebEnginePage *self,
    const QUrl *requestUrl,
    QAuthenticator *authenticator,
    const QString *proxyHost) {
  self->proxyAuthenticationRequired(*requestUrl, authenticator, *proxyHost);
}

//  void
//      QWebEnginePage::renderProcessTerminated(RenderProcessTerminationStatu
//      s terminationStatus, int exitCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage23renderProcessTerminatedENS_30RenderProcessTerminationStatusEi(
    QWebEnginePage *self,
    QWebEnginePage::RenderProcessTerminationStatus terminationStatus,
    int exitCode) {
  self->renderProcessTerminated(terminationStatus, exitCode);
}

//  void QWebEnginePage::desktopMediaRequested(const
//      QWebEngineDesktopMediaRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage21desktopMediaRequestedERK29QWebEngineDesktopMediaRequest(
    QWebEnginePage *self,
    const QWebEngineDesktopMediaRequest *request) {
  self->desktopMediaRequested(*request);
}

//  void QWebEnginePage::certificateError(const QWebEngineCertificateError
//      &certificateError)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage16certificateErrorERK26QWebEngineCertificateError(
    QWebEnginePage *self,
    const QWebEngineCertificateError *certificateError) {
  self->certificateError(*certificateError);
}

//  void QWebEnginePage::navigationRequested(QWebEngineNavigationRequest
//      &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage19navigationRequestedER27QWebEngineNavigationRequest(
    QWebEnginePage *self,
    QWebEngineNavigationRequest *request) {
  self->navigationRequested(*request);
}

//  void QWebEnginePage::newWindowRequested(QWebEngineNewWindowRequest
//      &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage18newWindowRequestedER26QWebEngineNewWindowRequest(
    QWebEnginePage *self,
    QWebEngineNewWindowRequest *request) {
  self->newWindowRequested(*request);
}

//  void QWebEnginePage::titleChanged(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage12titleChangedERK7QString(
    QWebEnginePage *self,
    const QString *title) {
  self->titleChanged(*title);
}

//  void QWebEnginePage::urlChanged(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage10urlChangedERK4QUrl(
    QWebEnginePage *self,
    const QUrl *url) {
  self->urlChanged(*url);
}

//  void QWebEnginePage::iconUrlChanged(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage14iconUrlChangedERK4QUrl(
    QWebEnginePage *self,
    const QUrl *url) {
  self->iconUrlChanged(*url);
}

//  void QWebEnginePage::iconChanged(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage11iconChangedERK5QIcon(
    QWebEnginePage *self,
    const QIcon *icon) {
  self->iconChanged(*icon);
}

//  void QWebEnginePage::zoomFactorChanged(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage17zoomFactorChangedEd(
    QWebEnginePage *self,
    qreal factor) {
  self->zoomFactorChanged(factor);
}

//  void QWebEnginePage::scrollPositionChanged(const QPointF &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage21scrollPositionChangedERK7QPointF(
    QWebEnginePage *self,
    const QPointF *position) {
  self->scrollPositionChanged(*position);
}

//  void QWebEnginePage::contentsSizeChanged(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage19contentsSizeChangedERK6QSizeF(
    QWebEnginePage *self,
    const QSizeF *size) {
  self->contentsSizeChanged(*size);
}

//  void QWebEnginePage::audioMutedChanged(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage17audioMutedChangedEb(
    QWebEnginePage *self,
    bool muted) {
  self->audioMutedChanged(muted);
}

//  void QWebEnginePage::recentlyAudibleChanged(bool recentlyAudible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage22recentlyAudibleChangedEb(
    QWebEnginePage *self,
    bool recentlyAudible) {
  self->recentlyAudibleChanged(recentlyAudible);
}

//  void QWebEnginePage::renderProcessPidChanged(qint64 pid)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage23renderProcessPidChangedEx(
    QWebEnginePage *self,
    qint64 pid) {
  self->renderProcessPidChanged(pid);
}

//  void QWebEnginePage::pdfPrintingFinished(const QString &filePath, bool
//      success)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage19pdfPrintingFinishedERK7QStringb(
    QWebEnginePage *self,
    const QString *filePath,
    bool success) {
  self->pdfPrintingFinished(*filePath, success);
}

//  void QWebEnginePage::printRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage14printRequestedEv(QWebEnginePage *self) {
  self->printRequested();
}

//  void QWebEnginePage::printRequestedByFrame(QWebEngineFrame frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage21printRequestedByFrameE15QWebEngineFrame(
    QWebEnginePage *self,
    const QWebEngineFrame *frame) {
  self->printRequestedByFrame(*frame);
}

//  void QWebEnginePage::visibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage14visibleChangedEb(
    QWebEnginePage *self,
    bool visible) {
  self->visibleChanged(visible);
}

//  void QWebEnginePage::lifecycleStateChanged(LifecycleState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage21lifecycleStateChangedENS_14LifecycleStateE(
    QWebEnginePage *self,
    QWebEnginePage::LifecycleState state) {
  self->lifecycleStateChanged(state);
}

//  void QWebEnginePage::recommendedStateChanged(LifecycleState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage23recommendedStateChangedENS_14LifecycleStateE(
    QWebEnginePage *self,
    QWebEnginePage::LifecycleState state) {
  self->recommendedStateChanged(state);
}

//  void QWebEnginePage::findTextFinished(const QWebEngineFindTextResult
//      &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage16findTextFinishedERK24QWebEngineFindTextResult(
    QWebEnginePage *self,
    const QWebEngineFindTextResult *result) {
  self->findTextFinished(*result);
}

//  void QWebEnginePage::_q_aboutToDelete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage16_q_aboutToDeleteEv(QWebEnginePage *self) {
  self->_q_aboutToDelete();
}

//  void QWebEnginePage::webAuthUxRequested(QWebEngineWebAuthUxRequest
//      *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage18webAuthUxRequestedEP26QWebEngineWebAuthUxRequest(
    QWebEnginePage *self,
    QWebEngineWebAuthUxRequest *request) {
  self->webAuthUxRequested(request);
}

//  QWebEnginePage *QWebEnginePage::createWindow(WebWindowType type)
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_ZN14QWebEnginePage12createWindowENS_13WebWindowTypeE(
    QWebEnginePage *self,
    QWebEnginePage::WebWindowType type) {
  return self->createWindow(type);
}

//  QStringList QWebEnginePage::chooseFiles(FileSelectionMode mode, const
//      QStringList &oldFiles, const QStringList &acceptedMimeTypes)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN14QWebEnginePage11chooseFilesENS_17FileSelectionModeERK5QListI7QStringES5_(
    QWebEnginePage *self,
    QWebEnginePage::FileSelectionMode mode,
    const QList<QString> *oldFiles,
    const QList<QString> *acceptedMimeTypes) {
  return new QList<QString>(
      self->chooseFiles(
          mode,
          *oldFiles,
          *acceptedMimeTypes));
}

//  void QWebEnginePage::javaScriptAlert(const QUrl &securityOrigin, const
//      QString &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage15javaScriptAlertERK4QUrlRK7QString(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    const QString *msg) {
  self->javaScriptAlert(*securityOrigin, *msg);
}

//  bool QWebEnginePage::javaScriptConfirm(const QUrl &securityOrigin, const
//      QString &msg)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWebEnginePage17javaScriptConfirmERK4QUrlRK7QString(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    const QString *msg) {
  return self->javaScriptConfirm(*securityOrigin, *msg);
}

//  bool QWebEnginePage::javaScriptPrompt(const QUrl &securityOrigin, const
//      QString &msg, const QString &defaultValue, QString *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWebEnginePage16javaScriptPromptERK4QUrlRK7QStringS5_PS3_(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    const QString *msg,
    const QString *defaultValue,
    QString *result) {
  return self->javaScriptPrompt(
      *securityOrigin,
      *msg,
      *defaultValue,
      result);
}

//  void
//      QWebEnginePage::javaScriptConsoleMessage(JavaScriptConsoleMessageLeve
//      l level, const QString &message, int lineNumber, const QString
//      &sourceID)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage24javaScriptConsoleMessageENS_29JavaScriptConsoleMessageLevelERK7QStringiS3_(
    QWebEnginePage *self,
    QWebEnginePage::JavaScriptConsoleMessageLevel level,
    const QString *message,
    int lineNumber,
    const QString *sourceID) {
  self->javaScriptConsoleMessage(level, *message, lineNumber, *sourceID);
}

//  bool QWebEnginePage::acceptNavigationRequest(const QUrl &url,
//      NavigationType type, bool isMainFrame)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWebEnginePage23acceptNavigationRequestERK4QUrlNS_14NavigationTypeEb(
    QWebEnginePage *self,
    const QUrl *url,
    QWebEnginePage::NavigationType type,
    bool isMainFrame) {
  return self->acceptNavigationRequest(*url, type, isMainFrame);
}

//  QWebEnginePagePrivate *QWebEnginePage::d_func()
extern "C" Q_DECL_EXPORT
QWebEnginePagePrivate *ritual_ZN14QWebEnginePage6d_funcEv(
    QWebEnginePage *self) {
  return self->d_func();
}

//  const QWebEnginePagePrivate *QWebEnginePage::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEnginePagePrivate *ritual_ZNK14QWebEnginePage6d_funcEv(
    const QWebEnginePage *self) {
  return self->d_func();
}

//  void QWebEnginePage::runJavaScriptImpl(const QString &scriptSource,
//      quint32 worldId, QtPrivate::QSlotObjectBase *callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEnginePage17runJavaScriptImplERK7QStringjPN9QtPrivate15QSlotObjectBaseE(
    QWebEnginePage *self,
    const QString *scriptSource,
    quint32 worldId,
    QtPrivate::QSlotObjectBase *callback) {
  self->runJavaScriptImpl(*scriptSource, worldId, callback);
}

//  a Python function taken by a CuteQWebEnginePage, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEnginePage(
    QWebEnginePage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEnginePage *>(self)->take(key, call);
}

//  void QWebEnginePage::triggerAction(WebAction action, bool checked)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEnginePage13triggerActionENS_9WebActionEb(
    QWebEnginePage *self,
    QWebEnginePage::WebAction action,
    bool checked) {
  self->QWebEnginePage::triggerAction(action, checked);
}

//  bool QWebEnginePage::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWebEnginePage5eventEP6QEvent(
    QWebEnginePage *self,
    QEvent *a0) {
  return self->QWebEnginePage::event(a0);
}

//  QWebEnginePage *QWebEnginePage::createWindow(WebWindowType type)
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_own_ZN14QWebEnginePage12createWindowENS_13WebWindowTypeE(
    QWebEnginePage *self,
    QWebEnginePage::WebWindowType type) {
  return static_cast<OwnQWebEnginePage *>(self)->OwnQWebEnginePage::createWindow(
      type);
}

//  void QWebEnginePage::javaScriptAlert(const QUrl &securityOrigin, const
//      QString &msg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEnginePage15javaScriptAlertERK4QUrlRK7QString(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    const QString *msg) {
  static_cast<OwnQWebEnginePage *>(self)->OwnQWebEnginePage::javaScriptAlert(
      *securityOrigin,
      *msg);
}

//  bool QWebEnginePage::javaScriptConfirm(const QUrl &securityOrigin, const
//      QString &msg)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWebEnginePage17javaScriptConfirmERK4QUrlRK7QString(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    const QString *msg) {
  return static_cast<OwnQWebEnginePage *>(self)->OwnQWebEnginePage::javaScriptConfirm(
      *securityOrigin,
      *msg);
}

//  bool QWebEnginePage::javaScriptPrompt(const QUrl &securityOrigin, const
//      QString &msg, const QString &defaultValue, QString *result)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWebEnginePage16javaScriptPromptERK4QUrlRK7QStringS5_PS3_(
    QWebEnginePage *self,
    const QUrl *securityOrigin,
    const QString *msg,
    const QString *defaultValue,
    QString *result) {
  return static_cast<OwnQWebEnginePage *>(self)->OwnQWebEnginePage::javaScriptPrompt(
      *securityOrigin,
      *msg,
      *defaultValue,
      result);
}

//  void
//      QWebEnginePage::javaScriptConsoleMessage(JavaScriptConsoleMessageLeve
//      l level, const QString &message, int lineNumber, const QString
//      &sourceID)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEnginePage24javaScriptConsoleMessageENS_29JavaScriptConsoleMessageLevelERK7QStringiS3_(
    QWebEnginePage *self,
    QWebEnginePage::JavaScriptConsoleMessageLevel level,
    const QString *message,
    int lineNumber,
    const QString *sourceID) {
  static_cast<OwnQWebEnginePage *>(self)->OwnQWebEnginePage::javaScriptConsoleMessage(
      level,
      *message,
      lineNumber,
      *sourceID);
}

//  bool QWebEnginePage::acceptNavigationRequest(const QUrl &url,
//      NavigationType type, bool isMainFrame)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWebEnginePage23acceptNavigationRequestERK4QUrlNS_14NavigationTypeEb(
    QWebEnginePage *self,
    const QUrl *url,
    QWebEnginePage::NavigationType type,
    bool isMainFrame) {
  return static_cast<OwnQWebEnginePage *>(self)->OwnQWebEnginePage::acceptNavigationRequest(
      *url,
      type,
      isMainFrame);
}

//  a std::optional<QWebEngineFrame> a ritual of QWebEnginePage gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebEnginePage__std_optional_QWebEngineFrame(
    std::optional<QWebEngineFrame> *self) {
  delete self;
}
