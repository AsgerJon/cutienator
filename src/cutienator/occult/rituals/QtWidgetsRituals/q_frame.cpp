//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qframe.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qframe.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QFrame may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFrame : QFrame {
  using QFrame::event;
  using QFrame::paintEvent;
  using QFrame::changeEvent;
  using QFrame::initStyleOption;
};

//  A QFrame that Python can take functions over in. Every QFrame
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQFrameCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFrameCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQFrameCall2)(const void *, QPaintEvent *, int *);
typedef void (*CuteQFrameCall3)(const void *, QEvent *, int *);
typedef void (*CuteQFrameCall4)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQFrameCall5)(const void *, int *);
typedef void (*CuteQFrameCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQFrameCall7)(const void *, int *);
typedef int (*CuteQFrameCall8)(const void *, int, int *);
typedef bool (*CuteQFrameCall9)(const void *, int *);
typedef void * (*CuteQFrameCall10)(const void *, int *);
typedef void (*CuteQFrameCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFrameCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFrameCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFrameCall14)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQFrameCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQFrameCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQFrameCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQFrameCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFrameCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFrameCall20)(const void *, QEnterEvent *, int *);
typedef void (*CuteQFrameCall21)(const void *, QEvent *, int *);
typedef void (*CuteQFrameCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQFrameCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQFrameCall24)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQFrameCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQFrameCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQFrameCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFrameCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFrameCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFrameCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFrameCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQFrameCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQFrameCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQFrameCall34)(const void *, int, int *);
typedef void (*CuteQFrameCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQFrameCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQFrameCall37)(const void *, int *);
typedef void (*CuteQFrameCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQFrameCall39)(const void *, int, int *);
typedef bool (*CuteQFrameCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFrameCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFrameCall42)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFrameCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFrameCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFrameCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFrameCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFrame : public QFrame {
public:
  using QFrame::QFrame;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
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

  //  QSize QFrame::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFrameCall0 call = reinterpret_cast<CuteQFrameCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFrame::sizeHint();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QFrame::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFrameCall1 call = reinterpret_cast<CuteQFrameCall1>(taken[1]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QFrame::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QFrame::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFrameCall2 call = reinterpret_cast<CuteQFrameCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::paintEvent(a0);
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFrameCall3 call = reinterpret_cast<CuteQFrameCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFrameCall4 call = reinterpret_cast<CuteQFrameCall4>(taken[4]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFrameCall5 call = reinterpret_cast<CuteQFrameCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFrameCall6 call = reinterpret_cast<CuteQFrameCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFrameCall7 call = reinterpret_cast<CuteQFrameCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFrameCall8 call = reinterpret_cast<CuteQFrameCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFrameCall9 call = reinterpret_cast<CuteQFrameCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFrameCall10 call = reinterpret_cast<CuteQFrameCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFrameCall11 call = reinterpret_cast<CuteQFrameCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFrameCall12 call = reinterpret_cast<CuteQFrameCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFrameCall13 call = reinterpret_cast<CuteQFrameCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFrameCall14 call = reinterpret_cast<CuteQFrameCall14>(taken[14]);
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
      CuteQFrameCall15 call = reinterpret_cast<CuteQFrameCall15>(taken[15]);
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
      CuteQFrameCall16 call = reinterpret_cast<CuteQFrameCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFrameCall17 call = reinterpret_cast<CuteQFrameCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFrameCall18 call = reinterpret_cast<CuteQFrameCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFrameCall19 call = reinterpret_cast<CuteQFrameCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFrameCall20 call = reinterpret_cast<CuteQFrameCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFrameCall21 call = reinterpret_cast<CuteQFrameCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFrameCall22 call = reinterpret_cast<CuteQFrameCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFrameCall23 call = reinterpret_cast<CuteQFrameCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFrameCall24 call = reinterpret_cast<CuteQFrameCall24>(taken[24]);
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
      CuteQFrameCall25 call = reinterpret_cast<CuteQFrameCall25>(taken[25]);
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
      CuteQFrameCall26 call = reinterpret_cast<CuteQFrameCall26>(taken[26]);
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
      CuteQFrameCall27 call = reinterpret_cast<CuteQFrameCall27>(taken[27]);
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
      CuteQFrameCall28 call = reinterpret_cast<CuteQFrameCall28>(taken[28]);
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
      CuteQFrameCall29 call = reinterpret_cast<CuteQFrameCall29>(taken[29]);
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
      CuteQFrameCall30 call = reinterpret_cast<CuteQFrameCall30>(taken[30]);
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
      CuteQFrameCall31 call = reinterpret_cast<CuteQFrameCall31>(taken[31]);
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
      CuteQFrameCall32 call = reinterpret_cast<CuteQFrameCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQFrameCall33 call = reinterpret_cast<CuteQFrameCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQFrameCall34 call = reinterpret_cast<CuteQFrameCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQFrameCall35 call = reinterpret_cast<CuteQFrameCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQFrameCall36 call = reinterpret_cast<CuteQFrameCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQFrameCall37 call = reinterpret_cast<CuteQFrameCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQFrameCall38 call = reinterpret_cast<CuteQFrameCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFrameCall39 call = reinterpret_cast<CuteQFrameCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQFrameCall40 call = reinterpret_cast<CuteQFrameCall40>(taken[40]);
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
      CuteQFrameCall41 call = reinterpret_cast<CuteQFrameCall41>(taken[41]);
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
      CuteQFrameCall42 call = reinterpret_cast<CuteQFrameCall42>(taken[42]);
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
      CuteQFrameCall43 call = reinterpret_cast<CuteQFrameCall43>(taken[43]);
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
      CuteQFrameCall44 call = reinterpret_cast<CuteQFrameCall44>(taken[44]);
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
      CuteQFrameCall45 call = reinterpret_cast<CuteQFrameCall45>(taken[45]);
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
      CuteQFrameCall46 call = reinterpret_cast<CuteQFrameCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QFrame10metaObjectEv(const QFrame *self) {
  return self->metaObject();
}

//  QString QFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QFrame2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QFrame::tr(s, c, n));
}

//  QFrame::QFrame(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QFrame *ritual_ZN6QFrameC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQFrame(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QFrame::~QFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrameD1Ev(QFrame *self) {
  delete self;
}

