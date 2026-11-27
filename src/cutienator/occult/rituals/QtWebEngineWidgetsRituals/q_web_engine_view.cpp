//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineWidgets/qwebengineview.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWebEngineWidgets/qwebengineview.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtWebEngineCore/qwebenginehttprequest.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpageranges.h>
#include <QtWebEngineCore/qwebengineframe.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWebEngineView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWebEngineView : QWebEngineView {
  using QWebEngineView::createWindow;
  using QWebEngineView::contextMenuEvent;
  using QWebEngineView::event;
  using QWebEngineView::showEvent;
  using QWebEngineView::hideEvent;
  using QWebEngineView::closeEvent;
  using QWebEngineView::dragEnterEvent;
  using QWebEngineView::dragLeaveEvent;
  using QWebEngineView::dragMoveEvent;
  using QWebEngineView::dropEvent;
};

//  A QWebEngineView that Python can take functions over in. Every QWebEngineView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQWebEngineViewCall0)(const void *, int *);
typedef void * (*CuteQWebEngineViewCall1)(const void *, int, int *);
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(contextmenu)
typedef void (*CuteQWebEngineViewCall2)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(contextmenu)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineViewCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineViewCall4)(const void *, QShowEvent *, int *);
typedef void (*CuteQWebEngineViewCall5)(const void *, QHideEvent *, int *);
typedef void (*CuteQWebEngineViewCall6)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWebEngineViewCall7)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWebEngineViewCall8)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWebEngineViewCall9)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWebEngineViewCall10)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQWebEngineViewCall11)(const void *, int *);
typedef void (*CuteQWebEngineViewCall12)(const void *, bool, int *);
typedef const QSize * (*CuteQWebEngineViewCall13)(const void *, int *);
typedef int (*CuteQWebEngineViewCall14)(const void *, int, int *);
typedef bool (*CuteQWebEngineViewCall15)(const void *, int *);
typedef void * (*CuteQWebEngineViewCall16)(const void *, int *);
typedef void (*CuteQWebEngineViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWebEngineViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWebEngineViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWebEngineViewCall20)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQWebEngineViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWebEngineViewCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWebEngineViewCall23)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWebEngineViewCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWebEngineViewCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWebEngineViewCall26)(const void *, QEnterEvent *, int *);
typedef void (*CuteQWebEngineViewCall27)(const void *, QEvent *, int *);
typedef void (*CuteQWebEngineViewCall28)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWebEngineViewCall29)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWebEngineViewCall30)(const void *, QResizeEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQWebEngineViewCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQWebEngineViewCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQWebEngineViewCall33)(const void *, QEvent *, int *);
typedef int (*CuteQWebEngineViewCall34)(const void *, int, int *);
typedef void (*CuteQWebEngineViewCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQWebEngineViewCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQWebEngineViewCall37)(const void *, int *);
typedef void (*CuteQWebEngineViewCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQWebEngineViewCall39)(const void *, int, int *);
typedef bool (*CuteQWebEngineViewCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineViewCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineViewCall42)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineViewCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineViewCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineViewCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineViewCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineView : public QWebEngineView {
public:
  using QWebEngineView::QWebEngineView;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWebEngineView12createWindowEN14QWebEnginePage13WebWindowTypeE")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(contextmenu)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(contextmenu)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[40] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSize QWebEngineView::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEngineViewCall0 call = reinterpret_cast<CuteQWebEngineViewCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWebEngineView::sizeHint();
  }

  //  QWebEngineView
  //      *QWebEngineView::createWindow(QWebEnginePage::WebWindowType type)
  QWebEngineView *createWindow(QWebEnginePage::WebWindowType type) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEngineViewCall1 call = reinterpret_cast<CuteQWebEngineViewCall1>(taken[1]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<QWebEngineView *>(given);
    }
    return QWebEngineView::createWindow(type);
  }

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(contextmenu)
  //  void QWebEngineView::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebEngineViewCall2 call = reinterpret_cast<CuteQWebEngineViewCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWebEngineView::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(contextmenu)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if !defined(QT_NO_QOBJECT)
  //  bool QWebEngineView::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebEngineViewCall3 call = reinterpret_cast<CuteQWebEngineViewCall3>(taken[3]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWebEngineView::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWebEngineView::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebEngineViewCall4 call = reinterpret_cast<CuteQWebEngineViewCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWebEngineView::showEvent(a0);
  }

  //  void QWebEngineView::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebEngineViewCall5 call = reinterpret_cast<CuteQWebEngineViewCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWebEngineView::hideEvent(a0);
  }

  //  void QWebEngineView::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebEngineViewCall6 call = reinterpret_cast<CuteQWebEngineViewCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWebEngineView::closeEvent(a0);
  }

