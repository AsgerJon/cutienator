//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qslider.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(slider)
#include <QtWidgets/qslider.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSlider may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSlider : QSlider {
  using QSlider::paintEvent;
  using QSlider::mousePressEvent;
  using QSlider::mouseReleaseEvent;
  using QSlider::mouseMoveEvent;
  using QSlider::initStyleOption;
};

//  A QSlider that Python can take functions over in. Every QSlider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(slider)
typedef const QSize * (*CuteQSliderCall0)(const void *, int *);
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
typedef const QSize * (*CuteQSliderCall1)(const void *, int *);
#endif  // QT_CONFIG(slider)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(slider)
typedef bool (*CuteQSliderCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(slider)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(slider)
typedef void (*CuteQSliderCall3)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
typedef void (*CuteQSliderCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
typedef void (*CuteQSliderCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
typedef void (*CuteQSliderCall6)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
typedef void (*CuteQSliderCall7)(const void *, QStyleOptionSlider *, int *);
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(abstractslider)
typedef void (*CuteQSliderCall8)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(abstractslider)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractslider)
typedef void (*CuteQSliderCall9)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(abstractslider)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(abstractslider)
typedef void (*CuteQSliderCall10)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(abstractslider)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(abstractslider)
typedef void (*CuteQSliderCall11)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(abstractslider)
typedef int (*CuteQSliderCall12)(const void *, int *);
typedef void (*CuteQSliderCall13)(const void *, bool, int *);
typedef int (*CuteQSliderCall14)(const void *, int, int *);
typedef bool (*CuteQSliderCall15)(const void *, int *);
typedef void * (*CuteQSliderCall16)(const void *, int *);
typedef void (*CuteQSliderCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSliderCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSliderCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSliderCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSliderCall21)(const void *, QEnterEvent *, int *);
typedef void (*CuteQSliderCall22)(const void *, QEvent *, int *);
typedef void (*CuteQSliderCall23)(const void *, QMoveEvent *, int *);
typedef void (*CuteQSliderCall24)(const void *, QResizeEvent *, int *);
typedef void (*CuteQSliderCall25)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQSliderCall26)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQSliderCall27)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQSliderCall28)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSliderCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSliderCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSliderCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSliderCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQSliderCall33)(const void *, QShowEvent *, int *);
typedef void (*CuteQSliderCall34)(const void *, QHideEvent *, int *);
typedef int (*CuteQSliderCall35)(const void *, int, int *);
typedef void (*CuteQSliderCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQSliderCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQSliderCall38)(const void *, int *);
typedef void (*CuteQSliderCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQSliderCall40)(const void *, int, int *);
typedef bool (*CuteQSliderCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSliderCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSliderCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSliderCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSliderCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSliderCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSlider : public QSlider {
public:
  using QSlider::QSlider;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK7QSlider15initStyleOptionEP18QStyleOptionSlider")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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

#if QT_CONFIG(slider)
  //  QSize QSlider::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSliderCall0 call = reinterpret_cast<CuteQSliderCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSlider::sizeHint();
  }
#endif  // QT_CONFIG(slider)

#if QT_CONFIG(slider)
  //  QSize QSlider::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSliderCall1 call = reinterpret_cast<CuteQSliderCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSlider::minimumSizeHint();
  }
#endif  // QT_CONFIG(slider)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(slider)
  //  bool QSlider::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSliderCall2 call = reinterpret_cast<CuteQSliderCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSlider::event(event);
  }
#endif  // QT_CONFIG(slider)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(slider)
  //  void QSlider::paintEvent(QPaintEvent *ev)
  void paintEvent(QPaintEvent *ev) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSliderCall3 call = reinterpret_cast<CuteQSliderCall3>(taken[3]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QSlider::paintEvent(ev);
  }
#endif  // QT_CONFIG(slider)

#if QT_CONFIG(slider)
  //  void QSlider::mousePressEvent(QMouseEvent *ev)
  void mousePressEvent(QMouseEvent *ev) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSliderCall4 call = reinterpret_cast<CuteQSliderCall4>(taken[4]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QSlider::mousePressEvent(ev);
  }
#endif  // QT_CONFIG(slider)

#if QT_CONFIG(slider)
  //  void QSlider::mouseReleaseEvent(QMouseEvent *ev)
  void mouseReleaseEvent(QMouseEvent *ev) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSliderCall5 call = reinterpret_cast<CuteQSliderCall5>(taken[5]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QSlider::mouseReleaseEvent(ev);
  }
#endif  // QT_CONFIG(slider)

