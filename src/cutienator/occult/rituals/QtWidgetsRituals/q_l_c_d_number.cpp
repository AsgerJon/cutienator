//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlcdnumber.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(lcdnumber)
#include <QtWidgets/qlcdnumber.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLCDNumber may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLCDNumber : QLCDNumber {
  using QLCDNumber::event;
  using QLCDNumber::paintEvent;
};

//  A QLCDNumber that Python can take functions over in. Every QLCDNumber
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(lcdnumber)
typedef const QSize * (*CuteQLCDNumberCall0)(const void *, int *);
#endif  // QT_CONFIG(lcdnumber)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lcdnumber)
typedef bool (*CuteQLCDNumberCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(lcdnumber)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lcdnumber)
typedef void (*CuteQLCDNumberCall2)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(lcdnumber)
typedef void (*CuteQLCDNumberCall3)(const void *, QEvent *, int *);
typedef void (*CuteQLCDNumberCall4)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQLCDNumberCall5)(const void *, int *);
typedef void (*CuteQLCDNumberCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQLCDNumberCall7)(const void *, int *);
typedef int (*CuteQLCDNumberCall8)(const void *, int, int *);
typedef bool (*CuteQLCDNumberCall9)(const void *, int *);
typedef void * (*CuteQLCDNumberCall10)(const void *, int *);
typedef void (*CuteQLCDNumberCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQLCDNumberCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQLCDNumberCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQLCDNumberCall14)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQLCDNumberCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQLCDNumberCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQLCDNumberCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQLCDNumberCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQLCDNumberCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQLCDNumberCall20)(const void *, QEnterEvent *, int *);
typedef void (*CuteQLCDNumberCall21)(const void *, QEvent *, int *);
typedef void (*CuteQLCDNumberCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQLCDNumberCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQLCDNumberCall24)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQLCDNumberCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQLCDNumberCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQLCDNumberCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLCDNumberCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLCDNumberCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLCDNumberCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLCDNumberCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQLCDNumberCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQLCDNumberCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQLCDNumberCall34)(const void *, int, int *);
typedef void (*CuteQLCDNumberCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQLCDNumberCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQLCDNumberCall37)(const void *, int *);
typedef void (*CuteQLCDNumberCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQLCDNumberCall39)(const void *, int, int *);
typedef bool (*CuteQLCDNumberCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLCDNumberCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLCDNumberCall42)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLCDNumberCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLCDNumberCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLCDNumberCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLCDNumberCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLCDNumber : public QLCDNumber {
public:
  using QLCDNumber::QLCDNumber;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(lcdnumber)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(lcdnumber)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lcdnumber)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(lcdnumber)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lcdnumber)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(lcdnumber)
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

#if QT_CONFIG(lcdnumber)
  //  QSize QLCDNumber::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLCDNumberCall0 call = reinterpret_cast<CuteQLCDNumberCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLCDNumber::sizeHint();
  }
#endif  // QT_CONFIG(lcdnumber)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lcdnumber)
  //  bool QLCDNumber::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLCDNumberCall1 call = reinterpret_cast<CuteQLCDNumberCall1>(taken[1]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QLCDNumber::event(e);
  }
#endif  // QT_CONFIG(lcdnumber)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(lcdnumber)
  //  void QLCDNumber::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLCDNumberCall2 call = reinterpret_cast<CuteQLCDNumberCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLCDNumber::paintEvent(a0);
  }
