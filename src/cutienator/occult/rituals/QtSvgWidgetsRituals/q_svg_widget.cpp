//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvgWidgets/qsvgwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtSvgWidgets/qsvgwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSvgWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSvgWidget : QSvgWidget {
  using QSvgWidget::paintEvent;
};

//  A QSvgWidget that Python can take functions over in. Every QSvgWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSvgWidgetCall0)(const void *, int *);
typedef void (*CuteQSvgWidgetCall1)(const void *, QPaintEvent *, int *);
typedef int (*CuteQSvgWidgetCall2)(const void *, int *);
typedef void (*CuteQSvgWidgetCall3)(const void *, bool, int *);
typedef const QSize * (*CuteQSvgWidgetCall4)(const void *, int *);
typedef int (*CuteQSvgWidgetCall5)(const void *, int, int *);
typedef bool (*CuteQSvgWidgetCall6)(const void *, int *);
typedef void * (*CuteQSvgWidgetCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSvgWidgetCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgWidgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSvgWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSvgWidgetCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSvgWidgetCall12)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQSvgWidgetCall13)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQSvgWidgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSvgWidgetCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSvgWidgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSvgWidgetCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSvgWidgetCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQSvgWidgetCall19)(const void *, QEvent *, int *);
typedef void (*CuteQSvgWidgetCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQSvgWidgetCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQSvgWidgetCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQSvgWidgetCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQSvgWidgetCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQSvgWidgetCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSvgWidgetCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSvgWidgetCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSvgWidgetCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSvgWidgetCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQSvgWidgetCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQSvgWidgetCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQSvgWidgetCall32)(const void *, QEvent *, int *);
typedef int (*CuteQSvgWidgetCall33)(const void *, int, int *);
typedef void (*CuteQSvgWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQSvgWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQSvgWidgetCall36)(const void *, int *);
typedef void (*CuteQSvgWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQSvgWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQSvgWidgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSvgWidgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSvgWidget : public QSvgWidget {
public:
  using QSvgWidget::QSvgWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
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

  //  QSize QSvgWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgWidgetCall0 call = reinterpret_cast<CuteQSvgWidgetCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSvgWidget::sizeHint();
  }

  //  void QSvgWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgWidgetCall1 call = reinterpret_cast<CuteQSvgWidgetCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QSvgWidget::paintEvent(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgWidgetCall2 call = reinterpret_cast<CuteQSvgWidgetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgWidgetCall3 call = reinterpret_cast<CuteQSvgWidgetCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSvgWidgetCall4 call = reinterpret_cast<CuteQSvgWidgetCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSvgWidgetCall5 call = reinterpret_cast<CuteQSvgWidgetCall5>(taken[5]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSvgWidgetCall6 call = reinterpret_cast<CuteQSvgWidgetCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSvgWidgetCall7 call = reinterpret_cast<CuteQSvgWidgetCall7>(taken[7]);
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
      CuteQSvgWidgetCall8 call = reinterpret_cast<CuteQSvgWidgetCall8>(taken[8]);
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
      CuteQSvgWidgetCall9 call = reinterpret_cast<CuteQSvgWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSvgWidgetCall10 call = reinterpret_cast<CuteQSvgWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSvgWidgetCall11 call = reinterpret_cast<CuteQSvgWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSvgWidgetCall12 call = reinterpret_cast<CuteQSvgWidgetCall12>(taken[12]);
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
      CuteQSvgWidgetCall13 call = reinterpret_cast<CuteQSvgWidgetCall13>(taken[13]);
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
      CuteQSvgWidgetCall14 call = reinterpret_cast<CuteQSvgWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSvgWidgetCall15 call = reinterpret_cast<CuteQSvgWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSvgWidgetCall16 call = reinterpret_cast<CuteQSvgWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSvgWidgetCall17 call = reinterpret_cast<CuteQSvgWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSvgWidgetCall18 call = reinterpret_cast<CuteQSvgWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSvgWidgetCall19 call = reinterpret_cast<CuteQSvgWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSvgWidgetCall20 call = reinterpret_cast<CuteQSvgWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSvgWidgetCall21 call = reinterpret_cast<CuteQSvgWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSvgWidgetCall22 call = reinterpret_cast<CuteQSvgWidgetCall22>(taken[22]);
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
      CuteQSvgWidgetCall23 call = reinterpret_cast<CuteQSvgWidgetCall23>(taken[23]);
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
      CuteQSvgWidgetCall24 call = reinterpret_cast<CuteQSvgWidgetCall24>(taken[24]);
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
      CuteQSvgWidgetCall25 call = reinterpret_cast<CuteQSvgWidgetCall25>(taken[25]);
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
      CuteQSvgWidgetCall26 call = reinterpret_cast<CuteQSvgWidgetCall26>(taken[26]);
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
      CuteQSvgWidgetCall27 call = reinterpret_cast<CuteQSvgWidgetCall27>(taken[27]);
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
      CuteQSvgWidgetCall28 call = reinterpret_cast<CuteQSvgWidgetCall28>(taken[28]);
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
      CuteQSvgWidgetCall29 call = reinterpret_cast<CuteQSvgWidgetCall29>(taken[29]);
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
      CuteQSvgWidgetCall30 call = reinterpret_cast<CuteQSvgWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSvgWidgetCall31 call = reinterpret_cast<CuteQSvgWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSvgWidgetCall32 call = reinterpret_cast<CuteQSvgWidgetCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQSvgWidgetCall33 call = reinterpret_cast<CuteQSvgWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQSvgWidgetCall34 call = reinterpret_cast<CuteQSvgWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQSvgWidgetCall35 call = reinterpret_cast<CuteQSvgWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQSvgWidgetCall36 call = reinterpret_cast<CuteQSvgWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQSvgWidgetCall37 call = reinterpret_cast<CuteQSvgWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQSvgWidgetCall38 call = reinterpret_cast<CuteQSvgWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQSvgWidgetCall39 call = reinterpret_cast<CuteQSvgWidgetCall39>(taken[39]);
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
      CuteQSvgWidgetCall40 call = reinterpret_cast<CuteQSvgWidgetCall40>(taken[40]);
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
      CuteQSvgWidgetCall41 call = reinterpret_cast<CuteQSvgWidgetCall41>(taken[41]);
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
      CuteQSvgWidgetCall42 call = reinterpret_cast<CuteQSvgWidgetCall42>(taken[42]);
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
      CuteQSvgWidgetCall43 call = reinterpret_cast<CuteQSvgWidgetCall43>(taken[43]);
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
      CuteQSvgWidgetCall44 call = reinterpret_cast<CuteQSvgWidgetCall44>(taken[44]);
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
      CuteQSvgWidgetCall45 call = reinterpret_cast<CuteQSvgWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSvgWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QSvgWidget10metaObjectEv(
    const QSvgWidget *self) {
  return self->metaObject();
}

//  void *QSvgWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QSvgWidget11qt_metacastEPKc(
    QSvgWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSvgWidget::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSvgWidget11qt_metacallEN11QMetaObject4CallEiPPv(
    QSvgWidget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSvgWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSvgWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSvgWidget::tr(s, c, n));
}