#if QT_CONFIG(slider)
  //  void QSlider::mouseMoveEvent(QMouseEvent *ev)
  void mouseMoveEvent(QMouseEvent *ev) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSliderCall6 call = reinterpret_cast<CuteQSliderCall6>(taken[6]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QSlider::mouseMoveEvent(ev);
  }
#endif  // QT_CONFIG(slider)

#if QT_CONFIG(slider)
  //  void QSlider::initStyleOption(QStyleOptionSlider *option) const
  void initStyleOption(QStyleOptionSlider *option) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSliderCall7 call = reinterpret_cast<CuteQSliderCall7>(taken[7]);
      call(this, option, &handled);
      if (handled) return;
    }
    QSlider::initStyleOption(option);
  }
#endif  // QT_CONFIG(slider)

#if QT_CONFIG(abstractslider)
  //  void QAbstractSlider::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSliderCall8 call = reinterpret_cast<CuteQSliderCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQSliderCall9 call = reinterpret_cast<CuteQSliderCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractSlider::timerEvent(a0);
  }
#endif  // QT_CONFIG(abstractslider)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(abstractslider)
  //  void QAbstractSlider::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSliderCall10 call = reinterpret_cast<CuteQSliderCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractSlider::wheelEvent(e);
  }
#endif  // QT_CONFIG(abstractslider)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(abstractslider)
  //  void QAbstractSlider::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSliderCall11 call = reinterpret_cast<CuteQSliderCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractSlider::changeEvent(e);
  }
#endif  // QT_CONFIG(abstractslider)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSliderCall12 call = reinterpret_cast<CuteQSliderCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSliderCall13 call = reinterpret_cast<CuteQSliderCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSliderCall14 call = reinterpret_cast<CuteQSliderCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSliderCall15 call = reinterpret_cast<CuteQSliderCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSliderCall16 call = reinterpret_cast<CuteQSliderCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSliderCall17 call = reinterpret_cast<CuteQSliderCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSliderCall18 call = reinterpret_cast<CuteQSliderCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSliderCall19 call = reinterpret_cast<CuteQSliderCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSliderCall20 call = reinterpret_cast<CuteQSliderCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSliderCall21 call = reinterpret_cast<CuteQSliderCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSliderCall22 call = reinterpret_cast<CuteQSliderCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSliderCall23 call = reinterpret_cast<CuteQSliderCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSliderCall24 call = reinterpret_cast<CuteQSliderCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSliderCall25 call = reinterpret_cast<CuteQSliderCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSliderCall26 call = reinterpret_cast<CuteQSliderCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSliderCall27 call = reinterpret_cast<CuteQSliderCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSliderCall28 call = reinterpret_cast<CuteQSliderCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSliderCall29 call = reinterpret_cast<CuteQSliderCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSliderCall30 call = reinterpret_cast<CuteQSliderCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSliderCall31 call = reinterpret_cast<CuteQSliderCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSliderCall32 call = reinterpret_cast<CuteQSliderCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSliderCall33 call = reinterpret_cast<CuteQSliderCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSliderCall34 call = reinterpret_cast<CuteQSliderCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQSliderCall35 call = reinterpret_cast<CuteQSliderCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQSliderCall36 call = reinterpret_cast<CuteQSliderCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQSliderCall37 call = reinterpret_cast<CuteQSliderCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQSliderCall38 call = reinterpret_cast<CuteQSliderCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQSliderCall39 call = reinterpret_cast<CuteQSliderCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQSliderCall40 call = reinterpret_cast<CuteQSliderCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQSliderCall41 call = reinterpret_cast<CuteQSliderCall41>(taken[41]);
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
      CuteQSliderCall42 call = reinterpret_cast<CuteQSliderCall42>(taken[42]);
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
      CuteQSliderCall43 call = reinterpret_cast<CuteQSliderCall43>(taken[43]);
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
      CuteQSliderCall44 call = reinterpret_cast<CuteQSliderCall44>(taken[44]);
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
      CuteQSliderCall45 call = reinterpret_cast<CuteQSliderCall45>(taken[45]);
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
      CuteQSliderCall46 call = reinterpret_cast<CuteQSliderCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSlider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QSlider10metaObjectEv(const QSlider *self) {
  return self->metaObject();
}

//  QString QSlider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QSlider2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QSlider::tr(s, c, n));
}

//  QSlider::QSlider(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSlider *ritual_ZN7QSliderC1EP7QWidget(QWidget *parent) {
  return new CuteQSlider(parent);
}

