//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpsearchquerywidget.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtTools/qttools-config.h> before the #if, as it defines
//  QT_CONFIG(fullqthelp).
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpsearchquerywidget.h>
#include <QtCore/qstring.h>
#include <QtHelp/qhelpsearchengine.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QHelpSearchQueryWidget that Python can take functions over in. Every QHelpSearchQueryWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHelpSearchQueryWidgetCall0)(const void *, QFocusEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall1)(const void *, QEvent *, int *);
typedef int (*CuteQHelpSearchQueryWidgetCall2)(const void *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall3)(const void *, bool, int *);
typedef const QSize * (*CuteQHelpSearchQueryWidgetCall4)(const void *, int *);
typedef const QSize * (*CuteQHelpSearchQueryWidgetCall5)(const void *, int *);
typedef int (*CuteQHelpSearchQueryWidgetCall6)(const void *, int, int *);
typedef bool (*CuteQHelpSearchQueryWidgetCall7)(const void *, int *);
typedef void * (*CuteQHelpSearchQueryWidgetCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchQueryWidgetCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchQueryWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall13)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQHelpSearchQueryWidgetCall14)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQHelpSearchQueryWidgetCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall19)(const void *, QEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall21)(const void *, QMoveEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall22)(const void *, QResizeEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall23)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQHelpSearchQueryWidgetCall24)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQHelpSearchQueryWidgetCall25)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQHelpSearchQueryWidgetCall26)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchQueryWidgetCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchQueryWidgetCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchQueryWidgetCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchQueryWidgetCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQHelpSearchQueryWidgetCall31)(const void *, QShowEvent *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall32)(const void *, QHideEvent *, int *);
typedef int (*CuteQHelpSearchQueryWidgetCall33)(const void *, int, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQHelpSearchQueryWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQHelpSearchQueryWidgetCall36)(const void *, int *);
typedef void (*CuteQHelpSearchQueryWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQHelpSearchQueryWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQHelpSearchQueryWidgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchQueryWidgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchQueryWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchQueryWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchQueryWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchQueryWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchQueryWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpSearchQueryWidget : public QHelpSearchQueryWidget {
public:
  using QHelpSearchQueryWidget::QHelpSearchQueryWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
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

  //  void QHelpSearchQueryWidget::focusInEvent(QFocusEvent *focusEvent)
  void focusInEvent(QFocusEvent *focusEvent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall0 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall0>(taken[0]);
      call(this, focusEvent, &handled);
      if (handled) return;
    }
    QHelpSearchQueryWidget::focusInEvent(focusEvent);
  }

  //  void QHelpSearchQueryWidget::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall1 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QHelpSearchQueryWidget::changeEvent(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall2 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall3 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall4 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall5 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall6 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall6>(taken[6]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall7 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall8 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall9 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall10 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall11 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall12 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall13 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall14 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall15 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall16 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall17 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall18 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall19 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall20 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall21 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall22 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall23 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall23>(taken[23]);
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
      CuteQHelpSearchQueryWidgetCall24 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall24>(taken[24]);
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
      CuteQHelpSearchQueryWidgetCall25 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall25>(taken[25]);
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
      CuteQHelpSearchQueryWidgetCall26 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall26>(taken[26]);
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
      CuteQHelpSearchQueryWidgetCall27 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall27>(taken[27]);
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
      CuteQHelpSearchQueryWidgetCall28 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall28>(taken[28]);
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
      CuteQHelpSearchQueryWidgetCall29 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall29>(taken[29]);
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
      CuteQHelpSearchQueryWidgetCall30 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall30>(taken[30]);
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
      CuteQHelpSearchQueryWidgetCall31 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall32 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall33 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall34 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall35 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall36 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall37 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall38 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQHelpSearchQueryWidgetCall39 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall39>(taken[39]);
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
      CuteQHelpSearchQueryWidgetCall40 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall40>(taken[40]);
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
      CuteQHelpSearchQueryWidgetCall41 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall41>(taken[41]);
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
      CuteQHelpSearchQueryWidgetCall42 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall42>(taken[42]);
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
      CuteQHelpSearchQueryWidgetCall43 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall43>(taken[43]);
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
      CuteQHelpSearchQueryWidgetCall44 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall44>(taken[44]);
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
      CuteQHelpSearchQueryWidgetCall45 call = reinterpret_cast<CuteQHelpSearchQueryWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpSearchQueryWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QHelpSearchQueryWidget10metaObjectEv(
    const QHelpSearchQueryWidget *self) {
  return self->metaObject();
}

//  void *QHelpSearchQueryWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QHelpSearchQueryWidget11qt_metacastEPKc(
    QHelpSearchQueryWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpSearchQueryWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QHelpSearchQueryWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpSearchQueryWidget::tr(s, c, n));
}

