//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebView/qwebview.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWebView/qwebview.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtWebView/qwebviewloadinginfo.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWebView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWebView : QWebView {
  using QWebView::event;
};

//  A QWebView that Python can take functions over in. Every QWebView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebViewCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQWebViewCall1)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQWebViewCall2)(const void *, int *);
typedef const QSize * (*CuteQWebViewCall3)(const void *, int *);
typedef void * (*CuteQWebViewCall4)(const void *, int *);
typedef void * (*CuteQWebViewCall5)(const void *, int *);
typedef void (*CuteQWebViewCall6)(const void *, QExposeEvent *, int *);
typedef void (*CuteQWebViewCall7)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWebViewCall8)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWebViewCall9)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWebViewCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWebViewCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWebViewCall12)(const void *, QShowEvent *, int *);
typedef void (*CuteQWebViewCall13)(const void *, QHideEvent *, int *);
typedef void (*CuteQWebViewCall14)(const void *, QCloseEvent *, int *);
typedef void (*CuteQWebViewCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWebViewCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWebViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWebViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWebViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWebViewCall20)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQWebViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWebViewCall22)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQWebViewCall23)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQWebViewCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebViewCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebView : public QWebView {
public:
  using QWebView::QWebView;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWebView::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebViewCall0 call = reinterpret_cast<CuteQWebViewCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWebView::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebViewCall1 call = reinterpret_cast<CuteQWebViewCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebViewCall2 call = reinterpret_cast<CuteQWebViewCall2>(taken[2]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebViewCall3 call = reinterpret_cast<CuteQWebViewCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebViewCall4 call = reinterpret_cast<CuteQWebViewCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebViewCall5 call = reinterpret_cast<CuteQWebViewCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebViewCall6 call = reinterpret_cast<CuteQWebViewCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::exposeEvent(a0);
  }

  //  void QWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWebViewCall7 call = reinterpret_cast<CuteQWebViewCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::resizeEvent(a0);
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWebViewCall8 call = reinterpret_cast<CuteQWebViewCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWebViewCall9 call = reinterpret_cast<CuteQWebViewCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWebViewCall10 call = reinterpret_cast<CuteQWebViewCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWebViewCall11 call = reinterpret_cast<CuteQWebViewCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWebViewCall12 call = reinterpret_cast<CuteQWebViewCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWebViewCall13 call = reinterpret_cast<CuteQWebViewCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWebViewCall14 call = reinterpret_cast<CuteQWebViewCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWebViewCall15 call = reinterpret_cast<CuteQWebViewCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWebViewCall16 call = reinterpret_cast<CuteQWebViewCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWebViewCall17 call = reinterpret_cast<CuteQWebViewCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWebViewCall18 call = reinterpret_cast<CuteQWebViewCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWebViewCall19 call = reinterpret_cast<CuteQWebViewCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWebViewCall20 call = reinterpret_cast<CuteQWebViewCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWebViewCall21 call = reinterpret_cast<CuteQWebViewCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWebViewCall22 call = reinterpret_cast<CuteQWebViewCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

#if QT_CONFIG(tabletevent)
  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWebViewCall23 call = reinterpret_cast<CuteQWebViewCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQWebViewCall24 call = reinterpret_cast<CuteQWebViewCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWebViewCall25 call = reinterpret_cast<CuteQWebViewCall25>(taken[25]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWebViewCall26 call = reinterpret_cast<CuteQWebViewCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWebViewCall27 call = reinterpret_cast<CuteQWebViewCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWebViewCall28 call = reinterpret_cast<CuteQWebViewCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWebViewCall29 call = reinterpret_cast<CuteQWebViewCall29>(taken[29]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWebViewCall30 call = reinterpret_cast<CuteQWebViewCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QWebView10metaObjectEv(const QWebView *self) {
  return self->metaObject();
}

//  void *QWebView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8QWebView11qt_metacastEPKc(QWebView *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QWebView11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QWebView2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QWebView::tr(s, c, n));
}

//  QWebView::QWebView(QScreen *screen)
extern "C" Q_DECL_EXPORT
QWebView *ritual_ZN8QWebViewC1EP7QScreen(QScreen *screen) {
  return new CuteQWebView(screen);
}

//  QWebView::QWebView(QWindow *parent)
extern "C" Q_DECL_EXPORT
QWebView *ritual_ZN8QWebViewC1EP7QWindow(QWindow *parent) {
  return new CuteQWebView(parent);
}

//  QWebView::~QWebView()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebViewD1Ev(QWebView *self) {
  delete self;
}

//  QString QWebView::httpUserAgentString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QWebView19httpUserAgentStringEv(const QWebView *self) {
  return new QString(self->httpUserAgentString());
}

//  QUrl QWebView::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QWebView3urlEv(const QWebView *self) {
  return new QUrl(self->url());
}

//  bool QWebView::canGoBack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QWebView9canGoBackEv(const QWebView *self) {
  return self->canGoBack();
}

