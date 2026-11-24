//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDesignerWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDesignerWidget : QDesignerWidget {
  using QDesignerWidget::paintEvent;
};

//  A QDesignerWidget that Python can take functions over in. Every QDesignerWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQDesignerWidgetCall0)(const void *, int *);
typedef void (*CuteQDesignerWidgetCall1)(const void *, QPaintEvent *, int *);
typedef int (*CuteQDesignerWidgetCall2)(const void *, int *);
typedef void (*CuteQDesignerWidgetCall3)(const void *, bool, int *);
typedef const QSize * (*CuteQDesignerWidgetCall4)(const void *, int *);
typedef int (*CuteQDesignerWidgetCall5)(const void *, int, int *);
typedef bool (*CuteQDesignerWidgetCall6)(const void *, int *);
typedef void * (*CuteQDesignerWidgetCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerWidgetCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerWidgetCall12)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerWidgetCall13)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerWidgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerWidgetCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerWidgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerWidgetCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerWidgetCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerWidgetCall19)(const void *, QEvent *, int *);
typedef void (*CuteQDesignerWidgetCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerWidgetCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDesignerWidgetCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerWidgetCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerWidgetCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerWidgetCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerWidgetCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQDesignerWidgetCall32)(const void *, QEvent *, int *);
typedef int (*CuteQDesignerWidgetCall33)(const void *, int, int *);
typedef void (*CuteQDesignerWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerWidgetCall36)(const void *, int *);
typedef void (*CuteQDesignerWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQDesignerWidgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerWidget : public QDesignerWidget {
public:
  using QDesignerWidget::QDesignerWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
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

  //  QSize QDesignerWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerWidgetCall0 call = reinterpret_cast<CuteQDesignerWidgetCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDesignerWidget::minimumSizeHint();
  }

  //  void QDesignerWidget::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerWidgetCall1 call = reinterpret_cast<CuteQDesignerWidgetCall1>(taken[1]);
      call(this, e, &handled);
      if (handled) return;
    }
    QDesignerWidget::paintEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerWidgetCall2 call = reinterpret_cast<CuteQDesignerWidgetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerWidgetCall3 call = reinterpret_cast<CuteQDesignerWidgetCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerWidgetCall4 call = reinterpret_cast<CuteQDesignerWidgetCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerWidgetCall5 call = reinterpret_cast<CuteQDesignerWidgetCall5>(taken[5]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerWidgetCall6 call = reinterpret_cast<CuteQDesignerWidgetCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerWidgetCall7 call = reinterpret_cast<CuteQDesignerWidgetCall7>(taken[7]);
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
      CuteQDesignerWidgetCall8 call = reinterpret_cast<CuteQDesignerWidgetCall8>(taken[8]);
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
      CuteQDesignerWidgetCall9 call = reinterpret_cast<CuteQDesignerWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerWidgetCall10 call = reinterpret_cast<CuteQDesignerWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerWidgetCall11 call = reinterpret_cast<CuteQDesignerWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerWidgetCall12 call = reinterpret_cast<CuteQDesignerWidgetCall12>(taken[12]);
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
      CuteQDesignerWidgetCall13 call = reinterpret_cast<CuteQDesignerWidgetCall13>(taken[13]);
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
      CuteQDesignerWidgetCall14 call = reinterpret_cast<CuteQDesignerWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerWidgetCall15 call = reinterpret_cast<CuteQDesignerWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerWidgetCall16 call = reinterpret_cast<CuteQDesignerWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerWidgetCall17 call = reinterpret_cast<CuteQDesignerWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerWidgetCall18 call = reinterpret_cast<CuteQDesignerWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerWidgetCall19 call = reinterpret_cast<CuteQDesignerWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerWidgetCall20 call = reinterpret_cast<CuteQDesignerWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerWidgetCall21 call = reinterpret_cast<CuteQDesignerWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerWidgetCall22 call = reinterpret_cast<CuteQDesignerWidgetCall22>(taken[22]);
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
      CuteQDesignerWidgetCall23 call = reinterpret_cast<CuteQDesignerWidgetCall23>(taken[23]);
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
      CuteQDesignerWidgetCall24 call = reinterpret_cast<CuteQDesignerWidgetCall24>(taken[24]);
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
      CuteQDesignerWidgetCall25 call = reinterpret_cast<CuteQDesignerWidgetCall25>(taken[25]);
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
      CuteQDesignerWidgetCall26 call = reinterpret_cast<CuteQDesignerWidgetCall26>(taken[26]);
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
      CuteQDesignerWidgetCall27 call = reinterpret_cast<CuteQDesignerWidgetCall27>(taken[27]);
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
      CuteQDesignerWidgetCall28 call = reinterpret_cast<CuteQDesignerWidgetCall28>(taken[28]);
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
      CuteQDesignerWidgetCall29 call = reinterpret_cast<CuteQDesignerWidgetCall29>(taken[29]);
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
      CuteQDesignerWidgetCall30 call = reinterpret_cast<CuteQDesignerWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDesignerWidgetCall31 call = reinterpret_cast<CuteQDesignerWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDesignerWidgetCall32 call = reinterpret_cast<CuteQDesignerWidgetCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerWidgetCall33 call = reinterpret_cast<CuteQDesignerWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerWidgetCall34 call = reinterpret_cast<CuteQDesignerWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerWidgetCall35 call = reinterpret_cast<CuteQDesignerWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerWidgetCall36 call = reinterpret_cast<CuteQDesignerWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerWidgetCall37 call = reinterpret_cast<CuteQDesignerWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerWidgetCall38 call = reinterpret_cast<CuteQDesignerWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerWidgetCall39 call = reinterpret_cast<CuteQDesignerWidgetCall39>(taken[39]);
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
      CuteQDesignerWidgetCall40 call = reinterpret_cast<CuteQDesignerWidgetCall40>(taken[40]);
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
      CuteQDesignerWidgetCall41 call = reinterpret_cast<CuteQDesignerWidgetCall41>(taken[41]);
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
      CuteQDesignerWidgetCall42 call = reinterpret_cast<CuteQDesignerWidgetCall42>(taken[42]);
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
      CuteQDesignerWidgetCall43 call = reinterpret_cast<CuteQDesignerWidgetCall43>(taken[43]);
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
      CuteQDesignerWidgetCall44 call = reinterpret_cast<CuteQDesignerWidgetCall44>(taken[44]);
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
      CuteQDesignerWidgetCall45 call = reinterpret_cast<CuteQDesignerWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QDesignerWidget10metaObjectEv(
    const QDesignerWidget *self) {
  return self->metaObject();
}

//  QString QDesignerWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QDesignerWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerWidget::tr(s, c, n));
}

