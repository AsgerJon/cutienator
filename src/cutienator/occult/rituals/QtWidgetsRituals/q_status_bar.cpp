//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstatusbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(statusbar)
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QStatusBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStatusBar : QStatusBar {
  using QStatusBar::showEvent;
  using QStatusBar::paintEvent;
  using QStatusBar::resizeEvent;
  using QStatusBar::event;
};

//  A QStatusBar that Python can take functions over in. Every QStatusBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(statusbar)
typedef void (*CuteQStatusBarCall0)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(statusbar)
#if QT_CONFIG(statusbar)
typedef void (*CuteQStatusBarCall1)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(statusbar)
#if QT_CONFIG(statusbar)
typedef void (*CuteQStatusBarCall2)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(statusbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(statusbar)
typedef bool (*CuteQStatusBarCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(statusbar)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQStatusBarCall4)(const void *, int *);
typedef void (*CuteQStatusBarCall5)(const void *, bool, int *);
typedef const QSize * (*CuteQStatusBarCall6)(const void *, int *);
typedef const QSize * (*CuteQStatusBarCall7)(const void *, int *);
typedef int (*CuteQStatusBarCall8)(const void *, int, int *);
typedef bool (*CuteQStatusBarCall9)(const void *, int *);
typedef void * (*CuteQStatusBarCall10)(const void *, int *);
typedef void (*CuteQStatusBarCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQStatusBarCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQStatusBarCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQStatusBarCall14)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQStatusBarCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQStatusBarCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQStatusBarCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQStatusBarCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQStatusBarCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQStatusBarCall20)(const void *, QEnterEvent *, int *);
typedef void (*CuteQStatusBarCall21)(const void *, QEvent *, int *);
typedef void (*CuteQStatusBarCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQStatusBarCall23)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQStatusBarCall24)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQStatusBarCall25)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQStatusBarCall26)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQStatusBarCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQStatusBarCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQStatusBarCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQStatusBarCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQStatusBarCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQStatusBarCall32)(const void *, QEvent *, int *);
typedef int (*CuteQStatusBarCall33)(const void *, int, int *);
typedef void (*CuteQStatusBarCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQStatusBarCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQStatusBarCall36)(const void *, int *);
typedef void (*CuteQStatusBarCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQStatusBarCall38)(const void *, int, int *);
typedef bool (*CuteQStatusBarCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStatusBarCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusBarCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusBarCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusBarCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusBarCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusBarCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStatusBar : public QStatusBar {
public:
  using QStatusBar::QStatusBar;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(statusbar)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(statusbar)
#if QT_CONFIG(statusbar)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(statusbar)
#if QT_CONFIG(statusbar)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(statusbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(statusbar)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(statusbar)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[23] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[39] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(statusbar)
  //  void QStatusBar::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStatusBarCall0 call = reinterpret_cast<CuteQStatusBarCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QStatusBar::showEvent(a0);
  }
#endif  // QT_CONFIG(statusbar)

#if QT_CONFIG(statusbar)
  //  void QStatusBar::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStatusBarCall1 call = reinterpret_cast<CuteQStatusBarCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QStatusBar::paintEvent(a0);
  }
#endif  // QT_CONFIG(statusbar)

#if QT_CONFIG(statusbar)
  //  void QStatusBar::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStatusBarCall2 call = reinterpret_cast<CuteQStatusBarCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QStatusBar::resizeEvent(a0);
  }
#endif  // QT_CONFIG(statusbar)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(statusbar)
  //  bool QStatusBar::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStatusBarCall3 call = reinterpret_cast<CuteQStatusBarCall3>(taken[3]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QStatusBar::event(a0);
  }