#if QT_CONFIG(draganddrop)
  //  void QWebEngineView::dragEnterEvent(QDragEnterEvent *e)
  void dragEnterEvent(QDragEnterEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWebEngineViewCall7 call = reinterpret_cast<CuteQWebEngineViewCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QWebEngineView::dragEnterEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWebEngineViewCall8 call = reinterpret_cast<CuteQWebEngineViewCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QWebEngineView::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWebEngineView::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWebEngineViewCall9 call = reinterpret_cast<CuteQWebEngineViewCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QWebEngineView::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWebEngineView::dropEvent(QDropEvent *e)
  void dropEvent(QDropEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWebEngineViewCall10 call = reinterpret_cast<CuteQWebEngineViewCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QWebEngineView::dropEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWebEngineViewCall11 call = reinterpret_cast<CuteQWebEngineViewCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWebEngineViewCall12 call = reinterpret_cast<CuteQWebEngineViewCall12>(taken[12]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQWebEngineViewCall13 call = reinterpret_cast<CuteQWebEngineViewCall13>(taken[13]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQWebEngineViewCall14 call = reinterpret_cast<CuteQWebEngineViewCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQWebEngineViewCall15 call = reinterpret_cast<CuteQWebEngineViewCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQWebEngineViewCall16 call = reinterpret_cast<CuteQWebEngineViewCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWebEngineViewCall17 call = reinterpret_cast<CuteQWebEngineViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWebEngineViewCall18 call = reinterpret_cast<CuteQWebEngineViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWebEngineViewCall19 call = reinterpret_cast<CuteQWebEngineViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWebEngineViewCall20 call = reinterpret_cast<CuteQWebEngineViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWebEngineViewCall21 call = reinterpret_cast<CuteQWebEngineViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWebEngineViewCall22 call = reinterpret_cast<CuteQWebEngineViewCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWebEngineViewCall23 call = reinterpret_cast<CuteQWebEngineViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWebEngineViewCall24 call = reinterpret_cast<CuteQWebEngineViewCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWebEngineViewCall25 call = reinterpret_cast<CuteQWebEngineViewCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWebEngineViewCall26 call = reinterpret_cast<CuteQWebEngineViewCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWebEngineViewCall27 call = reinterpret_cast<CuteQWebEngineViewCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWebEngineViewCall28 call = reinterpret_cast<CuteQWebEngineViewCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWebEngineViewCall29 call = reinterpret_cast<CuteQWebEngineViewCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWebEngineViewCall30 call = reinterpret_cast<CuteQWebEngineViewCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWebEngineViewCall31 call = reinterpret_cast<CuteQWebEngineViewCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWebEngineViewCall32 call = reinterpret_cast<CuteQWebEngineViewCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQWebEngineViewCall33 call = reinterpret_cast<CuteQWebEngineViewCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQWebEngineViewCall34 call = reinterpret_cast<CuteQWebEngineViewCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQWebEngineViewCall35 call = reinterpret_cast<CuteQWebEngineViewCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQWebEngineViewCall36 call = reinterpret_cast<CuteQWebEngineViewCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQWebEngineViewCall37 call = reinterpret_cast<CuteQWebEngineViewCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQWebEngineViewCall38 call = reinterpret_cast<CuteQWebEngineViewCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQWebEngineViewCall39 call = reinterpret_cast<CuteQWebEngineViewCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQWebEngineViewCall40 call = reinterpret_cast<CuteQWebEngineViewCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQWebEngineViewCall41 call = reinterpret_cast<CuteQWebEngineViewCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQWebEngineViewCall42 call = reinterpret_cast<CuteQWebEngineViewCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQWebEngineViewCall43 call = reinterpret_cast<CuteQWebEngineViewCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQWebEngineViewCall44 call = reinterpret_cast<CuteQWebEngineViewCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQWebEngineViewCall45 call = reinterpret_cast<CuteQWebEngineViewCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQWebEngineViewCall46 call = reinterpret_cast<CuteQWebEngineViewCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWebEngineView10metaObjectEv(
    const QWebEngineView *self) {
  return self->metaObject();
}

//  void *QWebEngineView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QWebEngineView11qt_metacastEPKc(
    QWebEngineView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QWebEngineView11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWebEngineView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineView::tr(s, c, n));
}

//  QWebEngineView::QWebEngineView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWebEngineView *ritual_ZN14QWebEngineViewC1EP7QWidget(QWidget *parent) {
  return new CuteQWebEngineView(parent);
}

//  QWebEngineView::QWebEngineView(QWebEngineProfile *profile, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QWebEngineView *ritual_ZN14QWebEngineViewC1EP17QWebEngineProfileP7QWidget(
    QWebEngineProfile *profile,
    QWidget *parent) {
  return new CuteQWebEngineView(profile, parent);
}

