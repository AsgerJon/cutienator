//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpfiltersettingswidget.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtTools/qttools-config.h> before the #if, as it defines
//  QT_CONFIG(fullqthelp).
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpfiltersettingswidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QHelpFilterSettingsWidget that Python can take functions over in. Every QHelpFilterSettingsWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQHelpFilterSettingsWidgetCall0)(const void *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall1)(const void *, bool, int *);
typedef const QSize * (*CuteQHelpFilterSettingsWidgetCall2)(const void *, int *);
typedef const QSize * (*CuteQHelpFilterSettingsWidgetCall3)(const void *, int *);
typedef int (*CuteQHelpFilterSettingsWidgetCall4)(const void *, int, int *);
typedef bool (*CuteQHelpFilterSettingsWidgetCall5)(const void *, int *);
typedef void * (*CuteQHelpFilterSettingsWidgetCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpFilterSettingsWidgetCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterSettingsWidgetCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall11)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQHelpFilterSettingsWidgetCall12)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQHelpFilterSettingsWidgetCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall17)(const void *, QEnterEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall18)(const void *, QEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall19)(const void *, QPaintEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQHelpFilterSettingsWidgetCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQHelpFilterSettingsWidgetCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQHelpFilterSettingsWidgetCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpFilterSettingsWidgetCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpFilterSettingsWidgetCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpFilterSettingsWidgetCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHelpFilterSettingsWidgetCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQHelpFilterSettingsWidgetCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall32)(const void *, QEvent *, int *);
typedef int (*CuteQHelpFilterSettingsWidgetCall33)(const void *, int, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQHelpFilterSettingsWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQHelpFilterSettingsWidgetCall36)(const void *, int *);
typedef void (*CuteQHelpFilterSettingsWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQHelpFilterSettingsWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQHelpFilterSettingsWidgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpFilterSettingsWidgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterSettingsWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterSettingsWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterSettingsWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterSettingsWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterSettingsWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpFilterSettingsWidget : public QHelpFilterSettingsWidget {
public:
  using QHelpFilterSettingsWidget::QHelpFilterSettingsWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[30] = call;
      return true;
    }
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

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall0 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall1 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall1>(taken[1]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall2 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall3 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall4 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall4>(taken[4]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall5 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall6 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall7 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall8 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall9 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall10 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall11 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall12 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall13 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall14 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall15 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall16 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall17 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall18 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall19 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall20 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall21 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall22 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall23 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall24 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall25 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall26 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall27 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall28 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall29 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall30 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall31 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall32 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall33 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall34 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall35 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall36 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall37 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall38 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQHelpFilterSettingsWidgetCall39 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall39>(taken[39]);
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
      CuteQHelpFilterSettingsWidgetCall40 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall40>(taken[40]);
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
      CuteQHelpFilterSettingsWidgetCall41 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall41>(taken[41]);
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
      CuteQHelpFilterSettingsWidgetCall42 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall42>(taken[42]);
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
      CuteQHelpFilterSettingsWidgetCall43 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall43>(taken[43]);
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
      CuteQHelpFilterSettingsWidgetCall44 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall44>(taken[44]);
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
      CuteQHelpFilterSettingsWidgetCall45 call = reinterpret_cast<CuteQHelpFilterSettingsWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpFilterSettingsWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QHelpFilterSettingsWidget10metaObjectEv(
    const QHelpFilterSettingsWidget *self) {
  return self->metaObject();
}

//  void *QHelpFilterSettingsWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QHelpFilterSettingsWidget11qt_metacastEPKc(
    QHelpFilterSettingsWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpFilterSettingsWidget::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QHelpFilterSettingsWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpFilterSettingsWidget::tr(s, c, n));
}

//  QHelpFilterSettingsWidget::QHelpFilterSettingsWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QHelpFilterSettingsWidget *ritual_ZN25QHelpFilterSettingsWidgetC1EP7QWidget(
    QWidget *parent) {
  return new CuteQHelpFilterSettingsWidget(parent);
}

//  QHelpFilterSettingsWidget::~QHelpFilterSettingsWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHelpFilterSettingsWidgetD1Ev(
    QHelpFilterSettingsWidget *self) {
  delete self;
}

//  void QHelpFilterSettingsWidget::setAvailableComponents(const QStringList
//      &components)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHelpFilterSettingsWidget22setAvailableComponentsERK5QListI7QStringE(
    QHelpFilterSettingsWidget *self,
    const QList<QString> *components) {
  self->setAvailableComponents(*components);
}

//  void QHelpFilterSettingsWidget::setAvailableVersions(const
//      QList<QVersionNumber> &versions)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHelpFilterSettingsWidget20setAvailableVersionsERK5QListI14QVersionNumberE(
    QHelpFilterSettingsWidget *self,
    const QList<QVersionNumber> *versions) {
  self->setAvailableVersions(*versions);
}

//  void QHelpFilterSettingsWidget::readSettings(const QHelpFilterEngine
//      *filterEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHelpFilterSettingsWidget12readSettingsEPK17QHelpFilterEngine(
    QHelpFilterSettingsWidget *self,
    const QHelpFilterEngine *filterEngine) {
  self->readSettings(filterEngine);
}

//  bool QHelpFilterSettingsWidget::applySettings(QHelpFilterEngine
//      *filterEngine) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QHelpFilterSettingsWidget13applySettingsEP17QHelpFilterEngine(
    const QHelpFilterSettingsWidget *self,
    QHelpFilterEngine *filterEngine) {
  return self->applySettings(filterEngine);
}

//  QHelpFilterSettingsWidgetPrivate *QHelpFilterSettingsWidget::d_func()
extern "C" Q_DECL_EXPORT
QHelpFilterSettingsWidgetPrivate *ritual_ZN25QHelpFilterSettingsWidget6d_funcEv(
    QHelpFilterSettingsWidget *self) {
  return self->d_func();
}

//  const QHelpFilterSettingsWidgetPrivate
//      *QHelpFilterSettingsWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QHelpFilterSettingsWidgetPrivate *ritual_ZNK25QHelpFilterSettingsWidget6d_funcEv(
    const QHelpFilterSettingsWidget *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHelpFilterSettingsWidget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpFilterSettingsWidget(
    QHelpFilterSettingsWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpFilterSettingsWidget *>(self)->take(key, call);
}

#endif  // QT_CONFIG(fullqthelp)