//  QHelpSearchQueryWidget::QHelpSearchQueryWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QHelpSearchQueryWidget *ritual_ZN22QHelpSearchQueryWidgetC1EP7QWidget(
    QWidget *parent) {
  return new CuteQHelpSearchQueryWidget(parent);
}

//  QHelpSearchQueryWidget::~QHelpSearchQueryWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidgetD1Ev(QHelpSearchQueryWidget *self) {
  delete self;
}

//  void QHelpSearchQueryWidget::expandExtendedSearch()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget20expandExtendedSearchEv(
    QHelpSearchQueryWidget *self) {
  self->expandExtendedSearch();
}

//  void QHelpSearchQueryWidget::collapseExtendedSearch()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget22collapseExtendedSearchEv(
    QHelpSearchQueryWidget *self) {
  self->collapseExtendedSearch();
}

#if QT_DEPRECATED_SINCE(5, 9)
//  QList<QHelpSearchQuery> QHelpSearchQueryWidget::query() const
extern "C" Q_DECL_EXPORT
QList<QHelpSearchQuery> *ritual_ZNK22QHelpSearchQueryWidget5queryEv(
    const QHelpSearchQueryWidget *self) {
  return new QList<QHelpSearchQuery>(self->query());
}
#endif  // QT_DEPRECATED_SINCE(5, 9)

#if QT_DEPRECATED_SINCE(5, 9)
//  void QHelpSearchQueryWidget::setQuery(const QList<QHelpSearchQuery>
//      &queryList)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget8setQueryERK5QListI16QHelpSearchQueryE(
    QHelpSearchQueryWidget *self,
    const QList<QHelpSearchQuery> *queryList) {
  self->setQuery(*queryList);
}
#endif  // QT_DEPRECATED_SINCE(5, 9)

//  QString QHelpSearchQueryWidget::searchInput() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHelpSearchQueryWidget11searchInputEv(
    const QHelpSearchQueryWidget *self) {
  return new QString(self->searchInput());
}

//  void QHelpSearchQueryWidget::setSearchInput(const QString &searchInput)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget14setSearchInputERK7QString(
    QHelpSearchQueryWidget *self,
    const QString *searchInput) {
  self->setSearchInput(*searchInput);
}

//  bool QHelpSearchQueryWidget::isCompactMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QHelpSearchQueryWidget13isCompactModeEv(
    const QHelpSearchQueryWidget *self) {
  return self->isCompactMode();
}

//  void QHelpSearchQueryWidget::setCompactMode(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget14setCompactModeEb(
    QHelpSearchQueryWidget *self,
    bool on) {
  self->setCompactMode(on);
}

//  void QHelpSearchQueryWidget::search()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget6searchEv(
    QHelpSearchQueryWidget *self) {
  self->search();
}

//  void QHelpSearchQueryWidget::focusInEvent(QFocusEvent *focusEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget12focusInEventEP11QFocusEvent(
    QHelpSearchQueryWidget *self,
    QFocusEvent *focusEvent) {
  self->focusInEvent(focusEvent);
}

//  void QHelpSearchQueryWidget::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpSearchQueryWidget11changeEventEP6QEvent(
    QHelpSearchQueryWidget *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  a Python function taken by a CuteQHelpSearchQueryWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpSearchQueryWidget(
    QHelpSearchQueryWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpSearchQueryWidget *>(self)->take(key, call);
}

//  void QHelpSearchQueryWidget::focusInEvent(QFocusEvent *focusEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QHelpSearchQueryWidget12focusInEventEP11QFocusEvent(
    QHelpSearchQueryWidget *self,
    QFocusEvent *focusEvent) {
  self->QHelpSearchQueryWidget::focusInEvent(focusEvent);
}

//  void QHelpSearchQueryWidget::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QHelpSearchQueryWidget11changeEventEP6QEvent(
    QHelpSearchQueryWidget *self,
    QEvent *event) {
  self->QHelpSearchQueryWidget::changeEvent(event);
}

#endif  // QT_CONFIG(fullqthelp)