//  QWebEngineView::QWebEngineView(QWebEnginePage *page, QWidget *parent)
extern "C" Q_DECL_EXPORT
QWebEngineView *ritual_ZN14QWebEngineViewC1EP14QWebEnginePageP7QWidget(
    QWebEnginePage *page,
    QWidget *parent) {
  return new CuteQWebEngineView(page, parent);
}

//  QWebEngineView::~QWebEngineView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineViewD1Ev(QWebEngineView *self) {
  delete self;
}

//  QWebEngineView *QWebEngineView::forPage(const QWebEnginePage *page)
extern "C" Q_DECL_EXPORT
QWebEngineView *ritual_ZN14QWebEngineView7forPageEPK14QWebEnginePage(
    const QWebEnginePage *page) {
  return QWebEngineView::forPage(page);
}

//  QWebEnginePage *QWebEngineView::page() const
extern "C" Q_DECL_EXPORT
QWebEnginePage *ritual_ZNK14QWebEngineView4pageEv(
    const QWebEngineView *self) {
  return self->page();
}

//  void QWebEngineView::setPage(QWebEnginePage *page)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView7setPageEP14QWebEnginePage(
    QWebEngineView *self,
    QWebEnginePage *page) {
  self->setPage(page);
}

//  void QWebEngineView::load(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView4loadERK4QUrl(
    QWebEngineView *self,
    const QUrl *url) {
  self->load(*url);
}

//  void QWebEngineView::load(const QWebEngineHttpRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView4loadERK21QWebEngineHttpRequest(
    QWebEngineView *self,
    const QWebEngineHttpRequest *request) {
  self->load(*request);
}

//  void QWebEngineView::setHtml(const QString &html, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView7setHtmlERK7QStringRK4QUrl(
    QWebEngineView *self,
    const QString *html,
    const QUrl *baseUrl) {
  self->setHtml(*html, *baseUrl);
}

//  void QWebEngineView::setContent(const QByteArray &data, const QString
//      &mimeType, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView10setContentERK10QByteArrayRK7QStringRK4QUrl(
    QWebEngineView *self,
    const QByteArray *data,
    const QString *mimeType,
    const QUrl *baseUrl) {
  self->setContent(*data, *mimeType, *baseUrl);
}

//  QWebEngineHistory *QWebEngineView::history() const
extern "C" Q_DECL_EXPORT
QWebEngineHistory *ritual_ZNK14QWebEngineView7historyEv(
    const QWebEngineView *self) {
  return self->history();
}

//  QString QWebEngineView::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWebEngineView5titleEv(const QWebEngineView *self) {
  return new QString(self->title());
}