#endif  // QT_CONFIG(statusbar)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStatusBarCall4 call = reinterpret_cast<CuteQStatusBarCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStatusBarCall5 call = reinterpret_cast<CuteQStatusBarCall5>(taken[5]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQStatusBarCall6 call = reinterpret_cast<CuteQStatusBarCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQStatusBarCall7 call = reinterpret_cast<CuteQStatusBarCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQStatusBarCall8 call = reinterpret_cast<CuteQStatusBarCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQStatusBarCall9 call = reinterpret_cast<CuteQStatusBarCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQStatusBarCall10 call = reinterpret_cast<CuteQStatusBarCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStatusBarCall11 call = reinterpret_cast<CuteQStatusBarCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQStatusBarCall12 call = reinterpret_cast<CuteQStatusBarCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQStatusBarCall13 call = reinterpret_cast<CuteQStatusBarCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQStatusBarCall14 call = reinterpret_cast<CuteQStatusBarCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQStatusBarCall15 call = reinterpret_cast<CuteQStatusBarCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQStatusBarCall16 call = reinterpret_cast<CuteQStatusBarCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQStatusBarCall17 call = reinterpret_cast<CuteQStatusBarCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQStatusBarCall18 call = reinterpret_cast<CuteQStatusBarCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQStatusBarCall19 call = reinterpret_cast<CuteQStatusBarCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQStatusBarCall20 call = reinterpret_cast<CuteQStatusBarCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQStatusBarCall21 call = reinterpret_cast<CuteQStatusBarCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQStatusBarCall22 call = reinterpret_cast<CuteQStatusBarCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQStatusBarCall23 call = reinterpret_cast<CuteQStatusBarCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQStatusBarCall24 call = reinterpret_cast<CuteQStatusBarCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQStatusBarCall25 call = reinterpret_cast<CuteQStatusBarCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQStatusBarCall26 call = reinterpret_cast<CuteQStatusBarCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQStatusBarCall27 call = reinterpret_cast<CuteQStatusBarCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQStatusBarCall28 call = reinterpret_cast<CuteQStatusBarCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQStatusBarCall29 call = reinterpret_cast<CuteQStatusBarCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQStatusBarCall30 call = reinterpret_cast<CuteQStatusBarCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQStatusBarCall31 call = reinterpret_cast<CuteQStatusBarCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQStatusBarCall32 call = reinterpret_cast<CuteQStatusBarCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQStatusBarCall33 call = reinterpret_cast<CuteQStatusBarCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQStatusBarCall34 call = reinterpret_cast<CuteQStatusBarCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQStatusBarCall35 call = reinterpret_cast<CuteQStatusBarCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQStatusBarCall36 call = reinterpret_cast<CuteQStatusBarCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQStatusBarCall37 call = reinterpret_cast<CuteQStatusBarCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQStatusBarCall38 call = reinterpret_cast<CuteQStatusBarCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQStatusBarCall39 call = reinterpret_cast<CuteQStatusBarCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQStatusBarCall40 call = reinterpret_cast<CuteQStatusBarCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQStatusBarCall41 call = reinterpret_cast<CuteQStatusBarCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQStatusBarCall42 call = reinterpret_cast<CuteQStatusBarCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQStatusBarCall43 call = reinterpret_cast<CuteQStatusBarCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQStatusBarCall44 call = reinterpret_cast<CuteQStatusBarCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQStatusBarCall45 call = reinterpret_cast<CuteQStatusBarCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStatusBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QStatusBar10metaObjectEv(
    const QStatusBar *self) {
  return self->metaObject();
}

//  QString QStatusBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QStatusBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStatusBar::tr(s, c, n));
}

//  QStatusBar::QStatusBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QStatusBar *ritual_ZN10QStatusBarC1EP7QWidget(QWidget *parent) {
  return new CuteQStatusBar(parent);
}

//  QStatusBar::~QStatusBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBarD1Ev(QStatusBar *self) {
  delete self;
}

//  void QStatusBar::addWidget(QWidget *widget, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar9addWidgetEP7QWidgeti(
    QStatusBar *self,
    QWidget *widget,
    int stretch) {
  self->addWidget(widget, stretch);
}

