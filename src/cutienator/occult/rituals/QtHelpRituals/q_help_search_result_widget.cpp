//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpsearchresultwidget.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtTools/qttools-config.h> before the #if, as it defines
//  QT_CONFIG(fullqthelp).
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpsearchresultwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHelpSearchResultWidget that Python can take functions over in. Every QHelpSearchResultWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHelpSearchResultWidgetCall0)(const void *, QEvent *, int *);
typedef int (*CuteQHelpSearchResultWidgetCall1)(const void *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall2)(const void *, bool, int *);
typedef const QSize * (*CuteQHelpSearchResultWidgetCall3)(const void *, int *);
typedef const QSize * (*CuteQHelpSearchResultWidgetCall4)(const void *, int *);
typedef int (*CuteQHelpSearchResultWidgetCall5)(const void *, int, int *);
typedef bool (*CuteQHelpSearchResultWidgetCall6)(const void *, int *);
typedef void * (*CuteQHelpSearchResultWidgetCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchResultWidgetCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchResultWidgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall12)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQHelpSearchResultWidgetCall13)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQHelpSearchResultWidgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall19)(const void *, QEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall21)(const void *, QMoveEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall22)(const void *, QResizeEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall23)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQHelpSearchResultWidgetCall24)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQHelpSearchResultWidgetCall25)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQHelpSearchResultWidgetCall26)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchResultWidgetCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchResultWidgetCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchResultWidgetCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchResultWidgetCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchResultWidgetCall31)(const void *, QShowEvent *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall32)(const void *, QHideEvent *, int *);
typedef int (*CuteQHelpSearchResultWidgetCall33)(const void *, int, int *);
typedef void (*CuteQHelpSearchResultWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQHelpSearchResultWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQHelpSearchResultWidgetCall36)(const void *, int *);
typedef void (*CuteQHelpSearchResultWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQHelpSearchResultWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQHelpSearchResultWidgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchResultWidgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchResultWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchResultWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchResultWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchResultWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchResultWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpSearchResultWidget : public QHelpSearchResultWidget {
public:
  using QHelpSearchResultWidget::QHelpSearchResultWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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

  //  void QHelpSearchResultWidget::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall0 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QHelpSearchResultWidget::changeEvent(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall1 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall2 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall3 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall4 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall5 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall5>(taken[5]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall6 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall7 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall8 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall9 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall10 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall11 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall12 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall13 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall14 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall15 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall16 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall17 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall18 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall19 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall20 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall21 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall22 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall23 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall23>(taken[23]);
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
      CuteQHelpSearchResultWidgetCall24 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall24>(taken[24]);
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
      CuteQHelpSearchResultWidgetCall25 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall25>(taken[25]);
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
      CuteQHelpSearchResultWidgetCall26 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall26>(taken[26]);
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
      CuteQHelpSearchResultWidgetCall27 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall27>(taken[27]);
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
      CuteQHelpSearchResultWidgetCall28 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall28>(taken[28]);
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
      CuteQHelpSearchResultWidgetCall29 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall29>(taken[29]);
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
      CuteQHelpSearchResultWidgetCall30 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall31 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall32 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall33 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall34 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall35 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall36 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall37 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall38 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQHelpSearchResultWidgetCall39 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall39>(taken[39]);
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
      CuteQHelpSearchResultWidgetCall40 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall40>(taken[40]);
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
      CuteQHelpSearchResultWidgetCall41 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall41>(taken[41]);
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
      CuteQHelpSearchResultWidgetCall42 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall42>(taken[42]);
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
      CuteQHelpSearchResultWidgetCall43 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall43>(taken[43]);
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
      CuteQHelpSearchResultWidgetCall44 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall44>(taken[44]);
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
      CuteQHelpSearchResultWidgetCall45 call = reinterpret_cast<CuteQHelpSearchResultWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpSearchResultWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QHelpSearchResultWidget10metaObjectEv(
    const QHelpSearchResultWidget *self) {
  return self->metaObject();
}

//  void *QHelpSearchResultWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QHelpSearchResultWidget11qt_metacastEPKc(
    QHelpSearchResultWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpSearchResultWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QHelpSearchResultWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpSearchResultWidget::tr(s, c, n));
}

//  QHelpSearchResultWidget::~QHelpSearchResultWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QHelpSearchResultWidgetD1Ev(QHelpSearchResultWidget *self) {
  delete self;
}

//  QUrl QHelpSearchResultWidget::linkAt(const QPoint &point)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN23QHelpSearchResultWidget6linkAtERK6QPoint(
    QHelpSearchResultWidget *self,
    const QPoint *point) {
  return new QUrl(self->linkAt(*point));
}

//  void QHelpSearchResultWidget::requestShowLink(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QHelpSearchResultWidget15requestShowLinkERK4QUrl(
    QHelpSearchResultWidget *self,
    const QUrl *url) {
  self->requestShowLink(*url);
}

//  QHelpSearchResultWidget::QHelpSearchResultWidget(QHelpSearchEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QHelpSearchResultWidget *ritual_ZN23QHelpSearchResultWidgetC1EP17QHelpSearchEngine(
    QHelpSearchEngine *engine) {
  return new CuteQHelpSearchResultWidget(engine);
}

//  void QHelpSearchResultWidget::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QHelpSearchResultWidget11changeEventEP6QEvent(
    QHelpSearchResultWidget *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  a Python function taken by a CuteQHelpSearchResultWidget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpSearchResultWidget(
    QHelpSearchResultWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpSearchResultWidget *>(self)->take(key, call);
}

//  void QHelpSearchResultWidget::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QHelpSearchResultWidget11changeEventEP6QEvent(
    QHelpSearchResultWidget *self,
    QEvent *event) {
  self->QHelpSearchResultWidget::changeEvent(event);
}

#endif  // QT_CONFIG(fullqthelp)