//  void QWebEngineView::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView6setUrlERK4QUrl(
    QWebEngineView *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  QUrl QWebEngineView::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QWebEngineView3urlEv(const QWebEngineView *self) {
  return new QUrl(self->url());
}

//  QUrl QWebEngineView::iconUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QWebEngineView7iconUrlEv(const QWebEngineView *self) {
  return new QUrl(self->iconUrl());
}

//  QIcon QWebEngineView::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK14QWebEngineView4iconEv(const QWebEngineView *self) {
  return new QIcon(self->icon());
}

//  bool QWebEngineView::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWebEngineView12hasSelectionEv(const QWebEngineView *self) {
  return self->hasSelection();
}

//  QString QWebEngineView::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWebEngineView12selectedTextEv(
    const QWebEngineView *self) {
  return new QString(self->selectedText());
}

#if QT_CONFIG(action)
//  QAction *QWebEngineView::pageAction(QWebEnginePage::WebAction action)
//      const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK14QWebEngineView10pageActionEN14QWebEnginePage9WebActionE(
    const QWebEngineView *self,
    QWebEnginePage::WebAction action) {
  return self->pageAction(action);
}
#endif  // QT_CONFIG(action)

//  void QWebEngineView::triggerPageAction(QWebEnginePage::WebAction action,
//      bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView17triggerPageActionEN14QWebEnginePage9WebActionEb(
    QWebEngineView *self,
    QWebEnginePage::WebAction action,
    bool checked) {
  self->triggerPageAction(action, checked);
}

//  qreal QWebEngineView::zoomFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QWebEngineView10zoomFactorEv(const QWebEngineView *self) {
  return self->zoomFactor();
}

//  void QWebEngineView::setZoomFactor(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView13setZoomFactorEd(
    QWebEngineView *self,
    qreal factor) {
  self->setZoomFactor(factor);
}

//  void QWebEngineView::findText(const QString &subString,
//      QWebEnginePage::FindFlags options, const std::function<void (const
//      QWebEngineFindTextResult &)> &resultCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView8findTextERK7QString6QFlagsIN14QWebEnginePage8FindFlagEERKSt8functionIFvRK24QWebEngineFindTextResultEE(
    QWebEngineView *self,
    const QString *subString,
    int options,
    const std::function<void (const QWebEngineFindTextResult &)> *resultCallback) {
  self->findText(
      *subString,
      QFlags<QWebEnginePage::FindFlag>::fromInt(options),
      *resultCallback);
}

//  QSize QWebEngineView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QWebEngineView8sizeHintEv(const QWebEngineView *self) {
  return new QSize(self->sizeHint());
}

//  QWebEngineSettings *QWebEngineView::settings() const
extern "C" Q_DECL_EXPORT
QWebEngineSettings *ritual_ZNK14QWebEngineView8settingsEv(
    const QWebEngineView *self) {
  return self->settings();
}

#if QT_CONFIG(menu)
//  QMenu *QWebEngineView::createStandardContextMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN14QWebEngineView25createStandardContextMenuEv(
    QWebEngineView *self) {
  return self->createStandardContextMenu();
}
#endif  // QT_CONFIG(menu)

//  QWebEngineContextMenuRequest *QWebEngineView::lastContextMenuRequest()
//      const
extern "C" Q_DECL_EXPORT
QWebEngineContextMenuRequest *ritual_ZNK14QWebEngineView22lastContextMenuRequestEv(
    const QWebEngineView *self) {
  return self->lastContextMenuRequest();
}

//  void QWebEngineView::printToPdf(const QString &filePath, const
//      QPageLayout &layout, const QPageRanges &ranges)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView10printToPdfERK7QStringRK11QPageLayoutRK11QPageRanges(
    QWebEngineView *self,
    const QString *filePath,
    const QPageLayout *layout,
    const QPageRanges *ranges) {
  self->printToPdf(*filePath, *layout, *ranges);
}