//  int QStatusBar::insertWidget(int index, QWidget *widget, int stretch)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStatusBar12insertWidgetEiP7QWidgeti(
    QStatusBar *self,
    int index,
    QWidget *widget,
    int stretch) {
  return self->insertWidget(index, widget, stretch);
}

//  void QStatusBar::addPermanentWidget(QWidget *widget, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar18addPermanentWidgetEP7QWidgeti(
    QStatusBar *self,
    QWidget *widget,
    int stretch) {
  self->addPermanentWidget(widget, stretch);
}

//  int QStatusBar::insertPermanentWidget(int index, QWidget *widget, int
//      stretch)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStatusBar21insertPermanentWidgetEiP7QWidgeti(
    QStatusBar *self,
    int index,
    QWidget *widget,
    int stretch) {
  return self->insertPermanentWidget(index, widget, stretch);
}

//  void QStatusBar::removeWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar12removeWidgetEP7QWidget(
    QStatusBar *self,
    QWidget *widget) {
  self->removeWidget(widget);
}

//  void QStatusBar::setSizeGripEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar18setSizeGripEnabledEb(QStatusBar *self, bool a0) {
  self->setSizeGripEnabled(a0);
}

//  bool QStatusBar::isSizeGripEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStatusBar17isSizeGripEnabledEv(const QStatusBar *self) {
  return self->isSizeGripEnabled();
}

//  QString QStatusBar::currentMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QStatusBar14currentMessageEv(const QStatusBar *self) {
  return new QString(self->currentMessage());
}

//  void QStatusBar::showMessage(const QString &text, int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar11showMessageERK7QStringi(
    QStatusBar *self,
    const QString *text,
    int timeout) {
  self->showMessage(*text, timeout);
}

//  void QStatusBar::clearMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar12clearMessageEv(QStatusBar *self) {
  self->clearMessage();
}

//  void QStatusBar::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar9showEventEP10QShowEvent(
    QStatusBar *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QStatusBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar10paintEventEP11QPaintEvent(
    QStatusBar *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QStatusBar::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar11resizeEventEP12QResizeEvent(
    QStatusBar *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QStatusBar::reformat()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar8reformatEv(QStatusBar *self) {
  self->reformat();
}

//  void QStatusBar::hideOrShow()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar10hideOrShowEv(QStatusBar *self) {
  self->hideOrShow();
}

//  bool QStatusBar::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QStatusBar5eventEP6QEvent(QStatusBar *self, QEvent *a0) {
  return self->event(a0);
}

//  a Python function taken by a CuteQStatusBar, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStatusBar(QStatusBar *self, const char *key, void *call) {
  return static_cast<CuteQStatusBar *>(self)->take(key, call);
}

//  void QStatusBar::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QStatusBar9showEventEP10QShowEvent(
    QStatusBar *self,
    QShowEvent *a0) {
  static_cast<OwnQStatusBar *>(self)->OwnQStatusBar::showEvent(a0);
}

//  void QStatusBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QStatusBar10paintEventEP11QPaintEvent(
    QStatusBar *self,
    QPaintEvent *a0) {
  static_cast<OwnQStatusBar *>(self)->OwnQStatusBar::paintEvent(a0);
}

//  void QStatusBar::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QStatusBar11resizeEventEP12QResizeEvent(
    QStatusBar *self,
    QResizeEvent *a0) {
  static_cast<OwnQStatusBar *>(self)->OwnQStatusBar::resizeEvent(a0);
}

//  bool QStatusBar::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QStatusBar5eventEP6QEvent(QStatusBar *self, QEvent *a0) {
  return static_cast<OwnQStatusBar *>(self)->OwnQStatusBar::event(a0);
}

#endif  // QT_CONFIG(statusbar)
#endif  // QT_CONFIG(statusbar)