//  QSlider::QSlider(Qt::Orientation orientation, QWidget *parent)
extern "C" Q_DECL_EXPORT
QSlider *ritual_ZN7QSliderC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation orientation,
    QWidget *parent) {
  return new CuteQSlider(orientation, parent);
}

//  QSlider::~QSlider()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSliderD1Ev(QSlider *self) {
  delete self;
}

//  QSize QSlider::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QSlider8sizeHintEv(const QSlider *self) {
  return new QSize(self->sizeHint());
}

//  QSize QSlider::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QSlider15minimumSizeHintEv(const QSlider *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QSlider::setTickPosition(TickPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider15setTickPositionENS_12TickPositionE(
    QSlider *self,
    QSlider::TickPosition position) {
  self->setTickPosition(position);
}

//  TickPosition QSlider::tickPosition() const
extern "C" Q_DECL_EXPORT
QSlider::TickPosition ritual_ZNK7QSlider12tickPositionEv(
    const QSlider *self) {
  return self->tickPosition();
}

//  void QSlider::setTickInterval(int ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider15setTickIntervalEi(QSlider *self, int ti) {
  self->setTickInterval(ti);
}

//  int QSlider::tickInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSlider12tickIntervalEv(const QSlider *self) {
  return self->tickInterval();
}

//  bool QSlider::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QSlider5eventEP6QEvent(QSlider *self, QEvent *event) {
  return self->event(event);
}

//  void QSlider::paintEvent(QPaintEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider10paintEventEP11QPaintEvent(
    QSlider *self,
    QPaintEvent *ev) {
  self->paintEvent(ev);
}

//  void QSlider::mousePressEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider15mousePressEventEP11QMouseEvent(
    QSlider *self,
    QMouseEvent *ev) {
  self->mousePressEvent(ev);
}

//  void QSlider::mouseReleaseEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider17mouseReleaseEventEP11QMouseEvent(
    QSlider *self,
    QMouseEvent *ev) {
  self->mouseReleaseEvent(ev);
}

//  void QSlider::mouseMoveEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider14mouseMoveEventEP11QMouseEvent(
    QSlider *self,
    QMouseEvent *ev) {
  self->mouseMoveEvent(ev);
}

//  void QSlider::initStyleOption(QStyleOptionSlider *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QSlider15initStyleOptionEP18QStyleOptionSlider(
    const QSlider *self,
    QStyleOptionSlider *option) {
  self->initStyleOption(option);
}

//  a Python function taken by a CuteQSlider, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSlider(QSlider *self, const char *key, void *call) {
  return static_cast<CuteQSlider *>(self)->take(key, call);
}

//  QSize QSlider::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QSlider8sizeHintEv(const QSlider *self) {
  return new QSize(self->QSlider::sizeHint());
}

//  QSize QSlider::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QSlider15minimumSizeHintEv(const QSlider *self) {
  return new QSize(self->QSlider::minimumSizeHint());
}

//  bool QSlider::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QSlider5eventEP6QEvent(QSlider *self, QEvent *event) {
  return self->QSlider::event(event);
}

//  void QSlider::paintEvent(QPaintEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QSlider10paintEventEP11QPaintEvent(
    QSlider *self,
    QPaintEvent *ev) {
  static_cast<OwnQSlider *>(self)->OwnQSlider::paintEvent(ev);
}

//  void QSlider::mousePressEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QSlider15mousePressEventEP11QMouseEvent(
    QSlider *self,
    QMouseEvent *ev) {
  static_cast<OwnQSlider *>(self)->OwnQSlider::mousePressEvent(ev);
}

//  void QSlider::mouseReleaseEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QSlider17mouseReleaseEventEP11QMouseEvent(
    QSlider *self,
    QMouseEvent *ev) {
  static_cast<OwnQSlider *>(self)->OwnQSlider::mouseReleaseEvent(ev);
}

//  void QSlider::mouseMoveEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QSlider14mouseMoveEventEP11QMouseEvent(
    QSlider *self,
    QMouseEvent *ev) {
  static_cast<OwnQSlider *>(self)->OwnQSlider::mouseMoveEvent(ev);
}

//  void QSlider::initStyleOption(QStyleOptionSlider *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK7QSlider15initStyleOptionEP18QStyleOptionSlider(
    const QSlider *self,
    QStyleOptionSlider *option) {
  static_cast<const OwnQSlider *>(self)->OwnQSlider::initStyleOption(option);
}

#endif  // QT_CONFIG(slider)