//  QDesignerWidget::QDesignerWidget(QDesignerFormWindowInterface
//      *formWindow, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerWidget *ritual_ZN15QDesignerWidgetC1EP28QDesignerFormWindowInterfaceP7QWidget(
    QDesignerFormWindowInterface *formWindow,
    QWidget *parent) {
  return new CuteQDesignerWidget(formWindow, parent);
}

//  QDesignerWidget::~QDesignerWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDesignerWidgetD1Ev(QDesignerWidget *self) {
  delete self;
}

//  QDesignerFormWindowInterface *QDesignerWidget::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK15QDesignerWidget10formWindowEv(
    const QDesignerWidget *self) {
  return self->formWindow();
}

//  QSize QDesignerWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QDesignerWidget15minimumSizeHintEv(
    const QDesignerWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QDesignerWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDesignerWidget10paintEventEP11QPaintEvent(
    QDesignerWidget *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  a Python function taken by a CuteQDesignerWidget, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerWidget(
    QDesignerWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerWidget *>(self)->take(key, call);
}

//  QSize QDesignerWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QDesignerWidget15minimumSizeHintEv(
    const QDesignerWidget *self) {
  return new QSize(self->QDesignerWidget::minimumSizeHint());
}

//  void QDesignerWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QDesignerWidget10paintEventEP11QPaintEvent(
    QDesignerWidget *self,
    QPaintEvent *e) {
  static_cast<OwnQDesignerWidget *>(self)->OwnQDesignerWidget::paintEvent(e);
}
