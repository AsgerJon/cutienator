//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qscrollbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(scrollbar)
#include <QtWidgets/qscrollbar.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QScrollBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQScrollBar : QScrollBar {
  using QScrollBar::wheelEvent;
  using QScrollBar::paintEvent;
  using QScrollBar::mousePressEvent;
  using QScrollBar::mouseReleaseEvent;
  using QScrollBar::mouseMoveEvent;
  using QScrollBar::hideEvent;
  using QScrollBar::contextMenuEvent;
  using QScrollBar::initStyleOption;
};

//  A QScrollBar that Python can take functions over in. Every QScrollBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(scrollbar)
typedef const QSize * (*CuteQScrollBarCall0)(const void *, int *);
#endif  // QT_CONFIG(scrollbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollbar)
typedef bool (*CuteQScrollBarCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall2)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall3)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall6)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall7)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall8)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollbar)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollbar)
typedef void (*CuteQScrollBarCall9)(const void *, QStyleOptionSlider *, int *);
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(abstractslider)
typedef void (*CuteQScrollBarCall10)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(abstractslider)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractslider)
typedef void (*CuteQScrollBarCall11)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(abstractslider)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractslider)
typedef void (*CuteQScrollBarCall12)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(abstractslider)
typedef int (*CuteQScrollBarCall13)(const void *, int *);
typedef void (*CuteQScrollBarCall14)(const void *, bool, int *);
typedef const QSize * (*CuteQScrollBarCall15)(const void *, int *);
typedef int (*CuteQScrollBarCall16)(const void *, int, int *);
typedef bool (*CuteQScrollBarCall17)(const void *, int *);
typedef void * (*CuteQScrollBarCall18)(const void *, int *);
typedef void (*CuteQScrollBarCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQScrollBarCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQScrollBarCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQScrollBarCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQScrollBarCall23)(const void *, QEnterEvent *, int *);
typedef void (*CuteQScrollBarCall24)(const void *, QEvent *, int *);
typedef void (*CuteQScrollBarCall25)(const void *, QMoveEvent *, int *);
typedef void (*CuteQScrollBarCall26)(const void *, QResizeEvent *, int *);
typedef void (*CuteQScrollBarCall27)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQScrollBarCall28)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQScrollBarCall29)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQScrollBarCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQScrollBarCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQScrollBarCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQScrollBarCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQScrollBarCall34)(const void *, QShowEvent *, int *);
typedef int (*CuteQScrollBarCall35)(const void *, int, int *);
typedef void (*CuteQScrollBarCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQScrollBarCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQScrollBarCall38)(const void *, int *);
typedef void (*CuteQScrollBarCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQScrollBarCall40)(const void *, int, int *);
typedef bool (*CuteQScrollBarCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScrollBarCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollBarCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollBarCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollBarCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollBarCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScrollBar : public QScrollBar {
public:
  using QScrollBar::QScrollBar;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZNK10QScrollBar15initStyleOptionEP18QStyleOptionSlider")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

#if QT_CONFIG(scrollbar)
  //  QSize QScrollBar::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScrollBarCall0 call = reinterpret_cast<CuteQScrollBarCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QScrollBar::sizeHint();
  }
#endif  // QT_CONFIG(scrollbar)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollbar)
  //  bool QScrollBar::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScrollBarCall1 call = reinterpret_cast<CuteQScrollBarCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QScrollBar::event(event);
  }
#endif  // QT_CONFIG(scrollbar)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollbar)
  //  void QScrollBar::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQScrollBarCall2 call = reinterpret_cast<CuteQScrollBarCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollBar::wheelEvent(a0);
  }
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(scrollbar)
  //  void QScrollBar::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScrollBarCall3 call = reinterpret_cast<CuteQScrollBarCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollBar::paintEvent(a0);
  }
#endif  // QT_CONFIG(scrollbar)

#if QT_CONFIG(scrollbar)
  //  void QScrollBar::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScrollBarCall4 call = reinterpret_cast<CuteQScrollBarCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollBar::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(scrollbar)

#if QT_CONFIG(scrollbar)
  //  void QScrollBar::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScrollBarCall5 call = reinterpret_cast<CuteQScrollBarCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollBar::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(scrollbar)

#if QT_CONFIG(scrollbar)
  //  void QScrollBar::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQScrollBarCall6 call = reinterpret_cast<CuteQScrollBarCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollBar::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(scrollbar)

#if QT_CONFIG(scrollbar)
  //  void QScrollBar::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQScrollBarCall7 call = reinterpret_cast<CuteQScrollBarCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollBar::hideEvent(a0);
  }