//  int QFrame::frameStyle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame10frameStyleEv(const QFrame *self) {
  return self->frameStyle();
}

//  void QFrame::setFrameStyle(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame13setFrameStyleEi(QFrame *self, int a0) {
  self->setFrameStyle(a0);
}

//  int QFrame::frameWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame10frameWidthEv(const QFrame *self) {
  return self->frameWidth();
}

//  QSize QFrame::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QFrame8sizeHintEv(const QFrame *self) {
  return new QSize(self->sizeHint());
}

//  Shape QFrame::frameShape() const
extern "C" Q_DECL_EXPORT
QFrame::Shape ritual_ZNK6QFrame10frameShapeEv(const QFrame *self) {
  return self->frameShape();
}

//  void QFrame::setFrameShape(Shape a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame13setFrameShapeENS_5ShapeE(
    QFrame *self,
    QFrame::Shape a0) {
  self->setFrameShape(a0);
}

//  Shadow QFrame::frameShadow() const
extern "C" Q_DECL_EXPORT
QFrame::Shadow ritual_ZNK6QFrame11frameShadowEv(const QFrame *self) {
  return self->frameShadow();
}

//  void QFrame::setFrameShadow(Shadow a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame14setFrameShadowENS_6ShadowE(
    QFrame *self,
    QFrame::Shadow a0) {
  self->setFrameShadow(a0);
}

//  int QFrame::lineWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame9lineWidthEv(const QFrame *self) {
  return self->lineWidth();
}

//  void QFrame::setLineWidth(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame12setLineWidthEi(QFrame *self, int a0) {
  self->setLineWidth(a0);
}

//  int QFrame::midLineWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame12midLineWidthEv(const QFrame *self) {
  return self->midLineWidth();
}

//  void QFrame::setMidLineWidth(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame15setMidLineWidthEi(QFrame *self, int a0) {
  self->setMidLineWidth(a0);
}

//  QRect QFrame::frameRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QFrame9frameRectEv(const QFrame *self) {
  return new QRect(self->frameRect());
}

//  void QFrame::setFrameRect(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame12setFrameRectERK5QRect(QFrame *self, const QRect *a0) {
  self->setFrameRect(*a0);
}

//  bool QFrame::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QFrame5eventEP6QEvent(QFrame *self, QEvent *e) {
  return self->event(e);
}

//  void QFrame::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame10paintEventEP11QPaintEvent(
    QFrame *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QFrame::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame11changeEventEP6QEvent(QFrame *self, QEvent *a0) {
  self->changeEvent(a0);
}

//  void QFrame::drawFrame(QPainter *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame9drawFrameEP8QPainter(QFrame *self, QPainter *a0) {
  self->drawFrame(a0);
}

//  void QFrame::initStyleOption(QStyleOptionFrame *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame(
    const QFrame *self,
    QStyleOptionFrame *option) {
  self->initStyleOption(option);
}

//  QFramePrivate *QFrame::d_func()
extern "C" Q_DECL_EXPORT
QFramePrivate *ritual_ZN6QFrame6d_funcEv(QFrame *self) {
  return self->d_func();
}

//  const QFramePrivate *QFrame::d_func() const
extern "C" Q_DECL_EXPORT
const QFramePrivate *ritual_ZNK6QFrame6d_funcEv(const QFrame *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQFrame, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFrame(QFrame *self, const char *key, void *call) {
  return static_cast<CuteQFrame *>(self)->take(key, call);
}

//  QSize QFrame::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK6QFrame8sizeHintEv(const QFrame *self) {
  return new QSize(self->QFrame::sizeHint());
}

//  bool QFrame::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QFrame5eventEP6QEvent(QFrame *self, QEvent *e) {
  return static_cast<OwnQFrame *>(self)->OwnQFrame::event(e);
}

//  void QFrame::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QFrame10paintEventEP11QPaintEvent(
    QFrame *self,
    QPaintEvent *a0) {
  static_cast<OwnQFrame *>(self)->OwnQFrame::paintEvent(a0);
}

//  void QFrame::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QFrame11changeEventEP6QEvent(QFrame *self, QEvent *a0) {
  static_cast<OwnQFrame *>(self)->OwnQFrame::changeEvent(a0);
}

//  void QFrame::initStyleOption(QStyleOptionFrame *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame(
    const QFrame *self,
    QStyleOptionFrame *option) {
  static_cast<const OwnQFrame *>(self)->OwnQFrame::initStyleOption(option);
}