//  void QWebEngineView::printToPdf(const std::function<void (const
//      QByteArray &)> &resultCallback, const QPageLayout &layout, const
//      QPageRanges &ranges)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView10printToPdfERKSt8functionIFvRK10QByteArrayEERK11QPageLayoutRK11QPageRanges(
    QWebEngineView *self,
    const std::function<void (const QByteArray &)> *resultCallback,
    const QPageLayout *layout,
    const QPageRanges *ranges) {
  self->printToPdf(*resultCallback, *layout, *ranges);
}

//  void QWebEngineView::print(QPrinter *printer)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView5printEP8QPrinter(
    QWebEngineView *self,
    QPrinter *printer) {
  self->print(printer);
}

//  void QWebEngineView::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView4stopEv(QWebEngineView *self) {
  self->stop();
}

//  void QWebEngineView::back()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView4backEv(QWebEngineView *self) {
  self->back();
}

//  void QWebEngineView::forward()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView7forwardEv(QWebEngineView *self) {
  self->forward();
}

//  void QWebEngineView::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView6reloadEv(QWebEngineView *self) {
  self->reload();
}

//  void QWebEngineView::loadStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView11loadStartedEv(QWebEngineView *self) {
  self->loadStarted();
}

//  void QWebEngineView::loadProgress(int progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView12loadProgressEi(
    QWebEngineView *self,
    int progress) {
  self->loadProgress(progress);
}

//  void QWebEngineView::loadFinished(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView12loadFinishedEb(
    QWebEngineView *self,
    bool a0) {
  self->loadFinished(a0);
}

//  void QWebEngineView::titleChanged(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView12titleChangedERK7QString(
    QWebEngineView *self,
    const QString *title) {
  self->titleChanged(*title);
}

//  void QWebEngineView::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView16selectionChangedEv(QWebEngineView *self) {
  self->selectionChanged();
}

//  void QWebEngineView::urlChanged(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView10urlChangedERK4QUrl(
    QWebEngineView *self,
    const QUrl *a0) {
  self->urlChanged(*a0);
}

//  void QWebEngineView::iconUrlChanged(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView14iconUrlChangedERK4QUrl(
    QWebEngineView *self,
    const QUrl *a0) {
  self->iconUrlChanged(*a0);
}

//  void QWebEngineView::iconChanged(const QIcon &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView11iconChangedERK5QIcon(
    QWebEngineView *self,
    const QIcon *a0) {
  self->iconChanged(*a0);
}

//  void QWebEngineView::renderProcessTerminated(QWebEnginePage::RenderProces
//      sTerminationStatus terminationStatus, int exitCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView23renderProcessTerminatedEN14QWebEnginePage30RenderProcessTerminationStatusEi(
    QWebEngineView *self,
    QWebEnginePage::RenderProcessTerminationStatus terminationStatus,
    int exitCode) {
  self->renderProcessTerminated(terminationStatus, exitCode);
}

//  void QWebEngineView::pdfPrintingFinished(const QString &filePath, bool
//      success)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView19pdfPrintingFinishedERK7QStringb(
    QWebEngineView *self,
    const QString *filePath,
    bool success) {
  self->pdfPrintingFinished(*filePath, success);
}

//  void QWebEngineView::printRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView14printRequestedEv(QWebEngineView *self) {
  self->printRequested();
}

//  void QWebEngineView::printRequestedByFrame(QWebEngineFrame frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView21printRequestedByFrameE15QWebEngineFrame(
    QWebEngineView *self,
    const QWebEngineFrame *frame) {
  self->printRequestedByFrame(*frame);
}

//  void QWebEngineView::printFinished(bool success)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView13printFinishedEb(
    QWebEngineView *self,
    bool success) {
  self->printFinished(success);
}

//  QWebEngineView
//      *QWebEngineView::createWindow(QWebEnginePage::WebWindowType type)
extern "C" Q_DECL_EXPORT
QWebEngineView *ritual_ZN14QWebEngineView12createWindowEN14QWebEnginePage13WebWindowTypeE(
    QWebEngineView *self,
    QWebEnginePage::WebWindowType type) {
  return self->createWindow(type);
}

