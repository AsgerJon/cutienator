//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfocusframe.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qfocusframe.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QFocusFrame may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFocusFrame : QFocusFrame {
  using QFocusFrame::event;
  using QFocusFrame::eventFilter;
  using QFocusFrame::paintEvent;
  using QFocusFrame::initStyleOption;
};

//  A QFocusFrame that Python can take functions over in. Every QFocusFrame
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFocusFrameCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFocusFrameCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQFocusFrameCall2)(const void *, QPaintEvent *, int *);
typedef void (*CuteQFocusFrameCall3)(const void *, QStyleOption *, int *);
typedef int (*CuteQFocusFrameCall4)(const void *, int *);
typedef void (*CuteQFocusFrameCall5)(const void *, bool, int *);
typedef const QSize * (*CuteQFocusFrameCall6)(const void *, int *);
typedef const QSize * (*CuteQFocusFrameCall7)(const void *, int *);
typedef int (*CuteQFocusFrameCall8)(const void *, int, int *);
typedef bool (*CuteQFocusFrameCall9)(const void *, int *);
typedef void * (*CuteQFocusFrameCall10)(const void *, int *);
typedef void (*CuteQFocusFrameCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFocusFrameCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFocusFrameCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFocusFrameCall14)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQFocusFrameCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQFocusFrameCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQFocusFrameCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQFocusFrameCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFocusFrameCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFocusFrameCall20)(const void *, QEnterEvent *, int *);
typedef void (*CuteQFocusFrameCall21)(const void *, QEvent *, int *);
typedef void (*CuteQFocusFrameCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQFocusFrameCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQFocusFrameCall24)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQFocusFrameCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQFocusFrameCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQFocusFrameCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFocusFrameCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFocusFrameCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFocusFrameCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFocusFrameCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQFocusFrameCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQFocusFrameCall33)(const void *, QHideEvent *, int *);
typedef void (*CuteQFocusFrameCall34)(const void *, QEvent *, int *);
typedef int (*CuteQFocusFrameCall35)(const void *, int, int *);
typedef void (*CuteQFocusFrameCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQFocusFrameCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQFocusFrameCall38)(const void *, int *);
typedef void (*CuteQFocusFrameCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQFocusFrameCall40)(const void *, int, int *);
typedef bool (*CuteQFocusFrameCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFocusFrameCall42)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFocusFrameCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFocusFrameCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFocusFrameCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFocusFrameCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFocusFrame : public QFocusFrame {
public:
  using QFocusFrame::QFocusFrame;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFocusFrame15initStyleOptionEP12QStyleOption")) {
      taken[3] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
  //  bool QFocusFrame::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFocusFrameCall0 call = reinterpret_cast<CuteQFocusFrameCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QFocusFrame::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QFocusFrame::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFocusFrameCall1 call = reinterpret_cast<CuteQFocusFrameCall1>(taken[1]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QFocusFrame::eventFilter(a0, a1);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QFocusFrame::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFocusFrameCall2 call = reinterpret_cast<CuteQFocusFrameCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFocusFrame::paintEvent(a0);
  }

  //  void QFocusFrame::initStyleOption(QStyleOption *option) const
  void initStyleOption(QStyleOption *option) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFocusFrameCall3 call = reinterpret_cast<CuteQFocusFrameCall3>(taken[3]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFocusFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFocusFrameCall4 call = reinterpret_cast<CuteQFocusFrameCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFocusFrameCall5 call = reinterpret_cast<CuteQFocusFrameCall5>(taken[5]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFocusFrameCall6 call = reinterpret_cast<CuteQFocusFrameCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFocusFrameCall7 call = reinterpret_cast<CuteQFocusFrameCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFocusFrameCall8 call = reinterpret_cast<CuteQFocusFrameCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFocusFrameCall9 call = reinterpret_cast<CuteQFocusFrameCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFocusFrameCall10 call = reinterpret_cast<CuteQFocusFrameCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFocusFrameCall11 call = reinterpret_cast<CuteQFocusFrameCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFocusFrameCall12 call = reinterpret_cast<CuteQFocusFrameCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFocusFrameCall13 call = reinterpret_cast<CuteQFocusFrameCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFocusFrameCall14 call = reinterpret_cast<CuteQFocusFrameCall14>(taken[14]);
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
      CuteQFocusFrameCall15 call = reinterpret_cast<CuteQFocusFrameCall15>(taken[15]);
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
      CuteQFocusFrameCall16 call = reinterpret_cast<CuteQFocusFrameCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFocusFrameCall17 call = reinterpret_cast<CuteQFocusFrameCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFocusFrameCall18 call = reinterpret_cast<CuteQFocusFrameCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFocusFrameCall19 call = reinterpret_cast<CuteQFocusFrameCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFocusFrameCall20 call = reinterpret_cast<CuteQFocusFrameCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFocusFrameCall21 call = reinterpret_cast<CuteQFocusFrameCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFocusFrameCall22 call = reinterpret_cast<CuteQFocusFrameCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFocusFrameCall23 call = reinterpret_cast<CuteQFocusFrameCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFocusFrameCall24 call = reinterpret_cast<CuteQFocusFrameCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFocusFrameCall25 call = reinterpret_cast<CuteQFocusFrameCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFocusFrameCall26 call = reinterpret_cast<CuteQFocusFrameCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFocusFrameCall27 call = reinterpret_cast<CuteQFocusFrameCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFocusFrameCall28 call = reinterpret_cast<CuteQFocusFrameCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFocusFrameCall29 call = reinterpret_cast<CuteQFocusFrameCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQFocusFrameCall30 call = reinterpret_cast<CuteQFocusFrameCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQFocusFrameCall31 call = reinterpret_cast<CuteQFocusFrameCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQFocusFrameCall32 call = reinterpret_cast<CuteQFocusFrameCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQFocusFrameCall33 call = reinterpret_cast<CuteQFocusFrameCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQFocusFrameCall34 call = reinterpret_cast<CuteQFocusFrameCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQFocusFrameCall35 call = reinterpret_cast<CuteQFocusFrameCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQFocusFrameCall36 call = reinterpret_cast<CuteQFocusFrameCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQFocusFrameCall37 call = reinterpret_cast<CuteQFocusFrameCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQFocusFrameCall38 call = reinterpret_cast<CuteQFocusFrameCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQFocusFrameCall39 call = reinterpret_cast<CuteQFocusFrameCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQFocusFrameCall40 call = reinterpret_cast<CuteQFocusFrameCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQFocusFrameCall41 call = reinterpret_cast<CuteQFocusFrameCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQFocusFrameCall42 call = reinterpret_cast<CuteQFocusFrameCall42>(taken[42]);
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
      CuteQFocusFrameCall43 call = reinterpret_cast<CuteQFocusFrameCall43>(taken[43]);
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
      CuteQFocusFrameCall44 call = reinterpret_cast<CuteQFocusFrameCall44>(taken[44]);
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
      CuteQFocusFrameCall45 call = reinterpret_cast<CuteQFocusFrameCall45>(taken[45]);
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
      CuteQFocusFrameCall46 call = reinterpret_cast<CuteQFocusFrameCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFocusFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFocusFrame10metaObjectEv(
    const QFocusFrame *self) {
  return self->metaObject();
}

//  QString QFocusFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFocusFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFocusFrame::tr(s, c, n));
}

//  QFocusFrame::QFocusFrame(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFocusFrame *ritual_ZN11QFocusFrameC1EP7QWidget(QWidget *parent) {
  return new CuteQFocusFrame(parent);
}