#endif  // QT_CONFIG(lcdnumber)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLCDNumberCall3 call = reinterpret_cast<CuteQLCDNumberCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLCDNumberCall4 call = reinterpret_cast<CuteQLCDNumberCall4>(taken[4]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLCDNumberCall5 call = reinterpret_cast<CuteQLCDNumberCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLCDNumberCall6 call = reinterpret_cast<CuteQLCDNumberCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLCDNumberCall7 call = reinterpret_cast<CuteQLCDNumberCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLCDNumberCall8 call = reinterpret_cast<CuteQLCDNumberCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLCDNumberCall9 call = reinterpret_cast<CuteQLCDNumberCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQLCDNumberCall10 call = reinterpret_cast<CuteQLCDNumberCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLCDNumberCall11 call = reinterpret_cast<CuteQLCDNumberCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQLCDNumberCall12 call = reinterpret_cast<CuteQLCDNumberCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLCDNumberCall13 call = reinterpret_cast<CuteQLCDNumberCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLCDNumberCall14 call = reinterpret_cast<CuteQLCDNumberCall14>(taken[14]);
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
      CuteQLCDNumberCall15 call = reinterpret_cast<CuteQLCDNumberCall15>(taken[15]);
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
      CuteQLCDNumberCall16 call = reinterpret_cast<CuteQLCDNumberCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLCDNumberCall17 call = reinterpret_cast<CuteQLCDNumberCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLCDNumberCall18 call = reinterpret_cast<CuteQLCDNumberCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLCDNumberCall19 call = reinterpret_cast<CuteQLCDNumberCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLCDNumberCall20 call = reinterpret_cast<CuteQLCDNumberCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLCDNumberCall21 call = reinterpret_cast<CuteQLCDNumberCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQLCDNumberCall22 call = reinterpret_cast<CuteQLCDNumberCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQLCDNumberCall23 call = reinterpret_cast<CuteQLCDNumberCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQLCDNumberCall24 call = reinterpret_cast<CuteQLCDNumberCall24>(taken[24]);
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
      CuteQLCDNumberCall25 call = reinterpret_cast<CuteQLCDNumberCall25>(taken[25]);
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
      CuteQLCDNumberCall26 call = reinterpret_cast<CuteQLCDNumberCall26>(taken[26]);
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
      CuteQLCDNumberCall27 call = reinterpret_cast<CuteQLCDNumberCall27>(taken[27]);
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
      CuteQLCDNumberCall28 call = reinterpret_cast<CuteQLCDNumberCall28>(taken[28]);
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
      CuteQLCDNumberCall29 call = reinterpret_cast<CuteQLCDNumberCall29>(taken[29]);
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
      CuteQLCDNumberCall30 call = reinterpret_cast<CuteQLCDNumberCall30>(taken[30]);
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
      CuteQLCDNumberCall31 call = reinterpret_cast<CuteQLCDNumberCall31>(taken[31]);
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
      CuteQLCDNumberCall32 call = reinterpret_cast<CuteQLCDNumberCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQLCDNumberCall33 call = reinterpret_cast<CuteQLCDNumberCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQLCDNumberCall34 call = reinterpret_cast<CuteQLCDNumberCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQLCDNumberCall35 call = reinterpret_cast<CuteQLCDNumberCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQLCDNumberCall36 call = reinterpret_cast<CuteQLCDNumberCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQLCDNumberCall37 call = reinterpret_cast<CuteQLCDNumberCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQLCDNumberCall38 call = reinterpret_cast<CuteQLCDNumberCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQLCDNumberCall39 call = reinterpret_cast<CuteQLCDNumberCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQLCDNumberCall40 call = reinterpret_cast<CuteQLCDNumberCall40>(taken[40]);
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
      CuteQLCDNumberCall41 call = reinterpret_cast<CuteQLCDNumberCall41>(taken[41]);
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
      CuteQLCDNumberCall42 call = reinterpret_cast<CuteQLCDNumberCall42>(taken[42]);
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
      CuteQLCDNumberCall43 call = reinterpret_cast<CuteQLCDNumberCall43>(taken[43]);
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
      CuteQLCDNumberCall44 call = reinterpret_cast<CuteQLCDNumberCall44>(taken[44]);
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
      CuteQLCDNumberCall45 call = reinterpret_cast<CuteQLCDNumberCall45>(taken[45]);
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
      CuteQLCDNumberCall46 call = reinterpret_cast<CuteQLCDNumberCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLCDNumber::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QLCDNumber10metaObjectEv(
    const QLCDNumber *self) {
  return self->metaObject();
}

//  QString QLCDNumber::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QLCDNumber2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLCDNumber::tr(s, c, n));
}

//  QLCDNumber::QLCDNumber(QWidget *parent)
extern "C" Q_DECL_EXPORT
QLCDNumber *ritual_ZN10QLCDNumberC1EP7QWidget(QWidget *parent) {
  return new CuteQLCDNumber(parent);
}

//  QLCDNumber::QLCDNumber(uint numDigits, QWidget *parent)
extern "C" Q_DECL_EXPORT
QLCDNumber *ritual_ZN10QLCDNumberC1EjP7QWidget(
    uint numDigits,
    QWidget *parent) {
  return new CuteQLCDNumber(numDigits, parent);
}

//  QLCDNumber::~QLCDNumber()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumberD1Ev(QLCDNumber *self) {
  delete self;
}