#endif  // QT_CONFIG(scrollbar)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollbar)
  //  void QScrollBar::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScrollBarCall8 call = reinterpret_cast<CuteQScrollBarCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollBar::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollbar)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(scrollbar)
  //  void QScrollBar::initStyleOption(QStyleOptionSlider *option) const
  void initStyleOption(QStyleOptionSlider *option) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQScrollBarCall9 call = reinterpret_cast<CuteQScrollBarCall9>(taken[9]);
      call(this, option, &handled);
      if (handled) return;
    }
    QScrollBar::initStyleOption(option);
  }
#endif  // QT_CONFIG(scrollbar)

#if QT_CONFIG(abstractslider)
  //  void QAbstractSlider::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[10]) {
      int handled = 0;
      CuteQScrollBarCall10 call = reinterpret_cast<CuteQScrollBarCall10>(taken[10]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QAbstractSlider::keyPressEvent(ev);
  }
#endif  // QT_CONFIG(abstractslider)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractslider)
  //  void QAbstractSlider::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQScrollBarCall11 call = reinterpret_cast<CuteQScrollBarCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractSlider::timerEvent(a0);
  }
#endif  // QT_CONFIG(abstractslider)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(abstractslider)
  //  void QAbstractSlider::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQScrollBarCall12 call = reinterpret_cast<CuteQScrollBarCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractSlider::changeEvent(e);
  }
#endif  // QT_CONFIG(abstractslider)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQScrollBarCall13 call = reinterpret_cast<CuteQScrollBarCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQScrollBarCall14 call = reinterpret_cast<CuteQScrollBarCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQScrollBarCall15 call = reinterpret_cast<CuteQScrollBarCall15>(taken[15]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQScrollBarCall16 call = reinterpret_cast<CuteQScrollBarCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQScrollBarCall17 call = reinterpret_cast<CuteQScrollBarCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQScrollBarCall18 call = reinterpret_cast<CuteQScrollBarCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQScrollBarCall19 call = reinterpret_cast<CuteQScrollBarCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQScrollBarCall20 call = reinterpret_cast<CuteQScrollBarCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQScrollBarCall21 call = reinterpret_cast<CuteQScrollBarCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQScrollBarCall22 call = reinterpret_cast<CuteQScrollBarCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQScrollBarCall23 call = reinterpret_cast<CuteQScrollBarCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQScrollBarCall24 call = reinterpret_cast<CuteQScrollBarCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQScrollBarCall25 call = reinterpret_cast<CuteQScrollBarCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQScrollBarCall26 call = reinterpret_cast<CuteQScrollBarCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQScrollBarCall27 call = reinterpret_cast<CuteQScrollBarCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQScrollBarCall28 call = reinterpret_cast<CuteQScrollBarCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQScrollBarCall29 call = reinterpret_cast<CuteQScrollBarCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQScrollBarCall30 call = reinterpret_cast<CuteQScrollBarCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQScrollBarCall31 call = reinterpret_cast<CuteQScrollBarCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQScrollBarCall32 call = reinterpret_cast<CuteQScrollBarCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQScrollBarCall33 call = reinterpret_cast<CuteQScrollBarCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQScrollBarCall34 call = reinterpret_cast<CuteQScrollBarCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQScrollBarCall35 call = reinterpret_cast<CuteQScrollBarCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQScrollBarCall36 call = reinterpret_cast<CuteQScrollBarCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQScrollBarCall37 call = reinterpret_cast<CuteQScrollBarCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQScrollBarCall38 call = reinterpret_cast<CuteQScrollBarCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQScrollBarCall39 call = reinterpret_cast<CuteQScrollBarCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQScrollBarCall40 call = reinterpret_cast<CuteQScrollBarCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQScrollBarCall41 call = reinterpret_cast<CuteQScrollBarCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQScrollBarCall42 call = reinterpret_cast<CuteQScrollBarCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQScrollBarCall43 call = reinterpret_cast<CuteQScrollBarCall43>(taken[43]);
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
      CuteQScrollBarCall44 call = reinterpret_cast<CuteQScrollBarCall44>(taken[44]);
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
      CuteQScrollBarCall45 call = reinterpret_cast<CuteQScrollBarCall45>(taken[45]);
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
      CuteQScrollBarCall46 call = reinterpret_cast<CuteQScrollBarCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScrollBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QScrollBar10metaObjectEv(
    const QScrollBar *self) {
  return self->metaObject();
}

//  QString QScrollBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QScrollBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScrollBar::tr(s, c, n));
}

//  QScrollBar::QScrollBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZN10QScrollBarC1EP7QWidget(QWidget *parent) {
  return new CuteQScrollBar(parent);
}

//  QScrollBar::QScrollBar(Qt::Orientation a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZN10QScrollBarC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation a0,
    QWidget *parent) {
  return new CuteQScrollBar(a0, parent);
}

//  QScrollBar::~QScrollBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBarD1Ev(QScrollBar *self) {
  delete self;
}

//  QSize QScrollBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QScrollBar8sizeHintEv(const QScrollBar *self) {
  return new QSize(self->sizeHint());
}