//  QFocusFrame::~QFocusFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFocusFrameD1Ev(QFocusFrame *self) {
  delete self;
}

//  void QFocusFrame::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFocusFrame9setWidgetEP7QWidget(
    QFocusFrame *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QFocusFrame::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QFocusFrame6widgetEv(const QFocusFrame *self) {
  return self->widget();
}

//  bool QFocusFrame::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFocusFrame5eventEP6QEvent(QFocusFrame *self, QEvent *e) {
  return self->event(e);
}

//  bool QFocusFrame::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFocusFrame11eventFilterEP7QObjectP6QEvent(
    QFocusFrame *self,
    QObject *a0,
    QEvent *a1) {
  return self->eventFilter(a0, a1);
}

//  void QFocusFrame::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFocusFrame10paintEventEP11QPaintEvent(
    QFocusFrame *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QFocusFrame::initStyleOption(QStyleOption *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QFocusFrame15initStyleOptionEP12QStyleOption(
    const QFocusFrame *self,
    QStyleOption *option) {
  self->initStyleOption(option);
}

//  a Python function taken by a CuteQFocusFrame, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFocusFrame(
    QFocusFrame *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFocusFrame *>(self)->take(key, call);
}

//  bool QFocusFrame::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QFocusFrame5eventEP6QEvent(
    QFocusFrame *self,
    QEvent *e) {
  return static_cast<OwnQFocusFrame *>(self)->OwnQFocusFrame::event(e);
}

//  bool QFocusFrame::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QFocusFrame11eventFilterEP7QObjectP6QEvent(
    QFocusFrame *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQFocusFrame *>(self)->OwnQFocusFrame::eventFilter(
      a0,
      a1);
}

//  void QFocusFrame::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFocusFrame10paintEventEP11QPaintEvent(
    QFocusFrame *self,
    QPaintEvent *a0) {
  static_cast<OwnQFocusFrame *>(self)->OwnQFocusFrame::paintEvent(a0);
}

//  void QFocusFrame::initStyleOption(QStyleOption *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QFocusFrame15initStyleOptionEP12QStyleOption(
    const QFocusFrame *self,
    QStyleOption *option) {
  static_cast<const OwnQFocusFrame *>(self)->OwnQFocusFrame::initStyleOption(
      option);
}