#if QT_CONFIG(contextmenu)
//  void QWebEngineView::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView16contextMenuEventEP17QContextMenuEvent(
    QWebEngineView *self,
    QContextMenuEvent *a0) {
  self->contextMenuEvent(a0);
}
#endif  // QT_CONFIG(contextmenu)

//  bool QWebEngineView::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWebEngineView5eventEP6QEvent(
    QWebEngineView *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QWebEngineView::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView9showEventEP10QShowEvent(
    QWebEngineView *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QWebEngineView::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView9hideEventEP10QHideEvent(
    QWebEngineView *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QWebEngineView::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView10closeEventEP11QCloseEvent(
    QWebEngineView *self,
    QCloseEvent *a0) {
  self->closeEvent(a0);
}

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView14dragEnterEventEP15QDragEnterEvent(
    QWebEngineView *self,
    QDragEnterEvent *e) {
  self->dragEnterEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView14dragLeaveEventEP15QDragLeaveEvent(
    QWebEngineView *self,
    QDragLeaveEvent *e) {
  self->dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView13dragMoveEventEP14QDragMoveEvent(
    QWebEngineView *self,
    QDragMoveEvent *e) {
  self->dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebEngineView9dropEventEP10QDropEvent(
    QWebEngineView *self,
    QDropEvent *e) {
  self->dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

//  QWebEngineViewPrivate *QWebEngineView::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineViewPrivate *ritual_ZN14QWebEngineView6d_funcEv(
    QWebEngineView *self) {
  return self->d_func();
}

//  const QWebEngineViewPrivate *QWebEngineView::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineViewPrivate *ritual_ZNK14QWebEngineView6d_funcEv(
    const QWebEngineView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQWebEngineView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineView(
    QWebEngineView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineView *>(self)->take(key, call);
}

//  QSize QWebEngineView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK14QWebEngineView8sizeHintEv(
    const QWebEngineView *self) {
  return new QSize(self->QWebEngineView::sizeHint());
}

//  QWebEngineView
//      *QWebEngineView::createWindow(QWebEnginePage::WebWindowType type)
extern "C" Q_DECL_EXPORT
QWebEngineView *ritual_own_ZN14QWebEngineView12createWindowEN14QWebEnginePage13WebWindowTypeE(
    QWebEngineView *self,
    QWebEnginePage::WebWindowType type) {
  return static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::createWindow(
      type);
}

#if QT_CONFIG(contextmenu)
//  void QWebEngineView::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView16contextMenuEventEP17QContextMenuEvent(
    QWebEngineView *self,
    QContextMenuEvent *a0) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::contextMenuEvent(
      a0);
}
#endif  // QT_CONFIG(contextmenu)

//  bool QWebEngineView::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWebEngineView5eventEP6QEvent(
    QWebEngineView *self,
    QEvent *a0) {
  return static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::event(
      a0);
}

//  void QWebEngineView::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView9showEventEP10QShowEvent(
    QWebEngineView *self,
    QShowEvent *a0) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::showEvent(a0);
}

//  void QWebEngineView::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView9hideEventEP10QHideEvent(
    QWebEngineView *self,
    QHideEvent *a0) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::hideEvent(a0);
}

//  void QWebEngineView::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView10closeEventEP11QCloseEvent(
    QWebEngineView *self,
    QCloseEvent *a0) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::closeEvent(a0);
}

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView14dragEnterEventEP15QDragEnterEvent(
    QWebEngineView *self,
    QDragEnterEvent *e) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::dragEnterEvent(
      e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView14dragLeaveEventEP15QDragLeaveEvent(
    QWebEngineView *self,
    QDragLeaveEvent *e) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::dragLeaveEvent(
      e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView13dragMoveEventEP14QDragMoveEvent(
    QWebEngineView *self,
    QDragMoveEvent *e) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::dragMoveEvent(
      e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWebEngineView::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWebEngineView9dropEventEP10QDropEvent(
    QWebEngineView *self,
    QDropEvent *e) {
  static_cast<OwnQWebEngineView *>(self)->OwnQWebEngineView::dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)