//  bool QWebView::canGoForward() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QWebView12canGoForwardEv(const QWebView *self) {
  return self->canGoForward();
}

//  QString QWebView::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QWebView5titleEv(const QWebView *self) {
  return new QString(self->title());
}

//  int QWebView::loadProgress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QWebView12loadProgressEv(const QWebView *self) {
  return self->loadProgress();
}

//  bool QWebView::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QWebView9isLoadingEv(const QWebView *self) {
  return self->isLoading();
}

//  QWebViewSettings *QWebView::settings() const
extern "C" Q_DECL_EXPORT
QWebViewSettings *ritual_ZNK8QWebView8settingsEv(const QWebView *self) {
  return self->settings();
}

//  void QWebView::runJavaScript(const QString &script, const
//      std::function<void (const QVariant &)> &resultCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView13runJavaScriptERK7QStringRKSt8functionIFvRK8QVariantEE(
    QWebView *self,
    const QString *script,
    const std::function<void (const QVariant &)> *resultCallback) {
  self->runJavaScript(*script, *resultCallback);
}

//  void QWebView::setHttpUserAgentString(const QString &httpUserAgent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView22setHttpUserAgentStringERK7QString(
    QWebView *self,
    const QString *httpUserAgent) {
  self->setHttpUserAgentString(*httpUserAgent);
}

//  void QWebView::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView6setUrlERK4QUrl(QWebView *self, const QUrl *url) {
  self->setUrl(*url);
}

//  void QWebView::goBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView6goBackEv(QWebView *self) {
  self->goBack();
}

//  void QWebView::goForward()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView9goForwardEv(QWebView *self) {
  self->goForward();
}

//  void QWebView::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView6reloadEv(QWebView *self) {
  self->reload();
}

//  void QWebView::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView4stopEv(QWebView *self) {
  self->stop();
}

//  void QWebView::loadHtml(const QString &html, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView8loadHtmlERK7QStringRK4QUrl(
    QWebView *self,
    const QString *html,
    const QUrl *baseUrl) {
  self->loadHtml(*html, *baseUrl);
}

//  void QWebView::setCookie(const QString &domain, const QString &name,
//      const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView9setCookieERK7QStringS2_S2_(
    QWebView *self,
    const QString *domain,
    const QString *name,
    const QString *value) {
  self->setCookie(*domain, *name, *value);
}

//  void QWebView::deleteCookie(const QString &domain, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView12deleteCookieERK7QStringS2_(
    QWebView *self,
    const QString *domain,
    const QString *name) {
  self->deleteCookie(*domain, *name);
}

//  void QWebView::deleteAllCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView16deleteAllCookiesEv(QWebView *self) {
  self->deleteAllCookies();
}

//  void QWebView::titleChanged(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView12titleChangedERK7QString(
    QWebView *self,
    const QString *title) {
  self->titleChanged(*title);
}

//  void QWebView::urlChanged(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView10urlChangedERK4QUrl(
    QWebView *self,
    const QUrl *url) {
  self->urlChanged(*url);
}

//  void QWebView::loadingChanged(const QWebViewLoadingInfo &loadingInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView14loadingChangedERK19QWebViewLoadingInfo(
    QWebView *self,
    const QWebViewLoadingInfo *loadingInfo) {
  self->loadingChanged(*loadingInfo);
}

//  void QWebView::loadProgressChanged(int loadProgress)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView19loadProgressChangedEi(
    QWebView *self,
    int loadProgress) {
  self->loadProgressChanged(loadProgress);
}

//  void QWebView::httpUserAgentStringChanged(const QString &userAgent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView26httpUserAgentStringChangedERK7QString(
    QWebView *self,
    const QString *userAgent) {
  self->httpUserAgentStringChanged(*userAgent);
}

//  void QWebView::cookieAdded(const QString &domain, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView11cookieAddedERK7QStringS2_(
    QWebView *self,
    const QString *domain,
    const QString *name) {
  self->cookieAdded(*domain, *name);
}

//  void QWebView::cookieRemoved(const QString &domain, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QWebView13cookieRemovedERK7QStringS2_(
    QWebView *self,
    const QString *domain,
    const QString *name) {
  self->cookieRemoved(*domain, *name);
}

//  bool QWebView::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QWebView5eventEP6QEvent(QWebView *self, QEvent *a0) {
  return self->event(a0);
}

//  QWebView::QWebView(QWebViewFactory::Hint a0)
extern "C" Q_DECL_EXPORT
QWebView *ritual_ZN8QWebViewC1EN15QWebViewFactory4HintE(
    QWebViewFactory::Hint a0) {
  return new CuteQWebView(a0);
}

//  a Python function taken by a CuteQWebView, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebView(QWebView *self, const char *key, void *call) {
  return static_cast<CuteQWebView *>(self)->take(key, call);
}

//  bool QWebView::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QWebView5eventEP6QEvent(QWebView *self, QEvent *a0) {
  return static_cast<OwnQWebView *>(self)->OwnQWebView::event(a0);
}