//  bool QScrollBar::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QScrollBar5eventEP6QEvent(QScrollBar *self, QEvent *event) {
  return self->event(event);
}

#if !defined(QT_NO_CONTEXTMENU)
//  QMenu *QScrollBar::createStandardContextMenu(QPoint position)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN10QScrollBar25createStandardContextMenuE6QPoint(
    QScrollBar *self,
    const QPoint *position) {
  return self->createStandardContextMenu(*position);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(wheelevent)
//  void QScrollBar::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar10wheelEventEP11QWheelEvent(
    QScrollBar *self,
    QWheelEvent *a0) {
  self->wheelEvent(a0);
}
#endif  // QT_CONFIG(wheelevent)

//  void QScrollBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar10paintEventEP11QPaintEvent(
    QScrollBar *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QScrollBar::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar15mousePressEventEP11QMouseEvent(
    QScrollBar *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QScrollBar::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar17mouseReleaseEventEP11QMouseEvent(
    QScrollBar *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QScrollBar::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar14mouseMoveEventEP11QMouseEvent(
    QScrollBar *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QScrollBar::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar9hideEventEP10QHideEvent(
    QScrollBar *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QScrollBar::sliderChange(SliderChange change)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar12sliderChangeEN15QAbstractSlider12SliderChangeE(
    QScrollBar *self,
    QAbstractSlider::SliderChange change) {
  self->sliderChange(change);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QScrollBar::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBar16contextMenuEventEP17QContextMenuEvent(
    QScrollBar *self,
    QContextMenuEvent *a0) {
  self->contextMenuEvent(a0);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  void QScrollBar::initStyleOption(QStyleOptionSlider *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QScrollBar15initStyleOptionEP18QStyleOptionSlider(
    const QScrollBar *self,
    QStyleOptionSlider *option) {
  self->initStyleOption(option);
}

//  QScrollBarPrivate *QScrollBar::d_func()
extern "C" Q_DECL_EXPORT
QScrollBarPrivate *ritual_ZN10QScrollBar6d_funcEv(QScrollBar *self) {
  return self->d_func();
}

//  const QScrollBarPrivate *QScrollBar::d_func() const
extern "C" Q_DECL_EXPORT
const QScrollBarPrivate *ritual_ZNK10QScrollBar6d_funcEv(
    const QScrollBar *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQScrollBar, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScrollBar(QScrollBar *self, const char *key, void *call) {
  return static_cast<CuteQScrollBar *>(self)->take(key, call);
}

//  QSize QScrollBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QScrollBar8sizeHintEv(const QScrollBar *self) {
  return new QSize(self->QScrollBar::sizeHint());
}

//  bool QScrollBar::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QScrollBar5eventEP6QEvent(
    QScrollBar *self,
    QEvent *event) {
  return self->QScrollBar::event(event);
}

#if QT_CONFIG(wheelevent)
//  void QScrollBar::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QScrollBar10wheelEventEP11QWheelEvent(
    QScrollBar *self,
    QWheelEvent *a0) {
  static_cast<OwnQScrollBar *>(self)->OwnQScrollBar::wheelEvent(a0);
}
#endif  // QT_CONFIG(wheelevent)

//  void QScrollBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QScrollBar10paintEventEP11QPaintEvent(
    QScrollBar *self,
    QPaintEvent *a0) {
  static_cast<OwnQScrollBar *>(self)->OwnQScrollBar::paintEvent(a0);
}

//  void QScrollBar::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QScrollBar15mousePressEventEP11QMouseEvent(
    QScrollBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQScrollBar *>(self)->OwnQScrollBar::mousePressEvent(a0);
}

//  void QScrollBar::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QScrollBar17mouseReleaseEventEP11QMouseEvent(
    QScrollBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQScrollBar *>(self)->OwnQScrollBar::mouseReleaseEvent(a0);
}

//  void QScrollBar::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QScrollBar14mouseMoveEventEP11QMouseEvent(
    QScrollBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQScrollBar *>(self)->OwnQScrollBar::mouseMoveEvent(a0);
}

//  void QScrollBar::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QScrollBar9hideEventEP10QHideEvent(
    QScrollBar *self,
    QHideEvent *a0) {
  static_cast<OwnQScrollBar *>(self)->OwnQScrollBar::hideEvent(a0);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QScrollBar::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QScrollBar16contextMenuEventEP17QContextMenuEvent(
    QScrollBar *self,
    QContextMenuEvent *a0) {
  static_cast<OwnQScrollBar *>(self)->OwnQScrollBar::contextMenuEvent(a0);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  void QScrollBar::initStyleOption(QStyleOptionSlider *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10QScrollBar15initStyleOptionEP18QStyleOptionSlider(
    const QScrollBar *self,
    QStyleOptionSlider *option) {
  static_cast<const OwnQScrollBar *>(self)->OwnQScrollBar::initStyleOption(
      option);
}

#endif  // QT_CONFIG(scrollbar)