//  QSvgWidget::QSvgWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSvgWidget *ritual_ZN10QSvgWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQSvgWidget(parent);
}

//  QSvgWidget::QSvgWidget(const QString &file, QWidget *parent)
extern "C" Q_DECL_EXPORT
QSvgWidget *ritual_ZN10QSvgWidgetC1ERK7QStringP7QWidget(
    const QString *file,
    QWidget *parent) {
  return new CuteQSvgWidget(*file, parent);
}

//  QSvgWidget::~QSvgWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgWidgetD1Ev(QSvgWidget *self) {
  delete self;
}

//  QSvgRenderer *QSvgWidget::renderer() const
extern "C" Q_DECL_EXPORT
QSvgRenderer *ritual_ZNK10QSvgWidget8rendererEv(const QSvgWidget *self) {
  return self->renderer();
}

//  QSize QSvgWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QSvgWidget8sizeHintEv(const QSvgWidget *self) {
  return new QSize(self->sizeHint());
}

//  QtSvg::Options QSvgWidget::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSvgWidget7optionsEv(const QSvgWidget *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QSvgWidget::setOptions(QtSvg::Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgWidget10setOptionsE6QFlagsIN5QtSvg6OptionEE(
    QSvgWidget *self,
    int options) {
  self->setOptions(QFlags<QtSvg::Option>::fromInt(options));
}

//  void QSvgWidget::load(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgWidget4loadERK7QString(
    QSvgWidget *self,
    const QString *file) {
  self->load(*file);
}

//  void QSvgWidget::load(const QByteArray &contents)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgWidget4loadERK10QByteArray(
    QSvgWidget *self,
    const QByteArray *contents) {
  self->load(*contents);
}

//  void QSvgWidget::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgWidget10paintEventEP11QPaintEvent(
    QSvgWidget *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  QSvgWidgetPrivate *QSvgWidget::d_func()
extern "C" Q_DECL_EXPORT
QSvgWidgetPrivate *ritual_ZN10QSvgWidget6d_funcEv(QSvgWidget *self) {
  return self->d_func();
}

//  const QSvgWidgetPrivate *QSvgWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QSvgWidgetPrivate *ritual_ZNK10QSvgWidget6d_funcEv(
    const QSvgWidget *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSvgWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgWidget(QSvgWidget *self, const char *key, void *call) {
  return static_cast<CuteQSvgWidget *>(self)->take(key, call);
}

//  QSize QSvgWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QSvgWidget8sizeHintEv(const QSvgWidget *self) {
  return new QSize(self->QSvgWidget::sizeHint());
}

//  void QSvgWidget::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSvgWidget10paintEventEP11QPaintEvent(
    QSvgWidget *self,
    QPaintEvent *event) {
  static_cast<OwnQSvgWidget *>(self)->OwnQSvgWidget::paintEvent(event);
}