//  bool QLCDNumber::smallDecimalPoint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QLCDNumber17smallDecimalPointEv(const QLCDNumber *self) {
  return self->smallDecimalPoint();
}

//  int QLCDNumber::digitCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QLCDNumber10digitCountEv(const QLCDNumber *self) {
  return self->digitCount();
}

//  void QLCDNumber::setDigitCount(int nDigits)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber13setDigitCountEi(QLCDNumber *self, int nDigits) {
  self->setDigitCount(nDigits);
}

//  bool QLCDNumber::checkOverflow(double num) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QLCDNumber13checkOverflowEd(
    const QLCDNumber *self,
    double num) {
  return self->checkOverflow(num);
}

//  bool QLCDNumber::checkOverflow(int num) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QLCDNumber13checkOverflowEi(
    const QLCDNumber *self,
    int num) {
  return self->checkOverflow(num);
}

//  Mode QLCDNumber::mode() const
extern "C" Q_DECL_EXPORT
QLCDNumber::Mode ritual_ZNK10QLCDNumber4modeEv(const QLCDNumber *self) {
  return self->mode();
}

//  void QLCDNumber::setMode(Mode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7setModeENS_4ModeE(
    QLCDNumber *self,
    QLCDNumber::Mode a0) {
  self->setMode(a0);
}

//  SegmentStyle QLCDNumber::segmentStyle() const
extern "C" Q_DECL_EXPORT
QLCDNumber::SegmentStyle ritual_ZNK10QLCDNumber12segmentStyleEv(
    const QLCDNumber *self) {
  return self->segmentStyle();
}

//  void QLCDNumber::setSegmentStyle(SegmentStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber15setSegmentStyleENS_12SegmentStyleE(
    QLCDNumber *self,
    QLCDNumber::SegmentStyle a0) {
  self->setSegmentStyle(a0);
}

//  double QLCDNumber::value() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK10QLCDNumber5valueEv(const QLCDNumber *self) {
  return self->value();
}

//  int QLCDNumber::intValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QLCDNumber8intValueEv(const QLCDNumber *self) {
  return self->intValue();
}

//  QSize QLCDNumber::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QLCDNumber8sizeHintEv(const QLCDNumber *self) {
  return new QSize(self->sizeHint());
}

//  void QLCDNumber::display(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7displayERK7QString(
    QLCDNumber *self,
    const QString *str) {
  self->display(*str);
}

//  void QLCDNumber::display(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7displayEi(QLCDNumber *self, int num) {
  self->display(num);
}

//  void QLCDNumber::display(double num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7displayEd(QLCDNumber *self, double num) {
  self->display(num);
}

//  void QLCDNumber::setHexMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setHexModeEv(QLCDNumber *self) {
  self->setHexMode();
}

//  void QLCDNumber::setDecMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setDecModeEv(QLCDNumber *self) {
  self->setDecMode();
}

//  void QLCDNumber::setOctMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setOctModeEv(QLCDNumber *self) {
  self->setOctMode();
}

//  void QLCDNumber::setBinMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setBinModeEv(QLCDNumber *self) {
  self->setBinMode();
}

//  void QLCDNumber::setSmallDecimalPoint(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber20setSmallDecimalPointEb(
    QLCDNumber *self,
    bool a0) {
  self->setSmallDecimalPoint(a0);
}

//  bool QLCDNumber::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QLCDNumber5eventEP6QEvent(QLCDNumber *self, QEvent *e) {
  return self->event(e);
}

//  void QLCDNumber::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10paintEventEP11QPaintEvent(
    QLCDNumber *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  a Python function taken by a CuteQLCDNumber, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLCDNumber(QLCDNumber *self, const char *key, void *call) {
  return static_cast<CuteQLCDNumber *>(self)->take(key, call);
}

//  QSize QLCDNumber::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QLCDNumber8sizeHintEv(const QLCDNumber *self) {
  return new QSize(self->QLCDNumber::sizeHint());
}

//  bool QLCDNumber::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QLCDNumber5eventEP6QEvent(QLCDNumber *self, QEvent *e) {
  return static_cast<OwnQLCDNumber *>(self)->OwnQLCDNumber::event(e);
}

//  void QLCDNumber::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QLCDNumber10paintEventEP11QPaintEvent(
    QLCDNumber *self,
    QPaintEvent *a0) {
  static_cast<OwnQLCDNumber *>(self)->OwnQLCDNumber::paintEvent(a0);
}

#endif  // QT_CONFIG(lcdnumber)
